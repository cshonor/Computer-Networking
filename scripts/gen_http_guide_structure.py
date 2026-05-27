# -*- coding: utf-8 -*-
"""Generate http-authoritative-guide/ chapter folders and section files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "http-authoritative-guide"

CHAPTERS = [
    ("chapter-01-http-overview", "第1章 HTTP概述", [
        ("01-http-messenger.md", "1.1 HTTP——因特网的多媒体信使"),
        ("02-web-client-server.md", "1.2 Web客户端和服务器"),
        ("03-resource.md", "1.3 资源"),
        ("04-transaction.md", "1.4 事务"),
        ("05-message.md", "1.5 报文"),
        ("06-connection.md", "1.6 连接"),
        ("07-protocol-version.md", "1.7 协议版本"),
        ("08-web-component.md", "1.8 Web的结构组件"),
        ("09-conclusion.md", "1.9 起始部分的结束语"),
        ("10-more-info.md", "1.10 更多信息"),
    ]),
    ("chapter-02-url-and-resource", "第2章 URL与资源", [
        ("01-identifier.md", "2.1 浏览因特网的标识符"),
        ("02-url-syntax.md", "2.2 URL语法"),
        ("03-short-url-resolve.md", "2.3 短URL与URL解析"),
        ("04-relative-url.md", "2.4 相对URL"),
        ("05-url-shortcut.md", "2.5 URL快捷方式"),
        ("06-urn-future.md", "2.6 未来的URL：URN"),
    ]),
    ("chapter-03-http-message", "第3章 HTTP报文", [
        ("01-message-flow.md", "3.1 流动的报文"),
        ("02-message-component.md", "3.2 报文的组成部分"),
        ("03-method.md", "3.3 方法"),
        ("04-status-code.md", "3.4 状态码"),
        ("05-header.md", "3.5 首部"),
        ("06-entity.md", "3.6 实体"),
    ]),
    ("chapter-04-connection-management", "第4章 连接管理", [
        ("01-connection-desire.md", "4.1 对连接的渴望"),
        ("02-tcp-connection.md", "4.2 TCP连接"),
        ("03-http-connection.md", "4.3 HTTP连接"),
        ("04-parallel-connection.md", "4.4 并行连接"),
        ("05-persistent-connection.md", "4.5 持久连接"),
        ("06-pipeline-connection.md", "4.6 管道连接"),
        ("07-close-connection.md", "4.7 关闭连接"),
        ("08-connection-limit.md", "4.8 连接限制与设置"),
    ]),
    ("chapter-05-web-server", "第5章 Web服务器", [
        ("01-server-type.md", "5.1 各种Web服务器"),
        ("02-server-structure.md", "5.2 服务器结构"),
        ("03-virtual-host.md", "5.3 虚拟主机"),
        ("04-gateway.md", "5.4 网关"),
        ("05-server-security.md", "5.5 服务器安全与访问控制"),
    ]),
    ("chapter-06-proxy", "第6章 代理", [
        ("01-middleman.md", "6.1 中间人"),
        ("02-proxy-type.md", "6.2 代理的类型与使用场景"),
        ("03-proxy-request-response.md", "6.3 代理请求与响应"),
        ("04-proxy-topology.md", "6.4 代理拓扑与路由"),
        ("05-proxy-security-filter.md", "6.5 代理安全与过滤"),
        ("06-proxy-config.md", "6.6 代理配置"),
    ]),
    ("chapter-07-cache", "第7章 缓存", [
        ("01-cache-basic.md", "7.1 缓存的基本思想"),
        ("02-cache-type-level.md", "7.2 缓存的类型与层级"),
        ("03-cache-control.md", "7.3 缓存控制"),
        ("04-cache-expire-revalidate.md", "7.4 缓存过期与再验证"),
        ("05-cache-manage.md", "7.5 缓存实体的管理"),
        ("06-cache-problem.md", "7.6 缓存问题与规避"),
    ]),
    ("chapter-08-gateway-tunnel-relay", "第8章 集成点：网关、隧道及中继", [
        ("01-gateway.md", "8.1 网关"),
        ("02-tunnel.md", "8.2 隧道"),
        ("03-relay.md", "8.3 中继"),
        ("04-scenario.md", "8.4 各类集成组件应用场景"),
    ]),
    ("chapter-09-web-robot", "第9章 Web机器人", [
        ("01-robot-overview.md", "9.1 爬虫与机器人概述"),
        ("02-robot-architecture.md", "9.2 爬虫架构与工作流程"),
        ("03-robot-strategy.md", "9.3 爬虫策略"),
        ("04-robot-rule.md", "9.4 机器人规范与限制"),
        ("05-robot-security.md", "9.5 爬虫安全与问题"),
    ]),
    ("chapter-10-http-ng", "第10章 HTTP-NG", [
        ("01-evolution-demand.md", "10.1 HTTP的演进需求"),
        ("02-http-ng-arch.md", "10.2 HTTP-NG架构"),
        ("03-modular-design.md", "10.3 模块化设计"),
        ("04-feature-improve.md", "10.4 协议特性与改进点"),
    ]),
    ("chapter-11-client-id-cookie", "第11章 客户端识别与Cookie机制", [
        ("01-client-identify.md", "11.1 客户端身份识别方案"),
        ("02-cookie-basic.md", "11.2 Cookie基础"),
        ("03-cookie-workflow.md", "11.3 Cookie工作原理"),
        ("04-cookie-attribute.md", "11.4 Cookie规范与属性"),
        ("05-cookie-security-privacy.md", "11.5 Cookie安全与隐私问题"),
    ]),
    ("chapter-12-basic-auth", "第12章 基本认证机制", [
        ("01-auth-overview.md", "12.1 HTTP认证概述"),
        ("02-basic-auth-flow.md", "12.2 基本认证流程"),
        ("03-basic-auth-message.md", "12.3 基本认证报文细节"),
        ("04-basic-auth-defect.md", "12.4 基本认证的安全缺陷"),
    ]),
    ("chapter-13-digest-auth", "第13章 摘要认证", [
        ("01-digest-improve.md", "13.1 摘要认证改进点"),
        ("02-digest-auth-flow.md", "13.2 摘要认证流程"),
        ("03-digest-algorithm.md", "13.3 摘要算法与报文"),
        ("04-digest-variant.md", "13.4 摘要认证变种与扩展"),
    ]),
    ("chapter-14-secure-http", "第14章 安全HTTP", [
        ("01-web-security-demand.md", "14.1 Web安全需求"),
        ("02-https-tls-ssl.md", "14.2 HTTPS与TLS/SSL基础"),
        ("03-https-handshake.md", "14.3 HTTPS握手流程"),
        ("04-encrypt-cert-key.md", "14.4 加密、证书与密钥"),
        ("05-secure-config.md", "14.5 安全协议配置与实践"),
    ]),
    ("chapter-15-entity-encoding", "第15章 实体和编码", [
        ("01-http-entity.md", "15.1 HTTP实体"),
        ("02-content-encoding.md", "15.2 内容编码"),
        ("03-transfer-encoding.md", "15.3 传输编码"),
        ("04-chunked-encoding.md", "15.4 分块编码"),
        ("05-entity-header.md", "15.5 实体首部详解"),
    ]),
    ("chapter-16-internationalization", "第16章 国际化", [
        ("01-charset-encoding.md", "16.1 字符集与编码问题"),
        ("02-charset-mark.md", "16.2 字符集标记"),
        ("03-multi-language.md", "16.3 多语言内容处理"),
        ("04-i18n-header.md", "16.4 国际化相关首部"),
    ]),
    ("chapter-17-content-negotiation-transcode", "第17章 内容协商与转码", [
        ("01-content-negotiation.md", "17.1 内容协商概述"),
        ("02-client-driven-negotiation.md", "17.2 客户端驱动协商"),
        ("03-server-driven-negotiation.md", "17.3 服务器驱动协商"),
        ("04-transcode.md", "17.4 转码与内容转换"),
    ]),
    ("chapter-18-web-hosting", "第18章 Web主机托管", [
        ("01-hosting-mode.md", "18.1 主机托管模式"),
        ("02-domain-virtual-host.md", "18.2 基于域名的虚拟主机"),
        ("03-ip-virtual-host.md", "18.3 基于IP的虚拟主机"),
        ("04-hosting-deploy.md", "18.4 托管架构与部署"),
    ]),
    ("chapter-19-publishing-system", "第19章 发布系统", [
        ("01-publish-process.md", "19.1 Web内容发布流程"),
        ("02-publish-tool-protocol.md", "19.2 发布工具与协议"),
        ("03-content-sync-update.md", "19.3 内容同步与更新"),
        ("04-large-site-arch.md", "19.4 大型站点发布架构"),
    ]),
    ("chapter-20-redirect-load-balance", "第20章 重定向与负载均衡", [
        ("01-http-redirect.md", "20.1 HTTP重定向"),
        ("02-redirect-status-code.md", "20.2 重定向状态码与使用场景"),
        ("03-load-balance-basic.md", "20.3 负载均衡基础"),
        ("04-traffic-schedule.md", "20.4 基于HTTP的流量调度"),
    ]),
    ("chapter-21-log-tracking", "第21章 日志记录与使用情况跟踪", [
        ("01-web-log-basic.md", "21.1 Web日志基础"),
        ("02-log-format-field.md", "21.2 日志格式与字段"),
        ("03-statistics-track.md", "21.3 访问统计与用户跟踪"),
        ("04-log-analyze-privacy.md", "21.4 日志分析与隐私问题"),
    ]),
]

SECTION_TPL = """# {title}

