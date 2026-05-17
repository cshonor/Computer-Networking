# Study Outline · TCP/IP Illustrated Vol.1 (2nd Edition)

> 说明：早期笔记按**第 1 版 30 章**建目录，已作废。以下严格按**第 2 版 18 章**。

## 全书目录（18 章）

```
tcpip_illustrated_v2/
├─ 00_architecture/
│  ├─ ch01_overview.md
│  └─ ch02_internet_addresses.md
├─ 01_link_layer/
│  └─ ch03_link_layer.md
├─ 02_network_layer/
│  ├─ ch04_arp.md
│  ├─ ch05_ip.md
│  ├─ ch06_system_config_dhcp.md
│  ├─ ch07_firewall_nat.md
│  ├─ ch08_icmpv4_icmpv6.md
│  └─ ch09_broadcast_multicast.md   # 第2版：广播与本地多播
├─ 03_transport_layer/
│  ├─ ch10_udp.md
│  ├─ ch12_tcp_intro.md
│  ├─ ch13_tcp_connection.md
│  ├─ ch14_tcp_timeout_retransmit.md
│  ├─ ch15_tcp_dataflow_window.md
│  ├─ ch16_tcp_congestion.md
│  └─ ch17_tcp_keepalive.md
├─ 04_application_security/
│  ├─ ch11_dns.md
│  └─ ch18_security.md
├─ OUTLINE.md
└─ README.md
```

> 原书无第 9 章在部分提纲中省略；第 2 版含**广播与本地多播**相关章节，已单列 `ch09`。

---

## 一、整体知识框架（按分层归类）

### 体系与架构（Overview）

| 章 | 主题 | 笔记 |
|----|------|------|
| 1 | 概述：分层、端到端、套接字 API | [ch01](./00_architecture/ch01_overview.md) |
| 2 | Internet 地址：IPv4/IPv6、CIDR | [ch02](./00_architecture/ch02_internet_addresses.md) |

### 链路层（Link Layer）

| 章 | 主题 | 笔记 |
|----|------|------|
| 3 | 以太网帧、Wi-Fi、MTU、VLAN | [ch03](./01_link_layer/ch03_link_layer.md) |

### 网络层（Network Layer）

| 章 | 主题 | 笔记 |
|----|------|------|
| 4 | ARP 与邻居发现 | [ch04](./02_network_layer/ch04_arp.md) |
| 5 | IP 首部、分片、路由转发 | [ch05](./02_network_layer/ch05_ip.md) |
| 6 | DHCP 与自动配置 | [ch06](./02_network_layer/ch06_system_config_dhcp.md) |
| 7 | 防火墙与 NAT | [ch07](./02_network_layer/ch07_firewall_nat.md) |
| 8 | ICMPv4 / ICMPv6 | [ch08](./02_network_layer/ch08_icmpv4_icmpv6.md) |
| 9 | 广播与本地多播 | [ch09](./02_network_layer/ch09_broadcast_multicast.md) |

### 传输层（Transport Layer）

| 章 | 主题 | 笔记 |
|----|------|------|
| 10 | UDP、与 IP 分片交互 | [ch10](./03_transport_layer/ch10_udp.md) |
| 12 | TCP 初步 | [ch12](./03_transport_layer/ch12_tcp_intro.md) |
| 13 | 连接管理：握手、挥手、状态机 | [ch13](./03_transport_layer/ch13_tcp_connection.md) |
| 14 | 超时与重传、RTT、快速重传 | [ch14](./03_transport_layer/ch14_tcp_timeout_retransmit.md) |
| 15 | 数据流与窗口：滑动窗口、Nagle | [ch15](./03_transport_layer/ch15_tcp_dataflow_window.md) |
| 16 | 拥塞控制 | [ch16](./03_transport_layer/ch16_tcp_congestion.md) |
| 17 | 保活 Keepalive | [ch17](./03_transport_layer/ch17_tcp_keepalive.md) |

### 应用层与安全

| 章 | 主题 | 笔记 |
|----|------|------|
| 11 | DNS | [ch11](./04_application_security/ch11_dns.md) |
| 18 | 安全：IPsec、TLS/DTLS 等 | [ch18](./04_application_security/ch18_security.md) |

---

## 二、分层考点 · 难点 · 易混淆

### 1. 链路层与网络层

| 类型 | 内容 |
|------|------|
| **核心** | MTU、ARP 缓存、IPv4/IPv6 首部、IP 分片与重组 |
| **难点** | CIDR **最长前缀匹配**；IP 分片**偏移量**计算 |
| **易混** | **MAC（跳对跳）** vs **IP（端到端）** |
| **易混** | 以太网 **CSMA/CD** vs Wi-Fi **CSMA/CA**（隐藏终端） |

