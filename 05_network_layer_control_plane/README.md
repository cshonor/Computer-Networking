# 第5章 网络层：控制平面

> 本章小节索引。每个子目录内均有 `README.md` / `study.md` / `demo_code/`。

本章覆盖**控制平面 vs 数据平面**、**路由算法（LS/DV）**、**OSPF**、**BGP**、**SDN 控制器**、**ICMP** 与 **SNMP/NETCONF** 等。完整精读见 **[study.md](./study.md)**。  
**入门**：[控制平面是什么](./study.md#ch5-control-plane-basics) · 对照 [第 4 章数据平面](../04_network_layer_data_plane/study.md)

**整理稿小节编号 ↔ 仓库目录**：文稿 **§5.1 概述** 与 **§5.2 路由算法** 合并入目录 **`5.1_routing_algorithm`**；**§5.3–5.7** 及章末总结分别对应 **`5.2`–`5.5`** 子目录与 `study.md` 锚点（**§5.6–5.7 与总结** 均在章内 [`study.md`](./study.md#ch5-6) 后半）。

## 小节列表

- [5.1_routing_algorithm](./5.1_routing_algorithm/README.md) — 控制平面范式、Per-router vs SDN、**LS/DV**（[§5.1–5.2](./study.md#ch5-1)）  
- [5.2_ospf_intra_as_routing](./5.2_ospf_intra_as_routing/README.md) — OSPF、区域、ABR/ASBR（[§5.3](./study.md#ch5-3)）  
- [5.3_bgp_inter_as_routing](./5.3_bgp_inter_as_routing/README.md) — BGP、eBGP/iBGP、属性与策略、Anycast（[§5.4](./study.md#ch5-4)）  
- [5.4_sdn_controller_plane](./5.4_sdn_controller_plane/README.md) — SDN 三层、OpenFlow 交互（[§5.5](./study.md#ch5-5)）  
- [5.5_icmp_snmp_network_manage](./5.5_icmp_snmp_network_manage/README.md) — ICMP、Traceroute、SNMP、NETCONF/YANG、章总结（[§5.6–5.8](./study.md#ch5-6)）  
