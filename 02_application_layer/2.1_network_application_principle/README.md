# 2.1 — network application principle

## 知识点速记

- **定位**：最顶层；Socket（IP+端口）
- **端口**：[应用约定=TCP首部端口](./study.md#ch2-1-ports-tcp)（80/443/25/143…）
- **C/S vs P2P**：[背诵对比表](./study.md#ch2-1-exam) — Web/邮件 vs BT/区块链
- **选 TCP/UDP**：可靠性、时延、带宽、完整性四维
- **口诀**：可靠→TCP；实时→UDP

## 与后端开发的联系

- 微服务/API 先定：**协议、会话、缓存** 各在哪一层；别把缓存策略当成应用协议本身

## 延伸阅读

- 背诵版：[study.md](./study.md) · 章级：[§2.1](../study.md#ch2-1) · [2.5 P2P](../2.5_p2p_file_distribution/study.md)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记 |
| `study.md` | 可背诵完整版 + 易错表 |
| `demo_code/` | 示例代码 |
