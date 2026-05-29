# 第 7 章：防火墙与网络地址转换（NAT）

> 按书节速记：[7.1](7.1-introduction.md) · [7.2](7.2-packet-filter-firewall.md) · [7.3](7.3-nat-napt.md) · [7.4](7.7-nat-traversal.md) · [7.5](7.5-acl-port-control.md) · [7.6](7.6-ipv6-nat-transition.md) · [7.7](7.7-security-attacks.md) · [7.8](7.8-summary.md) · [QUICKREF §7](../QUICKREF.md)

> 《TCP/IP 详解》卷1 第 2 版（Fall, 2016）· 精细化学习笔记（同步自 [tcpip_vol1_ed2_notes](../../tcpip_vol1_ed2_notes/03_network_layer/ch07_firewall_nat.md)）  
> 前置：[ch05 IP](../chapter05-ip-protocol/study.md) · [ch01 端到端](../chapter01-overview/study.md#ch01-e2e) · 自顶向下：[§4.3 NAT](../../top_down/04_network_layer_data_plane/study.md#ch4-3)

**Middlebox** 打破早期 **端到端透明**：防火墙建立**受限连通**安全边界，**NAT** 在 IPv4 枯竭下实现地址复用 — 网络从「哑核心、智能边缘」转向**状态化边界**。

---

<a id="ch07-1"></a>

## 7.1 引言

→ 精读：[7.1-introduction.md](7.1-introduction.md)

### 为何需要 Middlebox

早期 **端到端透明**（只转发、不改包）→ 现实压力：

| 压力 | 应对 |
|------|------|
| **IPv4 枯竭** | **NAT** 地址复用 |
| **安全威胁** | **防火墙** 边界过滤 |

打破透明，换 **安全 + 地址复用**。

### 防火墙 vs NAT

| | **防火墙** | **NAT** |
|--|------------|---------|
| 角色 | 流量警察 | 地址翻译官 |
| 核心 | **受限连通 + 策略过滤** | **私网→公网 + PAT 端口复用** |
| 节 | [7.2](#ch07-2) | [7.3](#ch07-3) |

### 代价（破坏端到端）

- 真实 IP/端口被改写；外网难主动连内网  
- **ALG**、**STUN/TURN/ICE**；会话表状态开销  

### 开发默认前提

假设必有 NAT/防火墙 → **保活**、端口映射/DMZ、不依赖固定公网 IP。

### 为何仍必需

IPv4 枯竭 + 经济边界防护 → **现实折中**（非理想端到端）。

### 本章主线

包过滤/状态防火墙 · NAT/PAT · 穿透 · 家用路由器二合一

---

<a id="ch07-2"></a>

## 7.2 防火墙

→ 精读：[7.2-packet-filter-firewall.md](7.2-packet-filter-firewall.md)

部署于**可信内网**与**不可信外网**边界，按规则管控往来流量 — 阻止未授权访问、放行合法通信。

### 包过滤（L3/L4）

- **转发前**匹配 IP/TCP/UDP 首部（地址、协议号、端口、TCP 标志）  
- **无状态**：逐包独立判决，快但易被伪造包绕过  
- **有状态**：**五元组状态表**跟踪会话，回程匹配表项放行 → 主流方案  

### 应用层网关 / 代理防火墙（L7）

- 内网只连**防火墙**；防火墙再**新建连接**访问外网 — **无端到端直连**  
- 可解析 HTTP/FTP 等内容；隐藏内网拓扑；延迟与开销大  
- 勿与 NAT 的 **ALG（改载荷地址）** 混为一谈 → [7.3](#ch07-3)

### DMZ

隔离网段放对外服务器；外网仅达 DMZ；DMZ 通常**不可直入内网**。

### 二者对比

| | 包过滤 | 代理 |
|--|--------|------|
| 层 | L3/L4 | L7 |
| 行为 | 头部检查 + 可选状态表 | 双重连接 + 应用解析 |
| 性能 | 高 | 低 |
| 深度 | 头部/会话 | 应用内容 |

<a id="ch07-2-state"></a>

### TCP 状态检测（补充机制）

1. **SYN** 到达 → 策略允许 → 状态表建**半开**项  
2. 后续包校验 **SEQ/ACK**；无状态项却带 ACK → 可能非法注入  
3. 反向 **SYN-ACK** 与初始五元组/状态一致 → Allow；违规 → Drop  

### 防火墙 vs IDS

| | 防火墙 | IDS |
|--|--------|-----|
| 角色 | **阻断**准入 | **检测**报警，常不直接阻断 |

---

<a id="ch07-3"></a>

## 7.3 网络地址转换（NAT）

缓解地址短缺，但使中间节点维护映射状态，**端到端透明性**受损。

### 7.3.1 基本 NAT 与 NAPT

| 类型 | 行为 |
|------|------|
| **基本 NAT** | 主要改 **IP**；内网 ↔ 公网池 **一对一** |
| **NAPT (NAT/PAT)** | **IP + 端口** 多对一；最常见；默认仅**由内向外**易建立 |

### 7.3.2 映射行为 (Mapping)

内部 `(IP:Port)` → 外部 `(IP:Port)` 的分配规则：

| 类型 | 行为 |
|------|------|
| **端点无关 (EIM)** | 无论外部目标是谁，同一内部端点 → **同一**外部映射 |
| **地址依赖 (ADM)** | 发往不同外部地址 → **不同**外部端口 |

### 7.3.3 过滤行为 (Filtering)

外向内的报文是否允许：

| 类型 | 行为 | P2P |
|------|------|-----|
| **端点无关 (EIF)** | 有映射则**任意**外部主机可打入 | 较易 |
| **地址依赖 (ADF)** | 仅曾通信过的外部 IP 可回包 | **更安全**，P2P 更难 |

> **考点**：决定 P2P 能否打通的往往是 **Filtering**，不仅是 Mapping。

### 7.3.4–7.3.5 服务器与发夹 (Hairpinning)

内网 A、B 经公网信令交换到的是**公网映射**；若 A 访问「自己的公网 IP:端口」指向 B，需 NAT **发夹**：识别目的为自身公网地址的流量并**转回内网**，否则同网段无法互访映射端点。

### 7.3.6–7.3.7 ALG 与 CGN

| 主题 | 说明 |
|------|------|
| **NAT ALG / 编辑器** | 改应用层中的**私网 IP 泄露**（如 FTP **PORT** 命令） |
| **CGN (NAT444)** | ISP 侧多层 NAT；额外延迟、**端口配额**更紧 |

→ FTP/ALG 属边界盒行为，非链路层协议本身。

---

<a id="ch07-4"></a>

## 7.4 NAT 穿越

在受限环境下恢复 **P2P**。

### 打孔 (Hole Punching)

经**信令服务器**协调，A、B **同时**向对方发探测包 → NAT 视为**由内向外**合法流 → 状态表开**针孔**允许反向报文。

### STUN / TURN / ICE

| 协议 | 机制 | 核心 | 限制 |
|------|------|------|------|
| **STUN** | 反射寻址 | 获知自身公网 **IP:Port** | 轻量；难穿 **对称型 NAT** |
| **TURN** | 中继 | 公网服务器转发全部流量 | 成功率高；带宽/成本高 |
| **ICE** | 交互式连接 | 组合 STUN/TURN，选最优路径 | WebRTC 等标配 |

---

<a id="ch07-5"></a>

## 7.5 配置实践与协议交互

### 处理顺序（架构要点）

**过滤规则应先于 NAT 转换**。

先 NAT 会让攻击/无效流量占满**状态表/端口映射** → 合法流 **DoS**；应先 Drop 黑名单再建映射。

### UPnP / NAT-PMP / PCP

| 协议 | 场景 |
|------|------|
| **UPnP / NAT-PMP** | 家用网关；主机动态申请端口映射；**认证弱** |
| **PCP** | 现代 IETF 标准；映射生命周期等；CGN 环境更规范 |

---

<a id="ch07-6"></a>

## 7.6 IPv4/IPv6 共存与过渡

NAT 在 v6 时代常作**协议桥梁**，而非仅省地址。

### 7.6.1 DS-Lite

内网仍跑 **IPv4**，CPE **B4** 将 IPv4 封装进 **IPv6 隧道** → 运营商 **AFTR** 解封装并 **NAT44**。

### 7.6.2 NAT64 与 DNS64

仅 **IPv6 客户端** 访问仅 **IPv4 服务器** 的闭环：

| 组件 | 作用 |
|------|------|
| **DNS64** | 无 AAAA 时**合成**含 IPv4 的伪 AAAA |
| **NAT64** | 将 **IPv4-Embedded IPv6**（如 **64:ff9b::/96**）译为 IPv4 首部 |

→ DNS 细节：[ch11 DNS](../chapter11-dns-domain-resolve/study.md)

---

<a id="ch07-7"></a>

## 7.7 相关攻击

状态化中间件引入新攻击面。

| 攻击 | 说明 |
|------|------|
| **状态表溢出 DoS** | 大量伪造 SYN 占满防火墙/NAT 表 |
| **分片绕过** | 操纵分片偏移，使非法 L4 信息在首包审查后于内网**重组** |
| **状态注入** | 伪造 ACK/序列号误导状态表 |

**缓解**：每源地址映射上限、**TCP MSS** 限制、**uRPF**、严格碎片策略。

→ 源 IP 不可信：[ch05 §5.7](../chapter05-ip-protocol/study.md#ch05-7)

---

<a id="ch07-exam"></a>

## 7.8 总结与考点

边界设计需在 **Security / Transparency / Complexity** 间折中。

### 三条结论

1. **防火墙 + NAT** 使互联网失去无状态简洁性 → 协议栈需 **ALG** 等感知中间件。  
2. **NAT Filtering Behavior** 常是决定 **P2P** 能否连通的关键。  
3. IPv6 普及前，**NAT64/DNS64** 等长期承担**跨族**连通。

### 易混速记

| 问题 | 要点 |
|------|------|
| NAPT vs 基本 NAT | 是否改**端口**、多对一 |
| EIM vs ADM | 映射是否随**外部目标**变化 |
| EIF vs ADF | 外向内是否只允许**曾通信过的 IP** |
| Hairpin | 内网访问**本 NAT 公网 IP** 的回环 |
| 过滤 vs NAT 顺序 | **先过滤后 NAT** |

### 下一章

- [ch08 ICMP](../chapter08-icmpv4-icmpv6/study.md) — 不可达、PMTUD  
- [ch11 DNS](../chapter11-dns-domain-resolve/study.md) — DNS64  
- [04_network_layer §4.3 NAT](../../top_down/04_network_layer_data_plane/4.3_ipv4_ipv6_nat/README.md)

---

## Top-Down

- [study.md §4.3](../../top_down/04_network_layer_data_plane/study.md#ch4-3) · [中间盒 §4.5](../../top_down/04_network_layer_data_plane/study.md#ch4-5)

## Lab

- 家用路由器：端口映射、DMZ、UPnP 开关对比  
- `conntrack -L`（Linux）观察 NAT 状态  
- WebRTC：`ice` 候选类型（host/srflx/relay）

## Go / Rust

- **K8s**：Service **ClusterIP / NodePort / LoadBalancer** 与 kube-proxy NAT  
- **云**：SNAT 网关、安全组 = 有状态过滤 + 无 NAT 场景  
- **排障**：P2P 失败先查 NAT 类型 + 是否需 TURN；FTP 被动模式 + ALG
