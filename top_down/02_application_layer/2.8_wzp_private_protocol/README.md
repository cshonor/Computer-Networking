# 2.8 — WZP 私有应用层协议

## 知识点速记

- **WanZhi Protocol** · TCP **9988** · 轻量 IM
- **帧**：`4B Len(BE) + 1B Cmd + Body`（Len = Cmd+Body，防粘包）
- **KV**：`key=value|...`（≠ HTTP `:`）
- **指令**：0x01 登录 · 0x02 ACK · 0x03 聊天 · 0x04 状态 · 0x05 文件 · 0x06 下线
- **背诵**：[5 行](./study.md#ch2-8-exam) · 代码：[wzp_codec.py](./demo_code/wzp_codec.py)

## 与后端开发的联系

- 自定义 RPC、游戏协议、物联网二进制帧；Length-prefix + 命令字是通用模式

## 延伸阅读

- [study.md](./study.md) · [2.2 HTTP 对比](../2.2_http_and_web/study.md) · [2.7 TCP Socket](../2.7_socket_programming_tcp/study.md)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记 |
| `study.md` | 可背诵完整版 |
| `demo_code/wzp_codec.py` | 组包/解包示例 |
