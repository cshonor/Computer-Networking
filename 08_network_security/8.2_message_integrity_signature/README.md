# 8.2 — message integrity signature

## 知识点速记

- **Hash**：SHA-256+；禁 MD5/SHA-1 作安全依赖。  
- **HMAC**：标准 MAC；禁自造 `Hash(Key‖Msg)`。  
- **数字签名 + CA**：解决公钥归属与不可否认（结合流程与法律语境）。

## 与后端开发的联系

- JWT `none`、弱 HMAC secret、证书链校验被跳过等常见线上事故。

## 延伸阅读

- [§8.3 完整性与签名](../study.md#ch8-3) · [§8.4 端点鉴别](../study.md#ch8-4)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 个人小节笔记 |
| `problem.md` | 错题与面试题 |
| `demo_code/` | 示例代码 |
