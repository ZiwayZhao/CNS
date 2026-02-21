Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized by attaching a code during attendance control.  
- This contains only a continuous number, which is also noted on the attendance list next to the signature field.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems (GlRNVS)**  
Module: IN0010  
Examiner: Prof. Dr.-Ing. Georg Carle  
Exam: Endterm  
Date: Tuesday, July 26, 2016, 10:30–12:00  

**A1 A2 A3 A4 A5**  

**Instructions for Processing:**  
- This exam consists of 20 pages with a total of 5 tasks as well as a double-sided printed formula collection.  
- Please check now that you have received a complete set of information.  
- The tearing out of pages from the exam is prohibited.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be counted where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-task.  
- Please do not write with red/green colors or with pencil.  
- The total score for this exam is 85 points.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - an analog dictionary German ↔ native language without annotations  
- Please turn off all electronic devices completely, store them in your bag, and close it.  

---

**Task 1**  
Short Tasks (21.5 Points)  
The following sub-tasks can be solved independently of each other.  

a) *Name the layers (in English or German) of the ISO/OSI model in ascending order.  
1. Physical Layer, Data-Link Layer, Network Layer, Transport Layer, Session Layer, Presentation Layer, Application Layer  

b) *Given the 32-bit long date 0x81ff0010 in Network Byte Order. What is the representation in Little Endian?  
0x1000ff81  

c) *Given the following network. Draw all collision domains.  

d) *Briefly explain two problems that can occur with RIP.  
1. Only Hop Count as a metric ⇒ the shortest route is always chosen, even if a longer route would offer higher bandwidth or lower delay.  
2. It may take several minutes for changes to be fully known in the network, as updates are only sent every 30 seconds.  
The maximum distance is 15 hops, as larger values are interpreted as "unreachable" ⇒ the maximum size of the network is limited to 15 hops.  
Count-to-Infinity: With topology changes, incorrect routing information can spread depending on the update order until the max. hop counter is reached.  

e) *What is the difference between RTT and TTL?  
RTT: Time from sending a request to receiving a response from the destination  
TTL: Field in the IPv4 header that "counts" hops starting from a start value down  

f) *What is the function of a resolver?  
Allows recursive name resolution in DNS (usually FQDN to IP address).  

g) *Justify whether a resolver must be located in the same broadcast domain as the requesting client.  
No, as resolvers are addressed on Layer 3/4 (IP + UDP/TCP 53).  

h) *What is meant by a "prefix-free code"?  
A valid codeword is never a prefix of another codeword of the same code.  

i) *Determine the reverse FQDN for 128.66.50.60.  
60.50.66.128.in-addr.arpa.  

j) *What system calls are necessary to create a UDP socket for bidirectional communication?  
socket() and bind()  

k) *What is the shorthand notation for the IPv6 address 2001:0db8:0000:0000:0a00:0000:0000:000c?  
2001:db8::a00:0:0:c  

l) *Briefly explain what SLAAC is used for.  
Automatic and stateless generation/assignment of IPv6 addresses based on the MAC address.  

m) *Name two routing protocols.  
RIP, OSPF, BGP, IGRP, EIGRP, IS-IS  

n) *Justify why a minimum frame size is required in IEEE 802.3.  
Ethernet does not use acknowledgments but detects collisions. If a collision occurs, the affected frame must be resent. To assign a collision to a transmission, it must also be detected during the serialization of the respective frame by the sender.  

o) *Calculate or justify the necessary signal power P so that with a noise power of P_S = 1.0 mW, a signal-to-noise ratio of 6 dB is achieved.  
SNR = 10·log(P/P_N) ⇔ P_S = 10^(SNR/10)·P_N = 10^(6/10)·1 mW ≈ 3.98 mW  

p) *Given an alphabet with a total of 64 different characters with equal probabilities. Justify whether the average codeword length when using Huffman coding is greater than, equal to, or less than 6 bits.  
Since the occurrence probability of the characters is uniformly distributed, all codewords have the same length. A complete binary tree of height log(64) = 6 is created, so the average codeword length is equal to 6 bits.  

---

**Task 2**  
Sampling and Quantization (11 Points)  
Given is the time signal s(t) shown in Figure 2.1. This was created by modulating rectangular pulses onto a cosine carrier of frequency f = 1.  
This signal is to be sampled and quantized, and its information recovered.  

a) *Sample the signal s(t) at the time points t[n] = n + 0.5 for n = 0, 1, ... . Enter the sample values in Figure 2.1 and give the sample values s[n] in decimal notation in the designated row.  
Assuming that s(t) is uniformly distributed in the interval I = [-2; 2]. The sample values are to be quantized into four discrete values such that the quantization error in I is minimized.  

