# 21.2 日志格式

> 本章：[chapter-summary.md](./chapter-summary.md#ch21-2) · [ch05.10](../chapter-05-web-server/10-logging.md)

## 本节核心目标

掌握 **CLF / Combined** 及代理专用格式，以便对接分析工具。

---

<a id="ch21-2-why-standard"></a>

## 为何用标准格式

标准格式可直接使用大量**开源/商用**分析工具做压缩、汇总、可视化。

---

<a id="ch21-2-clf"></a>

## 21.2.1 常见日志格式（CLF）

NCSA 定义；许多服务器**默认**格式。

| 字段 | 说明 |
|------|------|
| `remotehost` | 客户端 IP 或主机名 |
| `username` | ident 查找结果 |
| `auth-username` | 认证用户名 |
| `timestamp` | 时间戳 |
| `request-line` | 请求行原文 |
| `response-code` | 状态码 |
| `response-size` | 响应大小 |

```
127.0.0.1 - - [21/May/2026:10:00:00 +0800] "GET /index.html HTTP/1.1" 200 1234
```

---

<a id="ch21-2-combined"></a>

## 21.2.2 组合日志格式（Combined）

在 CLF 基础上增加：

| 字段 | 用途 |
|------|------|
| **`Referer`** | 用户从哪来 |
| **`User-Agent`** | 浏览器/爬虫标识 |

Apache 等广泛支持。

---

<a id="ch21-2-netscape"></a>

## 21.2.3–21.2.4 网景扩展日志（Extended 1 & 2）

面向**代理/缓存**的扩展，额外度量例如：

| 类别 | 示例字段 |
|------|----------|
| 代理响应码 | 代理层状态 |
| 报文大小 | 客户端↔代理、代理↔源站 请求/首部大小 |
| **`route`** | 路由路径 |
| 完成状态 | `FIN`、`INTR`（中断）等 |
| 缓存结果 | `WRITTEN`、`REFRESHED` 等 |

---

<a id="ch21-2-squid"></a>

## 21.2.5 Squid 代理日志格式

Squid 项目格式，被许多后继代理沿用。

| 字段 | 说明 |
|------|------|
| **`action-code`** | 代理行为 |
| **耗时** | 毫秒级 |

**action-code 示例**：

| 代码 | 含义 |
|------|------|
| `TCP_HIT` | 缓存命中 |
| `TCP_MISS` | 未命中 |
| `TCP_REFRESH_MISS` | 再验证后过期，重新获取 |

→ 与 [ch07 Hit/Miss](../chapter-07-cache/05-hit-miss.md)、[ch20 ICP](../chapter-20-redirect-load-balance/07-icp.md) 对照。

---

## 拓展（预留）

- **JSON** 结构化日志的索引性能  
- **ELK/EFK** 管道  

---

## 抓包/实操记录

（待填：Apache Combined vs Squid access.log 各一条）

---

## 疑问与总结

| 场景 | 首选格式 |
|------|----------|
| 源站 Web 服务器 | CLF / Combined |
| 代理/缓存 | Netscape Extended / Squid |
