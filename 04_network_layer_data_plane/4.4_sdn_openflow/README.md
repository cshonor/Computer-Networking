# 4.4 — sdn openflow

## 知识点速记

- **泛化转发**：**Match + Action**；不限于目的 IP。  
- **流表项**：匹配字段、计数器、动作（转发/丢弃/**改写字段**）。  
- **能力**：同设备上可实现转发、ACL、LB/NAT 等策略（依表项与 pipeline）。

## 与后端开发的联系

- 云网络可编程数据平面、Service Mesh 旁路、零信任策略下发，与「流级策略」思维相通。

## 延伸阅读

- 章级精读：[study.md § 4.4](../study.md#ch4-4)（含 [SDN 架构图](../assets/sdn_controller_architecture.png)）  
- **中间盒与章末总结**：[§4.5](../study.md#ch4-5) · [§4.6](../study.md#ch4-6)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `demo_code/` | 示例代码 |
