/*
 * UNP 卷1 · 图 1-5 · TCP Daytime 客户端（IPv4 协议相关 / 硬编码）
 * 节：1.2_SimpleTimeClient
 * 路径：code/1.2_SimpleTimeClient/original_c/daytimetcpcli.c
 * 用法：daytimetcpcli <IPv4地址>     例：daytimetcpcli 127.0.0.1
 * 依赖：原书 unp.h + libunp（附录 D）
 * 对照：1.3 daytimetcpcli6.c（IPv6 硬编码）· daytimetcpcligai.c（getaddrinfo）
 */
#include "unp.h"

int
main(int argc, char **argv)
{
    int                 sockfd, n;              /* sockfd：已连接 TCP 套接字；n：本次 read 字节数 */
    char                recvline[MAXLINE + 1];  /* 读缓冲；+1 留 '\0'，便于当 C 字符串打印 */
    struct sockaddr_in  servaddr;               /* IPv4 专用地址结构（协议强耦合点） */

    /* 必须传入一个参数：服务器 IPv4 点分十进制字符串 */
    if (argc != 2)
        err_quit("usage: daytimetcpcli <IPaddress>");

    /* ① 创建套接字：AF_INET=IPv4，SOCK_STREAM=TCP，协议字段 0=默认 TCP */
    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
        err_sys("socket error");

    /* ② 填充服务器地址：先清零，再设族、端口、IP */
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;              /* 地址族必须与 socket 一致 */
    servaddr.sin_port   = htons(13);            /* Daytime 标准服务端口 13；主机序→网络序 */
    /* argv[1]：用户给的 IP 字符串 → 二进制 sin_addr（网络字节序） */
    if (inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0)
        err_quit("inet_pton error for %s", argv[1]);

    /* ③ 主动打开：内核完成 TCP 三次握手；SA* 为 sockaddr 通用指针写法 */
    if (connect(sockfd, (SA *) &servaddr, sizeof(servaddr)) < 0)
        err_sys("connect error");

    /* ④ 读对端发来的 Daytime 文本（可能分多次到达）；返回 0 表示对端关闭（FIN） */
    while ((n = read(sockfd, recvline, MAXLINE)) > 0) {
        recvline[n] = 0;    /* 在末尾加 NUL，保证 fputs 按字符串输出 */
        if (fputs(recvline, stdout) == EOF)
            err_sys("fputs error");
    }
    if (n < 0)              /* while 因错误退出：如连接复位、EINTR 未重试等 */
        err_sys("read error");

    /* ⑤ 进程退出 → 内核关闭 sockfd，通常发 FIN；生产代码建议显式 close(sockfd) */
    exit(0);
}
