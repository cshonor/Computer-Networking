# Outline · TCP/IP Illustrated Vol.1, 2nd Ed. (Fall, 2016)

> **机械工业出版社 2016 · 全书 18 章**（非 29/30 章老版）。

## 目录结构（与仓库文件夹对齐）

```
tcpip_vol1_ed2_notes/
├─ 01_architecture/           # 体系架构
│  ├─ ch01_introduction.md
│  └─ ch02_internet_addresses.md
├─ 02_link_layer/             # 链路层
│  └─ ch03_link_layer.md
├─ 03_network_layer/          # 网络层
│  ├─ ch04_arp.md … ch08_icmpv4_icmpv6.md
├─ 04_transport_layer/        # 传输层（UDP + TCP）
│  ├─ ch09_broadcast_multicast.md
│  ├─ ch10_udp.md
│  ├─ ch12_tcp_intro.md … ch17_tcp_keepalive.md
├─ 05_application_security/   # 应用与安全
│  ├─ ch11_dns.md
│  └─ ch18_security.md
├─ VERSIONS.md
├─ QUICKREF.md                # 一页考点 + Go/Rust
└─ OUTLINE.md
```

## 官方 18 章目录

| 章 | 标题 | 笔记 |
|----|------|------|
| 1 | 概述 | [ch01](./01_architecture/ch01_introduction.md) |
| 2 | Internet 地址结构 | [ch02](./01_architecture/ch02_internet_addresses.md) |
| 3 | 链路层 | [ch03](./02_link_layer/ch03_link_layer.md) |
| 4 | ARP | [ch04](./03_network_layer/ch04_arp.md) |
| 5 | IP（IPv4/IPv6） | [ch05](./03_network_layer/ch05_ip.md) |
| 6 | 系统配置：DHCP | [ch06](./03_network_layer/ch06_dhcp.md) |
| 7 | 防火墙与 NAT | [ch07](./03_network_layer/ch07_firewall_nat.md) |
| 8 | ICMPv4/ICMPv6 | [ch08](./03_network_layer/ch08_icmpv4_icmpv6.md) |
| 9 | 广播与多播（IGMP/MLD） | [ch09](./04_transport_layer/ch09_broadcast_multicast.md) |
| 10 | UDP 与 IP 分片 | [ch10](./04_transport_layer/ch10_udp.md) |
| 11 | DNS | [ch11](./05_application_security/ch11_dns.md) |
| 12 | TCP 基础 | [ch12](./04_transport_layer/ch12_tcp_intro.md) |
| 13 | TCP 连接管理 | [ch13](./04_transport_layer/ch13_tcp_connection.md) |
| 14 | TCP 超时与重传 | [ch14](./04_transport_layer/ch14_tcp_timeout_retransmit.md) |
| 15 | TCP 数据流与窗口 | [ch15](./04_transport_layer/ch15_tcp_dataflow_window.md) |
| 16 | TCP 拥塞控制 | [ch16](./04_transport_layer/ch16_tcp_congestion.md) |
| 17 | TCP 保活 | [ch17](./04_transport_layer/ch17_tcp_keepalive.md) |
| 18 | 安全 | [ch18](./05_application_security/ch18_security.md) |

**一页速览**：[QUICKREF.md](./QUICKREF.md)

## 与自顶向下课程对照

| 本书（第 2 版） | 自顶向下仓库 |
|-----------------|--------------|
| 1–3 | [01](../01_network_basics/) · [06 链路](../06_link_layer_and_lan/) |
| 4–8 | [04 数据平面](../04_network_layer_data_plane/) · [05 控制](../05_network_layer_control_plane/) |
| 9–17 | [03 运输层](../03_transport_layer/study.md) |
| 11 | [02/2.4 DNS](../02_application_layer/2.4_dns_service/) |
| 18 | [08 安全](../08_network_security/) |

版本辨析 → [VERSIONS.md](./VERSIONS.md)
