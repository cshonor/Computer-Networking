# 5.1 各种形状和尺寸的Web服务器

> 本章：[chapter-summary.md](./chapter-summary.md#ch05-1) · 全书：[../README.md](../README.md)

## 本节核心目标

认识 **Web 服务器** 的共同职责与三种常见形态。

---

<a id="ch05-1-role"></a>

## 一、核心职责

无论规模大小，Web 服务器都要：

1. **接收** HTTP 请求  
2. **处理** 请求  
3. **回送** 内容给客户端  

实现上包含：**HTTP 语义**、**TCP 连接管理**、**资源与配置**。

→ [5.3 七步生命周期](./03-server-lifecycle.md)

---

<a id="ch05-1-forms"></a>

## 二、三种形态

| 类型 | 例子 | 特点 |
|------|------|------|
| **通用软件服务器** | Apache、IIS、**Nginx**、Caddy | 跑在通用 OS 上，可扩展 |
| **Web 服务器设备** | 专用硬件盒 | 预装、裁剪 OS，即插即用 |
| **嵌入式服务器** | 打印机、路由器管理页 | 微型 HTTP，设备配置 UI |

---

## 拓展（预留）

- Nginx 事件驱动 vs Apache 多进程/模块  
- Docker/K8s 中 Ingress + 后端 Pod  

---

## 抓包/实操记录

（待填：本机 `nginx -v` / `httpd -v`）

---

## 疑问与总结

**服务器 = HTTP + TCP + 资源映射**；形态不同，七步模型相同。
