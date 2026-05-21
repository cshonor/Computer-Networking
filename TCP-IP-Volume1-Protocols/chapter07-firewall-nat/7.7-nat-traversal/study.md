# 7.4 NAT 穿越 (NAT Traversal)

> 章级精读：[../study.md#ch07-4](../study.md#ch07-4) · [§7.3 NAT 类型](7.3-nat-napt/study.md)

## 本节核心目标

掌握 **打洞**、**STUN / TURN / ICE** — Go/Rust WebRTC、游戏、P2P 必备。

---

## 打洞 (Hole Punching)

- 内网主机先向**公网对端/服务器**发 UDP → NAT 建立**外向映射**。
- 对端再向该 **(公网IP, 端口)** 发包 → 可能穿入（取决于 NAT 类型）。

---

## 三剑客

| 协议 | 作用 |
|------|------|
| **STUN** | 查询“我在 NAT 外的 **(reflexive) IP:端口**” |
| **TURN** | 打洞失败时 **中继 Relay** 转发 |
| **ICE** | 候选地址收集 + 连通性检查，选**最优路径** |

---

## 实战（Go / Rust）

- **Go**：`pion/ice`、`pion/webrtc`
- **Rust**：`webrtc-rs`、`libp2p` + STUN
- 常退化为 TURN → 先查是否 **对称 NAT**、防火墙 UDP 超时。

---

## 保活

- NAT 映射空闲超时 → 需 **STUN binding 刷新** 或应用层心跳 → [ch17 TCP Keepalive](../../chapter17-tcp-keepalive/study.md)
