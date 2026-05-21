# 2.4 CIDR 与聚合

> 章级精读：[../study.md#ch02-4](../study.md#ch02-4) · 控制平面：[§5 路由](../../../05_network_layer_control_plane/study.md)

## 本节核心目标

理解 **CIDR** 如何缓解地址枯竭与 **ROAD（路由表爆炸）**。

---

## 无类别域间路由 (CIDR)

- **废除 A/B/C 刚性边界**，前缀任意长度（如 `/21`）。
- 地址 = **网络前缀 + 主机部分**，由掩码/前缀长度界定。

---

## 路由聚合 (Aggregation / Supernet)

- 将多个**相邻小前缀**汇总为**更短一条**（超网），减少核心路由器 **FIB/RIB 表项**。
- 与 BGP 聚合、ISP 地址块分配强相关 → 见自顶向下 [§5 BGP](../../../05_network_layer_control_plane/5.3_bgp_inter_as_routing/study.md)。

---

## 考点

| 概念 | 一句话 |
|------|--------|
| CIDR | 无类前缀分配 |
| 聚合 | 多条路由变一条，**缩短前缀** |
