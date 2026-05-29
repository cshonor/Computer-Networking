# 14.7 HTTPS——细节介绍

> 本章：[chapter-summary.md](./chapter-summary.md#ch14-7) · [ch08 SSL 卸载](../chapter-08-gateway-tunnel-relay/02-protocol-gateway.md#ch08-2-https-http)

## 本节核心目标

掌握 **https:// :443**、**TLS 握手**、证书**四步验证**与**虚拟主机**证书问题。

---

<a id="ch14-7-overview"></a>

## 14.7.1–14.7.2 概述

| 项 | 值 |
|----|-----|
| 方案 | **`https://`** |
| 默认端口 | **443**（HTTP 为 80） |

---

<a id="ch14-7-handshake"></a>

## 14.7.3–14.7.4 建立安全传输

1. **TCP** 连 443  
2. **TLS 握手**：版本、密码套件、**服务器证书**、生成**会话密钥**  
3. HTTP 报文经 TLS **加密**后进 TCP  

---

<a id="ch14-7-verify"></a>

## 14.7.6 站点证书有效性（四步）

1. **日期**是否在有效期内  
2. **颁发者 CA** 是否受信  
3. **签名**是否有效（用 CA 公钥验）  
4. **证书域名**是否与访问域名**匹配**  

---

<a id="ch14-7-vhost"></a>

## 14.7.7 虚拟主机与证书（易错）

一 IP:443 传统上常只能绑**一张**证书 → 多域名虚拟主机可能**域名不匹配**警告。

**SNI**（Server Name Indication）：客户端在握手时发**目标主机名** → 服务器选对应证书 → [ch18](../chapter-18-web-hosting/chapter-summary.md)

---

## 抓包/实操记录

（待填：TLS Client Hello 里 SNI）

---

## 疑问与总结

**HTTPS = HTTP + TLS；握手定密钥，之后全是密文 Application Data。**
