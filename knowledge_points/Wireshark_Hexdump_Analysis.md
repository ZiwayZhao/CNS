# 知识点复习：Wireshark Hexdump 硬解码与报文构造 (INHN0012 专属必考)

## 📌 INHN0012 专属题型解析 (价值 16~20 分)
在传统的 IN0010 夏季考试中，教授只会让你画画网络拓扑。但在你的 **INHN0012 冬季考试（如 Endterm 2024/2025）** 中，**硬解码/构造报文 Hexdump** 是压轴级别的大题。

这道题通常会给你一个网络拓扑图，上面有所有设备的 IP 和 MAC 地址。然后给你一张满是十六进制 `0x` 空格的表格，让你**直接扮演计算机的网卡**，徒手把这串数据的每一个 Byte 填进去！

---

## 🎯 经典全真题：ARP Request 的手工构造
**场景还原 (基于 Endterm):**
一台 PC (`IP: 192.168.0.8`, `MAC: 04:7b:cb:b7:08:00`) 重启后，想要 SSH 连接到外网的一台服务器。它的默认网关/路由器是 R1 (`IP: 192.168.0.254`)。
**Question:** 因为刚重启，PC 的 ARP 缓存是空的。请填写它发出的第一个数据帧的 Hexdump。

**解题心法与填充步骤：**

### 第一步：明确要发什么包？
既然跨网段通信且不知道路由器的 MAC 地址，发出的第一个包必然是 **ARP Request (查路由器的 MAC)**。
*注意：ARP 工作在 Layer 2 之上，它没有 IP 报头，直接被封存在 Ethernet 帧里！*

### 第二步：构造 Layer 2 Ethernet Header (14 Bytes)
以太网帧头的标准格式 (考试 Cheat Sheet 会印给你)：`[DA (6B)] + [SA (6B)] + [EtherType (2B)]`

1. **DA (Destination MAC)**: 因为是 ARP 找人，所以必须是全网广播。填入全 F：
   👉 `ff ff ff ff ff ff`
2. **SA (Source MAC)**: 发送者 PC 的网卡物理地址。
   👉 `04 7b cb b7 08 00`
3. **EtherType (类型)**: 标志着 Payload 里装的是什么。IPv4 是 `08 00`，而我们这里装的是 ARP，必须填 ARP 专属代码（考场查表）：
   👉 `08 06`

*至此，前 14 个字节（第一行的 `0x00 ff ff ff...` 到 `08 06` 填完）。*

### 第三步：构造 ARP Payload (28 Bytes)
ARP 的报文结构非常机械化，对着试卷后的 Cheat Sheet 暴力填空：

1. **Hardware Type**: 以太网永远是 1。👉 `00 01`
2. **Protocol Type**: 我们用 ARP 查的是 IPv4。IPv4代码是 `08 00`。👉 `08 00`
3. **Hardware Length**: MAC地址长 6 Bytes。👉 `06`
4. **Protocol Length**: IPv4地址长 4 Bytes。👉 `04`
5. **Operation**: 这是一个请求 (Request = 1)，不是回复 (Reply = 2)。👉 `00 01`
6. **Sender HW Address**: 我的 MAC。👉 `04 7b cb b7 08 00`
7. **Sender Protocol Address**: 我的 IP `192.168.0.8`。（考试中允许直接写人类可读的数字，如 `192 168 00 08` 或者转 16 进制 `c0 a8 00 08`）。
8. **Target HW Address**: 我要找的目标 MAC。**我不知道，所以全填 0！** 👉 `00 00 00 00 00 00`
9. **Target Protocol Address**: 我要找谁的 MAC？我要找路由器 `192.168.0.254` 的！👉 `192 168 00 254`

### 第四步：FCS / 帧尾巴
一般题目会直接给出这 4 个 Bytes 的 CRC 校验和（例如告诉你 `FCS = 42 0a f1 73`），你只需要把它顺着写在 Payload 的最后面即可，同时在它下面标上一条竖线写上 `end of frame`。

---

## 避坑指南 (Survival Guide)
- **大坑 1：包类型的判断。** 当你看到主机第一次发包时，千万不要一上来就写 IPv4 (08 00) + TCP！一定是先发 **ARP (08 06)**！如果题目说“ARP 表已经有了”，再去构造真正的 IPv4 包。
- **大坑 2：Little / Big Endian。** 考试中如果没有要求，默认顺着写，但不要把 `0x0806` 拆错。
- **大坑 3：L3 Sender。** 如果是 ICMP Time Exceeded 的回包，注意 Source IP 往往是**导致丢包的那台路由器中途的接口 IP**，而不是最终的 Server IP。
