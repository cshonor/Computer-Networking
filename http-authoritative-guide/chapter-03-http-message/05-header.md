# 3.5 首部

> 本章：[chapter-summary.md](./chapter-summary.md#ch03-5) · [3.2 结构](./02-message-component.md) · [ch15 实体首部](../chapter-15-entity-encoding/chapter-summary.md)

## 本节核心目标

理解 HTTP **首部**作为报文「控制中心」；掌握**通用 / 请求 / 响应 / 实体 / 扩展**五类及转发规则。

---

<a id="ch03-5-classes"></a>

## 一、五类首部

| 类别 | 谁用 | 作用 | 例子 |
|------|------|------|------|
| **通用首部** | 请求、响应均可 | 基本报文信息 | `Date`、`Connection`、`Transfer-Encoding` |
| **请求首部** | 仅请求 | 客户端偏好与能力 | `Accept`、`User-Agent`、`Host` |
| **响应首部** | 仅响应 | 服务器与处理上下文 | `Server`、`Set-Cookie` |
| **实体首部** | 带实体的报文 | 描述**主体**元数据 | `Content-Type`、`Content-Length`、`ETag`、`Last-Modified` |
| **扩展首部** | 非正式标准 | 试验或厂商扩展 | `X-*` 等 |

---

## 二、逻辑脉络

- **通用**：何时、如何传、连接选项  
- **请求**：我能接受什么（`Accept*`）、我是谁、要什么资源  
- **响应**：服务器信息、缓存策略指令  
- **实体**：body 的类型、长度、校验与缓存验证线索  

实体首部与 [3.6 实体](./06-entity.md)、[ch15 编码](../chapter-15-entity-encoding/chapter-summary.md) 紧密相关。

---

## 三、易错

| 点 | 说明 |
|----|------|
| **扩展首部** | 代理/客户端**不认识也必须接受**并**原样转发**（除非 hop-by-hop 禁止） |
| **Connection** | 列在其中的首部为**逐跳**；不列的可能端到端 |

---

## 拓展（预留）

- 内容协商：`Accept-Language`、`Accept-Charset`  
- **CORS** 预检与自定义首部（→ [ch14 安全 HTTP](../chapter-14-secure-http/chapter-summary.md)）

---

## 抓包/实操记录

（待填：同一响应中 General / Response / Entity 分组）

---

## 疑问与总结

首部是 **名: 值** 列表；**空行** 后才是 body。
