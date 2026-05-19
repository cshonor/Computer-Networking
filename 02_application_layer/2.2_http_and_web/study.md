# 2.2 HTTP 与 Web

> 章级精读：[../study.md#ch2-2](../study.md#ch2-2) · 四层嵌套：[#ch2-http-stack](#ch2-http-stack)

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

展开顺序：**Ethernet II → IPv4 → TCP → [HTTP 明文]**（HTTPS 先看到 TLS，解密后才见 HTTP）

---

## 个人总结

HTTP 是互联网使用最广泛的应用层协议；**装在 TCP 里、再被 IP 和以太网帧一层层包住**。无状态靠 Cookie 补状态；后端开发必会读请求行/状态码/首部。
