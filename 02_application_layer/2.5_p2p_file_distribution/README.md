# 2.5 — p2p file distribution

## 知识点速记

- **C/S vs P2P 下界**：`D_CS` 与 `D_P2P` 典型 `max{...}` 公式；P2P 含 **Σu_i** 项体现聚合上行。
- **自扩展**：规模上升时，若激励与可达性良好，总供给能力可随 peer 增加。
- **BitTorrent**：**Rarest First** + **Tit-for-Tat** 抑制搭便车。

## 与后端开发的联系

- 大文件分发、软件更新、实时音视频 SFU 等，本质是**谁在承担带宽与时间下界**。

## 延伸阅读

- 章级精读：[study.md § 2.5](../study.md#ch2-5)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `problem.md` | 错题与面试题 |
| `demo_code/` | 示例代码 |
