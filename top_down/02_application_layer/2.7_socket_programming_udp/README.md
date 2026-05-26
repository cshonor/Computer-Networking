# 2.7 — socket programming udp

## 知识点速记

- **UDP**：无连接；`sendto` / `recvfrom`；适合可容忍丢包、低时延场景（DNS、部分实时业务等）。
- **Python 要点**：`SOCK_DGRAM`、`bind`、`recvfrom` 循环。
- **进阶**：字节序、MTU、应用层可靠性设计。

## 与后端开发的联系

- 游戏、RTC、日志上报等常选 UDP/QUIC；需自研**重传、分片、拥塞**或与 QUIC 栈配合。

## 延伸阅读

- 章内 UDP 示例与说明：[study.md § 2.7.2](../study.md#ch2-7-udp)  
- 整节上下文（含 TCP 对比）：[study.md § 2.7](../study.md#ch2-7)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `demo_code/` | 建议放 UDP 实验代码 |
