# 15.6 传输编码和分块编码

> 本章：[chapter-summary.md](./chapter-summary.md#ch15-6) · [15.2 定长规则](./02-content-length.md#ch15-2-rules)

## 本节核心目标

掌握 **`Transfer-Encoding`**、**chunked**、拖挂（Trailer）及与内容编码的组合。

---

<a id="ch15-6-why"></a>

## 15.6.1 为何需要

动态生成内容时**事先不知总长** → 无法发 `Content-Length` → 用**传输编码**改「怎么传」。

---

<a id="ch15-6-headers"></a>

## 15.6.2 首部

| 首部 | 方向 | 作用 |
|------|------|------|
| **`Transfer-Encoding`** | 响应（常见） | 用了何种传输编码 |
| **`TE`** | 请求 | 客户端支持的 TE 扩展 |

---

<a id="ch15-6-chunked"></a>

## 15.6.3 分块编码（Chunked）

```text
<十六进制长度> CRLF
<数据> CRLF
…
0 CRLF          ← 结束
[Trailer 首部…]
CRLF
```

- **0 块** = 主体结束 → 兼容**持久连接**  
- **`Trailer`**：预告拖挂首部（如事后才算的 `Content-MD5`）

---

<a id="ch15-6-rules"></a>

## 15.6.4–15.6.5 组合与规则

- 可先 **gzip（内容）** 再 **chunked（传输）**  
- **chunked 必须是最后一个** TE，且**不能重复应用**  
- 除关连接外，TE 集合**必须含 chunked**（若用 TE）

---

## 拓展（预留）

- **HTTP/2** 无 chunked，用帧流式传  

---

## 抓包/实操记录

（待填：Wireshark chunked 重组）

---

## 疑问与总结

**Content-Encoding = 货物怎么压；Transfer-Encoding = 箱子怎么运。**
