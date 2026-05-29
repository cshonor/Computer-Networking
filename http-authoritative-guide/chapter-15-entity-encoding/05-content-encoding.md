# 15.5 内容编码

> 本章：[chapter-summary.md](./chapter-summary.md#ch15-5) · [15.6 传输编码](./06-transfer-chunked.md)

## 本节核心目标

区分 **内容编码**（压缩等）与传输编码；**Accept-Encoding** 协商。

---

<a id="ch15-5-process"></a>

## 15.5.1 过程

1. 生成原始响应（原始 Type/Length）  
2. 编码器压缩 → 设 **`Content-Encoding`**，保留 **`Content-Type`**，**更新 `Content-Length`** 为压缩后大小  
3. 客户端按 `Content-Encoding` **解压**

---

<a id="ch15-5-types"></a>

## 15.5.2 常用类型

| 值 | 说明 |
|----|------|
| **gzip** | 最常用 |
| **compress** / **deflate** | 其他压缩 |
| **identity** | 无编码（默认） |

---

<a id="ch15-5-accept"></a>

## 15.5.3 Accept-Encoding

```http
Accept-Encoding: gzip;q=1.0, identity;q=0.5
```

客户端声明可解码算法及 **q 优先级**。

---

## 抓包/实操记录

（待填：响应 `Content-Encoding: gzip`）

---

## 疑问与总结

**内容编码改 body 字节；Type 仍描述解压后的格式。**
