# 6.4 客户端的代理设置

> 本章：[chapter-summary.md](./chapter-summary.md#ch06-4) · [6.3 部署](./03-proxy-placement.md)

## 本节核心目标

掌握浏览器导向代理的三种配置：**手工、PAC、WPAD**。

---

<a id="ch06-4-manual"></a>

## 一、手工配置

显式 **host:port**。

| 缺点 |
|------|
| 死板、难故障转移 |
| 大规模运维成本高 |

---

<a id="ch06-4-pac"></a>

## 二、PAC（Proxy Auto-Configuration）

| 项 | 说明 |
|----|------|
| 文件 | `.pac`，MIME `application/x-ns-proxy-autoconfig` |
| 核心函数 | `FindProxyForURL(url, host)` |
| 返回值 | `DIRECT` / `PROXY host:port` / `SOCKS host:port` |

支持按域名/URL **动态选路**、**故障转移**。

---

<a id="ch06-4-wpad"></a>

## 三、WPAD（自动发现 PAC 位置）

按序尝试找到 PAC URI：

1. **DHCP**  
2. **SLP**  
3. DNS **`wpad`** 子域  
4. DNS **SRV**  
5. DNS **TXT**  

---

## 拓展（预留）

- **GPO** 下发 PAC  
- **WPAD 欺骗**（不可信局域网 MITM 风险）  

---

## 抓包/实操记录

（待填：Windows「自动检测设置」）

---

## 疑问与总结

**企业网常见 PAC；WPAD 要警惕恶意 DHCP/DNS。**
