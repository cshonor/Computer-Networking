# 12.1 认证

> 本章：[chapter-summary.md](./chapter-summary.md#ch12-1) · 全书：[../README.md](../README.md) · [ch11 登录](../chapter-11-client-id-cookie/04-user-login.md)

## 本节核心目标

掌握 HTTP **质询/响应**认证框架、相关首部与 **realm（安全域）**。

---

<a id="ch12-1-challenge"></a>

## 12.1.1 质询/响应框架

| 步 | 行为 |
|----|------|
| 1 | 客户端请求（可无凭证） |
| 2 | 服务器**不执行**敏感操作，返回**认证质询** |
| 3 | 客户端附**用户名/密码**重试 |
| 4 | 匹配则正常处理并返回资源 |

---

<a id="ch12-1-headers"></a>

## 12.1.2 四步与首部

```text
① GET（无 Authorization）
② 401 Unauthorized + WWW-Authenticate（算法、realm）
③ 带 Authorization 的重复请求
④ 200 OK（可选 Authentication-Info）
```

| 官方协议 | 章节 |
|----------|------|
| **基本认证（Basic）** | 本章 [12.2](./02-basic-auth.md) |
| **摘要认证（Digest）** | [ch13](../chapter-13-digest-auth/chapter-summary.md) |

---

<a id="ch12-1-realm"></a>

## 12.1.3 安全域（Realm）

服务器把受保护资源划成**安全域**，每域可有不同用户集与密码规则。

```http
WWW-Authenticate: Basic realm="Corporate Financials"
```

`realm` 提示用户应输入**哪套**账号密码。

---

## 拓展（预留）

- **JWT / OAuth 2.0** 与 SPA 前后端分离  

---

## 抓包/实操记录

（待填：`curl -v -u user:pass URL`）

---

## 疑问与总结

**401 对源站；407 对代理** — [ch06](../chapter-06-proxy/07-proxy-auth.md)
