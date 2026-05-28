# 2.2 URL 的语法

> 本章：[chapter-summary.md](./chapter-summary.md#ch02-2) · [2.5 常见方案](#ch02-2-schemes) · [ch03 报文](../chapter-03-http-message/chapter-summary.md)

## 本节核心目标

掌握 URL **9 个组件**的通用格式；理解 scheme / host / path 等含义与易错点。

---

<a id="ch02-2-format"></a>

## 一、通用格式（9 部分）

```text
<scheme>://<user>:<password>@<host>:<port>/<path>;<params>?<query>#<frag>
```

**几乎必备三件套**：**方案（scheme）**、**主机（host）**、**路径（path）**。

---

<a id="ch02-2-scheme"></a>

## 二、方案（Scheme）——用什么协议

| 点 | 说明 |
|----|------|
| **定义** | 访问资源用的协议名：`http`、`https`、`ftp`… |
| **格式** | 字母开头，第一个 **`:`** 与后面分隔 |
| **易错** | **大小写无关**：`http://` = `HTTP://` |

---

## 三、主机与端口（Host & Port）

| 组件 | 说明 |
|------|------|
| **Host** | 资源所在机器：**主机名**（DNS 解析）或 **IP** |
| **Port** | 服务监听端口；**HTTP 省略时默认 80**，**HTTPS 默认 443** |

---

## 四、用户名与密码（User & Password）

格式：`<user>:<password>@`（在 host 之前）

| 场景 | 说明 |
|------|------|
| **FTP 等** | 可能需要凭证 |
| **只写用户名** | 可能发 `user:` + 默认密码（如 FTP 匿名） |
| **都省略** | 部分客户端自动填 `anonymous` |

**安全**：明文出现在 URL 中极不安全；HTTPS 也不加密 URL 路径（只加密连接内容时需知）。

---

## 五、路径（Path）

- 资源在服务器上的**逻辑/物理位置**  
- 常类似 UNIX：**`/`** 分隔路径段（path segment）

---

## 六、参数（Parameters）

- 用 **`;`** 分隔的**名/值**对，给应用额外输入（如 FTP 传输模式）  
- **每个路径段**可带自己的 `;params`

例：`http://host/items;type=text`（示意）

---

## 七、查询字符串（Query）

- **`?`** 开头，常为 **`key=value&key2=value2`**  
- 激活网关/搜索等，**缩小**请求范围  
- REST 常见：**Path 定位资源，Query 过滤**（拓展）

---

## 八、片段（Fragment）

- **`#`** 右侧，指向 HTML 文档内锚点、小节等  
- **重点**：**不发给服务器**；浏览器取回**完整资源**后**本地**滚动/定位

---

<a id="ch02-2-schemes"></a>

## 九、常见方案速览（原书 2.5）

| 方案 | 默认端口 | 要点 |
|------|----------|------|
| **http** | 80 | `http://host:port/path?query#frag` |
| **https** | 443 | HTTP + **TLS**；语法同 http → [ch14](../chapter-14-secure-http/chapter-summary.md) |
| **mailto** | — | 指向**邮箱**，非 HTTP 资源 |
| **ftp** | 21 | 上传/下载文件 |
| **rtsp / rtspu** | — | 实时流；`u` 表示用 **UDP** |
| **file** | — | 本地/网络文件；省略 host 常为 **localhost** |
| **news** | — | 新闻组；URL **无 host**，靠客户端配置的新闻服务器 |

**拓展**：移动端 `weixin://`、`alipay://` 等 **Deep Link / Custom URI Scheme**。

---

## 易错汇总

| 点 | 说明 |
|----|------|
| **#frag** | 服务器不见 fragment |
| **默认端口** | http **80**、https **443** |
| **; vs ?** | `;` 多为路径段参数（少见）；`?` 为查询（常见） |

---

## 拓展（预留）

- SPA 中 **Hash 路由**（`#/path`）与 fragment 的关系  
- `encodeURI` vs `encodeURIComponent` → 见 [2.4](./03-short-url-resolve.md)

---

## 抓包/实操记录

（待填：拆解浏览器里一条完整 URL 各段）

---

## 疑问与总结

先会**拆 URL**，再读 HTTP 请求行里的 **request-URL**。
