Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Please sign only after attaching the sticker with the QR code during the attendance check.  
- Your signature should extend somewhat onto the sticker and reach the other half onto the cover sheet.  
- By signing, you also confirm the correctness of the student ID number printed on the sticker.  
*The QR code on the sticker contains only a four-digit identification number, which allows us to automatically assign your exam. No personal data is included.*

**Fundamentals of Computer Networks and Distributed Systems**  
Module: IN0010 Date: 21.09.2015  
Examiner: Prof. Dr. Uwe Baumgarten Exam: Repetition  

**A1 A2 A3 A4 A5**  
First Correction  
Second Correction  
Leaving the auditorium from to  
from to  
Submitted early by  
Other  
Repetition  

**Fundamentals of Computer Networks and Distributed Systems**  
Prof. Dr. Uwe Baumgarten  
Department of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  
Monday, 21.09.2015  
11:00–12:30  

- This exam comprises  
  - 24 pages with a total of 5 tasks as well as  
  - a double-sided formula collection.  
  Please check now that you have received a complete set of information.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be counted where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write in red/green colors or with a pencil.  
- The total number of points is 85.  
- The following aids are allowed:  
  - a non-programmable calculator  
  - an analog dictionary German ↔ native language without annotations  
- Please turn off your mobile phones completely and pack them as well as all other electronic devices and other materials into your bags and close them.  

---

**Task 1**  
NAT and Static Routing (19 Points)  
We consider the network from Figure 1.1. PC1 and PC2 are connected to each other and to the router R1 via the switch S. The local network uses addresses from the subnet 172.18.32.128/26. The router R1 is connected to a transport network with a prefix length of 30 with R2 and the Internet.

```
131.159.132.134
eth0
eth0
www.google.de
PC1
eth0 eth1
eth1 eth1 eth0
S R3
eth0
eth2 R1 R2 eth2
eth0 eth0
www.google.com
PC2
```

**Figure 1.1: Network Topology**  

a) * Determine the broadcast address of the subnet 172.18.32.128/26.  

b) * Assign IP addresses from the subnet 172.18.32.128/26 to PC1, PC2, and R1. Enter them directly into Figure 1.1.  

c) * Determine the network address of the transport network between R1 and R2.  

d) Assign R1 an address from the transport network. Enter this directly into Figure 1.1.  

e) * How many /30 subnets are there in the network 131.159.132.0/24?  

f) * Justify why R1 must support NAT to enable PC1 and PC2 to access the Internet.  

g) * What transport protocol and destination port are used when PC1 accesses the website www.google.de via a browser?  

In the following, we will abbreviate IP and MAC addresses according to the schema <Device>.<Interface>, e.g., R1.eth0 for the corresponding address at interface eth0 of router R1. Note that there are four additional routers between R2 and R3. PC1 is now accessing the website www.google.de.  

h) Complete the header fields for the request from PC1 to www.google.de in the three empty boxes in Figure 1.2. If a field cannot be determined unambiguously, make a sensible choice.  

**Note:**  
- If you could not solve sub-task 1g), assume destination port 443.  
- The hostname of the server hosting www.google.de can be abbreviated as "G".  

i) Complete the header fields for the response from www.google.de to PC1 in the three empty boxes in Figure 1.3. If a field cannot be determined unambiguously, make a sensible choice.  
**Note:**  
- The hostname of the server hosting www.google.de can be abbreviated as "G".  

---

**Task 2**  
Neighbor Discovery (18 Points)  
We now consider the scenario from Figure 2.1. Host A knows the IP addresses of Host B. To find out the MAC address, A sends a Neighbor Solicitation message.

```
A B
IPv4: 192.0.2.10 IPv4: 192.0.2.11  
IPv6: 2001:db8::123:4567 IPv6: 2001:db8::89ab:cdef  
MAC: 00:00:5e:00:53:aa MAC: 00:00:5e:00:53:bb  
```

**Figure 2.1: Network Topology for Neighbor Discovery**  

a) * What is the essential difference between addresses at Layer 2 and Layer 3 regarding their use?  

b) * Argue which layer of the ISO/OSI model the Neighbor Discovery Protocol belongs to.  

c) Provide the L3-SDU for the sent Neighbor Solicitation message in hexadecimal notation. If a field cannot be determined unambiguously, make a sensible choice. Any checksums should be marked with "xx".  
**Note:** Each box corresponds to an octet. More space than needed is provided. The formula collection contains the necessary messages and headers.  

```
offset in octets +0x0 +0x1 +0x2 +0x3 +0x4 +0x5 +0x6 +0x7  
0x0000  
0x0008  
0x0010  
0x0018  
0x0020  
0x0028  
```

