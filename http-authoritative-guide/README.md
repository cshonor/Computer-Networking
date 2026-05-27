# HTTP 权威指南 学习笔记

《HTTP 权威指南》

> **打开本文件夹**：每章一个 `chapter-XX-*/`；**`chapter-summary.md` = 本章总览**，**`序号-英文名.md` = 小节笔记**。

## 书籍信息

| 项 | 说明 |
|----|------|
| 书名 | 《HTTP 权威指南》 |
| 结构 | 21 章，见 [OUTLINE.md](./OUTLINE.md) |

## 目录规范

- `chapter-xx-…/`：独立章节文件夹
- `chapter-summary.md`：本章整体总结、知识梳理
- `01-xxx.md`：对应小节独立笔记（见名知意，不用 section 通用名）
- `.gitkeep`：Git 空目录追踪

## 章节目录

| 章 | 文件夹 | 总览 |
|----|--------|------|
| 第1章 HTTP概述 | [chapter-01-http-overview/](./chapter-01-http-overview/) | [summary](./chapter-01-http-overview/chapter-summary.md) |
| 第2章 URL与资源 | [chapter-02-url-and-resource/](./chapter-02-url-and-resource/) | [summary](./chapter-02-url-and-resource/chapter-summary.md) |
| 第3章 HTTP报文 | [chapter-03-http-message/](./chapter-03-http-message/) | [summary](./chapter-03-http-message/chapter-summary.md) |
| 第4章 连接管理 | [chapter-04-connection-management/](./chapter-04-connection-management/) | [summary](./chapter-04-connection-management/chapter-summary.md) |
| 第5章 Web服务器 | [chapter-05-web-server/](./chapter-05-web-server/) | [summary](./chapter-05-web-server/chapter-summary.md) |
| 第6章 代理 | [chapter-06-proxy/](./chapter-06-proxy/) | [summary](./chapter-06-proxy/chapter-summary.md) |
| 第7章 缓存 | [chapter-07-cache/](./chapter-07-cache/) | [summary](./chapter-07-cache/chapter-summary.md) |
| 第8章 集成点：网关、隧道及中继 | [chapter-08-gateway-tunnel-relay/](./chapter-08-gateway-tunnel-relay/) | [summary](./chapter-08-gateway-tunnel-relay/chapter-summary.md) |
| 第9章 Web机器人 | [chapter-09-web-robot/](./chapter-09-web-robot/) | [summary](./chapter-09-web-robot/chapter-summary.md) |
| 第10章 HTTP-NG | [chapter-10-http-ng/](./chapter-10-http-ng/) | [summary](./chapter-10-http-ng/chapter-summary.md) |
| 第11章 客户端识别与Cookie机制 | [chapter-11-client-id-cookie/](./chapter-11-client-id-cookie/) | [summary](./chapter-11-client-id-cookie/chapter-summary.md) |
| 第12章 基本认证机制 | [chapter-12-basic-auth/](./chapter-12-basic-auth/) | [summary](./chapter-12-basic-auth/chapter-summary.md) |
| 第13章 摘要认证 | [chapter-13-digest-auth/](./chapter-13-digest-auth/) | [summary](./chapter-13-digest-auth/chapter-summary.md) |
| 第14章 安全HTTP | [chapter-14-secure-http/](./chapter-14-secure-http/) | [summary](./chapter-14-secure-http/chapter-summary.md) |
| 第15章 实体和编码 | [chapter-15-entity-encoding/](./chapter-15-entity-encoding/) | [summary](./chapter-15-entity-encoding/chapter-summary.md) |
| 第16章 国际化 | [chapter-16-internationalization/](./chapter-16-internationalization/) | [summary](./chapter-16-internationalization/chapter-summary.md) |
| 第17章 内容协商与转码 | [chapter-17-content-negotiation-transcode/](./chapter-17-content-negotiation-transcode/) | [summary](./chapter-17-content-negotiation-transcode/chapter-summary.md) |
| 第18章 Web主机托管 | [chapter-18-web-hosting/](./chapter-18-web-hosting/) | [summary](./chapter-18-web-hosting/chapter-summary.md) |
| 第19章 发布系统 | [chapter-19-publishing-system/](./chapter-19-publishing-system/) | [summary](./chapter-19-publishing-system/chapter-summary.md) |
| 第20章 重定向与负载均衡 | [chapter-20-redirect-load-balance/](./chapter-20-redirect-load-balance/) | [summary](./chapter-20-redirect-load-balance/chapter-summary.md) |
| 第21章 日志记录与使用情况跟踪 | [chapter-21-log-tracking/](./chapter-21-log-tracking/) | [summary](./chapter-21-log-tracking/chapter-summary.md) |

## 前置知识

- [计算机网络 自顶向下](../top_down/)
- [TCP/IP 详解 卷一](../TCP-IP-Volume1-Protocols/)

## 配套工具

Wireshark · [wireshark-packet-analysis](../wireshark-packet-analysis/) · NotebookLM（按章上传 `chapter-summary.md` 或单节 `*.md`）

## 小节模板

```markdown
# 小节标题
## 核心知识点
## 抓包/实操记录
## 疑问与总结
```
