# 2.2 HTTP 与 Web

> 章级精读：[../study.md#ch2-2](../study.md#ch2-2) · 四层嵌套：[#ch2-http-stack](#ch2-http-stack) · **TCP 载荷明文/密文**：[#ch2-http-tls-payload](#ch2-http-tls-payload)

## 本节核心目标

掌握万维网与 HTTP 协议工作原理，以及 HTTP 在 TCP/IP 栈中的位置。

## 核心知识点

1. Web 组成：浏览器、Web 服务器、HTML、URL
2. HTTP 核心特点：无状态、基于 TCP
3. HTTP 连接类型：非持久连接、持久连接
4. HTTP 请求报文、响应报文结构
5. Cookie 状态管理、代理缓存加速原理

---

<a id="ch2-http-stack"></a>

## 完整层级嵌套总览

**以太网帧 → IP 数据报 → TCP 报文段 → HTTP 报文**

HTTP 属于**应用层**，放在 **TCP 的数据载荷（Payload）**里，分**请求报文**与**响应报文**两种。

```text
以太网帧
└── IP 数据报
    └── TCP 报文段
        ├── TCP 首部（端口、Seq、Ack…）
        └── TCP 数据区
            └── HTTP 报文（请求/响应文本）
```

| 层 | PDU | 本例谁变、谁不变 |
|----|-----|------------------|
| 链路 | 以太网帧 | MAC **每跳换** |
| 网络 | IP 数据报 | 源/目 IP **端到端不变** |
| 运输 | TCP 段 | 四元组固定；序号/ACK 逐段变化 |
| 应用 | HTTP 报文 | 在 TCP 载荷里，**明文文本**（HTTPS 再套 TLS） |

→ 封装详解：[第 4 章 TCP⊂IP⊂MAC](../../04_network_layer_data_plane/study.md#ch4-encapsulation) · [以太网帧](../../06_link_layer_and_lan/study.md#ch6-ethernet-frame) · [Wireshark 树](../../04_network_layer_data_plane/study.md#ch4-encapsulation-wireshark)

---

<a id="ch2-http-tls-payload"></a>

## HTTP vs HTTPS：TCP 载荷是明文还是密文？

### 1）普通 HTTP：TCP 载荷 = **明文文本**

HTTP **直接**跑在 TCP 上：

```
┌──────────── TCP 段 ────────────┐
│ TCP 首部（20～60 B）           │
├──────────────────────────────┤
│ TCP 载荷 = 整个 HTTP 报文（明文）│
│ GET /path HTTP/1.1           │
│ Host: example.com            │
│ ...                          │
└──────────────────────────────┘
```

抓包 **TCP 数据区** 可直接读出：

```http
GET /shturl.cc/ HTTP/1.1
Host: shturl.cc
User-Agent: ...
```

**结论：HTTP → TCP 载荷 = 明文（裸奔，中间人可读）**

---

### 2）HTTPS = HTTP + **TLS**（套在 TCP 之上）

**逻辑分层（自下而上）**：

```text
TCP
 └── TLS（加密记录层）
      └── HTTP（应用层明文，仅在两端进程内）
```

**发送方向数据流**

1. **应用层**：HTTP **明文**（浏览器 / 服务器内部处理）  
2. **TLS 层**：把 HTTP 明文 **整体加密** → **TLS 密文记录**  
3. **TCP 层**：把 **TLS 密文** 放进 **TCP 载荷** 发出  

**抓包看到什么**

| 层级 | 抓包可见 |
|------|----------|
| TCP 首部 | 源/目的端口、序号等（**明文**） |
| **TCP 载荷** | **TLS 密文**（乱码，**不可直接读 HTTP**） |
| 中间路由器/Wi‑Fi/运营商 | 只见 TCP 头 + 密文，**看不到 URL、Cookie、正文** |

**结论：HTTPS → TCP 载荷 = TLS 密文（不是 HTTP 明文）**

---

### 3）抓包对比（一眼分清）

```text
【HTTP  端口 80】  Ethernet → IP → TCP → 载荷里直接是 GET / HTTP/1.1 ...

【HTTPS 端口 443】 Ethernet → IP → TCP → 载荷里是 TLS Application Data（密文）
                                    └── Wireshark 配密钥才可解密出 HTTP
```

> **HTTP/3**：HTTP 跑在 **QUIC（UDP）** 上，仍经 TLS 加密；载荷在 **UDP 包**里而非传统「TCP 载荷」，但**网络上仍是密文**。

---

### 4）考试 / 面试一句话

- **HTTP**：TCP 载荷里是 **明文 HTTP 文本**  
- **HTTPS**：HTTP 先经 **TLS 加密**，TCP 载荷里是 **密文**  

### 5）易混澄清

| ❌ 错误 | ✅ 正确 |
|--------|--------|
| HTTPS 的 TCP 载荷里还有明文 HTTP | 网上（TCP 载荷）**全程密文**；HTTP 明文只在**两端应用层** |
| TLS 在 IP 层 | TLS 在 **TCP 之上、HTTP 之下**（常称「介于应用与运输之间」） |
| 加密后 TCP 头也看不见 | **TCP/IP 首部仍明文**；加密的是 **载荷（TLS 记录）** |

→ HTTP 报文格式：[§一、二](#ch2-http-stack) · 首部结构图：[第 1 章 HTTP 响应](../01_network_basics/1.5_protocol_layer_architecture/study.md#ch1-5-app-messages)

---

## 一、HTTP 请求报文（客户端 → 服务器）

```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 Windows NT 10.0
Accept: text/html,image/webp
Connection: keep-alive


```

### 结构拆分

| 部分 | 示例 | 说明 |
|------|------|------|
| **请求行** | `GET /index.html HTTP/1.1` | 方法 + 路径 + 版本 |
| **请求头** | `Host:`、`User-Agent:`… | 多行键值对 |
| **空行** | （一行空行） | **必须有**，分隔头与体 |
| **请求体** | （可无） | GET 通常无；POST 表单/上传在体里 |

**请求行字段**

- **方法**：GET、POST、PUT、DELETE…
- **路径**：`/index.html` 等资源 URI
- **版本**：`HTTP/1.1`

---

## 二、HTTP 响应报文（服务器 → 客户端）

```http
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 19 May 2026
Content-Type: text/html
Content-Length: 1268
Connection: keep-alive

<html>
<head><title>测试页面</title></head>
<body><h1>欢迎访问网页</h1></body>
</html>
```

### 结构拆分

| 部分 | 示例 | 说明 |
|------|------|------|
| **状态行** | `HTTP/1.1 200 OK` | 版本 + **状态码** + 短语 |
| **响应头** | `Content-Type:`… | 类型、长度、服务器信息等 |
| **空行** | | 分隔头与正文 |
| **响应正文** | HTML 等 | 浏览器最终渲染的内容 |

**常见状态码**：`200` 成功 · `404` 未找到 · `500` 服务器错误

---

## 三、Wireshark 里「真实长什么样」

TCP 载荷里就是下面这段文本（`\r\n` = 回车换行）：

```text
GET / HTTP/1.1\r\n
Host: baidu.com\r\n
User-Agent: Mozilla/5.0\r\n
Accept: */*\r\n
\r\n
```

展开顺序：**Ethernet II → IPv4 → TCP → [HTTP 明文]**（HTTPS：**TCP 载荷 = TLS 密文**，见 [#ch2-http-tls-payload](#ch2-http-tls-payload)）

---

<a id="ch2-2-exam"></a>

## 易错点速记

| 易混 | 纠正 |
|------|------|
| HTTPS TCP 载荷 | **TLS 密文**，不是明文 HTTP |
| HTTP 在哪层明文？ | **仅两端应用进程内**；链路上 HTTP 裸奔、HTTPS 加密 |
| 端口 | HTTP **80**；HTTPS **443** |

---

## 个人总结

HTTP 在 **TCP 载荷里明文**；**HTTPS = TLS 加密后再进 TCP 载荷（密文）**。装在 IP/以太网帧里逐层封装。无状态靠 Cookie；必会请求行/状态码/首部。
