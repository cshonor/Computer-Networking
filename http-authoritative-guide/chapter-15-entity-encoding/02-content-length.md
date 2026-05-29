# 15.2 Content-Length：实体的大小

> 本章：[chapter-summary.md](./chapter-summary.md#ch15-2) · [ch04 截尾/持久连接](../chapter-04-connection-management/07-close-connection.md)

## 本节核心目标

掌握 **`Content-Length`** 含义、持久连接边界及**定长五条规则**。

---

<a id="ch15-2-meaning"></a>

## 重点

| 点 | 说明 |
|----|------|
| **计什么** | **内容编码之后**的最终字节数（如 gzip 后的大小） |
| **缺失** | 难判截尾；缓存代理常**拒缓存**无长度的 body |
| **错误长度** | 比缺失更糟；HTTP/1.1 客户端应报错 |
| **持久连接** | 靠 `Content-Length` 或 **chunked** 划界 → [15.6](./06-transfer-chunked.md) |

---

<a id="ch15-2-rules"></a>

## 15.2.5 确定主体长度的五条规则（优先级）

1. **无 body 的报文**：`HEAD`、**1xx**、**204**、**304** — 见空行即结束，忽略 `Content-Length`  
2. 有 **`Transfer-Encoding`**（非 identity）→ 以 **0 长度块**结束  
3. 有效 **`Content-Length`**（且无上述 TE）→ 用该值；**若与 TE 冲突，忽略 Content-Length**  
4. **`multipart/byteranges`** → 边界字符串  
5. **连接关闭**（仅**响应**可由服务器用关闭表示结束；客户端请求不能靠关连接表结束）

---

## 拓展（预留）

- **HTTP 请求走私**：CL 与 TE 解析不一致  

---

## 抓包/实操记录

（待填：chunked 时是否还有 Content-Length）

---

## 疑问与总结

**有 chunked 时别看错 Content-Length。**
