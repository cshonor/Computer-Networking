# 9.4 IGMP 和 MLD

> 章级精读：[../study.md#ch09-4](../study.md#ch09-4) · ND/MLD：[ch08 §8.5](../../chapter08-icmpv4-icmpv6/8.5-ipv6-ndp/study.md)

## 本节核心目标

掌握 **Report/Query**、**IGMPv3 SSM**、**IGMP Snooping**。

---

## IGMP (IPv4) / MLD (IPv6)

| 报文 | 方向 | 作用 |
|------|------|------|
| **Report** | 主机→路由器 | 加入组播组 |
| **Query** | 路由器→子网 | 还有谁在看？刷新软状态 |

- 路由器维护**组播转发表（软状态）**；超时无 Report → 停止向 LAN 转发该组。

---

## 版本要点

| 版本 | 进步 |
|------|------|
| v1/v2 | 加入/离开、抑制 |
| **IGMPv3 / MLDv2** | **SSM**：订阅 **(S,G)** 特定源，更安全 |

---

## IGMP Snooping（交换机）

- 交换机**偷听** IGMP → 只向**有订阅者**的端口转发组播。
- 无 Snooping 时组播可能被当**广播泛洪**。

---

## 实战：「别人收得到我收不到」

1. **未指定网卡** Join 组播  
2. **未响应 Query** → 几分钟后被 Snooping **掐流**  
3. Wi‑Fi/AP 未透传组播

定期 **Report** 或由栈自动响应 Query。
