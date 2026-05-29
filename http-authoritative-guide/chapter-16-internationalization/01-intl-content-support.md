# 16.1 HTTP对国际性内容的支持

> 本章：[chapter-summary.md](./chapter-summary.md#ch16-1) · 全书：[../README.md](../README.md) · [ch17 内容协商](../chapter-17-content-negotiation-transcode/chapter-summary.md)

## 本节核心目标

理解 HTTP 如何传输**任意语言**的二进制实体，以及**声明/协商**字符集与语言。

---

<a id="ch16-1-content"></a>

## 内容无关性

HTTP 实体主体 = **二进制容器**，可承载任何语言内容。

---

<a id="ch16-1-server"></a>

## 服务器声明

| 信息 | 首部 |
|------|------|
| **字符集** | `Content-Type: …; charset=utf-8` |
| **语言** | **`Content-Language`** |

→ [16.2](./02-charset-http.md)、[16.4](./04-language-tags.md)

---

<a id="ch16-1-client"></a>

## 客户端偏好

| 首部 | 作用 |
|------|------|
| **`Accept-Charset`** | 支持的字符集 |
| **`Accept-Language`** | 理解的语言及优先级 |

**质量因子 `q`**：

```http
Accept-Language: fr, en;q=0.8
```

首选法语，其次英语 → [ch17](../chapter-17-content-negotiation-transcode/01-content-negotiation.md)

---

## 抓包/实操记录

（待填：响应 Content-Language / Accept-Language）

---

## 疑问与总结

**HTTP 不传「语言」，传字节 + 元数据标签。**
