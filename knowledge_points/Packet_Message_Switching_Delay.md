# 知识点复习：Packet & Message Switching (分组交换与报文交换的传输延迟计算)

## 📌 考频分析 (Testing Frequency)
- **考频评级**：**极高频核心考点 (Very High Frequency / Core Calculation)**
- **复习建议**：**必须掌握公式背后的物理意义，能熟练代入具体数字计算，并理解 Packet Switching 为什么更快**
- **试卷覆盖情况**：
  - 此类计算题在历年真题中频繁出现（如 `retake_2020`, `retake_2021`, `retake_2022`, `retake_2024` 等）。经常作为压轴计算大题（如 The Clacks 题目或卫星通信大题）的子题目。

---

## 📚 考点核心：Transmission Time Formula (传输时间公式解剖)

在 `slides_chap3.pdf` 的核心推导中，这两种交换模式的传输时间计算是重中之重。
*(假设：数据总量为 $L$ (Payload)，附加 Header 大小为 $L_h$。中间经过 $n$ 个中间节点 (hops/satellites/routers)。发送数据率/带宽为 $r$。传播距离为 $d$，信号传播速度为 $v_{C0}$。)*

### 1. Message Switching (报文交换)
**特点**：整个报文作为一个整体在网络中传输，必须**完全存储后再转发** (Store-and-Forward)。
**公式**：
$$ T_{MS} = (n + 1)\frac{L_h + L}{r} + \frac{d}{v_{c0}} $$
**公式物理意义拆解**：
- $(n+1)$：由于有 $n$ 个中间节点，所以总共有 $n+1$ 段链路需要完整发送一遍报文。
- $\frac{L_h + L}{r}$：报文在每一段链路上的发送时间（Serialization Time / 序列化时间）。
- $\frac{d}{v_{c0}}$：整体的信号传播延迟 (Propagation Delay)。

### 2. Packet Switching (分组交换)
**特点**：将大报文切分为多个大小上限为 $p_{max}$ 的数据包。各数据包可以**流水线式** (Pipeline) 传输。
**公式**：
$$ T_{PS} = \frac{1}{r} \left( \lceil \frac{L}{p_{max}} \rceil \cdot L_h + L \right) + \frac{d}{v_{c0}} + n \cdot L_h + \frac{p_{max}}{r} $$

> **💡 如果觉得原版公式难记，我们可以用“流水线图法 / 最后一包法”去理解和计算：**
> 在理想的分组交换中，我们追踪**最后一个数据包**的旅程。
> **总时间 = 所有包在源主机发完的时间 (Serialization at Source) + 传播延迟 + 最后一个包在中间节点因为存储转发导致的额外耽搁时间**

具体到真题里（比如 `retake_2021.md`），考官会直接让你解释公式中的 $T_{PS}$ 三部分的含义：
1. `(总包数 * L_h + L) / r` ：在源节点把所有包（及其Header）发出去的总发送时间 (Serialization time at the source)。
2. `d / v_c0` ：信号走完全程的传播延迟 (Propagation delay)。
3. `n * (L_h + p_{max}) / r` ：因为是流水线传输，前面包的延迟被掩盖了。只有**最后一个包**在 $n$ 个中间节点上的存储转发时间 (Serialization time at hops) 构成了额外的延迟。

---

## 🎯 考法与真题解析 (Past Questions & Answers)

### 题型 1：公式三部分的含义 (Conceptual Understanding)
**Question:** From the lecture, the expression is known for calculating the transmission time in packet switching. Briefly explain the three summands.
**Answer:**
1. Serialization time of all fragments/packets at the source including headers.
2. Propagation delay over the entire distance.
3. Serialization time of a single fragment/packet that occurs at intermediate hops.
📍 **出处 (Source):** *[retake_2021-solution_en.md, Task 2e]*
💡 **中文解析**: 必背概念题。如果考查公式的含义，答出这三点即可。重点是要提到第三部分只算**单包**在中间节点的发送时间。

---

