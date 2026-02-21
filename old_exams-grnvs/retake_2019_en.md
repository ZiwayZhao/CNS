Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during attendance control by attaching a code sticker.  
- This contains only a sequential number, which is also noted on the attendance list next to the signature field.  
- **Sticker with SRID to be attached here**  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Retake  
Date: Tuesday, October 8, 2019  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 13:30–15:00  

### Instructions for Processing  
- This exam consists of 16 pages with a total of 6 tasks as well as an attached formula collection. Please check now that you have received a complete set of information.  
- The total score for this exam is 90 points.  
- The removal of pages from the exam is prohibited.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - an analog dictionary in the native language without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be counted where the solution method is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-task.  
- Do not write in red/green colors or with a pencil.  
- Turn off all electronic devices you have with you, store them in your bag, and close it.  

### Leaving the Lecture Hall from until / Early Submission by  

---  
### Task 1  
Short Tasks (17 Points)  
The following sub-tasks are to be answered independently of each other.  

a) *Name the necessary syscalls in the correct order to create a connection-oriented socket and connect to a server.  
b) *What is the purpose of SLAAC?  
c) *Given the 16-bit long date 10101010 11001100 in Network Byte Order. Provide the date in binary in Little Endian.  
d) *Name the essential task of the network layer.  
e) *Explain the difference between a nameserver and a resolver.  
f) *Briefly explain the difference between an MST and an SPT.  
g) *Sketch a non-constant, time-continuous signal s(t) that has a purely real spectrum.  
h) *Calculate or justify the necessary signal power P so that with a noise power of S, a signal-to-noise ratio of 6 dB is achieved.  
i) *Determine the IP address in your usual and fully shortened notation for the reverse FQDN 4.4.8.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.6.8.4.6.8.4.0.1.0.0.2.ip6.arpa.  
j) *An analog signal is to be quantized with 3 bits. The maximum quantization error within the quantization interval [a;b] should not exceed 1/8. The current average value of the signal is 0, i.e., the quantization interval is centered around 0. Determine the interval boundaries.  

---  
### Task 2  
Dynamic Routing (16 Points)  
Given is the simplified network shown in Figure 2.1. All routers use RIP as the routing protocol. The tables in Figure 2.1 represent the contents of the routing tables of the respective routers after RIP has reached a convergent state.  

| A | B | C | D |  
|---|---|---|---|  
| Dst | GW | Cost | Dst | GW | Cost | Dst | GW | Cost | Dst | GW | Cost |  
| B | - | 0 | A | - | 0 | A | - | 0 | A | B | 1 |  
| C | - | 0 | C | - | 0 | B | - | 0 | B | - | 0 |  
| D | B | 1 | D | - | 0 | D | - | 0 | C | - | 0 |  

**Figure 2.1: Simplified Network Topology**  

a) *What metric does RIP use? (without justification)  
b) *To which class of routing protocols does RIP belong? (without justification)  
c) To what extent are networks whose routers exclusively use RIP as the routing protocol limited in size?  
d) *What two components does an update contain that a RIP router regularly sends?  
e) What essential information from its own routing table is not contained in such an update?  
f) Justify whether RIP always chooses the fastest route to a destination.  

The location where router D is situated experienced a power outage, causing the connections to routers B and C to be severed. We assume that the failure of these routers is also immediately recognized.  

g) *Provide the routing table of the remaining routers immediately after the outage.  
h) Provide the routing tables after router A sends a regular update.  
i) Provide the routing tables after router B sends a regular update.  
j) Provide the routing tables after router C sends a regular update.  
k) Describe the further process if routers A, B, and C continue to send an update every 30 seconds in that order.  

---  
### Task 3  
Worst-Case Analysis (15 Points)  
To check the performance properties of a design, a worst-case analysis can be helpful. This involves examining the most unfavorable of all possible cases. Below, such an analysis is to be conducted for a Telnet connection. Telnet is a character-oriented protocol based on TCP. Similar to SSH, commands can be executed on a server accessible over the network using Telnet.  

