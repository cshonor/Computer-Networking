# 1.2 一个简单的时间获取客户程序

> [1.5 服务器](../1.5_SimpleTimeServer/notes.md) · [Ch 3.9 readn](../../Chapter03_SocketProgramIntro/3.9_Readn_Writen_Readline/notes.md)

---

## 核心主旨与关键论据

约 27 行 **TCP 时间客户端**，展示 **`socket → 填地址 → connect → 循环 read → exit`** 最小 API 路径。数据科学环境更常用 IPython/Jupyter，但底层仍是这些系统调用。

---

## 关键函数与代码拆解

| 步骤 | API | 要点 |
|------|-----|------|
| 头文件 | `#include "unp.h"` | 打包系统头与 `MAXLINE` |
| 创建 | `socket(AF_INET, SOCK_STREAM, 0)` | TCP/IPv4 |
| 地址 | `sockaddr_in` + **`bzero`** + **`htons(13)`** + **`inet_pton`** | 端口 13；网络字节序 |
| 连接 | `connect(sockfd, (SA *)&servaddr, sizeof(...))` | 强转 `SA *` |
| 读取 | **`while (read(...))`** | TCP **无边界**；26 字节可能 10+16 |
| 退出 | `exit` | 自动 **close** 所有 fd |

---

## 逻辑脉络

```text
准备通道 → 填目标 → 三次握手 → 循环读直到 0/错误 → exit 触发 FIN
```

---

## 易错细节与重点结论

| 陷阱 | 纠正 |
|------|------|
| 一次 read 读全 | 必须 **while** |
| `memset` 参数写反 | 本书用 **bzero** |
| connect 失败再 connect | **close + 新 socket** |

---

> 💡 **后续拓展留白**  
> - `EINTR` 处理  
> - sockaddr 对齐图  

---

## 个人学习总结

（待填）
