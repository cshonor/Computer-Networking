# 2.3 — email smtp pop3 imap

## 知识点速记

- **架构图**：[MUA/MTA/MDA + SMTP/POP3 流程](../assets/email_system_smtp_pop3.png)
- **SMTP**：25/587/465，**推**，HELO→MAIL→RCPT→DATA→`.`→QUIT
- **POP3**：110/995，**拉**，常下载删服务器 → [对比图](../assets/pop3_how_it_works.png)
- **IMAP**：143/993，信留服务器、多设备同步 → [图](../assets/imap_how_it_works.png)
- **MIME**：扩展 SMTP，Base64/UTF-8，不替代 SMTP
- **背诵**：[study.md §七](./study.md#ch2-3-exam)

## 与后端开发的联系

- 发信服务（验证码、通知邮件）需理解 **SMTP 认证、退信、SPF/DKIM/DMARC**（教材外常考工程点）。

## 延伸阅读

- 章级精读：[study.md § 2.3](../study.md#ch2-3)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `demo_code/` | 示例代码 |
