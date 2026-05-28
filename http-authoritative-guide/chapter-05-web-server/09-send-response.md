# 5.9 第六步——发送响应

> 本章：[chapter-summary.md](./chapter-summary.md#ch05-9) · [ch04 持久连接](../chapter-04-connection-management/05-persistent-connection.md)

## 本节核心目标

并发下**写回响应**，并避免持久连接上的**长度错误**。

---

<a id="ch05-9-state"></a>

## 一、连接状态机

服务器跟踪每条连接：**空闲 / 读请求 / 写响应** 等，在大量并发间切换。

---

<a id="ch05-9-keepalive"></a>

## 二、持久连接致命点（易错）

**Keep-Alive** 下必须给出**精确**的响应边界：

- 正确 **`Content-Length`**，或  
- **`Transfer-Encoding: chunked`**

否则客户端**不知道本条响应在哪结束** → 连接上后续报文**全部解析错乱**（挂起、死锁）→ [ch04 哑代理](../chapter-04-connection-management/05-persistent-connection.md#ch04-5-dumb-proxy)

---

## 拓展（预留）

- **`sendfile` 零拷贝** 发静态文件  
- 写缓冲与 **TCP_NODELAY**

---

## 抓包/实操记录

（待填：错误 Content-Length 时浏览器行为）

---

## 疑问与总结

**第 6 步 = 字节真正上网**；长度错 = 应用层协议级灾难。
