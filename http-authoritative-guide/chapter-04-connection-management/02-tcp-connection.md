# 4.2 TCP连接

> 本章：[chapter-summary.md](./chapter-summary.md#ch04-2) · 全书：[../README.md](../README.md) · 前章：[ch01 连接](../chapter-01-http-overview/06-connection.md)

## 本节核心目标

理解 **HTTP 几乎全靠 TCP/IP 承载**，以及 TCP 为 HTTP 提供的**可靠比特管道**与四元组标识。

---

<a id="ch04-2-pipe"></a>

## 一、可靠的 TCP 数据管道

建立 TCP 连接后，两端交换的字节：

- **不丢失、不损坏、不失序**  
- 一端写入的字节流，在另一端**按原顺序、正确**读出  

→ [ch01 §1.6](../chapter-01-http-overview/06-connection.md#ch01-6-stack)

---

<a id="ch04-2-stack"></a>

## 二、协议栈与分段

```text
HTTP
  │  （HTTPS：中间插入 TLS/SSL）
TCP  ← 切成 segment（段）
IP   ← 封装成 packet（分组）
```

| 封装 | 典型大小 |
|------|----------|
| IP 首部 | ~20 B |
| TCP 首部 | ~20 B |
| TCP 数据 | HTTP 报文字节 |

---

<a id="ch04-2-quad"></a>

## 三、四元组唯一标识连接

**`<源 IP, 源端口, 目的 IP, 目的端口>`** — 用**端口号**区分同一主机上的多个 TCP 连接。

| 角色 | 常见端口 |
|------|----------|
| HTTP 服务器 | **80** |
| HTTPS | **443** |

---

<a id="ch04-2-socket"></a>

## 四、套接字（Socket）API

OS 提供 Socket API，向 HTTP 程序员**隐藏** TCP/IP 细节：

- 创建、绑定、监听、接受连接  
- `read` / `write` 收发数据  

应用代码通常不直接拼 TCP 段，而是对**已连接的套接字**读写。

---

## 拓展（预留）

- Java `Socket`、Python `socket`、Go `net.Conn` 与 BSD socket 对应关系  

---

## 抓包/实操记录

（待填：Wireshark 看同一 HTTP 流上的 TCP 段序号）

---

## 疑问与总结

**HTTP 语义在应用层；可靠传输靠 TCP。**