d) * What function does the ICMP checksum serve?  

e) * Explain which parts of the L3-PDU are considered when calculating the ICMP checksum.  

f) * Differentiate between unicast, multicast, and broadcast.  

To work on the following sub-tasks without flipping pages, you will need the addresses from Figure 2.1, which is printed again below:  

```
A B  
IPv4: 192.0.2.10 IPv4: 192.0.2.11  
IPv6: 2001:db8::123:4567 IPv6: 2001:db8::89ab:cdef  
MAC: 00:00:5e:00:53:aa MAC: 00:00:5e:00:53:bb  
```

**Copy of Figure 2.1**  

```
0x0000 60 00 00 00 00 20 3a ff  
0x0008 20 01 0d b8 00 00 00 00  
0x0010 00 00 00 00 01 23 45 67  
0x0018 ff 02 00 00 00 00 00 00  
0x0020 00 00 00 00 ff ab cd ef  
0x0028 – – – – – – – –  
```

g) * Determine the Solicited-Node address for B.  

h) Provide the L3 header of the sent Neighbor Solicitation message in hexadecimal notation. If a field cannot be determined unambiguously, make a sensible choice.  
**Note:** Each box corresponds to an octet. More space than needed is provided. The formula collection contains the necessary messages and headers.  

```
offset in octets +0x0 +0x1 +0x2 +0x3 +0x4 +0x5 +0x6 +0x7  
0x0000  
0x0008  
0x0010  
0x0018  
0x0020  
0x0028  
```

i) Determine the multicast MAC address for the Solicited-Node address from sub-task 2g).  

j) Provide the Ethernet header of the sent packet in hexadecimal notation. If a field cannot be determined unambiguously, make a sensible choice.  
**Note:** Each box corresponds to an octet. More space than needed is provided. The formula collection contains the necessary messages and headers.  

```
offset in octets +0x0 +0x1 +0x2 +0x3 +0x4 +0x5 +0x6 +0x7  
0x0000  
0x0008  
0x0010  
```

---

**Task 3**  
Transport Protocols (19 Points)  
In this task, we consider the two transport protocols TCP and UDP in the context of the example network from Figure 3.1. The achievable data rate between computer A and router R is 100 kB/s, while between R and computer B it is only 9 kB/s.

```
rAR=100kB/s eth0 eth1 rRB=9kB/s  
/ /  
A R B  
Qmax=6kB  
```

**Figure 3.1: Network Topology**  

Since A can send data faster than R can forward it, R has a buffer (queue) where segments can be temporarily stored. This buffer has a size of Q = 6 kB. If the buffer overflows, further incoming messages are simply discarded.  

a) * Describe the difference between stream-oriented and datagram-oriented transmission and name one example each.  

b) * Determine the time until the buffer at R overflows if A sends data to B at the maximum possible data rate using UDP.  

c) * How is the inevitable loss compensated when using UDP?  

d) * Describe how TCP avoids the persistent buffer overflow at R.  

e) * How is the send window structured in TCP?  

f) * Explain how the development of the send window differs during Slow Start and Congestion Avoidance.  

In the following sub-task, we will examine the temporal development of the send window at A and the buffer fill level at R based on the known variant of TCP Reno from the lecture. We will consider the following quantities:  

| Variable | Meaning |  
|----------|---------|  
| w[t] | Size of the send window at A in time step t. |  
| z[t] | Number of bytes that R forwards in time step t towards B. |  
| Q[t] | Number of bytes that are in the buffer of R at time step t and waiting for forwarding. |  

In particular, the difference ∆[t] = w[t] - z[t] indicates the increase (or decrease) of the buffer in the respective time step. If the buffer fill level exceeds its maximum size Q = 6 kB, R discards further segments, which we will refer to as drops. The temporal development of the buffer fill level is therefore  

Q[t] = min{Q[t - 1] + ∆[t], Qmax}.  

The RTT between A and B is 1 s, the MSS is 1 kB. Headers can be neglected, and the receiving window at B is not limiting. For simplification, we will assume that acknowledgments from B to A cannot be lost and that A is able to recognize segment loss at the end of the current time step.  

g) Complete the development of the send window graphically in the solution field and fill in the table below it. This table gives the send window at A, the number of segments present at R, the number of forwarded segments, the buffer fill level, and the number of discarded segments (drops) per time step.

