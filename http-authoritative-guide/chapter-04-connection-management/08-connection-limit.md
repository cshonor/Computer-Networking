# 4.8 连接限制与设置

> 本章：[chapter-summary.md](./chapter-summary.md#ch04-8) · [4.4 并行](./04-parallel-connection.md) · [4.5 持久](./05-persistent-connection.md)

## 本节核心目标

归纳 **客户端与规范** 对连接数量的常见上限（本书 + 实践）。

---

<a id="ch04-8-limits"></a>

## 一、规范与浏览器侧

| 限制类型 | 典型值 | 出处/说明 |
|----------|--------|-----------|
| **HTTP/1.1 持久连接** | 对同一服务器/代理约 **2 条** | RFC 建议，防单用户占满服务器 |
| **并行连接（每主机）** | 约 **4～6** | 各浏览器实现不同（历史常引 4） |
| **总连接数** | 有上限 | 保护客户端内存与服务器 FD |

---

## 二、与性能策略的关系

```text
少量并行（4?） × 每条持久（≤2?） ≈ 同站并发事务有上限
```

- 对象很多时仍会**排队** → 推动 **HTTP/2 多路复用**、[域名分片](https://developer.mozilla.org/en-US/docs/Glossary/Domain_sharding)（已过时实践）等  

---

## 拓展（预留）

- `Max-Connections`、服务器 `worker_connections`  
- HTTP/2 `SETTINGS_MAX_CONCURRENT_STREAMS`

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**连接不是越多越好**；规范故意压低默认值以保护 Web 生态。
