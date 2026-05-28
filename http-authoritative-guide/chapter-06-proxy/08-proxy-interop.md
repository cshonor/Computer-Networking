# 6.8 代理的互操作性

> 本章：[chapter-summary.md](./chapter-summary.md#ch06-8) · [ch04 Connection](../chapter-04-connection-management/03-http-connection.md)

## 本节核心目标

代理作为中间人必须**保守转发**未知扩展，并用 **OPTIONS / Allow** 探测能力。

---

<a id="ch06-8-forward"></a>

## 一、未知首部与方法

| 规则 | 说明 |
|------|------|
| **不认识的扩展首部** | **原样转发**，**不得改变同名首部顺序** |
| **不认识的扩展方法** | 尽量转发；必须拦截时 → **`501 Not Implemented`** |

---

<a id="ch06-8-options"></a>

## 二、OPTIONS 与 Allow

| 项 | 说明 |
|----|------|
| **OPTIONS** | 探测服务器/资源支持的方法；`OPTIONS *` 探测整站 |
| **Allow** | 成功 `200` 响应中的实体首部，如 `Allow: GET, HEAD, PUT` |

**易错**：代理**不能**因不懂某方法就**删改 `Allow` 内容**。

---

## 拓展（预留）

- **CORS 预检** 重用 OPTIONS → 代理应透明转发 [ch14](../chapter-14-secure-http/chapter-summary.md) 相关首部  

---

## 抓包/实操记录

（待填：`curl -X OPTIONS -v https://example.com`）

---

## 疑问与总结

**代理默认是透明管道，不是协议警察（除非策略要求）。**
