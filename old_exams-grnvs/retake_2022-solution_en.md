Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by affixing a code sticker during attendance verification.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID here.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Basics of Computer Networks and Distributed Systems  
**Exam:** IN0010/Retake  
**Date:** Friday, October 7, 2022  
**Examiner:** Prof. Dr.-Ing. Georg Carle  
**Time:** 10:45 – 12:15  

Before we proceed with reading the instructions, please answer the following questions. This information helps us to examine the learning success in relation to individual components of the lecture. The information is voluntary and does not influence the grading. To exclude any influence, this page will not be accessible during the exam.

a) Did you attend the lecture?  
1 (always) 2 3 4 5 (never)  

b) Did you watch the recording from last year?  
1 (always) 2 3 4 5 (never)  

c) Did you attend the tutorial exercises?  
1 (always) 2 3 4 5 (never)  

d) Did you participate in the review sessions?  
1 (always) 2 3 4 5 (never)  

e) Did you watch the recording of the review session?  
1 (always) 2 3 4 5 (never)  

### Instructions for Processing
- This exam comprises 16 pages with a total of 7 tasks and a formula collection (cheat sheet). Please check now that you have received a complete set of information.
- The total score for this exam is 90 points.
- The removal of pages from the exam is prohibited.
- The following aids are permitted:
  - A non-programmable calculator
  - An analog dictionary German ↔ native language without annotations
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only results where the solution path is recognizable will be graded. Text tasks must be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write in red/green colors or with a pencil.
- Turn off all electronic devices completely, store them in your bag, and close it.

### Task 1  
**Multiple Choice (18 Points)**  
The following tasks are multiple choice/multiple answer, i.e., there is at least one correct answer option for each. Subtasks are scored with 1 point for each correct answer and -1 point for each incorrect mark. Missing marks have no effect. The minimum score per subtask is 0 points.

Please mark the correct answers.  
Marks can be crossed out by completely filling them in.  
Crossed-out answers can be marked next to them.

a) * Starting from the Autonomous Systems (AS) in Figure 1.1. Which routes will Vodafone communicate to Orange via the peering connection?  
1 AS7018 (AT&T)  
2 AS3209 (Vodafone)  
3 AS5511 (Orange)  

b) * Does Vodafone provide the route to Orange's customers to AT&T? Please provide only the most likely answer.  
Yes, as defined in BGP.  
Yes, to collect more money from its customers.  
No, Vodafone does not know the customers at all.  
No, as defined in BGP.  
Yes, to distribute the load on the Internet better.  

c) * Which of the following addresses will be globally routed?  
::1  
10.11.12.13  
fec0::1  
128.0.0.1  
fea0::1  
127.8.9.10  

d) * The path MTU is 1500B. IPv4 is used at layer 3. How large should the MSS be chosen if no TCP options are used?  
1500B  
1452B  
1540B  
1520B  
1480B  
1460B  

e) * Given is a line code that encodes 3 bits per symbol. It should achieve a data rate of 10 Mbit/s. Determine the minimal necessary bandwidth under the given conditions.  
1.33MHz  
0.67MHz  
0.33MHz  
3.33MHz  
1.67MHz  

f) * What is meant by channel coding?  
None of that  
Targeted addition of redundancy  
Removal of redundancy  
Representation of data through sequences of signal impulses  

g) * Let n be the length of the checksum, i.e., n = degree(r(x)), with n > 1. Which of the following errors will, regardless of the specific choice of the reduction polynomial, always and reliably be recognized?  
Errors consisting of multiple bursts  
Burst errors longer than n  
Isolated 2-bit errors  
1-bit errors  
Burst errors shorter than n  
Errors that are multiples of the reduction polynomial  

h) * With which of the following addressing types can there be more than one recipient?  
Broadcast  
Unicast  
Anycast  
Multicast  

i) * There are 30 hosts in an IPv4-based network. Which subnet mask describes the smallest possible subnet so that all hosts can be assigned an IPv4 address?  
255.255.255.248  
255.255.255.224  
255.255.255.254  
255.255.255.240  
255.255.255.192  
255.255.255.252  

