# Chapter 10 — Basic Troubleshooting Scenarios

> [README.md](./README.md) · [study.md](../study.md)

## 核心目标

不通、DNS 失败、连接被拒绝、RST — 用抓包**证实假设**。

## 场景清单（待填案例）

| 现象 | 先看什么包 | 常见结论 |
|------|------------|----------|
| ping 不通 | ICMP / ARP | 路由/ACL/未上线 |
| 域名打不开 | DNS 有无响应 | DNS 服务器/本机解析 |
| 连不上端口 | SYN 有无 SYN-ACK | 防火墙/服务未监听 |

## 笔记 / 总结

（待填）
