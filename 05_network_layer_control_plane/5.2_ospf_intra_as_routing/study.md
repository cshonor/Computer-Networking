# 5.2 OSPF 自治系统内部路由

> 章级精读：[§5.3 OSPF](../study.md#ch5-3) · 算法基础：[5.1 LS/Dijkstra](../5.1_routing_algorithm/study.md#ch5-1-ls) · 对比 RIP：[DV](../5.1_routing_algorithm/study.md#ch5-1-dv) · 域间：[5.3 BGP](../5.3_bgp_inter_as_routing/study.md)

## 本节核心目标

掌握 **OSPF 定位（IGP/LS）**、**IP 89**、**Area 0**、**LSA 泛洪**、邻居建立五步与 **Full** 邻接；能区分 **OSPF vs RIP**。

---

<a id="ch5-2-ospf-basics"></a>

## 一、基础定位（必背）

**OSPF**（Open Shortest Path First，**开放式最短路径优先**）

| 项 | 说明 |
|----|------|
| **协议类型** | **IGP 内部网关协议** — 仅用于**同一 AS（自治系统）**内 |
| **底层算法** | **链路状态 LS**（非距离矢量） |
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
| OSPF = 距离矢量？ | **否**；**链路状态**，本地 **Dijkstra** |
| 非骨干 Area 能直连？ | **否**；必须经 **Area 0** |
| OSPF 靠邻居传路由表？ | **否**；靠 **LSA 泛洪拓扑**，本地算路 |
| 目录 5.2 vs 章 §5.3 | 目录 **5.2=OSPF 精读**；章 **§5.3=OSPF** 概述 |

---

## 七、学习补充

> 实操 **多区域 OSPF**；Wireshark 抓 **Hello、DBD、LSR、LSU、LSAck**（过滤 `ospf` 或 IP proto 89）。

| 锚点 | 内容 |
|------|------|
| [#ch5-2-ospf-basics](#ch5-2-ospf-basics) | 定位 |
| [#ch5-2-ospf-features](#ch5-2-ospf-features) | 特点 / IP89 |
| [#ch5-2-ospf-area](#ch5-2-ospf-area) | Area 0 |
| [#ch5-2-ospf-neighbor](#ch5-2-ospf-neighbor) | 邻居五步 |
| [#ch5-2-ospf-vs-rip](#ch5-2-ospf-vs-rip) | vs RIP |
| [#ch5-2-ospf-exam](#ch5-2-ospf-exam) | 口诀 / 30 字 |
