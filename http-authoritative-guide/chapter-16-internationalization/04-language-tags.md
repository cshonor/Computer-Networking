# 16.4 语言标记与HTTP

> 本章：[chapter-summary.md](./chapter-summary.md#ch16-4) · [16.1 Accept-Language](./01-intl-content-support.md#ch16-1-client)

## 本节核心目标

掌握 **`Content-Language` / `Accept-Language`** 及 **RFC 3066** 风格标记语法。

---

<a id="ch16-4-usage"></a>

## 16.4.1–16.4.2 应用场景

| 首部 | 说明 |
|------|------|
| **`Content-Language`** | 实体受众语言；可多值（`mi, en`）；非仅文本（音频、电影） |
| **`Accept-Language`** | 客户端偏好 + **`q`** |

例：英语写的日语教材 → 只标 **`en`**（受众语言，非内容源语言）。

---

<a id="ch16-4-syntax"></a>

## 16.4.3–16.4.10 标记语法

**主标记-子标记**（`-` 分隔），大小写不敏感；惯例：

- **语言小写**：`en`  
- **地区大写**：`en-US`、`fr-FR`、`zh-CN`

| 首段 | 含义 |
|------|------|
| 2 字母 | ISO 639 |
| 3 字母 | ISO 639-2 |
| `i` | IANA 注册 |
| `x` | 私有 |

第二段常为 **ISO 3166** 国家（`US`、`CN`）。

---

## 拓展（预留）

- HTML **`lang`** 与 `Content-Language` 优先级  

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**语言标记描述「给谁看」，不是文件里写了哪国字。**
