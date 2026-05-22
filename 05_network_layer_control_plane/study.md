# 第5章 网络层：控制平面

控制平面是网络的「**大脑**」：负责**路由选择、策略与编排**，生成或下发转发表，驱动第 4 章 [数据平面](../04_network_layer_data_plane/study.md) 的转发行为。历史上经历了从**每路由器控制（Per-router control）**到**逻辑集中控制（SDN）**的范式演进。

---

<a id="ch5-control-plane-basics"></a>

## 控制平面是什么（与数据平面对照）

> 数据平面只做「按表转发」→ [第 4 章](../04_network_layer_data_plane/study.md#ch4-fib)

### 1. 核心作用

负责**决策与管理**，**不转发用户业务数据**；为数据平面提供转发依据（路由表 RIB → 转发表 FIB）。

### 2. 主要工作

| 工作 | 说明 |
|------|------|
| 运行路由协议 | 探测网络拓扑（OSPF、BGP 等） |
| 算路与建表 | 计算最优/可行路径，生成 **RIB**，下发 **FIB** |
| 维护邻居与状态 | 与相邻路由器/控制器同步链路、可达性 |
| 下发转发规则 | 管控接口、策略、ACL、链路 up/down |
| 处理协议报文 | 设备间交互、协商（Hello、LSA、BGP UPDATE…） |

### 3. 运行主体与速度

- **运行主体**：设备 **CPU + 软件**（路由协议进程、SDN 代理等）
- **速度**：远**慢于**数据平面（ASIC/TCAM 线速转发）

### 4. 运行时机

网络**初始化**、链路 **up/down**、拓扑变化、策略变更时**持续或触发**更新；平时也在后台维护邻居与定时刷新。

### 5. 一句话本质

**指挥中枢**：控制平面**定路线、下规则**；数据平面**无脑高速转发**。

```text
控制平面（慢、算路）  ──下发 FIB──►  数据平面（快、转发用户包）
```

### 易混

| | 控制平面 | 数据平面 |
|--|----------|----------|
| 干什么 | 算路、协商、管理 | 查 FIB、换 MAC、转发 |
| 跑在哪 | CPU 软件 | 输入/交换/输出硬件 |
| 碰用户业务包？ | **一般不转发**（只处理路由/管理报文） | **是** |
| 查什么表 | **RIB**（路由表） | **FIB**（转发表） |

---

<a id="ch5-1"></a>

## 5.1 概述（Introduction）

### 范式转移

传统**垂直集成**设备将控制逻辑固化在每台路由器中，协议创新受厂商软件周期约束，且易与各类**中间盒**交织。 **SDN** 将控制与转发分离，以 **Match + Action** 等抽象统一表达策略，使管理员能在逻辑中心做**流量工程（TE）**、负载均衡等——在纯分布式、仅以目的地为驱动的模型里，缺乏全局视图时往往**难以达到全局最优**。

### 传统路由 vs SDN 控制平面（对比）

| 维度 | 传统每路由器控制 | SDN 控制平面 |
|------|------------------|--------------|
| 控制逻辑位置 | 分布式，驻留在各交换机/路由器 | 逻辑集中，控制器在网元之外 |
| 转发决策基础 | 常见为基于目的前缀的最长匹配 | 泛化匹配 + 多种动作 |
| 创新与灵活性 | 依赖设备商版本节奏 | 北向 API、自动化与可编程 |
| 战略侧重 | 设备自治、本地优化 | 全局视图下的调度与编排 |

### 路由的本质

路由选择算法在抽象拓扑与**链路权值（Cost）**上求**低开销路径**；Cost 可对应跳数、带宽倒数、时延、运营策略等。控制平面的决策质量，最终依赖这些算法与策略的数学与工程约束。

---

<a id="ch5-2"></a>

## 5.2 路由选择算法（Routing Algorithms）

目标：基于拓扑与权值，构造从源到目的的可达路径（常为「最短」意义下的路径树/下一跳）。

### 5.2.1 链路状态（LS）

- **思想**：节点通过 **LSA** 等机制获知（近似）**全局拓扑**，用 **Dijkstra** 等算法计算最短路径。  
- **复杂度**：与实现有关，常见教学表述为 **O(N²)** 或使用优先队列的 **O(E log N)** 量级。  
- **工程风险（震荡）**：若链路权值与**瞬时负载**强耦合，流量迁移可能反复改变权值，引发**震荡**。实践中权值常相对平滑，或与负载解耦。

### 5.2.2 距离向量（DV）

- **Bellman-Ford 方程（形式）**：  
  `d_x(y) = min_v { c(x,v) + d_v(y) }`  
  其中 `d_x(y)` 为从 **x** 到 **y** 的最小开销，**v** 取 **x** 的邻居。

- **坏消息传得慢**：**计数到无穷（Count-to-infinity）** 等问题；**毒性逆转（Poisoned Reverse）** 可缓解部分简单环路，对更复杂拓扑仍有限。

### LS vs DV（教学对比）

| 维度 | LS | DV |
|------|----|----|
| 收敛 | 通常较快；单源 Dijkstra 计算量明确 | 可能较慢；收敛前可能出现临时环路 |
| 报文/状态 | LSA 泛洪，全网状态量大 | 仅与邻居交换向量，局部通信 |
| 健壮性 | 错误 LSA 影响范围可分析 | 错误向量可能沿邻居关系扩散 |

**连贯性**：AS **内部**常落地为 **OSPF**（LS 思路的工业实现）。

> **背诵提纲** → [5.1 路由算法精读](./5.1_routing_algorithm/study.md)（[AS≠IGP 通俗](./5.1_routing_algorithm/study.md#ch5-1-as-vs-igp) · [同AS实景](./5.1_routing_algorithm/study.md#ch5-1-same-as-scenario) · [IGP/EGP/AS](./5.1_routing_algorithm/study.md#ch5-1-igp-egp) · [协议速记卡](./5.1_routing_algorithm/study.md#ch5-1-protocol-card) · [Dijkstra 手算](./5.1_routing_algorithm/study.md#ch5-1-dijkstra) · [LS/DV](./5.1_routing_algorithm/study.md#ch5-1-compare) · [30 字](./5.1_routing_algorithm/study.md#ch5-1-exam)）

---

<a id="ch5-3"></a>

## 5.3 因特网中自治系统内部的路由选择：OSPF

因特网划分为多个**自治系统（AS）**。**OSPF（Open Shortest Path First）** 是典型的 **IGP**，在 AS 内基于链路状态计算最短路径。

- **封装**：报文直接封装在 **IP** 中，**协议号 89**（与 **RIP** 走 UDP、**BGP** 走 **TCP 179** 等区分）。  
- **能力（依实现/配置）**：鉴别、多路径、按链路度量做 TE 等。  
- **区域（Area）**：为抑制 LSA 泛洪规模，划分**区域**；**Area 0** 为骨干，负责区域间连通性摘要。  
- **角色**：**ABR**（区域边界）、**ASBR**（与其他 AS 或外部路由相连）等。

**工程意义**：区域将内部拓扑细节对外隐藏，降低内存与 SPF 计算压力。

> **背诵提纲** → [5.2 OSPF 精读](./5.2_ospf_intra_as_routing/study.md)（[三大概念通俗](./5.2_ospf_intra_as_routing/study.md#ch5-2-ospf-simple) · [Area 0](./5.2_ospf_intra_as_routing/study.md#ch5-2-ospf-area) · [邻居五步](./5.2_ospf_intra_as_routing/study.md#ch5-2-ospf-neighbor) · [vs RIP](./5.2_ospf_intra_as_routing/study.md#ch5-2-ospf-vs-rip) · [30 字](./5.2_ospf_intra_as_routing/study.md#ch5-2-ospf-exam)）

---

<a id="ch5-4"></a>

## 5.4 ISP 之间的路由选择：BGP

**BGP** 是域间路由的事实标准，常被称为因特网的**黏合剂**。与 IGP 追求「最短」不同，BGP 强烈受**策略**（商业关系、前缀过滤、对等协定）约束，路径往往是**可接受的商业路径**而非纯最小度量。

- **eBGP / iBGP**：**eBGP** 在 AS 边界交换可达前缀；**iBGP** 将外部可达性在 AS 内传播（常需路由反射器/联盟等防全互联）。  
- **关键路径属性（示例）**：  
  - **AS-PATH**：记录经过的 AS 序列，**防 AS 级环路**的核心之一。  
  - **NEXT-HOP**：到达前缀的下一跳（常需配合 IGP 解析可达性）。  
- **典型决策维度（教材/实现排序略有差异）**：如 **LOCAL_PREF**、**AS-PATH 长度**、**MED**、eBGP 优于 iBGP、Router ID 等；**热土豆（Hot Potato）** 体现尽快将流量交给邻居 AS、减少本 AS 承载的意图。  
- **Anycast**：不同站点通告**相同前缀**，由 BGP 将用户导向拓扑上较近或较优的入口（DNS 根、CDN 等常见）。

> **背诵提纲** → [5.3 BGP 精读](./5.3_bgp_inter_as_routing/study.md)（[快递公司版](./5.3_bgp_inter_as_routing/study.md#ch5-3-bgp-courier) · [选路规则](./5.3_bgp_inter_as_routing/study.md#ch5-3-bgp-selection) · [路径向量](./5.3_bgp_inter_as_routing/study.md#ch5-3-path-vector) · [eBGP/iBGP](./5.3_bgp_inter_as_routing/study.md#ch5-3-bgp-neighbor) · [30 字](./5.3_bgp_inter_as_routing/study.md#ch5-3-bgp-exam)）

---

<a id="ch5-5"></a>

## 5.5 SDN 控制平面

SDN 将分布式控制逻辑**上收**到可编程的软件栈，与第 4 章**流表**衔接：控制器计算并下发**流表项**。

### 三层模型（概念）

1. **南向（通信层）**：控制器 ↔ 数据平面，如 **OpenFlow** 等。  
2. **网络状态/拓扑层**：维护拓扑、链路、统计与流表状态。  
3. **北向（策略/应用层）**：对上层应用暴露 API（REST、gRPC 等），承载负载均衡、ACL、TE 等 App。

### OpenFlow 交互（经典）

- **Packet-in**：未命中流表或需上送时，交换机将分组（或首部）送控制器。  
- **Flow-mod**：控制器**增删改**流表项。  
- **Packet-out / 读状态**：主动发包或查询计数器/端口状态。

**So What?** 控制器直接驱动第 4 章讨论的**泛化转发/流表**，实现细粒度、可演进的流量控制。

> **背诵提纲** → [5.4 SDN 控制器精读](./5.4_sdn_controller_plane/study.md)（[南北向](./5.4_sdn_controller_plane/study.md#ch5-4-interfaces) · [vs 传统](./5.4_sdn_controller_plane/study.md#ch5-4-vs-traditional) · [挑战](./5.4_sdn_controller_plane/study.md#ch5-4-challenges) · [30 字](./5.4_sdn_controller_plane/study.md#ch5-4-exam)）

---

<a id="ch5-6"></a>

## 5.6 ICMP：因特网控制报文协议

**ICMP** 用于诊断与控制消息，封装在 IP 数据报中（**不是**上层用户数据的传输通道）。

- **常见类型（示例）**：目的不可达（**Type 3**）、**超时（Type 11，TTL 耗尽）**、Echo 请求/应答（**Ping，Type 8/0**）等。**源抑制（Source Quench，Type 4）** 在历史上曾用于拥塞提示，**现代网络已基本弃用**（以端到端拥塞控制为主）。  
- **Traceroute（典型 UDP 实现思路）**：源发送 TTL=1,2,3… 的探测包；中间路由器返回 **ICMP Time Exceeded**；到达目标后常因**未监听高端口**等得到 **ICMP Port Unreachable**，据此推断路径。  
  - 实际实现还有 **ICMP trace、TCP trace** 等变体。  
- **工程现实**：企业防火墙常**过滤 ICMP**，导致 Ping/Traceroute 出现 `*` 或超时，**不等于**业务 TCP/HTTP 一定故障。

> **背诵提纲** → [5.5 ICMP 精读](./5.5_icmp_snmp_network_manage/study.md)（[类型表](./5.5_icmp_snmp_network_manage/study.md#ch5-55-icmp) · [ping 排障](./5.5_icmp_snmp_network_manage/study.md#ch5-55-ping-troubleshoot) · [30 字](./5.5_icmp_snmp_network_manage/study.md#ch5-55-exam)）

---

<a id="ch5-7"></a>

## 5.7 网络管理、SNMP 与 NETCONF/YANG

网络管理从「救火」走向**可观测 + 自动化编排**。

### SNMP

- **组成**：管理站、被管设备上的 **Agent**、**MIB**（管理信息库）。  
- **常用操作**：**Get**、**GetNext**、**GetBulk**、**Set**；异步 **Trap**；**Inform**（带确认的通告，语义因部署而异）。  
- **安全**：避免 **SNMPv1/v2c** 明文共同体串；生产应优先 **SNMPv3**（认证与加密）。

> **SNMP 流程与版本** → [5.5 精读 §二](./5.5_icmp_snmp_network_manage/study.md#ch5-55-snmp-flow) · [NETCONF/Telemetry](./5.5_icmp_snmp_network_manage/study.md#ch5-55-other-mgmt)

### NETCONF 与 YANG

- **YANG**：数据建模语言，描述配置/状态的结构与约束。  
- **NETCONF**：基于 RPC 的配置与操作接口，常见承载为 **SSH**；支持候选配置、提交与回滚等能力（依实现）。  
- **So What?**：相对 SNMP 以轮询为主的「拉」，**流式遥测（Streaming Telemetry）** 等提供高频「推」，更适配大规模云网运维。

---

<a id="ch5-8"></a>

## 总结

控制平面是**图论算法、分布式系统与商业策略**的交汇：从 **OSPF** 的严谨域内计算，到 **BGP** 的策略域间选路，再到 **SDN** 的可编程集中控制，以及 **ICMP/SNMP/NETCONF** 的运维闭环。其长期目标不变：**在可扩展、可运维、可演进的前提下，为数据平面提供正确且可控的转发语义。**

---

*本笔记整理自精读材料，可与教材第 5 章对照阅读。*
