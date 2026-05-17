# 18 章一页速览 · 考点 + Go/Rust（Fall 第 2 版）

> 配合 [OUTLINE.md](./OUTLINE.md) · 自顶向下精读 [03_transport_layer/study.md](../03_transport_layer/study.md)

| 章 | 主题 | 核心考点 | Go / Rust 场景 |
|----|------|----------|----------------|
| 1 | 概述 | 分层、端到端、**Socket API** | 一切网络编程入口 |
| 2 | 地址结构 | IPv4/IPv6、**CIDR**、特殊地址 | `net.IP` 解析、监听 `0.0.0.0` / `::` |
| 3 | 链路层 | 以太网帧、**MTU**、VLAN、Wi-Fi | MTU 影响 UDP/TCP 分包策略 |
| 4 | ARP | ARP 缓存、**邻居发现**（IPv6） | 容器/本机 ARP 表排障 |
| 5 | IP | 首部、**分片/重组**、IPv6 | 见 ch10：避免 IP 分片 |
| 6 | DHCP | 自动配置、租约 | 云主机/容器网络启动 |
| 7 | NAT/防火墙 | **NAT**、状态防火墙、ALG | K8s Service、端口映射、连接跟踪满 |
| 8 | ICMP | Ping、Traceroute、**PMTUD** | `ping`、路径 MTU 发现失败 |
| 9 | 广播/多播 | IGMP/MLD、多播地址 | 视频监控、服务发现（mDNS） |
| 10 | UDP | 无连接、**UDP+IP 分片** | **QUIC/游戏**：单包 ≤1400B；见 [§3.3](../03_transport_layer/study.md#ch3-3) |
| 11 | DNS | 解析流程、记录类型、**DNSSEC** | `net.Resolver`、超时、缓存 |
| 12 | TCP 基础 | 首部、序号、端口 | 抓包对照 [tcp_header.png](../03_transport_layer/assets/tcp_header.png) |
| 13 | TCP 连接 | **三次握手/四次挥手**、状态机、**TIME_WAIT** | 短连接耗尽端口；`SO_REUSEADDR`、连接池 → [§3.1](../03_transport_layer/study.md#ch3-1-tcp-conn) |
| 14 | 超时重传 | **RTT**、超时、**快速重传** | 调 `TCP_USER_TIMEOUT`、重试策略 |
| 15 | 数据流/窗口 | **rwnd**、滑动窗口、**Nagle**、延迟 ACK | **`SetNoDelay(true)`** / `set_nodelay(true)` 防小包卡顿 |
| 16 | 拥塞控制 | **cwnd**、慢启动、拥塞避免、AIMD | 高 BDP、BBR（扩展阅读）；[§3.7](../03_transport_layer/study.md#ch3-7) |
| 17 | 保活 | **Keepalive** 探测死连接 | 长连接探活 vs 应用层心跳 |
| 18 | 安全 | **TLS**、IPsec、EAP、DNSSEC | HTTPS、`rustls`/`crypto/tls`；[ch08 安全](../08_network_security/) |

## 五条易混（背）

1. **rwnd**（接收方） vs **cwnd**（网络）→ 发送 `min(rwnd, cwnd)`  
2. **TCP 分段**（MSS） vs **IP 分片**（MTU）→ UDP 大包怕后者  
3. **UDP 分用**：目的端口；**TCP**：四元组  
4. **TIME_WAIT**：主动关闭方、约 **2MSL**  
5. 第 2 版 **无** Telnet/FTP 章 → 应用协议看自顶向下第 2 章 + 工程实践

## 推荐学习顺序（后端）

`1→2→10→13→14→15→16` → 并行 [03_transport_layer/study.md](../03_transport_layer/study.md) → `5→7→11→18`
