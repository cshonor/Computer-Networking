# 10.5 第一层——报文传输

> 本章：[chapter-summary.md](./chapter-summary.md#ch10-5) · [10.8 WebMUX](./08-webmux.md)

## 本节核心目标

报文传输层的**性能目标**：降时延、复用、多路复用、公平分段。

---

<a id="ch10-5-goals"></a>

## 优化机制

| 机制 | 作用 |
|------|------|
| **管道化 / 批量化** | 减少 RTT |
| **连接重用** | 提高带宽利用率 |
| **多路复用** | 单物理连接上**并行多报文流** |
| **分段与交错** | 不同优先级流公平传输，减轻**线头阻塞（HOL）** |

→ 对比 HTTP/1.1 管道 [ch04](../chapter-04-connection-management/06-pipeline-connection.md)（仍 FIFO 响应）

---

## 抓包/实操记录

（待填：HTTP/2 多 Stream 同连接）

---

## 疑问与总结

**第一层只管「怎么快传」，不管 GET/POST 语义。**
