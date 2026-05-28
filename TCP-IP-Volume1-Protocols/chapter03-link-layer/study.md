# 第 3 章：链路层（Link Layer）

> 按书节速记：[3.1](3.1-introduction.md) · [3.2](3.2-ethernet-ieee802-encapsulation.md) · [Hub](3.2-hub-core.md) · [3.3](3.3-full-duplex-autoneg.md) · [3.4](3.4-bridge-switch-stp.md) · [3.5](3.5-wireless-80211.md) · [3.6](3.6-ppp-protocol.md) · [3.7](3.7-loopback-interface.md) · [3.8](3.8-mtu.md) · [3.9](3.9-tunnel-basics.md) · [3.10](3.10-link-layer-security.md) · [3.11](3.11-summary.md) · [3.12](3.12-references.md) · [QUICKREF §3](../QUICKREF.md)

> 《TCP/IP 详解》卷1 第 2 版（Fall, 2016）· 精细化学习笔记（同步自 [tcpip_vol1_ed2_notes](../../tcpip_vol1_ed2_notes/02_link_layer/ch03_link_layer.md)）  
> 自顶向下对照：[06_link_layer_and_lan/study.md](../../top_down/06_link_layer_and_lan/study.md)

链路层是协议栈**最底层**：在特定物理介质上收发比特流，为 **IP** 提供封装与分发，并支撑 **ARP/RARP**。

---

<a id="ch03-1"></a>

## 3.1 引言

### 定位

- **组帧（Framing）**：将 IP 数据报等封装为带首部/尾部的**帧**。
- **链路控制**：建链、维护、拆链、**差错检测**（通常不重传）。

### 三大职能

1. 为 **IP** 提供报文收发接口  
2. 支持 **ARP** 请求/应答  
3. 支持 **RARP**（特定环境）

### 承上启下

- 向下：驱动控制网卡等硬件  
- 向上：**多路复用** — 按类型字段分发给 IP、ARP 等

### 收发流程

| 方向 | 步骤 |
|------|------|
| **发送** | 网络层报文 → 加 MAC、类型字段 → 驱动发物理信号 |
| **接收** | 收信号 → **CRC** 校验 → 按类型**分用**到 IP/ARP |

### 结构（文本化图）

```text
        [ IP ] [ ARP ] [ RARP ]
              ↑    ↑      ↑
         链路层（以太网 / PPP / Wi-Fi …）
              ↓
           网卡 / 驱动
```

### 易混

**链路层可靠吗？** 多数局域网（以太网）**只检错丢弃、不重传**；Wi-Fi 等可有 **ACK** 等有限可靠机制。

---

<a id="ch03-2"></a>

## 3.2 以太网与 IEEE 802

**介质访问**：Hub + **CSMA/CD** + 一大冲突域（[Hub 精读](3.2-hub-core.md)）· Switch + MAC 表 + **每端口一域**  
**帧**：Ethernet II · **MTU 1500** · `0x0800/0806/86DD` · **FCS 只检错不重传** · 64–1518B  
**802.1Q Tag**：`0x8100` · TCI=**PCP(3)+DEI(1)+VID(12)** · VID **1–4094** · PCP **0–7**（6=语音）· **AX**=LACP

