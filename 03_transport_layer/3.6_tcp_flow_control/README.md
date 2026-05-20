# 3.6 — TCP 流量控制

## 知识点速记

- **定义**：接收方限发送速率，防**接收缓冲区**溢出
- **rwnd**：剩余可收字节；首部 **Window** 字段随 ACK 通告
- **公式**：`min(rwnd, cwnd)`；cwnd 属拥塞控制
- **零窗口**：rwnd=0 停发 → **探测** + **窗口更新**
- **背诵**：[3 行口诀](./study.md#ch3-6-exam) · 章级：[§3.5-flow](../study.md#ch3-5-flow)

## 与后端开发的联系

- 慢客户端、大上传：无视 rwnd 会丢包；抓包可见 persist 探测

## 延伸阅读

- [study.md](./study.md) · [3.5 TCP](../3.5_tcp_connection_and_transmission/study.md) · [3.7 拥塞](../3.7_tcp_congestion_control/study.md)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记 |
| `study.md` | 可背诵完整版 |
| `demo_code/` | 示例代码 |
