# 知识点精讲：CSMA 的持续监听策略 (1-persistent vs Non-persistent) 🎧

针对你提出的问题：“CSMA中 persistent 的考法是？”

**一句话定心丸：和 ALOHA 的命运一样，这部分的计算与画图题在现在的真实 INHN0012 考卷中【完全绝迹】！** 
在整个题库中搜索 `persistent`，除了 2011 年的一套超级古老试卷中有一道让你画 `1-persistent CSMA/CD` 碰撞图的题目外，近十年的考试里从来没有出现过。

即便真的以极其变态的小概率在 Multiple Choice (选择题) 或者 1 分的简述题里考到了，你只需要掌握这 **3 种策略**在“有人正在说话 (Medium Busy)”时的真实生理反应即可秒杀。

---

## 考点：三种 CSMA 监听策略 (Media Access Control)

所谓的 `persistent` (持续性) 策略，核心是在解决一个问题：**当我想发消息，但我“插上耳朵听”的时候发现线路里正有人在说话，我接下来的策略该怎么定？**

### 策略 1：1-persistent (死心眼型 / 激进型) —— 以太网的基石
- **做法**: 如果听到线路正忙，它**绝不走开**，而是如同死心眼一样**一直死死盯着线路 (Listen continuously)**。
- **触发机制**: 等到线路空闲的那 0.0001 秒的一瞬间，它立刻以 **100% 的概率 ($p=1$)** 把自己的包撞出去。
- **致命缺点**: 如果同时有 2 个“死心眼”在旁边蹲守，只要线路一空，他俩同时 100% 冲出去，**必定发生连环车祸 (Guaranteed Collision)**。
- 💡 *补充：这也是为什么以太网在 CSMA 后面必须加一个 /CD (Collision Detection) 来兜底。*

### 策略 2：Non-persistent (佛系随缘型)
- **做法**: 如果听到线路正忙，它**立刻放弃监听**，转身去睡个随机长度的觉 (Wait a random time)。醒来后再重新听一听。
- **优点**: 极大地减少了“大家蹲在同一个终点线撞车”的概率 (Reduces collisions)。
- **致命缺点**: 当线路其实已经空闲下来时，它可能还在梦里，导致线路白白闲置 (Higher media idle time / lower utilization)。

### 策略 3：p-persistent (掷骰子型) —— 完美中庸
- **前提**: 必须在**分槽 (Slotted)** 的网络中使用。
- **做法**: 听到线路空闲时，它**不 100% 冲出去**，而是拿出一个骰子。以概率 $p$ 发送；以概率 $1-p$ 往后退让一个时间槽 (Defer to the next slot)。如果退让后线路又被人占了，就重新听。
- **优点**: 在保证较低碰撞率的前提下，又不会像佛系随缘型那样白白让人等太久。

---

## 终极防坑总结

考试如果问这三种有什么根本区别，你就记住以下中英对照词：
- **1-persistent**: 疯狂死守，空闲立马发 $\implies$ **High collision probability** (高拥堵碰撞)。
- **Non-persistent**: 忙就休眠随机时间 $\implies$ **High delay / Medium under-utilization** (高延迟，信道浪费)。
- **p-persistent**: 空闲掷骰子 $\implies$ 平衡了碰撞率和延迟。

搞定了这个角落里的灰尘知识点，咱们是不是可以向高分大乱斗的 **Layer 3 路由表机制 (Dijkstra vs Distance Vector)** 进发了？
