# computer_network_top_down

> 后端开发专用 · 计算机网络（自顶向下方法）学习仓库  
> 主攻方向：**网络编程、Socket 通信、TCP/IP 底层、服务端网络原理**  
> 学习顺序：先应用层 → 运输层 → 网络层 → 链路层，贴合后端日常开发

## 仓库整体目录结构

```
Computer-Networking/
├─ top_down/                      # 自顶向下教材 Ch1–8 + 99 实践（01_–99_ 章节目录）
│  ├─ 01_network_basics … 08_network_security
│  └─ 99_socket_code_demo / 99_practice_wireshark_lab / 99_review_exercises_notes
├─ TCP-IP-Volume1-Protocols/      # TCP/IP 详解 卷1 第2版（18 章 chapterXX/study.md）
├─ UNP_Vol1/                      # UNIX 网络编程 卷1
└─ tcpip_vol1_ed2_notes/          # TCP/IP 精读源稿（可同步至 TCP-IP-Volume1-Protocols）
```

---

## 学习笔记导航（study.md）

每章 **章级 `study.md`** = 完整精读；各小节 **`*/study.md`** = 精简背版（考点 + 易错点 + 心得留白）。  
**双轨对照**：自顶向下（[top_down/](top_down/) 内 01–08）↔ [TCP/IP 卷1 第2版](TCP-IP-Volume1-Protocols/QUICKREF.md)（源稿：[tcpip_vol1_ed2_notes](tcpip_vol1_ed2_notes/QUICKREF.md)）

### 第 1 章 · 网络基础 — [01_network_basics/study.md](top_down/01_network_basics/study.md)

| 小节 | 笔记 |
|------|------|
| 1.1 互联网概述 | [study.md](top_down/01_network_basics/1.1_internet_overview/study.md) |
| 1.2 网络边缘与接入 | [study.md](top_down/01_network_basics/1.2_network_edge_and_access/study.md) |
| 1.3 网络核心与交换 | [study.md](top_down/01_network_basics/1.3_network_core_switching/study.md) |
| 1.4 时延丢包吞吐量 | [study.md](top_down/01_network_basics/1.4_delay_loss_throughput/study.md) |
| 1.5 协议分层 | [study.md](top_down/01_network_basics/1.5_protocol_layer_architecture/study.md) |

### 第 2 章 · 应用层 — [02_application_layer/study.md](top_down/02_application_layer/study.md)

| 小节 | 笔记 |
|------|------|
| 2.1 应用层原理 | [study.md](top_down/02_application_layer/2.1_network_application_principle/study.md) |
| 2.2 HTTP 与 Web | [study.md](top_down/02_application_layer/2.2_http_and_web/study.md) |
| 2.3 电子邮件 | [study.md](top_down/02_application_layer/2.3_email_smtp_pop3_imap/study.md) |
| 2.4 DNS | [study.md](top_down/02_application_layer/2.4_dns_service/study.md) |
| 2.5 P2P | [study.md](top_down/02_application_layer/2.5_p2p_file_distribution/study.md) |
| 2.6 视频流媒体 | [study.md](top_down/02_application_layer/2.6_video_streaming/study.md) |
| 2.7 UDP Socket | [study.md](top_down/02_application_layer/2.7_socket_programming_udp/study.md) |
| 2.7 TCP Socket | [study.md](top_down/02_application_layer/2.7_socket_programming_tcp/study.md) |
| 2.8 WZP 私有协议 | [study.md](top_down/02_application_layer/2.8_wzp_private_protocol/study.md) |

### 第 3 章 · 运输层 — [03_transport_layer/study.md](top_down/03_transport_layer/study.md)

| 小节 | 笔记 |
|------|------|
| 3.1 运输层概述 | [study.md](top_down/03_transport_layer/3.1_transport_service_intro/study.md) |
| 3.2 复用与分用 | [study.md](top_down/03_transport_layer/3.2_multiplexing_demultiplexing/study.md) |
| 3.3 UDP | [study.md](top_down/03_transport_layer/3.3_udp_protocol/study.md) |
| 3.4 可靠传输原理 | [study.md](top_down/03_transport_layer/3.4_reliable_data_transfer_principle/study.md) |
| 3.5 TCP 连接与传输 | [study.md](top_down/03_transport_layer/3.5_tcp_connection_and_transmission/study.md) |
| 3.6 TCP 流量控制 | [study.md](top_down/03_transport_layer/3.6_tcp_flow_control/study.md) |
| 3.7 TCP 拥塞控制 | [study.md](top_down/03_transport_layer/3.7_tcp_congestion_control/study.md) |

### 第 4 章 · 网络层数据平面 — [04_network_layer_data_plane/study.md](top_down/04_network_layer_data_plane/study.md)

