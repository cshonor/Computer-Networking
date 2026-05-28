# 7.10 设置缓存控制

> 本章：[chapter-summary.md](./chapter-summary.md#ch07-10) · [7.9 指令](./09-cache-control.md)

## 本节核心目标

会在**服务器端**正确下发缓存首部；知道 **META HTTP-EQUIV** 的陷阱。

---

<a id="ch07-10-apache"></a>

## 7.10.1 Apache 模块（示例）

| 模块 | 用途 |
|------|------|
| **`mod_headers`** | `Header set Cache-Control no-cache` 等 |
| **`mod_expires`** | `ExpiresDefault "access plus 1 month"` |
| **`mod_cern_meta`** | 元文件关联首部 |

---

<a id="ch07-10-meta"></a>

## 7.10.2 HTTP-EQUIV（易错）

```html
<META HTTP-EQUIV="Cache-control" CONTENT="no-cache">
```

| 设想 | 现实 |
|------|------|
| 服务器解析 META 插入响应首部 | **极少**服务器/代理支持；负载高 |

→ 浏览器与代理规则**脱节**；**强烈不推荐**，应在**响应 HTTP 首部**配置。

---

## 抓包/实操记录

（待填：看响应头是否含 META 期望的 Cache-Control）

---

## 疑问与总结

**缓存听的是 HTTP 响应头，不是 HTML 里的 META。**
