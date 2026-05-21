# 6.5 以太网上的 PPP (PPPoE)

> 章级精读：[../study.md#ch06-4](../study.md#ch06-4) · PPP：[ch03 §3.6](../../chapter03-link-layer/3.6-ppp-protocol/study.md)

## 本节核心目标

理解家庭宽带用 **PPPoE** 在以太网上跑 **PPP 认证 + IPCP 配址**。

---

## 为何 PP PoE

- 运营商需在以太网接入上完成**账号认证**与**动态 IP 下发**。
- **PPP** 原生为点到点；**PPPoE** = PPP 载荷封装在以太网帧中。

---

## 流程（概念）

1. **发现** PPPoE 会话（PADI/PADO…）。
2. **LCP** 建链 + **PAP/CHAP** 认证。
3. **IPCP** 协商获得运营商分配的 IPv4 地址、DNS 等。

---

## 与 DHCP 关系

- 家庭光猫“拨号上网”常见 **PPPoE**；内网 PC 仍可用 **DHCP** 向路由器要私网地址（双层结构）。
