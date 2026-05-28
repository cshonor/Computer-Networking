# 第 2 章 URL 与资源

> 全书：[../README.md](../README.md) · 后继：[ch03 HTTP 报文](../chapter-03-http-message/chapter-summary.md) · 前置：[ch01](../chapter-01-http-overview/chapter-summary.md)

## 本章概述

**URL** 如何命名与定位 Web 资源：语法九组件、相对/自动扩展、字符编码、常见方案，以及 **URN** 展望。HTTP 请求行中的 URL 见 [ch03 §3.2](../chapter-03-http-message/02-message-component.md)。

> **目录说明**：`03-short-url-resolve.md` 文件名保留生成器命名，内容为 **§2.4 字符编码**；**§2.3 快捷方式** 拆在 `04`+`05`。

---

## 知识框架

```text
2.1 URL = 因特网资源地址（URI 子集）
2.2 九组件：scheme · host · port · path · ;params · ?query · #frag
2.3 相对 URL + 浏览器自动扩展（04/05）
2.4 百分号编码与安全字符集（03 文件）
2.5 常见 scheme：http/https/ftp…（合在 02 末尾）
2.6 URL 绑位置 → PURL/URN
```

---

## 重点与难点

| 节 | 重点 | 易错 |
|----|------|------|
| **2.1** | URL = 协议+主机+路径 | 与 URN「只命名不定位」对比 |
| **2.2** | 必备 scheme/host/path；**# 不发服务器** | http **80**；scheme 大小写无关 |
| **2.3** | Base URL + 相对解析 | 代理下自动扩展可能失效 |
| **2.4** | `%20` 等转义 | encodeURI vs encodeURIComponent |
| **2.5** | https=443 | news 无 host |
| **2.6** | 死链与持久命名 | URN 落地难 |

---

## 实操要点

- 地址栏拆解一条 `https://…?…#…`  
- 同一页面改 `<base href>` 观察相对链接  
- 对比 `encodeURI` / `encodeURIComponent` 输出

---

## 小节索引

| 书节 | 文件 | 链接 |
|------|------|------|
| <a id="ch02-1"></a> **2.1** | `01-identifier.md` | [浏览因特网资源](./01-identifier.md) |
| <a id="ch02-2"></a> **2.2** | `02-url-syntax.md` | [九组件](./02-url-syntax.md#ch02-2-format) · [方案](./02-url-syntax.md#ch02-2-schemes) |
| <a id="ch02-3"></a> **2.3** | `04`+`05` | [相对 URL](./04-relative-url.md) · [自动扩展](./05-url-shortcut.md) |
| <a id="ch02-4"></a> **2.4** | `03-short-url-resolve.md` | [字符编码](./03-short-url-resolve.md#ch02-4-encoding) |
| <a id="ch02-5"></a> **2.5** | （在 02 内） | [常见方案](./02-url-syntax.md#ch02-2-schemes) |
| <a id="ch02-6"></a> **2.6** | `06-urn-future.md` | [URN/PURL](./06-urn-future.md) |

---

## 一句话过章

**URL 拆九段发请求；相对链接靠 Base；特殊字符要 % 编码；# 只给浏览器；跨网后交给 HTTP。**
