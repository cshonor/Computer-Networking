# 2.3 URL 快捷方式（一）相对 URL

> 本章：[chapter-summary.md](./chapter-summary.md#ch02-3) · [（二）自动扩展](./05-url-shortcut.md) · [2.2 绝对 URL](./02-url-syntax.md)

## 本节核心目标

理解**相对 URL**、**基础 URL（Base URL）** 及合并为绝对 URL 的规则。

---

<a id="ch02-3-relative"></a>

## 一、相对 URL 是什么？

| 点 | 说明 |
|----|------|
| **定义** | **不完整**的 URL 缩略形式 |
| **解析** | 必须相对某个 **基础 URL（Base URL）** 合并成**绝对 URL** |

**好处**：整站搬迁时，站内链接仍有效（可移植性）。

---

## 二、基础 URL 从哪来？

| 来源 | 说明 |
|------|------|
| **1. `<BASE href="...">`** | HTML 内**显式**指定 |
| **2. 封装资源 URL** | 未写 `<BASE>` 时，用**当前文档自身 URL** |
| **3. 无基础** | 相对 URL **无效/损坏** |

---

## 三、解析算法（直觉）

把相对 URL 与 Base **拆成组件**（scheme、host、port、path…）：

- 相对 URL 某组件**为空** → **继承** Base 的该组件  
- 非空 → 用相对部分（path 常按目录规则拼接）  

最终得到完整绝对 URL，再发起 HTTP 请求。

**例**（示意）

```text
Base:    http://www.example.com/dir/page.html
相对:    ../img/a.png
绝对:    http://www.example.com/img/a.png
```

---

## 易错

- 忘记 `<BASE>` 导致站内链接指向错误主机  
- `../` 层级数算错

---

## 抓包/实操记录

（待填：保存网页 + 相对链接，改 Base 看解析结果）

---

## 疑问与总结

相对 URL 减轻维护；发请求前在客户端**必先绝对化**。
