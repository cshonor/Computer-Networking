# Study Outline · TCP/IP Illustrated, Volume 1

## Repository layout

```
tcpip_vol1_notes/
├─ 01_link_layer/
│  ├─ 第1章 概述.md
│  └─ 第2章 链路层.md
├─ 02_network_layer/
│  ├─ 第3章 IP网际协议.md
│  … (ch. 4–10)
├─ 03_transport_layer/
│  ├─ 第11章 UDP用户数据报协议.md
│  … (ch. 12–13, 17–25)
├─ 04_application_layer/
│  ├─ 第14章 DNS域名系统.md
│  … (ch. 15–16, 26–30)
├─ OUTLINE.md（本文件）
└─ README.md
```

> 说明：卷1原书第 14–16 章在**应用层**内容，第 17–25 章在**传输层**；目录按原书章节号分模块存放。

---

## 推荐阅读顺序（后端向）

### 路线 A：先抓 TCP/UDP（与自顶向下第 3 章同步）

1. 第 11 章 UDP → 对照 [03_transport_layer/study.md §3.3](../03_transport_layer/study.md#ch3-3)
2. 第 17–18 章 TCP 首部、建连/终止 → 对照 [§3.1 TCP](../03_transport_layer/study.md#ch3-1-tcp-conn)
3. 第 19–21 章 交互/成块数据、超时重传 → 对照 [§3.4–3.5](../03_transport_layer/study.md#ch3-4)
4. 第 24 章 拥塞控制 → 对照 [§3.6–3.7](../03_transport_layer/study.md#ch3-6)
5. 第 22–23、25 章 定时器与性能（进阶）

### 路线 B：配合应用层

- 第 14 章 DNS → [02_application_layer/2.4](../02_application_layer/2.4_dns_service/)
- 第 27–28 章 FTP/SMTP → [2.3 邮件](../02_application_layer/2.3_email_smtp_pop3_imap/) · HTTP 见 [2.2](../02_application_layer/2.2_http_and_web/)

### 路线 C：网络层与排障

- 第 3 章 IP → [04_network_layer_data_plane](../04_network_layer_data_plane/)
- 第 4 章 ARP → [06_link_layer 6.4](../06_link_layer_and_lan/6.4_ethernet_arp_switch_vlan/)
- 第 6–8 章 ICMP / Ping / Traceroute → 排障实战，可记入 [99_practice_wireshark_lab](../99_practice_wireshark_lab/)

---

## 与「自顶向下」仓库对照表

| 卷1章节 | 主题 | 自顶向下仓库 |
|---------|------|----------------|
| 1–2 | 概述、链路层 | [01_network_basics](../01_network_basics/) · [06_link_layer](../06_link_layer_and_lan/) |
| 3 | IP | [04_network_layer_data_plane](../04_network_layer_data_plane/) |
| 4 | ARP | [06_link_layer/6.4](../06_link_layer_and_lan/6.4_ethernet_arp_switch_vlan/) |
| 6–8 | ICMP、Ping、Traceroute | 实验：[99_practice_wireshark_lab](../99_practice_wireshark_lab/) |
| 9–10 | 选路、动态选路 | [05_network_layer_control_plane](../05_network_layer_control_plane/) |
| 11 | UDP | [03_transport_layer §3.3](../03_transport_layer/study.md#ch3-3) |
| 12–13 | 广播/多播、IGMP | [03 §3.3](../03_transport_layer/study.md#ch3-3) · [07 无线](../07_wireless_mobile_network/)（选学） |
| 17–25 | TCP 全系 | [03_transport_layer](../03_transport_layer/) |
| 14 | DNS | [02/2.4 DNS](../02_application_layer/2.4_dns_service/) |
| 26–28 | Telnet/FTP/SMTP | [02 应用层](../02_application_layer/) |
| 29 | SNMP | 运维向，可选 |
| 30 | 其他 | 拓展阅读 |

---

## 学习建议

- **卷1 + Wireshark**：每章尽量抓 1 个典型报文（UDP DNS、TCP 三次握手、ICMP ping）。
- **与自顶向下互补**：自顶向下笔记记「考什么」；卷1笔记记「包长什么样、定时器怎么动」。
- 卷1 **第 12–16 章**与 **第 17 章**之间可跳读，按路线 A/B 选一侧先深入即可。
