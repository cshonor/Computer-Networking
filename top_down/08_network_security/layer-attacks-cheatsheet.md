# 分层典型攻击 · 一页背诵版

> 与 [第 8 章 study.md](./study.md) · [TLS §8.5](./study.md#ch8-5) · [防火墙 §8.9](./study.md#ch8-9) 配合  
> TCP/IP 卷1 第 1 章同主题：[§1.8 体系结构威胁](../../TCP-IP-Volume1-Protocols/chapter01-overview/1.8-architecture-threat.md)  
> TCP/IP 卷1 第 3 章精读：[§3.10 链路层攻击](../../TCP-IP-Volume1-Protocols/chapter03-link-layer/3.10-link-layer-security.md)  
> 协议栈对照：[§1.5 五层](../01_network_basics/1.5_protocol_layer_architecture/study.md#ch1-5) · [§6.4 ARP](../06_link_layer_and_lan/6.4_ethernet_arp_switch_vlan/study.md) · [§3.5 TCP](../03_transport_layer/3.5_tcp_connection_and_transmission/study.md) · [§2.2 HTTP](../02_application_layer/2.2_http_and_web/study.md)

---

<a id="ch8-layer-table"></a>

## 1. 本章级总表（原理 + 关联层 + 防御要点）

| 攻击 | 原理（人话） | 层 | 典型场景 | 防御要点 |
|------|----------------|-----|----------|----------|
| **IP 欺骗** | 伪造**源 IP**，接收方以为是可信主机 | 网络（IP） | 反射放大、绕过 IP 白名单 | 入口过滤（BCP38）、不单独信源 IP；上层鉴别 |
| **DoS / DDoS** | 海量无效流量或半开连接，耗尽**带宽/CPU/连接表** | 多层面 | 网站/游戏服被打瘫 | 限速、CDN、SYN Cookie、清洗、冗余 |
| **窃听** | 明文或无线链路上**抓包**看内容 | 链路嗅探 + 应用明文 | 咖啡厅 Wi‑Fi、Hub 时代 | **TLS/HTTPS**、WPA3、物理/逻辑隔离 |
| **ARP 欺骗** | 伪造 ARP 应答，改内网 **IP→MAC** 表，流量被劫持 | 链路（ARP） | 同一局域网 MITM | 静态 ARP、DAI、802.1X、加密上层 |
| **MAC 欺骗 / MAC 泛洪** | 伪造源 MAC，或塞满交换机 **CAM 表** → 泛洪可被嗅探 | 链路（帧/交换机） | 内网渗透、旁路监听 | 端口安全、MAC 绑定、划分 VLAN |
| **TCP 劫持 / 会话劫持** | 猜到 **SEQ**，插入报文篡改会话（如改金额） | 传输（TCP） | 明文长连接、弱随机 | 强随机 ISN、**TLS**、短会话 |
| **SYN 洪泛** | 大量 SYN 不回 ACK，占满**半开连接表** | 传输（TCP） | 针对 Web/SSH 端口 | SYN Cookie、防火墙、限速 |
| **UDP 洪水** | 海量 UDP 占满带宽或拖垮应用 | 传输（UDP） | DNS/NTP 反射放大 | 限速、关闭不必要 UDP、清洗 |
| **DNS 欺骗 / 缓存投毒** | 伪造 DNS 应答，域名→**恶意 IP** | 应用（DNS） | 钓鱼、劫持上网 | DNSSEC、DoH/DoT、校验应答 |
| **HTTP 劫持 / MITM** | 中间截获 **HTTP**，改页面、插广告、偷密码 | 链路→应用 | 运营商插广告、公共 Wi‑Fi | **HTTPS + HSTS**、证书校验 |

---

<a id="ch8-layer-oneline"></a>

## 2. 每层一句话（串 HTTP/TCP/IP/链路）

| 层 | 你学过的核心 | 典型攻击 | 本质 |
|----|--------------|----------|------|
| **链路** | 帧、MAC、ARP、交换机、[§6.1 三选一](../06_link_layer_and_lan/6.1_link_layer_service/study.md#ch6-1-daily) | ARP 欺骗、MAC 欺骗/泛洪、无线窃听 | 内网常**默认信任**，缺身份验证 |
| **网络** | IP、路由、[§4.3](../04_network_layer_data_plane/4.3_ipv4_ipv6_nat/study.md) | IP 欺骗、分片攻击、ICMP 洪水 | **不验源 IP 真假**，只管转发 |
| **传输** | 端口、TCP 握手/SEQ、[§3.5](../03_transport_layer/3.5_tcp_connection_and_transmission/study.md) | SYN 洪水、TCP 劫持、UDP 洪水、端口扫描 | 握手与序号可被**伪造/预测** |
| **应用** | HTTP/DNS 内容、[§2.2](../02_application_layer/2.2_http_and_web/study.md) | HTTP 劫持、DNS 欺骗、SQL 注入、XSS | **明文**或**输入未校验** |

```text
一次 HTTPS 上网（安全栈）：
浏览器 ── TLS（机密+完整+鉴别）──► 服务器
         └── TCP ── IP ── 以太网/Wi‑Fi
链路层 ARP/MITM 仍可能，但 TLS 保护应用内容（证书要对）
```

---

<a id="ch8-layer-exam"></a>

## 3. 考试 30 秒背诵（按层背）

- **链路**：ARP 欺骗 · MAC 欺骗/泛洪 · 无线窃听  
- **网络**：IP 欺骗 · ICMP/分片类攻击  
- **传输**：SYN 洪水 · TCP 劫持 · UDP 洪水  
- **应用**：HTTP 劫持 · DNS 欺骗 · SQL 注入 · XSS  

**口诀**：链偷 ARP MAC，网骗 IP，传 SYN 劫，应 HTTP DNS 注。

---

<a id="ch8-layer-analogy"></a>

## 4. 寄快递类比（新手秒懂）

| 攻击 | 类比 |
|------|------|
| IP 欺骗 | 信封写**别人的寄件人**，查不到真凶 |
| ARP 欺骗 | 门卫（ARP 表）被骗，**A 的信全转给你** |
| DoS | 一天寄 **10 万空包裹**，快递站瘫痪 |
| 窃听 | 楼道**偷看没封口的信**（明文 HTTP） |
| SYN 洪水 | 只填**寄件单不取件**，占满柜台格子 |
| DNS 欺骗 | 把「百度」地址**改成你家**（钓鱼） |
| HTTP 劫持 | 中途**换页、插广告**（HTTPS=密封箱+验章） |

---

## 5. 后续拓展留白

- [ ] [TCP/IP Ch18 TLS/IPsec](../../TCP-IP-Volume1-Protocols/chapter18-network-security/study.md)
- [ ] CSRF / 会话固定 / 点击劫持（Web 专节）
- [ ] DDoS 反射（DNS/NTP/SSDP）与 BCP38

---

## 6. 个人学习总结

（待填）
