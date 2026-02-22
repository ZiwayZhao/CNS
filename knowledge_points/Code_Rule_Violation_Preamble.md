# 知识点复习：编码违例 (Code Rule Violation) 与 具体以太网成帧 (Preamble)

## 📌 考点 1：Code Rule Violation 真的考过吗？怎么考的？
**答案：绝对考过！而且是在近期考试中作为“成帧机制”的核心替代方案来考察的。**

在 **Endterm 2025 (最新考卷)** 的简答题中，教授直接出了一道送分(命)题：
**Question:** Name an alternative mechanism to control characters, how the beginning and end of a message can be signaled in line coding, and describe how this could be implemented.
*(说出一种替代控制字符的成帧机制，并描述如何实现它。)*

**Answer 满分标准答案:**
- **Mechanism (机制)**: **Code rule violation** (编码规则违例)
- **Description (描述/实现)**: Not returning to zero in a pulse (cf. NRZ) or sending a permanent invalid level. *(例如在带有跳变规则的编码中，故意不跳变，或者发送一个永远非法的电压电平。)*

此外，在 **Midterm 2019** 和 **Midterm 2023** 中，选择题也多次出现：
*题型：有哪些方法可以用来识别一帧的边界 (recognizing frame boundaries)？*
*正确选项必含：L3 header length, **code rule violation**, control characters (如 4B5B 提供的).*

**💡 总结：**
不要把它当做课外拓展。你只需要记住这个词（**Code rule violation**），知道它意味着底层曼彻斯特编码故意发错一个波形来充当边界，就可以拿到这几道题的满分。

---

## 📌 考点 2：以太网 (Ethernet) 的前导码 (Preamble) 与具体成帧例子会考吗？

你在 PPT 里肯定看到了 IEEE 802.3 (Ethernet) 的真实帧长得像这样：
`[Preamble] [SFD] [Destination MAC] [Source MAC] [Type] [Payload] [FCS]`

关于这种具体的协议字段，考卷的宽容度非常高：
1. **会不会考默写字段长度？**
   **极小概率！** 即使考了网络包结构的分析题 (Wireshark Hexdump 还原题)，试卷后方的 **Cheat Sheet** 都会完整把全套头部格式（包含字段和长度）印给你照着抄填。
   
2. **Preamble (前导码) 的核心考点是什么？**
   Preamble 是一长串连续跳变的 `10101010...` 信号。
   如果你在考试中被问到：**以太网的 Preamble 有什么作用？**
   **标准答案**：**Clock recovery / Synchronization (时钟恢复/物理层时钟同步)**。
   接收方的网卡刚通电睡醒，必须靠这串没用的前导码来把自己的频率调整到跟发送方一模一样，调整好了之后，紧接着看到一个 `SFD`（Start Frame Delimiter, 帧起始定界符，最后两位突然变成 `11`），网卡就知道可以开始正式接收数据了。

3. **你提到的 GIOF？**
   推测你看到的是 **GFP (Generic Framing Procedure)**，或者 WLAN 里面的 **PLCP (Physical Layer Convergence Procedure) Header**。
   考试中如果出现这类长串名字的非常见成帧协议，99% 的情况是作为背景信息。教授只会问你这些表皮底下的核心逻辑（即：它们是基于 Length specification，还是基于 Code Rule Violation？）。不要去死记硬背每个协议的开头叫什么名字，**记住底层的那 5 大心法分类**（见 Grand Summary）才是王道！