| w [kB] | s |  
|--------|---|  
| 3      | 20|  
| 19     | 19|  
| 4      | 18|  
| 17     | 17|  
| 5      | 16|  
| 16     | 16|  
| 15     | 15|  
| 6      | 14|  
| 14     | 14|  
| 13     | 13|  
| 12     | 12|  
| 11     | 11|  
| 10     | 10|  
| 9      | 9 |  
| 8      | 8 |  
| 7      | 7 |  
| 6      | 6 |  
| 5      | 5 |  
| 4      | 4 |  
| 3      | 3 |  
| 2      | 2 |  
| 1      | 1 |  
| 0      | 0 |  

| t [s] |  
|--------|  
| ws[t] |  
| 1      |  
| 2      |  
| 4      |  
| 8      |  
| Q[t-1] + ws[t] |  
| 1      |  
| 2      |  
| 4      |  
| 8      |  
| z[t] |  
| 1      |  
| 2      |  
| 4      |  
| 8      |  
| Q[t] |  
| 0      |  
| 0      |  
| 0      |  
| 0      |  
| Drops |  
| 0      |  
| 0      |  
| 0      |  
| 0      |  

h) * How does TCP compensate for the drops from sub-task 3g)?  

i) * Justify whether TCP can fully utilize the available bandwidth of a connection.  

**Additional template for sub-task 3g). Clearly mark invalid solutions.**  

| w [kB] | s |  
|--------|---|  
| 20     | 20|  
| 19     | 19|  
| 18     | 18|  
| 17     | 17|  
| 16     | 16|  
| 15     | 15|  
| 14     | 14|  
| 13     | 13|  
| 12     | 12|  
| 11     | 11|  
| 10     | 10|  
| 9      | 9 |  
| 8      | 8 |  
| 7      | 7 |  
| 6      | 6 |  
| 5      | 5 |  
| 4      | 4 |  
| 3      | 3 |  
| 2      | 2 |  
| 1      | 1 |  
| 0      | 0 |  

| t [s] |  
|--------|  
| ws[t] |  
| 1      |  
| 2      |  
| 4      |  
| 8      |  
| Q[t-1] + ws[t] |  
| 1      |  
| 2      |  
| 4      |  
| 8      |  
| z[t] |  
| 1      |  
| 2      |  
| 4      |  
| 8      |  
| Q[t] |  
| 0      |  
| 0      |  
| 0      |  
| 0      |  
| Drops |  
| 0      |  
| 0      |  
| 0      |  
| 0      |  

---

**Task 4**  
Fast Ethernet (13 Points)  
We consider the simple network from Figure 4.1. The three computers PC1, PC2, and PC3 are connected to each other via a hub H. The distance between PC3 and H can be neglected. Fast Ethernet is used at Layer 1/2 according to IEEE 802.3u (100BASE-TX). There are no devices between PC1 and H that operate at Layer 2 or higher.

```
PC3  
PC1 PC2  
H  
...  
400m 100m  
```

**Figure 4.1: Network Segment**  

a) * Justify whether simplex, half-duplex, or full-duplex connections are possible in the network segment from Figure 4.1.  

b) * Name and describe the media access method used in detail.  

At time t = 0 µs, PC1 begins transmitting a frame 50B long. At time t = 2 µs, PC2 begins transmitting a frame 25B long.  

c) * Determine the serialization time for both frames.  

d) * Determine the propagation delay between PC1 and PC2.  

e) Draw a detailed path-time diagram that represents all events.  
**Scale:** 1 µs = 5 mm vertical, 100 m = 2 cm horizontal.  

f) Explain what problem is observed in sub-task 4e).  

g) * Determine the minimum frame length in bytes so that the problem from sub-task 4e) can no longer occur.  

---

**Task 5**  
Short Tasks (16 Points)  
**Note:** The following sub-tasks can each be solved independently of one another.  

a) * What devices/objects are depicted in the solution field?  

b) * Describe the purpose and function of Binary Exponential Backoff.  

c) * Describe the function of the TCP 3-Way Handshake.  

d) * Explain the difference between static and dynamic routing.  

e) * Briefly explain the difference between Fourier series and Fourier transformation in terms of their application.  

f) Provide the bit sequence 111010 as a Manchester-encoded baseband signal.  
**Note:** There are two complementary solutions. Providing one solution is sufficient.  

g) * Assign the following signal space assignments to the possible modulation methods (multiple answers possible, providing the abbreviations is sufficient).  

h) * What is meant by a Shortest Path Tree?  

i) * Briefly explain the function of the system call bind().  

j) * Briefly explain the function of the system call listen().  

k) * Briefly explain the function of the system call connect().  

l) * Briefly explain the function of the system call accept().  

---

**Additional space for solutions – please clearly mark the affiliation with the respective task and cross out invalid solutions!**