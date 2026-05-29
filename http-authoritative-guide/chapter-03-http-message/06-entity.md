# 3.6 实体

> 本章：[chapter-summary.md](./chapter-summary.md#ch03-6) · 详 [ch15 实体和编码](../chapter-15-entity-encoding/chapter-summary.md)

## 本节核心目标

在 ch03 报文框架下理解 **实体（entity）**：可选的**实体首部 + 实体主体**。

---

<a id="ch03-6-entity"></a>

## 与报文的关系

```text
起始行
报文首部
空行
├─ 实体首部（Content-Type、Content-Length…）
├─ 空行（若有实体首部块）
└─ 实体主体（body 字节）
```

**报文 = 箱子；实体 = 货物** → [15.1](../chapter-15-entity-encoding/01-entity-cargo.md)

---

## 必记实体首部（入门）

| 首部 | 作用 |
|------|------|
| **`Content-Type`** | MIME 类型 |
| **`Content-Length`** | 主体长度 → [15.2](../chapter-15-entity-encoding/02-content-length.md) |
| **`Content-Encoding`** | 如 gzip → [15.5](../chapter-15-entity-encoding/05-content-encoding.md) |

缓存/验证：`ETag`、`Last-Modified` → [15.8](../chapter-15-entity-encoding/08-validators-freshness.md)、[ch07](../chapter-07-cache/chapter-summary.md)

---

## 抓包/实操记录

（待填：响应里 Content-Type 与 body 大小）

---

## 疑问与总结

**ch03 只建立概念；编码、定长、范围见第 15 章。**
