# 9.4 拒绝机器人访问

> 本章：[chapter-summary.md](./chapter-summary.md#ch09-4) · [ch07 缓存 META 陷阱](../chapter-07-cache/10-configure-cache.md#ch07-10-meta)

## 本节核心目标

掌握 **robots.txt**、**HTML meta robots** 的格式、匹配规则与缓存注意点。

---

<a id="ch09-4-fetch"></a>

## 9.4.1–9.4.2 获取 robots.txt

爬行某**主机:端口**前应先：

```http
GET /robots.txt HTTP/1.1
Host: example.com
```

- 按**主机名 + 端口**；每个虚拟 docroot **独立** `robots.txt`  

---

<a id="ch09-4-format"></a>

## 9.4.3 格式与规则

纯文本，记录以空行分隔：

| 指令 | 含义 |
|------|------|
| **`User-Agent: name`** | 适用机器人名**子串**（不区分大小写），`*` = 全部 |
| **`Disallow: path`** | 禁止的 **URL 前缀** |
| **`Allow: path`** | 显式允许的前缀 |

**匹配**：路径**大小写敏感**的前缀；`Disallow:` 空 = 全禁。  
除 `/` 外需**反转义**再比较。`#` 起为注释。

---

<a id="ch09-4-cache"></a>

## 9.4.4–9.4.5 易错：缓存 robots.txt

机器人常**缓存** `robots.txt`。  
无明确 `Cache-Control` 时默认缓存过久（如 7 天）→ 站长紧急改规则**不生效**。

---

<a id="ch09-4-meta"></a>

## 9.4.7 HTML robot-control

```html
<meta name="robots" content="noindex,nofollow">
```

| 指令 | 含义 |
|------|------|
| **NOINDEX** | 不索引本页 |
| **NOFOLLOW** | 不跟本页链接 |
| **NOARCHIVE** | 不存快照 |
| **ALL / NONE** | 组合语义 |

无法写根目录 `robots.txt` 时的补充。

---

## 拓展（预留）

- **`sitemap.xml`** 与 robots 配合引导收录  

---

## 抓包/实操记录

（待填：`curl https://example.com/robots.txt`）

---

## 疑问与总结

**robots = 自愿契约**；不守规矩的爬虫仍可能被技术手段封。
