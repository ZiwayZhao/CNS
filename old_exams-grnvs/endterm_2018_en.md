Chair of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized by attaching a code during the attendance check.  
- This code contains only a sequential number, which is also noted on the attendance lists next to the signature field.  
- This will be used as a pseudonym to allow a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Endterm  
Date: Wednesday, August 1, 2018  
Examiner: Prof. Dr. Uwe Baumgarten  
Time: 08:00–09:30  

**A1 A2 A3 A4 A5**  
I  
II  

**Instructions for Completion:**  
- This exam comprises  
  - 16 pages with a total of 5 tasks as well as  
  - a double-sided formula collection.  
Please check now that you have received a complete set of information.  
- The removal of pages from the exam is prohibited.  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only results where the solution path is recognizable will be counted. Text problems must also be justified unless explicitly stated otherwise in the respective subtask.  
- Calculation results must be given rounded to two significant decimal places unless explicitly stated otherwise in the respective subtasks.  
- Do not write with red/green colors or with a pencil.  
- The total score for this exam is 90 points.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - an analog dictionary in the native language without notes  
- Please turn off all electronic devices you have with you completely, store them in your bag, and close it.  

**Leaving the lecture hall until / Early submission by**  

---

**Task 1**  
Short Tasks (13 points)  
The following subtasks are to be answered independently of each other.  

a) *Mark all collision domains in the network below.  
0  
Important: Ensure that only the interfaces that are included in the marking are those that are also located in the respective collision domain!  
1  

b) *Mark all broadcast domains in the network below.  
0  
Important: Ensure that only the interfaces that are included in the marking are those that are also located in the respective broadcast domain!  
1  

c) *How many different IPv6 addresses are theoretically possible? (State as a power)  
0  
1  

d) *Name 2 routable protocols. (without justification)  
0  
1  

e) *What is meant by a socket?  
0  
1  

f) *Briefly describe the difference between Interior and Exterior Gateway Protocols (IGPs and EGPs).  
0  
1  

g) *Explain the difference between the syscalls send() and sendto().  
0  
1  

h) *Name the necessary syscalls in the correct order to create a connection-oriented socket and prepare for incoming connections.  
1  
2  

i) *Give the 32-bit data 0x01 23 45 67 in Network Byte Order in Big Endian.  
0  
1  

j) *Give 10 Gbit in the unit MiBan.  
0  
1  

k) *Determine the network and broadcast addresses of the smallest possible subnet that includes at least the addresses 203.0.113.17 and 203.0.113.46.  
0  
1  

---

**Task 2**  
Ethernet Physical Layer (17 points)  
In this task, we investigate two different implementations of the Ethernet Physical Layer. First, we discuss the (somewhat outdated) 10BASE-2. The Manchester encoding is used as the line code. No additional channel coding takes place. Given is the idealized 10BASE-2 signal shown in Figure 2.1.  

s(t)  
A  
−  
t/10 7s  
1 2 3 4 5 6 7 8 9 10  
−  
A  

**Figure 2.1:** Idealized course of a 10BASE-2 signal.  

a) *Is the signal time continuous or time discrete (without justification)?  
0  
1  

b) *Determine the bit sequence transmitted in the time interval t [0µs, 1µs).  
0  
Note: There are two valid solutions.  
1  
2  

c) *How long does it take to serialize a single bit?  
0  
1  

d) *Determine the data rate achievable with 10BASE-2 (calculation or justification).  
0  
1  

e) *Determine the minimum necessary spectral bandwidth according to Hartley to achieve the data rate determined in subtask d) with a binary line code.  
0  
1  
2  

f) *Justify why 10BASE-2 occupies at least a bandwidth of B = 10 MHz.  
0  
1  

g) *Justify which other binary line code can achieve a higher data rate at the same spectral bandwidth.  
1  

h) *What essential advantage does the Manchester code offer?  
0  
1  

Next, we consider the newer 100BASE-TX standard. This uses MLT-3 with 4B5B encoding as the line code. The effective data rate is 100 Mbit/s. In Figure 2.2, an idealized signal course of a single wire is shown, which represents the first four bits of the message 0101111101.  

s(t)  
A  
1 2 3 4 5 6 7 8 9 10 t/T  
−  
A  

**Figure 2.2:** Idealized course of an MLT-3 signal.  

i) *Complete the signal course in Figure 2.2 with the remaining six bits.  
0  

j) *Justify whether problems occur when recognizing long sequences of zeros or ones when using the MLT-3 encoding.  
0  
1  
2  

k) *Name two advantages that the 4B5B encoding brings.  
0  
1  
2  

