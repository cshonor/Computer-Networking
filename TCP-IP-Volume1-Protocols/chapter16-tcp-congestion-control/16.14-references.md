# 16.14 参考文献

> 章级导读：[../study.md](../study.md)

## 建议优先查阅

| RFC | 内容 |
|-----|------|
| **RFC 5681** | TCP 拥塞控制（Reno 族） |
| **RFC 3168** | ECN |
| **RFC 2018** | SACK |
| **RFC 6582** | NewReno |

---

## Lab

- `ss -ti`：`cwnd`、`ssthresh`
- `sysctl net.ipv4.tcp_congestion_control`
- `tc qdisc` + RED/ECN（进阶）
