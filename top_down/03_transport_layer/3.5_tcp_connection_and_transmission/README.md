# 3.5 — TCP 连接与传输

## 知识点速记

- **四特性**：面向连接、可靠、字节流、全双工
- **三次握手**：[状态图](./study.md#ch3-5-diagram-handshake) · SYN/ACK 序号计算
- **四次挥手**：[半关闭+TIME_WAIT](./study.md#ch3-5-diagram-close)
- **可靠**：累积 ACK、超时重传、**3 重复 ACK 快重传**
- **背诵**：[50 字](./study.md#ch3-5-exam) · rwnd：[章级 flow](../study.md#ch3-5-flow)

## 与后端开发的联系

- `CLOSE_WAIT` 泄漏、`TIME_WAIT` 过多、握手/挥手序号算错

## 延伸阅读

- [study.md](./study.md) · [3.4 可靠原理](../3.4_reliable_data_transfer_principle/study.md)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记 |
| `study.md` | 可背诵完整版 |
| `demo_code/` | 示例代码 |
