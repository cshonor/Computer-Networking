# 1.3 资源

> 本章：[chapter-summary.md](./chapter-summary.md#ch01-3) · [ch02 URL](../chapter-02-url-and-resource/chapter-summary.md)

## 本节核心目标

理解 **Web 资源**、**MIME 类型**、**URI / URL / URN** 的关系。

---

<a id="ch01-3-resource"></a>

## 一、资源（Web Resource）

**Web 服务器 = 资源的宿主**

| 类型 | 例子 |
|------|------|
| **静态** | HTML、图片、文件 |
| **动态** | 按请求生成的程序输出（CGI、API） |

---

<a id="ch01-3-mime"></a>

## 二、媒体类型（MIME）

HTTP 给每个对象打**格式标签** → **`Content-Type`** 首部常用

格式：**`type/subtype`**

| 例子 | MIME |
|------|------|
| HTML | `text/html` |
| 纯文本 | `text/plain` |
| JPEG | `image/jpeg` |

→ 实体首部详 [ch03 §3.5](../chapter-03-http-message/05-header.md)、[ch15](../chapter-15-entity-encoding/chapter-summary.md)

---

<a id="ch01-3-uri"></a>

## 三、URI、URL、URN

| 概念 | 说明 |
|------|------|
| **URI** | 统一资源**标识符**（大类） |
| **URL** | URI 最常见形式：**如何 + 去哪** 取资源 → [ch02](../chapter-02-url-and-resource/01-identifier.md) |
| **URN** | **持久名称**，不绑死位置 → [ch02 §2.6](../chapter-02-url-and-resource/06-urn-future.md) |

---

## 易错

口语里常混说 URI/URL；严格说 **URL ⊂ URI**，**URN** 仍少见。

---

## 拓展（预留）

- REST 里「资源」的抽象（名词 + HTTP 方法）

---

## 抓包/实操记录

（待填：响应头 `Content-Type`）

---

## 疑问与总结

**先有名（URI）再有事务**；MIME 告诉客户端怎么解析 body。
