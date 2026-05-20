# 4.2 — router internal working

## 知识点速记

- **四块**：输入（LPM/TCAM）→ 交换结构（内存/总线/Crossbar）→ 输出（队列/调度）→ 控制 CPU。  
- **三种交换**：[精读+对比表](./study.md#ch4-2-switching) · [总线图](./study.md#ch4-2-switch-diagram) · [背诵](./study.md#ch4-2-switch-exam)  
- **输入/输出排队**与 **HOL 阻塞**概念。  
- **队列丢包**：[Tail Drop](./study.md#ch4-2-tail-drop) · [RED 曲线](./study.md#ch4-2-red-diagram) · [WRED](./study.md#ch4-2-wred-diagram) · [WFQ 读图](./study.md#ch4-2-wfq-diagram) · [速记卡](./study.md#ch4-2-queue-exam)  
- **调度**：FIFO、优先级、**WFQ**（与 AQM 配合）。  
- **缓冲**：警惕 Bufferbloat；经验式 **`B ≈ (RTT·R)/√N`** 仅作量级直觉（见章内说明）。

## 与后端开发的联系

- 云上「同区延迟」与「跨区 RTT」、队列丢包导致 TCP 吞吐塌陷，都与路由器/交换机排队与缓冲策略相关。

## 延伸阅读

- 章级精读：[study.md § 4.2](../study.md#ch4-2)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `demo_code/` | 示例代码 |
