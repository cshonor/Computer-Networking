# 1.5 报文

> 本章：[chapter-summary.md](./chapter-summary.md#ch01-5) · [ch03 报文详解](../chapter-03-http-message/chapter-summary.md)

## 本节核心目标

了解 HTTP **报文**为（ mostly ）**文本行**结构及**三段式**组成。

---

<a id="ch01-5-structure"></a>

## 一、基本特性

- 由**一行行字符串**构成，**纯文本**为主（便于 Telnet/curl 调试）  
- **请求报文** vs **响应报文**

---

## 二、三段式结构

```text
┌─ 起始行 ───── 请求：方法 URL 版本 / 响应：版本 状态码 原因
├─ 首部 ─────── 名: 值（多行）
├─ 空行 ─────── 仅 CRLF，首部结束
└─ 主体 body ── 可选；可二进制
```

| 段 | 请求例 | 响应例 |
|----|--------|--------|
| **起始行** | `GET /index.html HTTP/1.1` | `HTTP/1.1 200 OK` |
| **首部** | `Host: example.com` | `Content-Type: text/html` |
| **主体** | POST 表单数据 | HTML、图片字节 |

---

## 易错

| 点 | 说明 |
|----|------|
| **首部必须是文本** | 行格式、空行分隔 |
| **body 可任意二进制** | 图片/视频靠 `Content-Type` 解释 |

→ 深读 [ch03 §3.2](../chapter-03-http-message/02-message-component.md)

---

## 抓包/实操记录

（待填：Wireshark Follow HTTP Stream）

---

## 疑问与总结

**空行**是首部与 body 的分界；漏空行是常见解析 bug。
