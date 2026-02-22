# 知识点复习：CSMA/CD (Carrier Sense Multiple Access with Collision Detection)

## 📌 考频分析 (Testing Frequency)
- **考频评级**：**极高频 (Very High Frequency)**
- **复习建议**：**必考知识点！主要以两类题型出现：1. 理论简答题（对比 CSMA/CA）；2. 物理极限计算题（算网线最大长度）。**
- **试卷覆盖情况**：
  - 理论简答题常客 (Endterm 2015, 2022; Midterm 2016, 2019, 2020)。
  - 高难度物理硬核计算见于 `tutorial04`。

---

## 📚 考点 1：机制原理与核心特征 (The Mechanism)

CSMA/CD 是**有线以太网 (Ethernet)** 最核心的早期灵魂协议。

### 工作流程：
1. **Listen before talk (先听后发)**：发包前先感知信道是否空闲。
2. **Listen while talking (边发边听)**：这与无线网不同，有线网卡**可以一边发送数据，一边检测线缆上的电压变化**，从而瞬间发现冲突。
3. **Collision Detection & JAM Signal (碰撞检测与拥塞信号)**：
   - 只要检测到冲突，立刻停止发送正常数据。
   - **立刻发送一小段 JAM 信号**。作用是确保网络上**所有人**（哪怕是最远端的机器）都能明确知道发生了碰撞并丢弃当前碎片。
4. **Resend after Backoff (退避重传)**：使用 BEB (Binary Exponential Backoff) 算法，等待一个随机时间后再试。对于 CSMA/CD 而言，**只有发生了碰撞之后才会触发退避倒数**（没碰撞时只要信道空闲就直接发）。

### 考点问答：
**Question:** How are successful transmissions recognized for CSMA/CD with Ethernet?
**Answer:** A transmission is assumed to be successful **if no collision was detected** during the transmission or no JAM signal was received. *(CSMA/CD 绝对不使用 ACK 确认包，没听到车祸声音就默认货物送达！)*
📍 **出处 (Source):** *[tutorial04-solution.pdf, Problem 3g]*

---

## 💥 考点 2：终极必考大题：CSMA/CD vs CSMA/CA

这是期中期末的拿分重地。

**Question:** What is the essential difference between CSMA/CD and CSMA/CA?
**Answer (标准答案得分点):**
1. **Collision Handling (碰撞处理，最核心)**：
   - CSMA/CD detects collisions while transmitting and aborts. 
   - CSMA/CA cannot reliably detect collisions (because of the Hidden Station problem in wireless), so it tries to **avoid** them.
2. **Acknowledgements (是否使用确认包)**：
   - CSMA/CA 强制要求接收方发送 **ACK (确认包)**。
   - CSMA/CD **不需要 ACK**。
3. **Random Backoff (退避时机的不同)**：
   - CSMA/CD 只有在发生了碰撞之后才去摇号等待 (Randomizes only after a collision)。
   - CSMA/CA 哪怕信道本来就是空的，也**必须**先强制执行一段随机等待 (Contention window)，防患于未然。
📍 **出处 (Source):** *[endterm_2022-solution_en.md; midterm_2019-solution_en.md]*

**Question的延伸:** Why does CSMA/CD generally not work in wireless networks?
**Answer:** Because of the **"Hidden Station" problem**. (发送方可能听不见另一个发送方的声音，导致他以为没碰撞，但接收方那里已经撞车了；加上无线设备无法一边大功率发送、一边听微弱的回音，无法实现物理上的 Collision Detection)。

---

## 🧮 考点 3：物理极限公式推导与经典画图题 (Tutorial 04 核心全解)

在 `tutorial04` 的 Problem 3 中，通过一道极其经典的综合题，完美揭示了 CSMA/CD 为什么需要那个该死的物理极限公式，这也是考试最爱的考点组合。

### 3.1 碰撞是谁检测的？如何判定发送成功？(重点解答)

