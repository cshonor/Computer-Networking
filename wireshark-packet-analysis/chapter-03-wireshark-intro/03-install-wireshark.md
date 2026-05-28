# 3.3 安装 Wireshark

> 本章：[chapter-summary.md](./chapter-summary.md) · 全书：[../README.md](../README.md) · 逐步安装：[../cheatsheet/install-and-verify.md](../cheatsheet/install-and-verify.md)

**核心主旨**：Windows / Linux / macOS 安装流程；**Npcap** 为 Windows 抓包必备。

## 核心知识点

### 3.3.1 Windows（Win10/11 64 位）

| 步 | 操作 |
|----|------|
| 1 | [wireshark.org/download](https://www.wireshark.org/download.html) → **Windows x64 Installer** |
| 2 | 许可：同意 |
| 3 | **务必勾选 Npcap**（必选）；USBPcap 可选；其余默认 |
| 4 | Npcap 子安装一路默认 |
| 5 | 开始菜单打开 Wireshark |

| 组件 | 作用 |
|------|------|
| **Npcap** | 现行抓包驱动（教材旧称 WinPcap，角色相同） |
| **USBPcap** | USB 抓包，以太网排障可不装 |

**PATH（可选）**：将 `C:\Program Files\Wireshark` 加入环境变量 → 命令行可用 **tshark**。

---

### 3.3.2 Linux（Ubuntu / Debian）

```bash
sudo apt update
sudo apt install wireshark -y
sudo usermod -aG wireshark $USER   # 免每次 sudo
# 注销重新登录
```

RHEL/Fedora：`sudo dnf install wireshark wireshark-cli`

---

### 3.3.3 macOS

| 步 | 操作 |
|----|------|
| 1 | 官网下载 **.dmg** |
| 2 | 拖入 **Applications** |
| 3 | 若被拦截：**系统设置** → **隐私与安全性** → **仍要打开** |
| 4 | 允许安装 **tshark** 等命令行组件 |

`brew install --cask wireshark`

## 抓包/实操记录

完整验证步骤（含首次抓包命令）：[install-and-verify.md](../cheatsheet/install-and-verify.md)

| 检查项 | 通过标准 |
|--------|----------|
| 驱动 | `Capture` → `Interfaces` 网卡非灰 |
| 试抓 | Start → 上网 → 包列表递增 |
| 命令行 | `tshark -D` 有接口列表 |

## 疑问与总结

- **装得上 ≠ 抓得到**：无 Npcap、无权限、虚拟网卡限制 → Interfaces 空或 0 包。
- Windows 无原生 **tcpdump**，用 **tshark** 或 WSL（见第 6 章）。
