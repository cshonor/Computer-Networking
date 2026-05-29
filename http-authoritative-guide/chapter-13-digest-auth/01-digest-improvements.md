# 13.1 摘要认证的改进

> 本章：[chapter-summary.md](./chapter-summary.md#ch13-1) · 全书：[../README.md](../README.md) · [ch12 Basic](../chapter-12-basic-auth/chapter-summary.md)

## 本节核心目标

理解 Digest 相对 Basic 的核心：**不传密码**，用**摘要 + nonce** 防重放。

---

<a id="ch13-1-digest"></a>

## 13.1.1 用摘要保护密码

| Basic | Digest |
|-------|--------|
| 传 `user:pass`（Base-64） | 传**密码摘要指纹** |
| 网络可见可解码 | 服务器存密码（或 H(A1)）本地比对 |

箴言：**绝不通过网络发送密码**。

---

<a id="ch13-1-hash"></a>

## 13.1.2 单向摘要

**单向散列** `H(d)`：任意输入 → **定长**输出；难从摘要反推密码。

书中常用 **MD5**（128 bit → 32 个十六进制字符）。  
→ 现代：MD5 已不推荐用于新设计；概念仍考 **nonce + 哈希**。

---

<a id="ch13-1-nonce"></a>

## 13.1.3 随机数（nonce）防重放

仅藏密码不够：攻击者可**重放**旧摘要。

服务器在质询里发 **nonce**（随时间/每次变化）→ 客户端必须把 **nonce 混入**摘要计算 → nonce 变则旧摘要失效。

---

<a id="ch13-1-handshake"></a>

## 13.1.4 四步握手

1. 服务器：`WWW-Authenticate`（含 **nonce**、算法、realm、qop 等）  
2. 客户端：选算法，用密码 + nonce 等算**摘要**  
3. 客户端：`Authorization`（含 digest、nc、cnonce…）  
4. 服务器：验证通过 → `200`；可选 **`Authentication-Info`**

---

## 拓展（预留）

- **Salt**、bcrypt/Argon2 抗彩虹表  

---

## 抓包/实操记录

（待填：401 响应里 `WWW-Authenticate: Digest`）

---

## 疑问与总结

**Digest 解决 Basic 的「明文/简单重放」，不是万能加密。**
