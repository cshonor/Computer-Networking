# 2.3 — email smtp pop3 imap

## 知识点速记

- **异步邮件**：UA ↔ 邮件服务器 ↔（SMTP 转发）↔ 对端；用户读信多为 **Pull**（POP3/IMAP/HTTP）。
- **SMTP**：命令驱动（`MAIL FROM`、`RCPT TO`、`DATA`）；基于 **TCP**。
- **MIME**：非 ASCII 与附件；`Content-Type`、`Content-Transfer-Encoding`。
- **POP3 / IMAP / HTTP**：简单下载 vs 服务器状态 vs Web 邮件主流。

## 与后端开发的联系

- 发信服务（验证码、通知邮件）需理解 **SMTP 认证、退信、SPF/DKIM/DMARC**（教材外常考工程点）。

## 延伸阅读

- 章级精读：[study.md § 2.3](../study.md#ch2-3)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `problem.md` | 错题与面试题 |
| `demo_code/` | 示例代码 |
