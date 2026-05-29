# 15.9 范围请求

> 本章：[chapter-summary.md](./chapter-summary.md#ch15-9) · [15.7 实例](./07-instances.md)

## 本节核心目标

用 **`Range` / `Content-Range`** 请求或返回**部分字节**。

---

<a id="ch15-9-mechanism"></a>

## 机制

**请求**：

```http
Range: bytes=20224-
Accept-Ranges: bytes   ← 服务器声明支持时用响应
```

**响应**：

```http
HTTP/1.1 206 Partial Content
Content-Range: bytes 20224-65536/65537
```

---

## 前提

客户端与服务器须针对**同一实例**（同一版本）；否则范围无意义。

---

## 抓包/实操记录

（待填：`curl -H "Range: bytes=0-99" -I`）

---

## 疑问与总结

**断点续传、视频拖动依赖 206 + Content-Range。**
