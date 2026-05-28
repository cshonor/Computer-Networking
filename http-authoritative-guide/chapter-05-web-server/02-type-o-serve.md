# 5.2 最小的Perl Web服务器

> 本章：[chapter-summary.md](./chapter-summary.md#ch05-2) · [5.3 商用七步](./03-server-lifecycle.md)

## 本节核心目标

通过 **`type-o-serve`** 理解「收请求 → 人写响应 → 发回」的最小 HTTP 循环。

---

<a id="ch05-2-tool"></a>

## 一、定位

| 属性 | 说明 |
|------|------|
| **不是** | 生产级完整服务器 |
| **是** | **调试/教学** 工具：手搓极端 HTTP 场景 |

---

<a id="ch05-2-flow"></a>

## 二、交互逻辑

1. 监听指定端口  
2. **打印**收到的请求报文  
3. 操作者**手动输入**响应行 + 首部 + 空行 + body  
4. 工具把响应**发回**客户端  

可模拟畸形首部、错误 `Content-Length` 等 → 配合 [ch04 关闭连接](../chapter-04-connection-management/07-close-connection.md)

---

## 拓展（预留）

| 现代替代 | 用途 |
|----------|------|
| `curl -v` | 发请求、看响应 |
| `nc` / Telnet | 手敲 HTTP |
| `python -m http.server` | 静态文件极简服务 |
| Postman | GUI 调试 |

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**看懂报文字节流比背框架更重要**；type-o-serve 把「第 2、6 步」暴露给人。
