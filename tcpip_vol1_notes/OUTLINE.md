# Study Outline · TCP/IP Illustrated, Vol.1

## 仓库目录（29/30 章通用）

```
tcpip_vol1_notes/
├─ 01_link_layer/
│  ├─ ch01_overview.md
│  └─ ch02_link_layer.md
├─ 02_network_layer/
│  ├─ ch03_ip.md … ch10_dynamic_routing.md
├─ 03_transport_layer/
│  ├─ ch11_udp.md … ch13_igmp.md
│  └─ ch17_tcp.md … ch25_tcp_performance.md
├─ 04_application_layer/
│  ├─ ch14_dns.md … ch16_bootp.md
│  ├─ ch26_telnet.md … ch29_snmp.md
│  └─ ch30_other_protocols.md   ←  mainly 1st ed.
├─ VERSIONS.md
├─ OUTLINE.md
└─ README.md
```

---

## 第 2 版标准目录（29 章）

| 章 | 标题 | 笔记文件 |
|----|------|----------|
| 1 | 概述 | [ch01](./01_link_layer/ch01_overview.md) |
| 2 | 链路层 | [ch02](./01_link_layer/ch02_link_layer.md) |
| 3 | IP：网际协议 | [ch03](./02_network_layer/ch03_ip.md) |
| 4 | ARP | [ch04](./02_network_layer/ch04_arp.md) |
| 5 | RARP | [ch05](./02_network_layer/ch05_rarp.md) |
| 6 | ICMP | [ch06](./02_network_layer/ch06_icmp.md) |
| 7 | Ping | [ch07](./02_network_layer/ch07_ping.md) |
| 8 | Traceroute | [ch08](./02_network_layer/ch08_traceroute.md) |
| 9 | IP 选路 | [ch09](./02_network_layer/ch09_ip_routing.md) |
| 10 | 动态选路 | [ch10](./02_network_layer/ch10_dynamic_routing.md) |
| 11 | UDP | [ch11](./03_transport_layer/ch11_udp.md) |
| 12 | 广播和多播 | [ch12](./03_transport_layer/ch12_broadcast_multicast.md) |
| 13 | IGMP | [ch13](./03_transport_layer/ch13_igmp.md) |
| 14 | DNS | [ch14](./04_application_layer/ch14_dns.md) |
| 15 | TFTP | [ch15](./04_application_layer/ch15_tftp.md) |
| 16 | BOOTP | [ch16](./04_application_layer/ch16_bootp.md) |
| 17 | TCP | [ch17](./03_transport_layer/ch17_tcp.md) |
| 18 | TCP 连接建立与终止 | [ch18](./03_transport_layer/ch18_tcp_connection.md) |
| 19 | TCP 交互数据流 | [ch19](./03_transport_layer/ch19_tcp_interactive_data.md) |
| 20 | TCP 成块数据流 | [ch20](./03_transport_layer/ch20_tcp_bulk_data.md) |
| 21 | TCP 超时与重传 | [ch21](./03_transport_layer/ch21_tcp_timeout_retransmit.md) |
| 22 | TCP 坚持定时器 | [ch22](./03_transport_layer/ch22_tcp_persist_timer.md) |
| 23 | TCP 保活定时器 | [ch23](./03_transport_layer/ch23_tcp_keepalive.md) |
| 24 | TCP 拥塞控制 | [ch24](./03_transport_layer/ch24_tcp_congestion.md) |
| 25 | TCP 未来与性能 | [ch25](./03_transport_layer/ch25_tcp_performance.md) |
| 26 | Telnet | [ch26](./04_application_layer/ch26_telnet.md) |
| 27 | FTP | [ch27](./04_application_layer/ch27_ftp.md) |
| 28 | SMTP | [ch28](./04_application_layer/ch28_smtp.md) |
| 29 | SNMP | [ch29](./04_application_layer/ch29_snmp.md) |
| 30 | （第 1 版常见）其他/拓展 | [ch30](./04_application_layer/ch30_other_protocols.md) |

第 1 版与第 2 版**仅差约一章**，传输层 **17–25**、网络层 **3–10** 为重点，与自顶向下 [第 3 章](../03_transport_layer/study.md) 高度重合。

---

## 分层考点摘要

### 链路层 + 网络层

- **核心**：MTU、ARP、IP 首部、分片与重组、CIDR 最长前缀匹配。  
- **易混**：**MAC（跳对跳）** vs **IP（端到端）**；**TCP 分段（MSS）** vs **IP 分片（MTU）**。

### 传输层

- **核心**：UDP 无状态；TCP 状态机；**rwnd（流量控制）** vs **cwnd（拥塞控制）** → `min(rwnd, cwnd)`。  
- **易混**：只看目的端口分用（UDP）vs 四元组（TCP）。

→ 精读：[03_transport_layer/study.md](../03_transport_layer/study.md) · [§3.2 分用](../03_transport_layer/study.md#ch3-2)

---

## 报文封装（复习）

```text
应用数据 → +TCP/UDP 头 → +IP 头 → +以太网帧 → 物理比特流
```

---

<a id="go-rust"></a>

## Go / Rust 实战 ↔ 卷1 章号

| 场景 | 卷1 章节 | 自顶向下精读 |
|------|----------|----------------|
| `TIME_WAIT`、端口耗尽 | **ch18** 连接建立与终止 | [§3.1 挥手](../03_transport_layer/study.md#ch3-1-tcp-conn) |
| Nagle + 延迟 ACK 小包卡顿 | **ch19** 交互数据流 | [§3.5 流控](../03_transport_layer/study.md#ch3-5-flow) |
| UDP 大包、IP 分片、QUIC 思路 | **ch11** UDP + **ch03** IP | [§3.3 UDP](../03_transport_layer/study.md#ch3-3) |

**实践速记**：连接池 / `SO_REUSEADDR`；Go 常默认 `SetNoDelay(true)`，Rust 需 `set_nodelay(true)`；UDP 应用层切块 **≤ ~1400 B** 避免 IP 分片。

---

## 与自顶向下仓库对照

| 卷1 | 自顶向下 |
|-----|----------|
| 1–2 | [01_network_basics](../01_network_basics/) · [06_link_layer](../06_link_layer_and_lan/) |
| 3–10 | [04](../04_network_layer_data_plane/) · [05](../05_network_layer_control_plane/) |
| 11–13, 17–25 | [03_transport_layer](../03_transport_layer/) |
| 14, 28 | [02 DNS / 邮件](../02_application_layer/) |
| 安全（第 2 版增补） | [08_network_security](../08_network_security/) |

版本细节 → [VERSIONS.md](./VERSIONS.md)
