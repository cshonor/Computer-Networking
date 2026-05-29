# 12.2 基本认证

> 本章：[chapter-summary.md](./chapter-summary.md#ch12-2) · [12.3 缺陷](./03-security-flaws.md)

## 本节核心目标

掌握 **Basic** 质询/响应格式、**Base-64** 编码及**代理认证**首部差异。

---

<a id="ch12-2-format"></a>

## 12.2.1 首部格式

| 方向 | 首部 | 示例 |
|------|------|------|
| 服务器 → 客户端 | **`WWW-Authenticate`** | `Basic realm="quoted-realm"` |
| 客户端 → 服务器 | **`Authorization`** | `Basic base64(user:pass)` |

Basic **不使用** `Authentication-Info`。

---

<a id="ch12-2-base64"></a>

## 12.2.2 Base-64 编码（易错）

```text
username + ":" + password  →  Base-64  →  Authorization 值
```

| 目的 | 说明 |
|------|------|
| 合法字符 | 避免首部非法字符、国际字符问题 |
| 「扰乱」 | 防管理员**无意间**看到明文 |

**不是加密**：嗅探者 **Base-64 解码即得明文**。

---

<a id="ch12-2-proxy"></a>

## 12.2.3 代理认证

| 项 | 源站认证 | 代理认证 |
|----|----------|----------|
| 状态码 | **401** | **407** |
| 质询 | `WWW-Authenticate` | **`Proxy-Authenticate`** |
| 凭证 | `Authorization` | **`Proxy-Authorization`** |

→ [ch06 §6.7](../chapter-06-proxy/07-proxy-auth.md)

---

## 拓展（预留）

- CORS **`Access-Control-Allow-Credentials`** 与跨域带凭证  

---

## 抓包/实操记录

（待填：Wireshark 解码 Base64 Authorization）

---

## 疑问与总结

**Basic = 最简单、最广支持；安全靠 HTTPS 叠层。**
