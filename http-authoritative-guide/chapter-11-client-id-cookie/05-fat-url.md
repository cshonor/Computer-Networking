# 11.5 胖URL

> 本章：[chapter-summary.md](./chapter-summary.md#ch11-5) · [ch02 URL](../chapter-02-url-and-resource/chapter-summary.md) · [ch07 缓存](../chapter-07-cache/01-redundant-transfer.md)

## 本节核心目标

理解 **胖 URL（Fat URL）** 如何在 URL 里塞状态及其**致命缺点**。

---

<a id="ch11-5-mechanism"></a>

## 机制

服务器在返回页面的**每个链接**里嵌入状态，例如：

```text
/ref=gr_gifts/002-1145265
```

用户点链 → 服务器从 URL 读出会话/用户 ID。

---

<a id="ch11-5-pain"></a>

## 四大痛点

| # | 问题 |
|---|------|
| 1 | **丑陋**，难读难记 |
| 2 | **不能安全分享** — 别人打开 = 偷/改你的会话（如购物车） |
| 3 | **破坏缓存** — 每用户 URL 唯一 → **公共缓存失效** → [ch07](../chapter-07-cache/chapter-summary.md) |
| 4 | **易丢状态** — 离站、改地址栏、关浏览器即断链 |

→ 重定向胖 URL [ch20](../chapter-20-redirect-load-balance/chapter-summary.md)

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**胖 URL 是 Cookie 出现前的权宜之计；今天应少用。**
