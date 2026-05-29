# 14.1 保护HTTP的安全

> 本章：[chapter-summary.md](./chapter-summary.md#ch14-1) · 全书：[../README.md](../README.md) · [ch12/ch13 认证](../chapter-12-basic-auth/chapter-summary.md)

## 本节核心目标

理解 **HTTPS** 要满足的**安全属性**及其在协议栈中的位置。

---

<a id="ch14-1-needs"></a>

## 安全 HTTP 的需求

| 属性 | 说明 |
|------|------|
| **服务器认证** | 确认对端是真站点 |
| **客户端认证** | 确认用户（可选） |
| **完整性** | 防篡改 |
| **加密** | 防窃听 |
| **效率** | 可接受的性能 |
| **普适性** | 广泛实现 |
| **可管理** | 跨地域、可扩展 |

---

<a id="ch14-1-https"></a>

## HTTPS 架构

```text
HTTP 报文
   ↓
TLS/SSL 密码层  ← HTTPS 插入此处
   ↓
TCP（通常 :443）
```

**不是**把明文 HTTP 直接交给 TCP。

---

## 拓展（预留）

- Basic/Digest（应用层）vs **TLS（信道）** 防 MITM 的差异  

---

## 抓包/实操记录

（待填：Wireshark「TLS」解密或只看密文）

---

## 疑问与总结

**认证在 ch12/13；保密与身份在 TLS。**
