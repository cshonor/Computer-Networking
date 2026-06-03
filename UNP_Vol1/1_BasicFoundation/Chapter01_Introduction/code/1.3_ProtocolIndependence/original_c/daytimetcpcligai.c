/*
 * UNP 卷1 · 协议无关 TCP Daytime 客户端（getaddrinfo 范式，Ch11 完整落地）
 * 节：1.3_ProtocolIndependence
 * 路径：code/1.3_ProtocolIndependence/original_c/daytimetcpcligai.c
 * 用法：daytimetcpcligai <主机名>   例：daytimetcpcligai localhost
 * 要点：不写死 AF_INET/AF_INET6；由 DNS 返回 addrinfo 链表，遍历 connect
 */
#include "unp.h"

int
main(int argc, char **argv)
{
    int                 err, sockfd, n;
    char                recvline[MAXLINE + 1];
    struct addrinfo     hints, *res, *rp;       /* hints：查询条件；res：结果链表头；rp：遍历指针 */

    if (argc != 2)
        err_quit("usage: daytimetcpcligai <hostname>");

    /* 清零 hints，只设置关心的字段；其余为 0 表示“由系统默认选择” */
    bzero(&hints, sizeof(struct addrinfo));
    hints.ai_family   = AF_UNSPEC;              /* 不限制 v4/v6，DNS 可返回双栈多条记录 */
    hints.ai_socktype = SOCK_STREAM;            /* 要 TCP；过滤掉 UDP 等其它套接字类型 */

    /* 服务名 "daytime" 走 /etc/services 或等价数据库 → 端口 13 */
    /* 成功：res 指向链表；失败：返回非 0，用 gai_strerror(err)，勿用 strerror(errno) */
    if ((err = getaddrinfo(argv[1], "daytime", &hints, &res)) != 0)
        err_quit("getaddrinfo error for %s: %s", argv[1], gai_strerror(err));

    /* 按优先级尝试链表中的每个地址（可能先 v6 后 v4，取决于系统/DNS） */
    for (rp = res; rp != NULL; rp = rp->ai_next) {
        /* 用解析结果里的族/类型/协议创建套接字，无需手写 sockaddr_in(6) */
        sockfd = socket(rp->ai_family, rp->ai_socktype, rp->ai_protocol);
        if (sockfd < 0)
            continue;   /* 例如本机未启用某协议族，试下一条 */

        /* ai_addr 已是通用 sockaddr*，长度用 ai_addrlen（勿 sizeof(sockaddr_in)） */
        if (connect(sockfd, rp->ai_addr, rp->ai_addrlen) == 0)
            break;      /* 连接成功，跳出 for；sockfd 即所用连接 */
        close(sockfd);  /* 本条地址失败（超时、拒绝等），关闭 fd 再试 ai_next */
    }
    if (rp == NULL)     /* 链表耗尽仍无成功 connect */
        err_quit("connect error");

    while ((n = read(sockfd, recvline, MAXLINE)) > 0) {
        recvline[n] = 0;
        if (fputs(recvline, stdout) == EOF)
            err_sys("fputs error");
    }
    if (n < 0)
        err_sys("read error");

    freeaddrinfo(res);  /* 释放 getaddrinfo 分配的链表；漏调会内存泄漏 */
    exit(0);
}