b) *Specify the quantization levels.  
In I, equidistantly chosen levels minimize the error. The levels are therefore:  
S = {-1.5, -0.5, 0.5, 1.5}  

c) *Determine the maximum quantization error within I.  
With N = 4 quantization levels, we obtain for the max. error within I (quantization error of the 1st kind)  
Δ = (b - a) / 2N = (2 - (-2)) / 8 = 0.5  

d) Enter the quantized sample values ŷ[n] in Figure 2.1 in the designated row.  

e) *How many bits are needed to represent the quantization levels?  
n = log2(N) = 2 bits  

f) *Briefly justify which modulation method was likely used in the generation of s(t).  
QAM can be excluded, as the task only used a cosine carrier. In 4-PSK, phase jumps of 90° and 270° could occur, but only phase jumps of 0° and 180° occur.  
⇒ Amplitude Shift Keying with four levels (4-ASK), as the individual sample values only differ in their amplitudes and lie close to the four expected quantization levels.  

g) *Provide a valid signal space assignment.  
Note: There are several possible solutions. Providing one solution is sufficient.  
Q = {00, 01, 10, 11}  

---

**Task 3**  
Data Matrix in Grain Fields (15 Points)  
The Moepisi from the planet Gliese 587 have made great technological advances and discovered a new planet - Earth. This planet, it seems, is populated by a strange species. To make contact with these beings, the Moepisi use a laser beam to burn data matrix codes into grain fields.  
To transmit the i-th letter, it is first represented as a 7-bit long ASCII character, which is then encoded as an 8-bit long date d = a + 1. A sequence of k letters is encoded as a polynomial  
d(x) = Σ d_i x^(k - i) with d_i ∈ {0, 1, ..., 255}  

a) *Provide d(x) for the message "Hello" (without quotation marks).  
d(x) = 73x^4 + 102x^3 + 109x^2 + 109x + 112  

b) The message can be secured using Reed-Solomon code, as both defects can occur in the grain field transmission. This is a block code that maps a data block d(x) of length k bytes to a code block c(x) of length n bytes. Within a code block, a certain number of erroneous bytes can be corrected.  

c) *Justify whether the procedure described here is channel coding or source coding.  
Channel coding, as structured redundancy is added to the message to enable error correction.  

**Note:** If you could not solve sub-task a), use the polynomial d(x) = 78x^4 + 112x^3 + 102x^2 + 113x + 106 for the following sub-tasks.  
The code block c(x) for a data block d(x) is calculated according to  
c(x) = d(x)·x^n-k + e(x), where e(x) = d(x)·x^n-k mod r(x) represents the redundant information. In this case, k = 5B is mapped to n = 12B. The corresponding reduction polynomial r(x) is  
r(x) = 254x^6 + 92x^5 + 240x^4 + 134x^3 + 144x^2 + 68x + 23.  

d) *In what way does e(x) differ from a checksum, as used, for example, in CRC?  
Channel coding: Error correction  
CRC: Error detection  

e) *Justify how the first 5 bytes of the code block are composed.  
The first 5 bytes correspond to the message d(x) multiplied by x^n-k, which corresponds to a shift of the corresponding position by 7 bytes. Additionally, the degree of e(x) is smaller than n - k and thus e(x) has no influence on the first 5 bytes.  

f) As shown in the solution field for sub-task e), individual symbols in the data matrix are represented as 8 bits in the form of blocks of 3 × 3 pixels, where the two upper right corners of each block remain free. The pixels are numbered according to their significance (1 marks the least significant bit).  

g) *Mark the set (logically 1) bit positions for the second symbol.  

---

**Task 4**  
NAT and Static Routing (15 Points)  
We consider the network shown in Figure 4.1. PC1 and PC2 are connected to each other and to router R1 via switch S. In the local network, the subnet 10.12.121.32/28 is used. Router R1 is connected to a transport network of prefix length 30 with R2, which represents the gateway to the Internet on the side of a service provider.  

a) *Determine the broadcast address of the subnet 10.12.121.32/28.  
Prefix length 28 ⇒ 4 bits host part ⇒ 2^4 = 16 addresses in the subnet ⇒ 10.12.121.47 is the broadcast address.  

b) *Assign IP addresses from the subnet 10.12.121.32/28 to PC1, PC2, and R1. Enter them directly in Figure 4.1.  

c) *Determine the network address of the transport network between R1 and R2.  
Prefix length 30 ⇒ 2 bits host part ⇒ 4 addresses in the subnet. Since R2 has 131.159.205.101, 131.159.205.103 must be the broadcast address, and 131.159.205.100 is therefore the network address.  

