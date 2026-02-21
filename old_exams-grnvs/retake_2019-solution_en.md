Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by affixing a code during the attendance check.  
- This contains only a sequential number, which is also noted on the attendance list next to the signature field.  
- This will be used as a pseudonym to allow for a unique assignment of your exam.  

### Basics of Computer Networks and Distributed Systems  
Exam: IN0010/Retake  
Date: Tuesday, October 8, 2019  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 13:30–15:00  

### Instructions for Processing
- This exam consists of 16 pages with a total of 6 tasks as well as an attached formula collection. Please check now that you have received a complete set of information.  
- The total score for this exam is 90 points.  
- It is prohibited to detach pages from the exam.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - an analog dictionary in the native language without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only results where the solution method is recognizable will be counted. Text tasks must also be justified unless otherwise stated in the respective sub-task.  
- Do not write with red/green colors or with pencil.  
- Turn off all electronic devices you have brought, store them in your bag, and close it.  

### Leaving the Lecture Hall / Early Submission  

---

### Task 1  
Short Tasks (17 Points)  
The following sub-tasks are to be answered independently of each other.  

a) *Name the necessary syscalls in the correct order to create a connection-oriented socket and connect to a server.*  
- `socket()`  
- `connect()`  

b) *What is the purpose of SLAAC?*  
For the automatic configuration of IPv6 addresses based on Prefix Announcement and MAC address.  

c) *Given the 16-bit long data 10101010 11001100 in Network Byte Order. Provide the data in binary in Little Endian.*  
11001100 10101010  

d) *Name the essential tasks of the network layer.*  
End-to-end addressing  

e) *Explain the difference between a nameserver and a resolver.*  
Nameservers are authoritative for one or more zones and only respond to queries regarding these zones.  
Resolvers resolve queries iteratively using the respective responsible nameservers (or recursively forward them to another resolver) and return the final result to the requestor.  

f) *Briefly explain the difference between an MST and an SPT.*  
MST: Minimum spanning tree that connects all nodes at the overall minimal edge cost (metric: sum of the costs of all edges).  
SPT: Spanning tree that makes all other nodes reachable from a starting node via the shortest path (metric: sum of the costs along a path from the root to its target).  

g) *Sketch a non-constant, time-continuous signal \( s(t) \) that has a purely real spectrum.*  

h) *Calculate or justify the necessary signal power \( P \) so that with a noise power of \( S_0 \), a signal-to-noise ratio of 6 dB is achieved.*  
\[
SNR = 10 \log \left( \frac{S}{P} \right) = 10 \cdot \frac{SNR}{10} \Rightarrow P = \frac{10^{6/10}}{1 \text{ mW}} \approx 3.98 \text{ mW}
\]  

i) *Determine the IP address in your usual and fully shortened notation for the reverse FQDN 4.4.8.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.6.8.4.6.8.4.0.1.0.0.2.ip6.arpa.*  
2001:486:4860::8844  

j) *An analog signal is to be quantized with 3 bits. The maximum quantization error within the quantization interval [a; b] should not exceed 1/8. The current mean value of the signal is 0, i.e., the quantization interval is centered around 0. Determine the interval boundaries.*  
- Since the interval is centered around 0, \( b = a \).  
- \( M = 2^3 = 8 \)  
- Maximum error \( \Delta = 1/4 \)  
- \( a = -2 \) and \( b = 2 \)  

---

### Task 2  
Dynamic Routing (16 Points)  
Given the simplified network depicted in Figure 2.1. All routers use RIP as the routing protocol. The tables in Figure 2.1 show the contents of the routing tables of the respective routers after RIP has reached a convergent state.  

| A | B | C | D |  
|---|---|---|---|  
| Dst | GW | Cost | Dst | GW | Cost | Dst | GW | Cost | Dst | GW | Cost |  
| B | - | 0 | A | - | 0 | A | - | 0 | A | B | 1 |  
| C | - | 0 | C | - | 0 | B | - | 0 | B | - | 0 |  
| D | B | 1 | D | - | 0 | D | - | 0 | C | - | 0 |  

**Figure 2.1: Simplified Network Topology**  

a) *What metric does RIP use?* (without justification)  
Hop Count  

b) *To which class of routing protocols does RIP belong?* (without justification)  
Distance Vector  

c) *To what extent are networks whose routers exclusively use RIP as a routing protocol limited in size?*  
The hop count of 15 is interpreted as unreachable.  

d) *What two components does an update contain that a RIP router regularly sends?*  
Destination and cost to the destination.  

