# 3.2 报文的组成部分

> 本章：[chapter-summary.md](./chapter-summary.md#ch03-2) · [3.3 方法](./03-method.md) · [Wireshark HTTP](../../../wireshark-packet-analysis/chapter-09-application-layer-proto/03-http-protocol.md)

## 本节核心目标

掌握 HTTP 报文**三段式结构**：起始行、首部、可选实体主体；区分请求报文与响应报文。

---

<a id="ch03-2-structure"></a>

## 一、两类报文

| 类型 | 作用 |
|------|------|
| **请求报文（request）** | 向 Web 服务器**请求一个动作** |
| **响应报文（response）** | 把**结果**返回给客户端 |

---

## 二、三段结构

```text
┌─ 起始行（start line）──── 整体描述（一行）
├─ 首部（header）────────── 零个或多个 名字: 值
├─ 空行（CRLF）──────────── 首部结束标志
└─ 实体主体（entity-body）── 可选；文本或二进制；可为空
```

### 1）起始行

| 类型 | 格式 |
|------|------|
| **请求** | `<method> <request-URL> <version>` |
| **响应** | `<version> <status> <reason-phrase>` |

### 2）首部（header）

- 属性字典：`名字: 值`（冒号后可有空格）  
- 为报文添加**附加信息**（缓存、类型、认证等）→ [3.5](./05-header.md)

### 3）实体主体（entity-body）

- **可选**数据块；GET 响应体、POST 表单等  
- 详 [3.6](./06-entity.md)

---

## 三、关键字段含义

| 字段 | 说明 |
|------|------|
| **method** | 希望对资源执行的动作（GET、POST…）→ [3.3](./03-method.md) |
| **status-code** | 三位数字，**机器**读的结果 → [3.4](./04-status-code.md) |
| **reason-phrase** | 状态码的**人类可读**短语；**不影响**程序逻辑 |
| **version** | `HTTP/<major>.<minor>`，声明支持的 HTTP 版本 |

---

## 四、易错

| 点 | 说明 |
|----|------|
| **行结束** | 规范为 **CRLF**；稳健实现也应接受**单独 LF** |
| **首部结束** | 必须有空行（仅 CRLF）分隔首部与主体；历史实现常漏空行 → **解析要容错** |
| **版本比较** | **不能当小数**！`HTTP/2.22` **>** `HTTP/2.3`（比较 **22** 与 **3**） |

---

## 拓展（预留）

- HTTP/1.1 强制 **Host** 首部等与 1.0 的结构差异  
- HTTP/2 **二进制分帧**对传统「纯文本三段式」的颠覆 → [ch10](../chapter-10-http-ng/chapter-summary.md)

---

## 抓包/实操记录

（待填：Wireshark 展开 Hypertext Transfer Protocol，标出 Request Line / Headers / Body）

---

## 疑问与总结

请求与响应**结构对称**；差异主要在**起始行**第一行格式。
