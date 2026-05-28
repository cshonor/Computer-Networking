# 4.3 HTTP连接

> 本章：[chapter-summary.md](./chapter-summary.md#ch04-3) · [3.5 首部](../chapter-03-http-message/05-header.md) · [4.4 并行](./04-parallel-connection.md)

## 本节核心目标

掌握 **`Connection` 逐跳首部**、代理的**首部保护**，以及**串行事务**的性能痛点。

---

<a id="ch04-3-connection-hdr"></a>

## 一、Connection 首部（易错）

`Connection` 是 **hop-by-hop（逐跳）** 首部：

- 列表里的名字**只作用于当前这一条 TCP 连接**  
- **代理转发前必须删除** `Connection` 及其列出的所有首部 → **首部保护（header protection）**

其他常见**不能盲目转发**的逐跳首部：

| 首部 | 说明 |
|------|------|
| `Proxy-Authenticate` | 代理认证 |
| `Proxy-Connection` | 非标准、历史遗留 |
| `Transfer-Encoding` | 分块编码边界 |
| `Upgrade` | 协议升级 |

→ 通用首部分类 [ch03 §3.5](../chapter-03-http-message/05-header.md)

---

<a id="ch04-3-serial"></a>

## 二、串行事务时延

传统浏览器对一页多个嵌入对象：

1. **依次**建连  
2. **依次**下载  

叠加：**连接握手 + 慢启动** × N，用户长时间**白屏**。

---

## 拓展（预留）

- HTTP/2 **多路复用** 在单 TCP 上并行流 → [ch10](../chapter-10-http-ng/chapter-summary.md)  
- HTTP/3 / QUIC 减轻 TCP 层 HOL 阻塞

---

## 抓包/实操记录

（待填：经公司代理时 `Connection` 是否被剥掉）

---

## 疑问与总结

**代理不是透明管道**；逐跳首部必须在每一跳重新协商。