**Figure 3.1: Telnet Network Topology: Client sends user input to server**  

For the worst-case analysis, the data transmission from a Telnet client to the server is to be examined. A Telnet connection has already been established. Figure 3.1 illustrates the network topology. In the considered scenario, Ethernet and IPv4 are used as Layer 2 and Layer 3 protocols.  

a) *How can Telnet prevent the TCP stacks of sender and receiver from buffering information?  
b) *Why is preventing buffering by the TCP stack sensible for Telnet?  
c) *Why is it generally sensible for TCP to attempt to buffer data?  
d) *Determine the maximum size of a TCP header in bytes. (Justification!)  
e) *Determine the maximum size of an IPv4 header in bytes. (Justification!)  
f) *Determine the minimum ratio of Layer 4 SDU to Layer 2 PDU.  

In RFC791 Section 3.2, the following statement can be found: “Every internet module must be able to forward a datagram of 68 octets without further fragmentation.”  

g) *Justify the above statement from RFC791.  
h) *Justify how many packets are maximally needed, assuming a minimum MTU, to transport a Telnet payload?  

The above calculation assumes the use of IPv4. Next, the impact of switching to IPv6 will be examined.  

i) What challenge arises for calculating the ratio of Layer 4 SDU to Layer 2 PDU (as determined in sub-task f) due to the use of IPv6?  
j) Assuming the Layer 3 header can be estimated at 100 B, what follows from the cited RFC8200 passage for the number of transmitted IPv6 packets?  

---  
### Task 4  
Wireshark (20 Points)  
Given is the network from Figure 4.1. Router R1 is connected to the Internet via a standard DSL connection. The depicted packet is directed from PC1 to Srv.  

**Figure 4.1a: Network Topology**  

```
0x0000 90 e2 ba 2a 8d 97 90 e2 ba 86 dd 60 88 64 11 00  
0x0010 0d 42 00 56 00 57 60 06 7d 4c 00 40 3a 40 20 01  
0x0020 4c a0 20 01 00 11 a1 88 65 ad 93 a5 09 48 20 01  
0x0030 48 60 48 60 00 00 00 00 00 00 00 00 88 88 80 00  
0x0040 df 0e 6a d2 00 1b 92 df 89 5d 00 00 00 00 e5 57  
0x0050 0b 00 00 00 00 00 10 11 12 13 14 15 16 17 18 19  
0x0060 1a 1b 1c 1d 1e 1f 20 21 22 23 24 25 26 27 28 29  
0x0070 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35 36 37  
```

**Figure 4.1b: Ethernet Frame between R1 and R2**  

The offset is the index in the byte array and must be specified as 0-based (as in Java code). Provide interpreted data such as addresses or ports in their usual and shortened notation.  

**Note:** Use the printed header and information from the cheatsheet for the solution.  
Example: Determine the Layer 2 address of the recipient.  
Offset: 0x0000 Length: 6  
Address: 90:e2:ba:2a:8d:97 belongs to node: <Name>  

a) *Show whether the recipient address is a multicast address.  
b) *Determine the Layer 2 address of the sender.  
Offset: Length:  
Address: belongs to node:  

c) *How can the type of the payload be recognized?  

**Figure 4.2 shows the format of the PPPoE header that follows directly after the Ethernet header. This is another Layer 2 header that serves communication between routers of different households and a regional broadband router of a service provider.**  

```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
0B Version Type Code SessionID  
4B Length PPPProtocol  
8B Payload  
```

**Figure 4.2: Structure of the PPPoE Header**  

d) Mark the individual fields of the PPPoE header directly in Figure 4.1b.  
e) *What is the MTU for standard Fast Ethernet? (without justification)  
f) *What is the MTU in the present case? (without justification)  
g) *What impact does this have on Layers 3 and 4?  

From the value "PPPProtocol," it is evident that the payload is an IPv6 packet.  
h) *Determine the Layer 3 address of the sender.  
Offset: Length:  
Address:  

i) *Determine the Layer 3 address of the recipient.  
Offset: Length:  
Address:  

