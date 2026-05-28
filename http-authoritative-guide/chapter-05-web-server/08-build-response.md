# 5.8 第五步——构建响应

> 本章：[chapter-summary.md](./chapter-summary.md#ch05-8) · [ch03 状态码](../chapter-03-http-message/04-status-code.md) · [ch01 MIME](../chapter-01-http-overview/03-resource.md#ch01-3-mime)

## 本节核心目标

组织 **状态码、首部、实体**；掌握 **MIME 判定** 与 **3xx 重定向**。

---

<a id="ch05-8-entity"></a>

## 一、响应实体

有 body 时通常需要：

- **`Content-Type`**（MIME）  
- **`Content-Length`**（或 chunked）  
- **报文主体**

---

<a id="ch05-8-mime"></a>

## 二、MIME 类型判定

| 方式 | 说明 |
|------|------|
| **扩展名表** | `mime.types`，最常见 |
| **魔法字节** | 读文件头匹配 magic |
| **显式配置** | 强制某目录一种类型 |
| **内容协商** | 多格式副本，按 `Accept` 选最佳 → [ch17](../chapter-17-content-negotiation-transcode/chapter-summary.md) |

---

<a id="ch05-8-redirect"></a>

## 三、重定向（3xx）

| 场景 | 常见码 |
|------|--------|
| 永久搬家 | **301** |
| 临时搬家 | **302/303/307**（语义略异，见 ch03） |
| URL 增强（胖 URL） | 3xx |
| 负载均衡 / 会话粘滞 | 3xx 到特定机器 |
| 目录缺尾部 `/` | 补 `/ 后重定向 |

→ [ch20 重定向](../chapter-20-redirect-load-balance/chapter-summary.md)

---

## 抓包/实操记录

（待填：`file` 命令 vs 响应 `Content-Type`）

---

## 疑问与总结

**第 5 步决定客户端怎么解析 body**；错 MIME 比错状态码更隐蔽。
