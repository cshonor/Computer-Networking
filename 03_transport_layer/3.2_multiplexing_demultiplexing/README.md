# 3.2 — multiplexing demultiplexing

## 知识点速记

- **复用**：多进程 → 封装端口 → 一条 IP；**分用**：一条 IP → 按端口分到进程。
- **UDP**：目的端口分用；**TCP**：**四元组**；80 端口 TCP 可多连接、UDP 通常单绑。
- **端口**：0–1023 周知 / 1024–49151 注册 / 49152–65535 动态。
- **速背+易错**：[§3.2 六](../study.md#ch3-2-exam) · 图：[总览](../assets/mux_demux_overview.png) · [UDP](../assets/udp_demux.png) · [TCP](../assets/tcp_mux_4tuple.png)

## 与后端开发的联系

- 同一机器多服务靠**不同端口**；连接风暴、端口耗尽、`TIME_WAIT` 占满本地端口，都与四元组与状态机相关。

## 延伸阅读

- 章级精读：[study.md § 3.2](../study.md#ch3-2)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `demo_code/` | 示例代码 |
