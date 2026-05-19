# 2.2 — http and web

## 知识点速记

- **HTTP 演进**：非持续连接 RTT 开销大；**HTTP/1.1 持续连接**；流水线受 **HOL** 限制。
- **报文**：请求行/首部 + 响应状态行/首部；[HTTP 明文 vs HTTPS 密文](./study.md#ch2-http-tls-payload)（TCP 载荷）
- **Cookie**：无状态 HTTP 上叠会话；`Set-Cookie` / `Cookie` + 存储。
- **缓存**：代理 + **条件 GET**（304）；`ETag`、`Cache-Control`。
- **HTTP/2**：二进制分帧、多路复用；**HTTP/3 + QUIC**：UDP 之上，缓解 TCP 侧 HOL 等问题。

## 与后端开发的联系

- 接口性能：**RTT、连接复用、TLS 握手、Body 大小、缓存头** 共同决定；与 CDN/网关配置强相关。

## 延伸阅读

- 章级精读：[study.md § 2.2](../study.md#ch2-2)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `demo_code/` | 示例代码 |
