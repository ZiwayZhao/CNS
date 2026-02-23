# 知识点精讲：物理层 L1 的基带调制与信号频域分析 (Modulation & Signals) 📡

根据我们制定的《L1 终极考点地毯式搜查计划》，在清空了高频区（采样量化、信道编码、线路编码）之后，剩下的就是偏向于信号与系统理论的“概念背诵区”。

这部分在早年的 GRNVS 考试中会有一些画图题，但在现在的 INHN0012 中，它已经被极度压缩成了**纯粹的 1 分英语填空题**或**多项选择题**。你只需要记住以下几个“条件反射”级别的知识锚点！

---

## 考点一：数字调制技术 (Digital Modulation) 的四字真诀

数字调制就是如何通过改变正弦波的物理特征，把纯数字的 0 和 1 送上天线发射出去。考试必考这 4 种缩写的全称和物理意义。

**必背对应表（送分题专属）**：
1. **ASK (Amplitude Shift Keying - 振幅键控)**：只改变波的**高低/振幅 (Amplitude)**。
2. **FSK (Frequency Shift Keying - 频率键控)**：只改变波的**疏密/频率 (Frequency)**。
3. **PSK (Phase Shift Keying - 相位键控)**：只改变波的**起始位置/相位 (Phase)**。
4. **QAM (Quadrature Amplitude Modulation - 正交振幅调制) 【终极 Boss】**：
   - **真题重现**: *What does QAM modulate?* (QAM 调制了波的什么属性？)
   - **满分答案**: **Amplitude and Phase (同时改变振幅和相位)**。

*💡 防坑技巧：如果考你的识图题（比如给你一张星座图 Constellation Diagram），纯点都在一个圆圈上的必定是纯 PSK；点分布在横过来的水平线上的肯定是纯 ASK；点像围棋盘一样散布在整个直角坐标系里的，绝对是神级合体 QAM！*

---

## 考点二：Fourier (傅里叶) 级数与变换的概念游戏

别怕，计算机网络的课绝对不会考你手算傅里叶积分。但教授极度喜欢出一道有关傅里叶适用条件的 T/F 判错题。

**真题重现 (Endterm 2022 / Retake 2019 / Quiz 5 2017)**: 
*Which statements about Fourier series and Fourier transformations are correct?*

这里有一个所有上这门课的学生都会搞混，但你只要背下来就能秒杀的**十字交叉法则**：
- **Fourier Series (傅里叶级数)**: **只能用于周期信号！只能用于周期信号！(ONLY for Periodic signals)**。如果用来分析非周期信号，就是错的。
- **Fourier Transformation (傅里叶变换)**: **牛逼，通吃一切！(For both Periodic and Non-periodic / aperiodic signals)**。

**秒杀真题选项**：
- *Using Fourier transformation, the spectrum of periodic signals can be determined.* ✅ (变换能看周期)
- *Using Fourier transformation, the spectrum of non-periodic signals can be determined.* ✅ (变换也能看非周期)
- *Using Fourier series, the spectrum of periodic signals can be determined.* ✅ (级数只能看周期)
- *Using Fourier series, the spectrum of non-periodic signals can be determined.* ❌ (**看到这条直接划掉！级数不能看非周期信号！**)

如果遇到简答题：*Justify why a series expansion of $g(t)$ using Fourier series is not possible?* 
答案一句话：*Because $g(t)$ is not periodic, and Fourier series can only analyze periodic signals.*

---

## 考点三：Decibel (dB, 分贝) 的极简送分公式

物理层的极偶尔情况会让你计算信号在漫长电缆中衰减后的强度（信噪比）。这里没有任何复杂的对数解方程，只考你懂不具备背最基础的加法。

**核心考法（记住这个换算表）**：
- 功率每放大 **10 倍** $\implies +10 \text{ dB}$
- 功率每放大 **2 倍** $\implies +3 \text{ dB}$
- 如果考题问你 $1000$ 倍是多少？$\implies 10 \times 10 \times 10 \implies 10 + 10 + 10 = \mathbf{30 \text{ dB}}$。
- 若问你一半功率如何表示？$\implies -3 \text{ dB}$。

物理层 (L1) 所有能榨出分的知识点，到此彻底宣告结案！接下来，网络协议栈中真正的深水区——Layer 3 路由！
