# 2.6 — video streaming

## 知识点速记

- **DASH**：HTTP 拉取分片 + **Manifest** 驱动码率自适应。
- **CDN**：**Enter Deep**（深边缘）vs **Bring Home**（IXP 大 PoP）；时延与运维权衡。
- **GSLB**：DNS 层或 HTTP 层调度，把用户导向较优边缘节点。

## 与后端开发的联系

- 视频/大静态资源：**缓存键、Range 请求、签名 URL、多 CDN 容灾** 是常见后端课题。

## 延伸阅读

- 章级精读：[study.md § 2.6](../study.md#ch2-6)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `problem.md` | 错题与面试题 |
| `demo_code/` | 示例代码 |
