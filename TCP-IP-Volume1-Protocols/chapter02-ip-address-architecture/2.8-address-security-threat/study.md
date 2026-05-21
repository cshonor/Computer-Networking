# 2.8 与 IP 地址相关的攻击

> 章级精读：[../study.md#ch02-8](../study.md#ch02-8) · 安全章：[ch18](../../chapter18-network-security/study.md)

## 本节核心目标

认识 **IP 欺骗** 根因与边界防护思路。

---

## IP 欺骗 (IP Spoofing)

- 网络层**不原生校验**源 IP 真实性 → 攻击者可伪造源地址。
- 后果：误导接收方、**反射型 DDoS**（放大攻击把回复打向受害者）。

---

## 防护（主流）

| 手段 | 说明 |
|------|------|
| **BCP 38 / 入站过滤** | 边界丢弃**源地址不属于本 AS/站点** 的出站包 |
| **uRPF** | 反向路径转发检查（与路由表一致性） |
| 应用层 | 不单独依赖 IP 做身份（TLS、令牌） |

→ 与 [ch01 信任模型](../../chapter01-overview/study.md#ch01-std-security)、[ch18](../../chapter18-network-security/study.md) 衔接。
