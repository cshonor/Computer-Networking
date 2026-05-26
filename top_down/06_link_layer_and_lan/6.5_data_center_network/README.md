# 6.5 — data center network

## 说明（目录名 vs 整理稿）

本目录名为 **`data_center_network`**；精读文稿中 **§6.5 MPLS**、**§6.6 数据中心**、**§6.7 Web 历程**、**§6.8 总结** 均在章级 [`study.md`](../study.md) 中，请用下列锚点阅读。

## 知识点速记

- **MPLS**：标签交换、LDP、TE/FRR。  
- **叶脊 + ECMP**：东西向流量、高二分带宽。  
- **Web 历程**：DHCP → ARP/DNS → 逐跳封装 → TCP/HTTP。  
- **实践**：VLAN 规模、**STP 与数据中心 L3 Clos 的取舍**、**LACP（802.1AX）**。

## 与后端开发的联系

- 云上 VPC、专线、DCI；本地机架布线、ToR 上行、MLAG。

## 延伸阅读

- [§6.5 MPLS](../study.md#ch6-5) · [§6.6 数据中心](../study.md#ch6-6) · [§6.7 Web 历程](../study.md#ch6-7) · [§6.8 总结](../study.md#ch6-8)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `demo_code/` | 示例代码 |
