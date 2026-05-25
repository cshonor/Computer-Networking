# 第 1 章：简介（厚版）

> 阶段一 · 逐节 `1.x_*.md`（含核心主旨、细节、逻辑、易错、留白）

## 小节索引

| 节 | 目录 | 备注 |
|----|------|------|
| 1.1 | [1.1_Overview](./1.1_Overview.md) | C/S、TCP/IP、LAN/WAN、[C/S→B/S](./1.1_Overview.md#ch1-1-cs-bs) |
| 1.2 | [1.2_SimpleTimeClient](./1.2_SimpleTimeClient.md) | **厚** · socket/connect/循环 read |
| 1.3 | [1.3_ProtocolIndependence](./1.3_ProtocolIndependence.md) | IPv6、getaddrinfo |
| 1.4 | [1.4_ErrorHandlingWrapper](./1.4_ErrorHandlingWrapper.md) | 包裹函数、errno |
| 1.5 | [1.5_SimpleTimeServer](./1.5_SimpleTimeServer.md) | **厚** · bind/listen/accept |
| 1.6～1.12 | 各目录 | 索引/ OSI / BSD / 测试网 / POSIX / LP64 / 小结 |

## 速记

```text
C/S；两层→三层→B/S；TCP/IP；LAN 无路由 WAN 经路由器。
客户 socket→connect→while read；服 bind→listen→accept。
包裹函数大写；errno 仅错误时有意义。
协议无关→Ch11 getaddrinfo；套接字在应用↔传输交界。
```
