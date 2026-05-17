# 第 10 章：用户数据报协议（UDP）与 IP 分片

> 《TCP/IP 详解》卷1 第 2 版（Fall, 2016）· 精细化学习笔记  
> 前置：[ch05 IP](../03_network_layer/ch05_ip.md) · [ch03 MTU](../02_link_layer/ch03_link_layer.md#ch03-8) · [ch08 PMTUD](../03_network_layer/ch08_icmpv4_icmpv6.md#ch08-3)  
> 自顶向下精读：[§3.3 UDP](../../03_transport_layer/study.md#ch3-3) · 首部图：[udp_header_fields.png](../../03_transport_layer/assets/udp_header_fields.png)

**UDP** 不是「简陋的不可靠协议」，而是传输层**极简主义**：仅提供**端口解复用**与**可选/强制校验和**，把拥塞控制、重传、流控交给应用层 — **QUIC、RoCE、实时音视频** 的基石。极简也暴露底层风险：**超 MTU → IP 分片** 时的连锁丢包与安全面。

---

<a id="ch10-1"></a>

## 10.1–10.2 UDP 核心架构

### 定位

| 特性 | 说明 |
|------|------|
| **无连接** | 无握手，无连接状态 |
| **尽力而为** | 继承 IP：可能丢包、**乱序**（ECMP 多路径尤甚） |
| **消息边界** | 一次 `write` → 一个 UDP 数据报；`read` 得完整报文，**无 TCP 粘包** |

### UDP 首部（8 字节）

![UDP 首部](../../03_transport_layer/assets/udp_header_fields.png)

| 字段 | 位宽 | 工程意义 |
|------|------|----------|
| 源端口 | 16 | 可选；不需回访可置 **0** |
| **目的端口** | 16 | **解复用**键 → 套接字队列 |
| UDP 长度 | 16 | 头+数据；理论最大 **65535** |
| 校验和 | 16 | 头+数据+**伪首部** |

### 封装

```text
应用载荷 → UDP 头(8B) → IP 载荷；IP 协议字段 = 17 (UDP)
```

### 最佳实践

万兆/数据中心：无 TCP 式拥塞反馈 → 应用须自实现**速率/窗口控制**，否则缓冲区溢出**灾难性丢包**。

→ 分用对比 TCP：[§3.2](../../03_transport_layer/study.md#ch3-2) · [§3.3 vs TCP](../../03_transport_layer/study.md#ch3-3-vs-tcp)

---

<a id="ch10-3"></a>

## 10.3–10.6 校验和与跨版本特性

### 端到端论点

**伪首部**含源/目的 IP、协议号、UDP 长度 — 跨层但用于检测**错递**（IP 路由错误等），符合 [ch01 端到端](../01_architecture/ch01_introduction.md#ch01-e2e)。

![伪首部与封装](../../03_transport_layer/assets/udp_header_pseudo.png)

### IPv4 vs IPv6

| | IPv4 | IPv6 |
|--|------|------|
| UDP 校验和 | **可选**（全 0 = 未计算） | **强制**；为 0 则**非法丢弃** |
| 原因 | IPv4 有 IP 首部校验和 | v6 **无 IP 首部校验和**，UDP 为最后屏障 |

### UDP-Lite (RFC 3828)

**部分校验**：仅保护头与关键元数据；载荷位损坏可保留 — **VoIP/多媒体** 中「坏一点」优于整包丢。

---

<a id="ch10-7"></a>

## 10.7–10.10 IP 分片与路径 MTU

### 分片字段（IPv4）

| 字段 | 作用 |
|------|------|
| **Identification** | 同原报文各片相同 |
| **Flags** | **DF**=禁止分片；**MF**=后续还有片 |
| **Fragment Offset** | 以 **8 字节**为单位 |

超链路 **MTU**（以太网常 **1500**）→ IP 分片。**IPv6 路由器不分片** → 源端须 PMTUD 或缩小包 → [ch05](ch05_ip.md#ch05-3)、[ch08 Type 2](ch08_icmpv4_icmpv6.md#ch08-3)

### 连锁失效

**分片无独立重传**：丢 **1** 片 → 接收方丢弃**整组**重组 → 应用层感知为**整包丢失**，丢包率被放大。

### 10.9 陷阱：分片与 ARP/ND

大 UDP 触发多片时，常**仅首片**触发 **ARP**（v4）或 **ND**（v6）。解析 MAC 期间**后续片**先到 → 发送/重组缓冲有限 → **静默丢片** → 重组永久失败。

→ [ch04 ARP](../03_network_layer/ch04_arp.md) · [ch08 ND](ch08_icmpv4_icmpv6.md#ch08-5)

### 案例：约 4000 字节应用数据，MTU 1500

```text
总 IP 报文：20(IP) + 8(UDP) + 3992(Data) = 4020 B
每片 IP 载荷上限：1500 - 20 = 1480 B

片1：1480 B 数据，MF=1，Offset=0
片2：1480 B 数据，MF=1，Offset=1480/8=185
片3：1032 B 数据（含 UDP 头剩余+载荷），MF=0，Offset=2960/8=370
```

（首片通常携带完整 UDP 首部；具体划分以实现为准，**Offset 必为 8 的倍数**。）

### 工程原则

- **避免 IP 分片**：单 UDP ≤ **路径 MTU − IP头 − UDP头**（常 **≤1472** 或保守 **1400**）  
- 启用 **PMTUD**（DF=1）探测路径 MTU  
- 勿假设防火墙转发所有分片

---

<a id="ch10-11"></a>

## 10.11–10.13 服务器设计与限制

### 多宿主绑定

绑定 **`INADDR_ANY`** 时，回复源 IP 可能≠客户端请求的**目的 IP**（弱主机 + 路由选择）→ 客户端防火墙/策略拒收。

**实践**：按接口绑定，或明确源地址选择策略。

### 缓冲区与截断

| 套接字选项 | 影响 |
|------------|------|
| **SO_SNDBUF** | 发送缓冲上限 |
| **SO_RCVBUF** | 接收缓冲上限 |

接收缓冲 **小于** 到达数据报：BSD 等可 **MSG_TRUNC** 并丢弃超出；Windows 行为可能不同 → 应用层用**长度前缀**等避免非确定性。

### 组播/广播套接字

与 [ch09](ch09_broadcast_multicast.md) 联动：`SO_REUSEADDR`、TTL、出口接口。

---

<a id="ch10-14"></a>

## 10.14 安全性

### 反射/放大 DDoS

伪造**受害者源 IP** → 向 DNS/NTP/SSDP 等发**小 UDP 请求** → 服务器向受害者回**大响应** → 放大。

### 分片重组攻击

大量**缺最后一片**或**重叠偏移**的片 → 占满主机**重组缓冲**（Teardrop 类变体）→ 内存耗尽。

**缓解**：入口过滤（BCP38）、限制重组资源、禁用异常分片、应用层不依赖超大 UDP。

→ [ch05 IP 欺骗](../03_network_layer/ch05_ip.md#ch05-7)

---

<a id="ch10-exam"></a>

## 10.15 总结与考点

UDP 的「极简之美」= 忠实传递 IP 语义 + **低延迟**；代价是应用承担**可靠性与拥塞**。

### 易混速记

| 问题 | 要点 |
|------|------|
| UDP vs TCP 边界 | UDP **保留报文边界**；TCP **字节流** |
| v4 vs v6 校验和 | v4 可省略；v6 **必须** |
| TCP 分段 vs IP 分片 | TCP 按 **MSS**；UDP 大包走 **IP 分片**（危险） |
| DF + 过大 | **ICMP 需要分片/PTB** → PMTUD |
| 分片丢一片 | **整报文废** |
| 端口 0 | 源端口可为 0；目的端口不可 |

### 推荐包长（实践）

| 场景 | 建议 |
|------|------|
| 互联网 UDP | **≤1200–1400 B** 载荷（留 IP/UDP 头与隧道余量） |
| 数据中心 | 仍测路径 MTU；RDMA/QUIC 自有帧边界 |

### 下一章

- [ch12 TCP 基础](ch12_tcp_intro.md) — 有状态传输  
- [ch11 DNS](../05_application_security/ch11_dns.md) — UDP/53  
- [ch09 组播](ch09_broadcast_multicast.md)

---

## Top-Down

- [study.md §3.3](../../03_transport_layer/study.md#ch3-3) · [#ch3-3-exam](../../03_transport_layer/study.md#ch3-3-exam)

## Lab

- Wireshark：`udp` · `udp.port == 53`；观察分片 `ip.frag_offset`  
- `ping -f -l 1500`（Windows）/ `ping -M do -s 1472` 测 PMTUD  
- `sysctl` / `netstat` 看重组超时

## Go / Rust

- **Go**：`net.ListenUDP`；`ipv4.PacketConn` 设 **DF**；`ReadFromUDP` 注意缓冲 ≥ 最大报文  
- **Rust**：`tokio::net::UdpSocket`；QUIC 在 UDP 之上自建可靠层  
- **QUIC/游戏**：单 datagram ≤ **path MTU**；勿依赖 IP 分片
