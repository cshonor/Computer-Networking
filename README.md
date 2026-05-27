# computer_network_top_down

> 后端开发专用 · 计算机网络学习仓库  
> **三轨并行**：[自顶向下](top_down/) · [TCP/IP 详解 卷1](TCP-IP-Volume1-Protocols/) · [UNIX 网络编程 卷1](UNP_Vol1/)  
> 主攻：**HTTP/TCP/IP 原理、Socket 编程、抓包排障、安全与路由**

---

## 仓库目录（一眼看懂）

```
Computer-Networking/
├─ top_down/                      # 《自顶向下》Ch1–8 + 99 实践（01_–99_）
├─ TCP-IP-Volume1-Protocols/      # 《TCP/IP 详解》卷1 第2版（18 章，节笔记平铺在章目录）
├─ UNP_Vol1/                      # 《UNIX 网络编程》卷1（四阶段 Ch1–31，节笔记平铺）
├─ HTTP-The-Definitive-Guide/     # 《HTTP 权威指南》（按章 study.md）
├─ wireshark-packet-analysis/     # Wireshark 抓包实战笔记（英文目录，NotebookLM 友好）
└─ scripts/                       # 目录生成、链接修正等维护脚本
```

| 资料 | 入口 | 说明 |
|------|------|------|
| **自顶向下** | [top_down/README.md](top_down/README.md) | 章级 `study.md` + 小节 `*/study.md` |
| **TCP/IP 卷1** | [QUICKREF.md](TCP-IP-Volume1-Protocols/QUICKREF.md) · [OUTLINE.md](TCP-IP-Volume1-Protocols/OUTLINE.md) | `chapterNN-主题/` 下 `x.y-*.md` 与 `study.md` 同级 |
| **UNP 卷1** | [UNP_Vol1/README.md](UNP_Vol1/README.md) · [OUTLINE.md](UNP_Vol1/OUTLINE.md) | `ChapterNN_*/` 下 `x.y_*.md` 与 `study.md` 同级 |
| **HTTP 指南** | [HTTP-The-Definitive-Guide/](HTTP-The-Definitive-Guide/) | 应用层 HTTP 深化 |
| **Wireshark 实战** | [wireshark-packet-analysis/](wireshark-packet-analysis/) | 抓包笔记 · [study.md](wireshark-packet-analysis/study.md) · 配合 [99 实验](top_down/99_practice_wireshark_lab/) |

**双轨对照**：自顶向下 ↔ TCP/IP 卷1（各章 `study.md` 内互链）；写 Socket 时 **UNP** 与 **top_down §2.7 / §3** 对照。

---

## 专题速查（跨书）

