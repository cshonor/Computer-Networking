# 10.1 HTTP发展中存在的问题

> 本章：[chapter-summary.md](./chapter-summary.md#ch10-1) · 全书：[../README.md](../README.md) · [ch04 连接](../chapter-04-connection-management/chapter-summary.md)

## 本节核心目标

理解 HTTP/1.x 在 Web 爆炸后暴露的**架构局限**（为何需要下一代思路）。

---

<a id="ch10-1-pain"></a>

## 四大痛点

| 问题 | 说明 |
|------|------|
| **复杂性增加** | 缓存、持久连接、内容协商等不断**打补丁**，协议臃肿 |
| **可扩展性差** | 难在不破坏兼容的前提下加新特性 |
| **性能瓶颈** | 依赖 **TCP** 握手、短连接 RTT → [ch04](../chapter-04-connection-management/01-connection-desire.md) |
| **传输耦合** | 绑死 TCP/IP，难迁到无线、嵌入式等栈 |

---

## 拓展（预留）

- **HTTP/2**：二进制分帧、多路复用，缓解 HOL  
- **HTTP/3**：**QUIC（UDP）**，连接迁移、0-RTT  

→ 本书 HTTP-NG 是**历史草案**；现代答案在 2/3。

---

## 抓包/实操记录

（待填：HTTP/1.1 多对象页面的连接数）

---

## 疑问与总结

**HTTP/1.1 能跑，但「快、易扩展、少耦合」都不够。**
