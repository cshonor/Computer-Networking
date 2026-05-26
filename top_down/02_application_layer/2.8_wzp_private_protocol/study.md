# 2.8 自定义应用层私有协议 —— WZP

> 承载：[TCP 长连接](../3.5_tcp_connection_and_transmission/study.md) · 对比 HTTP：[2.2 KV/Body](../2.2_http_and_web/study.md#ch2-http-kv-body) · Socket：[2.7 TCP](../2.7_socket_programming_tcp/study.md)

## 协议概览

| 项 | 说明 |
|----|------|
| **全称** | **WanZhi Protocol**（万智 / 自研私有通信协议） |
| **承载** | **TCP** 可靠传输 |
| **默认端口** | **9988** |
| **定位** | 轻量私有 IM：登录、聊天、状态、简易文件；对标**简化版即时通信协议** |

---

## 一、整体报文格式（二进制固定头）

```text
+-------------+--------+-------------+
| 4 字节长度   | 1 字节  | 可变载荷体   |
| Len (BE)    | Cmd    | Body        |
+-------------+--------+-------------+
```

| 字段 | 宽度 | 说明 |
|------|------|------|
| **Len** | **4 B，大端** | **Cmd + Body** 的字节总数（**不含**这 4 字节本身）；用于 TCP **粘包/拆包** |
| **Cmd** | **1 B** | 指令码，区分业务 |
| **Body** | 可变 | 业务数据；内部 **WZP 专属 KV**（UTF-8 字符串） |

**组包顺序**：先拼 `Cmd + Body` → 算长度写 **4 字节 Len** → 再发 TCP。

**易错**：Len 是 **Cmd+Body 长度**，不是「整包含 4 字节头」的长度（与下方伪代码一致）。

---

## 二、全局指令码表

| 十进制 | 十六进制 | 名称 | 用途 |
|--------|----------|------|------|
| 1 | 0x01 | **WZP_LOGIN_REQ** | 客户端登录请求 |
| 2 | 0x02 | **WZP_LOGIN_ACK** | 服务端登录响应 |
| 3 | 0x03 | **WZP_CHAT_MSG** | 单聊消息 |
| 4 | 0x04 | **WZP_ONLINE_STATE** | 上下线状态 |
| 5 | 0x05 | **WZP_FILE_TRANS** | 简易文件分片 |
| 6 | 0x06 | **WZP_LOGOUT** | 客户端下线 |

---

## 三、载荷体 KV 规则（≠ HTTP）

**完全脱离 HTTP `Key: Value` 冒号规则**，WZP 自研语法：

| 符号 | 含义 |
|------|------|
| **`=`** | 键值分隔 |
| **`|`** | 多组参数分隔 |
| 编码 | **UTF-8** 字符串 |

通用格式：

```text
key1=value1|key2=value2|key3=value3
```

示例：

```text
uid=1001|uname=张三|pwd=123456
from=1001|to=1002|msg=晚上一起学网络
```

---

## 四、六大场景完整报文实例

### 1）登录请求 `WZP_LOGIN_REQ` (0x01)

```text
Body: uid=10086|username=WZP用户|pass=abc123
```

### 2）登录响应 `WZP_LOGIN_ACK` (0x02)

成功：

```text
code=200|result=登录成功|token=wzp666888
```

失败：

```text
code=500|result=账号密码错误
```

### 3）聊天 `WZP_CHAT_MSG` (0x03)

```text
sender=001|receiver=002|content=今天弄懂私有协议啦
```

### 4）上线状态 `WZP_ONLINE_STATE` (0x04)

```text
userid=003|status=online|nick=小网工
```

### 5）下线 `WZP_LOGOUT` (0x06)

```text
userid=001|tip=正常退出登录
```

### 6）文件分片 `WZP_FILE_TRANS` (0x05)

```text
filename=test.txt|filesize=2048|chunk=1|data=文件二进制内容
```

---

## 五、通信交互流程

1. 客户端 **TCP 连接** 服务端 **9988**，**长连接**  
2. 按 **Len + Cmd + Body** 组包发**登录包**  
3. 服务端 **先读 4 字节 Len**，再收满 **Cmd+Body**  
4. 读 **1 字节 Cmd**，按指令分支  
5. Body 按 **`|`**、**`=`** 解析 KV  
6. 业务处理后用**相同 WZP 格式**回包  
7. 聊天、状态推送**全程复用**此格式  
8. 客户端发 **0x06 下线** → 关闭 TCP  

---

## 六、与标准协议对比

| 对比 | HTTP | WZP |
|------|------|-----|
| 报文 | **文本**：请求行 + `Key: Value` + 空行 + Body | **二进制固定头** + 私有 KV |
| 连接 | 常短连接、一问一答 | **TCP 长连接**、实时推送 |
| 分隔 | 冒号+空格、`\r\n\r\n` | **`=`** 与 **`|`** |

| 对比 | SMTP | WZP |
|------|------|-----|
| 字段 | 固定邮件头 | **完全自定义** KV |

| 对比 | 微信/QQ 等 IM | WZP |
|------|---------------|-----|
| 性质 | 厂商**私有协议** | 教学用**同类设计思想**（自定义语法 + TCP） |

---

## 七、组包 / 解包核心逻辑

→ 可运行示例：[demo_code/wzp_codec.py](./demo_code/wzp_codec.py)

```python
# 组包：Len(4B BE) + Cmd(1B) + Body(UTF-8)
def wzp_pack(cmd, body_str):
    body_bytes = bytes([cmd]) + body_str.encode("utf-8")
    len_header = len(body_bytes).to_bytes(4, byteorder="big")
    return len_header + body_bytes

# 解包：先 4 字节 Len，再收满 payload
def wzp_unpack_from_bytes(payload):
    cmd = payload[0]
    body = payload[1:].decode("utf-8")
    kv = dict(item.split("=", 1) for item in body.split("|") if "=" in item)
    return cmd, kv
```

**解包步骤**：`recv(4)` → `n = int.from_bytes(..., "big")` → `recv(n)` → 解析 Cmd + 拆分 KV。

---

## 八、可扩展方向（了解）

1. **心跳包**（防长连接被中间设备断开）  
2. Body 改 **JSON**（`Content-Type` 思路的私有版）  
3. 载荷加密字段，如 `aes_key=xxx`  
4. 群聊、广播、语音片段  

---

<a id="ch2-8-exam"></a>

## 九、考试 / 项目速记

### 5 行口诀

1. **TCP 9988 长连接**；**4B 大端 Len + 1B Cmd + Body**  
2. **Len = Cmd+Body 长度**（不含 4 字节头）→ **防粘包**  
3. **KV：`=` 分键值，`| ` 分组**；UTF-8（≠ HTTP 冒号）  
4. **0x01 登录 · 0x03 聊天 · 0x06 下线**  
5. **私有协议 = 自定语法 + 可靠传输**（思想同商用 IM）  

### 30 字版

**WZP基于TCP端口9988；四字节大端长加一字节指令加Body；KV用等号竖线；Len防粘包；私有IM语法。**

---

## 个人总结

WZP 演示了**应用层自定义协议**的典型做法：在 TCP 字节流上用**长度前缀**定界，用**指令码**分业务，用**私有 KV** 带参数；与 HTTP 文本首部、SMTP 固定头形成对照。
