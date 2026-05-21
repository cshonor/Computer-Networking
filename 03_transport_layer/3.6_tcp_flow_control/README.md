# 3.6 — TCP 流量控制

## 知识点速记

- **定义**：接收方限发送速率，防**接收缓冲区**溢出
- **rwnd** · **min(rwnd,cwnd)** · [三窗一页](./study.md#ch3-6-all-windows)（链 [3.7](../3.7_tcp_congestion_control/study.md#ch3-7-three-windows)）
- **零窗口**：[停发](./study.md#ch3-6-zero-window) · [Persist 探测](./study.md#ch3-6-persist) · [窗口更新](./study.md#ch3-6-window-update)
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