j) * Which of the following properties apply to link-state routing protocols?  
The operating principle is similar to Dijkstra's algorithm.  
Routers exchange information with each other only about cumulative costs.  
Routers determine a minimal spanning tree from the exchanged information.  
Routers have no information about network topology.  
Routers regularly exchange status messages.  
The operating principle is similar to Bellman-Ford's algorithm.  

k) * You want to compress the following data stream and use a Huffman code for this. Which character in the corresponding Huffman tree has the lowest depth?  
DADCCBDBCD  

l) * Given is the time signal s(t) with s(t) = 1.5·cos(4ωt) + 3. Here, ω = 2π, T = 1s. Which of the following statements about the coefficients of the corresponding Fourier series is true?  
a = 4  
b = 4  
a = 1.5  
a = 1.5  
a = 4  
b = 1.5  
a = 3  
b = 6  
a = 6  
b = 1.5  
a = 1.5  
b = 4  

### Task 2  
**Short Tasks (4.5 Points)**  
a) * Given is the IPv4 address 203.0.113.4. Provide the corresponding FQDN of the PTR record.  
4.113.0.203.in-addr.arpa.  

b) * Given is the IPv4 subnet 192.168.240.15/20. Justify why this subnet cannot be merged with the subnet 192.168.223.15/20 into a /19 supernet.  
The relevant bits are in the 3rd byte of the addresses (since the first two are the same):  
240 = 11110000 (10) (2)  
223 = 11011111 (10) (2)  
The two networks differ in the 19th bit. Thus, there is no /19 supernet that unites both subnets. If they only differed in the 20th bit, it would work.  

c) * Given is the IPv4 subnet 192.168.240.15/20. With which other /20 network can this be merged into a /19 supernet?  
11110000 = 240 (2) (10)  
11100000 = 224 (2) (10)  
→ 192.168.224.0/20  

d) * Given is the IPv6 address 2001:0db8:0000:0000:0110:0000:0000:0123. Provide the address in the usual, fully abbreviated form.  
2001:db8::110:0:0:123  

### Task 3  
**Frequency Analysis (16.5 Points)**  
Given is the transmission pulse shown in Figure 3.1.  
a) * What is this transmission pulse commonly called? (no justification)  

b) * How is a logical 0 or 1 encoded using this pulse? (Justification or sketch)  
Manchester pulse  
Rising clock edge in the middle ⇒ logical 0  
Falling clock edge in the middle ⇒ logical 1  

c) * Briefly describe one advantage of this pulse.  
Due to the forced level change with each pulse, automatic clock synchronization between sender and receiver is possible.  

d) * Briefly describe one disadvantage of this pulse.  
Due to the forced level change (2 symbols per pulse), it results in a wider spectrum and thus higher influence of a low-pass filter on high-frequency components.  

Next, the frequency behavior of this transmission pulse should be examined.  

e) * Justify whether a Fourier transformation or a Fourier series is used here.  
Isolated pulse, i.e., non-periodic signal ⇒ no series expansion possible ⇒ Fourier transformation.  

f) * Provide an analytical expression for the transmission pulse shown in Figure 3.1.  
gManch(t) =  
- A, -T/2 ≤ t < 0  
0, 0 ≤ t < T/2  
0, otherwise  

g) * Why might it be useful to provide the spectrum of a transmission pulse as a magnitude?  
The spectrum has real and imaginary parts. If one wants to represent the spectrum only qualitatively in terms of its frequency components, the magnitude representation offers itself in a single diagram.  

h) * Determine the spectrum. Simplify the result as much as possible.  
(See exercise sheet)  
GManch(f) = √(2π) ∫(gManch(t)·e^(j2πft)dt) from -∞ to ∞  
= √(2π) [cos(2πft) - jsin(2πft)] from -T/2 to 0 + [cos(2πft) - jsin(2πft)] from 0 to T/2  
= √(2π) [(-[0 - sin(-πfT)] + j[-1 + cos(-πfT)] + [sin(πfT) - 0] - j[-cos(πfT) + 1])]  
= √(2π) [(-sin(πfT) - j + jcos(πfT) + sin(πfT) + jcos(πfT) - j)]  

### Task 4  
**The Clacks (14.5 Points)**  
The Clacks are a network of towers in Terry Pratchett's Discworld. They form one of the first telecommunications networks and are described as: three stories high, made of wood, and look as if they were hastily assembled, probably because they were. A lantern inside even allows transmission at night.  

