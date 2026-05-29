# 11.4 用户登录

> 本章：[chapter-summary.md](./chapter-summary.md#ch11-4) · [ch12 基本认证](../chapter-12-basic-auth/chapter-summary.md) · [ch13 摘要认证](../chapter-13-digest-auth/chapter-summary.md)

## 本节核心目标

掌握 **401 质询 / Authorization** 登录框架及状态负担在**浏览器**一侧。

---

<a id="ch11-4-flow"></a>

## 三步机制

```text
1. 服务器 → 401 Login Required + WWW-Authenticate
2. 浏览器弹窗 → 用户输入账号密码
3. 后续请求自动带 Authorization 首部
```

**状态**：由浏览器**缓存凭证**并重复发送，服务器可不维护会话表（仍可在服务端建 Session）。

---

## 拓展（预留）

- **OAuth 2.0 / OIDC**、SSO  

---

## 抓包/实操记录

（待填：`curl -v` 触发 401）

---

## 疑问与总结

**登录 = 显式凭证；与 Cookie 会话常组合使用。**
