# 第4章 网络层：数据平面

> 本章小节索引。每个子目录内均有 `README.md` / `study.md` / `problem.md` / `demo_code/`。

本章覆盖**转发与路由的区分**、**路由器体系结构**、**IPv4/IPv6/NAT/DHCP**、**SDN 与泛化转发**，以及**中间盒**与章末实践总结。完整精读见 **[study.md](./study.md)**。

**关于 §4.5–4.6**：仓库仅建有 **4.1–4.4** 子目录；**中间盒（§4.5）**与**本章总结（§4.6）**写在章级 [study.md](./study.md#ch4-5) 末尾两节。

## 小节列表

- [4.1_network_layer_overview](./4.1_network_layer_overview/README.md) — 数据/控制平面、转发 vs 路由、尽力而为  
- [4.2_router_internal_working](./4.2_router_internal_working/README.md) — 输入/交换/输出、LPM、排队、调度、缓冲  
- [4.3_ipv4_ipv6_nat](./4.3_ipv4_ipv6_nat/README.md) — IPv4 首部与分片、CIDR、DHCP、NAT、IPv6 与隧道  
- [4.4_sdn_openflow](./4.4_sdn_openflow/README.md) — Match+Action、流表示例；延伸阅读 [§4.5 中间盒](./study.md#ch4-5)  
