# 8.2 协议网关

> 本章：[chapter-summary.md](./chapter-summary.md#ch08-2) · [8.1 网关](./01-gateway.md)

## 本节核心目标

掌握 **HTTP 与非 HTTP 协议**之间的**双向自动翻译**及三类典型网关。

---

<a id="ch08-2-http-star"></a>

## 8.2.1 HTTP/*：服务器端 Web 网关

**HTTP 请求 → 其他协议 → 源站**

**FTP 网关示例**（`ftp://ftp.irs.gov/...` 的 HTTP 请求）：

1. 连 FTP **21**  
2. 发控制命令：`USER`、`PASS`、`CWD`、`TYPE A`、`MDTM`、`PASV`、`RETR`…  
3. 取数据 → 封装进 **HTTP 响应**  

---

<a id="ch08-2-http-https"></a>

## 8.2.2 HTTP/HTTPS：服务器端安全网关

| 路径 | 说明 |
|------|------|
| 客户端 → 网关 | 普通 **HTTP** |
| 网关 → 后端 | 加密为 **HTTPS** |

网关承担 TLS，增强隐私（客户端不直接握后端证书链）。

---

<a id="ch08-2-https-http"></a>

## 8.2.3 HTTPS/HTTP：客户端安全加速器

部署在源站前（**反向代理/拦截网关**）：

```text
客户端 ──HTTPS──► 网关（硬件解密）──HTTP 明文──► 源站
```

| 点 | 说明 |
|----|------|
| **性能** | 专用解密硬件，减轻源站 CPU |
| **易错** | 网关↔源站为**明文**，**内网必须可信**（VLAN/专线） |

→ [ch14 TLS](../chapter-14-secure-http/chapter-summary.md)

---

## 抓包/实操记录

（待填：SSL 卸载后内网是否仍为 HTTP）

---

## 疑问与总结

**SSL 卸载 = 性能换一段明文链路**；边界要画在网关内侧。
