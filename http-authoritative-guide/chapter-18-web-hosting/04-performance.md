# 18.4 让网站更快

> 本章：[chapter-summary.md](./chapter-summary.md#ch18-4) · [ch15 gzip](../chapter-15-entity-encoding/05-content-encoding.md) · [ch07 距离时延](../chapter-07-cache/04-distance-latency.md)

## 本节核心目标

网站加速两大维度：**近**与**小**。

---

<a id="ch18-4-near"></a>

## 1. 缩短距离、分散拥塞

- **集群 + 边缘 CDN/反向代理** → 内容靠近用户  
- 降低 RTT、缓解骨干拥塞 → [18.3](./03-reliability.md)

---

<a id="ch18-4-small"></a>

## 2. 减小传输负荷

- **内容编码**（gzip 等）减少字节 → [ch15 §15.5](../chapter-15-entity-encoding/05-content-encoding.md)  
- 配合缓存命中、HTTP/2 多路复用等

---

## 抓包/实操记录

（待填：边缘 POP TTFB vs 源站）

---

## 疑问与总结

**快 = 少走路 + 少传字节。**
