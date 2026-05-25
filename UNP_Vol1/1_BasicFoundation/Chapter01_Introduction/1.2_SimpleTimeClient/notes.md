# 1.2 一个简单的时间获取客户程序

> 对应服务器：[1.5](../1.5_SimpleTimeServer/notes.md) · 协议无关：[1.3](../1.3_ProtocolIndependence/notes.md)

## 核心知识点

约 27 行 TCP 时间客户端，展示 **socket → 填地址 → connect → 循环 read → exit** 的最小 API 流程。

## 关键函数与结构体

| API / 结构 | 要点 |
|------------|------|
| `#include "unp.h"` | 打包网络开发常用系统头文件与常量（如 `MAXLINE`） |
| `socket(AF_INET, SOCK_STREAM, 0)` | 创建 **IPv4 字节流（TCP）** 套接字，返回描述符 |
| `struct sockaddr_in` | 保存 IPv4 地址与端口 |
| `bzero()` | 结构体清零；比 `memset` 少一参数，不易写反参数顺序 |
| `htons(13)` | 端口 13（时间服务）→ **网络字节序** |
| `inet_pton()` | 点分十进制 / 文本 IP → 二进制（**支持 IPv4/IPv6**） |
| `connect(sockfd, (SA *)&servaddr, sizeof(servaddr))` | 发起 TCP 连接；需强转为通用 `SA *` 并传长度 |
| `read()` **循环** | TCP **无记录边界**；26 字节可能分多次到达（如 10+16） |
| `exit()` | 进程退出时 OS **自动关闭**所有已打开描述符（含套接字） |

## 执行流程原理

```text
socket 准备通道 → sockaddr_in 填目标 → connect 三次握手
→ while(read) 拼完整响应 → exit 回收描述符
```

**核心结论**：TCP 是**字节流**，必须把 `read` 放入循环，直到返回 **0**（对端关闭）或 **负值**（出错）。

## 易错点与坑点

| 陷阱 | 说明 |
|------|------|
| **一次 read 读全** | 广域网上极易截断；必须循环读 |
| **bzero vs memset** | `memset` 值/长度参数易写反；本书倾向 `bzero` 清零地址结构 |

## 个人学习总结

> 💡 可拓展：`sockaddr` vs `sockaddr_in` 内存对齐；`read` 遇 `EINTR` 的标准处理。
