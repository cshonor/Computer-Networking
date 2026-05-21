# 9.3 组播

> 章级精读：[../study.md#ch09-3](../study.md#ch09-3) · UDP 绑定：[ch10](../../chapter10-udp-ip-fragment/study.md)

## 本节核心目标

掌握 **D 类 IP → 以太网 MAC** 映射与**三层过滤**。

---

## IPv4 组播 → MAC（必背）

- IP：`224.0.0.0/4`（D 类）
- MAC：`01:00:5e` + **23 bit** 来自组播 IP 低 23 位
- **32 个不同组播 IP → 同一 MAC**（哈希碰撞）→ 网卡可能收到**未订阅**组

---

## 三层过滤

```text
1. 网卡硬件过滤器（不完美）
2. 驱动
3. IP/套接字层 — JoinGroup 后软件丢弃非本组包
```

---

## Go / Rust 坑

- `JoinMulticast` / `join_multicast_v4` 必须指定 **`Interface`**（多网卡）。
- 未 Join → 收不到；Join 错网卡 → IGMP Report 发错接口。

---

## IPv6

- 前缀 `ff00::/8`；映射规则见章级精读（与 v4 类似有范围压缩）。
