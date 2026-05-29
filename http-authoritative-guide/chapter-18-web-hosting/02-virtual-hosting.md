# 18.2 虚拟主机托管

> 本章：[chapter-summary.md](./chapter-summary.md#ch18-2) · [ch09 Host](../chapter-09-web-robot/02-robot-http.md#ch09-2-host) · [ch14 SNI](../chapter-14-secure-http/07-https-details.md#ch14-7-vhost)

## 本节核心目标

掌握 **HTTP/1.0 无主机名**痛点、早期权宜之计与 **`Host` 首部**（及 HTTPS **SNI**）。

---

<a id="ch18-2-problem"></a>

## 18.2.1 HTTP/1.0 缺陷

```http
GET /index.html HTTP/1.0
```

请求行**只有路径**，无主机名 → 同机多站（`joes.com` / `marys.com`）**无法区分** docroot。

---

<a id="ch18-2-workarounds"></a>

## 18.2.2 早期权宜之计

| 方案 | 缺点 |
|------|------|
| **路径前缀** `/joe/...` | 破坏 URL 期望 |
| **不同端口** 80/81 | 用户不愿记端口 |
| **虚拟 IP** | IP 数量有限、IPv4 稀缺、集群复杂 |

曾以 **IP 虚拟主机**最流行：按**目的 IP** 选站点。

---

<a id="ch18-2-host"></a>

## 18.2.3 HTTP/1.1 Host 首部（最终解）

```http
Host: www.example.com
Host: www.example.com:8080
```

| 规则 | 说明 |
|------|------|
| **1.1 客户端** | **必须**带 `Host` |
| **1.1 服务器** | 无 `Host` → **`400 Bad Request`** |
| **代理** | 转发前**必须**补/保留真实 `Host` |
| **默认端口** | 省略则用方案默认（HTTP **80**） |

→ [ch05 虚拟主机](../chapter-05-web-server/07-resource-mapping.md#ch05-7-docroot)

---

## 拓展：HTTPS 与 SNI

TLS 握手在 HTTP 之前 → 单 IP 多证书需 **SNI** 在握手时发主机名 → [ch14](../chapter-14-secure-http/07-https-details.md)

---

## 抓包/实操记录

（待填：请求行 + Host 与不同虚拟站响应）

---

## 疑问与总结

**虚拟主机现代靠 Host；HTTPS 还要 SNI。**
