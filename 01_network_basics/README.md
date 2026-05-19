# 第1章 计算机网络和因特网

> 本章小节索引。每个子目录内均有 `README.md` / `study.md` / `demo_code/`。

本章建立全局视角：从**网络边缘**到**网络核心**，理解**分组交换**、**时延与吞吐量**、**分层与封装**，并初步接触**安全威胁**与**发展脉络**。完整精读笔记（含 1.6–1.8）见 **[study.md](./study.md)**。

## 图

| 图 | 说明 |
|----|------|
| [internet_edge_and_core.png](./assets/internet_edge_and_core.png) | 1.1 边缘 vs 核心 |
| [isp_hierarchy.png](./assets/isp_hierarchy.png) | 1.1 ISP 层级 |
| [network_edge_last_mile.png](./assets/network_edge_last_mile.png) | 1.2 边缘·最后一公里 |
| [access_cable_hfc.png](./assets/access_cable_hfc.png) | 1.2 同轴/HFC |
| [access_ftth.png](./assets/access_ftth.png) | 1.2 FTTH 光纤到户 |
| [routing_vs_forwarding.png](./assets/routing_vs_forwarding.png) | 1.3 路由 vs 转发 |
| [packet_switching_store_forward.png](./assets/packet_switching_store_forward.png) | 1.3 存储转发·数据报/虚电路 |
| [virtual_circuit.png](./assets/virtual_circuit.png) | 1.3 虚电路 VCI 换标 |
| [http_response_structure.png](./assets/http_response_structure.png) | 1.5 HTTP 响应结构 |
| [smtp_message_structure.png](./assets/smtp_message_structure.png) | 1.5 SMTP 邮件三段 |
| [ssh2_binary_packet.png](./assets/ssh2_binary_packet.png) | 1.5 SSH2 二进制包 |
| [tcp_segment_header.png](./assets/tcp_segment_header.png) | 1.5 TCP 段首部 |
| [udp_datagram_header.png](./assets/udp_datagram_header.png) | 1.5 UDP 首部与伪首部 |
| [ipv4_datagram_header.png](./assets/ipv4_datagram_header.png) | 1.5 IPv4 首部 |
| [ethernet_frame_structure.png](./assets/ethernet_frame_structure.png) | 1.5 以太网帧结构 |

## 小节列表

- [1.1 互联网概述](./1.1_internet_overview/study.md) — 五大点背诵 + 易错点  
- [1.2 网络边缘与接入](./1.2_network_edge_and_access/study.md) — 边缘/接入网/光猫一体机/WiFi 数据流、DSL/同轴/光纤、易错表  
- [1.3 网络核心与交换](./1.3_network_core_switching/study.md) — FDM/TDM通俗、分组≠TDM、数据报/虚电路、路由 vs 转发  
- [1.4 时延丢包吞吐量](./1.4_delay_loss_throughput/study.md) — 四大时延、La/R、公式例题、木桶吞吐、易错表  
- [1.5 协议分层](./1.5_protocol_layer_architecture/study.md) — PDU、TCP/UDP、IPv4/以太网帧、HTTP/SMTP/SSH（**1.6–1.8** 见 [章级](./study.md)）  
