# 17.1 内容协商技术

> 本章：[chapter-summary.md](./chapter-summary.md#ch17-1) · 全书：[../README.md](../README.md) · [ch16 国际化](../chapter-16-internationalization/chapter-summary.md)

## 本节核心目标

理解 **变体（variant）** 与三种**内容协商**方式。

---

<a id="ch17-1-variant"></a>

## 变体

同一 **URL** 可对应多份资源（中/英版、不同 MIME 等）→ 需选**最适合客户端**的版本。

---

<a id="ch17-1-three"></a>

## 三大协商技术

| 方式 | 谁选 | 节 |
|------|------|-----|
| **客户端驱动** | 服务器列选项，**客户端**选 | [17.2](./02-client-driven-negotiation.md) |
| **服务器驱动** | 服务器读 **Accept\*** 首部自动选 | [17.3](./03-server-driven-negotiation.md) |
| **透明协商** | **代理缓存**代客户端协商 | [17.4](./04-transparent-negotiation.md) |

---

## 拓展（预留）

- API 网关 i18n 路由 vs HTTP 协商  

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**协商 = 同一 URI 多副本里挑一个返回。**
