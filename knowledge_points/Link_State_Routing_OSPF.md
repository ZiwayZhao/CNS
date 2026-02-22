# 知识点复习：Link State Routing & Dijkstra (链路状态路由与 Dijkstra 算法)

## 📌 考频分析 (Testing Frequency)
- **考频评级**：**极高频理论题 / 对比大题 (Very High Frequency / Core Theory)**
- **复习建议**：**必须死记硬背它和 Distance Vector (RIP) 的三大区别！**
- **试卷覆盖情况**：
  - 在绝大多数期中 (Midterm) 和期末 (Endterm) 考试中（如 2011, 2016, 2017, 2021, 2022），必定会有一道简答题让你对比 Link-State 和 Distance-Vector。
  - 这是 ISO/OSI 模型 Layer 3 (Network Layer) 路由协议的核心考点。

> **💡 说明 (Important Note):** 
> 经过对历年所有 Tutorial (01-14) 以及所有期中/期末真题的检索，慕尼黑工大 (TUM) 的 CNS 考试在 **近十几年中从未考过 Dijkstra 算法的表格计算或推图大题**（那种需要画表一步一步更新最优路径的繁琐计算题）。
>
> 考官将考察重点完全放在了：**OSPF (Link-State) 为什么优于 RIP (Distance-Vector)？它们的根本机制区别是什么？**
> 
> 因此，你的复习策略应当**完全转向理论背诵**，而不需要去刷 Dijkstra 画表题。

---

## 📚 考点核心与背诵指南 (Core Concepts & Cheat Sheet)

在 `slides_chap3.pdf` 中，明确给出了两大类动态路由协议 (Dynamic Routing Protocols) 的对比。这是考试唯一会考的地方。

### 1. Link State Protocols (链路状态协议，核心代表：OSPF, IS-IS)
- **核心算法**：它使用的是 **Dijkstra** 算法（一种贪心算法，逐步找出全图最短路径）。
- **工作原理 (最重要的考点)**：
  - 路由器不仅交换距离成本，还会交换**"如何到达"**的详细信息。
  - 每个路由器都会获得**全网的完整拓扑图 (Complete Topology Information / Global View)**。
  - 路由器根据这张完整的网图，自己用 Dijkstra 算出一棵"最短路径树 (Shortest Path Tree)"。
- **优点**：避免了路由环路 (Prevents routing loops at Layer 3)，不会出现 RIP 里的 "Count to infinity" 问题。

---

## 🎯 必考真题解析 (Past Questions - 纯背诵套路)

### 题型 1：终极必考对比简答题 (The Ultimate Comparison)
**Question:** RIP is a distance-vector protocol. Explain the difference to link-state protocols (like OSPF). / What is the difference between distance-vector and link-state routing protocols?
**Answer (标准答案采分点):**

1. **Topology View (拓扑视野，最重要得分点):** 
   - *Distance-Vector:* Neighboring routers only exchange distances to destinations. Each router has only a **local view** of the network (only knows next hop and distance).
   - *Link-State:* Neighboring routers exchange topology information about the part of the network they know. Each router receives a **complete view of the network (Global view of the topology).**
2. **Algorithm:**
   - *Distance-Vector* uses Bellman-Ford.
   - *Link-State* uses Dijkstra.
   📍 **出处 (Source):** *[midterm_2016_en.md; retake_2017_en.md; endterm_2011_en.md]*

💡 **中文解析**: 只要问这两者的区别，闭着眼睛写：**Distance-Vector 只知道下一跳和距离（Local view, 近视眼）；Link-State 拥有全网拓扑图（Complete Network Topology / Global view，上帝视角）。**

---

### 题型 2：OSPF 的优势与防环机制 (The Advantage of OSPF)
**Question:** Explain the main advantage of OSPF over RIP.
**Answer:** OSPF has accurate information about the network topology (Complete view), which **prevents loops at layer 3**.
📍 **出处 (Source):** *[retake_2016-solution_en.md, Task 1d]*

**Question:** Justify whether "Count-to-Infinity" can occur in Link-State protocols.
**Answer:** **No**, because each router has a global view of the network. Loops like those in Distance-Vector protocols are therefore excluded.
📍 **出处 (Source):** *[endterm_2011-solution_en.md, Task 1g]*

💡 **中文解析**: RIP 最害怕遇到断网后的“无穷大计数 (Count to Infinity)”死循环。而用 OSPF (Link-State) 绝对不会出现这个问题，因为大家手里都有全局地图，一断网全网立刻都知道了。

---

### 题型 3：协议连连看题 (Identifying Protocols)
**Question:** Which of the following protocols are Link State Protocol(s)? (e.g. from a list: RIP, OSPF, EIGRP, IS-IS, BGP)
**Answer:** **OSPF** and **IS-IS** are Link State Protocols.
📍 **出处 (Source):** *[quiz2_2021-solution_en.md]*

**Question (拓展):** Explain why OSPF could be assigned to Layer 3 of the ISO/OSI model.
**Answer:** OSPF is a routing protocol. Routing and path determination based on logical addressing (IP addresses) are exactly the core tasks of the Network Layer (Layer 3).
📍 **出处 (Source):** *[endterm_2021-solution_en.md, Task 8]*

---

### 总结 (Summary)
不要在这部分去练习画图和算表！把 **“Distance Vector = 瞎子摸象 + Bellman-Ford + RIP跳数限制(15)”** 和 **“Link State = 上帝视角 + Dijkstra算法 + OSPF 无环路(No Count-to-infinity)”** 刻在脑子里，遇到此类简答题稳定拿满分。
