/*
 * UNP 卷1 · 图 1-6 · TCP Daytime 客户端（IPv6 协议相关 / 硬编码）
 * 节：1.3_ProtocolIndependence
 * 路径：code/1.3_ProtocolIndependence/original_c/daytimetcpcli6.c
 * 用法：daytimetcpcli6 <IPv6地址>   例：daytimetcpcli6 ::1
 * 说明：相对 1.2 仅替换 AF_INET6 / sockaddr_in6 / sin6_*，仍无法双栈
 * 对照：1.2 daytimetcpcli.c · daytimetcpcligai.c（协议无关）
 */
#include "unp.h"

int
main(int argc, char **argv)
{
    int                  sockfd, n;
    char                 recvline[MAXLINE + 1];
    struct sockaddr_in6  servaddr;              /* IPv6 专用地址结构（另一套硬编码） */

    if (argc != 2)
        err_quit("usage: daytimetcpcli6 <IPaddress>");

    /* socket 族改为 AF_INET6；其余 TCP 语义与 IPv4 相同 */
    if ((sockfd = socket(AF_INET6, SOCK_STREAM, 0)) < 0)
        err_sys("socket error");

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin6_family = AF_INET6;            /* 必须与 socket(AF_INET6,...) 一致 */
    servaddr.sin6_port   = htons(13);           /* 端口号仍用 htons；与 IP 版本无关 */
    /* IPv6 文本地址（冒分十六进制）→ sin6_addr 128 位二进制 */
    if (inet_pton(AF_INET6, argv[1], &servaddr.sin6_addr) <= 0)
        err_quit("inet_pton error for %s", argv[1]);
    /* 链路本地地址常需 sin6_scope_id；本书 Daytime 示例未设置 */

    if (connect(sockfd, (SA *) &servaddr, sizeof(servaddr)) < 0)
        err_sys("connect error");

    while ((n = read(sockfd, recvline, MAXLINE)) > 0) {
        recvline[n] = 0;
        if (fputs(recvline, stdout) == EOF)
            err_sys("fputs error");
    }
    if (n < 0)
        err_sys("read error");

    exit(0);
}
