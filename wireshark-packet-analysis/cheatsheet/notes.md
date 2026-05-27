# Wireshark 速查笔记

> 全书：[../README.md](../README.md) · 官方：[Display Filter Reference](https://www.wireshark.org/docs/dfref/)

## 显示过滤器（Display Filters）

| 场景 | 过滤器 |
|------|--------|
| 某 IP | `ip.addr == 192.168.1.1` |
| 某端口 | `tcp.port == 8080` |
| HTTP | `http` |
| DNS | `dns` |
| TCP 握手 | `tcp.flags.syn==1 && tcp.flags.ack==0` |
| 重传 | `tcp.analysis.retransmission` |
| 零窗口 | `tcp.analysis.zero_window` |
| ARP | `arp` |
| ICMP | `icmp` |

## 捕获过滤器（Capture / BPF）

| 场景 | 过滤器 |
|------|--------|
| 某主机 | `host 192.168.1.1` |
| 某端口 | `port 443` |
| 组合 | `host 10.0.0.1 and port 8080` |

## 排障口诀

（待填）

## 个人常用组合

（待填）
