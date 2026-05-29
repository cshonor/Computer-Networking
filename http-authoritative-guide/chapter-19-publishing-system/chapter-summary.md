# 第19章 发布系统

> 全书：[../README.md](../README.md) · 前章：[ch18 托管](../chapter-18-web-hosting/chapter-summary.md) · 后章：[ch20 重定向](../chapter-20-redirect-load-balance/chapter-summary.md)

## 本章概述

Web **发布**在 HTTP 之上扩展：**FrontPage FPSE**（POST 内 **RPC**、根/子 Web、三类角色，安全风险高）与 **WebDAV**（**PROPFIND/LOCK/MKCOL** 等、**XML**、**Depth**、**207 Multi-Status**、锁防丢失更新）。现代 CMS 多用 REST API；网盘仍可见 WebDAV。规范 **RFC 4918**、版本 **RFC 3253**。

---

## 知识框架

```mermaid
flowchart LR
  CLIENT[写作客户端]
  CLIENT -->|FPSE POST RPC| SRV[Web 服务器]
  CLIENT -->|WebDAV 方法+XML| SRV
```

| 节 | 关键词 |
|----|--------|
| <a id="ch19-1"></a> **19.1** | FPSE、RPC、子 Web |
| <a id="ch19-2"></a> **19.2** | LOCK、Depth、207、DeltaV |
| <a id="ch19-3"></a> **19.3** | RFC 4918/3253 |

---

## 重点 & 难点

| 易错 | 要点 |
|------|------|
| WebDAV 替换 HTTP | **扩展**方法，仍 HTTP |
| DELETE 集合默认 Depth | **infinity** |
| PUT 任意写 | 锁定时要 **If + 令牌** |
| FPSE 安全 | 历史漏洞，慎开 |
| 2518 vs 4918 | 查 **4918** |

---

## 实操要点

- `curl -X OPTIONS https://dav.example/ -v`  
- 挂载 WebDAV 盘观察 LOCK/PUT  

---

## 小节索引

| 书节 | 文件 |
|------|------|
| 19.1 | [01-frontpage-fpse.md](./01-frontpage-fpse.md) |
| 19.2 | [02-webdav.md](./02-webdav.md) |
| 19.3 | [03-more-info.md](./03-more-info.md) |

---

## 自测

1. FPSE 如何在 HTTP 上传命令？  
2. 列出 4 个 WebDAV 方法。  
3. Depth 三个值含义？  
4. 为何用 207？  
5. RFC 3253 补什么？
