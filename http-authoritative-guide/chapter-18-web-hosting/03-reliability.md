# 18.3 使网站更可靠

> 本章：[chapter-summary.md](./chapter-summary.md#ch18-3) · [ch07 缓存](../chapter-07-cache/chapter-summary.md) · [ch20 重定向](../chapter-20-redirect-load-balance/chapter-summary.md)

## 本节核心目标

掌握 **镜像集群**、**CDN**、**Surrogate** 与透明代理缓存。

---

<a id="ch18-3-farm"></a>

## 18.3.1 镜像服务器集群

| 角色 | 说明 |
|------|------|
| **主原始服务器** | 内容权威 |
| **复制原始服务器** | 镜像副本 |

分发：局域网 **L4/L7 交换机**；地理分散用 **HTTP 重定向** 或 **DNS**（轮询等）。

---

<a id="ch18-3-cdn"></a>

## 18.3.2 CDN

专用分发网络：节点可为 Web 服务器、**反向代理**或**缓存**。

---

<a id="ch18-3-surrogate"></a>

## 18.3.3 反向代理缓存（Surrogate）

- **代表**源站接请求  
- **需求驱动**：只缓存被请求的热点；可 **prefetch**  

→ [ch06 反向代理](../chapter-06-proxy/02-why-use-proxy.md#ch06-2-eight)、[ch07](../chapter-07-cache/chapter-summary.md)

---

<a id="ch18-3-intercept"></a>

## 18.3.4 代理缓存（拦截环境）

透明拦截：L2/L3 设备把流量**强制**导向代理，客户端无感。

→ [ch06 §6.3](../chapter-06-proxy/03-proxy-placement.md#ch06-3-traffic)

---

## 抓包/实操记录

（待填：CDN 边缘 IP vs 源站 IP）

---

## 疑问与总结

**可靠 = 多副本 + 智能把用户导向健康/就近节点。**
