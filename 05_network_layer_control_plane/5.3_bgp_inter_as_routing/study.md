# 5.3 BGP 自治系统间路由

> 章级精读：[§5.4 BGP](../study.md#ch5-4) · AS 内：[5.2 OSPF](../5.2_ospf_intra_as_routing/study.md) · [AS≠IGP 通俗](../5.1_routing_algorithm/study.md#ch5-1-as-vs-igp) · [协议速记卡](../5.1_routing_algorithm/study.md#ch5-1-protocol-card)

## 本节核心目标

掌握 **BGP（EGP）** 定位、与 **OSPF（IGP）** 差异、**TCP 179**、**AS-Path 防环**、**eBGP/iBGP** 及**策略选路**；能默写对比表与考点。

---

<a id="ch5-3-bgp-basics"></a>

## 一、BGP 基础定位（必背）

**BGP**（Border Gateway Protocol，**边界网关协议**）

| 项 | 说明 |
|----|------|
| **协议类型** | **EGP 外部网关协议** — 作用于**不同 AS（自治系统）**之间 |
| **地位** | **互联网骨干核心协议**；全球跨运营商路由互通的「黏合剂」 |
| **选路本质** | **策略驱动**（非单纯最短路径/最短跳） |

一句话：**AS 之间怎么通、走谁家线路，由 BGP 按策略说了算。**

---

<a id="ch5-3-bgp-vs-ospf"></a>

## 二、BGP 与 OSPF 核心区别（必考表）

| 对比维度 | **OSPF（IGP）** | **BGP（EGP）** |
|----------|-----------------|----------------|
| **适用范围** | **同一 AS 内部** | **不同 AS 之间** |
| **核心算法/思路** | **链路状态**、最短路径（SPF） | **策略驱动**选路 |
| **设计目标** | 转发性能、时延最优 | **路由可控**、安全合规、**商业策略优先** |
| **封装** | **IP 协议号 89**（无 TCP/UDP） | **TCP 179** |

→ OSPF 精读：[5.2](../5.2_ospf_intra_as_routing/study.md#ch5-2-ospf-exam)

---

<a id="ch5-3-bgp-features"></a>

## 三、BGP 核心特性

| # | 特性 |
|---|------|
| 1 | 依托 **TCP 179** 建立邻居，**可靠**传输 UPDATE 等报文 |
| 2 | 路由携带 **AS-Path**（途经 AS 号列表）→ **天然防 AS 级环路** |
| 3 | 丰富**路径属性**：AS-Path、**Next_Hop**、**Local_Pref**、MED 等 |
| 4 | **策略能力强**：路由过滤、策略路由、优先级修改（import/export policy） |

### 封装对比（考试常考）

| 协议 | 类型 | 承载 |
|------|------|------|
| OSPF | IGP | **IP 89** |
| RIP | IGP | UDP 520 |
| **BGP** | EGP | **TCP 179** |

---

<a id="ch5-3-bgp-neighbor"></a>

## 四、BGP 两大邻居类型

| 类型 | 定义 | 典型场景 |
|------|------|----------|
| **eBGP** | **不同 AS** 之间建立的 BGP 邻居 | ISP 对等、跨运营商边界、AS 边界路由器 |
| **iBGP** | **同一 AS 内部** 建立的 BGP 邻居 | 将 eBGP 学到的前缀在 AS 内传播到所有边缘/核心 |

**iBGP 规则要点（了解）**

- 从 eBGP 学到的前缀可在 AS 内通过 **iBGP** 传递  
- iBGP 邻居间通告的路由，**下一跳常不自动改**（需 IGP 可达或策略调整）  
- 大规模 AS 常用 **路由反射器 RR**、**联盟** 避免 iBGP 全互联

---

<a id="ch5-3-bgp-policy"></a>

## 五、BGP 选路原则

**不单纯**以距离、带宽判定「最优」路径。

优先按：

- **商业策略**（客户 / 对等 / 提供商关系）  
- **路由优先级**（如 **Local_Pref** 越大越优先出 AS）  
- **运营商线路质量**、前缀过滤、AS-Path 长度等  

**常见决策维度（记名即可）**：Local_Pref → AS-Path 长度 → MED → eBGP 优于 iBGP → Router ID 等（具体顺序依厂商/配置）。

**热土豆（Hot Potato）**：尽快把流量交给**邻居 AS**，减少本 AS 承载。

---

<a id="ch5-3-bgp-exam"></a>

## 六、必考核心考点 · 考试背诵

### 四句口诀

```text
BGP边界跨AS间，TCP179策略选
AS-Path防环路，eBGP外iBGP内
IGP内网OSPF，EGP外网BGP扛
商业策略优先于，最短路径和带宽
```

### 30 字

**BGP：EGP、跨 AS、TCP179；AS-Path 防环；eBGP 对外 iBGP 对内；策略选路非纯最短。**

### 考点速记

| 点 | 一句 |
|----|------|
| 定位 | **EGP**，**不同 AS** 间，互联网骨干 |
| vs OSPF | OSPF=**IGP/AS 内/LS**；BGP=**EGP/AS 间/策略** |
| 防环 | **AS-Path** 记录途经 AS，见己 AS 则拒 |
| 邻居 | **eBGP** 跨 AS；**iBGP** 同 AS 内 |
| 封装 | **TCP 179**（OSPF 是 **IP 89**） |
| 选路 | **策略/商业** 优先，非纯最短 |

### 易错点

| 易混 | 纠正 |
|------|------|
| BGP 追求最短路径？ | **否**；**策略与商业关系**优先 |
| BGP 用 UDP？ | **否**；**TCP 179** |
| AS-Path 防什么环？ | **AS 级**环路；域内环路由靠 IGP |
| iBGP = 不同 AS？ | **否**；**同 AS 内**；跨 AS 是 **eBGP** |
| 目录 5.3 vs 章 §5.4 | 目录 **5.3=BGP 精读**；章 **§5.4=BGP** 概述 |

---

## 七、学习补充

> 理清全网 **AS 层级**转发：本 AS **IGP（OSPF）** 找下一跳，跨 AS 靠 **BGP** 选出口；抓包过滤 **tcp.port==179**。

| 锚点 | 内容 |
|------|------|
| [#ch5-3-bgp-basics](#ch5-3-bgp-basics) | 定位 |
| [#ch5-3-bgp-vs-ospf](#ch5-3-bgp-vs-ospf) | vs OSPF |
| [#ch5-3-bgp-features](#ch5-3-bgp-features) | TCP179 / AS-Path |
| [#ch5-3-bgp-neighbor](#ch5-3-bgp-neighbor) | eBGP / iBGP |
| [#ch5-3-bgp-policy](#ch5-3-bgp-policy) | 策略选路 |
| [#ch5-3-bgp-exam](#ch5-3-bgp-exam) | 口诀 / 30 字 |
