# 知识点复习：Multiple Access / Multiplexing (多路复用与多址接入)

## 📌 考频分析 (Testing Frequency)
- **考频评级**：**极高频 (Very High Frequency)**
- **复习建议**：**必考简答题！重点背诵 CSMA/CD vs CSMA/CA 的区别，以及 4 种基础复用技术。**
- **试卷覆盖情况**：
  - 几乎每年期中或期末必考一题纯理论简答（通常值 4~8 分）。
  - 有时会结合 ALOHA 或 CSMA/CD 出简单的画图题或公式题（如 Tutorial 04）。

---

## 📚 知识点 1：四大基础 Multiplexing Methods
**Question:** Name four different multiplexing methods discussed in the lecture regarding media access control.
**Answer:**
1. **Time Division Multiplexing (TDM - 时分复用):** 根据时间划分，不同的设备在不同的时隙 (Time slots) 发送数据。
2. **Frequency Division Multiplexing (FDM - 频分复用):** 根据频率划分，不同的设备使用不会互相重叠的不同频率 (Frequencies)。
3. **Space Division Multiplexing (SDM - 空分复用):** 根据空间划分，使用不同的物理传输路径 (Transmission paths)。
4. **Code Division Multiplexing (CDM - 码分复用):** 根据正交码划分，给不同的通信伙伴分配不同的正交字母表 (Orthogonal alphabets)。
📍 **出处 (Source):** *[endterm_2022-solution_en.md; midterm_2016-solution_en.md]*

---

## 💥 知识点 2：CSMA 家族 (Carrier Sense Multiple Access)

### 2.1 纯 CSMA、CD 与 CA 的原理对比
1. **CSMA (Carrier Sense):** 
   先听后说 (Listen before talk)。发数据前先感受信道是否空闲。
2. **CSMA/CD (Collision Detection - 冲突检测 - 用于 Ethernet):**
   边听边说。如果发送过程中检测到冲突，**立刻中止发送**，并发送一个 **JAM signal (拥塞信号)** 通知所有人。随后等待一个随机时间再重传。
3. **CSMA/CA (Collision Avoidance - 冲突避免 - 用于 WLAN / 802.11):**
   无线网络中由于物理限制无法边听边说，因此采用**避免**策略。在发送前，强制等待一段随机时间 (Contention window)，即使信道是空的。

### 2.2 终极必考题：CSMA/CD vs CSMA/CA 区别与退避算法
**Question:** What is the essential difference between CSMA/CD and CSMA/CA?
**Answer (标准答案采分点):**
- **Collision Handling (核心区别):** CSMA/CD can detect collisions while transmitting and aborts. CSMA/CA cannot detect collisions and instead tries to avoid them by randomizing the transmission start (Contention window).
- **Acknowledgements:** CSMA/CA requires explicit Acknowledgements (ACKs) to confirm successful transmission, whereas CSMA/CD does not use ACKs (success is assumed if no collision is detected).
- **Minimum size:** CSMA/CA requires a minimum frame length (e.g., 64B contention phase).
📍 **出处 (Source):** *[endterm_2022-solution_en.md, Task 1d; midterm_2019-solution_en.md, Task 2j]*

**Question:** Why does CSMA/CD generally not work in wireless networks?
**Answer:** Because of the **"Hidden Station" problem**. The transmitter may be unable to detect a collision in every situation since nodes might be out of range of each other but both reach the same receiver.

**Question:** What is the Binary Exponential Backoff?
**Answer:** After a collision, stations wait a random number of slot times. This maximum waiting boundary is **doubled** (exponential) after every consecutive collision, reducing the probability of multiple stations picking the same random number again.

---

## 📡 知识点 3：ALOHA 协议家族深度解析 (ALOHA Deep Dive)

ALOHA 系列是最早的随机接入协议（夏威夷大学发明）。虽然原始考频不如 CSMA 高，但是在 **2013, 2014, 2015** 年度的真题以及 **Tutorial 04** 中，对其进行了深度的公式推导和图表分析。

