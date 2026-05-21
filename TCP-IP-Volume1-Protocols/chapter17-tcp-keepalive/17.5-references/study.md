# 17.5 参考文献

> 章级导读：[../study.md](../study.md)

## 建议优先查阅

| 文档 | 内容 |
|------|------|
| **RFC 1122** | 主机要求（Keepalive 为可选、争议点） |
| **RFC 9293** | 现代 TCP 标准 |

---

## 历史争议

- 额外带宽/CPU；短暂网络波动可能**误杀**正常空闲连接
- 故长期为**可选**而非强制

---

## Lab

- `ss -o`：`timer:(keepalive,...)`
- `sysctl -a | grep keepalive`
- Wireshark：`tcp.analysis.keep_alive`
