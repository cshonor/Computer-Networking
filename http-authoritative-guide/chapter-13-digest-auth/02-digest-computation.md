# 13.2 摘要的计算

> 本章：[chapter-summary.md](./chapter-summary.md#ch13-2) · [13.3 qop](./03-qop-quality.md)

## 本节核心目标

掌握 Digest 公式中的 **H/KD、A1、A2、qop** 及预授权、对称认证。

---

<a id="ch13-2-components"></a>

## 13.2.1 输入组成

| 块 | 含义 |
|----|------|
| **H(d)、KD(s,d)** | 散列与「密钥+数据」组合函数 |
| **A1** | **安全**相关：用户、realm、密码、nonce… |
| **A2** | **报文**相关：方法、URI（及可选 body 哈希） |

---

<a id="ch13-2-h-kd"></a>

## 13.2.2 H 与 KD（RFC 2617）

```text
H(<data>) = MD5(<data>)
KD(<secret>, <data>) = H(concatenate(<secret>:<data>))
```

常见算法名：**MD5**、**MD5-sess**。

---

<a id="ch13-2-a1"></a>

## 13.2.3 A1（安全数据）

| 算法 | A1 |
|------|-----|
| **MD5** | `<user>:<realm>:<password>` |
| **MD5-sess** | `MD5(<user>:<realm>:<password>):<nonce>:<cnonce>` |

---

<a id="ch13-2-a2"></a>

## 13.2.4 A2（报文数据）

| qop | A2 |
|-----|-----|
| **`auth`**（默认） | `<method>:<uri>` |
| **`auth-int`** | `<method>:<uri>:H(<entity-body>)` |

防方法/URI（及 body）被篡改。

---

<a id="ch13-2-formula"></a>

## 13.2.5 总公式（qop=auth / auth-int）

```text
response = KD( H(A1), <nonce>:<nc>:<cnonce>:<qop>:H(A2) )
```

- **`nc`**：nonce 计数  
- **`cnonce`**：客户端随机数 → 防选择明文攻击  

---

<a id="ch13-2-preauth"></a>

## 13.2.6–13.2.7 会话与预授权

为少一轮 401，客户端可**预知下一 nonce** 直接带 `Authorization`：

- 服务器在 **`Authentication-Info`** 的 **`nextnonce`** 下发  
- 或短时间**重用**同一 nonce  

---

<a id="ch13-2-nonce"></a>

## 13.2.8 随机数选择

推荐 nonce 含时间戳、ETag、服务器私钥等，**限制有效期**，防对已更新资源的重放。

---

<a id="ch13-2-symmetric"></a>

## 13.2.9 对称认证

客户端也可验证**服务器**：服务器在 `Authentication-Info` 回 **`rspauth`**，客户端核对响应摘要，防**假服务器**。

---

## 抓包/实操记录

（待填：对照 Authorization 里 response= 字段）

---

## 疑问与总结

**背结构：A1 管身份，A2 管这条请求，KD 把它们绑进 nonce。**