A message is transmitted by displaying individual symbols through targeted opening and closing of the 2×4 flaps (see Figure 4.1), which are observed by staff on a tower 12 km away and may be forwarded from there. It takes 5 seconds to deliver a symbol.  

a) * How many bits can be transmitted with each symbol? The calculation must be evident.  
M = 28 distinguishable symbols ⇒ N = log2(28) = 8  

b) * Calculate the information content of any symbol under the assumption that all symbols have the same probability of occurrence.  
I(x) = -log2(1/28) = 8 bits  

c) * Determine the achievable data rate in B/s.  
r = (N / t) = (1 bit/s * bit/B) / 5s = 0.2 B/s  

d) * The patrician of Ankh-Morpork wants to send a 47-character message to his neighboring state. Messages are ASCII-encoded and terminated with NUL. The Clacks use an additional (unused by ASCII) bit per symbol for error detection. How many bytes does the message require?  
ASCII uses 7 bits + 1 parity bit = 8 bits per character  
48 characters × 8 bits = 48B  

e) * Calculate the serialization time in the case of message transmission.  
t = 48B / 0.2B/s = 240s  

f) * The original design of the Clacks included only 2×3 flaps. What else could the additional 2 flaps have been used for, besides simply representing more symbols? Justify.  
One option includes, among others:  
- Error correction (with 2 parity bits, one can correct 1-bit errors instead of just detecting them)  
- Control characters (e.g., start/end of message)  
- Clock synchronization  

g) Next, we want to determine the transmission time if packet switching is used instead of message switching. We assume that each packet contains 10B of payload data. A 2B header is added to each packet.  

h) Calculate the number of packets required.  
L = 48B  
p = 10B  
N = L / p = 48B / 10B = 5  

To reach the destination, the message must pass through 5 Clacks (including start and end). Their distance is 12 km each. There are no confirmations, but a packet is read completely before being forwarded.  

i) How long does it take until the message reaches its destination?  
Intermediate stations n = 3  
Header Lh = 2B  
Distance d = 4 × 12 km = 48 km  
T = n(L + Lh + n(L + p)) / νc0  
T = n(5×2B + 48B + 3(2B + 10B)) + ≈ 470s  

j) Explain the advantage of packet switching over message switching.  
It is generally faster because:  
- Not the entire message needs to be stored at each intermediate station, but only individual packets, allowing for faster transmission of the entire message.  
- In case of errors, only one packet needs to be retransmitted instead of the entire message.  
- The packets can take different routes in the Internet, relieving individual routers.  

k) Explain the advantage of packet switching over circuit switching.  
- Packets allow parallel use of a line by multiple participants since the line is not exclusively occupied.  
- The packets can take different routes in the Internet and thus arrive faster on average.  
- Metadata (e.g., for error detection) can be used more effectively.  

### Task 5  
**DNS (7 Points)**  
You are the system administrator of a small company that has secured the domain grnvs.tips. Your task is to fill out the following zone file so that the requirements of the individual subtasks are met. The beginning of the zone file is already provided.  
```
$TTL 86400 ; 1 day  
dns.lrz.eu. IN SOA ns.grnvs.tips. (  
hostmaster.grnvs.tips.  
164160 ; serial  
1800 ; refresh (30 minutes)  
300 ; retry (5 minutes)  
604800 ; expire (1 week)  
1800 ; nxdomain (30 minutes)  
)  
NS dns.lrz.eu.  
grnvs.tips. MX 10 mail.grnvs.tips.  
@ A 134.102.13.9  
@ AAAA 2001:db8::2  
$ORIGIN grnvs.tips.  
calendar AAAA 2005:db1::affe  
contacts CNAME calendar  
$TTL 5400  
mail CNAME mail.adzone.com.  
challenge TXT secret123  
```

a) * When someone calls grnvs.tips in their browser, your website should be displayed. Your web server has the IP addresses 134.102.13.9 and 2001:db8::2.  

b) * To facilitate better collaboration among employees, the two services calendar and contacts should be set up as subdomains. Both run on the server with the address 2005:db1::affe.  

c) * You do not want to operate your own mail server and have booked the mail service from adzone.com. For this, all incoming mails must be sent to the IP address of mail.adzone.com. Since you may want to change this in the future, the maximum validity of this entry should be 90 minutes.  

