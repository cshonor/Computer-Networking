# 4.1 网络层概述 · 考点速记

> 章级完整版：[../study.md#ch4-1](../study.md#ch4-1) · RIB/FIB 详版：[../study.md#ch4-1-rib-fib](../study.md#ch4-1-rib-fib)

## 数据平面

- **快、硬、局部** — 查 **FIB** → 转发（线速）
- 类比：**立交桥按路牌选出口**

## 控制平面

- **慢、软、全局** — 协议算路 → **RIB** → 下发 FIB
- 类比：**地图 App 规划全程**

## 转发 vs 路由

| 转发 | 路由 |
|------|------|
| 数据平面 · **FIB** | 控制平面 · **RIB** |
| 单跳查表 | 端到端算路 |

## 必背一句

**数据平面永远查 FIB；控制平面维护 RIB，最优路由下发成 FIB。**

## 口诀

**RIB 想清楚，FIB 干到底。**

## 图

- [RIB/FIB 架构](../assets/rib_fib_control_data_plane.png)
- [SDN 三层](../assets/sdn_controller_architecture.png)

## 100 字背版

见 [../study.md#ch4-1](../study.md#ch4-1) 第五节。
