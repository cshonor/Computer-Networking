# 4.1 — 网络层概述

## 知识点速记

- **定位**：寻址 + 选路 + 转发；**主机到主机**
- **双平面**：[读图](./study.md#ch4-1-diagram-planes) · 控制 RIB/路由表 → **FIB** 转发
- **服务模型**：虚电路 vs **数据报（IP）**；互联网为何选数据报
- **分层**：链路一跳 / 网络全程 / 运输进程
- **背诵**：[5 行口诀](./study.md#ch4-1-exam)

## 与后端开发的联系

- VPC 路由、NAT、LB 都建立在 IP 转发与路由表 / FIB 语义之上

## 延伸阅读

- [study.md](./study.md) · [章级总览](../study.md#ch4-dp-topdown) · [控制平面](../../05_network_layer_control_plane/study.md)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记 |
| `study.md` | 可背诵完整版 |
| `demo_code/` | 示例代码 |
