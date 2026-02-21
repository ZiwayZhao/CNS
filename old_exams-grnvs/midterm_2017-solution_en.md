Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by attaching a code during the attendance check.
- This contains only a continuous number, which is also noted on the attendance lists next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Module: IN0010  
Date: Friday, June 23, 2017  
Examiner: Prof. Dr.-Ing. Georg Carle  
Exam: Midterm  

### Instructions for Processing
- This exam consists of:
  - 8 pages with a total of 3 tasks and
  - a formula collection.
  
Please check now that you have received a complete set of information.
- The processing time is 45 minutes.
- The tearing out of pages from the exam is prohibited.
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only those results will be counted where the solution path is recognizable. Text problems must also be justified unless explicitly stated otherwise in the respective sub-task.
- Do not write with red/green colors or with pencil.
- The total score for this exam is 20 points, which will be scaled according to the bonus system.
- The following aids are allowed:
  - An analog dictionary in your native language without annotations.
- Turn off all electronic devices completely, store them in your bag, and close it.

---

### Task 1  
Media Access (7 Points)  
On the planet Gliese 581c, a water world inhabited by the Moepis, global warming has been occurring for several years. As a result, a small island has formed, which is being researched by the Moepis. Since the Moepis live far away from the island on the seabed, they have built a floating relay station to facilitate communication between the island and the Moepi base (see Figure 1.1).  

The frames will be received from the island or the Moepi base by the relay, checked for transmission errors, and forwarded to the respective other side. Neither the island nor the Moepi base needs to explicitly address the relay.  
On the path from island I to relay R, the Moepis use a more advanced method of wireless transmission based on electromagnetic waves. However, since water has a strong damping effect on electromagnetic waves, they use sound waves there. These propagate in water with approximately \( v_W = 1500 \, \text{m/s} \).

#### a) Justify which known network component from the lecture corresponds most closely to the relay.
- A switch or a bridge, as individual frames are checked for transmission errors and forwarded without the relay itself being addressed. (This excludes both hubs and routers as well as WLAN access points.)

#### b) Which method can the Moepis use to detect transmission errors?
- CRC

#### c) Describe the general function and goal of channel coding.
- Adding structured redundancy before/during transmission so that transmission errors can be corrected.

---

### Task 2  
Modulation (9 Points)  
In this task, we consider the process of pulse shaping in baseband and the subsequent modulation. We use the rectangular pulse as the basic pulse in baseband:

\[
\text{rect}(t) = 
\begin{cases} 
1 & \text{if } -\frac{T}{2} \leq t < \frac{T}{2} \\ 
0 & \text{otherwise} 
\end{cases}
\]

The modulation method uses the signal space points shown in Figure 2.1.  

#### a) What modulation method is being used?
- 4-QAM

#### b) Assign valid code words to the symbols in Figure 2.1.
  
#### c) Draw the basic pulse \(\text{rect}(t)\) in Figure 2.2.

We want to transmit the bit sequence 01101100.

#### d) Enter the corresponding code words for the bit sequence as well as the in-phase component \(I\) and quadrature component \(Q\).
  
| Code words | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
|------------|---|---|---|---|---|---|---|---|
| \(I\)      | 1 | 1 | 1 | 1 |   |   |   |   |
| \(Q\)      | 1 | 1 | 1 | 1 |   |   |   |   |

**Note:** If necessary, you will find an additional form for the following sub-tasks at the end of the exam. Clearly cross out invalid solutions.

#### e) Draw the baseband signal of the in-phase component for the given bit sequence in Figure 2.3.

#### f) Draw the baseband signal of the quadrature component for the given bit sequence in Figure 2.4.

The two baseband signals are now modulated with the frequency \( f = \frac{1}{T} \). For the in-phase component, we use the cosine carrier \( \cos(2\pi ft) \) and for the quadrature component, the sine carrier \( \sin(2\pi ft) \).

#### g) Draw the modulated signal of the in-phase component also in Figure 2.3.

#### h) Draw the modulated signal of the quadrature component also in Figure 2.4.

#### i) Draw the complete modulated signal in Figure 2.5.

---

### Task 3  
Short Tasks (4 Points)  

#### a) Justify whether 192.0.2.96/27 and 192.0.2.128/27 can be summarized?
- No, because in binary the last octet 96 = 01100000, 128 = 10000000. For /26, the first two bits would need to be the same.

#### b) Derive the usual link-local IPv6 address from the MAC address 00:00:5e:00:53:42 using the method known from the lecture. Provide this in shortened form.
- fe80::200:53ff:fe00:5342

#### c) Name two classes of routing protocols and briefly differentiate them.
- Link State Protocols and Distance Vector Protocols.  
  Link State Protocols know the entire network topology and calculate the routing table from it.  
  Distance Vector Protocols only know the direct neighbors and the networks reachable through them. The calculation of the routing table occurs iteratively.

#### d) What is ARP used for and how is this functionality achieved in IPv6?
- ARP resolves Layer 3 addresses (IP) to Layer 2 addresses (MAC). In IPv6, this is achieved through Neighbor Discovery in ICMPv6.

---

### Additional Forms for Task 2  

#### Additional Space for Solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to cross out invalid solutions.