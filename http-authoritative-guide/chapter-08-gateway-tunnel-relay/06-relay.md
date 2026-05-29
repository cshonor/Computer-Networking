# 8.6 中继

> 本章：[chapter-summary.md](./chapter-summary.md#ch08-6) · [ch04 §4.3 Connection 逐跳](../chapter-04-connection-management/03-http-connection.md#ch04-3-connection-hdr)

## 本节核心目标

理解 **HTTP 中继（Relay）** 与规范代理的差异，以及 **Keep-Alive 死锁**。

---

<a id="ch08-6-define"></a>

## 一、定义

**简化版代理**：只正确处理连接建立，之后对字节**盲目转发**，**不完全遵循 HTTP**。

---

<a id="ch08-6-deadlock"></a>

## 二、盲中继 + Keep-Alive 死锁（必背）

```text
1. 客户端 → 中继：请求带 Connection: Keep-Alive（逐跳）
2. 中继不懂，原样 → 源站
3. 源站以为中继要持久连接，回 Keep-Alive，保持打开
4. 中继转响应给客户端；客户端以为持久，中继不知道
5. 客户端在同一连接发第 2 个请求
   中继：以为事务结束，等关连接
   源站：等中继发数据
   → 死锁挂起
```

**根因**：未删除 **`Connection`** 及所列逐跳首部 → [ch04](../chapter-04-connection-management/03-http-connection.md)、[ch06](../chapter-06-proxy/chapter-summary.md)

---

## 三、实践建议

| 环境 | 建议 |
|------|------|
| 生产 | 用**完整 HTTP 代理**（Nginx、Squid 等） |
| 盲中继 | **极谨慎**，易互操作故障 |

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**中继省实现，付互操作代价；Connection 必须逐跳处理。**
