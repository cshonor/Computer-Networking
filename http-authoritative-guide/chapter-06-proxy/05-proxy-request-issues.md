# 6.5 与代理请求有关的一些棘手问题

> 本章：[chapter-summary.md](./chapter-summary.md#ch06-5) · [ch02 URL](../chapter-02-url-and-resource/chapter-summary.md) · [ch03 报文](../chapter-03-http-message/02-message-component.md)

## 本节核心目标

分清**发给代理 vs 发给源站**的 URI 形式，以及代理的**解析/转发规则**与常见陷阱。

---

<a id="ch06-5-uri-forms"></a>

## 一、代理 URI vs 服务器 URI

| 目标 | 请求行 URI |
|------|------------|
| **源服务器** | **部分 URI**（路径）`GET /index.html HTTP/1.1` |
| **代理** | **绝对 URI** `GET http://www.host.com/index.html HTTP/1.1` |

代理需知**完整目标**才能建连。

---

<a id="ch06-5-rules"></a>

## 二、代理处理规则

| 收到 | 行为 |
|------|------|
| **完整 URI** | 必须用该 URI |
| **部分 URI + `Host`** | 用 `Host` 定源站 |
| **部分 URI 无 `Host`** | 替代物：预配置真实 IP；拦截代理：用底层截获的原始 IP |

---

<a id="ch06-5-rewrite"></a>

## 三、URI 转发修改限制

拦截代理转发时**禁止随意改绝对路径**（例外：空路径可用 `/`）。  
乱改路径会导致下游应用崩溃。

---

## 易错陷阱

| 陷阱 | 说明 |
|------|------|
| **浏览器自动补全** | 无代理时 `oreilly` 可能试 `www.oreilly.com`；**显式代理**时可能直接发 `http://oreilly/` 给代理，代理若无容错则**失败** |
| **拦截代理 + DNS** | 客户端 DNS 到旧 IP，连接被截获；代理连真实源时 IP 可能已死 → 代理需 **`Host` 重解析** 等容错 |
| **HTTP/1.0 无 Host** | 虚拟主机与代理路由灾难 → [ch18](../chapter-18-web-hosting/chapter-summary.md) |

---

## 抓包/实操记录

（待填：经代理时请求行是否为绝对 URL）

---

## 疑问与总结

**代理看绝对 URL；源站看路径 + Host。**
