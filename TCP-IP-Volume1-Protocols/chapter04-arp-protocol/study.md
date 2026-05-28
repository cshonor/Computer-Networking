# 第 4 章：地址解析协议（ARP）

> 按书节速记：[4.1](4.1-introduction.md) · [4.2](4.2-arp-basic-operation.md) · [4.3](4.3-arp-cache.md) · [4.4](4.4-arp-packet-format.md) · [4.5](4.5-arp-tcpdump-example.md) · [4.6](4.6-arp-cache-timeout.md) · [4.7](4.7-proxy-arp.md) · [4.8](4.6-gratuitous-arp.md) · [4.9](4.9-arp-cli-commands.md) · [4.10](4.10-embedded-arp-setup.md) · [4.11](4.11-arp-spoof-defense.md) · [4.12](4.12-summary.md) · [QUICKREF §4](../QUICKREF.md)

> 《TCP/IP 详解》卷1 第 2 版（Fall, 2016）· 精细化学习笔记（同步自 [tcpip_vol1_ed2_notes](../../tcpip_vol1_ed2_notes/03_network_layer/ch04_arp.md)）  
> 链路层基础：[ch03 链路层](../chapter03-link-layer/study.md) · 自顶向下：[§6.4.1 ARP](../../top_down/06_link_layer_and_lan/study.md#ch6-4)

**ARP** 是 **IPv4 ↔ 以太网 MAC** 的战略支点：IP 提供端到端逻辑标识，**L2 交付必须靠 48 位 MAC**；硬件不识别 IP 标签，同网段内不能直接“按 IP 发帧”。

> **IPv6** 不用 ARP，而用 **邻居发现（ND，ICMPv6）** — 考点对照见 [ch08 ICMP](../chapter08-icmpv4-icmpv6/study.md)、[QUICKREF §4](../QUICKREF.md)。

---

<a id="ch04-1"></a>

## 4.1 引言与地址解析的必要性

→ 精读：[4.1 大白话](4.1-introduction.md) · [为何需要 ARP](4.1-introduction.md#ch04-1-why) · [触发条件](4.1-introduction.md#ch04-1-trigger) · [三行背诵](4.1-introduction.md#ch04-1-cheat)

- **功能**：**IPv4 → 以太网 MAC**（**RFC 826**）；**IPv6 用 ND**，不用 ARP。
- **范围**：**同一广播域**；跨网段 **ARP 网关**，不 ARP 远端主机。
- **L3/L2**：路由最终要坍缩成**下一跳 MAC**；ARP 是 IPv4 在以太网上的主要动态机制。

---

<a id="ch04-2"></a>

## 4.2 工作实例：直接交付与协议交互

→ 精读：[4.2](4.2-arp-basic-operation.md) · [每台设备 ARP 表不同](4.2-arp-basic-operation.md#ch04-2-per-device) · [路由表+ARP](4.2-arp-basic-operation.md#ch04-2-route-arp) · [端到端流程](4.2-arp-basic-operation.md#ch04-2-end-to-end)

### 何时走 ARP

主机判定目标 **B 与本机同一子网**（**IP + 掩码**匹配）→ **直接交付** → 必须先解析 **B 的 MAC** 再封装以太网帧。

| 概念 | 说明 |
|------|------|
| **直接交付** | 同一物理/广播域；掩码确认目标 IP 属本 subnet |
| **间接交付** | 跨子网：IP 目的为远端主机，**以太网目的 MAC 常为默认网关** |

→ 自顶向下必背：[§6.4.1](../../top_down/06_link_layer_and_lan/study.md#ch6-4)

### ARP 请求/响应循环

**按需触发**：缓存未命中时，常**挂起**待发 IP 数据报，先完成 ARP → **首包额外延迟**。

```text
1. 查内核 ARP 缓存
2. Miss → 构造 ARP 请求
   · 以太网目的 MAC = ff:ff:ff:ff:ff:ff（广播）
   · 子网内所有活动主机收到
3. 仅 IP 匹配的目标处理请求
4. 目标以单播 ARP 应答回请求方（请求里已有源 MAC）
```

### 效率逻辑

| 报文 | 为何 |
|------|------|
| **请求广播** | 尚不知目标 MAC，需覆盖全网段 |
| **应答单播** | 已知请求方 MAC，减少无关流量 |

---

<a id="ch04-3"></a>

## 4.3 ARP 缓存：效率优化的核心

避免反复广播（**广播风暴**）与重复解析开销。

### 条目字段

| 字段 | 作用 |
|------|------|
| **IP 地址** | 逻辑检索键 |
| **MAC 地址** | 映射结果 |
| **类型** | **dynamic**（协议学习）/ **static**（手工） |
| **Timeout** | 生命周期 |

### 典型 `arp -a` 映射

| Internet Address | Physical Address | Type |
|------------------|------------------|------|
| 192.168.1.1 | 00-50-56-c0-00-08 | dynamic |
| 192.168.1.254 | 00-0c-29-3e-0a-4b | static |

（Linux 现代等价：`ip neigh show`）

### 状态与超时

| 状态 | 说明 |
|------|------|
| **完整条目** | 解析成功；常见存活约 **20 分钟**（因内核而异） |
| **Incomplete** | 已发请求、未收到应答的临时项 |
| **自愈** | 超时删除陈旧映射 → 网卡更换 / IP 变更后可重新学习 |

### 风险

**Incomplete 堆积**：高频发往“尚未解析”的 IP 时，可能耗尽缓存资源 → 类似 **ARP Flooding** 的 DoS 面。

---

<a id="ch04-4"></a>

## 4.4 ARP 帧格式详解

ARP 是**链路层负载**（以太网类型 **0x0806**），**不**封装在 IP 数据报内。

### 28 字节首部（IPv4 + Ethernet）

按 **32 位对齐** 布局（字段顺序以 RFC 826 / 本书为准）：

| 字段 | 典型值 | 含义 |
|------|--------|------|
| 硬件类型 | **1** | 以太网 (802.3) |
| 协议类型 | **0x0800** | IPv4 |
| 硬件地址长度 | **6** | MAC |
| 协议地址长度 | **4** | IPv4 |
| **操作码 Opcode** | **1** = 请求，**2** = 应答 | |
| 发送方硬件/协议地址 | MAC + IP | |
| 目标硬件/协议地址 | MAC + IP | 请求时目标 MAC 常为全 0 |

```text
以太网帧：[ 目的 MAC ] [ 源 MAC ] [ 0x0806 ] [ ARP 28B ] [ 可选填充 ] [ FCS ]
```

### 解析失败行为

对**不存在的主机**：多次 ARP 尝试后**静默超时**；链路层通常**不**向 IP 返回明确 ARP 错误 → 上层可能最终收到 **ICMP Host Unreachable** → ARP 的**尽力而为**语义。

---

<a id="ch04-5"></a>

## 4.5 特殊场景：代理 ARP 与免费 ARP

### 代理 ARP（Proxy ARP）

路由器在条件下**代答** ARP，使主机以为目标在**同一链路**。

| 利 | 弊 |
|----|-----|
| 简化“无默认路由”的主机配置 | **隐藏真实拓扑**；排障困难 |

### 免费 ARP（Gratuitous ARP）

主机**广播**“自己的 IP → 自己的 MAC”的 ARP（常表现为 **请求** 形态，目标 IP = 本机 IP）。

| 用途 | 行为 |
|------|------|
| **ACD（地址冲突检测）** | 若收到**应答** → 该 IP 已被占用 → **负面确认** |
| **缓存刷新** | 故障转移 / 换网卡后，迫使邻居更新 ARP 表 |

### 易混（盲区）

免费 ARP **不期望**收到回复；**收到回复 = 配置冲突信号**，不是“正常握手成功”。

---

<a id="ch04-6"></a>

## 4.6 管理工具、安全威胁与本质总结

### 管理

| 工具 | 用途 |
|------|------|
| `arp`（Windows/旧 Unix） | 查看/增删静态映射 |
| `ip neigh`（Linux） | 邻居表：ARP + 状态（REACHABLE/STALE…） |

### 嵌入式配置（§4.10 思路）

设备**尚无 IP**、无 DHCP 时：对已知 **MAC** 配置**静态 ARP**，并发送特定 **ICMP** 等诱导 → 辅助绑定固定 IPv4 — 体现 ARP 在**引导阶段**的配置能力（具体帧长/实现因设备而异）。

### ARP 欺骗 / 中毒（Spoofing）

| 根因 | 后果 |
|------|------|
| **无状态、无认证** | 内核倾向接受**最新** ARP 应答，即使非对应请求 |
| 伪造应答 | **MITM**、嗅探、篡改局域网流量 |

缓解（工程侧，非本书重点）：**DAI**、**静态绑定**、**802.1X**、主机 **静态邻居**、加密上层（TLS）等。

---

<a id="ch04-exam"></a>

## 考点复盘

### 技术本质（三条）

1. **L3 → L2**：逻辑路由必须落实为**下一跳 MAC**；ARP 是 IPv4 以太网上的动态粘合剂。  
2. **动态自适应**：设备上下线、IP 变更时无需手工维护全网 MAC 表。  
3. **信任模型脆弱**：效率来自**局域网互信** → 也是**最主要 L2 安全风险**之一。

### 易混对照

| 问题 | 要点 |
|------|------|
| ARP vs RARP | ARP：IP→MAC；RARP：MAC→IP（少见，DHCP 取代） |
| ARP vs ND | **IPv4/ARP**；**IPv6/ND（ICMPv6）** |
| 请求 vs 应答 | 广播 vs 单播 |
| 代理 ARP vs 默认网关 | 代理“假装同网段”；正常跨网段用**网关 MAC** |
| ARP 失败 vs ICMP | ARP 超时静默；路由/防火墙可能再报 **Host Unreachable** |

### 下一章

- [ch05 IP](../chapter05-ip-protocol/study.md) — 首部、分片、间接交付的完整路径  
- [ch03 §3.1 链路层职能](../chapter03-link-layer/study.md#ch03-1) — ARP 分用入口

---

## Top-Down

- [06_link_layer_and_lan/study.md §6.4.1](../../top_down/06_link_layer_and_lan/study.md#ch6-4)  
- [06 §6.7 Web 请求微观路径](../../top_down/06_link_layer_and_lan/study.md#ch6-7)（DNS 前常需 ARP 网关）

## Lab

- `arp -a` / `ip neigh` 对照本书缓存状态  
- Wireshark：`arp` 过滤器，观察广播请求与单播应答  
- 同一子网 ping 首包延迟（首 ARP 解析）

## Go / Rust

- **Go**：`net.Interface` 看本机 MAC；排障用 `exec` 调 `ip neigh` 或读 `/proc/net/arp`（Linux）  
- **Rust**：`pnet` / 抓包库解析 ARP；容器网络注意**邻居表**与 **hairpin**  
- **实践**：跨子网发包时区分 **dst IP（远端）** 与 **L2 dst MAC（网关）**
