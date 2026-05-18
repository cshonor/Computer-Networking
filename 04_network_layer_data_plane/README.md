# 第 4 章：网络层 · 数据平面

> 本章笔记**只写数据平面**（转发、FIB、路由器硬件路径、可编程流表执行）。  
> **控制平面** → [../05_network_layer_control_plane/](../05_network_layer_control_plane/)

完整精读：**[study.md](./study.md)**

## 章内锚点

| 锚点 | 内容 |
|------|------|
| [#ch4-dp-topdown](./study.md#ch4-dp-topdown) | 总览、六步转发、输入/MAC |
| [#ch4-fib](./study.md#ch4-fib) | 转发表 FIB |
| [#ch4-2](./study.md#ch4-2) | 四大件、Crossbar、排队调度 |
| [#ch4-4](./study.md#ch4-4) | Match+Action |

## 小节

- [4.1_network_layer_overview](./4.1_network_layer_overview/) — 数据平面定位、FIB  
- [4.2_router_internal_working](./4.2_router_internal_working/) — 输入/交换/输出  
- [4.3_ipv4_ipv6_nat](./4.3_ipv4_ipv6_nat/) — IP 首部、LPM、NAT（执行面）  
- [4.4_sdn_openflow](./4.4_sdn_openflow/) — 流表、泛化转发  

## 图

- [rib_fib_control_data_plane.png](./assets/rib_fib_control_data_plane.png)（下半 = FIB）  
- [crossbar_switching_fabric.png](./assets/crossbar_switching_fabric.png)
