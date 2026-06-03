# 第 1 章：简介（厚版）

> 阶段一 · 逐节 `1.x_*.md`（含核心主旨、细节、逻辑、易错、留白）

## 小节索引

| 节 | 目录 | 备注 |
|----|------|------|
| 1.1 | [1.1_Overview](./1.1_Overview.md) | C/S、TCP/IP、LAN/WAN、[C/S→B/S](./1.1_Overview.md#ch1-1-cs-bs) |
| 1.2 | [1.2_SimpleTimeClient](./1.2_SimpleTimeClient.md) | **厚** · 五步法/socket/connect/循环 read/易错 |

<a id="ch1-2"></a>

### 1.2 时间客户端（速记）

→ 精读：[1.2](./1.2_SimpleTimeClient.md) · [C 源码](1.2_SimpleTimeClient.md#ch1-2-source) · [Rust](1.2_SimpleTimeClient.md#ch1-2-rust) · [字节序](1.2_SimpleTimeClient.md#ch1-2-byteorder) · [总结](1.2_SimpleTimeClient.md#ch1-2-summary)

**五步法**：`socket` → **组装 IP+端口（网络序：hton* / inet_pton）** → `connect`（内核三次握手）→ **`while read`** → `close`/`exit`

| 易错 | 规范 |
|------|------|
| 一次 read 读全 | **while**（TCP 无边界） |
| connect 失败再 connect | **close + 新 socket** |
| memset 写反 | **bzero** 清零 |

**13 端口 Daytime**；对端 [1.5 服务器](./1.5_SimpleTimeServer.md)

| 1.3 | [1.3_ProtocolIndependence](./1.3_ProtocolIndependence.md) | **厚** · 协议无关/getaddrinfo |
| 1.4 | [1.4_ErrorHandlingWrapper](./1.4_ErrorHandlingWrapper.md) | 包裹函数、errno |
| 1.5 | [1.5_SimpleTimeServer](./1.5_SimpleTimeServer.md) | **厚** · bind/listen/accept |
| 1.6～1.12 | 各目录 | 索引/ OSI / BSD / 测试网 / POSIX / LP64 / 小结 |

<a id="ch1-3"></a>

### 1.3 协议无关性（速记）

→ 精读：[1.3_ProtocolIndependence.md](./1.3_ProtocolIndependence.md) · [对照表](1.3_ProtocolIndependence.md#ch1-3-struct) · [三套源码](1.3_ProtocolIndependence.md#ch1-3-source)

**1.2 硬编码 IPv4** → **图 1-6 硬编码 IPv6**（仍耦合）→ **`getaddrinfo` + `AF_UNSPEC`**（双栈）

| 文件 | 模式 |
|------|------|
| [code/1.2/…/daytimetcpcli.c](./code/1.2_SimpleTimeClient/original_c/daytimetcpcli.c) | IPv4 硬编码 |
| [code/1.3/…/daytimetcpcli6.c](./code/1.3_ProtocolIndependence/original_c/daytimetcpcli6.c) | IPv6 硬编码 |
| [code/1.3/…/daytimetcpcligai.c](./code/1.3_ProtocolIndependence/original_c/daytimetcpcligai.c) | 协议无关 |

**规范**：禁用 `gethostbyname`；**`freeaddrinfo`** 必调 → [Ch 11.6](../../2_AdvancedSkill/Chapter11_Name_Address_Convert/11.6_Getaddrinfo_Func.md)

## 速记

```text
C/S；两层→三层→B/S；TCP/IP；LAN 无路由 WAN 经路由器。
客户 **socket→connect→while read**（[1.2 详](./1.2_SimpleTimeClient.md#ch1-2-flow)）；服 **bind→listen→accept**。
包裹函数大写；errno 仅错误时有意义。
协议无关→Ch11 getaddrinfo；套接字在应用↔传输交界。
```