| 小节 / 专题 | 笔记 |
|-------------|------|
| 4.1 网络层概述 | [study.md](top_down/04_network_layer_data_plane/4.1_network_layer_overview/study.md) |
| 4.2 路由器内部 | [study.md](top_down/04_network_layer_data_plane/4.2_router_internal_working/study.md) |
| 4.3 IPv4/IPv6/NAT | [study.md](top_down/04_network_layer_data_plane/4.3_ipv4_ipv6_nat/study.md) |
| 4.4 SDN/OpenFlow | [study.md](top_down/04_network_layer_data_plane/4.4_sdn_openflow/study.md) |
| **TCP⊂IP⊂MAC 封装** | [#ch4-encapsulation](top_down/04_network_layer_data_plane/study.md#ch4-encapsulation) |
| **逐跳转发全流程** | [#ch4-packet-walkthrough](top_down/04_network_layer_data_plane/study.md#ch4-packet-walkthrough) |

### 第 5 章 · 网络层控制平面 — [05_network_layer_control_plane/study.md](top_down/05_network_layer_control_plane/study.md)

| 小节 / 专题 | 笔记 |
|-------------|------|
| **控制平面是什么** | [#ch5-control-plane-basics](top_down/05_network_layer_control_plane/study.md#ch5-control-plane-basics) |
| 5.1 路由算法 | [study.md](top_down/05_network_layer_control_plane/5.1_routing_algorithm/study.md) |
| 5.2 OSPF | [study.md](top_down/05_network_layer_control_plane/5.2_ospf_intra_as_routing/study.md) |
| 5.3 BGP | [study.md](top_down/05_network_layer_control_plane/5.3_bgp_inter_as_routing/study.md) |
| 5.4 SDN 控制平面 | [study.md](top_down/05_network_layer_control_plane/5.4_sdn_controller_plane/study.md) |
| 5.5 ICMP/SNMP | [study.md](top_down/05_network_layer_control_plane/5.5_icmp_snmp_network_manage/study.md) |

### 第 6 章 · 链路层 — [06_link_layer_and_lan/study.md](top_down/06_link_layer_and_lan/study.md)

| 小节 | 笔记 |
|------|------|
| 6.1 链路层服务 | [study.md](top_down/06_link_layer_and_lan/6.1_link_layer_service/study.md) |
| 6.2 差错检测 | [study.md](top_down/06_link_layer_and_lan/6.2_error_detection_correction/study.md) |
| 6.3 MAC 协议 | [study.md](top_down/06_link_layer_and_lan/6.3_mac_protocol/study.md) |
| 6.4 以太网/ARP/交换机 | [study.md](top_down/06_link_layer_and_lan/6.4_ethernet_arp_switch_vlan/study.md) |
| 6.5 数据中心/MPLS | [study.md](top_down/06_link_layer_and_lan/6.5_data_center_network/study.md) |

### 第 7 章 · 无线网络（选学）— [07_wireless_mobile_network/study.md](top_down/07_wireless_mobile_network/study.md)

| 小节 | 笔记 |
|------|------|
| 7.1 Wi‑Fi / 802.11 | [study.md](top_down/07_wireless_mobile_network/7.1_wifi_802_11/study.md) |
| 7.2 4G/5G LTE | [study.md](top_down/07_wireless_mobile_network/7.2_4g_5g_lte/study.md) |
| 7.3 移动性管理 | [study.md](top_down/07_wireless_mobile_network/7.3_mobility_management/study.md) |

### 第 8 章 · 网络安全 — [08_network_security/study.md](top_down/08_network_security/study.md)

| 小节 | 笔记 |
|------|------|
| 8.1 密码学基础 | [study.md](top_down/08_network_security/8.1_basic_cryptography/study.md) |
| 8.2 完整性与签名 | [study.md](top_down/08_network_security/8.2_message_integrity_signature/study.md) |
| 8.3 TLS/HTTPS | [study.md](top_down/08_network_security/8.3_tls_https/study.md) |
| 8.4 IPsec/VPN | [study.md](top_down/08_network_security/8.4_ipsec_vpn/study.md) |
| 8.5 防火墙/IDS | [study.md](top_down/08_network_security/8.5_firewall_ids/study.md) |

### 实践与复习

| 目录 | 说明 |
|------|------|
| [99_practice_wireshark_lab](top_down/99_practice_wireshark_lab/) | Wireshark 抓包实验 |
| [99_socket_code_demo](top_down/99_socket_code_demo/) | Socket 示例代码 |
| [99_review_exercises_notes](top_down/99_review_exercises_notes/) | 习题与面试整理 |

---

## 后端必学核心路线（优先级从高到低）

1. **01 网络基础**：建立整体网络认知，看懂时延、分组交换、五层模型  
2. **02 应用层**：HTTP、DNS、邮件、Socket 入门，写服务端接口必备  
3. **03 运输层（重中之重）**
   - UDP 无连接通信  
   - TCP 三次握手、四次挥手、可靠传输、流量控制、拥塞控制  
   - 后端服务通信、长连接、短连接与这一章强相关  
4. **04–05 网络层**：数据平面转发 + 控制平面路由（OSPF/BGP）  
5. **06 链路层**：MAC、ARP、交换机原理  
6. **08 网络安全**：HTTPS、TLS、加密、防火墙  
7. **07 无线**：工作用到再学  

## 小节目录统一规范

每个小节文件夹内固定包含：

| 路径 | 用途 |
|------|------|
| `README.md` | 本章知识点精简笔记（速查） |
| `study.md` | 个人精读学习笔记（小节背版 + 链到章级） |
| `demo_code/` | 对应语言网络编程示例（Java / Go / Python / C++ 等） |

## 学习目标

1. 吃透 **Socket 网络编程**，能手写 TCP 服务端与客户端  
2. 理解 TCP 底层机制，能分析连接异常、粘包、断连等问题  
3. 掌握 **HTTP** 完整请求流程，能对照抓包看懂接口全链路  
4. 具备后端服务网络调优与线上网络问题排查的基本功  
5. 从容应对后端开发中的网络相关面试  

## 学习工具

- 抓包：Wireshark  
- 网络调试：NetAssist、`nc` 等  
- 编程环境：Go / Python / Java（任选其一为主即可）  
- 参考书：《计算机网络：自顶向下方法》  

## 提交规范

```
feat: 新增xx章节笔记
code: 完成TCP服务端代码
fix: 修正网络知识点错误
note: 整理面试网络题
```