### 3.1 Pure ALOHA vs Slotted ALOHA (纯与分槽的对比)
1. **Pure ALOHA (纯 ALOHA):** 想发就发。有数据立刻发送，如果不成功（没收到 ACK）就等随机时间重发。由于随时可能发包，发送窗口互相重叠的概率极大，导致效率极低。
2. **Slotted ALOHA (分槽 ALOHA):** 将时间划分为等长的离散时间槽 (Time slots)。设备**只能在每个时间槽的起点 (At the beginning of fixed time slots)** 开始发送。

### 3.2 历年真题：Slotted ALOHA 为什么更好？
**Question:** Justify why the throughput is higher in Slotted ALOHA compared to ALOHA.
**Answer:** In Slotted ALOHA, fewer collisions occur, as nodes only begin to send at specific times. The **interval within which two transmissions can overlap (vulnerable interval) is halved.**
*(中文解析：因为卡死了发送起点，包要么完全碰不到，要么百分百撞车，不存在“包的尾巴撞上别人包的头”这种部分重叠的情况，所以撞车概率减半，效率翻倍。)*
📍 **出处 (Source):** *[midterm_2013-solution_en.md, Task 2d]*

**Question的延伸:** What problems can arise when using Slotted ALOHA if the time slots are chosen to be very large compared to the message length?
**Answer:** Too large time slots compared to the message length result in high "waste". The slots are only occupied to a small extent, reducing throughput.
*(中文解析：时隙定得太大，发一个包用不完，剩下的时间全都干等着浪费掉了。)*
📍 **出处 (Source):** *[midterm_2013-solution_en.md, Task 2g]*

### 3.3 压轴计算题：ALOHA 的碰撞概率与发送概率推导
在 `tutorial04` 中，有一道关于 p-persistent Slotted ALOHA 的纯数学推导题（极其容易改头换面考出来）。
假设有 $n$ 个基站，每个基站每个时隙发送数据的概率是 $p$。

**Question 1 (成功率):** What is the probability that a collision-free transmission takes place in a time slot?
**Answer:** 如果要完全无碰撞，**必须只有 1 个基站发送，其他 $n-1$ 个基站都闭嘴**。这是一个二项分布 (Binomial Distribution)：
$P(\text{成功}) = \binom{n}{1} \times p^1 \times (1-p)^{n-1} = n \cdot p \cdot (1-p)^{n-1}$

**Question 2 (求极值):** Determine $p^*$ such that the probability of a collision-free transmission is maximized.
**Answer:** 对上面的成功率公式求关于 $p$ 的导数，令导数为 0 即可求出极值。
$\frac{\partial P}{\partial p} = 0 \implies p = \frac{1}{n}$
*(结论直接刻在DNA里：当发送概率 $p$ 等于 $1/n$ (站点总数的倒数) 时，ALOHA 网络的成功率达到理论最高。)*
📍 **出处 (Source):** *[tutorial04-solution.pdf, Problem 4]*

### 3.4 特殊应用：Framed Slotted ALOHA (RFID 中应用)
- 在考题中，如果提到 **RFID Tags** 和 Reader 之间的通信，使用的就是 Framed Slotted ALOHA (属于 TDM - Time Division Multiplexing 的一种应用)。
📍 **出处 (Source):** *[retake_2014-solution_en.md, Task 2]*

---

## 🧮 进阶公式陷阱：CSMA/CD 的极限距离 (Collision Detection Condition)
在 `tutorial04` 中有一道硬核计算题，必须要掌握这个物理硬核规则：

**Question:** What is the condition for CSMA/CD that a node can detect a collision in time?
**Answer:** The serialization time must be **at least twice** as long as the maximum possible propagation delay between the two most distant nodes ($t_s \ge 2 \times t_{p, max}$).
*(原因：最远的一个节点发出的干扰信号，必须在这个发送者把最后一滴数据挤出去之前，传回到发送者的耳朵里，这样发送者才知道发生了冲突。)*
计算公式推导：
$\frac{L_{min}}{r} \ge 2 \times \frac{d_{max}}{\nu \cdot c_0}$
由此可以算出以太网中两台电脑的最远距离 $d_{max}$。

---

### 总结
这块知识主要是背诵。务必精准写出四大 Multiplexing 的全称和解释，以及 CSMA/CD ("Ethernet, collision detection, jam signal") 对比 CSMA/CA ("Wireless/WLAN, collision avoidance, hidden station, ACK required, contention window") 的三大本质区别。
