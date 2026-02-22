# 知识点精讲：WLAN Access Point (无线接入点, AP) 的考法归纳 📡

在复习 Layer 2 / 以太网衍生知识点时，WLAN (IEEE 802.11) 以及它的核心设备 —— **Access Point (AP)** 经常在考试的各个角落“客串”出现。

根据对历年 INHN0012 考题的穷搜，教授对 AP 的考核主要集中在以下 4 个“概念防坑点”上。不需要死记复杂的无线电原理，只要掌握以下这几个被反复拎出来当考点的逻辑即可！

---

## 考点一：WLAN 运行模式的选择 (高频多项选择)

AP 决定了整个无线网的组网模式。
- **真题重现**: *Which of the following are valid 802.11 operating modes?* (下列哪些是有效的 802.11 运行模式？)
- **必背正确答案**:
  1. **Infrastructure mode (基础架构模式)**：这是最常见的模式！所有的客户端 (手机/电脑) 都不直接互相通信，而是全部连到一个中心节点 —— 也就是 **Access Point (AP)**，由 AP 来统筹转发。
  2. **Ad-hoc mode (自组网模式)**：不需要 AP！设备和设备之间直接拉起网络进行点对点 (P2P) 通信。这种又叫 Independent Basic Service Set (IBSS)。
- **常见干扰错误选项**:
  - *MDF (Multi-Frequency-Drift) mode* ❌ (教授瞎编的名词)
  - *Multicast mode* ❌ (多播是一种传输方式，不是 WLAN 的组网运行模式)

---

## 考点二：AP 的“非透明性”与 3 个 MAC 地址 (必杀简答题)

这是和有线网 Switch 最大的对比差别，也是在论述题里考得最深的地方。

- **核心概念**：有线网的交换机 (Switch) 对主机是**透明的 (Transparent)**，发件人只用写目的 MAC。但无线的 AP **不是透明的 (Not transparent for WLAN clients)**！
- **真题重现**: *Why are three MAC addresses usually used for IEEE 802.11 (WLAN), but only two MAC addresses for IEEE 802.3 (Ethernet)?*
- **解答精要**：因为 AP 不透明，它必须作为一个**显式的中间跳 (Explicitly addressed as an intermediate station)** 存在于源端和目的端之间。所以一帧无线报文发出去，不仅要带上真正的源发件人和最终收件人，还要带上当前这步必须要路过的 AP 基站的 MAC 地址。

---

## 考点三：无线介质的防冲突机制 CSMA/CA (简答及多选)

AP 所处的无限介质由于具有“隐蔽终端 (Hidden Terminal)”等问题，导致无法像有线网一样“边听边发”，所以 AP 网络必须使用特殊的介质访问协议。

- **真题重现**: *Briefly describe the main difference between CSMA/CD and CSMA/CA.*
- **标准答案拆解**:
  - **CSMA/CD (Collision Detection)**：用于有线以太网。它是在发生冲突**之后**去检测并补救 (only does this after a collision has occurred)。
  - **CSMA/CA (Collision Avoidance)**：用于包含 AP 的无线网络。因为无法可靠检测冲突，所以它采取“避让”原则 —— **即使信道是空闲的，也要在发送前随机倒数等待一段时间 (Randomizes media access even when the medium is free / fixes contention window)**，试图主动避免冲突的发生。

---

## 考点四：拓扑图中的 IP 划分连坐网段 (综合大题)

在网络层 (Layer 3) 的综合拓扑大题里，AP 经常以图标的形式出现。
- **考点精要**：请牢记，**Access Point (AP) 本质上就是一个工作在 Layer 2 的无线 Hub/Switch 集群**！
- 如果题目给了一张图，两台电脑 `PC1` 和 `PC2` 同时连在同一个 `AP` 上，然后 `AP` 连在路由器 `R1` 的某个接口上。
- **防坑推论**：这说明 `PC1`、`PC2` 以及路由器的以太网口，**它们全部处在同一个 IP Subnet (同一个局域网子网) 里！** (因为 AP 不过是个无线的 L2 转发器，不会像路由器那样割裂网络段)。你在给它们分配 IP 地址的话，必须分配同一个网段内的不同主机号。
