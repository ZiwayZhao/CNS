# 知识点复习：4B5B 编码 (4B5B Encoding)

## 📌 考频分析 (Testing Frequency)
- **考频评级**：**中高频 (Medium-High Frequency)**
- **复习建议**：不要被表象蒙蔽！这个考点**绝对考过**，而且考得非常深。在 **Endterm 2023, Endterm 2018, Endterm 2011** 以及 **Quiz 2017** 中都作为独立大题或核心概念被考查。
- **核心盲点**：由于它经常和 MLT-3 物理层信号画图题绑在一起，很多人以为它不重要。实际上，教授极其喜欢用它来考察你对 "Line Code (线路编码)" 和 "Channel Code (信道编码)" 区别的深刻理解，以及数据率 (Data rate) 的换算。

---

## 📚 考点 1：4B5B 的根本目的 (有什么好处？)
**Question (简答题必备):** What is the purpose of the 4B5B code? / Name two advantages that the 4B5B encoding brings.
*(4B5B 编码的目的是什么？/ 它带来了哪两个优势？)*

**Answer 满分采分点 (结合 2023 与 2018 年答案):**
1. **时钟恢复 (Clock Recovery)**: 限制了连续 `0` 或连续 `1` 的最大长度。通过把 4个比特的输入映射成 5个比特的输出，它**保证了信号中有足够的跳变 (level changes)**，这让接收方可以很容易地从中提取并同步时钟。
   *(2018 原文: Limiting the maximum length of zero sequences allows for clock recovery.)*
2. **提供控制字符 (Providing Control Characters)**: 4 bits 只有 16 种组合，但 5 bits 有 32 种组合。这意味着有 16 种组合被空出来了！其中一些被用作特殊的控制字符（比如帧标界 Start/End delimiters, 例如 2023 考卷中的 `J/K` 符号表示开始，`T` 表示结束）。

### 🌟 终极联动：4B5B 与成帧 (Framing) / 控制字符 (Control Characters) 的绝妙配合
还记得我们在 L2 Framing 中讲到的 **代码透明性危机 (Code Transparency, 怕 Payload 里混入控制字符)** 吗？
HDLC 的作法是使用暴力而笨拙的 **Bit-stuffing (位填充)**，看到连续的 1 就强行塞 0。
而 **4B5B 提供了一种降维打击的解法！**

当你使用了 4B5B 编码后，**你根本就不需要 Bit-stuffing 了**！
为什么？
- 我们规定用来标定一帧边界的控制密码，比如 `J` (`11000`) 和 `K` (`10001`)。
- 用户传输的任意正常数据（Data），不管是几万个 `0` 还是 `1`，在通过 4B5B 表被映射为 5-bit 代码时，**永远不会被映射成 `11000` 或 `10001`** (因为这些密码专属给 Control Character 使用了，不包含在那 16 个有效数据映射之中)。
- 因此，用户真正的 Payload 数据流无论怎么排列组合，它的 5-bit 编码结果都**绝对不可能**意外拼凑出控制字符。代码透明性危机被从根源上物理消灭了！

📍 **出处 (Source):** *[slides_chap2.pdf, Page 56: "What if control characters occur randomly in the payload data? In the case of the 4B5B code, this cannot happen."]*

---

## 💥 考点 2：它到底是 Line Code 还是 Channel Code？(神级辨析)
这是 **Endterm 2023** 的压轴简答辨析，极易踩坑！

**Question:** Justify whether the 4B5B code is a channel code or a line code. / Can transmission errors be corrected using 4B5B?
*(判断 4B5B 是信道编码还是线路编码。/ 4B5B 能纠正传输错误吗？)*

**Answer 核心逻辑:**
4B5B 严格来说两者都不是（它是一个 Block code），但在文献中通常被归类为 **Line Code (线路编码)**。
- **为什么不是 Channel Code (信道编码)？**
  信道编码的作用是“加入结构化的冗余度以便进行错误检测和纠正 (error detection and correction)”。**4B5B 绝对不能用来纠正错误 (cannot be corrected)！** 它产生的多余比特只是为了凑出控制字符和保证时钟跳变，不具备任何数学检错能力。
- **它和真正 Line Code (如 MLT-3, 曼彻斯特) 的关系：**
  真正的线路编码负责把比特映射成真实的物理电压信号。4B5B 虽然自己不直接产生电压，但它通过打破连续 `0`，使得后续的 MLT-3 编码能成功实现时钟恢复，因此通常归在 Line Code 章节。

📍 **出处 (Source):** *[endterm_2023-solution_en.md Q6.f, endterm_2011-solution_en.md Q1.l]*

---

## 🧮 考点 3：物理层速率换算计算题 (Data Rate Calculation)

当 4B5B 加入战场时，网络线缆里真实传输的比特比你实际“想要”传输的数据要多。每 4bit 净数据，要在网线上发 5bit。这就是 **25% 的物理层开销 (Overhead)**。

**Question (2018, 2011 计算预警):** What must the bit rate actually be at 100BASE-TX to achieve an effective transmission speed of 100 Mbit/s?
*(在 100BASE-TX 中，为了达到 100 Mbit/s 的有效(净)传输速度，底层的实际比特率必须是多少？)*

**Answer 计算公式:**
$$ r_{gross} = \frac{r_{net}}{(4/5)} = r_{net} \times 1.25 $$
$$ r_{gross} = 100 \text{ Mbit/s} \times 1.25 = \mathbf{125 \text{ Mbit/s}} $$

这个 125 Mbit/s 就是线缆上真实的脉冲发送频率 (Baud rate 相关)，非常经典的计算陷阱。

---
**复习小贴士：**考试时如果遇到题目给了一串 `0` 和 `1`，让你查表进行 4B5B 转换（Table 6.1），纯送分题。但一定要记住，**4B5B 的本质是为了保命（时钟同步）和发号施令（控制字符），绝不能防弹（错误纠正）。**
