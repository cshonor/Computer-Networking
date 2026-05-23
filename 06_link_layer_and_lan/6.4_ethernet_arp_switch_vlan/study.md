# 6.4 以太网、ARP、交换机与 VLAN

> 章级精读：[§6.4](../study.md#ch6-4) · **ARP 精编**：[#ch6-4-arp](#ch6-4-arp) · **VLAN**：[#ch6-4-vlan](#ch6-4-vlan)

## 一、以太网（Ethernet）

> 帧与 IP 嵌套 → [§6.1 帧≠IP](../study.md#ch6-frame-vs-ip) · [帧结构图](../study.md#ch6-ethernet-frame)

![以太网帧结构](../assets/ethernet_frame_structure.png)

- 目前局域网主流技术，基于 IEEE 802.3 / **Ethernet II**
- **Ethernet II 帧**（左→右）：前导 7 + SFD 1 + 目的/源 MAC 各 6 + 类型 2（`0x0800`=IPv4，**`0x0806`=ARP**）+ 数据 46–1500 + FCS 4
- **帧长**：最小 64B、最大 1518B（MTU **1500B**）
- 接收：**目的 MAC 匹配本口** → 验 FCS/帧长 → 剥帧上交网络层

---

## 二、ARP（地址解析协议）

<a id="ch6-4-arp"></a>

> **IP→MAC；查缓存→广播请求→单播应答→写缓存；帧类型 0x0806，非 IP 包。**

→ 章级报文十六进制：[#ch6-arp-format](../study.md#ch6-arp-format) · IPv6 用 **NDP**（非 ARP）

---

<a id="ch6-4-arp-def"></a>

### 1. 基础定义

**ARP（Address Resolution Protocol，地址解析协议）**  
工作在**网络层与数据链路层之间**，核心：**IP 地址 → MAC 地址**（三层地址译成二层地址）。

| 项 | 说明 |
|----|------|
| 标准 | **RFC 826** |
| 范围 | 仅 **IPv4**（IPv6 用 **NDP**） |

---

### 2. 核心背景（为什么需要 ARP）

| 层 | 地址 | 作用 |
|----|------|------|
| **网络层（IP）** | IP | **跨网段寻址**（找主机） |
| **链路层（MAC）** | MAC | **局域网内帧投递**（送到网卡） |

同网段通信：已知对方 **IP**，不知 **MAC** → **必须 ARP 转换**。

---

<a id="ch6-4-arp-flow"></a>

### 3. 工作流程（必背：查→广播→单播→存缓存）

1. 查**本地 ARP 缓存**（IP ↔ MAC）
2. **无记录** → 发 **ARP 请求（广播）**：「谁是 x.x.x.x？请回复 MAC。」
3. 同网段都收到；**仅 IP 匹配者** **单播应答**，带自己 MAC
4. 请求方**写入缓存**，后续直接用
5. 缓存**老化（约 20–60 分钟）**，过期重新解析

**一句话**：**广播请求、单播回应、缓存加速**。

---

<a id="ch6-4-arp-format"></a>

### 4. 报文格式（28 字节，以太网 Payload）

ARP **不是 IP 包**；封装在以太网帧 **Payload**，帧类型 **`0x0806`**。

![ARP 报文格式（32 位行对齐）：Hardware/Protocol Type → Operation 1/2 → Sender/Target 地址](../assets/arp_message_format_32bit.png)

| 图上字段 | 长度 | 典型值 / 说明 |
|----------|------|----------------|
| **Hardware Type** | 16 bit | 以太网 = **1** |
| **Protocol Type** | 16 bit | IPv4 = **0x0800** |
| **Hardware Length** | 8 bit | MAC = **6** |
| **Protocol Length** | 8 bit | IP = **4** |
| **Operation** | 16 bit | **1=Request，2=Reply** |
| **Sender Hardware Address** | 48 bit | 发送方 **MAC** |
| **Sender Protocol Address** | 32 bit | 发送方 **IP** |
| **Target Hardware Address** | 48 bit | 请求 **全 0**；应答 **真实 MAC** |
| **Target Protocol Address** | 32 bit | 要解析的 **IP** |

**合计**：2+2+1+1+2+6+4+6+4 = **28 字节**（以太网 IPv4/ARP 典型）

**请求 vs 应答（考试常考）**

| | **请求** | **应答** |
|---|----------|----------|
| 操作码 | **`0001`** | **`0002`** |
| ARP 目标 MAC | **`00:00:00:00:00:00`** | 真实 MAC |
| 以太网目的 MAC | **广播 FF:FF:FF:FF:FF:FF** | **单播**（请求方 MAC） |

→ 十六进制抓包示例：[#ch6-arp-format](../study.md#ch6-arp-format)

---

<a id="ch6-4-arp-extra"></a>

### 5. 关键附属机制

| 机制 | 说明 |
|------|------|
| **ARP 缓存** | 减广播；Windows `arp -a`，Linux `arp -n` |
| **免费 ARP（GARP）** | 主动广播自身 IP–MAC；**检测 IP 冲突**、更新邻居缓存 |
| **代理 ARP** | 路由器替跨网主机应答；跨子网「像同网段」 |
| **RARP** | MAC→IP；老旧无盘（了解） |

---

<a id="ch6-4-arp-security"></a>

### 6. 常见问题与攻击

| 问题 | 说明 |
|------|------|
| **ARP 欺骗（中毒）** | 伪造应答改他人缓存 → **流量劫持、中间人** |
| **IP 冲突** | 多机同 IP → 解析混乱 |
| **防御** | **静态 ARP 绑定**（固定 IP–MAC） |

---

<a id="ch6-4-arp-example"></a>

### 7. 通信举例（同网段）

电脑 **192.168.1.10** 访问 **192.168.1.20**：

1. 查缓存，无 `.20` 的 MAC  
2. **广播** ARP 请求  
3. `.20` **单播**回复 MAC  
4. 存缓存，封装以太网帧发送  

---

<a id="ch6-4-arp-cross-subnet"></a>

### 8. 跨子网通信（重点）

- **IP 目的** = 远端主机  
- **以太网目的 MAC** = **默认网关 MAC**（不是远端主机 MAC）

**流程**：**先 ARP 网关 IP** → 得网关 MAC → 帧发给网关 → 网关三层转发。

→ 逐跳实例：[4.3 一包怎么走](../../04_network_layer_data_plane/study.md#ch4-packet-walkthrough)

---

<a id="ch6-4-arp-exam"></a>

### 9. 考试默写 · 易错点

**5 行默写版**

```text
ARP：RFC826，IPv4 专用，IP→MAC，非 IP 包，以太网类型 0x0806。
流程：查缓存→广播请求(0001)→单播应答(0002)→写缓存(老化20–60min)。
请求：目标MAC全0，以太网目的广播；应答：单播回请求方。
跨子网：IP指远端，二层MAC指默认网关；先ARP网关。
攻击：ARP欺骗改缓存→静态绑定；IPv6用NDP不用ARP。
```

### 30 字

**ARP 把 IP 译 MAC；广播问、单播答、缓存；0x0806；跨网先 ARP 网关。**

| 易混 | 纠正 |
|------|------|
| ARP 是 IP 协议？ | **否**；以太网 **Payload**，类型 **0x0806** |
| 跨子网 ARP 目标主机？ | **否**；**ARP 网关**，MAC 填**网关** |
| IPv6 用 ARP？ | **NDP**（邻居发现） |
| 应答也广播？ | **否**；**单播**给请求方 |
| 请求目标 MAC？ | **全 0**（尚未知） |

---

## 三、交换机（Switch）

- 数据链路层设备，按 **MAC** 转发帧
- **学习**源 MAC→端口 → **转发**到目的端口；未知则**泛洪**
- 隔离**冲突域**（相对 Hub），端口常全双工

## 四、VLAN 虚拟局域网

<a id="ch6-4-vlan"></a>

> **一个 VLAN = 一个广播域；802.1Q 用 4 字节 Tag（VID）标识；Access 接终端剥标，Trunk 交换机互联带标。**

---

<a id="ch6-4-vlan-def"></a>

### 1. 什么是 VLAN

**VLAN（Virtual Local Area Network，虚拟局域网）**：把**同一物理局域网**在**逻辑上**划成**多个独立广播域**。

| 规则 | 说明 |
|------|------|
| **同 VLAN** | 可直接**二层互通** |
| **不同 VLAN** | **二层隔离**；互通须 **三层设备**（路由器 / 三层交换机） |

**作用（必背）**

| | |
|--|--|
| ✅ **隔离广播域** | 广播只在本 VLAN 内，不扩散全网 |
| ✅ **提高安全** | 不同部门默认隔离 |
| ✅ **管理灵活** | 按部门/业务划分，**不受物理位置限制** |

![VLAN 广播隔离：广播只在所属 VLAN 内泛洪](../assets/vlan_broadcast_isolation.png)

**图上要点**：同一交换机物理相连，**VLAN2 的广播不会进 VLAN1/VLAN3** → **一个 VLAN = 一个广播域**。

---

<a id="ch6-4-8021q"></a>

### 2. 802.1Q 标签（VLAN 核心）

**802.1Q**：IEEE 标准，定义 VLAN **帧格式**与跨交换机转发。

**在以太网帧 MAC 头后插入 4 字节 Tag**：

| 字段 | 长度 | 说明 |
|------|------|------|
| **TPID** | 2B | 固定 **`0x8100`**，标识 802.1Q 帧 |
| **TCI** | 2B | 含 **PCP**（3bit QoS）、**DEI**（1bit）、**VID**（12bit **VLAN ID**） |

- **VID 范围**：**1–4094**（**0、4095 保留**）
- **一句话**：交换机靠 **VID** 识别帧属于哪个 VLAN

![802.1Q 帧：Dest MAC + Src MAC + VLAN Tag(4B) + Type + Payload + FCS](../assets/ieee_8021q_frame_access_trunk.png)

| 图上要点 | 含义 |
|----------|------|
| **Tag 位置** | 插在**源 MAC 之后、Type 之前** |
| **Access 口** | 收：**无标帧打 PVID**；发：**剥标**给终端 |
| **Trunk 口** | 收/发：**带允许 VLAN 的标签**（Native VLAN 除外见下） |

→ 以太网帧基础：[§6.1 帧≠IP](../study.md#ch6-frame-vs-ip)

---

<a id="ch6-4-access-trunk"></a>

### 3. 端口类型：Access / Trunk

#### Access 端口（接入端口）

| 项 | 说明 |
|----|------|
| **连接** | **PC、打印机**等终端 |
| **VLAN 数** | **只能 1 个 VLAN** |
| **收帧** | 无标签 → 打上本端口 **PVID**（Port VLAN ID） |
| **发帧** | **去掉标签**（终端不认 Tag） |

**口诀**：**单 VLAN，进打标，出剥标**

#### Trunk 端口（中继端口）

| 项 | 说明 |
|----|------|
| **连接** | **交换机之间**、连路由器 Trunk 子接口 |
| **VLAN 数** | **允许多个 VLAN** 通过 |
| **收帧** | 带 Tag → **保留** |
| **发帧** | **除 Native VLAN（常默认 VLAN 1）外都带 Tag** |

**口诀**：**多 VLAN，带标签，交换机互联**

![Trunk：核心交换机与多台接入交换机，VLAN1/2/3 跨 Trunk 传递](../assets/vlan_trunk_multi_switch.png)

**图上要点**：各接入交换机下都有 VLAN1/2/3 云；**Trunk 口**在交换机间传**带 Tag 的多 VLAN 流量**。

---

<a id="ch6-4-vlan-compare"></a>

### 4. Access vs Trunk 对比（考试常考）

| 对比项 | **Access** | **Trunk** |
|--------|------------|-----------|
| 连接对象 | PC、终端 | **交换机**、路由器 |
| 所属 VLAN | **1 个** | **多个** |
| 发帧标签 | **不带标签** | **带标签**（Native VLAN 除外） |
| 核心作用 | 接入终端 | **跨交换机传递 VLAN** |

---

<a id="ch6-4-vlan-exam"></a>

### 5. 关键结论 · 易错点

**必背 5 条**

1. **一个 VLAN = 一个广播域**
2. **802.1Q** 插 **4 字节 Tag**，**VID** 标识 VLAN（1–4094）
3. **Access**：接终端，单 VLAN，**出帧无标签**
4. **Trunk**：交换机互联，多 VLAN，**出帧带标签**
5. **VLAN 间默认二层隔离**，互通需**三层转发**

| 易混 | 纠正 |
|------|------|
| VLAN = 不同网段？ | **二层广播域**；同 VLAN 可同网段；跨 VLAN 要**路由** |
| 终端能收带 Tag 帧？ | **一般不能**；Access **出帧剥标** |
| Trunk 只传一个 VLAN？ | **否**；**多 VLAN** 带 Tag 同链路传 |
| VID=0 能用？ | **0/4095 保留**；可用 **1–4094** |
| VLAN 靠 IP 区分？ | **靠 802.1Q VID**；IP 是三层 |

### 考试标准段落（可直接默写）

> VLAN 将同一物理 LAN 逻辑划分为多个广播域。802.1Q 在以太网帧中插入 4 字节标签，TPID 为 0x8100，VID（12bit）标识 VLAN（1–4094）。Access 端口连接终端，只属于一个 VLAN，收帧打 PVID、发帧剥标签；Trunk 端口用于交换机互联，允许多 VLAN 通过，发帧带标签（Native VLAN 除外）。不同 VLAN 二层隔离，跨 VLAN 通信需三层设备转发。

### 30 字

**一 VLAN 一广播域；802.1Q 四字节 VID；Access 单 VLAN 剥标；Trunk 多 VLAN 带标跨交换机。**

---

## 五、本节核心考点

- ARP 流程、缓存、请求/应答、广播/单播
- 同网段 vs 跨子网（网关 MAC）
- 交换机自学习、**VLAN / Access / Trunk / 802.1Q**

## 六、锚点索引

| 锚点 | 内容 |
|------|------|
| [#ch6-4-arp](#ch6-4-arp) | ARP 总览 |
| [#ch6-4-arp-flow](#ch6-4-arp-flow) | 工作流程 |
| [#ch6-4-arp-format](#ch6-4-arp-format) | 报文格式 |
| [#ch6-4-arp-cross-subnet](#ch6-4-arp-cross-subnet) | 跨子网 |
| [#ch6-4-arp-exam](#ch6-4-arp-exam) | 默写 · 易错 |
| [#ch6-4-vlan](#ch6-4-vlan) | VLAN 总览 |
| [#ch6-4-vlan-def](#ch6-4-vlan-def) | 定义与作用 |
| [#ch6-4-8021q](#ch6-4-8021q) | 802.1Q 帧 |
| [#ch6-4-access-trunk](#ch6-4-access-trunk) | Access / Trunk |
| [#ch6-4-vlan-compare](#ch6-4-vlan-compare) | 对比表 |
| [#ch6-4-vlan-exam](#ch6-4-vlan-exam) | 易错 · 默写段 |

---

## 七、个人学习心得与补充

> 可画带 VLAN 的组网图；`arp -a` 对照本机缓存
