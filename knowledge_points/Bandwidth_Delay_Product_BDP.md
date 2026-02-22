# 知识点复习：Bandwidth-Delay Product (带宽时延乘积 / BDP)

## 📌 考频分析 (Testing Frequency)
- **考频评级**：**中高频 (Medium-High Frequency)**
- **复习建议**：**极其好拿分的一道计算题/概念选择题。只需记住一个乘法公式！**
- **试卷覆盖情况**：
  - 常作为选择题出现考查概念或直接计算（例如 2019 年 Retake, 2020 年 Endterm）。
  - 在平时作业 (`tutorial04`) 中有完整的跨国海底光缆的物理意义计算。经常与 TCP 的窗口大小 (Window Size) 设计联系在一起。

---

## 📚 考点核心与物理意义 (Core Concept & Formula)

在 `slides_chap2.pdf` 和 `tutorial04` 中，专门定义了信道的“容量”或者“记忆量”。

### 1. 核心公式 (The Formula)
**BDP = Bandwidth $\times$ Propagation Delay** 
(带宽 $\times$ 传播延迟)
即：**$C = r \times t_p$**

*(注意：这里的延迟指的是单向传播延迟 $t_p = \frac{d}{v \cdot c_0}$，如果是讨论 TCP 确认机制通常会用 RTT（Round Trip Time，即往返延迟 = $2 \times t_p$），考试看清题目要求。普通 BDP 默认是单向延迟。)*

### 2. 物理意义 (The Physical Meaning)
**问：What does the bandwidth-delay product mean?**
**答：The bandwidth-delay product specifies the “amount of data stored” on the line, i.e., how many bits are serialized by the sender before the first bit reaches the receiver.**
*(它代表在特定传输方向上，同时“在飞行中” (in flight) 的数据量。你可以把它想象成一条水管，带宽 $r$ 是水管的粗细，延迟 $t_p$ 是水管的长度，BDP 就是这条水管里能装多少水。)*

---

## 🎯 考法分析与历年真题 (Past Questions & Answers)

### 题型 1：纯数字计算题 (The Direct Calculation)
**Question:** Given is a link with a bandwidth of 872 Mbit/s and a propagation delay of 96 ms. Determine the bandwidth-delay product.
**Answer:** 
$BDP = 872 \text{ Mbit/s} \times 96 \text{ ms}$
$BDP = 872 \times 10^6 \text{ bit/s} \times 96 \times 10^{-3} \text{ s} = 83,712,000 \text{ bit}$
转化为 Mbit 即为：**83.71 Mbit** （选项）。
📍 **出处 (Source):** *[endterm_2020-solution_en.md, Task 1e]*

💡 **中文解析与避坑**: 这是白送分题。唯一可能出错的地方是**单位换算**。
- `1 ms = 10^-3 s`
- `Mbit` 意思是 $10^6$ bit。
不要去乘 $1024$，在网络带宽计算中，k, M, G, T 统统都是 $10^3, 10^6, 10^9, 10^{12}$ 的十进制换算。

---

### 题型 2：跨过海底光缆的完整大题 (The Submarine Cable Problem)
**Question:** A submarine cable runs from Japan to the USA ($d = 10,000 \text{ km}$). Transmission rate is $r = 7.68 \text{ Tbit/s}$. The relative propagation speed of light in the fiber is $\nu = 2/3$ of $c_0$ ($3 \times 10^8 \text{ m/s}$). Determine the propagation delay, state the meaning of BDP, and calculate the BDP in Bytes.
**Answer:**

1. **传播延迟 (Propagation Delay $t_p$)**: 
   $t_p = \frac{d}{\nu c_0} = \frac{10,000,000 \text{ m}}{(2/3) \times 3 \times 10^8 \text{ m/s}} = 0.05 \text{ s} = 50 \text{ ms}$
2. **定义 (Meaning)**: 
   How many bits are serialized by the sender before the first bit reaches the receiver (The amount of data stored on the line).
3. **BDP 计算**: 
   $BDP = r \times t_p = 7.68 \times 10^{12} \text{ bit/s} \times 0.05 \text{ s} = 384 \times 10^9 \text{ bit} = 384 \text{ Gbit}$
   **换算成 Byte**: $384 \text{ Gbit} / 8 = 48 \text{ GB}$。
   📍 **出处 (Source):** *[tutorial04-solution.pdf, Problem 1]*

💡 **中文解析**: 这种题融合了光速的计算。记住光在光纤/铜缆中的速度通常是**真空光速的 2/3**。另外算出来的是 bit（比特），如果题目问的是 Byte（字节），记得除以 8。

---

### 题型 3：概念排除题 (Multiple Choice Concepts)
**Question (多选题陷阱):** The serialization time...
- [ ] can be determined from the bandwidth-delay product. *(False! 序列化时间 = 数据长度 / 带宽)*
- [ ] gives the necessary time for serializing a single bit. *(False! 通常指发完整个包的时间)*
- [x] is the quotient of frame length and data rate. *(True! $t_{serialize} = \frac{L}{r}$)*
📍 **出处 (Source):** *[retake_2019-solution_en.md, Task 6g]*

💡 **总结**: BDP 只跟**信道在空中所能容纳的最多数据量**相关，千万不要把 BDP 和包的发送时间（Serialization time）搞混。
