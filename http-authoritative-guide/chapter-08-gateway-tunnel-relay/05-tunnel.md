# 8.5 隧道

> 本章：[chapter-summary.md](./chapter-summary.md#ch08-5) · [ch04 Connection](../chapter-04-connection-management/03-http-connection.md) · [ch06 代理隧道](../chapter-06-proxy/01-middleman.md#ch06-1-vs-gateway)

## 本节核心目标

掌握 **CONNECT 隧道**、**SSL 穿透防火墙** 及与 **HTTPS 网关** 的区别。

> 对比：[TCP/IP 链路层/网络层隧道](../../TCP-IP-Volume1-Protocols/chapter03-link-layer/3.9-tunnel-basics.md)（IPIP/GRE）— **不同层次**；本章是 **HTTP CONNECT 应用层隧道**。

---

<a id="ch08-5-connect"></a>

## 8.5.1 CONNECT 建立隧道

```http
CONNECT host:port HTTP/1.0
```

| 阶段 | 行为 |
|------|------|
| 网关建 TCP 到 `host:port` | 成功则 `200 Connection Established` |
| 之后 | **盲转发**任意字节（非 HTTP 解析） |

用途：在**只允许 Web 流量**的防火墙上承载其他协议。

---

<a id="ch08-5-pipeline"></a>

## 8.5.2 数据、定时与连接（易错）

客户端可在收到 `200` **之前**管道化发送隧道数据。

若网关提前关连接 → 客户端难区分**网络故障** vs **认证拒绝**，可能**丢数据**。

---

<a id="ch08-5-ssl"></a>

## 8.5.3 SSL 隧道

加密 SSL 字节流**不能被普通代理解析** → 经 **80/443 上的 CONNECT** 穿过防火墙。

---

<a id="ch08-5-ssl-vs-gateway"></a>

## 8.5.4 SSL 隧道 vs HTTP/HTTPS 网关

| | HTTPS **网关** | **SSL 隧道** |
|---|----------------|--------------|
| 代理是否实现 SSL | **是**，解密/再加密 | **否**，只转发密文 |
| 可见性 | 可见 HTTP 明文 | 端到端加密 |

---

<a id="ch08-5-auth"></a>

## 8.5.5 隧道认证

CONNECT 前可用 **`Proxy-Authorization`** → [ch06 §6.7](../chapter-06-proxy/07-proxy-auth.md)

---

<a id="ch08-5-security"></a>

## 8.5.6 安全性（易错）

网关**无法验证**隧道内真实协议 → 可能被滥用（Telnet、游戏流量）。

**规范**：仅允许 **CONNECT 到知名端口**（如 **443**）。

---

## 拓展（预留）

- **WebSocket** 与 `Upgrade` vs CONNECT 全双工  

---

## 抓包/实操记录

（待填：`curl -x proxy:port -v https://example.com` 看 CONNECT）

---

## 疑问与总结

**隧道 = 借 HTTP 建 TCP 管道；不是 HTTP 代理转发语义。**