**针对疑惑 1：碰撞是发送方检测还是接收方检测？为何成功条件是 "OR"？**
- **只能由且必须由“发送方 (Sender)”检测**。在以太网网线中，发送方会在自己往线上灌入数据的同时，监听线缆上的实际电压。如果发现实际电压和自己发出去的电压不一致（比如别人也发了高电平导致叠加爆表），发送方自己就能立刻知道“撞车了”。
- 至于那个让人生疑的定义：“*A transmission is assumed to be successful if no collision was detected during the transmission or no JAM signal was received.*”
  这里其实是一个语言翻译的逻辑陷阱 (德语 `keine Kollision ... oder kein JAM` 实质上表达的是 `Neither ... Nor`)。正确理解是**绝对的并列且缺一不可 (AND)** 的否定：
  如果在发送完成的这一刻为止，**你自己的网卡没有检测到本地电压异常 (No collision detected locally)**，并且你也**没有收到远端其他任何人丢过来的 JAM 骂街拥塞信号 (No JAM received)**，你才敢相信你的货送到了。只要发生其中任意一个，就是失败。

### 3.2 经典真题重现：CSMA/CD 的血泪教训 (Tutorial 04 Problem 3)
题目给定了三个主机 (PC1, 2, 3) 连在一根线上。相距很远，带宽 $100\text{ Mbps}$，发包仅有 $94\text{ Bytes}$。
- PC1 在 $5\text{ }\mu\text{s}$ 起跑发包。发送这个小包只需要 $t_s = 7.52\text{ }\mu\text{s}$，所以 PC1 会在 $12.52\text{ }\mu\text{s}$ 的时候完工。
- PC3 在 $10\text{ }\mu\text{s}$ 的时候以为没车（因为 PC1 的光速信号要走 $7.5\text{ }\mu\text{s}$ 才能到 PC3，也就是 $12.5\text{ }\mu\text{s}$ 才到），所以 PC3 也起跑了。
- 在 $12.5\text{ }\mu\text{s}$ 时，PC1 的信号狠狠撞上了刚刚起步的 PC3！PC3 发现了碰撞，立刻停止发送，并大喊了一声 JAM 信号。

**核心惨案（Why CSMA/CD fails here）：**
- PC3 发出的 JAM 信号，还得花 $7.5\text{ }\mu\text{s}$ 的路程才能传回 PC1，也就是在 $20\text{ }\mu\text{s}$ 才能抵达 PC1 的耳朵里。
- 但是，PC1 的包特别小，早在 $12.52\text{ }\mu\text{s}$ 就**已经发送完毕了**！
- PC1 发完包之后，拍拍屁股下班了（它没在发送期听到本地碰撞，也没在没发完之前听到 JAM）。于是，**PC1 误以为自己发送成功了，根本不会去退避重传！** 这就是系统发生致命逻辑错误的根源。

### 3.3 拯救系统的极限公式规则 (Collision Detection Condition)

为了避免上述悲剧（包发得太快，导致碰撞报警信号送回来时自己已经下班了），协议做出了死规定：

**Question:** What is the condition for CSMA/CD that a node can detect a collision in time?
**Answer:** The **serialization time (发送时间 $t_s$)** must be **at least twice** as long as the maximum possible **propagation delay ($t_{p,max}$)** between the two most distant nodes.

✅ **必背大招公式：$$t_s \ge 2 \times t_{p, max}$$**

这个公式的物理意义就是：**最远端传回来的“车祸报警声 (JAM)”，必须赶在你把最后一滴数据挤出去下班之前，传回到你的耳朵里！**

公式展开如下：
$$ \frac{L_{min}}{r} \ge 2 \times \frac{d_{max}}{\nu \cdot c_0} $$
*(最小帧长 / 带宽 $\ge 2 \times$ 最大距离 / 实际光速)*

考场上，根据这个公式，要么让你求网线能拉多长 ($d_{max}$)，要么让你求以太网规定必须用 0 垫到多大字节以上的最小帧长 ($L_{min}$)。这一套组合拳是历年大题的宠儿。

📍 **出处 (Source):** *[tutorial04-solution.pdf, Problem 3 a-g 全系列]*
