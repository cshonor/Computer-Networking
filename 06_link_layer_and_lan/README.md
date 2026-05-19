# 第6章 链路层和局域网

> 本章小节索引。每个子目录内均有 `README.md` / `study.md` / `demo_code/`。

本章覆盖**成帧与 MAC**、**差错检测（含 CRC）**、**多路访问**、**以太网/ARP/交换机/VLAN**、**MPLS**、**数据中心网络**及**全章串联回顾**。完整精读见 **[study.md](./study.md)**。

**目录与整理稿编号**：`6.1`–`6.4` 与 §6.1–6.4 一一对应；仓库仅 **`6.5_data_center_network`** 一节目录名，精读中 **§6.5 MPLS**、**§6.6 数据中心**、**§6.7–6.8** 均在章内 [`study.md`](./study.md#ch6-5)，由 **`6.5`** 子目录 README 汇总链接。

## 图

- [link_layer_position_hop_by_hop.png](./assets/link_layer_position_hop_by_hop.png) — 链路层逐跳位置（[§6.1](./study.md#ch6-link-layer-hop)）  
- [#ch6-hop-ip-frame](./study.md#ch6-hop-ip-frame) — **IP 不变 / 每跳重封帧** 原理 + 示意图  
- [#ch6-frame-vs-ip](./study.md#ch6-frame-vs-ip) — **以太网帧≠IP 报**、MAC/FCS 校验

## 小节列表

- [6.1 链路层服务](./6.1_link_layer_service/study.md) — 成帧、MAC、差错（[§6.1](./study.md#ch6-1)）  
- [6.2 差错检测](./6.2_error_detection_correction/study.md) — 奇偶、校验和、CRC、FEC（[§6.2](./study.md#ch6-2)）  
- [6.3 MAC 协议](./6.3_mac_protocol/study.md) — CSMA/CD、CSMA/CA（[§6.3](./study.md#ch6-3)）  
- [6.4 以太网/ARP/交换机](./6.4_ethernet_arp_switch_vlan/study.md) — VLAN、802.1Q（[§6.4](./study.md#ch6-4)）  
- [6.5 数据中心网络](./6.5_data_center_network/study.md) — 叶脊、东西向流量（[§6.5–6.8](./study.md#ch6-5)）  
