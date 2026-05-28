# 1.4 事务

> 本章：[chapter-summary.md](./chapter-summary.md#ch01-4) · [ch03 方法/状态码](../chapter-03-http-message/chapter-summary.md)

## 本节核心目标

掌握 **HTTP 事务** = 请求 + 响应；了解常见**方法、状态码**与**一页多对象**。

---

<a id="ch01-4-tx"></a>

## 一、事务组成

| 部分 | 方向 | 内容 |
|------|------|------|
| **请求报文** | 客户端 → 服务器 | 要什么、怎么要 |
| **响应报文** | 服务器 → 客户端 | 结果、资源或错误 |

---

<a id="ch01-4-methods"></a>

## 二、方法（Methods）

请求里的**命令**，告诉服务器执行什么动作：

| 方法 | 作用 |
|------|------|
| **GET** | 获取资源 |
| **PUT** | 存储/替换资源 |
| **DELETE** | 删除 |
| **POST** | 提交数据 |
| **HEAD** | 只要首部，不要 body |

→ [ch03 §3.3](../chapter-03-http-message/03-method.md)

---

<a id="ch01-4-status"></a>

## 三、状态码（Status Codes）

响应里**三位数字** + 人类可读的 **原因短语（Reason Phrase）**

| 点 | 说明 |
|----|------|
| **程序** | 主要看**数字码** |
| **人** | 原因短语便于调试 |

→ [ch03 §3.4](../chapter-03-http-message/04-status-code.md)

---

<a id="ch01-4-multi"></a>

## 四、一页多个对象

一个 Web 页常是**多资源集合**：HTML + CSS + 图片 + 脚本…

- 浏览器往往发**多条 HTTP 事务**（甚至多台服务器）  
- 优化：**持久连接、HTTP/2 多路复用** → [ch04](../chapter-04-connection-management/chapter-summary.md)、[ch10](../chapter-10-http-ng/chapter-summary.md)

---

## 抓包/实操记录

（待填：打开一页数 DevTools Network 里请求条数）

---

## 疑问与总结

**事务 ≠ TCP 连接**；一条连接上可跑多个事务（持久连接时）。
