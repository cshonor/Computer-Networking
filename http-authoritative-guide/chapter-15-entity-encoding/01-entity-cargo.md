# 15.1 报文是箱子，实体是货物

> 本章：[chapter-summary.md](./chapter-summary.md#ch15-1) · [ch03 §3.6 实体](../chapter-03-http-message/06-entity.md) · [ch03 报文结构](../chapter-03-http-message/02-message-component.md)

## 本节核心目标

区分 **HTTP 报文**与 **实体**：首部 + 空行 + **实体**（实体首部 + 实体主体）。

---

<a id="ch15-1-structure"></a>

## 基本结构

```text
… 报文首部 …
CRLF
实体首部（可选）
CRLF
实体主体（可选字节流）
```

---

<a id="ch15-1-entity-headers"></a>

## 实体首部（常见）

| 首部 | 作用 |
|------|------|
| `Content-Type` | MIME 类型 |
| `Content-Length` | 主体字节数 |
| `Content-Language` | 语言 |
| `Content-Encoding` | **内容**编码（如 gzip） |
| `Content-Location` | 备用 URL |
| `Content-Range` | 字节范围 |
| `Content-MD5` | 主体校验和 |
| `Last-Modified` / `Expires` | 时间 |
| `Allow` | 允许的方法 |

**常一起用**：`ETag`、`Cache-Control`（虽非正式“实体首部”）→ [15.8](./08-validators-freshness.md)、[ch07](../chapter-07-cache/chapter-summary.md)

---

<a id="ch15-1-body"></a>

## 实体主体

原始或**经内容编码后**的字节（如 gzip 压缩后的数据在 body 里）。

---

## 拓展（预留）

- HTTP/2 **DATA 帧**拆分 body  

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**箱子 = 整条报文；货物 = 实体（描述 + body）。**
