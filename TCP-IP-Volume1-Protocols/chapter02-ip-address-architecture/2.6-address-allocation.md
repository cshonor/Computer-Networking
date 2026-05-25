# 2.6 分配

> 章级精读：[../study.md#ch02-6](../study.md#ch02-6)

## 本节核心目标

掌握全球 IP 空间的**层级分配体系**与 WHOIS 溯源。

---

## 层级结构

```text
IANA（全球池）
  → RIR（区域：APNIC、ARIN、RIPE、LACNIC、AFRINIC）
    → LIR / ISP / 大型企业
      → 终端用户或站点前缀
```

---

## 实操

- **WHOIS / RDAP**：查前缀归属、滥用投诉、路由溯源。
- 与 **BGP 宣告** 一致：分得地址块还需 ISP 愿意向上游 **aggregate/announce**。

---

## 与下一节关系

- 2.6 讲**谁发号**；2.7 讲**站点怎么规划用号**（家庭/企业/多宿主）。
