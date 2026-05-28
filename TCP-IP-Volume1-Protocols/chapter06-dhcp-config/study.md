# 第 6 章：系统配置 — DHCP 与自动配置

> 按书节速记：[6.1](6.1-introduction.md) · [6.2](6.2-dhcp-protocol.md) · [6.3](6.3-slaac-autoconfig.md) · [6.4](6.4-dhcp-dns-ddns.md) · [6.5](6.5-pppoe.md) · [6.6](6.6-dhcp-security.md) · [6.7](6.7-summary.md) · [QUICKREF §6](../QUICKREF.md)

> 《TCP/IP 详解》卷1 第 2 版（Fall, 2016）· 精细化学习笔记（同步自 [tcpip_vol1_ed2_notes](../../tcpip_vol1_ed2_notes/03_network_layer/ch06_dhcp.md)）  
> 前置：[ch05 IP](../chapter05-ip-protocol/study.md) · [ch04 ARP](../chapter04-arp-protocol/study.md) · 自顶向下：[§4.3 DHCP](../../top_down/04_network_layer_data_plane/study.md#ch4-3)

本章聚焦协议栈 **自举（Bootstrapping）**：主机如何从无到有获得 **IP、掩码、网关、DNS** 等参数 — 不仅是地址分配，更是**资源发现与策略下发**的纽带。

---

<a id="ch06-1"></a>

## 6.1 引言

### 静态配置的局限

| 问题 | 说明 |
|------|------|
| 管理成本 | 大规模、移动设备难以手工维护 |
| 地址利用率 | 离线主机仍占地址，无法回收 |
| 一致性 | 易 **IP 冲突**、网关/DNS 配错 |

### 动态配置的战略意义

**即插即用**；参数管理从单机收回到**逻辑层/服务端** → 支撑互联网规模扩张。

### 演进脉络

**RARP → BOOTP → DHCP**（IPv6 侧还有 **DHCPv6** 与 **SLAAC**）。

---

<a id="ch06-2"></a>

## 6.2 动态主机配置协议（DHCP）

**DHCP** 本质是 **应用层（UDP）** 协议，却在 **网络层初始化** 中起决定性作用。

### 为何放在应用层？

利用现有 **UDP 栈** 处理租约、多选项等复杂逻辑，**不必在内核重写**底层交互 — 降低内核复杂度。

---

<a id="ch06-2-lease"></a>

### 6.2.1 地址池与租约

| 概念 | 说明 |
|------|------|
| **地址池** | 服务器可分配的范围 |
| **租约 (Lease)** | 临时 IP 使用权，促进地址循环 |

| 定时器 | 时机 | 行为 |
|--------|------|------|
| **T1（续租）** | 租约 **50%** | 向**原服务器**单播 **Renew** |
| **T2（重绑定）** | 租约 **87.5%** | 原服务器无响应 → **广播**找任意可用服务器 |

---

<a id="ch06-2-msg"></a>

### 6.2.2 消息格式（BOOTP 兼容）

| 字段 | 含义 |
|------|------|
| **op** | 1=请求，2=应答 |
| **htype/hlen** | 硬件类型/长度（以太网 **1** / **6**）→ **媒介无关** |
| **xid** | 事务 ID，匹配请求/响应 |
| **ciaddr** | 客户端已知 IP |
| **yiaddr** | **Your IP** — 服务器分配 |
| **giaddr** | 中继代理地址（跨网段） |
| **Magic Cookie** | **99.130.83.99** — BOOTP/DHCP 分界，后续按 **选项** 解析 |

---

<a id="ch06-2-options"></a>

### 6.2.3 常用选项

| Option | 内容 |
|--------|------|
| **1** | 子网掩码 |
| **3** | 路由器（默认网关） |
| **6** | DNS 服务器 |
| **15** | 域名 |

---

<a id="ch06-2-dora"></a>

### 6.2.4 DORA 四步交互

| 步骤 | 含义 | L2 MAC | L3 IP |
|------|------|--------|-------|
| **Discover** | 找服务器 | Client → **FF:FF:FF:FF:FF:FF** | **0.0.0.0 → 255.255.255.255** |
| **Offer** | 提供配置 | Server → Client（或广播） | Server → **255.255.255.255** 等 |
| **Request** | 选中并请求（DECLINE 其他 Offer） | Client → **广播** | **0.0.0.0 → 255.255.255.255** |
| **ACK** | 租约生效 | Server → Client | Server → 255.255.255.255 等 |

**Request 广播的原因**：让网内**所有**曾 Offer 的服务器知晓客户端选择，释放未中标地址。

---

<a id="ch06-2-ext"></a>

### 6.2.5–6.2.12 扩展特性

| 主题 | 要点 |
|------|------|
| **DHCPv6** | 少用广播；组播 **ff02::1:2**；**Solicit → Advertise → Request → Reply**（四步，名称不同） |
| **中继 (Relay Agent)** | 捕获客户端广播 → **单播** 至远端服务器；**giaddr** 标识中继；解决广播不过路由器 |
| **位置/移动 (6.2.10–11)** | **LCI**、**LoST** 地理位置；**MoS**、**ANDSF** 辅助 WLAN/蜂窝选择 |
| **DHCP Probe (6.2.12)** | 分配后 **ARP** 或相邻探测，确认链路上地址可用 → **ACD 最后一道防线** |

### 常见故障

租约异常中止 · 中继路径 **MTU** 截断 · 未 Probe 导致 **IP 冲突**

→ 免费 ARP/ACD：[ch04 §4.5](../chapter04-arp-protocol/study.md#ch04-5)

---

<a id="ch06-3"></a>

## 6.3 无状态地址自动配置（SLAAC）

IPv6 哲学：可**不依赖中心化 DHCP** 合成地址。

### 6.3.1 IPv4 链路本地

DHCP 不可用时 → **169.254.0.0/16**（APIPA）；经 **ARP** 冲突检测，仅本地链路有效。

→ RFC 3927

### 6.3.2 IPv6 SLAAC（ICMPv6 NDP）

```text
主机 --[ RS 组播 ]--> 路由器
主机 <--[ RA 带 Prefix ]-- 路由器
```

1. **合成**：**网络前缀（RA）** + **接口标识符 IID**  
2. **EUI-64**：48b MAC 中间插 **0xFFFE**；翻转 **U/L 位（第 7 位）** 0→1 表示全局唯一（IEEE MAC 场景）  
3. **隐私扩展 (RFC 4941)**：随机、定期更换 IID，避免长期 MAC 映射被追踪

→ ND/ICMPv6：[ch08](../chapter08-icmpv4-icmpv6/study.md)

---

<a id="ch06-4"></a>

## 6.4–6.5 DHCP 与 DNS、以太网 PPP

### DDNS

DHCP 地址变更时，客户端或服务器**动态更新 DNS**（A/AAAA），维持对公服务连续性。

→ [ch11 DNS](../chapter11-dns-domain-resolve/study.md)

### PPPoE

宽带接入：将带**认证**的 **PPP** 封装进以太网；**发现阶段 + 会话阶段** 分发 IP — 运营商拨号常见。

→ [ch03 §PPP](../chapter03-link-layer/study.md#ch03-6)（PPP 帧格式见链路层章）

---

<a id="ch06-5"></a>

## 6.6 与系统配置相关的攻击

DHCP **无强认证**，默认信任**物理链路**。

| 攻击 | 说明 |
|------|------|
| **DHCP 饥饿** | 伪造大量 Discover，耗尽地址池 |
| ** Rogue DHCP** | 更快 Offer → 伪造网关/DNS → **MITM** |

**防御**：接入交换机 **DHCP Snooping** — 信任端口仅连合法服务器，丢弃其他端口的 DHCP **Server 报文**。

---

<a id="ch06-exam"></a>

## 6.7–6.8 总结与考点

### 对比表

| 特性 | DHCPv4 | DHCPv6 | IPv6 SLAAC |
|------|--------|--------|------------|
| 中心化 | 高（Stateful） | 高（Stateful） | **极低（Stateless）** |
| 传输 | UDP **67/68** | UDP **546/547** | **ICMPv6 NDP** |
| 底层 | **广播** | **组播** | **组播** |
| 优势 | 选项丰富、策略可控 | Rapid Commit 等 | 极简、去中心化 |
| 回退/本地 | **169.254.0.0/16** | — | **fe80::/10** 链路本地 |

### 架构视角（一句话）

从 **DHCP 的行政管理** 到 **SLAAC 的协作发现** — 按业务在**可控性**与**灵活性**之间选型（云/数据中心常仍重度依赖 DHCP/DHCPv6）。

### 关键 RFC

| RFC | 主题 |
|-----|------|
| 2131 | DHCPv4 |
| 3315 | DHCPv6 |
| 4862 | SLAAC |
| 4941 | SLAAC 隐私扩展 |
| 3927 | IPv4 链路本地 |

### 下一章

- [ch07 NAT/防火墙](../chapter07-firewall-nat/study.md)  
- [ch08 ICMP](../chapter08-icmpv4-icmpv6/study.md) — RA/RS、ND  
- [ch05 IP](../chapter05-ip-protocol/study.md)

---

## Top-Down

- [04_network_layer_data_plane §4.3](../../top_down/04_network_layer_data_plane/study.md#ch4-3)  
- [06_link_layer §6.7 Web 路径](../../top_down/06_link_layer_and_lan/study.md#ch6-7)（DHCP 获取地址）

## Lab

- `dhclient -v` / Windows `ipconfig /all` 看租约、T1/T2  
- Wireshark：`bootp` 过滤器，抓 **DORA**  
- 容器/K8s：CNI 与 DHCP 关系（多数用静态/CNI 而非经典 DORA）

## Go / Rust

- **Go**：`net.Interfaces()` 看重启后地址；云元数据（非 DHCP）替代场景  
- **排障**：无地址时查 **169.254.x.x**；IPv6 `fe80::` + `ip -6 addr`  
- **安全**：数据中心启用 **DHCP Snooping** + 固定 DNS
