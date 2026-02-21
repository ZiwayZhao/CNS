Chair of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized by affixing a code during the attendance check.  
- This code contains only a sequential number, which is also noted on the attendance list next to the signature field.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Endterm  
Date: Wednesday, August 1, 2018  
Examiner: Prof. Dr. Uwe Baumgarten  
Time: 08:00–09:30  

**Instructions for Completion**  
- This exam consists of 16 pages with a total of 5 tasks as well as a double-sided formula collection. Please check now that you have received a complete set of materials.  
- The tearing out of pages from the exam is prohibited.  
- Tasks marked with *g can be solved without knowledge of the results of previous tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective task.  
- Calculation results must be given rounded to two significant decimal places unless explicitly stated otherwise in the respective task.  
- Do not write with red/green colors or with pencil.  
- The total score for this exam is 90 points.  
- Permitted aids:  
  - A non-programmable calculator  
  - An analog dictionary in the native language without annotations  
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.  

**Task 1**  
Short Tasks (13 Points)  
The following sub-tasks are to be answered independently of each other.  

a) *Mark all collision domains in the network below.  
![Network Diagram]  
Important: Ensure that only the interfaces that are included in the marking are those that are also located in the respective collision domain!  

b) *Mark all broadcast domains in the network below.  
![Network Diagram]  
Important: Ensure that only the interfaces that are included in the marking are those that are also located in the respective broadcast domain!  

c) *How many different IPv6 addresses are theoretically possible? (Indicate as a power)  
0  
1 2^128 = 340282366920938463463374607431768211456  

d) *Name 2 routable protocols. (No justification required)  
0  
1 IPv4, IPv6 (other (older) routable protocols: Internetwork Packet Exchange (IPX), DECNET Phase V, Appletalk)  

e) *What is meant by a socket?  
0  
1 A resource of the operating system for communication between processes on potentially different hosts.  

f) *Briefly describe the difference between Interior and Exterior Gateway Protocols (IGPs and EGPs).  
0  
1 IGPs are used for exchanging routing information within Autonomous Systems, EGPs for exchanging routes between Autonomous Systems.  

g) *Explain the difference between the syscalls send() and sendto().  
0  
send() primarily works with connection-oriented sockets. The recipient is implicitly determined after the connection establishment (connect()).  
1  
sendto() primarily works with connectionless sockets. The recipient must therefore be explicitly specified with each call.  

h) *Name the necessary syscalls in the correct order to create a connection-oriented socket and prepare for incoming connections.  
0  
1 socket(), bind(), listen()  

i) *Give the 32-bit data 0x01 23 45 67 in Big Endian in Network Byte Order.  
0  
1 0x01 23 45 67  

j) *Convert 10 Gbit into MiB.  
0  
1 10 Gbit = 10^9 bit / 8 bit/B = 1192.09 MiB  

k) *Determine the network and broadcast addresses of the smallest possible subnet that includes at least the addresses 203.0.113.17 and 203.0.113.46.  
0  
1 Network address: 203.0.113.0  
Broadcast: 203.0.113.63  

**Task 2**  
Ethernet Physical Layer (17 Points)  
In this task, we will examine two different implementations of the Ethernet Physical Layer. First, we will discuss the (somewhat outdated) 10BASE-2. The Manchester coding will be used as the line code. No additional channel coding takes place. Given is the idealized representation of the 10BASE-2 signal in Figure 2.1.  

![10BASE-2 Signal]  

a) *Is the signal time continuous or time discrete (without justification)?  
0  
1 Time continuous  

b) *Determine the bit sequence transmitted in the time interval t [0µs, 1µs).  
0  
Note: There are two valid solutions.  
1  
According to the version used in IEEE 802.3: 01 01 11 11 01  
2  
Alternative: 10 10 00 00 10  

c) *How long does it take to serialize a single bit?  
0  
1 From Figure 2.1: T = 1 / 10^7 s = 0.1 µs  

