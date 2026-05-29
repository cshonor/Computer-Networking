# 11.3 客户端IP地址

> 本章：[chapter-summary.md](./chapter-summary.md#ch11-3) · [ch06 代理](../chapter-06-proxy/chapter-summary.md)

## 本节核心目标

理解为何 **IP 不能**作为稳定用户标识。

---

<a id="ch11-3-problems"></a>

## 重点缺陷

| 问题 | 说明 |
|------|------|
| **NAT / 代理** | 多用户**共享**出口 IP |
| **动态 IP** | DHCP、拨号 → IP **常变** |
| **拦截代理** | 源站只见**代理 IP** |
| **扩展首部** | `Client-IP`、`X-Forwarded-For` 非强制，**可伪造** |

→ 反向代理常设 `X-Forwarded-For` → [ch05](../chapter-05-web-server/chapter-summary.md)

---

## 拓展（预留）

- WAF + IP 信誉 + **设备指纹**  

---

## 抓包/实操记录

（待填：经代理时 `X-Forwarded-For`）

---

## 疑问与总结

**IP = 大致位置/线路，≠ 用户账号。**
