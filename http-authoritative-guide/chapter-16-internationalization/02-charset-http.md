# 16.2 字符集与HTTP

> 本章：[chapter-summary.md](./chapter-summary.md#ch16-2) · [ch15 Content-Type](../chapter-15-entity-encoding/04-media-type.md)

## 本节核心目标

掌握 **`charset`** 含义、MIME 标记、声明方式与 **Accept-Charset**。

---

<a id="ch16-2-charset"></a>

## 16.2.1 charset 是什么

`charset` 命名一套**二进制 ↔ 字符**的算法（如 `iso-8859-6`、`utf-8` 可变长）。

---

<a id="ch16-2-two-step"></a>

## 16.2.2 两步解码

1. **数据 → 字符代码**（编码方案）  
2. **代码 → 抽象字符**（编码字符集）  

字形由本地字体渲染，与 HTTP 无关。

---

<a id="ch16-2-wrong"></a>

## 16.2.3 字符集不对就乱码（易错）

同一字节在不同 charset 下映射不同字符 → ** Mojibake**。

---

<a id="ch16-2-mime"></a>

## 16.2.4 标准 MIME charset

IANA 注册：`us-ascii`、`iso-8859-1`（HTML 历史默认）、`windows-1252` 等。

---

<a id="ch16-2-declare"></a>

## 16.2.5 如何声明

| 优先级 | 方式 |
|--------|------|
| **首选** | `Content-Type: text/html; charset=utf-8` |
| 降级 | HTML `<META HTTP-EQUIV="Content-Type" … charset=…>` |
| 全无 | 浏览器常假设 **iso-8859-1** |

→ 勿依赖 META 做缓存控制 [ch07](../chapter-07-cache/10-configure-cache.md)

---

<a id="ch16-2-accept"></a>

## 16.2.6 Accept-Charset

客户端限制可接受的 charset；**无**对应 `Content-Charset` 响应首部，结果只在 **`Content-Type` 参数**里。

---

## 抓包/实操记录

（待填：UTF-8 页面故意用错 charset 看乱码）

---

## 疑问与总结

**charset 是解码说明书，不是 HTTP 正文的一部分。**