d) *Determine the data rate achievable with 10BASE-2 (calculation or justification).  
0  
1 r = 1 bit / T = 10 Mbit/s  

e) *Determine the minimum necessary spectral bandwidth according to Hartley to achieve the data rate determined in part d) with a binary line code.  
0  
1 r = 2B log2(M) ⇔ B = r / (2 log2(M)) = 5 MHz  

f) *Justify why 10BASE-2 occupies at least a bandwidth of B = 10 MHz.  
0  
1 The Manchester code represents a bit by two signal changes. It therefore has a baud rate that is twice as high as, for example, NRZ at the same bit rate. The required bandwidth doubles.  

g) *Justify which other binary line code can achieve a higher data rate at the same spectral bandwidth.  
0  
1 NRZ is suitable because here the baud rate corresponds exactly to the bit rate.  

h) *What essential advantage does the Manchester code offer?  
0  
1 Clock recovery (or DC-free)  

Next, we consider the newer 100BASE-TX standard. This uses MLT-3 with 4B5B encoding as the line code. The effective data rate is 100 Mbit/s. In Figure 2.2, an idealized signal progression of a single wire is shown, which represents the first four bits of the message 0101111101.  

![MLT-3 Signal]  

i) *Complete the signal progression in Figure 2.2 for the remaining six bits.  

j) *Justify whether problems arise when recognizing long sequences of zeros or ones with MLT-3 encoding.  
0  
1 Long sequences of zeros lead to a constant signal level. Since clock recovery is difficult here, this poses a problem.  

k) *Name two advantages that the 4B5B encoding brings.  
0  
1 Limiting the maximum length of zero sequences allows for clock recovery.  
2 Providing control characters.  

l) *What must the bit rate actually be at 100BASE-TX to achieve an effective transmission speed of 100 Mbit/s?  
Note: This only concerns the bit rate from the perspective of the physical layer. You do not need to consider the overhead caused by protocol headers!  
0  
1 r_gross = r_net / (4 / 5) = 125 Mbit/s  

**Task 3**  
TCP Flow and Congestion Control (22 Points)  
The most widely used transport protocol on the Internet is TCP. This implements mechanisms for flow and congestion control. Specifically, we will consider TCP "Reno" as introduced in the lecture.  

The following 6 sub-tasks are multiple-choice single-answer, i.e., you must choose exactly one solution for each sub-task.  
Mark the correct answers.  
Crossed answers can be struck through by completing the fill-in.  
Struck answers can be marked anew by the adjacent markings.  

Assign the following concepts and terms to either congestion or flow control:  
a) *Overload at the receiver  
b) *Overload at the sender  
c) Connection establishment  
d) Send window  
e) Receive window  
f) Packet loss in the network  

We will assume that the receive windows are always larger than the send windows.  

g) *Sketch by hand in the solution field a typical course of the send window size for TCP. Assume that the TCP connection was just established at time t = 0.  

h) Mark and name the two phases of congestion control in your solution to sub-task g).  

i) What triggers the transition between the two congestion control phases? (Without justification)  
0  
1 3 Duplicate ACKs  

j) *Under what circumstances does the congestion control mechanism start over? (Without justification)  
0  
1 Timeout  

To analyze the TCP data rate, we consider the course of a continuous data transmission, where the first phase of congestion control has already been completed. Since the receive window is assumed to always be sufficiently large, the size of the send window always corresponds to that of the congestion control window. There are no losses as long as the send window is smaller than its maximum value x, so ws < x. Once the send window reaches the value x, exactly one of the sent TCP segments is lost.  

k) *How does the receiver recognize the loss of a segment? (Without justification)  
0  
By an out-of-order received sequence number.  

l) *How does a single lost segment influence the send or congestion control window?  
0  
1 If 3 Duplicate ACKs are received, the congestion control window is halved.  
2 If a timeout occurs due to a missing ACK, the congestion control window is reduced to 1 and a new slow start is triggered.  

As concrete numerical values, we assume that the maximum TCP segment size (MSS) is 1460 B and the RTT is 200 ms. The serialization time of segments compared to the propagation delay is negligible. Segment loss occurs at a send window size of ws = 16 MSS.  

