# 5.6 第三步——处理请求

> 本章：[chapter-summary.md](./chapter-summary.md#ch05-6) · [ch03 方法](../chapter-03-http-message/03-method.md)

## 本节核心目标

服务器按**方法语义**路由请求，遵守 HTTP 规则。

---

<a id="ch05-6-semantics"></a>

## 方法语义（必背）

| 方法 | 实体主体 |
|------|----------|
| **GET** | **禁止**请求 body（有 body 的 GET 不符合语义） |
| **POST** | **必须有** body（提交数据） |
| **OPTIONS** | 不硬性要求 body |
| **HEAD** | 同 GET 但无响应 body |

处理阶段决定：鉴权、重定向、转发到应用服务器等 → [5.7](./07-resource-mapping.md)

---

## 抓包/实操记录

（待填：`curl -X OPTIONS -v`）

---

## 疑问与总结

**第 3 步 = 策略与路由**；别在 GET 里塞表单 body。
