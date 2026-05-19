# 1.5 — protocol layer architecture

## 知识点速记

- **五层**：应运网链物；PDU：报文→段→包→帧→比特
- **分层优点**：解耦、易维护、复用、标准化
- **对等层**：同层逻辑对话；实际靠下层封装传递
- **封装**：应用数据 → TCP → IP → **以太网帧（MAC 最外）**
- **1.6–1.8**：安全/历史/小结在章级 [study.md](../study.md#ch1-6)

## 与后端开发的联系

- Wireshark 树形展开 = 解封装；读包从帧剥到 HTTP 是基本功 → [ch4 抓包图](../../04_network_layer_data_plane/study.md#ch4-encapsulation-wireshark)

## 延伸阅读

- 背诵版：[study.md](./study.md) · 易错：[#ch1-5-exam](./study.md#ch1-5-exam) · 封装：[ch4](../../04_network_layer_data_plane/study.md#ch4-encapsulation)

## 本目录文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 小节速记（你正在看的） |
| `study.md` | 可背诵完整版 + 封装流程 |
| `demo_code/` | 示例代码 |
