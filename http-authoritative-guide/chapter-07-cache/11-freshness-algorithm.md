# 7.11 详细算法

> 本章：[chapter-summary.md](./chapter-summary.md#ch07-11) · [7.8 新鲜](./08-freshness-revalidation.md)

## 本节核心目标

理解规范中 **Age（使用期）** 与 **freshness_lifetime（新鲜生存期）** 的比较逻辑。

---

<a id="ch07-11-fresh"></a>

## 7.11.1 核心判定

```text
足够新鲜  ⇔  age < freshness_lifetime
```

---

<a id="ch07-11-age"></a>

## 7.11.2–7.11.3 使用期（Age）

组成：

- 源站发出后在网络/中间节点停留  
- **本地缓存**停留时间  

**表面使用期** = `响应获取时间 - Date`（取 `max(0, …)` 防时钟偏差）

**`Age` 首部**：HTTP/1.1 每跳累加停留时间。

**保守估计**：在 `apparent_age` 与 `Age` 中取大，再加请求-响应网络耗时估计 → 偏大、更安全。

```text
age = 到达缓存时的使用期 + 本地停留时间
```

---

<a id="ch07-11-lifetime"></a>

## 7.11.4–7.11.5 新鲜生存期

优先级（简）：

1. **`max-age` / `s-maxage`**  
2. **`Expires - Date`**  
3. **试探性（LM-Factor）** + 全局 min/max 夹限  

最后再用客户端请求的 **`max-stale` / `min-fresh` / `max-age`** 等**收紧或放宽**。

---

## 抓包/实操记录

（待填：计算 `Age` 与 `max-age` 是否仍新鲜）

---

## 疑问与总结

**实现缓存 = 实现这两套时钟算术。**
