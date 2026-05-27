# Chapter 6 — TShark & tcpdump

> [README.md](./README.md) · [study.md](../study.md)

## 核心目标

生产环境命令行抓包、文件轮转、与 GUI 联动分析。

## 命令备忘（待扩展）

```bash
# 示例
tshark -i eth0 -f "port 443" -w capture.pcapng
tcpdump -i any -nn host 10.0.0.1 -w out.pcap
```

## 笔记 / 练习 / 总结

（待填）
