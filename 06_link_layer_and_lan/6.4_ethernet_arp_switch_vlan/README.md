# 6.4 — ethernet arp switch vlan

## 知识点速记

- **MAC vs IP**；**跨子网 ARP**：目的 IP 是远端，**目的 MAC 是网关**。  
- **交换机自学习**：源 MAC 建表；未知目的泛洪。  
- **VLAN（802.1Q）**：逻辑隔离广播域与安全域。

## 与后端开发的联系

- K8s Service、MetalLB、VPC 内互通；排障先 `arp -a` / ND 与默认路由。

## 延伸阅读

- 章级精读：[study.md § 6.4](../study.md#ch6-4)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `problem.md` | 错题与面试题 |
| `demo_code/` | 示例代码 |
