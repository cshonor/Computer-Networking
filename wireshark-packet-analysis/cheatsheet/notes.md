# Wireshark 速查笔记

> 全书：[../README.md](../README.md) · 官方：[Display Filter Reference](https://www.wireshark.org/docs/dfref/)

## 显示过滤器（Display Filters）

| 场景 | 过滤器 |
|------|--------|
| 某 IP | `ip.addr == 192.168.1.1` |
| 某端口 | `tcp.port == 8080` |
| HTTP | `http` |
| HTTP 302 | `http.response.code == 302` |
| DNS | `dns` |
| DNS 查询 | `dns.flags.response == 0` |
| DHCP | `bootp` 或 `dhcp` |
| DHCP Discover | `dhcp.option.dhcp == 1` |
| SMTP | `smtp` |
| TCP 握手 | `tcp.flags.syn==1 && tcp.flags.ack==0` |
| TCP 挥手 | `tcp.flags.fin==1` |
| TCP RST | `tcp.flags.reset==1` |
| 某 TCP 流 | `tcp.stream eq 0` |
| UDP / DNS | `udp.port == 53` 或 `dns` |
| 重传 | `tcp.analysis.retransmission` |
| 快速重传 | `tcp.analysis.fast_retransmission` |
| 重复 ACK | `tcp.analysis.duplicate_ack` |
| 零窗口 | `tcp.analysis.zero_window` |
| 窗口更新 | `tcp.analysis.window_update` |
| ARP | `arp` |
| 隐藏 ARP | `!arp` |
| ICMP | `icmp` |
| Ping 请求 | `icmp.type == 8` |
| TTL 超时 | `icmp.type == 11` |
| IPv6 | `ipv6` |
| NDP | `icmpv6.type == 135 or icmpv6.type == 136` |
| HTTP Cookie | `http.cookie` |
| HTTP POST | `http.request.method == "POST"` |
| 802.11 管理帧 | `wlan.fc.type == 0` |
| Beacon | `wlan.fc.type_subtype == 0x08` |
| 指定 AP | `wlan.bssid == aa:bb:cc:dd:ee:ff` |
| 信道 11 | `wlan_radio.channel == 11` |
| EAPOL / WPA | `eapol` |

## 捕获过滤器（Capture / BPF）

| 场景 | 过滤器 |
|------|--------|
| 某主机 | `host 192.168.1.1` |
| 某端口 | `port 443` |
| 组合 | `host 10.0.0.1 and port 8080` |
| 仅 TCP RST（BPF） | `tcp[13] & 4 != 0` 或 `tcp&4==4` |

## 命令行（TShark / tcpdump）

| 场景 | 命令 |
|------|------|
| 列网卡 | `tshark -D` |
| 抓包写盘 | `tshark -ni 1 -w out.pcapng -f "host x"` |
| 离线显示滤 | `tshark -r out.pcapng -Y "http" -n` |
| 绝对时间 | `tshark -r out.pcapng -t ad` |
| 协议分层 | `tshark -r out.pcapng -q -z io,phs` |
| Follow TCP 0 | `tshark -r out.pcapng -q -z follow,tcp,ascii,0` |
| tcpdump 抓 | `sudo tcpdump -nni eth0 -w out.pcap 'tcp port 443'` |

详见 [第6章](../chapter-06-tshark-tcpdump/chapter-summary.md)。

## 排障口诀

（待填）

## 个人常用组合

（待填）
