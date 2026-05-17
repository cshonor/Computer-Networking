# computer_network_top_down

> 后端开发专用 · 计算机网络（自顶向下方法）学习仓库  
> 主攻方向：**网络编程、Socket 通信、TCP/IP 底层、服务端网络原理**  
> 学习顺序：先应用层 → 运输层 → 网络层 → 链路层，贴合后端日常开发

## 仓库整体目录结构

```
Computer-Networking/
├─ 01_network_basics              # 第1章 网络基础入门
├─ 02_application_layer           # 第2章 应用层（后端高频）
├─ 03_transport_layer             # 第3章 运输层（TCP/UDP 核心）
├─ 04_network_layer_data_plane    # 第4章 网络层-数据平面
├─ 05_network_layer_control_plane   # 第5章 网络层-控制平面
├─ 06_link_layer_and_lan          # 第6章 链路层与局域网
├─ 07_wireless_mobile_network     # 第7章 无线网络（选学）
├─ 08_network_security            # 第8章 网络安全（后端必备）
├─ 99_socket_code_demo            # 网络编程实战代码（汇总）
├─ 99_practice_wireshark_lab      # 抓包实验笔记
├─ 99_review_exercises_notes      # 综合笔记 + 面试总结
└─ tcpip_vol1_ed2_notes/          # TCP/IP 详解 卷1 第2版 Fall 2016（18 章，见 QUICKREF.md）
```

## 后端必学核心路线（优先级从高到低）

1. **01 网络基础**：建立整体网络认知，看懂时延、分组交换、五层模型  
2. **02 应用层**：HTTP、DNS、邮件、Socket 入门，写服务端接口必备  
3. **03 运输层（重中之重）**
   - UDP 无连接通信  
   - TCP 三次握手、四次挥手、可靠传输、流量控制、拥塞控制  
   - 后端服务通信、长连接、短连接与这一章强相关  
4. **04 网络层（数据平面）**：IP 地址、网段、NAT、路由转发  
5. **06 链路层**：MAC、ARP、交换机原理  
6. **08 网络安全**：HTTPS、TLS、加密、防火墙  
7. 其余章节：工作用到再深入学习  

## 小节目录统一规范

每个小节文件夹内固定包含：

| 路径 | 用途 |
|------|------|
| `README.md` | 本章知识点精简笔记（速查） |
| `study.md` | 个人精读学习笔记 |
| `demo_code/` | 对应语言网络编程示例（Java / Go / Python / C++ 等） |

## 学习目标

1. 吃透 **Socket 网络编程**，能手写 TCP 服务端与客户端  
2. 理解 TCP 底层机制，能分析连接异常、粘包、断连等问题  
3. 掌握 **HTTP** 完整请求流程，能对照抓包看懂接口全链路  
4. 具备后端服务网络调优与线上网络问题排查的基本功  
5. 从容应对后端开发中的网络相关面试  

## 学习工具

- 抓包：Wireshark  
- 网络调试：NetAssist、`nc` 等  
- 编程环境：Go / Python / Java（任选其一为主即可）  
- 参考书：《计算机网络：自顶向下方法》  

## 提交规范

```
feat: 新增xx章节笔记
code: 完成TCP服务端代码
fix: 修正网络知识点错误
note: 整理面试网络题
```
