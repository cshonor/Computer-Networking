# 第2章 应用层

> 本章小节索引。每个子目录内均有 `README.md` / `study.md` / `demo_code/`。

应用层是自顶向下的起点：**HTTP、DNS、邮件、P2P、CDN、Socket** 直接决定用户体验与后端接口形态。完整精读笔记见 **[study.md](./study.md)**。

## 图（部分）

| 图 | 说明 |
|----|------|
| [http_message_structure_request_response.png](./assets/http_message_structure_request_response.png) | 2.2 HTTP 请求/响应结构框图 |
| [http_post_request_headers_body.png](./assets/http_post_request_headers_body.png) | 2.2 POST 请求首部分区 |
| [http_response_headers_body.png](./assets/http_response_headers_body.png) | 2.2 响应首部与 HTML 体 |
| [email_system_architecture.png](./assets/email_system_architecture.png) | 2.3 邮件架构（UA/MTA、三步、考点） |
| [email_system_smtp_pop3.png](./assets/email_system_smtp_pop3.png) | 2.3 邮件系统简图 |
| [smtp_how_it_works.png](./assets/smtp_how_it_works.png) | 2.3 SMTP 原理 |
| [imap_how_it_works.png](./assets/imap_how_it_works.png) | 2.3 IMAP 多设备 |
| [pop3_how_it_works.png](./assets/pop3_how_it_works.png) | 2.3 POP3 下载删除 |
| [mpeg_dash_architecture.png](./assets/mpeg_dash_architecture.png) | 2.6 MPEG-DASH 转码→CDN→播放器 |

## 小节列表

- [2.1 应用层原理](./2.1_network_application_principle/study.md) — C/S vs P2P、默认端口=TCP首部、TCP/UDP 选型  
- [2.2 HTTP 与 Web](./2.2_http_and_web/study.md) — 文本vs IP偏移、结构框图读图、四段报文、GET/POST、HTTPS载荷  
- [2.3 电子邮件](./2.3_email_smtp_pop3_imap/study.md) — SMTP/IMAP CLI逐条报文、POP3对比、MIME、邮件实体格式通用  
- [2.4 DNS](./2.4_dns_service/study.md) — 四层架构、递归/迭代、RR精编默写表、12步解析、五句口诀  
- [2.5 P2P](./2.5_p2p_file_distribution/study.md) — vs C/S、BitTorrent/Tracker、Rarest+Tit-for-Tat、30 字背诵  
- [2.6 视频流媒体](./2.6_video_streaming/study.md) — DASH精编、vs HLS对比表、CDN、TCP/UDP、30字背诵  
- [2.7 UDP Socket](./2.7_socket_programming_udp/study.md) — 无连接编程（[§2.7.2](./study.md#ch2-7-udp)）  
- [2.7 TCP Socket](./2.7_socket_programming_tcp/study.md) — 面向连接编程（[§2.7.3](./study.md#ch2-7-tcp)）  
- [2.8 WZP 私有协议](./2.8_wzp_private_protocol/study.md) — Len+Cmd+Body、KV分隔、TCP 9988、组包解包、30字背诵  
