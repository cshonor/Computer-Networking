# 16.6 其他需要考虑的地方

> 本章：[chapter-summary.md](./chapter-summary.md#ch16-6)

## 本节核心目标

国际化在 **首部、日期、DNS** 等周边的兼容风险。

---

<a id="ch16-6-headers"></a>

## 16.6.1 首部与非法字节

HTTP 首部须 **US-ASCII**。`>127` 的字节可能导致老旧 `ctype` **越界/崩溃** → 必须边界检查。

---

<a id="ch16-6-date"></a>

## 16.6.2 日期格式

规范要求 **GMT** 英文月份；仍有服务器发**本地化月份名** → 客户端应**容错**不崩溃。

---

<a id="ch16-6-dns"></a>

## 16.6.3 DNS 与 IDN

早期 DNS **仅 ASCII**。

**现代**：**Punycode（RFC 3492）** 将 Unicode 域名转为 **`xn--`** ASCII → 浏览器 IDN 显示中文、解析用 Punycode。

---

## 抓包/实操记录

（待填：浏览器地址栏中文域 vs DNS 查询名）

---

## 疑问与总结

**国际化不止 body；首部、URI、主机名都要 ASCII 安全。**
