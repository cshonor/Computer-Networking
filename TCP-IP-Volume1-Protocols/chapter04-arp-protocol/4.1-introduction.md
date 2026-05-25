# 4.1 引言

> 章级精读：[../study.md#ch04-1](../study.md#ch04-1) · 上一章：[ch03](../../chapter03-link-layer/study.md)

## 本节核心目标

理解 **ARP** 在 IPv4 中把 **IP 地址解析为 MAC 地址** 的使命。

---

## 核心要点

- 链路层转发看 **MAC**；IP 数据报下发以太网前必须知道**下一跳 MAC**。
- **ARP** 在同广播域内动态完成 **IP → MAC** 映射。
- **IPv6** 用 **ND（ICMPv6）** 替代 ARP → [ch08](../../chapter08-icmpv4-icmpv6/study.md)。

---

## 何时触发 ARP

- 本机要发送 IP 包，且目的 MAC **未知**（缓存未命中）。
- 跨子网时 ARP 的往往是**默认网关**的 MAC，而非远端主机 MAC。
