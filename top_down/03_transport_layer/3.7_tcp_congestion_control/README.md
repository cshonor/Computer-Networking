# 3.7 — TCP 拥塞控制

## 知识点速记

- **cwnd=1**：[初值](./study.md#ch3-7-cwnd-1) · **ssthresh**：[初始大/来自上次事件](./study.md#ch3-7-ssthresh)
- **三窗联动**：[cwnd/ssthresh/rwnd](./study.md#ch3-7-three-windows) · [四阶段表](./study.md#ch3-7-cheat-sheet)
- **cwnd vs rwnd**：`min(cwnd, rwnd)` · [慢启动读图](./study.md#ch3-7-diagram-ss) · [背诵](./study.md#ch3-7-exam)
- **超时** vs **3 dup ACK**：[对照表](./study.md#ch3-7-diagram-timeout)
- **背诵**：[50 字](./study.md#ch3-7-exam)

## 与后端开发的联系

- 带宽跑不满、跨洲 RTT、BBR/CUBIC、缓冲膨胀

## 延伸阅读

- [study.md](./study.md) · [3.6 rwnd](../3.6_tcp_flow_control/study.md) · [章级 ch3-6/7](../study.md#ch3-6)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记 |
| `study.md` | 可背诵完整版 |
| `demo_code/` | 示例代码 |
