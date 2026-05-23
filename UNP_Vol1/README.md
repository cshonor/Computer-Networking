# UNP Vol1 — UNIX Network Programming 卷 1 学习目录

> 基于 **UNIX Network Programming, Volume 1, 3rd Edition**（Stevens / Fenner / Rudoff）  
> 四层结构：**阶段 → 章节 → 小节 → notes + code**

## 目录层级

```
UNP_Vol1/
├─ 1_BasicFoundation/          # 入门筑基期（Ch 1–8）
├─ 2_AdvancedSkill/              # 能力进阶期（Ch 11,13,14,16,26）
├─ 3_DeepMaster/                 # 深度精通期（Ch 17,20–22,24,25,28,29）
└─ 4_ArchitectureDesign/         # 架构拔高期（Ch 9–10,12,15,18–19,23,27,30–31）
```

## 命名规则

| 层级 | 格式 | 示例 |
|------|------|------|
| 一级 | `UNP_Vol1` | 根目录 |
| 二级 | `{序号}_{阶段英文名}` | `1_BasicFoundation` |
| 三级 | `Chapter{NN}_{章节英文名}` | `Chapter04_BasicTCPSocket` |
| 四级 | `{小节号}_{小节英文名}` | `4.3_Connect_Function` |

## 单小节固定结构

```
xx小节/
├─ notes.md              # 读书笔记（见下方模板）
└─ code/
   ├─ original_c/        # 书本原版 C 示例
   ├─ rewrite_go/        # Go 改写
   └─ rewrite_rust/      # Rust 改写
```

## notes.md 模板

```markdown
# 本节标题
## 核心知识点
## 关键函数与结构体
## 执行流程原理
## 易错点与坑点
## 个人学习总结
```

## 阶段与章节对照

| 阶段 | 章节 |
|------|------|
| **1_BasicFoundation** | 1 Introduction · 2 TCP/UDP/SCTP · 3 Socket Intro · 4 TCP Socket · 5 TCP Demo · 6 select/poll · 7 Socket Options · 8 UDP |
| **2_AdvancedSkill** | 11 Name/Address · 13 Daemon/inetd · 14 Advanced I/O · 16 Nonblocking I/O · 26 Threads |
| **3_DeepMaster** | 17 ioctl · 20 Broadcast · 21 Multicast · 22 Advanced UDP · 24 OOB · 25 Signal-Driven I/O · 28 Raw · 29 Datalink |
| **4_ArchitectureDesign** | 9–10 SCTP · 12 IPv4/6 · 15 Unix Domain · 18 Routing · 19 Key Mgmt · 23 Adv SCTP · 27 IP Options · 30 Design · 31 Streams |

## 维护

- 全书 **320** 个小节目录（Ch 1–31，不含 Exercises）
- 全部小节英文名以 `scripts/generate_structure.py` 内 `SECTIONS` 字典为准（四阶段全覆盖）
- 重新同步目录：`python scripts/generate_structure.py`（**不覆盖**已有 `notes.md`；自动迁移旧文件夹名并更新 `OUTLINE.md`）

→ 完整树形索引：[OUTLINE.md](./OUTLINE.md)
