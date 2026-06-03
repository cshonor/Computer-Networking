# 第 1 章：简介（厚版）

> 阶段一 · 逐节 `1.x_*.md`（含核心主旨、细节、逻辑、易错、留白）

## 小节索引

| 节 | 目录 | 备注 |
|----|------|------|
| 1.1 | [1.1_Overview](./1.1_Overview.md) | C/S、TCP/IP、LAN/WAN、[C/S→B/S](./1.1_Overview.md#ch1-1-cs-bs) |
| 1.2 | [1.2_SimpleTimeClient](./1.2_SimpleTimeClient.md) | **主笔记** + [阅读地图](1.2_SimpleTimeClient.md#ch1-2) |
| 1.2 附录 | [API](1.2_Appendix_API精读.md) · [源码](1.2_Appendix_源码与考点.md) · [C/字节序](1.2_Appendix_C新手与字节序.md) · [Rust](1.2_Appendix_Rust客户端.md) | 详文拆开、不重复 |

<a id="ch1-2"></a>

### 1.2 时间客户端（速记）

→ [主笔记·五步法/IP端口](1.2_SimpleTimeClient.md#ch1-2-flow) · [API connect/read](1.2_Appendix_API精读.md) · [源码](1.2_Appendix_源码与考点.md) · [C FAQ](1.2_Appendix_C新手与字节序.md)

**五步法**：`socket(AF_INET,TCP,0)` → 填 **sin_addr=IP / sin_port=13** → `connect` → **`while read`** → `exit` · [socket 三参数](1.2_SimpleTimeClient.md#ch1-2-socket)

| 易错 | 规范 |
|------|------|
| 搞不清 IP/端口 | **sin_addr / sin_port** 见主笔记表 |
| 一次 read 读全 | **while** |
| connect 失败再 connect | **close + 新 socket** |

**13 端口 Daytime**；对端 [1.5 服务器](./1.5_SimpleTimeServer.md)

| 1.3 | [1.3_ProtocolIndependence](./1.3_ProtocolIndependence.md) | **厚** · 协议无关/getaddrinfo |
| 1.4 | [1.4_ErrorHandlingWrapper](./1.4_ErrorHandlingWrapper.md) | **厚** · 包裹/errno/Pthread |
| 1.5 | [1.5_SimpleTimeServer](./1.5_SimpleTimeServer.md) | **厚** · bind/listen/accept |

<a id="ch1-4"></a>

### 1.4 错误处理 · 包裹函数（速记）

→ 精读：[1.4_ErrorHandlingWrapper.md](./1.4_ErrorHandlingWrapper.md) · [包裹源码](1.4_ErrorHandlingWrapper.md#ch1-4-source)

**规则**：小写 = 系统调用；**大写 = 包裹**（内建 `err_sys`）

| 范式 | 失败时 |
|------|--------|
| Unix API | **-1** + **errno** → `err_sys` |
| **Pthread** | **返回错误码**，**不**置 errno |

**不能盲用大写**：**EINTR / EAGAIN / ECONNRESET** → 小写 + 分支（Ch 5/6）

**链路**：1.2 裸 `if` → 1.4 `Socket`/`Connect` → Ch5/6 改造
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
