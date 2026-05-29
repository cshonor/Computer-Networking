# 13.4 应该考虑的实际问题

> 本章：[chapter-summary.md](./chapter-summary.md#ch13-4) · [ch06 代理改 URI](../chapter-06-proxy/05-proxy-request-issues.md) · [ch07 缓存](../chapter-07-cache/09-cache-control.md)

## 本节核心目标

部署 Digest 时的**多重质询、代理改 URI、缓存**等互操作规则。

---

<a id="ch13-4-multi"></a>

## 13.4.1 多重质询

服务器可同时提供 **Basic + Digest** → 客户端应选所支持**最强**机制，防「最弱环节」降级。

---

<a id="ch13-4-errors"></a>

## 13.4.2 差错处理

| 情况 | 处理 |
|------|------|
| 摘要不匹配 | 记失败日志 |
| `Authorization` 里 URI ≠ 请求行 URI | **`400 Bad Request`** |

---

<a id="ch13-4-domain"></a>

## 13.4.3 保护空间

**`domain`** + **`realm`** 定义凭证可**自动重用**的 URI 范围（列表及逻辑子路径）。

---

<a id="ch13-4-uri"></a>

## 13.4.4 代理重写 URI（易错）

摘要 **A2** 含**原始** `<method>:<uri>`。

代理若**改写 URI**（标准化主机名、转义等）→ 服务器侧摘要**对不上** → **认证失败**。

→ [ch06 §6.5](../chapter-06-proxy/05-proxy-request-issues.md)

---

<a id="ch13-4-cache"></a>

## 13.4.5 缓存

含 **`Authorization`** 的响应：

- 默认**不得**作为其他用户的缓存应答  
- 仅当 `Cache-Control: must-revalidate` 或 `public` 等明确允许时方可缓存，且常需**回源验证**

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**Digest 与「会改 URI 的代理」天然别扭。**
