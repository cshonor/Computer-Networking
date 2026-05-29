# 12.3 基本认证的安全缺陷

> 本章：[chapter-summary.md](./chapter-summary.md#ch12-3) · [ch13 摘要认证](../chapter-13-digest-auth/chapter-summary.md) · [ch14 HTTPS](../chapter-14-secure-http/chapter-summary.md)

## 本节核心目标

认清 Basic 的**五大缺陷**及**适用场景**（必须配 TLS）。

---

<a id="ch12-3-flaws"></a>

## 致命缺陷

| # | 问题 | 说明 |
|---|------|------|
| 1 | **明文等价** | Base-64 易解码，密码在网络上裸奔 |
| 2 | **密码复用** | 同一密码多站 → 一处泄露全盘 |
| 3 | **重放攻击** | 截获 `Authorization` 可**原样重放** |
| 4 | **无完整性** | 中间人可改请求其他部分 |
| 5 | **服务器欺骗** | 假站点骗用户交密码 |

---

<a id="ch12-3-mitigation"></a>

## 实用要点

| 场景 | 建议 |
|------|------|
| 仅防**无意**访问、内网低敏 | 可勉强用 Basic |
| **任何**需保密场景 | **Basic + HTTPS（TLS）** 隐藏通道；更好用 **Digest** 或现代 Token |

→ 重放缓解：[ch13](../chapter-13-digest-auth/chapter-summary.md)  
→ 通道加密：[ch14](../chapter-14-secure-http/chapter-summary.md)

---

## 拓展（预留）

- HTTPS 下仍可能 **钓鱼**（社会工程）  

---

## 抓包/实操记录

（待填：HTTP 明文 vs HTTPS 下 Authorization）

---

## 疑问与总结

**无 TLS 的 Basic ≈ 把密码贴在明信片上。**
