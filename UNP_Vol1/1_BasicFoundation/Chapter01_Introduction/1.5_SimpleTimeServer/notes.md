# 1.5 一个简单的时间获取服务器程序

> 对应客户端：[1.2](../1.2_SimpleTimeClient/notes.md) · 并发演进：Ch 4 / Ch 5

## 核心知识点

与 1.2 呼应的 TCP 时间服务器：**bind → listen → accept → 读写 → close**，展示被动接受连接的生命周期。

## 关键函数与结构体

| API | 要点 |
|-----|------|
| `Bind(listenfd, (SA *)&servaddr, sizeof(servaddr))` | 绑定端口 **13** 与本地地址 **`INADDR_ANY`**（接受任意网卡上的连接） |
| `Listen(listenfd, LISTENQ)` | 套接字变为**监听套接字**；`LISTENQ` = 内核排队最大连接数 |
| `Accept(listenfd, NULL, NULL)` | 阻塞等待连接；三次握手完成后返回**已连接套接字 `connfd`** |
| `time()` + `ctime()` + `snprintf()` | 秒数 → 可读时间字符串；**用 `snprintf` 而非 `sprintf`** |
| `Write()` | 写入套接字发给客户 |
| `close(connfd)` | 关闭当前连接，触发 TCP **四分组终止** |

## 执行流程原理

```text
bind（定端口）→ listen（被动队列）→ accept（分水岭）
  监听套接字 listenfd          已连接套接字 connfd
→ 写时间 → close(connfd) → 循环再 accept
```

**迭代服务器（iterative server）**：外层死循环一次只服务一个客户；上一客户慢会**阻塞**后续 `accept`。

## 易错点与坑点

| 陷阱 | 说明 |
|------|------|
| **`sprintf` / `gets` / `strcat`** | 可能缓冲区溢出；用 **`snprintf`** 等限长函数 |
| **迭代服务器瓶颈** | 处理耗时须改**并发服务器**（`fork`、线程等，后续章节） |

## 个人学习总结

> 💡 可拓展：`LISTENQ` 与半连接/全连接队列（Linux）；守护进程化步骤。
