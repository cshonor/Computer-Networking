# 2.4 — dns service

## 知识点速记

- **作用**：域名 ↔ IP（+ MX/CNAME/NS）
- **四层**：根(13组) → TLD → 权威 → 本地递归
- **查询**：客户端**递归**；本地→上级**迭代**
- **缓存**：浏览器/OS/本地 DNS，**TTL**
- **RR**：[精编+默写表](./study.md#ch2-4-rr)（A/AAAA/CNAME/MX/NS/PTR/SOA、五句口诀）
- **背诵**：[12 步流程](./study.md#ch2-4-flow) · [易错](./study.md#ch2-4-exam)

## 与后端开发的联系

- 排障：TTL、权威变更、解析链路、证书与域名一致性

## 延伸阅读

- 章级：[§2.4](../study.md#ch2-4) · 解析后：[2.2 HTTP](../2.2_http_and_web/study.md)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记 |
| `study.md` | 可背诵完整版 + 12 步流程 |
| `demo_code/` | 示例代码 |