l) *What must the bit rate actually be at 100BASE-TX to achieve an effective transmission speed of 100 Mbit/s?  
Note: This only concerns the bit rate from the perspective of the physical layer. You do not need to consider the overhead caused by protocol headers!  

---

**Task 3**  
TCP Flow and Congestion Control (22 points)  
The most widely used transport protocol on the Internet is TCP. It implements mechanisms for flow and congestion control. Specifically, in this task, we take TCP "Reno" as introduced in the lecture.  

The following 6 subtasks are multiple-choice single answer, i.e., you must choose exactly one solution for each subtask.  

- Mark the correct answers.  
- Crossed answers can be marked again by completing the adjacent markings.  

Assign the following concepts and terms to either congestion control or flow control:  

a) *Overload at the receiver  
both not applicable Congestion control Flow control  

b) *Overload at the sender  
both not applicable Congestion control Flow control  

c) Connection establishment  
both not applicable Congestion control Flow control  

d) Send window  
both not applicable Congestion control Flow control  

e) Receive window  
both not applicable Congestion control Flow control  

f) Packet loss in the network  
both not applicable Congestion control Flow control  

We will proceed from the assumption that the receive windows are always larger than the send windows.  

g) *Sketch by hand in the solution field a typical course of the send window size for TCP. Assume that the TCP connection was just established at time t = 0.  
0  
1  
2  

**Send window/Bytes**  
0 t/RTT  
0  

h) Mark and name the two phases of congestion control in your solution to subtask g).  
0  

i) What triggers the transition between the two congestion control phases? (without justification)  
0  
1  

j) *Under what circumstances does the congestion control mechanism start over? (without justification)  
0  
1  

To analyze the TCP data rate, we consider the course of a continuous data transmission, where the first phase of congestion control has already been completed. Since the receive window is assumed to always be sufficiently large, the size of the send window always corresponds to that of the congestion window. There are no losses as long as the send window is smaller than its maximum value x, i.e., ws < x. If the send window reaches the value x, exactly one of the sent TCP segments is lost.  

k) *How does the receiver recognize the loss of a segment? (without justification)  
0  
1  

l) *How does a single lost segment influence the send or congestion control window?  
0  
1  

As concrete numerical values, we assume that the maximum TCP segment size (MSS) is 1460 B and the RTT is 200 ms. The serialization time of segments compared to the propagation delay is negligible. Segment loss occurs at a send window size of ws = 16 MSS.  

m) *Create a diagram where the current size of the send window ws measured in multiples of the MSS is plotted over the time axis measured in multiples of the RTT. In your diagram, it should hold that at time t0 = 0 s, ws = x/2. Draw the diagram in the time interval t = 0,...,14.  
0  
1  
2  
3  

**ws/MSS**  
16  
15  
14  
13  
12  
11  
10  
9  
8  
7  
6  
5  
4  
3  
2  
1  
0  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 t/RTT  

n) Determine the period duration T between the reduction of the send window and the next segment loss generally depending on x.  
0  

o) Derive the number N of transmitted segments (including the lost segment at the end) per period duration generally depending on x. Simplify the result as much as possible.  
0  
1  
2  
3  

p) Determine the loss rate θ generally and as a numerical value.  
0  
1  

q) Using the results from subtasks n) – p), determine the average achievable transmission rate in kbit/s during the considered TCP transmission phase.  
0  

---

**Task 4**  
Wireshark (18 points)  
Given is the network from Figure 4.1a. PC1 has previously sent a packet to Srv. The depicted frame is an error message sent by R in response.  

**Figure 4.1a:** Network topology  
```
PC1 ------> Sw ------> R
```

```
0x0000 90 e2 ba 2a 8d 97 90 e2 ba 86 dd 60 08 00 45 c0
0x0010 00 53 20 dc 00 00 40 01 d2 5b c0 a8 02 fe c0 a8
0x0020 02 64 03 00 82 42 00 00 00 00 45 00 00 37 59 84
0x0030 00 00 40 11 9c 24 c0 a8 02 64 c0 00 02 01 cc 1a
0x0040 00 35 00 23 b2 4b 86 b2 01 20 00 01 00 00 00 00
0x0050 00 00 05 67 72 6e 76 73 03 6e 65 74 00 00 1c 00
0x0060 01
```

**Figure 4.1b:** Ethernet frame between Sw and PC1  

The offset is the index in the byte array and must be specified as 0-based (as in Java). Provide interpreted data such as addresses or ports in their usual and shortened notation.  
Note: Use the headers and information printed on the cheatsheet for the solution.  
Example: Determine the Layer 2 address of the recipient.  
Offset: 0 Length: 6  
Address: 90:e2:ba:2a:8d:97  
belongs to node: PC1  

