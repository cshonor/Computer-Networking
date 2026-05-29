# 15.4 媒体类型和字符集

> 本章：[chapter-summary.md](./chapter-summary.md#ch15-4) · [ch01 MIME](../chapter-01-http-overview/03-resource.md#ch01-3-mime) · [ch16 国际化](../chapter-16-internationalization/chapter-summary.md)

## 本节核心目标

掌握 **`Content-Type`**、**charset**、**multipart** 与范围多部分响应。

---

<a id="ch15-4-mime"></a>

## MIME 与 Content-Type

`type/subtype`，描述**原始**实体类型（不因 Content-Encoding 改变）。

例：`text/html`、`image/jpeg`

---

<a id="ch15-4-charset"></a>

## 15.4.1 字符集

```http
Content-Type: text/html; charset=iso-8859-4
```

→ 详 [ch16](../chapter-16-internationalization/01-charset-encoding.md)

---

<a id="ch15-4-multipart"></a>

## 15.4.2–15.4.3 多部分（Multipart）

由 **boundary** 分隔多个部分。

| 类型 | 用途 |
|------|------|
| **`multipart/form-data`** | 表单 + **文件上传** |
| **`multipart/byteranges`** | 多段范围响应（每段自有 Type/Range） |

---

## 抓包/实操记录

（待填：上传文件的 multipart 边界）

---

## 疑问与总结

**Content-Type 说「解码后是什么」；gzip 只影响 Content-Encoding。**
