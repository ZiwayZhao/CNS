# 知识点精讲：网络层 (L3) RIP 协议与 19分真题终极拆解 (含 Exercise 8 溯源) 🌪️

“RIP的整理当中为什么你没有把原题的每一个细节都总结出来... 题目也没找全？”

你的批评非常正确，也非常及时！在期末考试中，直接丢掉任何一个特定小题的语境，都是对复习的极其不负责任。因为 **INHN0012 的 2024 Endterm Problem 5 (Dynamic Routing, 19 credits)** 这道压轴题，实际上就是对平时作业 **`Tutorial 08 (Exercise 8)`** 的一次“连环魔改考察”！

为了让你在考场上遇到这 19 分时能“条件反射”般地写出满分答案，我这次重新扒出了这套试卷的**全部 11 个连环子问题 (a 到 k)**，并将它们与 Exercise 8 的推盘逻辑逐一对应，为你带来逐字逐句的**“保姆级真题精讲”**。

这 19 分的题看似吓人，但它其实是一场**填图游戏 + 默写填空**。请严格按照以下步骤拿下满分：

---

## 第一阶段：送分连击 (纯概念默写) 
题目直接以快问快答起手，这里总共 7 个小题 (a - g)，几乎白送一半的分数！

**a)* Which metric is used by RIP? (不用解释)**
- **满分答案**：`Hop Count` (跳数)。

**b)* RIP is a distance vector protocol. Explain the difference to link state protocols.**
- **核心踩分点**：一定要强调 RIP 没有全景图，只有邻居情报。
- **满分答案**：`The routers only know the next hop and distance for a destination, while link state protocols have a detailed view of the network (or parts of it).`

**c)* RIP is an interior gateway protocol. Explain the difference to exterior gateway protocols.**
- **核心踩分点**：还记得我们上节课总结的 AS (自治系统) 吗？用 Within 和 Between 区分！
- **满分答案**：`IGPs are used within a single autonomous system while EGPs are used between autonomous systems.`

**d)* To what extent are networks limited that use solely RIP as routing protocol?**
- **满分答案**：`The maximum hop count for RIP is 15` (最多只能传 15 跳，因此网络的物理直径不能大于这个数)。

**e)* Which information is contained in a routing update sent by RIP?**
- **大坑预警**：这是 Tutorial 08 里专门强调过的概念。广播包里到底有什么？
- **满分答案**：`Solely the reachable destinations and the cost. (In particular not the next hop.)` (只发“能去哪”和“花多大代价”，**绝对不发下一跳是谁**！因为对方收到后，下一跳自然就是你。)

**f)* Reason whether or not RIP always chooses the shortest path in based on the hop count.**
- **满分答案**：`Yes, hop count is RIP’s sole metric.` (是的，跳数更少就是王道)。

**g)* Reason whether or not RIP always chooses the fastest route in terms of bandwidth.**
- **满分答案**：`No, the number of hops does not tell anything about available bandwidth.` (一条千兆光纤绕远路，RIP 宁可走一条网速慢如牛但跳数少的破电话线)。

---

## 第二阶段：全卷最迷惑的填表题 (Converged State)
**h) Fill in the routing tables in Figure 5.1 (without intermediate steps) such that the tables represent a converged state.** 

**什么是 Converged State (收敛状态)？**
在平时的 `Exercise 8` 中，助教让你们一行一行地推算 Step 1, Step 2, Step 3... 路由器一直靠互发消息更新彼此的表。这个痛苦折磨的过程，直到大家最终拼凑出了一张**“全图最短路径真理表”**，再也没有人需要更新时，就叫 **Converged State (收敛状态)**。