a) *Determine the Layer 2 address of the sender.  
0  
1  
Offset: Length:  
2 Readable format:  
3 belongs to node:  

b) Determine the Layer 3 address of the recipient.  
0  
1  
Offset: Length:  
2 Address:  

c) Determine the Layer 3 address of the sender.  
0  
1  
Offset: Length:  
2 Address:  

Re-entry: The ICMP error message starts at index 34.  

d) Determine the type and code of the error message.  
0  
Offset: Length: 1  
Meaning Type/Code: 2  

e) Determine the Layer 3 address of Srv from the packet contained in the error message.  
0  
Offset: Length: 1  
Address: 2  

f) Determine the Layer 4 protocol used in the original message.  
0  
Offset: Length: 1  
Protocol: 2  

g) Determine the destination port used in the original message.  
0  
Offset: Length: 1  
Port: 2  

h) Which application protocol was probably used?  
0  
1  

i) Argue what kind of error triggered the error message.  
0  
1  
2  

---

**Task 5**  
IP Fragmentation and Path-MTU Discovery (20 points)  
In this task, we first consider fragmentation in IPv4. The network topology is given in Figure 5.1.  

```
MTU: 1500B  MTU: 1280B  MTU: 576B
PC1 -----> R1 -----> R2 -----> PC2
```

The routers R1 and R2 are configured so that the two hosts PC1 and PC2 can communicate with each other. The three network segments are independent of each other and use different transmission technologies, so the MTUs visible in the figure are given.  

a) *How should the MSS be chosen depending on the MTU? (Formula with variables)  
0  
1  

b) Provide typical numerical values for the formula from subtask a) as far as possible.  
0  
1  

c) *Justify whether fragments can be fragmented again.  
0  
1  

d) *At which point in the network are fragments reassembled? (Justification)  
0  
1  

e) *How can you tell that it is a fragment? Provide the solution as pseudocode, where the IP header fields are each present as variables with the same name.  
0  
1  
2  

```
fragmented =
```

f) *What must be considered in the Fragment Offset field in the IPv4 header?  
0  
1  

Assume that PC1 has established a TCP connection to PC2. PC1 wants to send 1460 B of payload data over this TCP connection to PC2. PC1 sends this data considering the necessary minimum IP and TCP headers. Router R1 cannot forward the resulting packet directly and must first fragment it.  

g) Provide the respective sizes of all IP packets sent from R1 to R2.  
0  
1  
2  

h) Router R2 must now process these packets appropriately. Provide the respective sizes of all IP packets sent from R2 to PC2.  
1  
2  
3  

As an alternative to IP fragmentation, we now consider Path-MTU Discovery. We continue to use the network topology from Figure 5.1. PC1 still wants to send payload data of 1460 B to PC2 over an already established TCP connection.  

Path-MTU Discovery is used to prevent fragmentation in the network. So that the sender does not have to perform IP fragmentation, it can adjust the TCP MSS accordingly.  

Path-MTU Discovery works as follows:  
- The sender first sends packets of the size of the local MTU.  
- These packets must not be fragmented in the network.  
- If a router receives such a packet but cannot forward it directly due to the MTU in the following network segment, it sends an ICMP Destination Unreachable, Fragmentation Needed (Type 3, Code 4) message back to the sender.  
- This message contains the MTU of the following network segment, and the router discards the original packet.  
- The sender must resend the data while adhering to this MTU. In TCP, this is possible by adjusting the MSS.  
- The sender stores the MTU for subsequent packets with the same destination.  

i) *How does the sender ensure that its packets are not allowed to be fragmented in the network?  
0  
1  

j) Calculate the respective sizes of all required IP packets to transmit TCP payload data of 1460 B from PC1 to PC2 without any fragmentation. Consider all necessary headers in their minimal size.  
0  
1  
2  
3  

k) Draw a simplified path-time diagram (serialization time and propagation delay can be neglected) for Path-MTU Discovery and the sending of the message (1460 B TCP payload data). Indicate the total size of the IP packet for data packets ("IP packet, 128 B"). ICMP Fragmentation Needed packets should be marked as such, and the returned MTU should be indicated ("ICMP Frag. needed, 256 B").  
0  
1  
2  
3  

Note: The initial congestion window for TCP is 4 MSS. Neglect TCP acknowledgments and any Layer 2 messages.  

---

**Additional space for solutions. Clearly mark the assignment to the respective subtask. Do not forget to cross out invalid solutions.**