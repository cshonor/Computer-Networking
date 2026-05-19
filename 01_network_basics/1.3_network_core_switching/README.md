# 1.3 — network core switching

## 知识点速记

- **网络核心**：路由器骨干；**转发**（本地出接口）vs **路由**（全局算路）→ 配图 `routing_vs_forwarding.png`
- **通俗深拆**：[FDM/TDM vs 分组调度](./study.md#ch1-3-switching-intuition) · 分组/IP/帧层级
- **电路交换**：独占链路；FDM（同时不同频）/ TDM（固定时隙）；电话网
- **分组交换**：存储转发、统计复用；`d ≈ N×(L/R)`；Internet 主流
- **数据报 vs 虚电路**：目的地址独立选路 vs VCI+呼叫建立+每跳换标（ATM）
- **对比**：电话用电路，互联网用分组

## 与后端开发的联系

- 排队时延、丢包与「核心拥塞」排查；与第 4 章 FIB、第 5 章 BGP/OSPF 衔接

## 延伸阅读

- 背诵版：[study.md](./study.md) · 章级：[study.md § 1.3](../study.md#ch1-3) · [FIB](../../04_network_layer_data_plane/study.md#ch4-fib)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 可背诵完整版 + 易错表 |
| `demo_code/` | 示例代码 |
