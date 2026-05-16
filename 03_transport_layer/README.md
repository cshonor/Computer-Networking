# 第3章 运输层

> 本章小节索引。每个子目录内均有 `README.md` / `study.md` / `problem.md` / `demo_code/`。

运输层实现**进程到进程**通信：多路复用/分解、**UDP**、可靠传输原理、**TCP**（连接、RTT、**流量控制 rwnd**、**拥塞控制**），以及 **QUIC / HTTP/3**。完整精读见 **[study.md](./study.md)**。

**与整理稿小节编号的对应**：文稿中 **§3.6 拥塞控制原理**、**§3.7 TCP 拥塞**、**§3.8 QUIC** 均在章内 `study.md` 中；仓库目录 **`3.6_tcp_flow_control`** 对应教材/文稿里的 **TCP 流量控制（rwnd）**（精读中置于 [§3.5 流量控制](./study.md#ch3-5-flow)）。

## 小节列表

- [3.1_transport_service_intro](./3.1_transport_service_intro/README.md) — 运输层角色、TCP/UDP、与网络层关系  
- [3.2_multiplexing_demultiplexing](./3.2_multiplexing_demultiplexing/README.md) — 端口、UDP/TCP 分解、监听与连接套接字  
- [3.3_udp_protocol](./3.3_udp_protocol/README.md) — UDP 首部、检验和、典型场景  
- [3.4_reliable_data_transfer_principle](./3.4_reliable_data_transfer_principle/README.md) — rdt、停等利用率、GBN/SR、窗口与序号  
- [3.5_tcp_connection_and_transmission](./3.5_tcp_connection_and_transmission/README.md) — TCP 段与字节流、RTT 与超时、握手挥手、与流量控制衔接  
- [3.6_tcp_flow_control](./3.6_tcp_flow_control/README.md) — **rwnd** 流量控制（见 [§3.5-flow](./study.md#ch3-5-flow)）  
- [3.7_tcp_congestion_control](./3.7_tcp_congestion_control/README.md) — 拥塞原理、TCP 拥塞控制、QUIC（[§3.6–3.8](./study.md#ch3-6)）  
