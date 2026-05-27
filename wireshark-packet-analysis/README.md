# Wireshark 数据包分析实战 — 学习笔记

> 英文目录结构，适配 **GitHub** + **NotebookLM** 上传精读。

## 学习背景

| 项 | 说明 |
|----|------|
| **前置** | [TCP/IP 详解 卷一](../TCP-IP-Volume1-Protocols/README.md) · [计算机网络 自顶向下](../top_down/README.md) |
| **目标** | 把网络理论落地**真实抓包**，服务后端开发与线上排障 |
| **实验** | [自顶向下 Wireshark 实验](../top_down/99_practice_wireshark_lab/README.md) |

## 目录结构

| 目录 | 内容 | 优先级 |
|------|------|--------|
| [01-basic-foundation](./01-basic-foundation/) | 网络基础 + 抓包原理 | **必学** |
| [02-wireshark-operation](./02-wireshark-operation/) | Wireshark 图形化操作 | **必学** |
| [03-command-line-tool](./03-command-line-tool/) | TShark / tcpdump | **必学** |
| [04-protocol-deep-dive](./04-protocol-deep-dive/) | 协议逐层抓包拆解 | **后端重点** |
| [05-real-world-practice](./05-real-world-practice/) | 慢网、故障排障案例 | **必学** |
| [06-extended-topic](./06-extended-topic/) | 安全、Wi‑Fi 抓包 | 选读 |
| [07-pcap-lab-files](./07-pcap-lab-files/) | 实验 PCAP（勿提交大文件） | 配套 |
| [08-cheat-sheet-summary](./08-cheat-sheet-summary/) | 过滤器速查、口诀 | 复习 |
| [reference](./reference/) | 延伸阅读与工具 | 存档 |

→ 章节索引：[study.md](./study.md) · 章节目录：[OUTLINE.md](./OUTLINE.md)

## 学习工具

- **Wireshark** / **TShark**
- **Docker** 实验环境（可选）
- **NotebookLM**：按章上传 `chapter-*.md` 精读；PCAP 放 `07-pcap-lab-files/`

## 使用说明

1. 每章打开对应 `chapter-*.md`，按模板填**过滤器、截图说明、PCAP 文件名**。  
2. 大体积 `.pcap` **不要进 Git**（见 `07-pcap-lab-files/.gitignore`），本地或网盘存放。  
3. 与理论笔记交叉链接：协议细节以 TCP/IP / 自顶向下为准，本仓库侧重**抓包验证**。
