# 第3章 运输层

> 本章小节索引。每个子目录内均有 `README.md` / `study.md` / `demo_code/`。

运输层实现**进程到进程**通信：多路复用/分解、**UDP**、可靠传输原理、**TCP**（连接、RTT、**流量控制 rwnd**、**拥塞控制**），以及 **QUIC / HTTP/3**。完整精读见 **[study.md](./study.md)**。

**与整理稿小节编号的对应**：文稿中 **§3.6 拥塞控制原理**、**§3.7 TCP 拥塞**、**§3.8 QUIC** 均在章内 `study.md` 中；仓库目录 **`3.6_tcp_flow_control`** 对应教材/文稿里的 **TCP 流量控制（rwnd）**（精读中置于 [§3.5 流量控制](./study.md#ch3-5-flow)）。

## 图（部分）

| 图 | 说明 |
|----|------|
| [transport_multiplexing_demultiplexing.png](./assets/transport_multiplexing_demultiplexing.png) | 3.1/3.2 多路复用·解复用（三主机 P1～P4） |
| [udp_header_fields.png](./assets/udp_header_fields.png) | 3.3 UDP 首部四字段（8 字节） |
| [rdt3_stop_wait_lost_ack.png](./assets/rdt3_stop_wait_lost_ack.png) | 3.4 rdt3.0 ACK 丢失超时重传 |
| [stop_wait_channel_utilization.png](./assets/stop_wait_channel_utilization.png) | 3.4 停等信道利用率 U |
| [gbn_cumulative_ack.png](./assets/gbn_cumulative_ack.png) | 3.4 GBN 累积确认 |
| [gbn_error_retransmit.png](./assets/gbn_error_retransmit.png) | 3.4 GBN 丢包回退重传 |
| [tcp_three_way_handshake.png](./assets/tcp_three_way_handshake.png) | 3.5 TCP 三次握手状态图 |
| [tcp_four_way_handshake.png](./assets/tcp_four_way_handshake.png) | 3.5 TCP 四次挥手与 TIME_WAIT |

## 小节列表

- [3.1 运输层概述](./3.1_transport_service_intro/study.md) — 进程到进程、复用分用图、端口、TCP/UDP、30 字背诵  
- [3.2 复用与分用](./3.2_multiplexing_demultiplexing/study.md) — 多进一/一进多、UDP目的端口/TCP四元组、30 字背诵  
- [3.3 UDP](./3.3_udp_protocol/study.md) — 8B首部读图、无连接不可靠、场景、UDP/TCP对比、30 字背诵  
- [3.4 可靠传输原理](./3.4_reliable_data_transfer_principle/study.md) — rdt演化、SW/GBN/SR对比、利用率公式、配图读图、50字背诵  
- [3.5 TCP 连接与传输](./3.5_tcp_connection_and_transmission/study.md) — 三次握手/四次挥手读图、序号ACK、快重传、50字背诵  
- [3.6 TCP 流量控制](./3.6_tcp_flow_control/study.md) — rwnd、滑动窗口（[§3.5-flow](./study.md#ch3-5-flow)）  
- [3.7 TCP 拥塞控制](./3.7_tcp_congestion_control/study.md) — cwnd、慢启动等（[§3.6–3.8](./study.md#ch3-6)）  
