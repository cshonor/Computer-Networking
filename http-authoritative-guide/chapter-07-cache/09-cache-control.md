# 7.9 控制缓存的能力

> 本章：[chapter-summary.md](./chapter-summary.md#ch07-9) · [ch03 首部](../chapter-03-http-message/05-header.md)

## 本节核心目标

掌握服务器/客户端用 **`Cache-Control`** 等指令约束缓存行为。

---

<a id="ch07-9-nostore"></a>

## 7.9.1 no-store 与 no-cache（易错）

| 指令 | 含义 |
|------|------|
| **`no-store`** | **禁止存储**副本；处理完即删（机密数据） |
| **`no-cache`** | 可存，但**提供给客户端前必须先与源站再验证** → 应理解为「**未经再验证禁止用**」 |

---

<a id="ch07-9-maxage"></a>

## 7.9.2 max-age / s-maxage

- **`max-age=N`**：新鲜 **N 秒**  
- **`s-maxage`**：仅**共享（公有）缓存**  
- **`max-age=0`**：每次使用前需刷新  

---

<a id="ch07-9-expires"></a>

## 7.9.3 Expires

绝对过期时间；**不推荐**（时钟问题）。

---

<a id="ch07-9-must-revalidate"></a>

## 7.9.4 must-revalidate

已**陈旧**的副本：**未经源站验证不得提供**。源站不可达 → **`504 Gateway Timeout`**（不能悄悄给旧内容）。

---

<a id="ch07-9-heuristic"></a>

## 7.9.5 试探性过期（Heuristic）

无 `max-age` 且无 `Expires` 时：

**LM-Factor**：新鲜期 ≈ `(现在 - Last-Modified) × 0.2`（文档越久未改越「稳定」）。

无 `Last-Modified` → 保守默认（1h/1d）或 **0** 强制每次验证。

---

<a id="ch07-9-client"></a>

## 7.9.6 客户端指令（请求）

| 指令 | 含义 |
|------|------|
| **`max-stale=N`** | 愿接受过期不超过 N 秒的陈旧内容 |
| **`min-fresh=N`** | 要求至少 N 秒内仍新鲜 |
| **`only-if-cached`** | 只读缓存，**不联系源站** |

浏览器「硬刷新」会附加更严的 `Cache-Control`。

---

## 抓包/实操记录

（待填：响应 `Cache-Control:` 与请求刷新）

---

## 疑问与总结

**no-store ≠ no-cache**；写错一字节语义差很多。
