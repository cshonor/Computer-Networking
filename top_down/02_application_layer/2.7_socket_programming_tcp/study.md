# 2.7 TCP Socket 网络编程

> 章级精读：[../study.md#ch2-7-tcp](../study.md#ch2-7-tcp)

## 本节核心目标

学会应用层如何通过 Socket 调用传输层 TCP。

## 核心知识点

1. Socket 本质：应用层与运输层之间的编程接口
2. TCP Socket 服务端流程：`socket` → `bind` → `listen` → `accept`
3. TCP Socket 客户端流程：`socket` → `connect`
4. 基于 TCP 实现可靠端到端通信

## 个人总结

Socket 就是程序员面向网络的统一编程入口。
