# 2.6 TCP 连接的建立和终止

> TIME_WAIT：[2.7](../2.7_TIME_WAIT_State/notes.md) · 并发分路：[2.10](../2.10_TCP_Port_ConcurrentServer/notes.md)

## 核心知识点

**三次握手**建立、**四次挥手**终止 + **11 种状态** — 排查网络故障与理解并发套接字状态的理论核心。

## 执行流程原理

### 2.6.1 三次握手（Three-Way Handshake）

| 步 | 方向 | 内容 |
|----|------|------|
| 1 | 客户 → 服 | **SYN**，ISN = J（`connect` 触发） |
| 2 | 服 → 客 | **SYN+ACK**，ACK J+1，ISN = K（`listen`/`accept`） |
| 3 | 客 → 服 | **ACK** K+1，连接建立 |

### 2.6.2 常见 TCP 选项（SYN 中携带）

| 选项 | 作用 |
|------|------|
| **MSS** | 本端可收的最大 TCP 分节，避免 IP 分片 |
| **Window Scale** | 突破 16 位窗口 65535 上限（高 BDP 管道） |
| **Timestamp** | 精确 RTT；**PAWS** 防序列号回绕 |

### 2.6.3 四次挥手（Four-Way Teardown）

1. 主动关闭方发 **FIN**（常 `close`）  
2. 被动方内核回 **ACK** → **半关闭**，应用见 **EOF**  
3. 被动方处理完后发 **FIN**  
4. 主动方回最后 **ACK**

### 2.6.4 TCP 状态转换图

`CLOSED` · `LISTEN` · `SYN_SENT` · `SYN_RCVD` · `ESTABLISHED` · `FIN_WAIT_1` · `CLOSE_WAIT` 等共 **11 种** — 与 **`netstat`** 输出一一对应。

## 易错点与坑点

支持**同时打开**（双方同时 SYN）与**同时关闭**（双方同时 FIN）→ 特殊分支如 **`CLOSING`**。

## 个人学习总结

> 💡 Wireshark 抓 3+4 个报文，对照序列号/标志位字段。
