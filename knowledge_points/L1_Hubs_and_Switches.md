# 知识点精讲：集线器 (Hub) 的所有核心考点梳理 🖲️

在复习物理层和数据链路层时，集线器 (Hub) 作为一个极其古老的网络设备，依然是考试中频繁出现的“背景板”和“垫脚石”。

针对你的问题：“主动 (Active Hub) 和被动 (Passive Hub) 会考吗？”
**结论：在近 3 年的 INHN0012 考试大纲和真题中，从未单独考查过“主动集线器”与“被动集线器”的区别。** 这是非常古早的网络硬件分类知识了（主动 Hub 能放大信号，相当于中继器；被动 Hub 只做物理并联不需电源）。教授并不仅考查偏门硬件，而是考查它对**网络拓扑结构和冲突域**的影响！

因此，复习 Hub 的时候，你只需要死死拿捏住下面这 **3 个高频核心考点**：

---

## 考点一：Hub (集线器) 与 Switch (交换机) 的本质区别 (必考简答)

历年真题中极其喜欢问一道简答题：
**Problem**: *Briefly describe the main difference between a hub and a switch.* (简述 Hub 和 Switch 的主要区别)

**标准答案 (Standard Answer)**:
> - **Hubs** forward frames to **all ports** except the one via which the frame was received. (集线器像一个大喇叭，把从一个口收到的信号，无脑地广播复制到除了接收口以外的所有其他端口。)
> - **Switches** forward frames **via the specific port** to which the receiver is connected (if there is an entry in the switching table). (交换机会查 MAC 地址表，只把帧精准地转发给目标端口。)

**延伸理解**：
- Hub 是 **Layer 1 (物理层)** 设备。它不懂 MAC 地址，只认电信号 (0和1)。
- Switch 是 **Layer 2 (数据链路层)** 设备。它能解析以太网帧结构，看得懂目的 MAC 地址。

---

## 考点二：极其致命的 Collision Domain (冲突域) 计算

这是 Hub 在考试中最“恶心”人的地方，通常出现在看图数数题里：
- **真题形式**: 给一张复杂的拓扑图 (夹杂着 Router, Switch, Hub)，问你这图里有几个 Collision Domains 和 Broadcast Domains。

**对于 Hub 的铁律**：
- **Hub 绝对不能隔离/切分冲突域 (Collision Domain)。**
- 连接在一个 Hub 上面的所有连线、所有主机，**全部共用同一个大冲突域**！
- 如果有两台主机同时向一个 Hub 发送数据，Hub 就会产生物理上的电平叠加，导致 **Collision (冲突)**。所以连在 Hub 上的所有设备必须运行 CSMA/CD 协议。

**对比记忆**：
- Switch (交换机) 的每一个物理端口，都是一个**独立**的冲突域。

---

## 考点三：Broadcast Domain (广播域) 限制与透明性

- **透明性 (Transparency)**：
  - 真题有道多选题：*Both hubs and switches are transparent devices.* ✅**(这是正确的！)**
  - 对两端的 PC 来说，它们根本不知道中间有个 Hub 或者 Switch。这和 Router 还有 WLAN AP 是不一样的 (WLAN AP 不透明，需要显式指定 MAC)。
  
- **能不能切分广播域？**
  - **绝不能！** Hub 和 L2 Switch 都**不能**隔离 Broadcast Domain。
  - 只有 **Layer 3 的 Router (路由器)** 或者带有 **VLAN 功能的 Switch** 才能把网络切分成不同的广播域。
  - 如果连在一个 Hub 上的电脑发了一个全 `FF:FF:FF:FF:FF:FF` 的以太网帧，整个 Hub 以及和它连着的所有交换机上的电脑，全都能收到。

---

## 💡 考前速记防坑指南

1. **别背 Active/Passive**：如果在选择题里看到 Active Hub / Passive Hub 的高深概念，直接当做干扰项排除。
2. **看到 Hub 就画大圈**：遇到数 Collision Domain 的题，只要这几根线插在同一个 Hub 上，用笔把它们全部圈进同一个“大圈”里，这整个大圈只能算作 **1** 个冲突域！
3. **智商区别**：Hub 只有嘴巴没有脑子 (Layer 1，全网群发)；Switch 既有嘴巴又有脑子 (Layer 2，查表点对点转发)。
