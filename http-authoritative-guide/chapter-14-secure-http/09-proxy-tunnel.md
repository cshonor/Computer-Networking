# 14.9 通过代理以隧道形式传输安全流量

> 本章：[chapter-summary.md](./chapter-summary.md#ch14-9) · [ch08 §8.5 CONNECT](../chapter-08-gateway-tunnel-relay/05-tunnel.md#ch08-5-connect)

## 本节核心目标

理解 HTTPS 下代理**读不到目标** → 用 **CONNECT 隧道**。

---

<a id="ch14-9-blind"></a>

## 代理解析盲区

明文 HTTP：代理读请求行、`Host` 转发。  
**HTTPS**：载荷已加密 → 代理**不知**目标主机。

---

<a id="ch14-9-connect"></a>

## CONNECT 隧道

```http
CONNECT home.example.com:443 HTTP/1.0
```

| 步 | 行为 |
|----|------|
| 1 | 客户端向代理发**明文 CONNECT** |
| 2 | 代理连目标 **:443**，回 **`200 Connection Established`** |
| 3 | 此后**盲转发** TLS 密文字节流 |

可与 **`Proxy-Authorization`** 结合 → [ch06](../chapter-06-proxy/07-proxy-auth.md)

---

## 抓包/实操记录

（待填：企业代理下 CONNECT 再 TLS）

---

## 疑问与总结

**HTTPS 过代理 = 先 CONNECT 挖隧道，再在隧道里 TLS。**
