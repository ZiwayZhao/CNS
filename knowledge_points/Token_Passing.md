# 知识点复习：Token Passing (令牌传递)

## 📌 考频分析 (Testing Frequency)
- **考频评级**：**高频 (High Frequency)**
- **复习建议**：**纯背诵考点。特别是在 Quiz 和选择题中非常喜欢考它对应的四个特征标签。偶尔在期末中考它的优缺点简答。**
- **试卷覆盖情况**：
  - 经常出现在单选/多选题中 (Quiz 1 2022, Quiz 2 2017/2023)。
  - 在简答题中被用来对比 CSMA/CD 的随机性，要求陈述其工作原理 (Retake 2011, 2012, 2017)。

---

## 📚 考点核心与工作原理 (Core Concept & How it works)

Token Passing 是一种**受控接入 (Controlled access)** 协议，主要用来防止网络冲突，常见于曾经的 Token Ring (IEEE 802.5) 与光纤分布数据接口 FDDI 网络。

### 1. 核心理论机制 (The Mechanism)
**Question:** Explain the media access method Token Passing / Briefly describe the principle of token passing.
**Answer:** 
1. **Logical Ring (逻辑环结构)**: 主机们（Hosts）被连接成一个逻辑上的圆环（Logical ring topology）。
2. **Token Circulation (令牌传递)**: 一个特殊的控制帧叫做 “Token (令牌)” 在环中不断传递。
3. **Authorization to send (发送权限)**: 只有**当前手里拿着 Token** 的机器，才被允许发送数据。
4. **Forwarding (用完转交)**: 一次发送完成后，或者持有了一定时间后，这台机器必须把 Token 顺着环传给下一个。
📍 **出处 (Source):** *[retake_2017-solution_en.md; retake_2012-solution_en.md]*

---

## 🎯 Quiz 必考四大黄金定语 (The 4 Golden Rules for Quizzes)

在各类选择题（如 Quiz 1 2022, Quiz 2 2023）中，只要看到问 "Which statements about Token Passing are correct?"，立刻找以下几个标准答案：

1. **"Token Passing is a media access method."** (正确 ✅)
2. **"Token Passing forms a logical ring topology."** (正确 ✅)
3. **"Token Passing is a deterministic method (确定性方法)."** (正确 ✅)
   - *（核心考点：因为它像接力赛一样挨个传令牌，你能算出来最糟糕的情况下，你最多等多久就能拿到拿牌，保证了最大延迟时间。）*
4. **"A station may only send after it has forwarded the token."** (错误 ❌)
   - *（纯属钓鱼选项。事实恰好相反：机器是在**拿到 Token 没传给别人之前**才能发消息。发完消息/收到对方回复后，才把这个 Token 转交/重新丢回环里。一旦传走了就不能发了！）*
5. **"When using Token Passing, collisions can occur."** (错误 ❌)
   - *（它的核心就是 Controlled access / Collision prevention。全网只有一个人拿着喇叭，绝对不可能撞车。）*

---

## ⚖️ 优缺点与应用 (Advantages vs Disadvantages)

**Question (高频简明对比):** Justify or refute the claim that using token-passing as an access protocol results in transmission times in the local network being largely deterministic. (判定 Token passing 是否导致局域网传输时间大多是确定性的？)
**Answer:** **True (Justify).** 
- **CSMA/CD** (如 Ethernet) 是随机的竞争接入。碰撞可能发生任意多次，导致重传延迟完全是**不确定**的 (Non-deterministic)。
- **Token-passing** 保证了**无碰撞 (Collision-free)** 和 **公平 (Fair)**，每个节点最多等一圈就能轮到自己，因此它的延迟和传输时间是高度**确定性**的 (Deterministic)。
📍 **出处 (Source):** *[retake_2011-solution_en.md, Task 5d]*

### 总结优缺点 (背诵用)
- **优点 (Pros):**
  - **No collisions (无碰撞)**：不需要因为冲突而重传。
  - **Determinism (确定性)**：有可预期的最大延迟上限。
- **缺点 (Cons):**
  - **Token lost (丢失问题)**：如果转交中途 Token 电子消失了，整个网络停摆。必须选出一个 Monitor Station (监控站) 负责重新捏造一个 Token 出来。
  - **Selfish node (单点故障)**：如果拿到 Token 的机器死机了不往下传，大家一起死。
  - **Waiting delay (白费力气)**：就算网络空空如也，你想说话也得等 Token 慢慢转悠到你这儿，初始延迟比 CSMA 更高。
