# 知识点精讲：以太网帧结构与 Wireshark 抓包实战 (Ethernet Frame & Hexdump) 🚀

在 INHN0012 考试中，关于以太网帧结构 (Ethernet Frame) 的考察极具实战性。教授不会只让你死记硬背各个字段的长度，而是会直接给你一段 **Wireshark/tcpdump 的十六进制 (Hexdump) 原始抓包数据**，让你在密密麻麻的数字中圈出指定的网络层信息。

这是一道必定出现的送分/送命题 (通常价值 15 分以上的综合大题)。如果你不了解以太网帧在抓包软件中的“隐藏规则”，你将在这道题上寸步难行。

---

## 一、 以太网帧的标准结构 (Ethernet II Frame)

一个完整的物理以太网帧在网线上跑的时候，包含以下字段 (按先后顺序)：

1. **Preamble (前导码 - 7 Bytes)**: `101010...` 交替，用于物理层时钟同步。
2. **SFD (Start of Frame Delimiter - 1 Byte)**: 值为 `10101011`，标志着帧的正式开始。
3. **Destination MAC (目的 MAC 地址 - 6 Bytes)**: 接收方的物理地址。
4. **Source MAC (源 MAC 地址 - 6 Bytes)**: 发送方的物理地址。
5. **Type / Length (类型/长度 - 2 Bytes)**:
   - 规定：如果值 $\ge 1536$ (也就是 `0x0600`)，代表这是 **Type (类型)** 字段，指明上层 (Layer 3) 协议类型。
   - 常见 Type 值 (必背):
     - `0x0800` = **IPv4**
     - `0x86DD` = **IPv6**
     - `0x0806` = **ARP**
6. **Payload (数据负载 - 46 ~ 1500 Bytes)**: 包含 L3 的 Header 和真正的用户数据。如果不足 46 字节，会进行 Padding (填充)。
7. **FCS (Frame Check Sequence - 4 Bytes)**: 也就是 CRC32 校验和，用于检错。

---

## 二、 ☠️ 抓包大题的终极陷阱：抓包软件隐藏了什么？

当你在考题上看到一堆形如 `0x0000 00 50 56 00 37 d1 ...` 的十六进制抓包数据时，**千万不要从前导码开始数！**

> **【考点防坑必读】**
> Wireshark 和操作系统的网卡驱动，在把以太网帧抓取上来显示给用户看时，**默认会剥离掉物理层的同步信息**。
> 1. **Preamble 和 SFD**：在 Hexdump 中**绝对看不到**！
> 2. **FCS (CRC校验和)**：大多数网卡在硬件层面验证完毕后就丢弃了，因此一般的 Hexdump 中也**没有 FCS** (除非题目如上方的真题一样，明确标注了 "including checksums")。

**实战破解口诀：Hexdump 的第 1 个字节，就是目的 MAC 地址的开始！**

---

## 三、 INHN0012 抓包大题实战破解步骤

假设题目给出了如下 Hexdump (本题取材自真题 Dump)：
```text
0x0000  00 50 56 00 37 d1 94 f7 ad 4f 08 00 86 dd 60 00
0x0010  ...
```
*(提示：`0x0000` 是行号偏移量，后面的双字母才是真实的数据)*

我们像剥洋葱一样，从左到右依次识别：

### 1. 找 Destination MAC (获取前 6 个 Byte)
- 跳过行首的 `0x0000`。
- 提取连续的 6 个字节：`00 50 56 00 37 d1`。
- **这就是接收方的 MAC 地址！**

### 2. 找 Source MAC (紧接着的 6 个 Byte)
- 紧接在目的 MAC 之后：`94 f7 ad 4f 08 00`。
- **这就是发送方 (Transmitter) 的 MAC 地址！**

### 3. 找 L3 Protocol Type (紧接着的 2 个 Byte)
- 这两个字节决定了上层到底是 IPv4 还是 IPv6！
- 提取：`86 dd` 
- 判断：`0x86DD` 代表它是 **IPv6**！(如果是 `08 00` 就是 IPv4)。

### 4. 寻找 Payload 与上层协议开头
- 自此，前 $6+6+2=14$ 个字节的以太网头部 (Ethernet Header) 结束。
- 紧接着的 `60 00` 开始，就是 **Layer 3 PDU (在这个例子中是 IPv6 Header)** 的起点。

---

## 四、 常见简答与填空题预判

除了直接让你在图上画圈圈，考试中还经常搭配以下小问：

1. **Why does an Ethernet frame require a minimum payload size of 46 bytes? (为什么以太网要求最小负载是46字节？)**
   - **Answer**: 为了满足 CSMA/CD 的冲突检测机制！最小帧长必须达到 64 Bytes (64 - 14头 - 4位FCS = 46 负载)，以便**发送方在发送完毕前能够听完一个完整的 RTT**，从而保证能检测到网络最远端的冲突 (Collision Detection)。*(现在虽然都是全双工交换机了，但为了向后兼容，这个规则被保留了下来)*。

