Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during the attendance check by affixing a code.
- This contains only a consecutive number, which is also noted on the attendance lists next to the signature field.
- This will be used as a pseudonym to allow a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Endterm  
Date: Monday, August 7, 2017  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 16:00–17:30  

### Instructions for Processing
- This exam consists of:
  - 16 pages with a total of 6 tasks as well as
  - a double-sided printed formula collection.  
Please check now that you have received a complete set of information.
- The removal of pages from the exam is prohibited.
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be counted where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective subtask.
- Do not write with red/green colors or with pencil.
- The total score for this exam is 90 points.
- The following aids are permitted:
  - An analog dictionary German ↔ native language without annotations.
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.

### Task 1  
Short Tasks (14 Points)  
a) * Briefly describe a network consisting of at least three hosts where the broadcast and collision domain are identical.  
0  
1  

b) * Explain the difference between channel coding (Layer 1) and checksums (Layer 2).  
0  
1  
2  

c) * What is meant by "well-known ports"?  
0  
1  

d) * Name the layers of the ISO/OSI model in descending order.  
0  
1  
2  

e) * Given the IP address 10.35.238.193. It is known that the subnet containing this address has 2046 usable addresses. Determine the network and broadcast address of the subnet.  
0  
1  
2  

f) * What is the purpose of the tool Traceroute?  
0  
1  

g) * Justify whether 192.0.2.96/27 and 192.0.2.128/27 can be summarized.  
0  
1  

h) * Briefly explain the difference between MAC and IP addresses regarding their use.  
0  
1  

i) * Sketch a non-constant, time-continuous signal s(t) that has a purely imaginary spectrum.  
0  
1  
2  

j) * Name two essential properties of Huffman coding.  
0  
1  

### Task 2  
Wireshark (25 Points)  
Given the network from Figure 2.1. PC1 and PC2 are connected via an Ethernet switch with router R. Within this local network, private addresses are used.  
PC1 sends a packet to server Srv. The corresponding Ethernet frame is captured at the marked point between switch S and router R in Figure 2.1. The corresponding hex dump of the frame (including checksum) is printed in Figure 2.2.  

```
PC1
   S
Internet
   Srv
   R
PC2
```

**Figure 2.1: Network Topology**  
```
0x0001 96 d7 9f 52 9d 4b 52 54 00 12 34 56 08 00 45 00
0x0002 00 60 1b fe 40 00 40 06 4c dd c0 a8 01 05 08 08
0x0003 04 04 9a a0 00 35 6d 30 93 19 cc d8 5c 44 80 18
0x0004 00 e5 73 cb 00 00 01 01 08 0a c3 fd 52 11 01 27
0x0005 4f 28 00 2a 78 cb 01 10 00 01 00 00 00 00 00 00
0x0006 01 31 01 31 03 31 36 38 03 31 39 32 07 69 6e 2d
0x0007 61 64 64 72 04 61 72 70 61 00 00 0c 00 01 1a ee
0x0008 1d 02
```
**Figure 2.2: Ethernet Frame Between S and R Including Checksum**  

For all subtasks, a brief justification must be provided, e.g., indicating or marking the relevant header field, noting the significance of the respective field, any scaling of fields, etc.  
Note: Use the header and information printed on the cheatsheet for the solution.  

a) * Mark and label all fields of Layer 2 in Figure 2.2.  
0  

b) * Determine (as far as possible) the Layer 2 addresses of the devices from Figure 2.1.  
1  
0  
1  

c) * Justify which Layer 3 protocol follows.  
0  
1  

d) * Determine the Layer 3 addresses of the devices from Figure 2.1 in their usual notation.  
0  
1  
2  

e) * Determine the length of the Layer 3 header.  
0  
1  

f) * Determine the total length of the packet, i.e., Layer 3 header including payload.  
0  
1  

g) * Justify which Layer 4 protocol follows.  
0  
1  

h) * Justify which protocol is used at the application layer.  
0  
1  
2  

The packet will be routed by R. In doing so, R uses a simple NAT implementation for address translation.  

i) * What information about the routed packet must R at least record in its NAT table?  
0  
(No specific values need to be provided.)  
1  
2  

j) * Which Layer 2 fields are modified during the forwarding of the packet by R? (No justification)  
0  
1  
2  

k) * Which Layer 3 header fields are modified during the forwarding of the packet by R in any case? (No justification)  
0  
1  
2  

