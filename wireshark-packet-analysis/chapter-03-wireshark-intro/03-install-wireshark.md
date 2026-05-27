# 3.3 安装 Wireshark

> 本章：[chapter-summary.md](./chapter-summary.md) · 全书：[../README.md](../README.md)

**核心主旨**：Windows / Linux / macOS 安装流程及底层抓包驱动依赖。

## 核心知识点

### 3.3.1 微软 Windows

| 组件 | 作用 |
|------|------|
| **Npcap**（现行） | 取代已停止维护的 **WinPcap**；在用户态与网卡驱动间提供抓包 API |
| **WinPcap**（旧资料） | 教材/旧版安装程序仍写 WinPcap；**务必勾选**安装抓包驱动，否则无法抓本机实时流量 |
| **USBPcap**（可选） | 从 **USB 设备** 采集；一般以太网排障可不装 |

**易错细节**

- 安装向导中确认勾选 **Install Npcap**（或旧包中的 Install WinPcap）。
- 企业环境可能需管理员安装；Npcap 安装时可勾选「Restrict Npcap driver's access」按需限制。
- 安装后重启抓包服务或重开 Wireshark。

### 3.3.2 Linux

**包管理器（推荐）**

```bash
# Debian / Ubuntu
sudo apt update
sudo apt install wireshark

# RHEL / Fedora 等
sudo dnf install wireshark wireshark-cli
```

**权限**：默认仅 root 可抓包 → 将用户加入 `wireshark` 组并配置 `dumpcap` setcap，或使用 `sudo wireshark`（见发行版文档）。

**源码编译（了解）**

```bash
./configure    # 检查依赖、指定前缀等
make
sudo make install
sudo ldconfig  # 刷新动态库缓存
```

### 3.3.3 macOS

- 从 [wireshark.org](https://www.wireshark.org/download.html) 下载 **macOS 安装包**（或 Homebrew：`brew install --cask wireshark`）。
- 按向导接受许可并完成安装；首次抓包可能需在 **系统设置 → 隐私与安全性** 中允许驱动/扩展。

## 抓包/实操记录

| 检查项 | 通过标准 |
|--------|----------|
| 驱动 | `Capture` → `Interfaces` 中能看到网卡，非灰显 |
| 试抓 | 选接口 → Start → 产生浏览器流量 → 列表有包递增 |
| 版本 | `Help` → `About` 记录版本号，便于对照教材 |

## 疑问与总结

- **装得上 ≠ 抓得到**：无驱动、无权限、虚拟网卡限制都会导致 Interfaces 为空或 0 包。
- Windows 新装优先认 **Npcap**；与教材「WinPcap」为同一角色，名称不同。
