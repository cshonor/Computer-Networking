# 6.4 DHCP 和 DNS 交互

> 章级精读：[../study.md#ch06-4](../study.md#ch06-4) · DNS：[ch11](../../chapter11-dns-domain-resolve/study.md)

## 本节核心目标

理解 **DDNS（动态 DNS 更新）** 解决“IP 变、名字不变”。

---

## 痛点

- DHCP 租约续期或重连 → 客户端 **IP 常变**。
- 其他设备用**主机名**访问时需最新 **A/AAAA** 记录。

---

## DDNS 机制

- **DHCP 服务器**（或客户端）在分配/更新 IP 后，向 DNS 发送**更新报文**，刷新 **FQDN ↔ IP** 映射。
- 依赖 DNS 与 DHCP 的**信任与认证**（如 TSIG），否则易被滥用。

---

## 实践

- 企业 AD、家用路由器“主机名注册”多属此类思路。
