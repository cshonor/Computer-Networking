# 6.2 安装 Tcpdump

> 本章：[chapter-summary.md](./chapter-summary.md) · 全书：[../README.md](../README.md)

**核心主旨**：UNIX/Linux 原生命令行嗅探器——轻量抓包探针。

## 核心知识点

| 项 | 说明 |
|----|------|
| **Tcpdump** | 最流行的 **原生** CLI 抓包工具；主要面向 **UNIX/Linux**（Windows 非官方主力） |
| **安装** | 包管理器；多数服务器发行版**预装** |

```bash
# Debian / Ubuntu
sudo apt install tcpdump

# RHEL / Fedora
sudo dnf install tcpdump
```

### 权限（易错）

| 要求 | 说明 |
|------|------|
| **Root / sudo** | 直接操作网卡；普通用户失败时**先查权限** |

```bash
sudo tcpdump -h
man tcpdump
```

## 抓包/实操记录

| 检查 | 命令 |
|------|------|
| 版本 | `tcpdump --version` |
| 网卡 | `ip link` 或 `tcpdump -D`（视版本） |

## 疑问与总结

- Tcpdump **解析深度**有限（约 L3/L4）；深度分析用 TShark 或 GUI 打开同一 pcap（见 [§6.9](./09-tshark-vs-tcpdump.md)）。
- 生产机常用：**tcpdump 抓** → 下载 → **Wireshark 看**。
