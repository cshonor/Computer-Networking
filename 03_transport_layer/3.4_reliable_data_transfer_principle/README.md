# 3.4 — 可靠数据传输原理

## 知识点速记

- **不可靠**：比特差错、丢包、乱序 → **ACK、超时、序号、窗口**
- **rdt**：1.0 理想 → 2.0 NAK → 2.1 序号+ACK → **3.0 停等+超时**
- **SW**：[ACK 丢失读图](./study.md#ch3-4-diagram-sw) · \(U=T_D/(T_D+RTT+T_A)\)
- **GBN**：发 N 收 1、[累积 ACK](./study.md#ch3-4-diagram-gbn)、丢包回退
- **SR**：发 N 收 N、单包重传；\(W_s+W_r\le 2^k\)
- **背诵**：[50 字](./study.md#ch3-4-exam)

## 与后端开发的联系

- 自定义协议、MQ、QUIC 内部均复用「序号 + 窗口 + 重传」

## 延伸阅读

- [study.md](./study.md) · [3.3 UDP](../3.3_udp_protocol/study.md) · [3.5 TCP](../3.5_tcp_connection_and_transmission/study.md)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记 |
| `study.md` | 可背诵完整版 |
| `demo_code/` | 示例代码 |
