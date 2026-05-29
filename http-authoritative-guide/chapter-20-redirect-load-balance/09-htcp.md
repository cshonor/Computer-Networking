# 20.9 超文本缓存协议（HTCP）

> 本章：[chapter-summary.md](./chapter-summary.md#ch20-9) · [ch17 透明协商/Vary](../chapter-17-content-negotiation-transcode/04-transparent-negotiation.md) · [20.7 ICP](./07-icp.md)

## 本节核心目标

理解 **HTCP** 如何超越 ICP 的「仅 URL」查询，支持**首部级**协作与认证。

---

<a id="ch20-9-why"></a>

## 为何需要 HTCP

ICP 只传 **URL** → HTTP/1.0/1.1 下**请求首部不同**时可能**错误命中**（假 HIT）。

HTCP：兄弟缓存间交换 **URL + 请求/响应首部**，降低误判。

→ 与 **`Vary`** 多变体缓存相关：[ch17 透明协商](../chapter-17-content-negotiation-transcode/04-transparent-negotiation.md)

---

<a id="ch20-9-auth"></a>

## 20.9.1 HTCP 认证

可选认证段：**HMAC-MD5** + 共享密钥，对请求/响应签名。

---

<a id="ch20-9-set"></a>

## 20.9.2 设置缓存策略

**`SET`** 报文可：

- 监控、添加、删除兄弟缓存中的文档  
- 修改对方已缓存对象的策略（如 **`Cache-Vary`**、**`Cache-Policy`** 等）

兄弟缓存**协作能力**显著强于 ICP。

---

## 拓展（预留）

- 单一 URL 查询无法处理 `Vary` 多变体 — HTCP 全量首部的必要性  

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

| 协议 | 查询粒度 | 主要问题 |
|------|----------|----------|
| **ICP** | URL | 错误命中、冗余 |
| **CARP** | Hash(URL) | 节点变更失效 |
| **HTCP** | URL + 首部 | 更准、可管策略 |
