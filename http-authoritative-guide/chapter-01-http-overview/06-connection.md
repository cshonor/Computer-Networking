# 1.6 连接

> 本章：[chapter-summary.md](./chapter-summary.md#ch01-6) · [ch04 连接管理](../chapter-04-connection-management/chapter-summary.md)

## 本节核心目标

理解 HTTP 如何依赖 **TCP/IP**，以及从 URL 到一次 HTTP 交换的**七步**。

---

<a id="ch01-6-stack"></a>

## 一、TCP/IP 协议栈

```text
应用层   HTTP
传输层   TCP  ← 无差错、按序、字节流
网络层   IP
```

| 层 | 给 HTTP 什么 |
|----|----------------|
| **TCP** | 可靠端到端连接 |
| **IP** | 主机寻址 |

---

<a id="ch01-6-connect"></a>

## 二、IP、端口、DNS

发报文前要先 **TCP 连接** 到服务器：

| 项 | 来源 |
|----|------|
| **IP** | URL 主机名 → **DNS** 解析 |
| **端口** | URL 显式端口；省略则 HTTP 默认 **80**（HTTPS **443**） |

→ URL 语法 [ch02](../chapter-02-url-and-resource/02-url-syntax.md)

---

<a id="ch01-6-seven"></a>

## 三、通信七步骤（背诵）

1. 解析 URL 主机名  
2. DNS → IP  
3. 解析端口（默认 80）  
4. 建立 **TCP** 连接  
5. 发送 **HTTP 请求**  
6. 接收 **HTTP 响应**  
7. 关闭连接（或复用）并展示  

→ 持久连接 [ch04](../chapter-04-connection-management/chapter-summary.md)

---

<a id="ch01-6-telnet"></a>

## 四、Telnet 调试

HTTP 基于 TCP、报文可读 → 可用 **Telnet**（或 `nc`）连 `host 80`，手敲：

```http
GET / HTTP/1.1
Host: example.com

```

（注意最后**空行**）

---

## 拓展（预留）

- 慢启动、Nagle 对 HTTP 延迟（ch04）  
- 与 [TCP/IP 卷1 ch01 DNS 概念](../../TCP-IP-Volume1-Protocols/chapter01-overview/study.md) · [自顶向下 2.4 DNS](../../top_down/02_application_layer/2.4_dns_service/study.md) 对照

---

## 抓包/实操记录

（待填：`Test-NetConnection example.com -Port 80` 或 `nc`）

---

## 疑问与总结

**HTTP 不自己传包**；断线先查 TCP/DNS，再查 HTTP 状态码。
