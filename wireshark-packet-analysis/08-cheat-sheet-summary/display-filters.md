# Display Filters 速查（显示过滤器）

> [08 README](./README.md) · 官方：[Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)

| 场景 | 过滤器 |
|------|--------|
| 某 IP | `ip.addr == 192.168.1.1` |
| 某端口 | `tcp.port == 8080` |
| HTTP | `http` |
| DNS | `dns` |
| TCP 握手 | `tcp.flags.syn==1 && tcp.flags.ack==0` |
| 重传 | `tcp.analysis.retransmission` |
| ARP | `arp` |
| ICMP | `icmp` |

（待填：个人常用组合）