d) *Assign R1 an address from the transport network. Enter it directly in Figure 4.1.  

e) *How many /30 subnets are there in the network 131.159.0.0/16?  
2^(30-16) = 2^14 = 16384  

f) *Justify why R1 must support NAT to enable PC1 and PC2 to access the Internet.  
The subnet 10.12.121.32/28 is part of the private address range 10.0.0.0/8, which is why the IP addresses are not globally unique.  

g) *What transport protocol and destination port are used when PC1 accesses the website www.google.de via a browser?  
TCP 443 (as Google uses HTTPS by default).  

---

**Task 5**  
Transport Protocols (22.5 Points)  
We consider a connection between a client C and a server S over the Internet. Operations below the transport layer can be neglected.  

a) *Explain two essential differences between TCP and UDP.  
1. TCP is connection-oriented while UDP operates connectionless, i.e., connection establishment and synchronization are omitted in UDP.  
2. TCP provides a reliable transmission, i.e., packets arrive completely and in the correct order or not at all. UDP works on a best-effort principle, i.e., it does not care about transmission errors or order.  

b) *Sketch the connection establishment as a simplified time-space diagram. For each exchanged message, indicate the sequence number, acknowledgment number, and the set flags.  
Note: Consider the initial sequence numbers given above.  

c) After establishing the connection, C requests the download of a movie, which is then sent by the server. The MSS is 1460B.  
*What is generally meant by an MSS?  
The maximum length of the payload per TCP segment, i.e., the maximum size of a Layer 4 SDU.  

d) *How is the frequently occurring value 1 MSS = 1460B calculated?  
1500B MTU minus IPv4 header and TCP header without options (about 20B).  

e) *Name the two phases that the congestion control mechanism of TCP goes through during the transmission phase (without justification).  
Slow Start and Congestion Avoidance.  

f) *Briefly describe the development of the size of the send window during both congestion control phases.  
Doubling for each fully acknowledged send window during Slow Start.  
Increase of 1 MSS for each fully acknowledged send window during the Congestion Avoidance phase.  

g) We want to determine the time required to transmit the movie, which has a size of L = 600 MiB. Serialization and processing times can be neglected. The initial request for download has already been sent, i.e., S starts directly with sending the movie.  
We consider the size w[k] of the send window at times k · RTT for k = 0, 1, ..., i.e., at the beginning of the k-th time step, k · RTT seconds have passed. The RTT is 10ms, and for k = 0, w[0] = 1 MSS. It is assumed that exactly one segment is lost as soon as Lw[k] ≥ x = 128 MSS. The receive window at C is chosen so that it has no influence on the development of the send window.  

h) *Determine the number n of segments to be transmitted.  
n = L / MSS = 600·2^20 B / 1460 B ≈ 430922  

i) *Determine the time t until the first segment loss occurs in seconds.  
At the beginning, the congestion control window grows by 1 MSS for each acknowledged MSS starting from w[0] = 1 MSS.  
A segment loss occurs as soon as w[n] = x, i.e.,  
k = log2(128) + 1 = 8  
t1 = k1 · RTT = 0.08s  

**Note:** From w[0] to w[7], there are not 7 but 8 transmission steps!  

j) *Determine the number n of successfully transmitted segments until the first segment loss occurs.  
Within these first 8 RTT,  
n1 = 2^k - 1 = 2^(k1 + 1) - 2 = 254 segments are transmitted.  

After the first segment loss, n2 = n - n1 segments remain to be transmitted.  
**Notes:**  
1. If you could not solve sub-task i), assume there are 430668 remaining segments.  
2. Consider the information in the section "Transport Layer" in the formula collection.  

k) *Determine the duration between the occurrence of further segment losses in seconds.  
T = (x / 2) · RTT = (128 / 2) · 10ms = 0.65s  

l) *Determine the remaining time t until the transmission is completed.  
According to the formula collection, for each Congestion Avoidance phase,  
n = 8 · x^2 + 4 · x = |x = 128| = 6240 segments are transmitted.  
Thus, n2/n ≈ 70 phases are passed, where in each phase exactly one segment is lost. Therefore, the remaining time is  
t2 = n20 · 0.65s ≈ 44.86s  

m) *Determine the total time t for data transmission in seconds.  
t = t1 + t2 = 44.93s  

n) *Justify whether UDP would be a sensible alternative for the download considered here.  
No, as UDP does not have any congestion control mechanisms, and thus caused segment losses would not be compensated. The downloaded movie would likely be corrupted.  
(Also acceptable: Argumentation with yes, if congestion control is implemented elsewhere, as individual errors in the video could be tolerable.)  

---

**Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.**