d) * To prove to the provider of adzone.com that you really own the domain grnvs.tips, the text secret123 should be stored under challenge.grnvs.tips.  

### Task 6  
**Dormitory Network Goes Internet (15.5 Points)**  
Given is a student dormitory with several houses, whose network is built over Ethernet and IPv4. Each household has its own private /24 prefix. The house network for house x is described by the prefix 10.0.x.0/24. All residents of a house are connected to each other via a switch, which is connected to the respective gateway of the house. These routers are interconnected over the transport network 10.0.255.0/24. A snippet of the network is shown in Figure 6.1.  

The dormitory has been assigned the public IP address 203.0.113.23. For the mapping between public and private IP addresses, the NAT-capable router has a mapping table that stores the relationship between local and global ports, as well as the IP addresses of the internal hosts. The NAT router is connected to the "Internet." This is represented as a cloud and has an unspecified number of hops between R and R.  

```
House 1   House 2  
10.0.1.0/24   10.0.2.0/24  
Residents   Residents  
1,1   2,1  
eth0   eth0  
P1 Transport Network  
10.0.255.0/24  
eth0   eth0   wan1   wan1   eth0   eth0  
P2   P3  
R1   R2  
Residents   Server  
1,2   2  
P4  
...  
wan1  
...  
NAT Router  
R  
N  
wan2  
P5  
wan0  
R  
x  
R  
y  
wan1  
P6  
wan1  
wan0  
```

a) * Name two ways to assign IP addresses to hosts/residents?  
- Manual/static configuration  
- DHCP  

b) What additional method of assignment is there for IPv6?  
- SLAAC  

c) * Why must there be a NAT-capable router?  
The IPv4 addresses of the residents are in the private address range 10.0.0.0/8. These are not globally routed.  

d) What advantage does this architecture with NAT offer?  
All residents can use the Internet with only one public address. This is an advantage especially in light of the address scarcity of IPv4.  

e) * How many entries can the mapping table of the NAT router have for TCP at most?  
2^16 (possible global ports)  

f) A resident now wants to access the website with the URL https://grnvs.net and knows its IP address 198.41.0.4.  

g) * To which TCP port will the request likely be addressed? (no justification)  
443  

h) * Which HTTP method will likely be used? (no justification)  
HTTP GET  

i) We consider the sending of the requests. Provide the corresponding header fields in the table at the marked points P1 to P6 in the graphic. Use the following notation: MAC(k.iface) for the MAC address of the interface iface of node k, e.g., MAC(R7.eth9) for the MAC address assigned to the interface eth9 at router R7; similarly, IP(k.iface) for the IP address. You can abbreviate residents with B. Please provide the ports as numbers.  

```
SRC-MAC           DST-MAC           SRC-IP           DST-IP           SRC-PORT           DST-PORT  
P1  MAC(B1,1)     MAC(R1.eth0)     IP(B1,1)        IP(G.wan0)      12345              443  
P2  MAC(B1,1)     MAC(R1.eth0)     IP(B1,1)        IP(G.wan0)      12345              443  
P3  MAC(R1.wan1)  MAC(NAT.wan1)    IP(B1,1)        IP(G.wan0)      12345              443  
P4  MAC(R1.wan1)  MAC(NAT.wan1)    IP(B1,1)        IP(G.wan0)      12345              443  
P5  MAC(NAT.wan2) MAC(Rx.wan0)     IP(NAT.wan2)    IP(G.wan0)      678c9              443  
P6  MAC(Ry.wan1)  MAC(G.wan0)      IP(NAT.wan2)    IP(G.wan0)      6789               443  
```

j) * We assume that the host is unreachable due to connection problems and router R sends an ICMP error message back. Will this arrive at resident 1,1? Justify.  
Since there was no outgoing ICMP message (e.g., with an Echo Request), no ICMP identifier was entered in the NAT. However, ICMP 'Destination Unreachable' messages contain, in addition to the IP header, the first 8 bytes of the payload. In these 8 bytes of payload, the source and destination port of the TCP header are located. A mapping is possible via the source port since it was set by the NAT and a corresponding entry (as a global port) was created in the NAT table.  