m) *Create a diagram in which the current size of the send window ws measured in multiples of MSS is plotted against the time axis measured in multiples of RTT. In your diagram, it should hold that at time t0 = 0 s, ws = x/2. Draw the diagram in the time interval t = 0,...,14.  

n) Determine the period duration T between the reduction of the send window and the next segment loss in general dependence on x.  
0  
1 T = (x / 2) / MSS = 1.8 s  

o) Derive the number N of segments transmitted per period duration (including the lost segment at the end) in general dependence on x. Simplify the result as much as possible.  
1  
With the shorthand notation = x we obtain:  
N = (n / 2) * (n / 2 + 1) / 2  
= n(n + 1) / 2  

p) Determine the loss rate θ in general and as a numerical value.  
0  
For each "sawtooth," exactly one segment is lost. Thus, we obtain for the loss rate:  
θ = N = (3n^2 + 3n) / 8  

q) Using the results from sub-tasks n) – p), determine the average achievable transmission rate in kbit/s during the considered TCP transmission phase.  
1  
For the data rate, we obtain:  
r = (1 - θ) * (N * 1460 * 8) / T = 694 kbit/s  

**Task 4**  
Wireshark (18 Points)  
Given is the network from Figure 4.1. PC1 has previously sent a packet to Srv. The frame shown is an error message that was then sent by R.  

![Network Topology]  

The offset is the index in the byte array and must be specified as 0-based (as in Java code). Provide interpreted data such as addresses or ports in their usual and shortened notation.  
Note: Use the headers and information printed on the cheat sheet for the solution.  

Example: Determine the Layer 2 address of the recipient.  
Offset: 0 Length: 6  
Address: 90:e2:ba:2a:8d:97  
Belongs to node: PC1  

a) *Determine the Layer 2 address of the sender.  
0  
1 Offset: 6 Length: 6  
2 Readable format: 90:e2:ba:86:dd:60  
3 Belongs to node: R  

b) Determine the Layer 3 address of the recipient.  
0  
1 Offset: 30 Length: 4  
2 Address: 192.168.2.100  

c) Determine the Layer 3 address of the sender.  
0  
1 Offset: 26 Length: 4  
2 Address: 192.168.2.254  

Re-entry: The ICMP error message starts at index 34.  

d) Determine the type and code of the error message.  
0  
Offset: 34 Length: 2  
1 Meaning Type/Code: Destination Unreachable, Network Unreachable  

e) Determine the Layer 3 address of Srv from the packet contained in the error message.  
0  
Offset: 58 Length: 4  
1 Address: 192.0.2.1  

f) Determine the Layer 4 protocol used in the original message.  
0  
Offset: 51 Length: 1  
1 Protocol: UDP  

g) Determine the destination port used in the original message.  
0  
Offset: 64 Length: 2  
1 Port: 53  

h) What application protocol was likely used?  
0  
1 DNS  

i) Argue what kind of error triggered the error message.  
0  
The packet is discarded because router R cannot forward the packet. Possible reasons for this could be:  
1  
- There is no common subnet configured between R and Srv.  
- A firewall is configured on R that blocks communication.  

**Task 5**  
IP Fragmentation and Path-MTU Discovery (20 Points)  
In this task, we first consider fragmentation in IPv4. The network topology is given in Figure 5.1.  

![Network Topology]  

The routers R1 and R2 are configured so that the two hosts PC1 and PC2 can communicate with each other. The three network segments are independent of each other and use different transmission technologies, so the MTUs shown in the figure apply.  

a) *How should the MSS be chosen depending on the MTU? (Formula with variables)  
0  
1 MSS = MTU - len(IP-Header) - len(TCP-Header)  

b) Provide typical numerical values for the formula from part a) as far as possible.  
0  
1 MSS = 1500 B - 20 B - 20 B = 1460 B  

