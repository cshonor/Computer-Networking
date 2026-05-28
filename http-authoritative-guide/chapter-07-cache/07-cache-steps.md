# 7.7 缓存的处理步骤

> 本章：[chapter-summary.md](./chapter-summary.md#ch07-7) · [ch05 服务器七步](../chapter-05-web-server/03-server-lifecycle.md)

## 本节核心目标

记住代理缓存处理 **GET** 的 **七步**（与 Web 服务器七步对照）。

---

<a id="ch07-7-seven"></a>

| 步 | 动作 |
|----|------|
| **1 接收** | 读连接上的请求报文 |
| **2 解析** | 结构化首部；URL 大小写/格式**规范化** |
| **3 查找** | 内存/磁盘/邻近节点查 URL 副本与元数据 |
| **4 新鲜度检测** | 过期则**再验证** → [7.8](./08-freshness-revalidation.md) |
| **5 创建响应** | 以源站首部为底，加 `Cache-Control`/`Age`/`Expires`/`Via`；**不得改 `Date`**（原始创建时间） |
| **6 发送** | 回客户端；可用 **sendfile** 等 |
| **7 日志** | 命中率统计、Squid/网景格式日志 → [ch21](../chapter-21-log-tracking/chapter-summary.md) |

---

## 抓包/实操记录

（待填：Squid access.log 字段）

---

## 疑问与总结

**第 5 步：可加缓存首部，不能伪造文档诞生时间。**
