# 6.6 追踪报文

> 本章：[chapter-summary.md](./chapter-summary.md#ch06-6) · [ch03 方法](../chapter-03-http-message/03-method.md)

## 本节核心目标

用 **`Via`** 与 **`TRACE` + `Max-Forwards`** 追踪代理链、发现环路。

---

<a id="ch06-6-via"></a>

## 一、Via 首部

每经过一个代理/网关，在 **`Via` 列表末尾**追加：

```http
Via: 1.1 proxy.irenes-isp.net, 1.0 cache.joes.com
```

语法：`Via: <协议版本> <节点名> [<注释>]`

| 用途 | 说明 |
|------|------|
| 记录路径 | 审计、排障 |
| **环路检测** | 转发前若 `Via` 中**已有自己名字** → 死循环 |
| 能力标识 | 沿途协议版本 |

**隐私**：防火墙代理可用**假名**、**合并**内部连续 `Via` 条目，防拓扑泄露。

---

<a id="ch06-6-trace"></a>

## 二、TRACE 与 Max-Forwards

| 机制 | 说明 |
|------|------|
| **TRACE** | 端点把收到的请求封装在 **`200 OK`** 里，`Content-Type: message/http`，供客户端查看被改动了什么 |
| **Max-Forwards** | 整数跳数；每跳 **减 1**；为 **0** 时**不再转发**，由当前节点直接回 TRACE 响应 |

用于探测链上**特定深度**的行为。

---

## 拓展（预留）

- 对比 **Zipkin/Jaeger** `traceparent` / `X-B3-*` 与 `Via`  

---

## 抓包/实操记录

（待填：`curl -X TRACE -H "Max-Forwards: 1"` 若服务器允许）

---

## 疑问与总结

**Via = 路过谁；TRACE = 中间人改没改报文。**