l) Under what circumstances must the source port of the message be modified by R?  
0  
1  

m) Under what circumstances must the destination port of the message be modified by R?  
0  
1  

Now, the ICMPv4 packet depicted in Figure 2.3 arrives at the public interface of R. Only the ICMPv4 packet is depicted, i.e., no Layer 2/3 header.  
```
0x0000 0b 00 c2 e1 00 11 00 00 45 80 00 3c 76 c7 00 00
0x0010 01 11 74 b1 c0 a8 01 05 08 08 04 04 af f8 00 35
0x0020 00 28 8c b2
```
**Figure 2.3: ICMP Packet Between Internet and R**  

n) * What type of ICMP message is it?  
0  
1  

o) * What problem in the network causes such a message to be generated?  
0  
1  
2  

p) * Mark the end of the ICMP header in Figure 2.3.  
0  
1  

q) * Assume the packet is a response to the packet originally sent by PC1. What problem occurs at R?  
0  
1  

r) * How can R still deliver the packet?  
0  
1  
2  

### Task 3  
WLAN (21 Points)  
We consider the wireless network depicted in Figure 3.1. NB1 and NB2 communicate, as is common in WLAN, exclusively with each other via the access point AP. Due to the large distance between NB1 and NB2, direct communication without AP is not possible.  

```
NB1 AP NB2
r = 1.0 Gbit/s r = 1.6 Gbit/s
100m 100m
```
**Figure 3.1: Network Topology**  

a) * Explain the principle of CSMA in general.  
0  
1  
2  

b) * Why does CSMA/CD generally not work in wireless networks?  
0  
1  

IEEE 802.11-based networks are slotted, meaning nodes do not start sending at arbitrary times but only at the beginning of time slots. At time t, both NB1 and NB2 have data ready to send. The medium is free at this time. The contention window is CW = {0, 1, ..., 15}.  

c) * Explain the significance of the contention window in media access.  
0  
1  
2  

d) * Calculate the probability that NB1 and NB2 start sending in the same time slot.  
0  
1  
2  

e) * Calculate the average waiting time (in slot times) of a station between the request for data and the start of transmission.  
1  
2  

NB1 starts transmitting a frame of length 1000B at time t = 0µs. Since in practice stations are not perfectly synchronized, at time t = 0.5µs, NB2 also starts sending a frame of the same length.  

f) * Determine the propagation delay of the signals between NB1 and NB2 and the AP.  
0  
1  
2  

g) * Determine the serialization times of the two packets.  
0  
1  
2  
3  

h) * Draw a detailed path-time diagram that represents all transmissions in the time interval t ∈ [0; 10µs).  
   Scale:  
   - Distance (horizontal): 1cm ≡ 20m  
   - Time (vertical): 1cm ≡ 1µs  
   Mark serialization times and propagation delays.  

i) * How do NB1 and NB2 recognize whether their transmissions were successful?  
0  
1  

j) * Explain the behavior of NB1 and NB2 in the case of an unsuccessful transmission.  
0  
1  
2  

### Task 4  
DNS (13 Points)  
Let the DNS structure depicted in Figure 4.1 be given.  
```
·
de com net
tum lrz nic tele root-servers gtld-servers
www dns1 f ns www a m
```
**Figure 4.1: DNS Structure**  

a) * Briefly explain what DNS is used for.  
0  
1  

b) * Mark and name all name components for the FQDN www.tum.de.  
0  
1  
www.tum.de.  
2  

Now, let the zone file for in.tum.de. from Figure 4.2 be given. For this zone, there is an authoritative nameserver named nsa.in.tum.de.  
```
1 $ORIGIN in.tum.de.
2 $TTL 1H
3
4 @ IN SOA nsa.in.tum.de. hostmaster.in.tum.de. (...)
5
6 in.tum.de. IN NS nsa.in.tum.de.
7 in.tum.de. IN MX 10 gchq.in.tum.de.
8
9 nsa.in.tum.de. IN A 131.159.0.1
10 www.in.tum.de. IN A 168.144.144.106
11 gchq.in.tum.de. IN A 131.159.0.76
```
**Figure 4.2: DNS Zone File on nsa.in.tum.de**  

c) * Mark the lines in Figure 4.2 that contain the address records for hosts.  
0  

d) * What function does the NS record have?  
1  
0  
1  

e) * Complete Figure 4.1 based on the information from the zone file in Figure 4.2.  
0  

