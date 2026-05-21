# 3.8 MTU 和路径 MTU (PMTU)

> 章级精读：[../study.md#ch03-8](../study.md#ch03-8) · ICMP PTB：[ch08](../../chapter08-icmpv4-icmpv6/study.md) · TCP MSS：[ch13](../../chapter13-tcp-connection-manage/study.md)

## 本节核心目标

区分 **MTU**、**MSS**、**IP 分片** 与 **路径 MTU 发现**。

---

## MTU（最大传输单元）

- 链路层一帧能承载的**最大 IP 载荷**（以太网常见 **1500**）。
- 过大 IP 包 → 路由器**分片**（性能差）或 **DF 置位** 时丢弃并 ICMP 通知。

---

## 路径 MTU 发现 (PMTUD)

- 探测端到端路径上的**最小 MTU**，发送方避免中途分片。
- 依赖 **ICMP Fragmentation Needed / Packet Too Big**（勿被防火墙误拦）→ [ch08](../../chapter08-icmpv4-icmpv6/study.md)。

---

## 与上层关系

| 层 | 机制 |
|----|------|
| TCP | **MSS 选项** ≈ MTU − IP头 − TCP头 |
| UDP | 应用需控制单报大小，否则 **IP 分片** 脆弱 → [ch10](../../chapter10-udp-ip-fragment/study.md) |

---

## 五条易混（背一条）

**TCP 分段（MSS）** 在端系统；**IP 分片** 在网络层 — UDP 大包怕后者。