→ 自顶向下：[06_link_layer](../06_link_layer_and_lan/) · [04_network_layer](../04_network_layer_data_plane/)

### 2. 传输层（TCP/UDP）

| 类型 | 内容 |
|------|------|
| **核心** | UDP 无状态；TCP 状态机；滑动窗口；拥塞状态机 |
| **难点** | **流量控制（rwnd，接收方）** 与 **拥塞控制（cwnd，网络）** 协同；有效窗口 **min(rwnd, cwnd)** |
| **易混** | **TCP 分段（MSS，传输层）** vs **IP 分片（MTU，网络层）** — UDP 大包常触发后者 |

→ 自顶向下：[03_transport_layer/study.md](../03_transport_layer/study.md)

---

## 三、通俗理论与图示

### 1. 报文封装（Socket 发送路径）

```text
应用层数据 (Payload)
  ↓ 传输层 + TCP/UDP 首部        → Segment / Datagram
  ↓ 网络层 + IP 首部             → IP Datagram
  ↓ 链路层 + MAC 首部 + FCS      → Ethernet Frame
  ↓ 物理层比特流
```

接收方：各层查**本层标识**（如 IP 协议号 → TCP/UDP），剥头后上交。

### 2. 以太网帧（示意）

```text
| 目的 MAC(6) | 源 MAC(6) | 类型(2) | 载荷 46~1500 B | FCS(4) |
```

**最小载荷 46 B**：经典以太网为保证冲突检测，帧长 ≥ 64 B（含头部）。

---

## 四、Go / Rust 实战与章节映射

### 场景 1：端口耗尽与 `TIME_WAIT`

| 项 | 说明 |
|----|------|
| **痛点** | 高频短连接 RPC → `cannot assign requested address` |
| **章节** | **第 13 章** 主动关闭方 → **TIME_WAIT**，约 **2MSL** |
| **原理** | 防止迟滞报文污染**同四元组**新连接 |
| **实践** | **连接池**长连接；Linux **`SO_REUSEADDR`** / 调 `tcp_tw_reuse`（谨慎） |

→ 精读：[03_transport_layer §3.1 挥手](../03_transport_layer/study.md#ch3-1-tcp-conn)

### 场景 2：Nagle × 延迟 ACK → 小包卡顿

| 项 | 说明 |
|----|------|
| **痛点** | 游戏/键鼠同步，连续小包延迟几十～几百 ms |
| **章节** | **第 15 章** Nagle + 延迟 ACK **互相等待** |
| **实践** | **禁用 Nagle**：Go `TCPConn` 常默认 `SetNoDelay(true)`；Rust `set_nodelay(true)` |

→ 精读：[§3.5 流量控制](../03_transport_layer/study.md#ch3-5-flow)

### 场景 3：UDP 大包与 IP 分片（QUIC 思路）

| 项 | 说明 |
|----|------|
| **痛点** | UDP 一次 `send` 4000 B，公网**任一分片丢则整包废** |
| **章节** | **第 3、5、10 章** MTU、IP 分片 |
| **实践** | 应用层切块 **≤ ~1400 B** 再发 UDP；QUIC 自建可靠与重传 |

→ 精读：[§3.3 UDP](../03_transport_layer/study.md#ch3-3)

---

## 五、与自顶向下仓库对照（简表）

| 卷1 第2版 | 自顶向下 |
|-----------|----------|
| 1–2 | [01_network_basics](../01_network_basics/) |
| 3 | [06_link_layer](../06_link_layer_and_lan/) |
| 4–9 | [04](../04_network_layer_data_plane/) · [05](../05_network_layer_control_plane/) · [06](../06_link_layer_and_lan/) |
| 10–17 | [03_transport_layer](../03_transport_layer/) |
| 11 | [02/2.4 DNS](../02_application_layer/2.4_dns_service/) |
| 18 | [08_network_security](../08_network_security/) |

---

## 六、推荐阅读顺序（后端）

1. **ch01–02** → **ch10 UDP** + **ch13–16 TCP**（配合 `03_transport_layer/study.md`）
2. **ch05、ch07** IP/NAT（配合 `04_network_layer`）
3. **ch11 DNS** + **ch18 安全**
4. 链路/广播（ch03、ch09）与 Wireshark：[99_practice_wireshark_lab](../99_practice_wireshark_lab/)
