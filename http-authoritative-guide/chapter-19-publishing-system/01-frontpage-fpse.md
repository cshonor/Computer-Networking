# 19.1 FrontPage为支持发布而做的服务器扩展

> 本章：[chapter-summary.md](./chapter-summary.md#ch19-1) · 全书：[../README.md](../README.md) · [ch05 CGI](../chapter-05-web-server/07-resource-mapping.md#ch05-7-dynamic)

## 本节核心目标

理解 **FPSE** 如何在 **HTTP POST 上叠 RPC** 做交互式发布（历史案例）。

---

<a id="ch19-1-fpse"></a>

## FrontPage 服务器扩展（FPSE）

- 装在 Web 服务器上的**扩展组件**（非 IIS 上常为 **CGI**）  
- 客户端 ↔ 网站之间的**发布枢纽**

---

<a id="ch19-1-rpc"></a>

## RPC 机制

不改变 HTTP 语义；在 **POST body** 里嵌 **RPC 方法/参数**（类似 CGI 编码：`+`、 `%XX`）。

流程：

1. **`GET`** 探 FPSE 脚本位置  
2. **`POST`** 执行 RPC 命令  

---

<a id="ch19-1-terms"></a>

## 术语

| 术语 | 说明 |
|------|------|
| **虚拟服务器** | 同机多站、独立域名/IP |
| **根 Web** | 默认顶层目录（每服务器一个） |
| **子 Web** | 根下独立子目录，独立权限 |

→ [ch18 虚拟主机](../chapter-18-web-hosting/02-virtual-hosting.md)

---

<a id="ch19-1-security"></a>

## 19.1.4 安全模型（易错）

| 角色 | 权限 |
|------|------|
| **管理员** | 完全控制 |
| **作者** | 编写、浏览 |
| **浏览者** | 浏览 |

依赖 OS/Web 服务器 ACL；历史版本漏洞多 → **谨慎启用 FPSE**。

---

## 拓展（预留）

- REST/GraphQL **CMS** vs 厚重客户端  
- 现代在线编辑器取代 FP  

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**发布协议 = HTTP 之上再套一层 RPC（FrontPage 路线）。**
