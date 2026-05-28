# 5.3 实际的Web服务器会做些什么

> 本章：[chapter-summary.md](./chapter-summary.md#ch05-3) · [ch04 连接](../chapter-04-connection-management/chapter-summary.md)

## 本节核心目标

记住商用 Web 服务器处理一次事务的 **七大步骤**（全书 ch5 骨架）。

---

<a id="ch05-3-seven"></a>

## 七步模型

| 步 | 动作 | 详节 |
|----|------|------|
| **1** | **建立连接** — 接受/拒绝/关闭 TCP | [5.4](./04-accept-connection.md) |
| **2** | **接收请求** — 读入并解析 HTTP 请求 | [5.5](./05-receive-request.md) |
| **3** | **处理请求** — 按方法/首部路由 | [5.6](./06-process-request.md) |
| **4** | **访问资源** — URI → 文件或程序 | [5.7](./07-resource-mapping.md) |
| **5** | **构建响应** — 状态码 + 首部 + body | [5.8](./08-build-response.md) |
| **6** | **发送响应** — 写回连接 | [5.9](./09-send-response.md) |
| **7** | **记录日志** — 落盘审计 | [5.10](./10-logging.md) |

```text
连接 → 读请求 → 处理 → 映射资源 → 组响应 → 发送 → 写日志
```

---

## 拓展（预留）

- Servlet 生命周期、Express **中间件洋葱模型**（请求自上而下、响应自下而上）

---

## 抓包/实操记录

（待填：对照 Nginx access log 一条记录对应哪几步）

---

## 疑问与总结

**后面 5.4–5.10 全是七步的展开**；排障时先定位卡在哪一步。
