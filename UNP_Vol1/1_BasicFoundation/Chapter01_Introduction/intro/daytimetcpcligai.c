/*
 * intro/daytimetcpcligai.c — 协议无关 TCP 时间客户端（getaddrinfo 范式）
 * 对照 daytimetcpcli.c / daytimetcpcli6.c；完整封装见 Ch11 Host_serv / tcp_connect
 * 编译需 unp.h / libunp
 */
#include "unp.h"

int
main(int argc, char **argv)
{
    int                 err, sockfd, n;
    char                recvline[MAXLINE + 1];
    struct addrinfo     hints, *res, *rp;

    if (argc != 2)
        err_quit("usage: daytimetcpcligai <hostname>");

    bzero(&hints, sizeof(struct addrinfo));
    hints.ai_family   = AF_UNSPEC;      /* IPv4 or IPv6 */
    hints.ai_socktype = SOCK_STREAM;

    if ((err = getaddrinfo(argv[1], "daytime", &hints, &res)) != 0)
        err_quit("getaddrinfo error for %s: %s", argv[1], gai_strerror(err));

    for (rp = res; rp != NULL; rp = rp->ai_next) {
        sockfd = socket(rp->ai_family, rp->ai_socktype, rp->ai_protocol);
        if (sockfd < 0)
            continue;   /* error, try next address */
        if (connect(sockfd, rp->ai_addr, rp->ai_addrlen) == 0)
            break;      /* success */
        close(sockfd);
    }
    if (rp == NULL)
        err_quit("connect error");

    while ((n = read(sockfd, recvline, MAXLINE)) > 0) {
        recvline[n] = 0;
        if (fputs(recvline, stdout) == EOF)
            err_sys("fputs error");
    }
    if (n < 0)
        err_sys("read error");

    freeaddrinfo(res);
    exit(0);
}