k) * In house 2, a resident operates their own server (Server Z). A client from outside the dormitory wants to reach this web server in house 2. Justify why this is not possible.  
A NAT router creates corresponding entries in the NAT table for connections from the dormitory. When a client now wants to establish a connection to the server (e.g., via HTTP/Port 80), there is no entry in the NAT table for this global port. Therefore, the NAT router does not know where to direct the packet.  

l) How can this problem be circumvented?  
By setting up static port forwarding.  

### Task 7  
**Congestion in Flow (14 Points)**  
In this task, we consider the effects of disturbances in the network on the transport layer. A simplified form of TCP Reno is considered, as presented in the lecture.  

a) * Explain the goal of congestion control in TCP and its implementation.  
The goal of congestion control is to avoid overload situations in the network. To do this, the sender must detect bottlenecks in the network and adjust the size of the send window accordingly.  

b) * Explain the goal of flow control in TCP and its implementation.  
The goal of flow control is to avoid overload situations at the receiver. This is achieved by the receiver specifying a maximum size for the sender's send window.  

We now consider a sequence of events and how they affect the size of the receive window. In the diagram below, the window size w is given in multiples of the MSS, and the time is given in multiples of the RTT between the communicating hosts.  

```
wc/MSS  
20  
33333-----DDDDDuuuuuppppp-----AAAAACCCCCKKKKKsssss  
33333-----DDDDDuuuuuppppp-----AAAAACCCCCKKKKKsssss  
18  
16  
TTTTTiiiiimmmmmeeeeeooooouuuuuttttt  
14  
12  
10  
8  
6  
CCCCCTTTTT ===== 66666  
4  
2  
0 t/RTT  
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28  
```

It holds that wc(0) = 1. We assume that the bandwidth on the path in the network is a maximum of 15 MSS/RTT. Initially, there are no timeouts.  

c) * Draw the course of wc for t < 18 RTT and justify it.  
At the beginning, we are in the "Slow Start" phase, where w grows exponentially (doubling per RTT).  
At wc = 16 > 15 or at t = 4 RTT, the sender will receive 3 Duplicate ACKs because a segment will not arrive.  
Then follows the "Congestion Avoidance" phase with w halved to 8 and a CT also of 8.  
w is then gradually increased by 1 until another disturbance occurs.  
At t = 13 RTT, wc = 16 > 15 again, leading to 3 Duplicate ACKs again.  
Thus, w is halved to 8 with unchanged CT.  
Then continues the CA phase, resulting in a linear increase.  

d) If we disregard the beginning, what effective transmission rate can communication take place at if no other disturbances occur? Provide the result in dependence on the MSS.  
By counting: (8+9+1(0)+11+12(1)+13+14+15+(0)15) MSS ≈ 11.89 MSS / 9 RTT  
Alternatively: n = 38x2 + 34x, for x = 16 follows: n = 108, with a loss rate of θ = 1108. Thus, the time between segment losses T = x + 1 RTT = 16 + 1 RTT = 9 RTT. Thus, a throughput r = 108 MSS / (1 + 1) = 11.89 MSS.  

At t = 18 RTT, a timeout occurs.  

e) * What could be a cause for this?  
All segments or ACKs are lost or only arrive after the timeout. (If individual ones still arrived, then there would be duplicate ACKs, not a timeout.) This can be the case in a complete overload of the network or in the failure of individual nodes/links.  

f) After that, there are no further disturbances. Complete the diagram until ≤ 28 RTT and justify it.  
Due to the timeout, the CT is reduced to wc/2 = 12/2 = 6, wc is set to 1, and it switches back into the 'Slow Start' phase.  
In the Slow Start phase, it is doubled again until w = 6 = CT or t = 22 RTT.  
Then linear increase in the CA phase.  

g) * What problem arises with the unreliability of layers 1 to 3 when using TCP?  
TCP congestion control always interprets the loss of segments as a result of a congestion situation in the network. The data rate is unnecessarily throttled if errors (e.g., bit errors) occur in the lower layers. In this case, reducing the data rate does not ensure proper transmission.  

### Additional Template for Task 7:  
```
wc/MSS  
20  
18  
16  
14  
12  
10  
8  
6  
4  
2  
0 t/RTT  
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28  
```

### Additional Space for Solutions. Please clearly mark the assignment to each subtask.  
Do not forget to cross out invalid solutions.