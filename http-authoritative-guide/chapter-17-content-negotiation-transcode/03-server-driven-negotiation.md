# 17.3 服务器驱动的协商

> 本章：[chapter-summary.md](./chapter-summary.md#ch17-3) · [ch16 Accept](../chapter-16-internationalization/01-intl-content-support.md)

## 本节核心目标

掌握 **Accept 族首部**、**q 值**、非 Accept 匹配及 Apache 实现。

---

<a id="ch17-3-accept"></a>

## 17.3.1 内容协商首部集（易错）

| 客户端请求 | 服务器响应实体 |
|------------|----------------|
| **`Accept`** | `Content-Type` |
| **`Accept-Language`** | `Content-Language` |
| **`Accept-Charset`** | `Content-Type; charset=` |
| **`Accept-Encoding`** | `Content-Encoding` |

**协商首部 = 采购意向**；**实体首部 = 货物标签**（ch15）。  
HTTP **无状态** → **每次请求**都要带 Accept 族。

---

<a id="ch17-3-q"></a>

## 17.3.2 质量值 q

`q` 范围 **0.0～1.0**（默认 1.0）。

```http
Accept-Language: en;q=0.5, fr;q=0.0, nl;q=1.0
```

首选荷兰语，英语备选，**拒绝**法语。

---

<a id="ch17-3-other"></a>

## 17.3.3 其他首部

如 **`User-Agent`** → 给旧浏览器无 JS 页面；通常**无 q**，硬编码规则。

---

<a id="ch17-3-apache"></a>

## 17.3.4 Apache

| 机制 | 说明 |
|------|------|
| **type-map** | 显式列出变体与协商首部 |
| **MultiViews** | 扫描 `*.en`、`*.fr` 等自动推断 |

---

## 拓展（预留）

- Nginx `map $http_accept_language`  

---

## 抓包/实操记录

（待填：请求 Accept-Language 与响应 Content-Language）

---

## 疑问与总结

**最常见模式：一次请求，服务器算最佳变体。**
