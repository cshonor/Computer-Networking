# 1.7 协议版本

> 本章：[chapter-summary.md](./chapter-summary.md#ch01-7) · [ch10 HTTP-NG](../chapter-10-http-ng/chapter-summary.md)

## 本节核心目标

梳理 HTTP **版本演进**及本书重点（**HTTP/1.1**）。

---

<a id="ch01-7-versions"></a>

## 版本对照

| 版本 | 时期/地位 | 要点 |
|------|-----------|------|
| **HTTP/0.9** | 1991 原型 | 仅 **GET**；无 MIME、无首部、无版本号 |
| **HTTP/1.0** | 首个普及 | 版本号、首部、扩展方法、多媒体 |
| **HTTP/1.0+** | 90 年代非官方 | 厂商扩展（如 **keep-alive**） |
| **HTTP/1.1** | **本书主线** | 修正语义、性能、复杂应用支持 |

---

## 现代延伸（预留）

| 版本 | 特征 |
|------|------|
| **HTTP/2** | 二进制分帧、多路复用 → [ch10](../chapter-10-http-ng/chapter-summary.md) |
| **HTTP/3** | 基于 **QUIC**（UDP 上） |

起始行里常有：`HTTP/1.1` → [ch03](../chapter-03-http-message/02-message-component.md)

---

## 抓包/实操记录

（待填：响应/请求行里的版本字符串）

---

## 疑问与总结

**0.9 几乎考古**；生产默认按 **1.1** 学，再叠 2/3。
