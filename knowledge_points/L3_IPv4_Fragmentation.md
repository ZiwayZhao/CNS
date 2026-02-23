# 知识点精讲：IPv4 分片 (Fragmentation) 与 Fragment Offset 考法揭秘 ✂️

很多同学在复习网络层时，会被 IPv4 头部的 `Fragment Offset` (分片偏移) 及其相关的分片计算题吓倒。在你提出“期末会考吗”这个问题时，我深度交叉对比了老版 GRNVS 题库和近 3 年的 INHN0012 真题库，得出了一个非常明确的应试结论。

---

## 结论一：大规模的“计算分表”时代已经过去

在非常古老的考试中（比如 2012-2016 年），教授喜欢出那种占 20 分的压轴大题：给你一个 1200 Byte 的包和一个 580 Byte 的 MTU，让你画出所有 3 个碎片的 IP 头部表格，填入 `Identifier`、`MF (More Fragments)` 标志位和精确计算的 `Fragment Offset`。

**但是在近 3 年的 INHN0012 考试中，这种题型被完全抛弃了！** 
取而代之的是更加偏向实际工程抓包和概念理解的选择简答题。关于 Fragment Offset 你现在只需要掌握以下 3 个核心降维考点！

---

## 考点一：防坑！"Fragment Offset" 字段 vs 抓包大题里的 "Offset"

在现在的真题中看到 "Offset" 这个词，90% 的概率不是在考分片，而是在考**协议偏移量**！

**1. IP 头部里的 `Fragment Offset` 字段考法：**
- **真题重现**: *Which IP header fields change while packets get routed from one endpoint to another?* (数据包在路由器间传递时，IP 头里哪些字段一定会变？)
  - 选项里有 `Fragment Offset`，请**千万别选**！
  - 数据包在正常路由时，变化的只有 **`TTL`** (减1) 和 **`Header Checksum`** (因为 TTL 变了所以要重算)。除非题目明确说明在此跳发生了分片，否则 `Fragment Offset` 随大流是不变的。

**2. 抓包大题里的 `Offset` 考法 (极其高频！)：**
题干往往是：*Determine the offset where the L7 PDU starts.* (确定大图里应用层数据也就是 L7 PDU 开始的十六进制偏移量)。
- 这里的 Offset 是指从帧的第 0 个字节开始数，它出现在哪一行哪一列（比如 `0x0042` 行）。这和 IP 分片**毫无关系**！你需要通过识别 `IHL` 和 `Header Length` 来生数出来。

---

## 考点二：IPv4 与 IPv6 分片机制的骨血级差异 (必考！)

现在的考试极其喜欢考查你对网络演进的理解。既然 IPv4 的分片要在路由器上做，太消耗路由器 CPU 算力了，那么 IPv6 怎么改革的？

**真题必考点 (多项选择/简答)：**
- **IPv4**：允许**中间路由器 (Intermediate routers)** 在发现下个链路的 MTU 过小时，对数据包进行即时分片。
- **IPv6 (大改版)**：**绝对不允许**路由器对封包进行分片跳！(IPv6 fragmentation is handled by the sending device, not intermediate routers)。
  - 如果 IPv6 路由发现包太大了过不去怎么办？它会直接把包**丢弃 (Discard)**，然后向发送方回复一个 ICMPv6 报错（Packet Too Big）。让发送方自己切碎了重新发！
- **IPv6 的 Fragment Header**：既然只有发送方能分片，IPv6 把分片信息从主 IP 头里移除了。它变成了一个可选的扩展头 (Extension Header)，里面依然包含 `MF (More Fragments)` 标志位。

---

## 考点三：为了防止分片的 MSS (最大报文段) 计算

既然大家都不喜欢分片（尤其是 IPv6），那么考试就会反向发问：发送方应该把包的最大载荷 (MSS) 设置为多少，才能确保在路上绝对不会被分片？

**真题计算套路：**
- **Question**: *Show that the maximum segment size (MSS), so that no fragmentation is required, is 1440 B in this scenario.*
- **解法逻辑 (倒扣法)**：
  1. 假设题目给的网络中最窄的瓶颈链路限制（比如 PPPoE 链路）MTU 是 **1480 Bytes**。
  2. 这 1480 Bytes 必须容纳 IP 包里的所有东西。
  3. 扣掉 **IPv4 Header (默认 20 Bytes)**。
  4. 扣掉 **TCP Header (默认 20 Bytes)**。
  5. 剩下能装多少应用层纯纯的数据 (MSS)？ $1480 - 20 - 20 = \mathbf{1440 \text{ Bytes}}$。
- **公式**：`MSS = 路径最小 MTU - IP头大小 - L4传输层头大小`。只要应用层每次吐出的数据不超过 MSS，整个旅途就绝对不会触发任何分片！
