# 7.6 IPv4/IPv6 共存和过渡中的 NAT

> 章级精读：[../study.md#ch07-6](../study.md#ch07-6) · DNS：[ch11](../../chapter11-dns-domain-resolve/study.md)

## 本节核心目标

了解 **DS-Lite**、**NAT64/DNS64** 在 v6 演进中的角色。

---

## DS-Lite

- 用户侧 **IPv4 私网** 流量封装进 **IPv6 隧道** 到运营商 **CGN** 再做 NAPT。
- 减轻家庭侧公网 v4 需求。

---

## NAT64 + DNS64

- **纯 IPv6 客户端** 访问 **IPv4 服务器**：
  - **DNS64** 合成 **AAAA**（指向 NAT64 前缀）
  - **NAT64** 将 v6 包译为 v4 并转发

---

## 考点

- NAT64 是**过渡**手段，长期目标是原生 v6 端到端。