> 本章：[chapter-summary.md](./chapter-summary.md) · 全书：[../README.md](../README.md)

## 核心知识点

（待填）

## 抓包/实操记录

（待填）

## 疑问与总结

（待填）
"""

SUMMARY_TPL = """# {ch_title}

> 全书：[../README.md](../README.md)

## 本章概述

（待填）

## 知识框架

（待填）

## 重点 & 难点

（待填）

## 实操要点

（待填）

## 小节索引

{index}
"""


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / ".gitkeep").write_text("", encoding="utf-8")

    outline_lines = ["# 章节目录\n", "| 章 | 文件夹 | 小节数 |\n", "|----|--------|--------|\n"]
    readme_rows = []

    for folder, ch_title, sections in CHAPTERS:
        ch_dir = ROOT / folder
        ch_dir.mkdir(parents=True, exist_ok=True)
        (ch_dir / ".gitkeep").write_text("", encoding="utf-8")

        index_lines = []
        for fname, sec_title in sections:
            (ch_dir / fname).write_text(
                SECTION_TPL.format(title=sec_title), encoding="utf-8"
            )
            index_lines.append(f"- [{sec_title}](./{fname})")

        (ch_dir / "chapter-summary.md").write_text(
            SUMMARY_TPL.format(ch_title=ch_title, index="\n".join(index_lines)),
            encoding="utf-8",
        )

        n = len(sections)
        outline_lines.append(f"| {ch_title.split(' ')[0]} | `{folder}/` | {n} |\n")
        readme_rows.append(
            f"| {ch_title} | [{folder}/](./{folder}/) | "
            f"[summary](./{folder}/chapter-summary.md) |"
        )

    (ROOT / "OUTLINE.md").write_text("".join(outline_lines), encoding="utf-8")

    readme = f"""# HTTP 权威指南 学习笔记

