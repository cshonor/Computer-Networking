# 14.8 HTTPS 客户端实例

> 本章：[chapter-summary.md](./chapter-summary.md#ch14-8)

## 本节核心目标

用 **OpenSSL** API 理解 HTTPS 客户端**分层步骤**（书中 C 示例脉络）。

---

<a id="ch14-8-steps"></a>

## 执行逻辑

| 步 | API/动作 |
|----|----------|
| 1 | `SSL_CTX_new` 初始化库与上下文 |
| 2 | 解析主机名 → IP |
| 3 | Socket 连 **443** |
| 4 | `SSL_set_fd` + **`SSL_connect`** 握手 |
| 5 | 打印协商密码套件、**X.509** 颁发者 |
| 6 | **`SSL_write`** 发明文 HTTP GET；**`SSL_read`** 收响应 |
| 7 | 关闭 SSL、释放上下文 |

应用仍写**明文 HTTP**；加密由 SSL 层完成。

---

## 拓展（预留）

- `curl -v https://`、Python `ssl` 模块对照  

---

## 抓包/实操记录

（待填）

---

## 疑问与总结

**编程模型：TCP socket 上叠 SSL，再当字节流写 HTTP。**
