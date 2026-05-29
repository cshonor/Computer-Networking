# 11.6 cookie

> 本章：[chapter-summary.md](./chapter-summary.md#ch11-6) · [ch07 缓存与 Cookie](../chapter-07-cache/chapter-summary.md)

## 本节核心目标

掌握 **Cookie** 类型、收发机制、作用域、v0/v1 语法及**缓存/隐私**规则。

---

<a id="ch11-6-types"></a>

## 11.6.1 类型

| 类型 | 寿命 | 存储 |
|------|------|------|
| **会话 Cookie** | 关浏览器即删 | 内存为主 |
| **持久 Cookie** | 有 **expires / Max-Age** | 硬盘 |

---

<a id="ch11-6-mechanism"></a>

## 11.6.2–11.6.3 机制与 Cookie 罐

```text
服务器 Set-Cookie（响应）→ 浏览器 cookie 罐 → 后续请求 Cookie（请求）
```

浏览器按站点维护本地存储，处理过期。

---

<a id="ch11-6-scope"></a>

## 11.6.4 作用域（Domain / Path）

| 属性 | 作用 |
|------|------|
| **`Domain`** | 如 `.amazon.com` — 子域共享 |
| **`Path`** | 如 `/autos/` — 路径前缀 |

**不会**把 Cookie 广播给所有站点。

---

<a id="ch11-6-v0"></a>

## 11.6.6 版本 0（Netscape）

```http
Set-Cookie: name=value [; expires=date] [; path=] [; domain=] [; secure]
```

| 易错 | 说明 |
|------|------|
| 无标准删除机制 | 靠过期覆盖 |
| **`expires`** | 依赖**客户端时钟** |

---

<a id="ch11-6-v1"></a>

## 11.6.7 版本 1（RFC 2965）

| 改进 | 说明 |
|------|------|
| **`Set-Cookie2` / `Cookie2`** | 新首部名 |
| **`Max-Age`** | 相对秒数，优于绝对日期 |
| **`Port`** | 限制端口 |
| **`Discard`** | 强制会话级 |
| **`Comment`** | 用途说明 |
| **`$Version="1"`** | 请求 Cookie 时版本协商 |

**现实**：广泛部署的是 **RFC 6265**（Cookie 现代标准），语法以 v0 为主并扩展属性。

---

<a id="ch11-6-cache"></a>

## 11.6.9 与缓存（易错）

| 规则 | 说明 |
|------|------|
| **绝不可** | 把含**用户私人 Cookie**的响应缓存给别人 → **越权** |
| 含 `Set-Cookie` 的响应 | 应 `Cache-Control: no-cache="Set-Cookie"` 等 |
| 带 `Cookie` 的请求 | 保守代理**不缓存**响应 |

→ [ch07 §7.9](../chapter-07-cache/09-cache-control.md)

---

<a id="ch11-6-privacy"></a>

## 11.6.10 隐私

- Cookie **不执行代码**，但可跨站追踪（如 **1×1 第三方像素**）  
- 营销公司可拼**浏览档案** → **GDPR**、第三方 Cookie 封杀  

---

## 拓展（预留）

- **`HttpOnly`**、**`Secure`**、**`SameSite`** — 防 XSS/CSRF  
- **Local Storage** vs Cookie  

---

## 抓包/实操记录

（待填：Application → Cookies；响应 `Set-Cookie`）

---

## 疑问与总结

**Cookie = 服务器贴在客户端的状态标签；作用域与缓存规则同样重要。**
