# 第2章 应用层

> 本章小节索引。每个子目录内均有 `README.md` / `study.md` / `demo_code/`。

应用层是自顶向下的起点：**HTTP、DNS、邮件、P2P、CDN、Socket** 直接决定用户体验与后端接口形态。完整精读笔记见 **[study.md](./study.md)**。

## 图（部分）

| 图 | 说明 |
|----|------|
| [email_system_architecture.png](./assets/email_system_architecture.png) | 2.3 邮件架构（UA/MTA、三步、考点） |
| [email_system_smtp_pop3.png](./assets/email_system_smtp_pop3.png) | 2.3 邮件系统简图 |
| [smtp_how_it_works.png](./assets/smtp_how_it_works.png) | 2.3 SMTP 原理 |
| [imap_how_it_works.png](./assets/imap_how_it_works.png) | 2.3 IMAP 多设备 |
| [pop3_how_it_works.png](./assets/pop3_how_it_works.png) | 2.3 POP3 下载删除 |

## 小节列表

- [2.1 应用层原理](./2.1_network_application_principle/study.md) — 定位、C/S vs P2P 对比表、四大需求、TCP/UDP 口诀、易错表  
- [2.2 HTTP 与 Web](./2.2_http_and_web/study.md) — 报文、[**HTTP/HTTPS TCP 载荷**](./2.2_http_and_web/study.md#ch2-http-tls-payload)、四层嵌套、Cookie  
- [2.3 电子邮件](./2.3_email_smtp_pop3_imap/study.md) — MUA/MTA、SMTP/POP3/IMAP 配图、MIME、考试速记  
- [2.4 DNS](./2.4_dns_service/study.md) — 层级、递归/迭代、RR  
- [2.5 P2P](./2.5_p2p_file_distribution/study.md) — BitTorrent、可扩展分发  
- [2.6 视频流媒体](./2.6_video_streaming/study.md) — DASH、CDN  
- [2.7 UDP Socket](./2.7_socket_programming_udp/study.md) — 无连接编程（[§2.7.2](./study.md#ch2-7-udp)）  
- [2.7 TCP Socket](./2.7_socket_programming_tcp/study.md) — 面向连接编程（[§2.7.3](./study.md#ch2-7-tcp)）  
