# 16.5 国际化的URI

> 本章：[chapter-summary.md](./chapter-summary.md#ch16-5) · [ch02 URL](../chapter-02-url-and-resource/chapter-summary.md)

## 本节核心目标

理解 URI 的 **ASCII 限制**、**% 转义** 及国际化陷阱。

---

<a id="ch16-5-ascii"></a>

## 16.5.1–16.5.2 可转抄与字符限制

URI 须在全球键盘/邮件/口头可准确复制 → 限制在 **US-ASCII** 子集（未保留、保留、转义）。

---

<a id="ch16-5-escape"></a>

## 16.5.3 转义

```text
% + 两位十六进制 ASCII 码
空格 → %20    % → %25
```

**禁止二次反转义**：`%25` 不应再被解成 `%` 后误当转义起始。

---

<a id="ch16-5-illegal"></a>

## 16.5.4 转义国际化字符（易错）

转义值须在 **0–127**。把 ISO-8859-1 高位直接 `%D6`（>127）**不符合规范**，下游可能崩溃。

正确：先 UTF-8 编码字节，再对每个字节 `%` 转义。

---

<a id="ch16-5-modal"></a>

## 16.5.5 URI 中的模态切换

iso-2022-jp 式切换在 URI 中**未良好定义**；交换应坚守 **ASCII**（现代 **IRI/Punycode** 另论）。

---

## 拓展（预留）

- **IDN**、**Punycode** `xn--` → [16.6](./06-other-considerations.md)

---

## 抓包/实操记录

（待填：中文路径的 percent-encoding）

---

## 疑问与总结

**URI 里看到的是 %XX，不是 Unicode 码点本身。**
