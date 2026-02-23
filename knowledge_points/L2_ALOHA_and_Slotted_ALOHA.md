# 知识点精讲：数据链路层 (L2) 纯 ALOHA 与分槽 ALOHA (Slotted ALOHA) 🛑

针对你的提问：“ALOHA 会考吗？”
**结论：在现代的 INHN0012 考试中，大题（计算题）考 ALOHA 的概率已经降到了【接近 0%】！** 它最新一次作为硬核大题出现，还是在 10 年前的 2014 年老课程 (GRNVS) 里。现在它最多只会在第一道 Multiple Choice (多选题) 里面作为一个**错误干扰选项**出现。

尽管如此，为了 100% 封死死角，如果你在选择题或简答题中撞到了它，只需要背下以下这几个核心逻辑：

---

## 考点一：Pure ALOHA (纯粹) 与 Slotted ALOHA (分槽) 的吞吐量对比

教授曾经在老试卷中多次问过这样一个英文简答题：
**真题重现 (Midterm 2013):** *Justify why the throughput is higher in Slotted ALOHA (为什么 Slotted ALOHA 的吞吐量/成功率更高？)*

**满分概念：**
- **Pure ALOHA (纯 ALOHA)**: 想发就发。只要两个包在时间上有哪怕 0.001 秒的重叠，这两个包就同时报废（Collision）。这种重叠的“危险期 (Vulnerable Period)”是两倍的包长。
- **Slotted ALOHA (分槽 ALOHA) 的杀手锏**: 它把时间强制切成了一个个的格子（Slot）。大家只能在格子的开头瞬间一起发。
- **满分作答词汇**: In Slotted ALOHA, fewer collisions occur, as nodes only begin to send at **specific times (the beginning of a slot)**. The interval within which two transmissions can overlap is therefore **only half as large (危险期减半)**.

## 考点二：Slotted ALOHA 的天然缺陷 (防坑简答题)

**真题重现:** *What problems can arise when using Slotted ALOHA if the time slots are chosen to be very large compared to the message length? (如果格子切得比实际的包裹大很多，会有什么问题？)*

**满分作答词汇**: High waste and reduced throughput! The slots are only occupied to a small extent, and **no transmissions can take place in the remaining time** (极度浪费信道利用率，因为发完之后剩下的空窗期没人能用)。

---

## 考点三：Framed Slotted ALOHA (高频老计算题：RFID 扫码模型)

RFID 门禁卡等经常使用“成帧分槽” ALOHA：把好几个槽 (Slots) 打包成一个帧 (Frame)。
假设有 $s$ 个空槽位，有 $n$ 个门禁卡想要发信号。每个人随机挑一个槽位。

1. **正好被读出的概率 (Discovery Slot, 即只有一个人挑了这个槽)**: 
   这就是经典的二项分布算式：$n$ 个人里面刚好挑出 1 个，别人都没挑它。
   $P(X=1) = n \times p \times (1-p)^{n-1}$ (其中 $p = \frac{1}{s}$)。
2. **极端情况思考题 (极端容易卡壳)**:
   - *如果 $n \gg s$ (门禁卡数量远大于槽位数) 会怎样？* $\implies$ 满分答案: 碰撞率极高 (High collision probability)，几乎没有读得出来的卡。
   - *如果 $n \ll s$ (槽位数远大于门禁卡) 会怎样？* $\implies$ 满分答案: 浪费带宽 (Wasted slots / The medium is not effectively utilized)。

---

## 总结
遇到 ALOHA 的题，不要慌，它的本质就是一个**靠纯碰运气**的介质访问协议，没有任何侦听（没有 Carrier Sense）。只要能答出 **"缩小危险期 (Reduce vulnerable period)"** 和 **"浪费槽位 (Wasted slots)"** 这两个踩分点，这部分的分你就稳拿！
