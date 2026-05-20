# 第 4 章：网络层 · 数据平面

> 本章笔记**只写数据平面**（转发、FIB、路由器硬件路径、可编程流表执行）。  
> **控制平面** → [../05_network_layer_control_plane/](../05_network_layer_control_plane/)

完整精读：**[study.md](./study.md)**

## 章内锚点

| 锚点 | 内容 |
|------|------|
| [#ch4-dp-topdown](./study.md#ch4-dp-topdown) | 总览、六步转发、输入/MAC |
| [#ch4-encapsulation](./study.md#ch4-encapsulation) | **TCP⊂IP⊂MAC** 嵌套、封装/解封装 |
| [#ch4-encapsulation-diagram](./study.md#ch4-encapsulation-diagram) | **一图汇总** + Wireshark 树形顺序 |
| [#ch4-packet-walkthrough](./study.md#ch4-packet-walkthrough) | **从零抠**：主机→路由器→下一跳，MAC/IP/FIB |
| [#ch4-fib](./study.md#ch4-fib) | 转发表 FIB |
| [#ch4-2](./study.md#ch4-2) | 四大件、Crossbar、排队调度 |
| [#ch4-4](./study.md#ch4-4) | Match+Action |

## 小节

- [4.1 网络层概述](./4.1_network_layer_overview/study.md) — 寻址选路转发、控制/数据平面、虚电路vs数据报、5行口诀  
- [4.2 路由器内部](./4.2_router_internal_working/study.md) — 四大件、Crossbar、FIB  
- [4.3 IPv4/IPv6/NAT](./4.3_ipv4_ipv6_nat/study.md) — CIDR、NAT、IPv6  
- [4.4 SDN/OpenFlow](./4.4_sdn_openflow/study.md) — 流表、Match+Action  

## 图

- [rib_fib_control_data_plane.png](./assets/rib_fib_control_data_plane.png) — 4.1 控制平面 RIB → 数据平面 FIB  
- [crossbar_switching_fabric.png](./assets/crossbar_switching_fabric.png)  
- [ipv4_datagram_header.png](./assets/ipv4_datagram_header.png) — IPv4 首部（[#ch4-ipv4-header](./study.md#ch4-ipv4-header) · [#Wireshark](./study.md#ch4-ipv4-wireshark)）
