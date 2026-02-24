# 考点终极攻坚：IPv6 NDP / 被请求节点组播 (Solicited-Node) / 组播 MAC 地址转换 🧙‍♂️

在复习 IPv6 时，很多同学在学完 **EUI-64**（已知单播 MAC 求 IPv6 或者反推）之后，看到 **NDP**（Neighbor Discovery Protocol）和 **Solicited-Node Multicast（被请求节点组播地址）** 就会彻底搞混，甚至瞎用“第 7 比特翻转”的口诀。

**它们是截然不同的两个考点！**
在近年（尤其是最新出炉的 **2024 Retake** 和 **2025 Endterm**）考试中，这部分是必考题，通常直接占 2-3 分的核心短题。它不考位运算，考的是“固定前缀拼接拼接游戏”。

---

## 核心前提：IPv6 为什么不用 Broadcast (全网广播)？

在 IPv4 时代，为了问一句“谁的 IP 是 192.168.1.5，请把 MAC 告诉我 (ARP)”，计算机会扯着嗓子大喊：目标 MAC `= FF:FF:FF:FF:FF:FF`（全网广播），这会吵醒局域网里所有休眠的网卡。

**IPv6 彻底废除了广播！** 取而代之的是 **NDP (Neighbor Discovery Protocol)**。
由于不能全网大喊，当想知道某个已知目标 IPv6 (例如 `fe80::1`) 的 MAC 地址时，发送方会去敲一个**“小群聊”**的门。这个“小群聊”就是 **Solicited-Node Multicast Address（被请求节点的组播地址）**。
- **优点**：只有目标 IP 同样凑巧落在这个“小群”里的网卡才会被叫醒，不会打扰其他无关电脑。

---

## 考点一：怎么计算 Solicited-Node Multicast Address？

这是考试最喜欢出的第一环！

**公式 / 拼接魔法：**
无论目标 IPv6 全名叫什么，它的 Solicited-Node 组播地址 **前面这 104 位全部是固定死板的**：
👉 **`ff02::1:ff`**

**剩下怎么填？**
直接从原本的目标 IPv6 地址的**最后 24 位（最后 6 个十六进制字符 / 最后 1.5 组数字）**原封不动地剪切下来，粘在后面！

### 🔍 实战演练1：
> 目标 IP：`fe80::2788:1fff:`**`feae:3c4a`**
- 找出最后 6 个字符：**`ae:3c4a`** (也就是 `ae3c4a`)
- 拿固定前缀 `ff02::1:ff`
- **拼装答案**：**`ff02::1:ffae:3c4a`**

这就是网卡准备去敲门的“小群聊”房间号！

---

## 考点二：怎么计算对应的 Multicast MAC Address (组播 MAC 地址)？

当网卡拿着刚才算好的 `ff02::...` 小群号准备发以太网帧时，以太网帧（Layer 2）也需要一个**目标 MAC 地址**。
这里**绝对不要使用 EUI-64（不要塞 FFFE，不要去翻转第 7 位）！**因为你正在生成的是一个**组播 MAC**，而不是单播 MAC。

**公式 / 拼接魔法：**
所有 IPv6 映射出的组播 MAC 地址，必须以 **`33:33`** 作为固定前导！
👉 **`33:33:`**

**剩下怎么填？**
取刚刚那个 Multicast IP 的**最后 32 位（最后 8 个十六进制字符 / 最后两组数字）**，变成 MAC 格式！

### 🔍 实战演练2（沿用演练1）：
> 刚才算出的组播 IP 为：`ff02::1:`**`ffae:3c4a`**
- 找出最后 8 个字符：**`ffae3c4a`** 
- 分开变成 MAC 的格式：**`ff:ae:3c:4a`**
- 拿固定前导：`33:33`
- **拼装答案**：**`33:33:ff:ae:3c:4a`**

这，就是底层的以太网网卡真正装进目标地址栏发送出去的乱码！

---

## 🚨 极其重要的“避坑区分表” (考前必看)

不要把单播和组播搞混了，口诀不同！

| 使用场景                                     | 考点特征词                                          | 使用的魔法口诀                                    |
| :------------------------------------------- | :-------------------------------------------------- | :------------------------------------------------ |
| **单播转换 (Unicast)**<br>给网卡分配 IP      | *EUI-64*、*Generate Link-Local*、*from MAC address* | **中间塞 FF:FE，第一字节翻转第 7 位**             |
| **组播转换 (Multicast)**<br>找隔壁邻居 (NDP) | *Solicited-Node Address*, *Multicast MAC Address*   | **固定前缀 `ff02::1:ff` / `33:33:` 加上尾巴照抄** |

---

## 🔥 全真考卷·原题复现 (来自慕尼黑工大原版密卷)

### 真题一：(Retake 2024 / Endterm 2025 祖传变种原题，价值 2 分)
> **Question:**
> Given is the following IPv6 address: `fe80::2788:1fff:feae:3c4a`. What is the corresponding Solicited Node Address as well as the Multicast MAC Address?
> `(给出 IPv6 地址 fe80::2788:1fff:feae:3c4a，求它对应的 Solicited Node 地址和组播 MAC 地址？)`

**参考答案 (手算拆解)：**
1. **Solicited Node Address**:
   - 取 IPv6 最后 6 个字符：`feae:3c4a` 里的 `ae3c4a`
   - 与 `ff02::1:ff00:0/104` 的前缀结合 (合并覆盖最后的补零)：
   - **答案**：`ff02::1:ffae:3c4a`

2. **Multicast MAC Address**:
   - 看到是 IPv6 的组播求 MAC，前导必须写下 `33:33`
   - 取刚才的组播 IP 最后 8 个字符（也就是 `ffae3c4a`）切成 MAC 段：`ff:ae:3c:4a`
   - 拼装！
   - **答案**：`33:33:ff:ae:3c:4a`

---

### 真题二：(Endterm 2013 经典拓扑抓包大题·NDP 反向推演)
> *(在抓包数据中出现了以下一条通信：)*
> `fc00::10 -> ff02::1:ff00:1, ICMPv6, Length: 86`
> `Neighbor Solicitation: whois fc00::1 from 90:e2:ba:2a:d2:a3`
> **Question:**
> *To which MAC address will this request be addressed? Name the address type and provide the specific MAC address.*
> `(请问这个请求帧的目标 MAC 地址是多少？并说出这个地址的类型名称。)`

**参考答案 (解析逆推)：**
1. 观察包裹特征，它是由 ICMPv6 发出的 `Neighbor Solicitation`（相当于 IPv4 的 ARP Request）。
2. 注意到它的目标 IP 并不是单播，而是 `ff02::1:ff00:1`（这是一个标准的 Solicited-Node Multicast Address）。
3. 题目让我们去找**这一下发出的以太网数据帧的目标 MAC**。因此这在考察 **Multicast IPv6 转 Multicast MAC**。
4. 目标 IP 最后 8 个字符是 `ff00:0001` (简写前的模样)。
5. MAC 前缀是 `33:33`。拼装最后 32 位：`ff:00:00:01`。
   - **地址类型 (Address Type)**：`Multicast MAC Address`
   - **具体地址 (Specific MAC)**：**`33:33:ff:00:00:01`**

---

掌握了以上**三条拼接法则**，以后在考场上只要看到 `Solicited Node` 或 `NDP multicast MAC` 的字眼，直接拿着后面的尾巴套上 `ff02::1:ff` 和 `33:33:` 两个万能模具，闭着眼睛拿满分。不要去算二进制，不要去翻转！