e) *What essential information is not contained in such an update of the own routing table?*  
Which next hop is required to reach the respective destination.  

f) *Justify whether RIP always chooses the fastest route to a destination.*  
No, because RIP only considers the number of hops but not data rate and delay.  

The location where router D is located experienced a power outage, which caused the connections to routers B and C to be severed. We assume that the failure of these routers is also immediately recognized.  

g) *Provide the routing table of the remaining routers immediately after the failure.*  

| A | B | C |  
|---|---|---|  
| Dst | GW | Cost | Dst | GW | Cost | Dst | GW | Cost |  
| B | - | 0 | A | - | 0 | A | - | 0 |  
| C | - | 0 | C | - | 0 | B | - | 0 |  
| ∞ | ∞ | ∞ |  
| D | B | 1 | D | - | D | - |  

h) *Provide the routing tables after router A has sent a regular update.*  

| A | B | C |  
|---|---|---|  
| Dst | GW | Cost | Dst | GW | Cost | Dst | GW | Cost |  
| B | - | 0 | A | - | 0 | A | - | 0 |  
| C | - | 0 | C | - | 0 | B | - | 0 |  
| D | B | 1 | D | A | 2 | D | A | 2 |  

i) *Provide the routing tables after router B has sent a regular update.*  

| A | B | C |  
|---|---|---|  
| Dst | GW | Cost | Dst | GW | Cost | Dst | GW | Cost |  
| B | - | 0 | A | - | 0 | A | - | 0 |  
| C | - | 0 | C | - | 0 | B | - | 0 |  
| D | B | 3 | D | A | 2 | D | A | 2 |  

j) *Provide the routing tables after router C has sent a regular update.*  

| A | B | C |  
|---|---|---|  
| Dst | GW | Cost | Dst | GW | Cost | Dst | GW | Cost |  
| B | - | 0 | A | - | 0 | A | - | 0 |  
| C | - | 0 | C | - | 0 | B | - | 0 |  
| D | B | 3 | D | A | 2 | D | A | 2 |  

k) *Describe the further process if routers A, B, and C continue to send an update every 30 seconds in that order.*  
When A sends the next update, the costs to B and C will rise to 4. This continues until the costs reach 15, and the route to D is therefore marked as unreachable.  

---

### Task 3  
Worst-Case Analysis (15 Points)  
To verify the performance characteristics of a design, a worst-case analysis can be helpful. This involves examining the most unfavorable of all possible cases. The following is to conduct such an analysis for a Telnet connection. Telnet is a character-oriented protocol based on TCP. Similar to SSH, commands can be executed on a server reachable over the network using Telnet.  

**Figure 3.1: Telnet Network Topology: Client sends user input to server**  

For the worst-case analysis, the data transmission from a Telnet client to the server is to be examined. A Telnet connection has already been established. Figure 3.1 shows the network topology. In the considered scenario, Ethernet and IPv4 are used as Layer 2 and 3 protocols.  

a) *How can Telnet prevent the TCP stacks of the sender and receiver from buffering information?*  
By enforcing the TCP PSH flag.  

b) *Why is preventing buffering by the TCP stack sensible for Telnet?*  
Telnet is interactive; buffering during closed input can lead to additional, undesirable transmission delays.  

c) *Why is it generally sensible for TCP to attempt to buffer data?*  
To maximize the ratio of payload to segment size. In other words, it attempts to minimize the overhead caused by headers through buffering.  

d) *Determine the maximum size of a TCP header in bytes. (Justification!)*  
TCP Header Field Data Offset (4 bits)  
Header size in multiples of 32 bits.  
Maximum: 60B  

e) *Determine the maximum size of an IPv4 header in bytes. (Justification!)*  
IPv4 Header Field IHL (4 bits)  
Header size in multiples of 32 bits.  
Maximum: 60B  

f) *Determine the minimum ratio of Layer 4 SDU to Layer 2 PDU.*  
- Minimum Layer 4 SDU: 1B  
- Maximum overhead: 14B (+4B) + 2 = 60B ≈ 134B (138B)  
- Ratio: \( \frac{0.0074074}{1} > v > \frac{1}{0.0071942446} \)  

g) In RFC 791 Section 3.2, the following statement can be found: "Every internet module must be able to forward a datagram of 68 octets without further fragmentation."  

h) *Justify the above statement from RFC 791.*  
In the words of the cited RFC 791: "This is because an internet header may be up to 60 octets, and the minimum fragment is 8 octets."  

