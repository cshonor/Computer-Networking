# 17.4 透明协商

> 本章：[chapter-summary.md](./chapter-summary.md#ch17-4) · [ch07 缓存](../chapter-07-cache/chapter-summary.md)

## 本节核心目标

理解代理缓存保存**多变体**、**`Vary`** 首部及匹配逻辑。

---

<a id="ch17-4-alternate"></a>

## 缓存与备用候选（Alternate）

代理可为同一 URL 存**多份变体**。  
收到请求时须用与源站相同的逻辑匹配 **Accept\*** 等，不能把法语页发给要西班牙语的用户。

---

<a id="ch17-4-vary"></a>

## 17.4.2 Vary 首部

```http
Vary: User-Agent, Accept-Language
```

告知缓存：此响应依赖哪些**请求首部**计算。

**新请求**须 URL + 常规匹配 + **`Vary` 所列首部值与缓存键完全一致**，否则**回源**。

---

## 易错

`Vary: User-Agent` 过细 → **命中率暴跌**（每 UA 一变体）。

---

## 抓包/实操记录

（待填：响应 `Vary:` 字段）

---

## 疑问与总结

**Vary = 告诉缓存「别只按 URL 命中」。**
