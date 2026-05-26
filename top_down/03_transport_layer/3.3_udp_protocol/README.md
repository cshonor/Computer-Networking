# 3.3 — UDP 协议

## 知识点速记

- **RFC 768 / IP 17**；无连接、不可靠、**8 B** 固定首部
- **四特性**：无连接、不可靠、面向报文、低时延
- **首部**：[读图](./study.md#ch3-3-diagram) · 源/目的端口、长度、检验和
- **场景**：语音、直播、游戏、DNS/DHCP
- **背诵**：[30 字](./study.md#ch3-3-exam) · 对比 TCP：[章级](../study.md#ch3-3-vs-tcp)

## 与后端开发的联系

- 日志、监控、游戏、RTC；HTTP/3（QUIC）基于 UDP

## 延伸阅读

- [study.md](./study.md) · [3.2 分用](../3.2_multiplexing_demultiplexing/study.md)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记 |
| `study.md` | 可背诵完整版 |
| `demo_code/` | 示例代码 |
