# 13.5 安全性考虑

> 本章：[chapter-summary.md](./chapter-summary.md#ch13-5) · [ch14 HTTPS](../chapter-14-secure-http/chapter-summary.md)

## 本节核心目标

Digest 在**无信道加密**下的威胁与对策；为何仍需 **HTTPS**。

---

<a id="ch13-5-threats"></a>

## 攻击与防范（简表）

| 威胁 | 说明 | 对策要点 |
|------|------|----------|
| **首部篡改** | Digest 不护全部首部 | **TLS** 或数字签名 |
| **重放** | 偷合法凭证重放 POST | 短效 nonce、绑 IP/时间/ETag |
| **降级攻击** | 中间人删 Digest 逼 Basic | 客户端/代理**只用最强**方案 |
| **词典攻击** | 穷举常见密码 + nonce | 强密码、过期策略 |
| **恶意代理/MITM** | 无加密仍可窃听元数据 | **SSL/HTTPS** |
| **选择明文攻击** | 恶意 nonce 降破解难度 | 必须 **`cnonce`** |
| **存储泄露** | 服务器存 H(A1)，泄露≈密码库泄露 | 同等级保护密码文件 |

---

## 重点结论

Digest 比 Basic 好，但**不能替代 HTTPS**。  
现代生产多：**HTTPS + JWT/OAuth**，纯 Digest 少见。

→ [ch14](../chapter-14-secure-http/chapter-summary.md)

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**第 13 章缺陷清单 = 第 14 章 HTTPS 的动机。**