c) *Justify whether fragments can be fragmented again.  
0  
1 Yes, the assignment of fragments occurs via ID (which is not changed) and offset.  

d) *At which point in the network are fragments reassembled? (Justification)  
0  
1 IP fragments are reassembled only at the destination host. The fragments can be routed over different paths.  

e) *How can you recognize that it is a fragment? Provide the solution as pseudocode, where the IP header fields are present as variables with the same name.  
0  
1 fragmented = MF || FragmentOffset > 0  

f) *What must be considered with the Fragment Offset field in the IPv4 header?  
0  
1 The Fragment Offset is specified in multiples of 8 octets/bytes.  

Assume that PC1 has established a TCP connection to PC2. PC1 wants to send 1460 B of payload over this TCP connection to PC2. PC1 sends this data considering the necessary minimum IP and TCP headers. Router R1 cannot forward the resulting packet directly and must first fragment it.  

g) Provide the respective size of all IP packets sent from R1 to R2.  
0  
1 1276 B = 20 B IP-Header + 20 B TCP-Header + 1236 B  
2 244 B = 20 B IP-Header + 224 B.  

The IP header for both packets is necessary, the TCP header only once, and the IP payload of fragments must be a multiple of 8 bytes due to the offset.  

h) Router R2 must now process these packets appropriately. Provide the respective size of all IP packets sent from R2 to PC2.  
0  
1 572 B = 20 B IP-Header + 20 B TCP-Header + 532 B,  
2 572 B = 20 B IP-Header + 552 B,  
3 172 B = 20 B IP-Header + 152 B,  
4 244 B = 20 B IP-Header + 224 B.  

The IP header is necessary in all packets, the TCP header only once, and the IP payload of fragments must be a multiple of 8 B due to the offset; packets must not be reassembled at R2.  

As an alternative to IP fragmentation, we now consider Path-MTU Discovery. We continue to use the network topology from Figure 5.1. PC1 still wants to send payload of length 1460 B to PC2 over an already established TCP connection.  

Path-MTU Discovery is used to prevent fragmentation in the network. So that the sender does not have to perform IP fragmentation, it can adjust the TCP MSS accordingly.  

Path-MTU Discovery works as follows:  
- The sender first sends packets of the size of the local MTU.  
- These packets must not be fragmented in the network.  
- If a router receives such a packet but cannot forward it directly due to the MTU in the subsequent network segment, it sends an ICMP Destination Unreachable, Fragmentation Needed (Type 3, Code 4) message to the sender.  
- This message contains the MTU of the subsequent network segment, and the router discards the original packet.  
- The sender must resend the data while adhering to this MTU. In TCP, this is possible by adjusting the MSS.  
- The sender retains the MTU for subsequent packets to the same destination.  

i) *How does the sender ensure that its packets are not allowed to be fragmented in the network?  
0  
1 The DF (Don't Fragment) flag used indicates to routers not to fragment the packets.  

j) Calculate the respective size of all required IP packets to transmit TCP payload of length 1460 B from PC1 to PC2 without any fragmentation. Consider all necessary headers in their minimal size.  
0  
1 576 B = 20 B IP-Header + 20 B TCP-Header + 536 B,  
2 576 B = 20 B IP-Header + 20 B TCP-Header + 536 B,  
3 428 B = 20 B IP-Header + 20 B TCP-Header + 388 B.  

The IP and TCP headers are necessary in each packet.  

k) Draw a simplified path-time diagram (serialization time and propagation delay can be neglected) for Path-MTU Discovery and the sending of the message (1460 B TCP payload). Indicate the total size of the IP packet for data packets ("IP packet, 128 B"). ICMP Fragmentation Needed packets should be marked as such, and the returned MTU should be indicated ("ICMP Frag. needed, 256 B").  
Note: The initial congestion window for TCP is 4 MSS. Neglect TCP acknowledgments and any Layer 2 messages.  

![Path-MTU Discovery Diagram]  

**Additional space for solutions. Clearly mark the assignment to the respective sub-task. Do not forget to strike out invalid solutions.**