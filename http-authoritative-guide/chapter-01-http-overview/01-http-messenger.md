# 1.1 HTTP——因特网的多媒体信使

> 本章：[chapter-summary.md](./chapter-summary.md#ch01-1) · 全书：[../README.md](../README.md)

## 本节核心目标

理解 HTTP 在万维网中的角色：**应用层**上传递多媒体对象的**公共语言**。

---

## 一、通信基础

- **Web 浏览器、服务器、Web 应用** 都通过 **HTTP** 互通信  
- HTTP 位于 **OSI/TCP-IP 应用层**（之下是 TCP、IP）→ [1.6](./06-connection.md)

---

## 二、核心功能

| 能力 | 说明 |
|------|------|
| **多格式** | 文本、图片、音视频等 |
| **可靠传输** | 依赖下层 **TCP** 提供无差错、按序字节流（HTTP 本身「尽力」语义见 ch01 与 ch03） |

---

## 拓展（预留）

- 流媒体、WebRTC 与 HTTP 的分工  
- 与 [TCP/IP 卷1 ch01](../../TCP-IP-Volume1-Protocols/chapter01-overview/study.md) 沙漏模型对照

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**HTTP = 应用层协议**；真正「可靠字节流」主要靠 **TCP**。
