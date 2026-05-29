# 20.5 代理的重定向方法

> 本章：[chapter-summary.md](./chapter-summary.md#ch20-5) · [ch06.4 客户端代理设置](../chapter-06-proxy/04-client-proxy-settings.md)

## 本节核心目标

掌握浏览器如何**发现并使用代理**：显式配置、**PAC**、**WPAD**。

---

<a id="ch20-5-explicit"></a>

## 20.5.1 显式浏览器配置

用户在浏览器填入代理 **主机:端口**。

| 缺点 | 说明 |
|------|------|
| **无自动回退** | 代理宕机 → 浏览器**不会**自动直连源站 |
| **难运维** | 增减代理须**每台终端**手工改 |

---

<a id="ch20-5-pac"></a>

## 20.5.2 代理自动配置（PAC）

| 项 | 内容 |
|----|------|
| **机制** | 下载 **PAC**（JavaScript）；每 URL 调 `FindProxyForURL(url, host)` |
| **返回值** | 代理列表或 **`DIRECT`**（直连） |
| **能力** | 按主机名、DNS、子网、时间等动态选路 |

**局限**：仍须手工配置 **PAC 文件 URL** — 非全自动。

```javascript
// PAC 示意
function FindProxyForURL(url, host) {
  if (isInNet(host, "10.0.0.0", "255.0.0.0")) return "DIRECT";
  return "PROXY cache.corp:8080";
}
```

---

<a id="ch20-5-wpad"></a>

## 20.5.3 Web 代理自动发现（WPAD）

| 项 | 内容 |
|----|------|
| **机制** | 自动定位 **PAC 的 URL（CURL）**，下载后执行 |
| **发现顺序** | DHCP → SLP → DNS 知名主机名 → DNS SRV → DNS TXT |
| **必须支持** | **DHCP**、**DNS 知名主机名** |

→ 与 [ch06.4](../chapter-06-proxy/04-client-proxy-settings.md) 互补：本书代理章讲用法，本章讲**重定向/LB 语境**。

---

## 拓展（预留）

- 公共 Wi‑Fi 下 **WPAD 劫持**、DNS 后缀欺骗与系统缓解  

---

## 抓包/实操记录

（待填：查看系统 PAC/WPAD 设置）

---

## 疑问与总结

**显式 < PAC < WPAD** — 自动化递增，部署与安全风险也递增。
