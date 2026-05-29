# 11.2 HTTP首部

> 本章：[chapter-summary.md](./chapter-summary.md#ch11-2) · [ch03 首部](../chapter-03-http-message/05-header.md)

## 本节核心目标

评估用 **From / User-Agent / Referer** 做识别的可行性与局限。

---

<a id="ch11-2-fields"></a>

## 核心字段

| 首部 | 内容 | 局限 |
|------|------|------|
| **`From`** | 用户 Email | 浏览器**极少发送**（防垃圾邮件）；爬虫可能带 |
| **`User-Agent`** | 浏览器/OS 版本 | **不能**唯一标识用户；仅做兼容/统计 |
| **`Referer`** | 从哪页链过来 | **非身份**；利于行为/兴趣分析 |

---

## 易错

三者**极易伪造**，区分度低 → **不能**当作可靠认证。

→ [ch09 机器人 UA](../chapter-09-web-robot/02-robot-http.md#ch09-2-headers)

---

## 抓包/实操记录

（待填：DevTools 请求头里是否有 `From`）

---

## 疑问与总结

**首部适合分析，不适合当身份证。**