| 主题 | 笔记 |
|------|------|
| **C/S → B/S 演进** | [TCP/IP 1.1](TCP-IP-Volume1-Protocols/chapter01-overview/1.1-architecture-principles.md#ch1-1-cs-bs) · [UNP 1.1](UNP_Vol1/1_BasicFoundation/Chapter01_Introduction/1.1_Overview.md#ch1-1-cs-bs) |
| **分层典型攻击** | [TCP/IP 1.8](TCP-IP-Volume1-Protocols/chapter01-overview/1.8-architecture-threat.md#ch1-8-attacks) · [一页背诵](top_down/08_network_security/layer-attacks-cheatsheet.md) |
| **日常上网链路三选一** | [§6.1](top_down/06_link_layer_and_lan/6.1_link_layer_service/study.md#ch6-1-daily)（以太网 / Wi‑Fi / PPPoE） |
| **TCP 封装与逐跳转发** | [§4 封装](top_down/04_network_layer_data_plane/study.md#ch4-encapsulation) · [全流程](top_down/04_network_layer_data_plane/study.md#ch4-packet-walkthrough) |
| **控制平面入门** | [§5 是什么](top_down/05_network_layer_control_plane/study.md#ch5-control-plane-basics) |

---

## 自顶向下 · 学习笔记导航

> 完整章表：[top_down/README.md](top_down/README.md)  
> 每章 **章级 `study.md`** = 精读；各小节 **`study.md`** = 背版（考点 + 易错 + 留白）。

### 第 1 章 · 网络基础 — [study.md](top_down/01_network_basics/study.md)

| 小节 | 笔记 |
|------|------|
| 1.1 互联网概述 | [study.md](top_down/01_network_basics/1.1_internet_overview/study.md) · [README 威胁地图](top_down/01_network_basics/1.1_internet_overview/README.md) |
| 1.2 网络边缘与接入 | [study.md](top_down/01_network_basics/1.2_network_edge_and_access/study.md) |
| 1.3 网络核心与交换 | [study.md](top_down/01_network_basics/1.3_network_core_switching/study.md) |
| 1.4 时延丢包吞吐量 | [study.md](top_down/01_network_basics/1.4_delay_loss_throughput/study.md) |
| 1.5 协议分层 | [study.md](top_down/01_network_basics/1.5_protocol_layer_architecture/study.md) |

### 第 2 章 · 应用层 — [study.md](top_down/02_application_layer/study.md)

| 小节 | 笔记 |
|------|------|
| 2.1 应用层原理 | [study.md](top_down/02_application_layer/2.1_network_application_principle/study.md) |
| 2.2 HTTP 与 Web | [study.md](top_down/02_application_layer/2.2_http_and_web/study.md) |
| 2.3 电子邮件 | [study.md](top_down/02_application_layer/2.3_email_smtp_pop3_imap/study.md) |
| 2.4 DNS | [study.md](top_down/02_application_layer/2.4_dns_service/study.md) |
| 2.5 P2P | [study.md](top_down/02_application_layer/2.5_p2p_file_distribution/study.md) |
| 2.6 视频流媒体 | [study.md](top_down/02_application_layer/2.6_video_streaming/study.md) |
| 2.7 UDP / TCP Socket | [UDP](top_down/02_application_layer/2.7_socket_programming_udp/study.md) · [TCP](top_down/02_application_layer/2.7_socket_programming_tcp/study.md) |
| 2.8 WZP 私有协议 | [study.md](top_down/02_application_layer/2.8_wzp_private_protocol/study.md) |

### 第 3 章 · 运输层 — [study.md](top_down/03_transport_layer/study.md)

| 小节 | 笔记 |
|------|------|
| 3.1 运输层概述 | [study.md](top_down/03_transport_layer/3.1_transport_service_intro/study.md) |
| 3.2 复用与分用 | [study.md](top_down/03_transport_layer/3.2_multiplexing_demultiplexing/study.md) |
| 3.3 UDP | [study.md](top_down/03_transport_layer/3.3_udp_protocol/study.md) |
| 3.4 可靠传输原理 | [study.md](top_down/03_transport_layer/3.4_reliable_data_transfer_principle/study.md) |
| 3.5 TCP 连接与传输 | [study.md](top_down/03_transport_layer/3.5_tcp_connection_and_transmission/study.md) |
| 3.6 TCP 流量控制 | [study.md](top_down/03_transport_layer/3.6_tcp_flow_control/study.md) |
| 3.7 TCP 拥塞控制 | [study.md](top_down/03_transport_layer/3.7_tcp_congestion_control/study.md) |

### 第 4 章 · 网络层数据平面 — [study.md](top_down/04_network_layer_data_plane/study.md)

| 小节 / 专题 | 笔记 |
|-------------|------|
| 4.1 网络层概述 | [study.md](top_down/04_network_layer_data_plane/4.1_network_layer_overview/study.md) |
| 4.2 路由器内部 | [study.md](top_down/04_network_layer_data_plane/4.2_router_internal_working/study.md) |
| 4.3 IPv4/IPv6/NAT | [study.md](top_down/04_network_layer_data_plane/4.3_ipv4_ipv6_nat/study.md) |
| 4.4 SDN/OpenFlow | [study.md](top_down/04_network_layer_data_plane/4.4_sdn_openflow/study.md) |
| **TCP⊂IP⊂MAC 封装** | [#ch4-encapsulation](top_down/04_network_layer_data_plane/study.md#ch4-encapsulation) |
| **逐跳转发全流程** | [#ch4-packet-walkthrough](top_down/04_network_layer_data_plane/study.md#ch4-packet-walkthrough) |

### 第 5 章 · 网络层控制平面 — [study.md](top_down/05_network_layer_control_plane/study.md)

| 小节 / 专题 | 笔记 |
|-------------|------|
| **控制平面是什么** | [#ch5-control-plane-basics](top_down/05_network_layer_control_plane/study.md#ch5-control-plane-basics) |
| 5.1 路由算法 | [study.md](top_down/05_network_layer_control_plane/5.1_routing_algorithm/study.md) |
| 5.2 OSPF | [study.md](top_down/05_network_layer_control_plane/5.2_ospf_intra_as_routing/study.md) |
| 5.3 BGP | [study.md](top_down/05_network_layer_control_plane/5.3_bgp_inter_as_routing/study.md) |
| 5.4 SDN 控制平面 | [study.md](top_down/05_network_layer_control_plane/5.4_sdn_controller_plane/study.md) |
| 5.5 ICMP/SNMP | [study.md](top_down/05_network_layer_control_plane/5.5_icmp_snmp_network_manage/study.md) |

### 第 6 章 · 链路层 — [study.md](top_down/06_link_layer_and_lan/study.md)

| 小节 | 笔记 |
|------|------|
| 6.1 链路层服务 | [study.md](top_down/06_link_layer_and_lan/6.1_link_layer_service/study.md) |
| 6.2 差错检测 | [study.md](top_down/06_link_layer_and_lan/6.2_error_detection_correction/study.md) |
| 6.3 MAC 协议 | [study.md](top_down/06_link_layer_and_lan/6.3_mac_protocol/study.md) |
| 6.4 以太网/ARP/交换机 | [study.md](top_down/06_link_layer_and_lan/6.4_ethernet_arp_switch_vlan/study.md) |
| 6.5 数据中心/MPLS | [study.md](top_down/06_link_layer_and_lan/6.5_data_center_network/study.md) |

### 第 7 章 · 无线网络（选学）— [study.md](top_down/07_wireless_mobile_network/study.md)

| 小节 | 笔记 |
|------|------|
| 7.1 Wi‑Fi / 802.11 | [study.md](top_down/07_wireless_mobile_network/7.1_wifi_802_11/study.md) |
| 7.2 4G/5G LTE | [study.md](top_down/07_wireless_mobile_network/7.2_4g_5g_lte/study.md) |
| 7.3 移动性管理 | [study.md](top_down/07_wireless_mobile_network/7.3_mobility_management/study.md) |

### 第 8 章 · 网络安全 — [study.md](top_down/08_network_security/study.md)

| 小节 / 专题 | 笔记 |
|-------------|------|
| **分层攻击一页表** | [layer-attacks-cheatsheet.md](top_down/08_network_security/layer-attacks-cheatsheet.md) |
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

## 后端必学路线（优先级）

1. **01 网络基础** → 五层、时延、分组交换  
2. **02 应用层** → HTTP、DNS、Socket 入门  
3. **03 运输层（重中之重）** → TCP/UDP、握手、可靠传输、拥塞  
4. **04–05 网络层** → 转发、OSPF/BGP  
5. **06 链路层** → MAC、ARP、交换机  
6. **08 安全** → TLS/HTTPS、威胁分层表  
7. **07 无线** → 用到再学  
8. **并行**：[UNP](UNP_Vol1/) 写代码 · [TCP/IP](TCP-IP-Volume1-Protocols/chapter01-overview/study.md) 抠协议细节  

---

## 小节目录规范（top_down）

| 路径 | 用途 |
|------|------|
| `README.md` | 小节速查 |
| `study.md` | 精读 / 背版 + 链到章级 |
| `demo_code/` | 示例代码 |

**UNP / TCP-IP**：节笔记为章目录下 `{节名}.md`，见各自 README。

---

## 学习目标

1. 吃透 **Socket**，能手写 TCP 客户/服务器  
2. 理解 TCP 机制，能分析粘包、断连、TIME_WAIT 等  
3. 掌握 **HTTP/HTTPS** 全流程，能对照抓包  
4. 具备路由、NAT、ARP、安全分层等排障常识  
5. 应对后端网络相关面试  

## 学习工具

- 抓包：Wireshark  
- 调试：`nc`、NetAssist 等  
- 语言：Go / Python / C（与 UNP 示例对照）  
- 教材：自顶向下 · TCP/IP 卷1 第2版 · UNP 卷1  

## 提交规范

```
feat: 新增xx章节笔记
docs: 补全/重组笔记与链接
refactor: 目录结构调整（如 top_down/）
code: 示例代码
fix: 修正知识点或链接
```
