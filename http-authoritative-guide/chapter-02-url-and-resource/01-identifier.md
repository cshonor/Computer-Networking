# 2.1 浏览因特网资源

> 本章：[chapter-summary.md](./chapter-summary.md#ch02-1) · 全书：[../README.md](../README.md) · 后继：[3.2 报文](../chapter-03-http-message/02-message-component.md)

## 本节核心目标

理解 **URL（统一资源定位符）** 是因特网资源的**标准化命名与寻址**机制。

---

## 一、URL 的作用

因特网像不断扩张的「城市」，**URL = 每个资源的精确地址**：

- 资源**叫什么**（路径、查询等）  
- **用什么协议**访问（http、https…）  
- **去哪台主机**取（主机名、端口）

应用程序靠 URL **查找并获取** Web 资源。

---

## 二、与 URI 的关系（拓展）

| 概念 | 说明 |
|------|------|
| **URI** | 统一资源**标识符**（更广） |
| **URL** | URI 的子集，强调**定位**（如何访问） |
| **URN** | 持久**名称**，不绑死位置 → [2.6](./06-urn-future.md) |

在协议栈中，URL 是 HTTP 等应用层的**入口键**。

---

## 拓展（预留）

- URL 在 DNS、TCP 连接、HTTP 请求行中的依次展开  
- 与 [ch03 起始行](../chapter-03-http-message/02-message-component.md) 中 request-URL 的对应

---

## 抓包/实操记录

（待填：浏览器地址栏 URL → DevTools 里实际请求的 URL）

---

## 疑问与总结

**URL 定位资源当前位置**；移动资源会导致**死链**——引出 URN/PURL。
