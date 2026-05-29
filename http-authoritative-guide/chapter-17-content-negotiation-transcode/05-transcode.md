# 17.5 转码

> 本章：[chapter-summary.md](./chapter-summary.md#ch17-5) · [ch15 Accept-Encoding](../chapter-15-entity-encoding/05-content-encoding.md)

## 本节核心目标

当无完全匹配变体时，通过 **转码（Transcoding）** 即时生成可接受表示。

---

<a id="ch17-5-format"></a>

## 17.5.1 格式转换

一种格式 → 另一种（HTML → WML；彩图 → 低分辨率黑白）。  
常由 **`Accept`** / **`User-Agent`** 触发。

---

<a id="ch17-5-synthesis"></a>

## 17.5.2 信息综合

提取/缩减：生成目录、去广告、关键词归类。

---

<a id="ch17-5-injection"></a>

## 17.5.3 内容注入

动态追加：定向广告、统计探针（tracking pixel）。

---

<a id="ch17-5-static-vs"></a>

## 17.5.4 转码 vs 静态预生成

| 静态预生成 | 转码 |
|------------|------|
| 存储、同步更新成本高 | **按需**计算，有延迟 |
| 动态广告难预生成 | 适合边缘即时处理 |

**实践**：转码下放**代理/边缘 CDN**（Edge Workers、动态 WebP/AVIF）。

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**转码改变 body 语义；须与缓存/Vary 策略一致。**
