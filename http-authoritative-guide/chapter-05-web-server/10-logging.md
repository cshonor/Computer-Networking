# 5.10 第七步——记录日志

> 本章：[chapter-summary.md](./chapter-summary.md#ch05-10) · [ch21 日志](../chapter-21-log-tracking/chapter-summary.md)

## 本节核心目标

理解事务结束后的**日志闭环**及与后续章节的衔接。

---

<a id="ch05-10-log"></a>

## 一、记录什么

事务完成后向日志**追加一行**（或结构化 JSON），典型包含：

- 客户端 IP（主机名若开启反向 DNS）  
- 时间、方法、URI、协议版本  
- 状态码、响应字节数  
- Referer、User-Agent 等（可配置）

---

## 二、格式与用途

- **Common / Combined Log Format** 等  
- 用于排障、审计、流量分析  

详 → [第21章 日志与跟踪](../chapter-21-log-tracking/chapter-summary.md)

---

## 抓包/实操记录

（待填：对照 access.log 一条与 Wireshark 一次 GET）

---

## 疑问与总结

**第 7 步不阻塞用户**，但排障第一现场往往是日志。