2. **Given the Type field `0x0806`, what protocol is encapsulated? (Type 等于 0806 代表封装了什么？)**
   - **Answer**: ARP (Address Resolution Protocol)。

3. **In the hexdump, why can't we see the Preamble? (为什么抓包文件里看不到前导码？)**
   - **Answer**: 物理层前导码 (Preamble) 和帧起始定界符 (SFD) 仅用于物理层的硬件时钟同步。网卡 (NIC) 在接收帧并向上层 (OS/网络协议栈) 递交时，硬件会自动剥离这些纯物理层信息，因此抓包软件无法捕获到它们。

---

## 五、 💡 延伸考点：以太网帧结构的其他常见选择/简答题

除了直接抓包分析，以太网帧还在以下几个角度高频出题（尤其是 Multiple Choice 和 Short Answers）：

### 1. 广播地址与 MAC 识别
**真题再现**：*Which of the following are Ethernet broadcast addresses?*
- **坑点**：以太网的广播 MAC 地址是**全 1**的，写成十六进制必须是 `ff:ff:ff:ff:ff:ff`。
- 其他诸如 `00:00:00:00:00:00` 或 `bb:bb:bb:bb:bb:bb` 都是干扰项。

### 2. VLAN 标签带来的 4B Overhead (开销)
题目中有时会提到 "adds 4B overhead to the Ethernet header"。
- 正常的 Ethernet Header 是 14 Bytes (6 目的MAC + 6 源MAC + 2 Type)。
- 如果启用了 **802.1Q (VLAN 虚拟局域网)** 技术，会在源 MAC 和 Type 字段之间，**硬塞进去一个 4 Bytes 的 VLAN Tag**。
- 此时 Header 总长度会变成 18 Bytes。在抓包题里如果看到了 `0x8100`，说明它带了 VLAN 标签，真实的 Type 字段被往后挤了 4 个字节！

### 3. 以太网的 MTU (Maximum Transmission Unit) 界限
- 以太网规定了其 Payload 最大为 **1500 Bytes**。
- 这 1500 字节的上限，被称为链路的 **MTU**。
- **高频考点**：它限制了网络层 (Layer 3) 封装的最大包长度。如果一个 IPv4/IPv6 的包大于 1500 字节，它在进入以太网链路前就必须进行 **Fragmentation (分片)**！

### 4. MAC 地址的层级寻址性质
- **真题再现**：*Which of the following statements regarding Layer 2 addresses in IEEE-like protocols are true?*
- **必背正确选项**：
  1. 长度是 **6B long** (6个字节/48位)。
  2. 能够在物理层面上 **Uniquely identify a specific device** (唯一标识一个设备硬件)。
  3. **Compatible between different IEEE standard** (比如在 802.3 有线以太网 和 802.11 Wi-Fi 中，MAC 地址格式是通用兼容的)。
- **常见错误选项 (用来骗你上当的)**：
  - *Divided into network and host part* ❌ (这是 IP 地址的特征，MAC地址没有子网概念)
  - *Can be resolved over the Internet / Used for routing over the Internet* ❌ (MAC 只能在本地局域网 L2 跳跃，出了路由器就没用了，Internet 路由靠 IP)。

### 5. ⚠️ WLAN (802.11) 帧结构考法：为什么要有 3 个 MAC 地址？
很多同学纳闷为什么很难见到 WLAN 帧结构的 Wireshark 抓包大题？因为 802.11 的帧头太复杂了（各种控制标位），而且只要 Cheatsheet 上没有给出的帧结构，考试**绝对不会**让你直接分析十六进制抓包！

例如 WLAN 控制帧里的 **`To DS`** 和 **`From DS`** ( Distribution System 分发系统) 标志位，在历年考试中**从来没有作为单独的填空或选择题出现过**。但它是下面这道**必考理论简答题**的底层原因：

- **真题再现**: *Why are three MAC addresses usually used for IEEE 802.11 (WLAN), but only two MAC addresses for IEEE 802.3 (Ethernet)?*
  (为什么 WLAN 帧通常有 3 个 MAC 地址，而以太网只有 2 个？)
- **Answer (核心背诵版)**: 
  Because the **Access Point (AP) is NOT transparent** for WLAN clients, it must be explicitly addressed as an **intermediate station** between the sender and receiver. In contrast, Ethernet Switches are transparent to other devices.
  *(翻译/理解：正因为有了 `To DS` / `From DS` 这种非透明的基站转发机制，WLAN 帧才不能像以太网那样只写上发送方和接收方的 MAC。在 WLAN 基础架构模式下，必须显式地写上中间节点 AP 的 MAC 地址，所以通常需要 3 个（甚至在 WDS 桥接模式下需要 4 个）MAC 地址！)*
