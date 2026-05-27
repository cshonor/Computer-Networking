# Chapter 8 — TCP / UDP（传输层 · 后端重点）

> [README.md](../README.md) · 全书：[study.md](../study.md)

## 本节核心目标

三次握手、四次挥手、重传、Dup ACK、零窗口；能在包列表里**对上线象**。

## 大纲

| 小节 | 要点 | 完成 |
|------|------|------|
| 1 | TCP 首部字段 | [ ] |
| 2 | 三次握手 / 四次挥手 | [ ] |
| 3 | 重传与 RTO | [ ] |
| 4 | 流量控制与窗口 | [ ] |
| 5 | UDP 无连接 | [ ] |

## 笔记正文

（待填）

## 抓包练习

| 项 | 示例 |
|----|------|
| 显示过滤 | `tcp` · `tcp.flags.syn==1` · `tcp.analysis.retransmission` |
| Follow | 右键 → Follow → TCP Stream |
| PCAP | `ch08-tcp-3way.pcap`（放本章目录或仓库根目录（*.pcap 已 gitignore）） |

## 与理论书衔接

- [TCP/IP Ch12–17 TCP](../../TCP-IP-Volume1-Protocols/chapter12-tcp-basic/study.md)
- [自顶向下 §3.5 TCP](../../top_down/03_transport_layer/3.5_tcp_connection_and_transmission/)

## 排障一句话

**有 SYN 无 SYN-ACK** → 中间丢或防火墙；**大量重传** → 链路/拥塞/对端问题。

## 个人总结

（待填）
