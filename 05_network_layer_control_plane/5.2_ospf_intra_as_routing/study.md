# 5.2 OSPF 自治系统内部路由

> 章级精读：[§5.3 OSPF](../study.md#ch5-3) · **LSA+Dijkstra**：[#ch5-2-lsa-dijkstra](#ch5-2-lsa-dijkstra) · **三大概念**：[#ch5-2-ospf-simple](#ch5-2-ospf-simple) · [组播≠CIDR](#ch5-2-multicast-vs-cidr) · 域间：[5.3 BGP](../5.3_bgp_inter_as_routing/study.md)

## 本节核心目标

掌握 **OSPF = 发 LSA + 本地 Dijkstra**；以及 **IP 89**、**Area 0**、邻居五步与 **Full** 邻接；能区分 **OSPF vs RIP**。**新手先读** [#ch5-2-lsa-dijkstra](#ch5-2-lsa-dijkstra) · [#ch5-2-ospf-simple](#ch5-2-ospf-simple)。

---

<a id="ch5-2-ospf-simple"></a>

## 〇、新手易懂：三大核心概念

> **89 识别 OSPF 包；Area 0 是主干道；LSA 泛洪同步同区域地图。**

---

<a id="ch5-2-ospf-ip89"></a>

### 1）IP 协议号 89

**通俗**：IP 首部有个**协议号**，告诉接收方「包里装的是哪种协议」。

| 编号 | 协议 |
|------|------|
| **6** | TCP |
| **17** | UDP |
| **1** | ICMP |
| **89** | **OSPF** |

- 组播收发（**广播网/以太网**上 Hello、LSAck 等仍用组播，**至今标配**）：
  - **224.0.0.5**（AllSPFRouters）— 所有 OSPF 路由器  
  - **224.0.0.6** — 只发给 **DR、BDR**

→ 考试精编：[#ch5-2-ospf-features](#ch5-2-ospf-features) · **224.0.0.5 与 CIDR 易混** → [#ch5-2-multicast-vs-cidr](#ch5-2-multicast-vs-cidr)

---

<a id="ch5-2-multicast-vs-cidr"></a>

#### 易混澄清：224.0.0.5 还在，没被 CIDR 取代

> **224.0.0.5 一直都在；CIDR 和组播是两回事，不是「有了 CIDR 就不用组播」。**

| | **224.0.0.5** | **CIDR** |
|---|---------------|----------|
| 是什么 | **D 类组播地址**（OSPF 专用） | **单播地址的 /前缀 记法** |
| 管什么 | **功能**：OSPF Hello/LSAck 发给所有路由器 | **记法**：如 `192.168.1.0/24` |
| 关系 | 可写成 `224.0.0.5/32`，**只是写法**，本质仍是**组播** | 只管**普通上网单播 IP**，**不管组播段** |

**224.0.0.0/4** 整段是**组播（D 类）**，与 CIDR 划分单播网段**各管各的、同时共存**。

**极简关系图**

```text
┌─────────────────┐   ┌──────────────────────┐   ┌─────────────────┐
│ 单播 + CIDR记法  │   │ 组播 224.0.0.5       │   │ OSPF 协议号 89  │
│ 192.168.1.0/24  │   │ D类 · OSPF Hello     │   │ IP首部字段=89   │
│ → 普通上网寻址   │   │ → 所有OSPF路由器听  │   │ → 识别OSPF报文  │
└─────────────────┘   └──────────────────────┘   └─────────────────┘
     记法/范围              组播功能                    封装识别
              三者不冲突，现代网络同时用
```

→ D 类组播背景：[4.3 有类编址 §D类](../../04_network_layer_data_plane/4.3_ipv4_ipv6_nat/study.md#ch4-3-classful) · CIDR：[4.3 CIDR 逻辑链](../../04_network_layer_data_plane/4.3_ipv4_ipv6_nat/study.md#ch4-3-cidr-chain)

---

<a id="ch5-2-ospf-area0-simple"></a>

### 2）Area 0 骨干区域

**通俗**：超大网络划成一块块 **Area**，**Area 0 = 城市主干道 / 中心骨干**。

| 规则 | 说明 |
|------|------|
| **必须直连** | 所有普通区域**必须连着 Area 0** |
| **中转互通** | 不同区域之间**只能经 Area 0** 转发 |
| **作用** | 防环路、缩小故障范围、减轻设备压力 |

```text
Area1 ──┐
Area2 ──┼── Area 0（骨干）── 区域间只走这里
Area3 ──┘
（非骨干之间不能直接「串门」）
```

→ 考试精编：[#ch5-2-ospf-area](#ch5-2-ospf-area)

---

<a id="ch5-2-ospf-lsa-flood"></a>

### 3）LSA 泛洪

**通俗**：**LSA = 链路状态信息**（周边线路、网段、快慢开销）；**泛洪 = 把网络地图同步给同区域所有路由器**。

| 步骤 | 动作 |
|------|------|
| 1 | 某路由器发现**线路变化** → 生成 LSA |
| 2 | 发给**邻居** |
| 3 | 邻居继续**转发**给其他邻居 |
| 4 | 最终**同区域所有路由器**拿到**相同拓扑地图（LSDB）** |

**关键特点**

| 特点 | 说明 |
|------|------|
| **范围** | **只在本 Area 内**传播，不跨区大范围扩散 |
| **触发** | **有变化才更新**，无变化不频繁发 |
| **算路** | 大家地图一样 → **各自独立**跑 **Dijkstra** 算最短路 |

→ 算法：[5.1 Dijkstra/LS](../5.1_routing_algorithm/study.md#ch5-1-ls) · **LSA≠路由**：[#ch5-2-lsa-dijkstra](#ch5-2-lsa-dijkstra) · 邻接五步：[#ch5-2-ospf-neighbor](#ch5-2-ospf-neighbor)

---

### 三者关联 + 组播（一句背）

**协议号 89 识别 OSPF 包 → Area 0 规整大网 → LSA 泛洪同步地图；以太网上 Hello 用组播 224.0.0.5（与 CIDR 单播记法并存）。**

| 点 | 记住 |
|----|------|
| **89** | IP 首部协议号，标识 OSPF |
| **Area 0** | 骨干，非骨干必须连它 |
| **LSA 泛洪** | 同区域同步 LSDB，各自 SPF |
| **224.0.0.5** | OSPF 组播地址，**没被淘汰** |

---

<a id="ch5-2-lsa-dijkstra"></a>

## 〇·二、一句话捋清：OSPF = **发 LSA** + **本地 Dijkstra**

> **邻居之间不传路由，只传 LSA；每台路由器拿齐 LSA 后，本地用 Dijkstra 算最短路径。**

### 1）先分清两个东西

| | **LSA** | **Dijkstra** |
|---|---------|--------------|
| 是什么 | OSPF 路由器**互相发的报文** | **本机内部**跑的算路算法 |
| 内容 | 我有哪些接口、连谁、带宽/开销 | **不写**在报文里 |
| 作用 | 描述**链路状态** | 用全部 LSA 拼拓扑 → **算最短路** |

**LSA 里只有「地图碎片」，没有「最终路由表」。**

---

### 2）完整流程（5 步）

1. 每台路由器**只把直连链路**打包成 **LSA**
2. **泛洪** LSA 给同区域所有 OSPF 邻居（经 LSU 等）
3. 大家收到全部 LSA → 拼成**一模一样的 LSDB（全网拓扑地图）**
4. **每台路由器单独跑 Dijkstra**，以自己为根，算到各网段最短路
5. 结果写入**本地路由表**（再下发 FIB）

---

### 3）为啥不传路由、只传 LSA？

| 传路由（DV 思路） | 传 LSA（OSPF/LS） |
|-------------------|-------------------|
| 易环路、信息失真 | 全网拓扑**一致** |
| 震荡大 | **各自独立算路**，稳定 |

---

### 4）通俗比喻

| 步骤 | 比喻 |
|------|------|
| LSA | 每人画**自家门口**道路图 |
| 泛洪 | **交换地图碎片** |
| LSDB | 集齐碎片 → **全城完整地图** |
| Dijkstra | 站在自家门口，算去全城**怎么走最近** |

---

### 5）名词对应

| 名词 | 记住 |
|------|------|
| 交换的数据 | **LSA** |
| 存所有 LSA 的库 | **LSDB** |
| 本机算路算法 | **Dijkstra（SPF）** |

**小总结**：邻居**只交换 LSA**，不交换算法、不交换路由；**Dijkstra 只在本机跑**，靠统一 LSDB 出路由表。

---

### 6）极简示意图

```text
  R1 ──LSA──► R2 ──LSA──► R3        （泛洪：只传链路状态，不传路由表）
   │           │           │
   └─ LSDB ────┴─ LSDB ────┴─ LSDB   （同 Area 内：三张表内容一致）

  R1 本地: LSDB + Dijkstra(根=R1) → R1 的路由表
  R2 本地: LSDB + Dijkstra(根=R2) → R2 的路由表   ← 同一地图，不同起点
  R3 本地: LSDB + Dijkstra(根=R3) → R3 的路由表
```

| 易混 | 纠正 |
|------|------|
| OSPF 邻居传路由表？ | **否**；传 **LSA**，路由**各自算** |
| Dijkstra 在报文里跑？ | **否**；**本机 CPU** 跑 SPF |
| LSDB 每台不一样？ | **同 Area 内应一致**（同步拓扑） |
| 和 RIP 一样靠邻居跳数？ | **否**；RIP 是 **DV**，OSPF 是 **LS** |

→ LS 原理：[5.1 链路状态](../5.1_routing_algorithm/study.md#ch5-1-ls) · Full 后 SPF：[#ch5-2-ospf-neighbor](#ch5-2-ospf-neighbor)

---

<a id="ch5-2-ospf-basics"></a>

## 一、基础定位（必背）

**OSPF**（Open Shortest Path First，**开放式最短路径优先**）

| 项 | 说明 |
|----|------|
| **协议类型** | **IGP 内部网关协议** — 仅用于**同一 AS（自治系统）**内 |
| **底层算法** | **链路状态 LS**（非距离矢量）→ [5.1 LS 精编](../5.1_routing_algorithm/study.md#ch5-1-ls) |
| **开放性** | 标准开放，**全厂商互通** |

一句话：**AS 内用 LS 算最短路，开放标准，不靠邻居跳数传路由表。**

---

<a id="ch5-2-ospf-features"></a>

## 二、核心特点

| # | 特点 |
|---|------|
| 1 | 直接封装 **IP，协议号 89** — **不用 TCP/UDP** |
| 2 | 度量 **Cost（开销）**：**带宽越大，Cost 越小** |
| 3 | 支持 **区域（Area）** 分层组网 |
| 4 | 支持 **报文认证**、**等价路由负载分担（ECMP）** |
| 5 | 全网泛洪 **LSA（链路状态通告）**，同步 **链路状态数据库 LSDB** |

### 与常见协议封装对比（易考）

| 协议 | 类型 | 承载 |
|------|------|------|
| **OSPF** | IGP / LS | **IP 89** |
| **RIP** | IGP / DV | **UDP 520** |
| **BGP** | EGP | **TCP 179** |

---

<a id="ch5-2-ospf-area"></a>

## 三、OSPF 区域规划

| 区域 | 要求 |
|------|------|
| **Area 0 骨干区域** | **必设**；**不可拆分、不可缺失** |
| **非骨干区域** | 必须通过 **ABR** **直连 Area 0**；**非骨干之间不能直接互通** |
| **目的** | 缩小 **LSA 泛洪**范围 → 降 CPU/内存、**加快收敛** |

```text
非骨干 Area X ──ABR── Area 0（骨干）──ABR── 非骨干 Area Y
```

> 角色：**ABR**（区域边界路由器）、**ASBR**（连外部/其他 AS）— 见章级 [#ch5-3](../study.md#ch5-3)

---

<a id="ch5-2-ospf-neighbor"></a>

## 四、邻居与邻接建立（全过程 · 必考顺序）

| 步骤 | 报文/动作 | 作用 |
|------|-----------|------|
| 1 | **Hello** | 发现邻居、协商参数 → 建立**邻居关系**（2-Way） |
| 2 | **DBD**（Database Description） | 交换链路库**摘要**，比对 LSDB 版本 |
| 3 | **LSR**（Link State Request） | 请求缺失的 LSA |
| 4 | **LSU**（Link State Update） + **LSAck** | 发送完整 LSA 并**确认** |
| 5 | 数据库一致 → **Full（完全邻接）** | 本地运行 **Dijkstra（SPF）** → 生成**路由表** → 下发 **FIB** |

```text
Hello → DBD → LSR/LSU/LSAck → Full → SPF(Dijkstra) → 路由表
```

**记忆**：**你好（Hello）→ 对账（DBD）→ 要细节（LSR）→ 更新确认（LSU/LSAck）→ 满状态算路（Full+SPF）**

---

<a id="ch5-2-ospf-vs-rip"></a>

## 五、OSPF 对比 RIP 优势

| 维度 | OSPF（LS） | RIP（DV） |
|------|------------|-----------|
| 收敛 | **快** | 慢 |
| 环路/计数到无穷 | **无 DV 经典缺陷** | **易环路、坏消息慢** |
| 网络规模 | **大型、多层级** | 小规模为主 |
| 扩展 | **区域化**架构 | 扁平跳数限制（RIPv1/2 15 跳） |
| 算路依据 | **全网拓扑 + SPF** | **邻居跳数向量** |

---

<a id="ch5-2-ospf-exam"></a>

## 六、考试背诵极简版

### 口诀

```text
OSPF IGP同AS内，IP89不用TCP
LSA泛洪Area0骨干，Cost小带宽大
Hello DBD LSR LSU，Full后Dijkstra算路
链路状态非矢量，比RIP快无无穷
```

### 30 字

**OSPF：AS 内 IGP、IP89、LSA+Area0、Hello→DBD→LSU→Full→SPF；非 DV，优于 RIP 收敛与扩展。**

### 考点速记

| 点 | 一句 |
|----|------|
| 类型 | **IGP**、**LS**、**AS 内** |
| 封装 | **IP 协议号 89** |
| 度量 | **Cost**（带宽↑ Cost↓） |
| 骨干 | **Area 0 必有**，非骨干经 ABR 连骨干 |
| 邻接 | **Hello → DBD → LSR/LSU/LSAck → Full → SPF** |
| vs RIP | OSPF=**LS**；RIP=**DV** |

### 易错点

| 易混 | 纠正 |
|------|------|
| OSPF 用 UDP？ | **否**；直接 **IP 89** |
| 224.0.0.5 被 CIDR 取代？ | **否**；组播**功能** vs CIDR **单播记法**，**并存** → [#ch5-2-multicast-vs-cidr](#ch5-2-multicast-vs-cidr) |
| OSPF = 距离矢量？ | **否**；**链路状态**，本地 **Dijkstra** |
| 非骨干 Area 能直连？ | **否**；必须经 **Area 0** |
| OSPF 靠邻居传路由表？ | **否**；靠 **LSA 泛洪拓扑**，本地算路 |
| 目录 5.2 vs 章 §5.3 | 目录 **5.2=OSPF 精读**；章 **§5.3=OSPF** 概述 |

---

## 七、学习补充

> 实操 **多区域 OSPF**；Wireshark 抓 **Hello、DBD、LSR、LSU、LSAck**（过滤 `ospf` 或 IP proto 89）。

| 锚点 | 内容 |
|------|------|
| [#ch5-2-lsa-dijkstra](#ch5-2-lsa-dijkstra) | LSA + 本地 Dijkstra |
| [#ch5-2-ospf-simple](#ch5-2-ospf-simple) | 三大概念通俗 |
| [#ch5-2-ospf-ip89](#ch5-2-ospf-ip89) | IP 协议号 89 |
| [#ch5-2-multicast-vs-cidr](#ch5-2-multicast-vs-cidr) | 224.0.0.5 vs CIDR |
| [#ch5-2-ospf-area0-simple](#ch5-2-ospf-area0-simple) | Area 0 骨干 |
| [#ch5-2-ospf-lsa-flood](#ch5-2-ospf-lsa-flood) | LSA 泛洪 |
| [#ch5-2-ospf-basics](#ch5-2-ospf-basics) | 定位 |
| [#ch5-2-ospf-features](#ch5-2-ospf-features) | 特点 / IP89 |
| [#ch5-2-ospf-area](#ch5-2-ospf-area) | Area 0 |
| [#ch5-2-ospf-neighbor](#ch5-2-ospf-neighbor) | 邻居五步 |
| [#ch5-2-ospf-vs-rip](#ch5-2-ospf-vs-rip) | vs RIP |
| [#ch5-2-ospf-exam](#ch5-2-ospf-exam) | 口诀 / 30 字 |
