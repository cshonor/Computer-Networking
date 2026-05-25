# 第 1 章：简介（Introduction）

> 《UNIX 网络编程》卷 1 · 阶段一 [1_BasicFoundation](../)  
> 逐节笔记：各 `x.x_*/notes.md` · 代码：`code/original_c`

## 本章目标

建立网络编程前提（客户/服务器、TCP/IP、LAN/WAN），用**极简 TCP 时间程序**走通客户端与服务器 API 流程，并确立**包裹函数、POSIX、协议无关**等全书规范。

---

## 小节索引

| 节 | 目录 | 主题 |
|----|------|------|
| 1.1 | [1.1_Overview](./1.1_Overview/notes.md) | 概述、C/S、TCP/IP、LAN/WAN |
| 1.2 | [1.2_SimpleTimeClient](./1.2_SimpleTimeClient/notes.md) | TCP 时间客户端、`socket/connect/read` |
| 1.3 | [1.3_ProtocolIndependence](./1.3_ProtocolIndependence/notes.md) | IPv4→IPv6、协议无关 |
| 1.4 | [1.4_ErrorHandlingWrapper](./1.4_ErrorHandlingWrapper/notes.md) | 包裹函数、`errno` |
| 1.5 | [1.5_SimpleTimeServer](./1.5_SimpleTimeServer/notes.md) | `bind/listen/accept`、迭代服务器 |
| 1.6 | [1.6_ProgramIndex](./1.6_ProgramIndex/notes.md) | 全书示例程序索引 |
| 1.7 | [1.7_OSIModel](./1.7_OSIModel/notes.md) | OSI 与 TCP/IP、套接字边界 |
| 1.8 | [1.8_BSDNetworkHistory](./1.8_BSDNetworkHistory/notes.md) | BSD 网络史 |
| 1.9 | [1.9_TestNetworkHost](./1.9_TestNetworkHost/notes.md) | 测试拓扑与 `netstat` 等 |
| 1.10 | [1.10_UnixStandard](./1.10_UnixStandard/notes.md) | POSIX / SUS / IETF |
| 1.11 | [1.11_64BitArchitecture](./1.11_64BitArchitecture/notes.md) | LP64、`socklen_t` |
| 1.12 | [1.12_Summary](./1.12_Summary/notes.md) | 本章小结 |

---

## 一章速记

```text
C/S + TCP/IP；LAN 无路由，WAN 经路由器连 Internet。
客户：socket → connect → while(read)；TCP 无边界必须循环读。
服务器：bind → listen → accept → write → close；迭代=一次一客户。
包裹函数大写版统一 err_sys；协议无关靠 getaddrinfo（Ch11）。
套接字在应用层↔传输层交界；64位长度用 socklen_t。
```

| 易混 | 一句 |
|------|------|
| Internet vs internet | 专有全球网 vs 任意 TCP/IP 网 |
| HTTP vs TCP/IP | 应用协议 vs 传输/网络协议 |
| listenfd vs connfd | 监听套接字 vs 已连接套接字 |
