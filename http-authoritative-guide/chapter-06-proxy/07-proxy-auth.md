# 6.7 代理认证

> 本章：[chapter-summary.md](./chapter-summary.md#ch06-7) · [ch12 基本认证](../chapter-12-basic-auth/chapter-summary.md) · [ch13 摘要认证](../chapter-13-digest-auth/chapter-summary.md)

## 本节核心目标

掌握 **407** 代理认证三步交互及多代理链的局限。

---

<a id="ch06-7-flow"></a>

## 交互流程

```text
1. 代理 → 客户端：407 Proxy Authentication Required
              + Proxy-Authenticate（类型如 Basic、realm）

2. 客户端 → 代理：重发请求 + Proxy-Authorization（凭证）

3. 代理验证 → 通过则转发源站；失败再 407
```

---

## 易错

**多级代理**各自 407 时，凭证与**具体代理**绑定不清 → 机制常**不好用**。

---

## 拓展（预留）

- **HTTPS CONNECT** 隧道：在明文 CONNECT 阶段带 `Proxy-Authorization` → [ch08 隧道](../chapter-08-gateway-tunnel-relay/05-tunnel.md#ch08-5-connect)

---

## 抓包/实操记录

（待填：企业代理 407 弹窗）

---

## 疑问与总结

**407 对的是代理，401 对的是源站**——别混。
