# 第 3 章 HTTP 报文

> 全书：[../README.md](../README.md) · 前置：[ch01](../chapter-01-http-overview/chapter-summary.md) · [ch02 URL](../chapter-02-url-and-resource/chapter-summary.md) · 后继：[ch04 连接](../chapter-04-connection-management/chapter-summary.md)

## 本章概述

HTTP 报文如何在应用之间**流动**（3.1），**长什么样**（3.2），以及**方法、状态码、首部**如何驱动事务（3.3～3.5）。实体 body 与编码见 **3.6**、[ch15](../chapter-15-entity-encoding/chapter-summary.md)。

---

## 知识框架

```text
3.1 流向：流入/流出 · 上游/下游（随报文反转）
3.2 结构：起始行 + 首部 + 空行 + 可选 body
3.3 方法：GET/HEAD/PUT/POST/TRACE/OPTIONS/DELETE + 扩展
3.4 状态码：1xx～5xx · 304/301/302 · 100 Continue 陷阱
3.5 首部：通用/请求/响应/实体/扩展
3.6 实体：实体首部 + body → 详 ch15
```

---

## 重点与难点

| 节 | 重点 | 易错 |
|----|------|------|
| **3.1** | 请求/响应都**向下游**；上下游看**发送关系** | 不能用「发给谁」固定上下游 |
| **3.2** | 三段式；首部以**空行**结束 | 版本号**不能当小数**比较 |
| **3.3** | HEAD 无 body；PUT 整资源替换 | 未知方法 → 501 |
| **3.4** | 五大类；304 与缓存 | 100 Continue 提前结束连接 |
| **3.5** | 五类首部分工 | 扩展首部须原样转发 |

---

## 实操要点

- Wireshark 过滤 `http`；对照 [09 章 HTTP](../../../wireshark-packet-analysis/chapter-09-application-layer-proto/03-http-protocol.md)  
- 抓一条 **GET + 200**、一条 **304**、一条 **302** 对比起始行与首部

---

## 小节索引

| 节 | 链接 |
|----|------|
| <a id="ch03-1"></a> **3.1 报文流** | [01-message-flow.md](./01-message-flow.md) · [上下游](./01-message-flow.md#ch03-1-up-down) |
| <a id="ch03-2"></a> **3.2 组成部分** | [02-message-component.md](./02-message-component.md) · [三段结构](./02-message-component.md#ch03-2-structure) |
| <a id="ch03-3"></a> **3.3 方法** | [03-method.md](./03-method.md) |
| <a id="ch03-4"></a> **3.4 状态码** | [04-status-code.md](./04-status-code.md) · [五大类](./04-status-code.md#ch03-4-classes) |
| <a id="ch03-5"></a> **3.5 首部** | [05-header.md](./05-header.md) · [五类](./05-header.md#ch03-5-classes) |
| <a id="ch03-6"></a> **3.6 实体** | [06-entity.md](./06-entity.md) · [ch15 详](../chapter-15-entity-encoding/chapter-summary.md) |

---

## 一句话过章

**报文向下游流；结构是起始行+首部+body；方法定动作，状态码定结果，首部定细节。**
