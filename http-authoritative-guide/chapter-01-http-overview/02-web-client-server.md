# 1.2 Web 客户端和服务器

> 本章：[chapter-summary.md](./chapter-summary.md#ch01-2) · [1.4 事务](./04-transaction.md)

## 本节核心目标

分清 **HTTP 客户端** 与 **HTTP 服务器** 的角色与一次交互闭环。

---

## 一、角色定义

| 角色 | 典型实现 | 做什么 |
|------|----------|--------|
| **客户端（Client）** | 浏览器、App、curl | 发 **HTTP 请求**，展示或处理响应 |
| **服务器（Server）** | Nginx、Apache、应用后端 | **存资源**，查对象，回 **HTTP 响应**（含类型、长度等元数据） |

---

## 二、交互逻辑

```text
客户端 ──请求报文──► 服务器
客户端 ◄──响应报文── 服务器（含对象或错误信息）
```

→ 细节：[1.4 事务](./04-transaction.md) · [1.5 报文](./05-message.md)

---

## 拓展（预留）

- 移动端 App、IoT 作客户端  
- 服务器**集群**、负载均衡（→ [ch20](../chapter-20-redirect-load-balance/chapter-summary.md)）

---

## 抓包/实操记录

（待填：`curl -v http://example.com` 看请求/响应）

---

## 疑问与总结

**C/S 模型**；谁发请求谁是客户端（即使服务器之间互调 API 时角色会反转）。