f) * What possibilities arise when multiple FQDNs refer to the same IP address?  
1  
0  
1  

g) * What advantages can it have when multiple IP addresses are assigned to an FQDN?  
0  
1  

We now consider the network topology depicted in Figure 4.3. The client uses the router as an access point to the Internet as well as a resolver. The router, in turn, uses ns.tele.com. as a resolver for recursive name resolution. Its IP address is known to the router. All other resolvers use iterative name resolution. The authoritative nameservers for the respective zones are listed in Table 4.1.  
```
dns1.lrz.de. www.tum.de.
1
Internet a.root-servers.net.
Client Router
m.gtld-servers.net.
ns.tele.com. f.nic.de.
```
**Figure 4.3: Network Topology**  

| Zone                  | Authoritative Nameserver       |
|-----------------------|--------------------------------|
| .                     | a.root-servers.net.            |
| com., net.           | m.gtld-servers.net.           |
| de.                   | f.nic.de.                     |
| tum.de., lrz.de.     | dns1.lrz.de.                  |
| tele.com.            | ns.tele.com.                  |
**Table 4.1: Zones and Authoritative Nameservers**  

h) * Explain the difference between recursive and iterative name resolution.  
0  
1  
2  

Assume for the following subtasks that all DNS caches are initially empty.  
i) The client now wants to access www.tum.de. Draw all necessary DNS messages in Figure 4.3 using arrows and number them in order. The first message is already provided as assistance.  
0  
Note: If necessary, you will find another template of Figure 4.3 at the end of the exam. Please clearly cross out invalid solutions.  

j) Immediately after, the client now wants to resolve www.in.tum.de. Briefly explain how this resolution differs from the one in subtask i).  
0  
1  

### Task 5  
Code Comprehension (7 Points)  
Given is the (somewhat simplified) source code known from the lecture:  
```c
1 struct sockaddr_in sa;
2 memset(&sa, 0, sizeof(sa));
3 sa.sin_family = AF_INET;
4 sa.sin_addr = INADDR_ANY;
5 sa.sin_port = htons(6112);
6 int sd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
7 bind(sd, (struct sockaddr *)&sa, sizeof(sa));
8 fd_set rfds, rfd;
9 FD_ZERO(&rfds)
10 FD_SET(sd, &rfds)
11 FD_SET(STDIN_FILENO, &rfds);
12 for (;;) {
13 rfd = rfds;
14 int ret = select(sd+1, &rfd, NULL, NULL, NULL);
15 (...)
16 }
```
a) * Briefly describe what function the source code snippet serves.  
0  
Note: A detailed explanation line by line is not necessary. 2-3 bullet points are sufficient.  
1  
2  

b) * What function does the function htons() serve in line 5?  
0  
1  

c) * What is the difference between the two socket types SOCK_DGRAM and SOCK_STREAM?  
0  
1  

d) * Describe the function of the syscall select(), as far as it is relevant for the printed source code. Explain, among other things, what happens with the argument rfd.  
0  
1  
2  
3  

### Task 6  
TCP (10 Points)  
The most commonly used transport protocol is TCP, which implements mechanisms for flow and congestion control. These differ in detail depending on the TCP variant. Specifically, we take TCP "Reno" as introduced in the lecture and exercises.  

a) * What is the purpose of flow control?  
0  
1  

b) * What is the purpose of congestion control?  
0  
1  

c) * What is the purpose of the "Window" field in the TCP header?  
0  
1  

d) * Sketch by hand in the solution field a typical course of the send window for TCP. Assume that the TCP connection was just established at time t = 0.  
0  
1  
2  

e) * Mark and name the individual congestion control phases in your solution from subtask d).  
0  

f) * What triggers the transition between the phases?  
1  
0  
1  

g) * Under what circumstances does the congestion control mechanism start over within a connection?  
0  
1  

h) * How does the receiver recognize the loss of a segment?  
0  
1  

i) * Briefly explain what happens when TCP is used in a network with a high data rate but a packet error probability of 1%.  
0  
1  

### Additional Space for Solutions. Clearly mark the assignment to the respective subtask.  
Do not forget to cross out invalid solutions.  
### Additional Template for Subtask 4i). Do not forget to cross out invalid solutions.  
```
dns1.lrz.de. www.tum.de.
1
Internet a.root-servers.net.
Client Router
m.gtld-servers.net.
ns.tele.com. f.nic.de.