《HTTP 权威指南》

> **打开本文件夹**：每章一个 `chapter-XX-*/`；**`chapter-summary.md` = 本章总览**，**`序号-英文名.md` = 小节笔记**。

## 书籍信息

| 项 | 说明 |
|----|------|
| 书名 | 《HTTP 权威指南》 |
| 结构 | 21 章，见 [OUTLINE.md](./OUTLINE.md) |

## 目录规范

- `chapter-xx-…/`：独立章节文件夹
- `chapter-summary.md`：本章整体总结、知识梳理
- `01-xxx.md`：对应小节独立笔记（见名知意，不用 section 通用名）
- `.gitkeep`：Git 空目录追踪

## 章节目录

| 章 | 文件夹 | 总览 |
|----|--------|------|
{chr(10).join(readme_rows)}

## 前置知识

- [计算机网络 自顶向下](../top_down/)
- [TCP/IP 详解 卷一](../TCP-IP-Volume1-Protocols/)

## 配套工具

Wireshark · [wireshark-packet-analysis](../wireshark-packet-analysis/) · NotebookLM（按章上传 `chapter-summary.md` 或单节 `*.md`）

## 小节模板

```markdown
# 小节标题
## 核心知识点
## 抓包/实操记录
## 疑问与总结
```
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    print(f"Generated {len(CHAPTERS)} chapters under {ROOT}")


if __name__ == "__main__":
    main()
