# 9.2 机器人的HTTP

> 本章：[chapter-summary.md](./chapter-summary.md#ch09-2) · [ch03 报文/方法](../chapter-03-http-message/chapter-summary.md) · [ch07 条件请求](../chapter-07-cache/08-freshness-revalidation.md)

## 本节核心目标

机器人作为 **HTTP 客户端** 必须正确实现的首部、虚拟主机与条件请求。

---

<a id="ch09-2-headers"></a>

## 9.2.1 识别请求首部

| 首部 | 用途 |
|------|------|
| **`User-Agent`** | 机器人名称/版本 |
| **`From`** | 管理者联系邮箱 |
| **`Accept`** | 可处理的媒体类型 |
| **`Referer`** | 从哪页发现本 URL |

---

<a id="ch09-2-host"></a>

## 9.2.2 虚拟主机与 Host（易错）

**必须**发 **`Host`**（HTTP/1.1）。

无 `Host` → 单 IP 多域名时拿到**默认站点** → URL 与内容**错配**。

→ [ch18 虚拟主机](../chapter-18-web-hosting/chapter-summary.md)

---

<a id="ch09-2-conditional"></a>

## 9.2.3 条件请求

用 **`If-Modified-Since`** / **`If-None-Match`** → 仅更新时拉全量 body（常 **304**）。

---

<a id="ch09-2-response"></a>

## 9.2.4 响应处理

- 正确理解 **200 / 404** 等状态码  
- 解析 HTML **`<meta http-equiv="Refresh">`** 等页内重定向  

---

<a id="ch09-2-ua"></a>

## 9.2.5 User-Agent 导向

站点可能按 UA 返回不同内容；非浏览器 UA 可能收到**错误提示页** → 需容错。

---

## 拓展（预留）

- 反爬：TLS **JA3**、必须执行 **JavaScript**  

---

## 抓包/实操记录

（待填：爬虫请求是否带 `Host:`）

---

## 疑问与总结

**机器人遵守的 HTTP 规则与浏览器同样硬，尤其是 Host。**
