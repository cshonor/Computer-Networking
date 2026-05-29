# 19.2 WebDAV与协作写作

> 本章：[chapter-summary.md](./chapter-summary.md#ch19-2) · [ch03 方法](../chapter-03-http-message/03-method.md) · [ch03 207](../chapter-03-http-message/04-status-code.md)

## 本节核心目标

掌握 **WebDAV** 新方法、**XML**、**Depth/Lock** 与协作锁定。

---

<a id="ch19-2-methods"></a>

## 19.2.1 新方法

| 方法 | 作用 |
|------|------|
| **PROPFIND** | 读属性 |
| **PROPPATCH** | 写/删属性 |
| **MKCOL** | 建集合（目录） |
| **COPY** / **MOVE** | 复制/移动 |
| **LOCK** / **UNLOCK** | 锁/解锁 |

---

<a id="ch19-2-xml"></a>

## 19.2.2 XML 与 DAV 名字空间

复杂结构用 **XML** 承载；**`DAV:`** 名字空间防冲突。

---

<a id="ch19-2-headers"></a>

## 19.2.3 WebDAV 首部

| 首部 | 用途 |
|------|------|
| **`DAV`** | `OPTIONS` 响应，声明能力（如 `DAV: 1, 2`） |
| **`Depth`** | `0` / `1` / `infinity` — 操作层级 |
| **`Destination`** | COPY/MOVE 目标 URI |
| **`If`** | 条件（锁令牌等） |
| **`Lock-Token`** | UNLOCK 用 |
| **`Overwrite`** | `T`/`F` |
| **`Timeout`** | 锁超时请求 |

---

<a id="ch19-2-lock"></a>

## 19.2.4–19.2.5 LOCK 与丢失更新

两人同时改同一文件 → **覆盖**。  
`LOCK` + XML（`<locktype>`、`<lockscope>` 独占/共享、`<owner>`）→ 服务器返回 **opaquelocktoken**。

---

<a id="ch19-2-propfind"></a>

## 19.2.7–19.2.8 PROPFIND

| 属性类型 | 例子 |
|----------|------|
| **活属性** | 可改（作者等） |
| **死属性** | 固定（Content-Type） |

`PROPFIND` + `<allprop>` / `<propname>` → 常回 **`207 Multi-Status`**（每成员独立状态）。

---

<a id="ch19-2-proppatch"></a>

## 19.2.9 PROPPATCH

原子：**全成功或全失败**；`<set>` / `<remove>`。

---

<a id="ch19-2-collections"></a>

## 19.2.10–19.2.13 集合与名字空间

| 方法 | 要点 |
|------|------|
| **MKCOL** | 建目录；不用 PUT/POST 以免语义混 |
| **DELETE** | 集合默认 **Depth: infinity**；有锁 → **207** |
| **COPY/MOVE** | 受 **Overwrite**、**Depth** 约束；移入已锁集合会受新锁约束 |

---

<a id="ch19-2-enhanced"></a>

## 19.2.14 增强的传统方法

- **`PUT`**：写入常须 **`If`** 带锁令牌  
- **`OPTIONS`**：探能力 → `DAV:`、`Allow:`

---

<a id="ch19-2-versioning"></a>

## 19.2.15 版本管理

原版 WebDAV 无版本；**RFC 3253**（DeltaV）增加版本追踪。

---

## 拓展（预留）

- Nextcloud、Finder 挂载 WebDAV  
- vs **Git/SVN**  

---

## 抓包/实操记录

（待填：`curl -X OPTIONS -v` 看 DAV 头）

---

## 疑问与总结

**WebDAV = HTTP 扩展方法 + XML + 锁；207 是批量状态的核心。**
