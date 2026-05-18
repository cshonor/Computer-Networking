# 4.1 网络层概述 · 考点速记

> **自顶向下总览**：[../study.md#ch4-dp-topdown](../study.md#ch4-dp-topdown)（六步转发、输入/交换/输出）  
> 考试精读：[../study.md#ch4-1](../study.md#ch4-1) · RIB/FIB：[../study.md#ch4-1-rib-fib](../study.md#ch4-1-rib-fib)

## 数据平面一句

收包 → 取目的 IP → **查 FIB** → 交换结构 → 出端口发出（**不算路**）

## 控制平面一句

OSPF/BGP 算路 → **RIB** → 下发 **FIB**

## 三块硬件路径

输入端口 → 交换结构（内存/总线/**Crossbar**）→ 输出端口

## vs 控制平面

运输车（FIB） vs 画地图的人（RIB）

## 易混

- 只查 **FIB**，不查 RIB  
- 下一跳 = **邻居路由器接口 IP**

## 图

- [RIB/FIB](../assets/rib_fib_control_data_plane.png) · [Crossbar](../assets/crossbar_switching_fabric.png)
