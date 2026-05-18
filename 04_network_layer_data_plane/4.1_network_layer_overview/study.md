# 4.1 网络层概述 · 考点速记

> 章级完整版：[../study.md#ch4-1](../study.md#ch4-1)

## 数据平面

- **快、硬、局部** — 查表 → 排队 → 转发（线速）
- 类比：**立交桥按路牌选出口**

## 控制平面

- **慢、软、全局** — OSPF/BGP 算路 → 写转发表
- 类比：**地图 App 规划全程**

## 转发 vs 路由

| 转发 | 路由 |
|------|------|
| 数据平面 | 控制平面 |
| 单跳查表 **FIB** | 端到端算路 → **RIB** |
| 图 | [RIB/FIB](../assets/rib_fib_control_data_plane.png) |

## SDN

- **转控分离**：控制器集中决策；交换机 **Match + Action**
- **北向** REST（应用）· **南向** OpenFlow（交换机）· **东西向** 控制器互联
- 架构图：[../assets/sdn_controller_architecture.png](../assets/sdn_controller_architecture.png)

## 100 字背版

见 [../study.md#ch4-1](../study.md#ch4-1) 第五节。
