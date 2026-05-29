# 15.3 实体摘要

> 本章：[chapter-summary.md](./chapter-summary.md#ch15-3)

## 本节核心目标

理解 **`Content-MD5`** 的计算时机与验证顺序。

---

<a id="ch15-3-md5"></a>

## Content-MD5

对实体主体做 **MD5**（在**内容编码之后、传输编码之前**）。

---

## 验证流程

1. 解除**传输编码**（如 chunked 解码）  
2. 对得到的 body 算 MD5  
3. 与 `Content-MD5` 比对  

代理**不得**擅自改 `Content-MD5`。

→ 现代少用；见 **RFC 3230** [15.11](./11-more-info.md)

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**先 TE 解码，再对「实体层」算 MD5。**
