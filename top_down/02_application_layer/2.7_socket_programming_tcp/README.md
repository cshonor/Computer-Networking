# 2.7 — socket programming tcp

## 知识点速记

- **TCP**：面向连接；**监听套接字** + **`accept` 派生连接套接字** 服务多客户端。
- **Python 要点**：`SOCK_STREAM`、`listen` 队列、`accept` 每连接处理（生产环境需并发模型）。
- **进阶**：`epoll` / 事件循环、反压、半关闭、`TIME_WAIT`（第 3 章深入）。

## 与后端开发的联系

- HTTP、gRPC、Redis 协议等多数建立在 **TCP 字节流** 之上；粘包/拆包在应用层解决。

## 延伸阅读

- 章内 TCP 示例与说明：[study.md § 2.7.3](../study.md#ch2-7-tcp)  
- 整节上下文（含 UDP 对比）：[study.md § 2.7](../study.md#ch2-7)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `demo_code/` | 建议放 TCP 实验代码 |