→ [TCI 详解](3.2-ethernet-ieee802-encapsulation.md#ch03-2-vlan-tci) · [帧结构](3.2-ethernet-ieee802-encapsulation.md#ch03-2-frame)

### 定位

现代局域网物理封装：**Ethernet II** 与 **IEEE 802.3** 深度互操作。

| 术语 | 说明 |
|------|------|
| **Ethernet II** | RFC 894，互联网最常用 |
| **LLC/SNAP** | RFC 1042，802.3 上承载 IP 等 |

### 知识点

- **802 族**：802.3 以太网、802.11 无线、802.1 桥接/VLAN  
- **类型字段判别**：值 **≥ 1536 (0x0600)** → **以太网类型**；**< 1536** → **802.3 长度** + LLC/SNAP  
- **802.1Q VLAN**：MAC 后插 **4 B** 标签  
- **802.1AX 聚合**：原 802.3ad，多链路捆绑

### 帧结构（文本化）

**Ethernet II**

```text
| 目的 MAC 6B | 源 MAC 6B | 类型 2B | 数据 46–1500B | FCS 4B |
```

**IEEE 802.3 + LLC/SNAP**

```text
前导码 7B + SFD 1B + 地址 + 长度 2B + LLC/SNAP 8B(含 0xAA-AA-03) + 数据 + FCS
```

### 封装流程

查 **MTU** → 以太网多用 **Ethernet II**；旧式 802 网可能多 **8 B LLC/SNAP**。

### 易混

**为何 Ethernet II 占主导？** 少 8 B 开销，处理更简单。

→ 分用类型字段：[ch01 §分用](../chapter01-overview/study.md#ch01-layering)（0x0800 = IPv4）

---

<a id="ch03-3"></a>

## 3.3 全双工、省电、自动协商与 802.3x

**半双工**：收发不能同时 · **CSMA/CD** · Hub  
**全双工**：可同时收发 · 交换点对点 · **冲突基本消失**  
**自动协商**：10/100/1000M + 双工；**千兆强制开**；优先级 **速率↑、全双工>半双工**  
**双工不匹配**：一端强全双工 + 一端自协商 → 对端常变半双工 → **丢包** · **光纤需手动配**

→ [双工+自协商](3.3-full-duplex-autoneg.md#ch03-3-cheat) · [魔术包流程](3.3-full-duplex-autoneg.md#ch03-3-magic-packet)

**WoL**：关机网卡监听 · **102B**=6×FF+MAC×16 · 网卡硬件唤醒 · **同局域网广播** · 不认 IP  
**EEE 802.3az**：空闲休眠、有流唤醒  
**802.3x**：全双工**二层逐跳** PAUSE（`0x8808`，`01:80:C2:00:00:01`）≠ **TCP 端到端**拥塞控制

→ [802.3x 完整版](3.3-full-duplex-autoneg.md#ch03-3-pause)

### 易混

| | 802.1X | 802.3x |
|--|--------|--------|
| 作用 | **端口接入认证** | **流量控制（PAUSE）** |

---

<a id="ch03-4"></a>

## 3.4 网桥与交换机

**学习**：源 MAC + 入端口 → **MAC 表**  
**转发**：已知单播 → **单端口**；端口**双向**（入/出看当前帧）  
**泛洪**：**本帧**除入端口外所有口（不回**本帧**进来的口；下一帧可从该口输出）  
**冲突域**：Hub=整网一大域 · Switch 全双工=**每端口一线**，端口间不冲突  
**广播域**：默认同一 · **VLAN** 隔离

→ [核心总览](3.4-bridge-switch-stp.md#ch03-4-core-summary) · [端口双向](3.4-bridge-switch-stp.md#ch03-4-port-bidir) · [STP](3.4-bridge-switch-stp.md#ch03-4-stp)

**环路危害**：S1↔S2 双链路例 → 帧转圈 · 广播风暴 · MAC 表震荡  
**STP/RSTP**：四台环 S0 根 · S3 **RP→S1** · 链路 S2–S3 上 **S3 侧 BP** · STP **30–50s** / RSTP **1–2s**  
**L2 交换**：MAC · 局域网内 · **L3 路由**：IP · 跨 VLAN/外网/AS

→ [STP 两台](3.4-bridge-switch-stp.md#ch03-4-stp-plain) · [四台选举](3.4-bridge-switch-stp.md#ch03-4-stp-4switch) · [根桥全DP·RP/DP](3.4-bridge-switch-stp.md#ch03-4-stp-rp-dp)

| | 交换机 | 路由器 |
|--|--------|--------|
| 层 | **L2 MAC** | **L3 IP** |

→ 自顶向下：[§6.4](../../top_down/06_link_layer_and_lan/study.md#ch6-4)

---

<a id="ch03-5"></a>

## 3.5 无线局域网（IEEE 802.11 / Wi-Fi）

**CSMA/CA**：先听 → 空闲 → **随机退避** → 发 → **ACK**（**避免**冲突，不 **CD**）  
**为何不用 CD**：发时**听不到别人**（近端掩蔽）  
**隐藏终端**：A、C 互不可闻，同时打 **AP** → AP 处撞车  
**RTS/CTS**：CTS 让能听见 AP 的站**静音**；大包常用

→ [CA vs CD](3.5-wireless-80211.md#ch03-5-cd-vs-ca) · [RTS/CTS 时序](3.5-wireless-80211.md#ch03-5-rts-cts-timeline) · [4 MAC 对照](3.5-wireless-80211.md#ch03-5-frame-mac) · [扫描/关联/认证](3.5-wireless-80211.md#ch03-5-bss-assoc)

| 术语 | 说明 |
|------|------|
| **CSMA/CA** | 载波监听 + **冲突避免**（Wi‑Fi） |
| **CSMA/CD** | 载波监听 + **冲突检测**（有线 Hub 半双工） |
| **NAV** | 虚拟载波监听，预约占用时长 |
| **DIFS / SIFS** | 发数据前等待 / ACK 前短等待（SIFS 优先级高） |

**帧**：最多 **4 MAC**（手机↔AP 常 **3**）；**SSID 名 / BSSID=AP MAC**  
**上线**：Beacon/Probe → **关联 AID** → **WPA 4 次握手**  
**物理**：802.11a/b/g → **11n** → **11ac/ax** · **安全**：WEP ✕ → **WPA2** → **WPA3**

→ 自顶向下：[§6.3](../../top_down/06_link_layer_and_lan/study.md#ch6-3) · 有线：[3.2 CSMA/CD](3.2-ethernet-ieee802-encapsulation.md#ch03-2-mac-evolution)

---

<a id="ch03-6"></a>

## 3.6 点到点协议（PPP）与 HDLC

**PPP 未废止**：Modem 少 · **PPPoE 宽带/移动网/跨厂商 WAN** 仍主流

**顺序**：**LCP** → **PAP/CHAP** → **NCP(IPCP 分 IP)** → 数据

| | PPP | HDLC |
|--|-----|------|
| 面向 | **字节** | **比特** |
| 认证 | **PAP/CHAP** | 无 |
| 场景 | **PPPoE**、跨厂商 | 同厂商串行专线 |

→ [仍用在哪](3.6-ppp-protocol.md#ch03-6-ppp-alive) · [LCP/NCP](3.6-ppp-protocol.md#ch03-6-ppp) · [对比](3.6-ppp-protocol.md#ch03-6-compare) · [PPPoE](3.6-ppp-protocol.md#ch03-6-pppoe) · [背诵](3.6-ppp-protocol.md#ch03-6-exam)

**易混**：PPP **无 MAC**、**无链路层可靠**；CHAP **优于** PAP。

---

<a id="ch03-7"></a>

## 3.7 环回（Loopback）

**127/8、::1** 不可路由 · **Loopback 口** 永 Up · **Router-ID** 优先环回最大 IP

**API**（程序接口）≠ **Loopback 口**（虚拟网络接口）

→ [127/::1](3.7-loopback-interface.md#ch03-7-addr) · [Router-ID](3.7-loopback-interface.md#ch03-7-rid) · [远程管理](3.7-loopback-interface.md#ch03-7-mgmt) · [速记表](3.7-loopback-interface.md#ch03-7-exam)

---

<a id="ch03-8"></a>

## 3.8 MTU 与路径 MTU

### 战略意义

**MTU** = 链路层帧对高层载荷上限；不匹配 → **IP 分片**多 → 效率↓、丢包风险↑。

| 术语 | 说明 |
|------|------|
| **MTU** | 单跳链路最大载荷 |
| **PMTUD** | **DF=1** 探测整条路径最小 MTU |

### 典型 MTU

| 链路 | MTU（字节，约） |
|------|-----------------|
| Hyperchannel | 65535 |
| 16M Token Ring | 17914 |
| **以太网** | **1500** |
| 802.3/802.2 | 1492 |
| PPP | 1500（常协商） |

### 流程

发 IP 包前查接口 MTU：  
- 超长且 **DF=0** → **IP 分片**  
- 超长且 **DF=1** → 丢弃 + **ICMP** 错误

### 易混

**链路层分片 vs IP 分片**：链路层通常**不分片**（超大帧丢弃）；**分片在 IP 层**。

→ 卷1 ch10 UDP + 本书 ch5：[ch10 UDP](../top_down/03_transport_layer/chapter10-udp-ip-fragment/study.md) · [§3.3 避免 IP 分片](../../top_down/03_transport_layer/study.md#ch3-3)

**Go/Rust**：`net.Interface` MTU；UDP 发送 ≤ MTU−IP/UDP 头；TCP **MSS** 由路径 MTU 推导。

---

<a id="ch03-9"></a>

## 3.9 隧道基础

**外层过路 / 内层到点** · **IPIP=4** · **GRE=47**

**MTU**：1500−隧道头（GRE 例 **1476**）· **PMTUD** 靠 ICMP，被拦易丢大包

→ [内外层头](3.9-tunnel-basics.md#ch03-9-encap) · [MTU/NAT/PMTUD](3.9-tunnel-basics.md#ch03-9-mtu-nat) · [IPIP/GRE](3.9-tunnel-basics.md#ch03-9-compare) · [口诀](3.9-tunnel-basics.md#ch03-9-exam)

---

<a id="ch03-10"></a>

## 3.10 链路层相关攻击

设计多假设**物理可信**，认证弱 → 易被滥用。

| 攻击 | 手段 |
|------|------|
| **MAC 泛洪** | 填满 CAM 表 → 交换机泛洪像 Hub → 嗅探 |
| **STP 劫持** | 伪造优根 BPDU → 流量引到攻击者 |
| **无线嗅探** | WEP/开放 WLAN → 见 [3.5](3.5-wireless-80211.md) |
| **ARP 欺骗** | 伪造 ARP → MITM → [ch04](../chapter04-arp-protocol/study.md) |
| **VLAN 跳跃** | DTP / 双 802.1Q 标签跨 VLAN |

**防护**：端口安全、802.1X、VLAN、BPDU/Root Guard；**不能替代 TLS/IPsec**。

→ 精读：[3.10](3.10-link-layer-security.md)（含 **5 条刷题对比表**）· [自顶向下 §8 分层攻击](../../top_down/08_network_security/layer-attacks-cheatsheet.md)

### 易混

**二层攻击**多在**同一广播域**；**三层**（如 BGP 劫持）可波及全球。

---

<a id="ch03-exam"></a>

## 3.11 总结与复盘

链路层通过**以太网 / Wi-Fi / PPP** 提供差异化介质访问，用 **MTU** 与**交换/STP** 解决边界与拓扑扩展。

| 协议 | 典型开销 | 默认 MTU | 场景 |
|------|----------|----------|------|
| **Ethernet II** | 18 B | **1500** | 有线局域网 |
| **802.11** | 24–34 B | ~2312 | 无线 |
| **PPP** | 5–8 B | 1500 | WAN 专线 |
| **Loopback** | 0（逻辑） | 65535 | 本机自测 |

**第一公里**：STP 收敛、Wi-Fi 的 CA，本质是在不确定物理环境下建立**尽量确定的逻辑连接**。

### 下一章

- [ch04 ARP](../chapter04-arp-protocol/study.md) — MAC 与 IP 映射  
- [ch05 IP](../chapter05-ip-protocol/study.md) — 网络层  
- [QUICKREF](../QUICKREF.md)
