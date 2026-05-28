# 5.7 第四步——对资源的映射及访问

> 本章：[chapter-summary.md](./chapter-summary.md#ch05-7) · [ch02 URL](../chapter-02-url-and-resource/chapter-summary.md) · [ch18 托管](../chapter-18-web-hosting/chapter-summary.md)

## 本节核心目标

把 **URI 映射**到磁盘文件、动态程序或用户目录，并理解**安全与虚拟主机**。

---

<a id="ch05-7-docroot"></a>

## 一、docroot（文档根）

**URI 路径 → `DocumentRoot` + 路径**

| 要点 | 说明 |
|------|------|
| Apache | `DocumentRoot` |
| **路径穿越** | 必须过滤 `../`，禁止逃出 docroot |
| **虚拟主机** | 按 **`Host`** 或 IP 选不同 docroot（`<VirtualHost>`）→ [ch18](../chapter-18-web-hosting/02-domain-virtual-host.md) |
| **用户目录** | `/~user/...` → `public_html` 等 |

---

<a id="ch05-7-dirindex"></a>

## 二、目录列表（易错）

请求指向**目录**时：

1. 找默认索引（`index.html`，`DirectoryIndex`）  
2. 若无索引且**未禁用**目录浏览（`Options -Indexes`）→ 自动生成 **HTML 文件列表** → **信息泄露**

---

<a id="ch05-7-dynamic"></a>

## 三、动态内容

| 机制 | 说明 |
|------|------|
| **CGI** | URI → 可执行程序，**运行**后输出作响应体 |
| Apache | `ScriptAlias`、`AddHandler` |
| **SSI** | 发前替换 HTML 注释中的变量/包含 |

现代栈常用 **FastCGI / 反向代理到应用**（Node、PHP-FPM）→ [ch08 网关](../chapter-08-gateway-tunnel-relay/01-gateway.md)

---

<a id="ch05-7-access"></a>

## 四、访问控制

- 按 **客户端 IP**  
- 要求 **密码**（Basic 等 → [ch12](../chapter-12-basic-auth/chapter-summary.md)）  

在本阶段决定是否允许进入 docroot。

---

## 抓包/实操记录

（待填：访问目录无 index 时是否 403/列表）

---

## 疑问与总结

**第 4 步 = 安全边界**；`../` 与目录索引是常见漏洞面。