i) *Justify how many packets are needed at most, assuming a minimum MTU, to transport 1B of payload with Telnet?*  
61B TCP/Telnet payload, 8B per fragmented packet.  
The number of packets required is therefore: \( \frac{61B}{8B} \).  

The above calculation assumes the use of IPv4. The influence of a switch to IPv6 will now be examined.  

j) *What challenge arises for calculating the ratio of Layer 4 SDU to Layer 2 PDU (as in sub-task f) due to the use of IPv6?*  
There is no fixed upper limit for the total size of all IPv6 extension headers.  

In the IPv6 specifying RFC 8200, the following passage can be found: "IPv6 requires that every link in the Internet have an MTU of 1280 octets or greater."  

k) *Assuming the Layer 3 header can be estimated at 100B. What follows from the cited RFC 8200 passage for the number of transmitted IPv6 packets?*  
The packet size remains below the minimum link MTU, so it does not need to be fragmented. The number of IPv6 packets transmitted by the sender is therefore: 1.  

---

### Task 4  
Wireshark (20 Points)  
Given the network as depicted in Figure 4.1. Router R1 is connected to the Internet via a typical household DSL connection. The packet shown is directed from PC1 to Srv.  

**Figure 4.1: Network Topology**  

The offset is the index into the byte array and must be specified as 0-based (as in Java code). Provide interpreted data such as addresses or ports in their usual and shortened notation.  

**Note:** Use the header and information printed on the cheatsheet for the solution.  
Example: Determine the Layer 2 address of the recipient.  

Offset: 0x0000 Length: 6  
Address: 90:e2:ba:2a:8d:97 belongs to node: <Name>  

a) *Show whether the recipient address is a multicast address.*  
The least significant bit of the first byte (0x90) of the recipient address is 0, indicating Unicast.  

b) *Determine the Layer 2 address of the sender.*  
Offset: 0x0006 (6) Length: 6  
Address: 90:e2:ba:86:dd:60 belongs to node: R1  

c) *How can the type of the payload be recognized?*  
Offset: 0x000c (12) Length: 2  

**Figure 4.2 shows the format of the PPPoE header that follows directly after the Ethernet header. This is another Layer 2 header used for communication between the routers of different households and a regional broadband router of a service provider.**  

d) *Mark the individual fields of the PPPoE header directly in Figure 4.1b.*  

e) *What is the MTU for typical Fast Ethernet?* (without justification)  
1500B  

f) *What is the MTU in the present case?* (without justification)  
1492B  

g) *What impact does this have on layers 3 and 4?*  
Since the MTU is smaller, it must either be fragmented at layer 3 or the MSS must be chosen correspondingly smaller.  
From the value "PPPProtocol," it can be inferred that the payload is an IPv6 packet.  

h) *Determine the Layer 3 address of the sender.*  
Offset: 0x001e (30) Length: 16  
Address: 2001:4ca0:2001:11:a188:65ad:93a5:948  

i) *Determine the Layer 3 address of the recipient.*  
Offset: 0x002e (46) Length: 16  
Address: 2001:4860:4860::8888  

j) *Justify how it can be recognized that the L3 header has a length of 40B.*  
The IPv6 header is always exactly 40B long (fixed length).  

k) *Determine the further payload of the IP packet (type/content). (Justification!)*  
ICMPv6 (NextHeader=0x3a at Offset 0x001c), Type 128/Code 0 Echo Request  

---

### Task 5  
CRC (11 Points)  
In the lecture, both error-detecting and error-correcting codes were presented.  

a) *Briefly justify whether an error-correcting code is automatically also an error-detecting code.*  
How should an error be corrected if it is not even recognized?  

b) *Is CRC used for Ethernet for error detection or error correction?*  
In general, only for error detection.  

c) We will consider CRC as introduced in the lecture. Given the reduction polynomial \( r(x) = x^2 + 1 \).  

d) *What is \( r(x) \) needed for?*  
A message of arbitrary length is mapped to a checksum of fixed length (here 2 bits).  

e) *When is \( r(x) \) irreducible?*  
If it cannot be expressed as the product of two polynomials of strictly smaller degree.  

f) *Show whether \( r(x) \) is irreducible.*  
\((x + 1)^2 = x^2 + 2x + 1 = x^2 + 1 = r(x) \) (since coefficients are taken modulo 2).  

g) *Name one advantage or a property resulting from using an irreducible polynomial for \( r(x) \).*  
In this case, a field with \( 2^n \) elements is formed with the help of \( r(x) \) and appropriately defined addition and multiplication, where \( n \) is the degree of the reduction polynomial.  

