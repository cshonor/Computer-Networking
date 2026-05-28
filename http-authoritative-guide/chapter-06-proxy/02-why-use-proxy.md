# 6.2 为什么使用代理

> 本章：[chapter-summary.md](./chapter-summary.md#ch06-2) · [ch01 §1.8](../chapter-01-http-overview/08-web-component.md#ch01-8-proxy)

## 本节核心目标

记住代理的 **八大应用场景** 及各自目的。

---

<a id="ch06-2-eight"></a>

## 八大用途

| # | 场景 | 作用 |
|---|------|------|
| 1 | **儿童过滤器** | 集中拦截不当内容 |
| 2 | **文档访问控制** | 统一认证，隐藏内网权限结构 |
| 3 | **安全防火墙** | 限制应用层协议进出，可挂病毒扫描 |
| 4 | **Web 缓存** | 本地副本，省带宽、降延迟 → [ch07](../chapter-07-cache/chapter-summary.md) |
| 5 | **反向代理/替代物** | 挡在源站前，**服务器加速器** → [ch18 CDN](../chapter-18-web-hosting/chapter-summary.md) |
| 6 | **内容路由器** | 按负载/类型/VIP 导向不同服务器或缓存 |
| 7 | **转码器** | 改 body 格式（GIF→JPEG、移动版 HTML）→ [ch17](../chapter-17-content-negotiation-transcode/chapter-summary.md) |
| 8 | **匿名者** | 剥离 IP、`From`、`Referer`、`Cookie` 等 |

---

## 易错

**匿名代理** 删掉 Cookie 等 → 依赖会话的站点（购物车）可能**失效**。

---

## 拓展（预留）

- **WAF** 在反向代理上的特征拦截  
- CDN 全球 **Surrogate** 部署  

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**正向代理多服务客户端；反向代理多服务源站与性能。**