**考场上如何填这张 "Converged Table" 表？**
这其实是一道寻找**全图最短跳数然后推算 Cost**的逻辑题。考卷上给了你：路由器 A、B、C、D、E（拓扑结构是 A/B 连着 C，C 连着 D，D 连着 E）。
你只需要把自己当成其中一个路由器（比如 A），然后看着整张拓扑图：
1. **找目标 (Destination)**：你要跑到 B、C、D、E。
2. **填下一跳 (Next Hop)**：要想走这条最近的路，你从 A 出来第一步跨到了谁的头上？（比如去 E 的最短路线是 A->C->D->E，A 离开家的第一步必须踩到 C 的头上，所以去往 E 的 Next Hop 填 **C**）。
3. **推算绝密 Cost**：这也是你在真题中最容易算大的一个坑！如果在表里面直接数“线段数”，A 到 E 确实应该有 3 根线。**但这道题的坑点在于：表上的 Cost 并不是指你走到目的地的总线段数，而是【抛开你自己走出的第一步，从 Next Hop (下一跳) 出发走到目的地的剩余线段数】！**
   - 比如 A 去 E，下一跳是 C。从 C 走到 E 还需要几根线？(C->D 和 D->E，共 2 根线)。所以 A 表格里填的 Cost 是 **2**！
   - 比如 A 去 C，下一跳是 C。从 C 走到 C 需要几根线？**0 根！** 所以 A 连自己亲邻居 C 的 Cost 是 **0**。
   - *(大白话：这就相当于算中间跨过了几个十字路口当跳板。用目标总线段数减去 1 即可。)*

> **真题实战 (填表诀窍)**：
> 1. 眼看地图，找最短路线，写下第一站是谁（Next Hop）。
> 2. 然后从这个第一站开始数，走到终点还有几条线，直接把这个数字填进 Cost！
> 根本不需要去管什么网络收敛的中间步骤，教授要的就是**最终大家都心知肚明后的那张真理图**！。

---

## 第三阶段：无限计数灾难爆发 (连环推理)
题目画风一转，给出了灾难剧本：“假设路由器 D 和 E 之间的线断了。D 第一时间发现了。请按顺序回答：”

**i) Router D sends a periodic update. Describe its immediate effect on the other routers.**
- **翻译**：D 发现路断了，发出广播更新，谁听到了什么？
- **满分答案**：`C is informed about the fail and will remove the route to E via D. A and B do not receive the update from D.`
- **讲解**：因为 D 只能跟隔壁的邻居说话！只能传达给 C，然后 C 会把通往 E 的路删掉。在这个瞬间，远处的 A 和 B 还是瞎子。

**j) Now, router A sends a periodic update. Describe its immediate effect on the other routers.**
- **翻译**：惨案来了。还没收到断网消息的 A，此时傻乎乎地发了它的常规更新广播！
- **满分答案**：`Since A still assumes there is a route to E via C, it is included in the update. B will ignore that (...), However, C now wrongly assumes that there is a route to E via A with cost 3 and installs this new route!`
- **讲解**：A 看着自己老旧的表：“大家听着，我虽然没直接连着 E，但我穿过 C 能到 E 哦（Cost 是 2）！” 
听到这句话的 C 傻眼了并感动得重新做人：“哎呀，我刚刚以为去 E 的路断了，原来大哥 A 能带我去！虽然大哥说他那条路代价是 2，那加上我到大哥的代价 1，总 Cost 变成 3！赶紧记在小本本上，去 E，下一跳找 A，代价 3！”

**k) Describe the problem that will now arise and how it can be solved.**
- **翻译**：描述接下来会发生什么致命故障，以及如何解决！
- **满分答案**：
  - **Problem**: `Count-to-Infinity: the non-existing route to E will circulate between A, B, and C until the tombstone of 15 is reached.` (这就是 Exercise 8 里面那个表，Cost 从 3 变 4，变 5... 互相疯狂推诿踢皮球，直到加到 15 爆表死掉)。
  - **Solution**: `Possible solutions include Split Horizon, Poison Reverse, and Triggered Updates.` 
  (水平分割：A 既然知道自己的路是基于 C 的，就绝对不能把这条路反过来吹给 C 听；毒性逆转：A 直接告诉 C 这条路代价是 16 走不通；触发更新：D 发现路断了立刻拉响警报，打破 30 秒规矩马上广播全服！)。

---

总结：通过深度绑定 Exercise 8 平时作业和 2024 Endterm 期末卷的这 11 个小题，你会发现这整整 19 分的大题，几乎完全就是一段**顺理成章的话剧演出**。

只要带着这份连环解答指南，这 19 分可以说直接装进了口袋里。我接下来为你呈上**第二战：把 2025 年真题里的 “IP Subnetting 子网切割 / LPM 匹配” 做同样的每一个细节拆解**，如何？
