# 第 3 章：链路层（Link Layer）

> 按书节速记：[3.1](3.1-introduction.md) · [3.2](3.2-ethernet-ieee802-encapsulation.md) · [3.3](3.3-full-duplex-autoneg.md) · [3.4](3.4-bridge-switch-stp.md) · [3.5](3.5-wireless-80211.md) · [3.6](3.6-ppp-protocol.md) · [3.7](3.7-loopback-interface.md) · [3.8](3.8-mtu.md) · [3.9](3.9-tunnel-basics.md) · [3.10](3.10-link-layer-security.md) · [3.11](3.11-summary.md) · [3.12](3.12-references.md) · [QUICKREF §3](../QUICKREF.md)

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

**介质访问**：Hub + **CSMA/CD** + 一大冲突域 · Switch + MAC 表 + **每端口一域**  
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

→ [STP 两台](3.4-bridge-switch-stp.md#ch03-4-stp-plain) · [四台选举](3.4-bridge-switch-stp.md#ch03-4-stp-4switch) · [RP≠本机DP](3.4-bridge-switch-stp.md#ch03-4-stp-rp-dp)

| | 交换机 | 路由器 |
|--|--------|--------|
| 层 | **L2 MAC** | **L3 IP** |

→ 自顶向下：[§6.4](../../top_down/06_link_layer_and_lan/study.md#ch6-4)

---

<a id="ch03-5"></a>

## 3.5 无线局域网（IEEE 802.11 / Wi-Fi）

### 定位

干扰与隐藏终端 → **CSMA/CA**（冲突**避免**，非 CD）。

| 术语 | 说明 |
|------|------|
| **CSMA/CA** | 载波监听 + 冲突避免 |
| **NAV** | 虚拟载波监听，预约信道占用时长 |

### MAC 要点

- **DIFS**：发数据前最小空闲等待  
- **SIFS**：ACK 前等待，**优先级最高**  
- **二进制指数退避**：冲突后随机退避  

### 物理演进

802.11a/b/g → **11n (MIMO)** → **11ac/ax**

### 安全

WEP（不安全）→ **WPA2 (AES)** → **WPA3**

### 交互（可选 RTS/CTS）

空闲 → DIFS → **RTS** → **CTS** → **Data** → **ACK**

### 四地址帧

**To DS / From DS** 标志决定地址个数；WDS/Mesh（11）用四地址；普通 AP 场景常用三地址。

### 易混

**为何不用 CSMA/CD？** 发送时难以同时检测远端微弱冲突（**近端掩蔽**）。

→ 自顶向下：[§6.3 多路访问](../../top_down/06_link_layer_and_lan/study.md#ch6-3)

---

<a id="ch03-6"></a>

## 3.6 点到点协议（PPP）与 HDLC

WAN 常用；无介质争用。精读 → [3.6 专节](./3.6-ppp-protocol.md) · [背诵清单](./3.6-ppp-protocol.md#ch03-6-exam)

| 协议 | 作用 |
|------|------|
| **LCP** | 链路参数（MRU、认证类型） |
| **NCP / IPCP** | 网络层参数（如分配 IP） |

**PPP 帧**：`7E | FF | 03 | 协议 2B | 载荷 | FCS | 7E`（**0x0021 = IP**）

| | PPP | HDLC |
|--|-----|------|
| 定位 | IETF、**异步+同步**、**PAP/CHAP**、无链路 ACK | ISO、**仅同步**、链路层**序号/确认**、无 IP 协商 |
| 关系 | PPP 帧**基于 HDLC 改造**，增 **Protocol** 字段 |

**易混**：PPP **不要 MAC**；PPP **无链路层可靠**（靠 TCP）；CHAP **优于** PAP。

---

<a id="ch03-7"></a>

## 3.7 环回（Loopback）

逻辑接口：数据**不经真实网卡**在协议栈内回流 — 排障与本地通信基础。

- **环回地址**：IPv4 **127.0.0.1**，IPv6 **::1**  
- 发往环回或本机 IP 的包可重定向到环回接口  
- 环回驱动直接放入**输入队列**

```text
应用 send → IP 识别 localhost → 在进链路层前“转弯” → IP 输入 → 套接字 recv
（无物理信号）
```

### 易混

**127.0.0.1** = 地址；**localhost** = 常通过 hosts/DNS 解析到该地址的名字。

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

在不支持某协议的网络里**嵌套承载**该协议（如 IPv6 over IPv4）。

- **封装**：内层包作为外层载荷  
- **单向链路**：卫星等场景  
- **递归隧道**：首部叠加，易 **MTU 溢出**（内层有效载荷常少 **≥20 B**）

```text
隧道入口： [ 外层 IPv4 头 ] + [ 内层 IPv6 头 ] + [ 数据 ]
         → 跨 IPv4 骨干 → 出口剥外层 → 还原 IPv6
```

---

<a id="ch03-10"></a>

## 3.10 链路层相关攻击

设计多假设**物理可信**，认证弱 → 易被滥用。

| 攻击 | 手段 |
|------|------|
| **MAC 泛洪** | 填满 MAC 表 → 交换机像集线器 → 嗅探 |
| **VLAN 跳跃** | 双 802.1Q 标签跨 VLAN |
| **STP 根劫持** | 高优先级 BPDU 夺根 → 截流 |

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
