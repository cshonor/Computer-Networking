# 5.4 SDN 控制平面架构

> 章级精读：[§5.5 SDN](../study.md#ch5-5) · 数据平面 OpenFlow/流表：[4.4](../../04_network_layer_data_plane/4.4_sdn_openflow/study.md) · 架构图：[../../04_network_layer_data_plane/assets/sdn_controller_architecture.png](../../04_network_layer_data_plane/assets/sdn_controller_architecture.png)

## 本节核心目标

掌握 **控数分离**、**集中式控制器**、**南向 OpenFlow / 北向 REST**、与传统网络对比及**三大挑战**；能区分控制平面（本章）与数据平面（4.4）。

---

<a id="ch5-4-sdn-core"></a>

## 一、SDN 核心思想（必背）

**转发与控制彻底分离（控数分离）**

| 平面 | 职责 |
|------|------|
| **控制平面** | **集中化** — 算路、策略、下发流表 |
| **数据平面** | 交换机/路由器**仅高速转发**（按流表 Match+Action） |

一句话：**大脑在控制器，交换机只干活。**

→ 数据平面详解：[4.4 SDN/OpenFlow](../../04_network_layer_data_plane/4.4_sdn_openflow/study.md#ch4-4-sdn-core)

---

<a id="ch5-4-controller"></a>

## 二、集中式控制器（SDN 大脑）

| # | 能力 |
|---|------|
| 1 | **统一感知**全网拓扑 |
| 2 | **全局集中**计算路由与策略 |
| 3 | **统一下发**流表项，**全网统一调度**流量 |

### OpenFlow 控制闭环（与 4.4 衔接）

| 消息 | 方向 | 作用 |
|------|------|------|
| **Packet-in** | 交换机 → 控制器 | 未知流/需决策时**上送** |
| **Flow-mod** | 控制器 → 交换机 | **增删改**流表项 |
| **Packet-out** | 控制器 → 交换机 | 控制器主动注入报文 |

→ [未知流 4 步](../../04_network_layer_data_plane/4.4_sdn_openflow/study.md#ch4-4-flow)

---

<a id="ch5-4-interfaces"></a>

## 三、南北向接口（必考）

| 接口 | 连接对象 | 主流协议/API | 作用 |
|------|----------|--------------|------|
| **南向** | 控制器 ↔ **转发交换机** | **OpenFlow** | 下发**流表规则**、读端口/计数器 |
| **北向** | 控制器 ↔ **上层业务应用** | **REST API**（亦常见 gRPC） | 开放网络能力：LB、防火墙、TE 等 |

```text
应用层 App ──北向 REST──► 控制器 ──南向 OpenFlow──► 交换机（数据平面）
```

> **易混**：OpenFlow = **南向**；REST = **北向**（见 [4.4 易错](../../04_network_layer_data_plane/4.4_sdn_openflow/study.md#ch4-4-exam)）

---

<a id="ch5-4-functions"></a>

## 四、控制器核心功能

- 全网拓扑**自动发现**与维护  
- **全局路由**统一运算  
- 流表**下发、更新、删除**  
- 全网流量**状态监控**与统计  
- **统一部署**安全策略、流量管控（ACL、QoS、TE）

---

<a id="ch5-4-controllers"></a>

## 五、主流 SDN 控制器（记名）

**Floodlight** · **OpenDaylight（ODL）** · **ONOS** · **Ryu**

（实验常用 **Ryu + Mininet**）

---

<a id="ch5-4-vs-traditional"></a>

## 六、SDN 与传统网络对比（考试表）

| 对比项 | 传统网络 | SDN 网络 |
|--------|----------|----------|
| **控制平面** | **分布式**，每台设备独立运行 | **集中**在中心控制器 |
| **路由计算** | 设备间**分布式协议**（OSPF/BGP）协商 | 控制器**全局统一**计算 |
| **配置管理** | 逐台 **CLI** 手工配置 | **代码化、自动化**批量部署 |
| **运维扩展** | 配置繁杂、难度大 | 架构简洁、**易扩展、易运维** |

→ 传统痛点：[4.4 §一](../../04_network_layer_data_plane/4.4_sdn_openflow/study.md#ch4-4-pain)

---

<a id="ch5-4-challenges"></a>

## 七、SDN 现存挑战

| # | 挑战 |
|---|------|
| 1 | 控制器 **单点故障** 隐患（需集群/HA） |
| 2 | 大规模网络 **流表下发**并发压力大 |
| 3 | **多控制器**集群间数据同步、**状态一致性**难保障 |

---

<a id="ch5-4-exam"></a>

## 八、考试背诵极简版

### 口诀

```text
控数分离集中脑，南向OpenFlow北REST
拓扑算路下流表，Packet-in与Flow-mod
Floodlight ODL ONOS Ryu记
传统分布SDN集中，单点故障要集群
```

### 30 字

**SDN 控数分离；控制器集中算路下流表；南向 OpenFlow、北向 REST；优于传统分布式运维。**

### 考点速记

| 点 | 一句 |
|----|------|
| 精髓 | **控数分离**、控制**集中** |
| 南向 | **OpenFlow** → 交换机 |
| 北向 | **REST** → 应用 |
| 控制器 | 拓扑、算路、**流表下发** |
| 挑战 | **单点故障**、下发性能、**多控一致** |
| 4.4 vs 5.4 | **4.4** 数据面/流表；**5.4** 控制面/控制器 |

### 易错点

| 易混 | 纠正 |
|------|------|
| SDN = 没有控制平面？ | **有**，且**上收到控制器** |
| OpenFlow = 北向？ | **南向**；北向是 **REST** 等 |
| SDN 取代 OSPF/BGP？ | 常**协同**；SDN 管策略/流表，IGP/BGP 仍可存在 |
| 目录 5.4 vs 章 §5.5 | 目录 **5.4=控制器精读**；章 **§5.5=SDN** 概述 |

---

<a id="ch5-4-practice"></a>

## 九、学习实践

> 搭建 **Ryu 控制器 + Mininet** 仿真环境：实操 **流表下发**、**Packet-in** 触发、流量转发；对照 [4.4 未知流流程](../../04_network_layer_data_plane/4.4_sdn_openflow/study.md#ch4-4-flow)。

| 锚点 | 内容 |
|------|------|
| [#ch5-4-sdn-core](#ch5-4-sdn-core) | 控数分离 |
| [#ch5-4-controller](#ch5-4-controller) | 集中控制器 |
| [#ch5-4-interfaces](#ch5-4-interfaces) | 南北向 |
| [#ch5-4-vs-traditional](#ch5-4-vs-traditional) | 对比表 |
| [#ch5-4-challenges](#ch5-4-challenges) | 三大挑战 |
| [#ch5-4-exam](#ch5-4-exam) | 口诀 / 30 字 |
