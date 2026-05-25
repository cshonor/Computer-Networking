# 4.5 ARP 例子（抓包与超时）

> 章级精读：[../study.md#ch04-2](../study.md#ch04-2) · [../study.md#ch04-4](../study.md#ch04-4)

## 本节核心目标

对照 **tcpdump/Wireshark** 理解正常 ARP 与**解析失败**行为。

---

## 正常过程

| 步骤 | 特征 |
|------|------|
| 请求 | 目的 MAC **广播 ff:ff:ff:ff:ff:ff** |
| 应答 | **单播** 回请求方 |
| 耗时 | 通常 **毫秒级** |

---

## 主机不存在

- 栈会**多次重试** ARP 请求。
- 最终 **Incomplete 超时**；链路层常**静默**，上层可能迟迟无响应或收到 **ICMP 不可达**。

---

## Lab

```bash
tcpdump -i eth0 arp
# 或
ip neigh show
```