h) *Briefly explain why an irreducible polynomial is often not chosen for a reduction polynomial for CRC. Give an example for CRC32 if applicable.*  
By specifically choosing the polynomial, certain error patterns can be reliably detected, e.g., the choice of the CRC32 polynomial detects all odd-numbered errors, even if they are longer than the reduction polynomial.  

A binary message given as the polynomial \( m(x) = x^5 + x^4 + x^2 + 1 \) could, among other specifications, be represented as 110101 or also, for example, 00110101.  

i) *Why are the two representations not equivalent?*  
They differ in length, as the length of the message or data word is missing in the specification.  
(There is indeed a difference whether 6 bits, 8 bits, or 42 bits are transmitted – and since it is not known in the context of the task whether we are dealing with octet speakers, we cannot simply omit the leading zeros.)  

We assume the representation 00100101 for \( m(x) \). The calculation of the CRC checksum with \( r(x) \) as the reduction polynomial is given as follows:  
00110101 000 mod 101 = 1g00  
101  
001  
110  
101  
001  
11 0  
10 1  
00 100  

j) *Describe the errors made in the above calculation. Also point out any resulting follow-up errors if applicable.*  
1. \( m(x) \) must be multiplied by \( x^2 \) and not \( x^3 \).  
2. The polynomial division is performed in the decimal system with carry instead of using XOR.  
3. The remainder is only 2 bits long, as \( m(x) \) is of degree 2. (Follow-up error of 1)  

---

### Task 6  
Multiple Choice (11 Points)  
The following sub-tasks can be solved independently of each other and come from the quizzes accompanying the lecture. The grading scheme also corresponds to that of the quizzes: 1 or 0 points for tasks with only one correct answer or a gradation to 0.5 points for a missing or incorrect answer, provided more than one answer is correct.  

Please mark the correct answers.  
Crossed answers can be struck through by completing the fill-in.  
Struck answers can be crossed out by marking next to them.  

a) *Which statements about Fourier series and Fourier transformations are correct regarding time-continuous signals?*  
- Using Fourier transformation, the spectrum of periodic signals can be determined.  
- Using Fourier series, the spectrum of periodic signals can be determined.  
- Using Fourier transformation, the spectrum of non-periodic signals can be determined.  
- Using Fourier series, the spectrum of non-periodic signals can be determined.  

b) *Given are the figures 6.1(a)–(d) below. Which signal properties apply?*  
- (a) time-discrete  
- (b) time-continuous  
- (c) time-continuous  
- (d) time-discrete  

c) *Given are the figures 6.1(a)–(d) below. Which signal properties apply?*  
- (a) value-continuous  
- (b) value-discrete  
- (c) value-continuous  
- (d) value-discrete  

d) *What tasks are related to the data link layer?*  
- Control of media access  
- Addressing between direct connection networks  
- Congestion control when forwarding messages  
- Protection against unauthorized eavesdropping of messages  
- Addressing in a direct connection network  
- Checking messages for transmission errors  

e) *Mark the matrix that represents the adjacency matrix for the network above as presented in the lecture.*  

f) *Given is the distance matrix D for the network above. For which minimum does \( D_n = D_{n+1} \) hold?*  
- \( n = 7 \)  
- \( n = 6 \)  
- \( n = 4 \)  
- \( n = 2 \)  
- \( n = 5 \)  
- \( n = 0 \)  
- \( n = 3 \)  
- \( n = 1 \)  

g) *The serialization time...*  
- is part of the delay between sender and receiver.  
- can be determined from the bandwidth-delay product.  
- gives the necessary time for serializing a single bit.  
- is the quotient of \( D_n \) distance between sender/receiver and the signal speed.  
- is the quotient of frame length and data rate.  

h) *How many broadcast domains does the adjacent network consist of?*  
- 5  
- 4  
- 3  
- 2  
- 1  
- 6  

i) *How many collision domains does the adjacent network consist of?*  
- 4  
- 5  
- 2  
- 1  
- 6  
- 3  

j) *Which of the following terms describe categories of IEEE 802.11 frame types?*  
- Management  
- Info  
- Data  
- Control  

k) *Which statements about IEEE 802.11 Access Points (APs) are correct?*  
- APs are transparent to all participants.  
- APs are only transparent within the wireless network.  
- APs are transparent to participants outside the wireless network.  
- APs are fundamentally directly addressed and are therefore not transparent.  

---

### Additional space for solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to strike out invalid solutions.