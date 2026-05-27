# Wireshark 数据包分析 — 学习笔记

> **打开本文件夹**：下面每个 **`chapter-XX-*/`** 是一章，**笔记在文件夹里的 `study.md`**。

## 学习背景

| 项 | 说明 |
|----|------|
| 前置 | [TCP/IP 卷一](../TCP-IP-Volume1-Protocols/) · [自顶向下](../top_down/) |
| 目标 | 理论落地抓包，服务后端排障 |
| 实验 | [自顶向下 Wireshark 实验](../top_down/99_practice_wireshark_lab/) |

## 章节目录

| 章 | 文件夹 | 笔记 |
|----|--------|------|
| 1 | [chapter-01-network-basics](./chapter-01-network-basics/) | [study.md](./chapter-01-network-basics/study.md) |
| 2 | [chapter-02-traffic-monitor](./chapter-02-traffic-monitor/) | [study.md](./chapter-02-traffic-monitor/study.md) |
| 3 | [chapter-03-wireshark-intro](./chapter-03-wireshark-intro/) | [study.md](./chapter-03-wireshark-intro/study.md) |
| 4 | [chapter-04-capture-packet](./chapter-04-capture-packet/) | [study.md](./chapter-04-capture-packet/study.md) |
| 5 | [chapter-05-advanced-feature](./chapter-05-advanced-feature/) | [study.md](./chapter-05-advanced-feature/study.md) |
| 6 | [chapter-06-tshark-tcpdump](./chapter-06-tshark-tcpdump/) | [study.md](./chapter-06-tshark-tcpdump/study.md) |
| 7 | [chapter-07-network-layer-proto](./chapter-07-network-layer-proto/) | [study.md](./chapter-07-network-layer-proto/study.md) |
| 8 | [chapter-08-transport-layer-tcp-udp](./chapter-08-transport-layer-tcp-udp/) | [study.md](./chapter-08-transport-layer-tcp-udp/study.md) **重点** |
| 9 | [chapter-09-application-layer-proto](./chapter-09-application-layer-proto/) | [study.md](./chapter-09-application-layer-proto/study.md) |
| 10 | [chapter-10-basic-scenario](./chapter-10-basic-scenario/) | [study.md](./chapter-10-basic-scenario/study.md) |
| 11 | [chapter-11-network-slow-fix](./chapter-11-network-slow-fix/) | [study.md](./chapter-11-network-slow-fix/study.md) |
| 12 | [chapter-12-security-analysis](./chapter-12-security-analysis/) | [study.md](./chapter-12-security-analysis/study.md) 选读 |
| 13 | [chapter-13-wifi-packet](./chapter-13-wifi-packet/) | [study.md](./chapter-13-wifi-packet/study.md) 选读 |

**速查**：[display-filters.md](./display-filters.md) · 导航：[study.md](./study.md)

## 目录约定

```text
wireshark-packet-analysis/
├── README.md                 ← 你在这里
├── study.md                  ← 全书导航
├── display-filters.md        ← 过滤器速查
├── chapter-01-network-basics/
│   ├── README.md
│   └── study.md              ← 第 1 章笔记（正文写这里）
├── chapter-02-…/
│   └── study.md
└── …
```

- **PCAP**：可放在对应章文件夹或本根目录（[.gitignore](./.gitignore) 已忽略 `*.pcap`）。  
- **NotebookLM**：按章上传该章的 `study.md` 即可。
