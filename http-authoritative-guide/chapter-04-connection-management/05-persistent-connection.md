# 4.5 持久连接

> 本章：[chapter-summary.md](./chapter-summary.md#ch04-5) · [4.6 管道](./06-pipeline-connection.md) · [4.7 关闭](./07-close-connection.md)

## 本节核心目标

掌握 **keep-alive / 持久连接** 如何省握手与慢启动，以及 **1.0+ 与 1.1** 的差异与**哑代理**陷阱。

---

<a id="ch04-5-combo"></a>

## 一、持久 + 并行

- **持久连接**：同站多资源**复用 TCP**  
- **单条连接**仍可能被**大对象阻塞**  
- 现代实践：**少量并行 + 每条持久**

---

<a id="ch04-5-keepalive"></a>

## 二、HTTP/1.0+ Keep-Alive

| 点 | 说明 |
|----|------|
| 协商 | 客户端 `Connection: Keep-Alive`，服务器同意则回送 |
| 截断 | 必须有正确 **`Content-Length`**（或等价机制） |
| 代理 | 须删除逐跳首部 |

---

<a id="ch04-5-dumb-proxy"></a>

## 三、哑代理与 Proxy-Connection（易错）

```text
客户端 ──Keep-Alive──► 哑代理 ──原样转发──► 服务器
         代理不知连接仍开着 → 报文挂起 / 浏览器死锁
```

- 网景曾用非标准 **`Proxy-Connection`**  
- **多级代理** 仍可能失效  

**HTTP/1.1** 用默认持久 + 明确的 `Connection: close` 缓解部分问题。

---

<a id="ch04-5-persistent"></a>

## 四、HTTP/1.1 持久连接（默认开）

| 规则 | 说明 |
|------|------|
| 默认 | **持久**，除非显式 `Connection: close` |
| 客户端限制 | 对同一服务器/代理通常最多 **2 条** 持久连接（防过载）→ [4.8](./08-connection-limit.md) |

---

## 抓包/实操记录

（待填：同一 TCP 流上多个 `GET` 的 `Seq` 连续）

---

## 疑问与总结

**1.1 默认别关；关要说 `Connection: close`。** 代理必须懂逐跳语义。
