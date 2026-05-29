# 15.8 验证码和新鲜度

> 本章：[chapter-summary.md](./chapter-summary.md#ch15-8) · [ch07 缓存新鲜](../chapter-07-cache/08-freshness-revalidation.md)

## 本节核心目标

**新鲜度指令**与**强/弱验证码**、条件请求。

---

<a id="ch15-8-fresh"></a>

## 15.8.1 新鲜度控制

| 首部 | 说明 |
|------|------|
| **`Expires`** | 绝对时间（时钟敏感） |
| **`Cache-Control`** | `max-age`、`s-maxage`、`no-cache`、`must-revalidate` 等 — **优先** |

---

<a id="ch15-8-validators"></a>

## 15.8.2 验证码

| 类型 | 例子 | 特点 |
|------|------|------|
| **弱** | `Last-Modified`（秒级）、`W/"..."` ETag | 语义大变才变 |
| **强** | **ETag** | 一字节变则变 |

条件请求：

- **`If-Modified-Since`**  
- **`If-None-Match`** → 不匹配则 **304**

---

## 抓包/实操记录

（待填：304 + ETag）

---

## 疑问与总结

**ch07 算法细节；本节强调实体首部角色。**
