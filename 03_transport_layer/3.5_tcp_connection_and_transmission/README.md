# 3.5 — tcp connection and transmission

## 知识点速记

- **字节流**：序号/确认号基于字节；**MSS** 多指载荷上限量级。
- **RTT 与超时**：`EstimatedRTT`、`DevRTT`、`TimeoutInterval = Est + 4·Dev`（教材常用系数）。
- **连接管理**：三次握手、四次挥手；**TIME_WAIT = 2MSL**（时长依实现）。
- **流量控制**：见同章 [rwnd 小节](../study.md#ch3-5-flow)（与 `3.6_tcp_flow_control` 目录对应）。

## 与后端开发的联系

- 连接泄漏、`CLOSE_WAIT`、`TIME_WAIT` 过多、Nagle 与延迟 ACK 交互等线上经典问题。

## 延伸阅读

- 章级精读：[study.md § 3.5](../study.md#ch3-5) · [流量控制 rwnd](../study.md#ch3-5-flow)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `problem.md` | 错题与面试题 |
| `demo_code/` | 示例代码 |
