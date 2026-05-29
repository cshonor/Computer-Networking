# 13.3 增强保护质量

> 本章：[chapter-summary.md](./chapter-summary.md#ch13-3) · [13.2 A2](./02-digest-computation.md#ch13-2-a2)

## 本节核心目标

理解 **`qop`（保护质量）** 协商及 **`Authentication-Info`** 首部。

---

<a id="ch13-3-qop"></a>

## qop 协商

| 步 | 行为 |
|----|------|
| 服务器 | `WWW-Authenticate` 列出支持的 **qop**（逗号分隔） |
| 客户端 | 在 `Authorization` 中**选一项**回送 |

---

<a id="ch13-3-auth-int"></a>

## 13.3.1 报文完整性（auth-int）

**`qop="auth-int"`** → A2 含 **`H(实体主体)`**  
验证身份 + **body 未被改**。

---

<a id="ch13-3-headers"></a>

## 13.3.2 首部

| 首部 | 用途 |
|------|------|
| `WWW-Authenticate` / `Authorization` | 同 Basic |
| **`Authentication-Info`** | `nextnonce`、`rspauth`、三步握手等 |

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**auth = 只认证；auth-int = 认证 + 实体完整性（仍非 TLS）。**
