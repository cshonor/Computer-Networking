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
        ("01-server-type.md", "5.1 各种形状和尺寸的Web服务器"),
        ("02-type-o-serve.md", "5.2 最小的Perl Web服务器"),
        ("03-server-lifecycle.md", "5.3 实际的Web服务器会做些什么"),
        ("04-accept-connection.md", "5.4 第一步——接受客户端连接"),
        ("05-receive-request.md", "5.5 第二步——接收请求报文"),
        ("06-process-request.md", "5.6 第三步——处理请求"),
        ("07-resource-mapping.md", "5.7 第四步——对资源的映射及访问"),
        ("08-build-response.md", "5.8 第五步——构建响应"),
        ("09-send-response.md", "5.9 第六步——发送响应"),
        ("10-logging.md", "5.10 第七步——记录日志"),
    ]),
    ("chapter-06-proxy", "第6章 代理", [
        ("01-middleman.md", "6.1 Web的中间实体"),
        ("02-why-use-proxy.md", "6.2 为什么使用代理"),
        ("03-proxy-placement.md", "6.3 代理会去往何处"),
        ("04-client-proxy-settings.md", "6.4 客户端的代理设置"),
        ("05-proxy-request-issues.md", "6.5 与代理请求有关的一些棘手问题"),
        ("06-trace-message.md", "6.6 追踪报文"),
        ("07-proxy-auth.md", "6.7 代理认证"),
        ("08-proxy-interop.md", "6.8 代理的互操作性"),
    ]),
    ("chapter-07-cache", "第7章 缓存", [
        ("01-redundant-transfer.md", "7.1 冗余的数据传输"),
        ("02-bandwidth-bottleneck.md", "7.2 带宽瓶颈"),
        ("03-flash-crowds.md", "7.3 瞬间拥塞"),
        ("04-distance-latency.md", "7.4 距离时延"),
        ("05-hit-miss.md", "7.5 命中和未命中的"),
        ("06-cache-topology.md", "7.6 缓存的拓扑结构"),
        ("07-cache-steps.md", "7.7 缓存的处理步骤"),
        ("08-freshness-revalidation.md", "7.8 保持副本的新鲜"),
        ("09-cache-control.md", "7.9 控制缓存的能力"),
        ("10-configure-cache.md", "7.10 设置缓存控制"),
        ("11-freshness-algorithm.md", "7.11 详细算法"),
        ("12-cache-ads.md", "7.12 缓存和广告"),
    ]),
    ("chapter-08-gateway-tunnel-relay", "第8章 集成点：网关、隧道及中继", [
        ("01-gateway.md", "8.1 网关"),
        ("02-protocol-gateway.md", "8.2 协议网关"),
        ("03-resource-gateway.md", "8.3 资源网关"),
        ("04-web-services.md", "8.4 应用程序接口和Web服务"),
        ("05-tunnel.md", "8.5 隧道"),
        ("06-relay.md", "8.6 中继"),
        ("07-more-info.md", "8.7 更多信息"),
    ]),
    ("chapter-09-web-robot", "第9章 Web机器人", [
        ("01-crawling.md", "9.1 爬虫及爬行方式"),
        ("02-robot-http.md", "9.2 机器人的HTTP"),
        ("03-misbehaving-robots.md", "9.3 行为不当的机器人"),
        ("04-robots-exclusion.md", "9.4 拒绝机器人访问"),
        ("05-robot-guidelines.md", "9.5 机器人的规范"),
        ("06-search-engine.md", "9.6 搜索引擎"),
    ]),
    ("chapter-10-http-ng", "第10章 HTTP-NG", [
        ("01-problems.md", "10.1 HTTP发展中存在的问题"),
        ("02-http-ng-activity.md", "10.2 HTTP-NG的活动"),
        ("03-modularity.md", "10.3 模块化及功能增强"),
        ("04-distributed-objects.md", "10.4 分布式对象"),
        ("05-message-transport.md", "10.5 第一层——报文传输"),
        ("06-remote-invocation.md", "10.6 第二层——远程调用"),
        ("07-web-application.md", "10.7 第三层——Web应用"),
        ("08-webmux.md", "10.8 WebMUX"),
        ("09-binary-wire.md", "10.9 二进制连接协议"),
        ("10-current-status.md", "10.10 当前的状态"),
        ("11-more-info.md", "10.11 更多信息"),
    ]),
    ("chapter-11-client-id-cookie", "第11章 客户端识别与Cookie机制", [
        ("01-personalization.md", "11.1 个性化接触"),
        ("02-http-headers.md", "11.2 HTTP首部"),
        ("03-client-ip.md", "11.3 客户端IP地址"),
        ("04-user-login.md", "11.4 用户登录"),
        ("05-fat-url.md", "11.5 胖URL"),
        ("06-cookie.md", "11.6 cookie"),
    ]),
    ("chapter-12-basic-auth", "第12章 基本认证机制", [
        ("01-authentication.md", "12.1 认证"),
        ("02-basic-auth.md", "12.2 基本认证"),
        ("03-security-flaws.md", "12.3 基本认证的安全缺陷"),
        ("04-more-info.md", "12.4 更多信息"),
    ]),
    ("chapter-13-digest-auth", "第13章 摘要认证", [
        ("01-digest-improvements.md", "13.1 摘要认证的改进"),
        ("02-digest-computation.md", "13.2 摘要的计算"),
        ("03-qop-quality.md", "13.3 增强保护质量"),
        ("04-practical-issues.md", "13.4 应该考虑的实际问题"),
        ("05-security-considerations.md", "13.5 安全性考虑"),
        ("06-more-info.md", "13.6 更多信息"),
    ]),
    ("chapter-14-secure-http", "第14章 安全HTTP", [
        ("01-protect-http.md", "14.1 保护HTTP的安全"),
        ("02-digital-crypto.md", "14.2 数字加密"),
        ("03-symmetric-key.md", "14.3 对称密钥加密技术"),
        ("04-public-key.md", "14.4 公开密钥加密技术"),
        ("05-digital-signature.md", "14.5 数字签名"),
        ("06-digital-cert.md", "14.6 数字证书"),
        ("07-https-details.md", "14.7 HTTPS——细节介绍"),
        ("08-https-client.md", "14.8 HTTPS客户端实例"),
        ("09-proxy-tunnel.md", "14.9 通过代理以隧道形式传输安全流量"),
        ("10-more-info.md", "14.10 更多信息"),
    ]),
    ("chapter-15-entity-encoding", "第15章 实体和编码", [
        ("01-entity-cargo.md", "15.1 报文是箱子，实体是货物"),
        ("02-content-length.md", "15.2 Content-Length: 实体的大小"),
        ("03-entity-digest.md", "15.3 实体摘要"),
        ("04-media-type.md", "15.4 媒体类型和字符集"),
        ("05-content-encoding.md", "15.5 内容编码"),
        ("06-transfer-chunked.md", "15.6 传输编码和分块编码"),
        ("07-instances.md", "15.7 随时间变化的实例"),
        ("08-validators-freshness.md", "15.8 验证码和新鲜度"),
        ("09-range-request.md", "15.9 范围请求"),
        ("10-delta-encoding.md", "15.10 差异编码"),
        ("11-more-info.md", "15.11 更多信息"),
    ]),
    ("chapter-16-internationalization", "第16章 国际化", [
        ("01-intl-content-support.md", "16.1 HTTP对国际性内容的支持"),
        ("02-charset-http.md", "16.2 字符集与HTTP"),
        ("03-charset-fundamentals.md", "16.3 多语言字符编码入门"),
        ("04-language-tags.md", "16.4 语言标记与HTTP"),
        ("05-intl-uri.md", "16.5 国际化的URI"),
        ("06-other-considerations.md", "16.6 其他需要考虑的地方"),
    ]),
    ("chapter-17-content-negotiation-transcode", "第17章 内容协商与转码", [
        ("01-content-negotiation.md", "17.1 内容协商技术"),
        ("02-client-driven-negotiation.md", "17.2 客户端驱动的协商"),
        ("03-server-driven-negotiation.md", "17.3 服务器驱动的协商"),
        ("04-transparent-negotiation.md", "17.4 透明协商"),
        ("05-transcode.md", "17.5 转码"),
        ("06-next-steps.md", "17.6 下一步计划"),
        ("07-more-info.md", "17.7 更多信息"),
    ]),
    ("chapter-18-web-hosting", "第18章 Web主机托管", [
        ("01-hosting-service.md", "18.1 主机托管服务"),
        ("02-virtual-hosting.md", "18.2 虚拟主机托管"),
        ("03-reliability.md", "18.3 使网站更可靠"),
        ("04-performance.md", "18.4 让网站更快"),
        ("05-more-info.md", "18.5 更多信息"),
    ]),
    ("chapter-19-publishing-system", "第19章 发布系统", [
        ("01-frontpage-fpse.md", "19.1 FrontPage为支持发布而做的服务器扩展"),
        ("02-webdav.md", "19.2 WebDAV与协作写作"),
        ("03-more-info.md", "19.3 更多信息"),
    ]),
    ("chapter-20-redirect-load-balance", "第20章 重定向与负载均衡", [
        ("01-why-redirect.md", "20.1 为什么要重定向"),
        ("02-where-redirect.md", "20.2 重定向到何地"),
        ("03-redirect-overview.md", "20.3 重定向协议概览"),
        ("04-general-redirect-methods.md", "20.4 通用的重定向方法"),
        ("05-proxy-redirect.md", "20.5 代理的重定向方法"),
        ("06-cache-redirect-wccp.md", "20.6 缓存重定向方法"),
        ("07-icp.md", "20.7 因特网缓存协议"),
        ("08-carp.md", "20.8 缓存阵列路由协议"),
        ("09-htcp.md", "20.9 超文本缓存协议"),
    ]),
    ("chapter-21-log-tracking", "第21章 日志记录与使用情况跟踪", [
        ("01-log-content.md", "21.1 记录内容"),
        ("02-log-formats.md", "21.2 日志格式"),
        ("03-hit-metering.md", "21.3 命中率测量"),
        ("04-privacy.md", "21.4 关于隐私的考虑"),
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

    outline_lines = ["# 章节目录\n", "| 章 | 文件夹 | 小节数 |\n", "|----|--------|--------|\n"]
    readme_rows = []

    for folder, ch_title, sections in CHAPTERS:
        ch_dir = ROOT / folder
        ch_dir.mkdir(parents=True, exist_ok=True)

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