### 题型 2：Message Switching 的序列化时间计算
**Question:** Calculate the serialization time in the case of message transmission. The message requires 48B and the data rate is 0.2 B/s.
**Answer:** $t = \frac{48\text{ B}}{0.2\text{ B/s}} = 240\text{ s}$. 
*(注：如果这里问的是从头到尾的序列化，且中间没有转发，就是单次发送时间。如果有多跳转发，请看后面的真题)*
📍 **出处 (Source):** *[retake_2022-solution_en.md, Task 4e]*

---

### 题型 3：Packet Switching 完整耗时计算大题 (The Pipeline Calculation)
**Question:** To reach the destination, a 48B message must pass through 3 intermediate Clacks (networks). Distance is $4 \times 12\text{km}$. Packet payload $p = 10\text{B}$, Header $L_h = 2\text{B}$.
Determine the transmission time if packet switching is used instead of message switching. 
**Answer:**
1. 分包数量：$N = \frac{48\text{B}}{10\text{B}} \rightarrow 5$ 个包。
2. 完整耗时 $T = \text{Source Serialization} + \text{Propagation} + \text{Delay at intermediate nodes}$
   - 在此题给定的公式解答为：$T = n(L + L_h + n(L + p)) / v_{c0}$ (这通常是一个特定场景的推导题)。但在标准答案给出的带入计算为：**总发送（5个头2B，数据48B）+ 3次中间节点转发延迟（每次转发 1个头2B+数据10B）** = $T = (5 \times 2\text{B} + 48\text{B}) + 3 \times (2\text{B} + 10\text{B})$ （注：这题简化了数据率 $r$ 为 1 的单位换算，重点在于时间叠加）。最终约为 470s。
📍 **出处 (Source):** *[retake_2022-solution_en.md, Task 4]*
💡 **中文解析与避坑指南**: 这是考试最容易失分的地方。在计算 Packet Switching 延迟时，请在草稿纸上画一下流水线。
- 你在**源主机**发送了 5 个包，总长度 $58\text{B}$。
- 在第一个路由器，它收完第一个 12B 的包后立刻发走，而不需要等后面那 4 个包。
- 最终的延迟 = **源主机发完所有包的时间 + (1包大小 $\times$ 中间路由器数量 $n$ ) / 发送速率。**

---

### 题型 4：优化/最小化传输时间 (Calculus Optimization)
**Question:** The transmission time of a message of length L divided into packets of size $p_{max}$ with header length $L_h$ over distance $d$ with $n$ hops and constant data rate $r$ is known. Determine the optimal packet size $p_{max}$ such that the transmission time is minimized.
*(假设 $L$ 是 $p_{max}$ 的整数倍, 即包的数量等于 $L/p_{max}$)*
📍 **出处 (Source):** *[retake_2020_en.md, Task 2]*

💡 **中文解析**: 
如果给你出这道题并要求推导最优包大小（通常是求导数），你应该将完整的 $T_{PS}$ 关于 $p_{max}$ 求偏导 $\frac{\partial T}{\partial p_{max}} = 0$。
- 把公式化简为关于 $p_{max}$ 的项：原公式中包含带 $p_{max}$ 的项为 $\frac{1}{r} (\frac{L}{p_{max}} L_h) + \frac{p_{max}}{r}$。
- 对 $p_{max}$ 求导：$-\frac{L \cdot L_h}{r \cdot p_{max}^2} + \frac{1}{r} = 0$
- 解出最优包大小：**$p_{max} = \sqrt{L \cdot L_h}$**
- *(这是非常容易拉开分差的一道数学推导题！)*

---

### 题型 5：为什么 Packet Switching 比 Message Switching 好？(The Advantage)
**Question:** Explain the advantage of packet switching over message switching.
**Answer:** It is generally faster because:
1. Not the entire message needs to be stored at each intermediate station, but only individual packets, allowing for faster transmission of the entire message (Lower serialization delays over multiple hops).
2. In case of errors, only one packet needs to be retransmitted instead of the entire message.
3. The packets can take different routes in the Internet, relieving individual routers.
📍 **出处 (Source):** *[retake_2022-solution_en.md, Task 4j & retake_2021-solution_en.md, Task 2d]*
💡 **中文解析**: 必背文字题。答出上面 3 点中的至少 1～2 点。最核心的一点就是**存储转发造成的延迟大幅降低** (pipeline 效应优势），其次是**出错只需重传一小段**的分治优势。
