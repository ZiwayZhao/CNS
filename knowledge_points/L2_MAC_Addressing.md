# 知识点复习：MAC 地址与 Layer 2 (数据链路层) 寻址核心考点

Layer 2 (L2) 寻址是历年 **Midterm 和 Endterm 必考的大题**。这部分看似简单，但教授非常喜欢在 **Hub vs Switch 的区别、冲突域的划分、以及 WLAN 与 Ethernet 的混组网** 中埋坑。

以下是提纯后的四大必考核心逻辑：

---

## 📌 考点 1：设备的 L2 透明性 (谁需要 MAC 地址？)
**经典真题:** *Do switches or hubs need a MAC address for their normal functions? (Switch 或 Hub 工作时需要 MAC 地址吗？)*

**满分答案: 不需要 (No)！**
- **Hub / Switch**: 它们工作在物理层或数据链路层，对于终端主机而言是**完全透明的 (transparent)**。它们只是负责转发别人的 Frame，**自己不会作为源或目的去收发数据**（除非为了远程管理，但那是另一回事）。
- **Router (路由器)**: **需要！** 路由器的每一个接口 (Interface) 都有自己独立的 MAC 地址和 IP 地址，因为它跨越了 L3。
- **Access Point (AP)**: **需要！** AP 它是无线和有线网络之间的桥接器，在无线的空气介质中，必须被当作一个实体的 Transmitter/Receiver 来寻址。

---

## 📌 考点 2：Hub vs Switch 的本质区别与冲突域 (Collision Domains)

每次给你一张网络拓扑图，让你画冲突域或填空时，牢记以下口诀：

| 设备类型            | 工作层级      | 处理逻辑                                                                                                                                                       | Collision Domains (冲突域)     | Broadcast Domains (广播域) |
| :------------------ | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------- | :------------------------- |
| **Hub (集线器)**    | L1 物理层     | 纯纯的复读机：从一个口进来的电信号，**原封不动地复制广播到所有其他端口**。                                                                                     | **N个端口 = 1 个巨大的冲突域** | 1 个                       |
| **Switch (交换机)** | L2 数据链路层 | 有脑子：内部有一张 **Switching Table (交换表)**。记住哪个端口连着哪个 MAC。收到包优先查表，只往目的端口发 (Unicast)。如果表里没有，才迫不得已广播 (Flooding)。 | **N个端口 = N 个隔离的冲突域** | 1 个                       |
| **Router (路由器)** | L3 网络层     | 隔离一切 L2 级别的喧嚣（如 ARP 广播请求绝对过不了路由器）。                                                                                                    | N 个                           | **N 个**                   |

**💡 高频选择题坑点:** *What security problem arises from using hubs?*
**答案:** Hub 存在严重的安全窃听漏洞 (eavesdropping)。因为 Hub 会把 PC1 发给 PC2 的包广播给所有人，同在一个 Hub 下的 PC3 可以用 Wireshark 轻松抓包偷看。

---

## 📌 考点 3：史诗级难点：WLAN (802.11) 与 Ethernet (802.3) 的 MAC 地址字段差异

**经典真题 (Midterm 2022, 2019, Endterm 2025):** 
*Why are usually three MAC addresses used in IEEE 802.11 (WLAN), but only two MAC addresses in IEEE 802.3 (Ethernet)?*

**底层逻辑剖析：**
在有线以太网 (Ethernet) 中，线缆是点对点或星型的，只需要 **Source Address (SA)** 和 **Destination Address (DA)** 就够了。
但在 WLAN 中（处于 Infrastructure 模式），所有的通信都必须**中转经过 Access Point (AP)**！空气是共享介质，你不仅要说明这个包**最终给谁**，还要说明此时此刻是**谁发进空气的、谁应该从空气里接住它**。

因此，WLAN 报文头部有多达 3 个（甚至 4 个）MAC 地址：
1. **SA (Source Address)**: 真正的起源发送者
2. **DA (Destination Address)**: 真正的最终接收者
3. **TA (Transmitter Address)**: 当前在空气中发出电磁波的设备
4. **RA (Receiver Address)**: 应当从空气中接收这段电磁波的设备

**🚀 终极杀手考题 (Endterm 2025 最新考点):**
**场景：** 有线的 `PC1` 要发数据给无线的 `Notebook_1`。中间隔着一个 `Switch` 和一个 `AP`。

1. **如果在 有线端 (Ethernet) 抓包：帧头写着谁的 MAC？**
   **答案:** 只有两个地址。`SA = PC1`，`DA = Notebook_1`。
   *(注意坑点：有线端的以太网帧里，永远填的是端到端的发送者和接受者。AP 在有线端扮演完全透明的网桥，PC1 根本不知道 AP 的存在！)*

2. **如果在 无线端 (空气中) 抓包（AP 发给 Notebook_1）：帧头写着谁的 MAC？**
   **答案:** 需要三个地址。
   - `TA (Transmitter)` = **AP** (当前是AP在空气中发信号)
   - `RA (Receiver)` = **Notebook_1** (笔记本在接收信号)
   - `SA (Source)` = **PC1** (真正的幕后黑手产生数据的起源)
   *(由于 DA 和 RA 都是 Notebook_1，所以在这里 RA 兼任了 DA 的角色，只用 3 个字段就够了)*

---

## 📌 考点 4：ARP 协议 (Address Resolution Protocol)
**考点归纳:**
- **作用:** 当你只知道目标的 IP 地址，却不知道它的 MAC 地址时使用（用来从 L3 地址映射到 L2 地址）。
- **流程:** 发送时，L2 的目的 MAC 必须填 **全F的广播地址 `ff:ff:ff:ff:ff:ff`**。同一网段内所有人都能收到，只有 IP 匹配的人才会回复带上自己的 MAC。
- **跨网段陷阱 (Retake 2012):** *If PC1 sends a packet to PC2 on a different subnet, does it need PC2's MAC address?*
  **答案：绝对不需要！(No)**。MAC 地址永远只在**同一个本地局域网（同一网段）内有效**。当你要发包给外网时，你查的是 **Default Gateway (默认网关/本地路由器)** 的 MAC 地址，把包扔给路由器，剩下的就不归你管了。
