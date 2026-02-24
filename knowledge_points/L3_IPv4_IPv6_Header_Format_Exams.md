# 考点终极攻坚：IPv4 与 IPv6 头部格式 (Header Format) 历年真题提取与解析 📝

很多同学在复习 IP 头部时，面对那一堆 `Total Length`、`IHL`、`Checksum` 往往不知道考试到底怎么考。
根据我对历年（包含最新的 INHN0012 和老版 GRNVS）真题的深度扒轨，现在的这部分考点**已经摒弃了要求你手动画全表格的变态死记硬背**，全盘转向了**“概念辨析（多项选择题）”**和**“Wireshark/偏移量联动（计算题）”**。

这篇文档为你提取了原汁原味的历年真题，并且配上了“怎么避坑”的保姆级解析。

---

## 题型一：IPv4 vs IPv6 头部概念大辨析 (多项选择题常客)

这绝对是每一张期末考卷必出的 2 分送分题。教授极度喜欢把 IPv4 的特性安在 IPv6 头上，或者把 IPv6 的进化史作为正确选项。

### 🚨 真实考题提取库：判断以下选项对错 (True / False)

**1. 考点：校验和 (Checksum) 的断舍离**
> **[2018 Midterm / 2024 Endterm 变种]** 
> 🔘 *The IPv6 header contains a CRC32 checksum.*
> 🔘 *The IPv6 header contains a checksum over the payload.*

- **答案与解析**：**全错 (False)！** 
- **避坑心法**：IPv4 有 Header Checksum 面条，但 IPv6 为了追求极致的路由转发速度，**彻底砍掉了 L3 的任何 Checksum**！不管是查整个包的还是查头部的，IPv6 通通没有！查错的任务已经被扔给了数据链路层 (L2 MAC FCS) 和传输层 (L4 TCP/UDP)。

**2. 考点：地址长度与基本设计**
> **[日常 Quiz 库]**
> 🔘 *Source and Destination address are 128 bits long.*
> 🔘 *The basic IPv6 header has a fixed length of 40 bytes.*

- **答案与解析**：**全对 (True)！** 
- **避坑心法**：这两句话是 IPv6 最神圣的根基。IPv4 是 32 位地址加可变长度头部（通过 `IHL` 字段表示），而 IPv6 是 128 位超长地址，加上**绝对固定死板的 40 字节基础头部**。因为固定，所以路由器解析起来飞快。

**3. 考点：扩展头 (Extension Header) 与对齐原则**
> **[历年考点高频陷阱]**
> 🔘 *The IPv6 header including its extension header must always be a multiple of 8 B.*

- **答案与解析**：**对 (True)！** 
- **避坑心法**：虽然基础头固定是 40 字节，但 IPv6 可以挂“拖油瓶”（扩展头）。这里的绝对铁律是**“8字节对齐”**。如果加减出来的头部长度不是 8 的倍数，系统会强制塞入 `Padding` (填充 0) 把它撑大。

---

## 题型二：路由器到底能不能分片？(Fragmentation 机制必考)

这个知识点是这门课的灵魂。教授为了让你记住“IPv4 耗费路由器算力，IPv6 减负”，设计了极其经典的陷阱。

### 🚨 真实考题提取库：谁有资格拿刀切包？

> **[2024 INHN0012 Quiz 核心考点] / [2019 Midterm]**
> Which of the following statements about fragmentation are correct?
> 🔘 *IPv6 fragments can be further fragmented by routers.*
> 🔘 *IPv6 fragments are reassembled at intermediate routers.*
> 🔘 *IPv6 fragmentation is handled by the sending device, not intermediate routers.*

- **答案与解析**：**只有最后一个对 (True)！前两个大错特错！**
- **避坑心法**：
  - **在 IPv4 时代**，如果一个硕大的包卡在了门槛（MTU）前，**中间的路由器 (Intermediate routers)** 会一边骂娘一边负责把包切开送过去。
  - **在 IPv6 时代**，路由器大爷罢工了！任何 IPv6 路由器只要看到包大于 MTU，**当场丢弃 (Drop)**，并且向发件人扔回一个 ICMPv6 报错（Packet Too Big）。**只有包的源发送方 (Sender)** 才有资格在家里把包切好，带上 Fragment Header 发出来。
  - 至于重组（Reassembled）？无论是 v4 还是 v6，**只有最终收件人 (Destination)** 才会去拼图！半路上的路由器一概不管碎片。

---

## 题型三：Wireshark 追踪图与 MSS 防分片倒扣题 (硬核计算)

如果在这个考点想卡你，就会出一套“防分片”的大题。即：为了不被丢包，我的数据到底最高能塞多少？

### 🚨 真实考题提取库：计算安全载荷 (Maximum Segment Size)

> **[2015 Midterm / 真题衍生]**
> *Scenario: A user is connected via a PPPoE link with an MTU of 1492 Bytes. The user wants to send TCP segments over IPv4 without ANY fragmentation.*
> *Question: Show that the maximum segment size (MSS), so that no fragmentation is required, is 1452 bytes.*

- **解题流程 (倒扣心法)**：
  1. **找总承重限制 (MTU)**：题目给出最窄的独木桥 MTU = `1492 Bytes`。
  2. **扣除 L3 头部 (IPv4)**：IPv4 不带 Option 时，标准头部有多大？**20 Bytes**！
  3. **扣除 L4 头部 (TCP)**：TCP 的标准头部有多大？也是 **20 Bytes**！
  4. **算出最终净含量 (MSS)**：`1492 - 20 (IP头) - 20 (TCP头) = 1452 Bytes`。
- **满分答法**：写出算式 `MSS = MTU - IPv4_Header - TCP_Header` 即可！

*(注：如果这题换成 IPv6，你就要毫不犹豫地扣掉 **40 Bytes** 的基础头！)*

### 🚨 补充陷阱：什么字段在路上会变？(Header Fields)

> **[2017 Midterm]**
> *Which IP header fields change while packets get routed from one endpoint to another?*
> (数据包在路由器间跳转时，IP头里的哪些字段每次都会发生变化？) 

- **必背答案**：
  - 对于 **IPv4**：**`TTL`** (每跳减1) 和 **`Header Checksum`** (因为 TTL 变了，所以每次都要重算)。另外，如果真的发生了分片，`Total Length`, `MF`, `Fragment Offset` 也会在那一跳发生改变。
  - 对于 **IPv6**：由于没有 Checksum 了，所以只有 **`Hop Limit`** (也就是 v6 版的 TTL) 在每一跳转发时会减 1。

---

拿着这份题库总结，你在期末考试的 Multiple Choice 部分无论是看到 `Checksum` 还是看到 `Fragmentation handled by routers`，你都能直接在两秒内锁定答案，稳稳拿下分数！
