# 1.8 Web 的结构组件

> 本章：[chapter-summary.md](./chapter-summary.md#ch01-8)

## 本节核心目标

认识除浏览器/源站外的 **HTTP 中间件** 五类角色。

---

<a id="ch01-8-proxy"></a>

## 1.8.1 代理（Proxies）

- 位于 **客户端与服务器之间**  
- 代表用户访问上游；防火墙、集成、加速  

→ [ch06 代理](../chapter-06-proxy/chapter-summary.md)

---

<a id="ch01-8-cache"></a>

## 1.8.2 缓存（Caches）

- 特殊代理：**本地副本**常用文档  
- 后续请求**就近命中**  

→ [ch07 缓存](../chapter-07-caching/chapter-summary.md)

---

<a id="ch01-8-gateway"></a>

## 1.8.3 网关（Gateways）

- 连接**不同协议**的应用（如 HTTP 前端 + **FTP** 后端）  
- 把异构响应封装成 HTTP  

→ [ch08 网关/隧道](../chapter-08-gateway-tunnel-relay/chapter-summary.md)

---

<a id="ch01-8-tunnel"></a>

## 1.8.4 隧道（Tunnels）

- 两条连接间**盲转发**（不解析内容）  
- 典型：**HTTP CONNECT** 穿防火墙传 **TLS**  

→ [ch08 隧道](../chapter-08-gateway-tunnel-relay/05-tunnel.md) · 对比 [TCP/IP ch03 隧道](../../TCP-IP-Volume1-Protocols/chapter03-link-layer/3.9-tunnel-basics.md)（网络层封装，概念不同层）

---

<a id="ch01-8-agent"></a>

## 1.8.5 Agent 代理

- **自动**发 HTTP 的客户端：爬虫、机器人、监控  

→ [ch09 爬虫](../chapter-09-web-robot/chapter-summary.md)

---

## 结构一览

```text
浏览器 ──► 代理/缓存 ──► 网关 ──► 源服务器
              │
              └── 隧道（如 SSL 穿透）
爬虫（Agent）──────────────► 服务器
```

---

## 抓包/实操记录

（待填：公司代理 `Via` / `X-Forwarded-For` 首部）

---

## 疑问与总结

**代理会改语义（缓存命中）**；**隧道尽量不解析**。