j) *Justify how it can be recognized that the Layer 3 header has a length of 40 B.  
k) *Determine the exact and further payload of the IP packet (type/content). (Justification!)  

---  
### Task 5  
CRC (11 Points)  
In the lecture, both error-detecting and error-correcting codes were presented.  
a) *Briefly justify whether an error-correcting code is automatically also an error-detecting code.  
b) *Is CRC used for error detection or error correction in Ethernet?  

We will now consider CRC as introduced in the lecture. Given is the reduction polynomial r(x) = x^2 + 1.  
c) *What is r(x) needed for?  
d) *When is r(x) irreducible?  
e) *Show whether r(x) is irreducible.  
f) *Name one advantage or a property resulting from using an irreducible polynomial for r(x).  
g) *Briefly explain why, for a reduction polynomial for CRC, an irreducible polynomial is often not chosen. If applicable, provide an example for CRC32.  

A binary message given as the polynomial m(x) = x^5 + x^4 + x^2 + 1 could – due to lack of further information – be represented as 110101 or also, for example, 00110101.  
h) *Why are the two representations not equivalent?  

We start from the representation 00100101 for m(x). Below is the calculation of the CRC checksum with r(x) as the reduction polynomial:  

```
00110101 000 mod 101 = 100  
```

i) *Describe the errors made in the above calculation. Also point out any resulting follow-up errors if applicable.  

---  
### Task 6  
Multiple Choice (11 Points)  
The following sub-tasks can each be solved independently and come from the quizzes accompanying the lecture. The grading scheme also corresponds to that of the quizzes: 1 or 0 points for tasks with only one correct answer or a gradation to 0.5 points for a missing or incorrect answer, provided more than one answer is correct.  

**Mark the correct answers**  
- Correct answers can be crossed out by completing the fill-in.  
- Crossed-out answers can be re-marked by the adjacent markers.  

a) *Which statements about Fourier series and Fourier transformations are correct regarding time-continuous signals?  
- The Fourier transformation allows determining the spectrum of periodic signals.  
- The Fourier series allows determining the spectrum of periodic signals.  
- The Fourier transformation allows determining the spectrum of non-periodic signals.  
- The Fourier series allows determining the spectrum of non-periodic signals.  

b) *Given are the figures 6.1(a)–(d) below. Which signal properties apply?  
- (a) time-discrete  
- (b) time-continuous  
- (c) time-continuous  
- (d) time-discrete  

c) *Given are the figures 6.1(a)–(d) below. Which signal properties apply?  
- (a) value-continuous  
- (b) value-continuous  
- (c) value-discrete  
- (d) value-continuous  

**Figure 6.1: Signals**  

d) *Which of the following tasks pertain to the data link layer?  
- Control of media access  
- Addressing between direct connection networks  
- Congestion control when forwarding messages  
- Protection against unauthorized eavesdropping of messages  
- Addressing in a direct connection network  
- Checking messages for transmission errors  

e) *Cross out the matrix that represents the adjacency matrix for the network above as discussed in the lecture.  

f) *Given the distance matrix D for the adjacent network. For which minimum does Dn = Dn+1 hold?  

g) *The serialization time...  
- is part of the delay between sender and receiver.  
- can be determined from the bandwidth-delay product.  
- gives the necessary time for serializing a single bit.  
- is the quotient of the distance between sender/receiver and the signal speed.  
- is the quotient of frame length and data rate.  

h) *How many broadcast domains does the adjacent network consist of?  

i) *How many collision domains does the adjacent network consist of?  

j) *Which of the following terms describe categories of IEEE 802.11 frame types?  
- Management  
- Info  
- Data  
- Control  

k) *Which statements about IEEE 802.11 Access Points (APs) are correct?  
- APs are transparent to all participants.  
- APs are only transparent within the wireless network.  
- APs are transparent to participants outside the wireless network.  
- APs are generally addressed directly and are therefore not transparent.  

---  
### Additional space for solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to cross out invalid solutions.