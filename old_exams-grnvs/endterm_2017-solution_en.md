Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by attaching a code during attendance control.
- This contains only a continuous number, which is also noted on the attendance lists next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
**Exam:** IN0010/Endterm  
**Date:** Monday, August 7, 2017  
**Examiner:** Prof. Dr.-Ing. Georg Carle  
**Time:** 16:00–17:30  

### Instructions for Completion
- This exam consists of:
  - 16 pages with a total of 6 tasks as well as
  - a double-sided printed formula collection.
- Please check now that you have received a complete set of documents.
- The removal of pages from the exam is prohibited.
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only results where the solution path is recognizable will be counted. Text problems must also be justified unless explicitly stated otherwise in the respective sub-task.
- Do not write in red/green colors or with pencil.
- The total score for this exam is 90 points.
- Allowed aids:
  - An analog dictionary German ↔ native language without annotations.
- Turn off all electronic devices completely, store them in your bag, and close it.

### Task 1  
**Short Tasks (14 Points)**  
a) *Briefly describe a network consisting of at least three hosts where the broadcast and collision domain are identical.*  
Three hosts connected via a hub. (Alternatively: Three hosts each connected to a dedicated interface of the same router.)

b) *Explain the difference between channel coding (Layer 1) and checksums (Layer 2).*  
The goal of channel coding is the correction of transmission errors. Checksums are used to detect remaining transmission errors (or incorrect decoding on Layer 1).

c) *What is meant by "well-known ports"?*  
Port numbers (TCP/UDP) < 1024.

d) *Name the layers of the ISO/OSI model in descending order.*  
1. Application Layer  
2. Presentation Layer  
3. Session Layer  
4. Transport Layer  
5. Network Layer  
6. Data Link Layer  
7. Physical Layer  

e) *Given the IP address 10.35.238.193. It is known that the subnet contains 2046 usable addresses. Determine the network and broadcast address of the subnet.*  
Network address: 10.35.232.0  
Broadcast address: 10.35.239.255  

f) *What is the purpose of the tool Traceroute?*  
To determine possible paths on Layer 3 to a specific destination.

g) *Justify whether 192.0.2.96/27 and 192.0.2.128/27 can be summarized.*  
No, in binary the last octet 96 = 01100000, 128 = 10000000. For /26, the two most significant bits of the octets must match.

h) *Briefly explain the difference between MAC and IP addresses concerning their use.*  
MAC addresses serve for addressing within local networks and for addressing the next hops. IP addresses serve for end-to-end addressing, i.e., indicating the sender and receiver of a packet across multiple hops.

i) *Sketch a non-constant, time-continuous signal \( s(t) \) that has a purely imaginary spectrum.*  
A time-continuous signal point-symmetric to any point on the ordinate.

j) *Name two essential properties of Huffman coding.*  
Lossless, prefix-free code, optimal code, entropy method.

### Task 2  
**Wireshark (25 Points)**  
Given the network from Figure 2.1. PC1 and PC2 are connected via an Ethernet switch with router R. Within this local network, private addresses are used.  
PC1 sends a packet to server Srv. The corresponding Ethernet frame is captured between switch S and router R at the marked point in Figure 2.1. The associated hex dump of the frame (including checksum) is printed in Figure 2.2.

**Figure 2.1: Network Topology**  
```
ReceiverAddress TransmitterAddress Ethertype
0x0001 96 d7 9f 52 9d 4b 52 54 00 12 34 56 08 00 45 00
TotalLength SourceAddress Destination
0x0002 00 60 1b fe 40 00 40 06 4c sdd c0 a8 01 05 08 08
Address DestinationPort
0x0003 04 04 9a a0 00 35 6d 30 93 19 cc d8 5c 44 80 18
0x0004 00 e5 73 cb 00 00 01 01 08 0a c3 fd 52 11 01 27
0x0005 4f 28 00 2a 78 cb 01 10 00 01 00 00 00 00 00 00
0x0006 01 31 01 31 03 31 36 38 03 31 39 32 07 69 6e 2d
0x0007 61 64 64 72 04 61 72 70 61 00 00 0c 00 01 1a ee
0x0008 1d 02
```
**Figure 2.2: Ethernet Frame between S and R including Checksum**  
For all sub-tasks, a brief justification must be provided, e.g., indicating or marking the relevant header field, noting the significance of the respective field, any scaling of fields, etc.  
**Note:** Use the headers and information printed on the cheatsheet for the solution.

a) *Mark and label all Layer 2 fields in Figure 2.2.*  

b) *Determine (as far as possible) the L2 addresses of the devices from Figure 2.1.*  
R (private interface): 96:d7:9f:52:9d:4b  
PC1: 52:54:00:12:34:56  

c) *Justify which L3 protocol follows.*  
Ethertype 0x0800 = IPv4  

d) *Determine the L3 addresses of the devices from Figure 2.1 in their usual notation.*  
PC1: 192.168.1.5  
Srv: 8.8.4.4  

e) *Determine the length of the L3 header.*  
Header Length 0x5 = 20B  

f) *Determine the total length of the packet, i.e., header of Layer 3 including payload.*  
Total Length 0x0060 = 96B  

g) *Justify which L4 protocol follows.*  
Protocol 0x06 = TCP  

h) *Justify which protocol is used at the application layer.*  
Destination Port 0x0035 = 53 ⇒ DNS  

The packet will be routed by R. In doing so, R uses a simple NAT implementation for address translation.  

i) *What information about the routed packet must R at least store in its NAT table?*  
(Concrete values are not necessary.)  
Private source IP, private source port, public (translated) source port.  

j) *Which Layer 2 fields are modified by R when forwarding the packet? (no justification)*  
Transmitter and Receiver MAC, Checksum  

k) *Which header fields on Layer 3 are modified when forwarding the packet by R in any case? (no justification)*  
TTL, Source IP, Header Checksum  

l) *Under what circumstances must the source port of the message be modified by R?*  
If the same port is already used in the NAT table.  

m) *Under what circumstances must the destination port of the message be modified by R?*  
Never, translation of the destination port makes no sense.  

Now an ICMPv4 packet as shown in Figure 2.3 arrives at the public interface of R. Only the ICMPv4 packet is depicted, i.e., no L2/L3 header.  

**Figure 2.3: ICMP Packet between Internet and R**  
```
Type Code End ICMPv4 Header
0x0000 0b 00 c2 e1 00 11 00 00 45 80 00 3c 76 c7 00 00
0x0010 01 11 74 b1 c0 a8 01 05 08 08 04 04 af f8 00 35
0x0020 00 28 8c b2
```

n) *What type of ICMP message is it?*  
Type 0x0b ⇒ Time Exceeded, Code 0x00 ⇒ TTL expired in transit  

o) *What problem in the network triggers such a message?*  
Time Exceeded / TTL expired in transit (unless it occurs as a result of a traceroute) is an indicator of routing loops.  

p) *Mark the end of the ICMP header in Figure 2.3.*  

q) *Assuming the packet is a response to the originally sent packet from PC1. What problem arises at R?*  
R cannot trivially reverse the address translation because the ICMP header has no port numbers.  

r) *How can R still deliver the packet?*  
The ICMP error message contains as payload the IP header and the subsequent 8B of the respective packet that triggered the message. There R finds in particular the source port, which it needs for address translation.  

### Task 3  
**WLAN (21 Points)**  
We consider the wireless network depicted in Figure 3.1. NB1 and NB2 communicate, as is usual in WLAN, exclusively with each other via the access point AP. Due to the large distance between NB1 and NB2, direct communication is not possible.  

**Figure 3.1: Network Topology**  
```
NB1 AP NB2  
r = 1.0 Gbit/s r = 1.6 Gbit/s  
100m 100m  
```

a) *Explain the principle of CSMA in general.*  
Carrier Sense Multiple Access, also describable as "listen before talk": The medium is monitored before sending. If the medium is free, transmission begins in the next time slot. Otherwise, the medium continues to be monitored.

b) *Why does CSMA/CD generally not work in wireless networks?*  
1. While one station is sending, the medium cannot usually be monitored simultaneously.  
2. NB1 and NB2 may be far enough apart that each still has a connection to the AP, but a transmission from NB1 will no longer be received by NB2 (Hidden Station).

IEEE 802.11-based networks are slotted, meaning nodes do not start sending at arbitrary times but only at the beginning of a time slot. At time \( t \), both NB1 and NB2 have data ready to send. The medium is free at this point. The contention window is \( CW = \{0, 1, \ldots, 15\} \).

c) *Explain the significance of the contention window in media access.*  
When a station is ready and the medium is free, a number of slot times is chosen independently and uniformly from the contention window, which is then waited. If the medium is still free after this time has elapsed, transmission begins in the next time slot. The goal is to reduce the probability of collisions.

d) *Calculate the probability that NB1 and NB2 start sending in the same time slot.*  
Let \( X_i \) be the random variable representing the number of time slots that node \( i \in \{1, 2\} \) waits.  
\[ Pr[X_1 = X_2] = \frac{1}{16} \cdot Pr[X_2 = n] = \frac{1}{16} \sum_{n=0}^{15} 1 = \frac{1}{16} \]

e) *Calculate the average waiting time (in slot times) of a station between requests for data and the beginning of a transmission.*  
Let \( X \) be the random variable representing the number of time slots that a node waits.  
\[ E[X] = \frac{1}{15} \cdot \sum_{n=0}^{15} n = \frac{15 \cdot 16}{16 \cdot 2} = 7.5 \]

NB1 starts transmitting a frame of length 1000B at time \( t = 0 \, \mu s \). Since in practice stations are not perfectly synchronized, at time \( t = 0.5 \, \mu s \), NB2 also starts sending a frame of the same length.

f) *Determine the propagation delay of signals between NB1 or NB2 and the AP.*  
\[ d = 100m \]  
\[ t_p = \frac{d}{\nu} = \frac{100m}{3 \cdot 10^8 m/s} \approx 333ns \]

g) *Determine the serialization times of the two packets.*  
For NB1:  
\[ t_1 = \frac{L}{\nu_r} = \frac{8000 \text{ bit}}{1 \cdot 10^9 \text{ bit/s}} = 8 \mu s \]  
For NB2:  
\[ t_2 = \frac{L}{\nu_r} = \frac{8000 \text{ bit}}{1.6 \cdot 10^9 \text{ bit/s}} = 5 \mu s \]  

h) *Draw a detailed path-time diagram that represents all transmissions in the time interval \( t \in [0; 10 \mu s) \). Scale:*
- Distance (horizontal): 1cm ≡ 20m  
- Time (vertical): 1cm ≡ 1μs  
Label serialization times and propagation delays.

i) *How do NB1 and NB2 recognize whether their transmissions were successful?*  
By receiving a link-layer acknowledgment from the AP.  

j) *Explain the behavior of NB1 and NB2 in the event of an unsuccessful transmission.*  
The start of a retransmission is randomly delayed: Instead of choosing from a contention window of fixed length, the interval of possible delays is doubled with each failure, and a wait time is chosen randomly, uniformly, and independently.

### Task 4  
**DNS (13 Points)**  
Consider the DNS structure shown in Figure 4.1.  
```
de com net g  
tum lrz nic tele root-servers gtld-servers  
www in dns1 f ns www a h m  
nsa www gchq  
```

a) *Briefly explain what DNS is used for.*  
Mapping between FQDNs and IP addresses.

b) *Mark and name all components of the FQDN www.tum.de.*  
Second Level Domain: tum  
TLD: de  
Hostname: www.tum.de. Root  

Now, additionally, the zone file for in.tum.de. from Figure 4.2 is given. For this zone, there is an authoritative nameserver named nsa.in.tum.de.  
```
$ORIGIN in.tum.de.  
$TTL 1H  

@ IN SOA nsa.in.tum.de. hostmaster.in.tum.de. (...)  
in.tum.de. IN NS nsa.in.tum.de.  
in.tum.de. IN MX 10 gchq.in.tum.de.  
nsa.in.tum.de. IN A 131.159.0.1  
www.in.tum.de. IN A 168.144.144.106  
gchq.in.tum.de. IN A 131.159.0.76  
```

c) *Mark the lines in Figure 4.2 that contain the address records for hosts.*  

d) *What function does the NS record have?*  
It points to the FQDN of the authoritative nameserver for the zone in.tum.de.  

e) *Complete Figure 4.1 based on the information from the zone file in Figure 4.2.*  

f) *What possibilities arise when multiple FQDNs point to the same IP address?*  
For example, multiple different websites on the same server or under the same IP address.  

g) *What advantages can it have when multiple IP addresses are assigned to one FQDN?*  
Load balancing (alternatively: IP dual-stack, i.e., simultaneous accessibility via IPv4 and IPv6).  

Now we consider the network topology depicted in Figure 4.3. The client uses the router as an access point to the internet and as a resolver. The router uses ns.tele.com as a resolver for recursive name resolution. Its IP address is known to the router. All other resolvers use iterative name resolution. The authoritative nameservers for the respective zones are listed in Table 4.1.  
```
dns1.lrz.de. www.tum.de.  
Internet a.root-servers.net.  
Client 10 Router  
m.gtld-servers.net.  
ns.tele.com. f.nic.de.  
```

**Table 4.1: Zones and Authoritative Nameservers**  

h) *Explain the difference between recursive and iterative name resolution.*  
In recursive resolution, only one query for a resource record is made to a configured resolver, which returns the final answer.  
In iterative resolution, the FQDN is resolved starting from the root zone (or the last known SOA) by querying the authoritative nameservers for the respective zones. The responses either contain the FQDN of an authoritative nameserver for the next deeper zone or the final resource record if the queried nameserver is authoritative for it.

Assume for the following sub-tasks that all DNS caches are initially empty.  

i) The client now wants to access www.tum.de. Draw all necessary DNS messages in Figure 4.3 using arrows and number them in order. The first message is already given as assistance.  
**Note:** If necessary, you will find another template of Figure 4.3 at the end of the exam. Please clearly cross out invalid solutions.  

j) Immediately after, the client wants to resolve www.in.tum.de. Briefly explain how this resolution differs from the one in sub-task i).  
Up to the resolver ns.tele.com, it is the same. Due to the information in the caches, ns.tele.com can directly query dns1.lrz.de. After that, there is again an iterative query at nsa.in.tum.de.  

### Task 5  
**Code Comprehension (7 Points)**  
Given the (somewhat simplified) source code known from the lecture:  
```c
struct sockaddr_in sa;  
memset(&sa, 0, sizeof(sa));  
sa.sin_family = AF_INET;  
sa.sin_addr = INADDR_ANY;  
sa.sin_port = htons(6112);  
int sd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);  
bind(sd, (struct sockaddr *)&sa, sizeof(sa));  
fd_set rfds, rfd;  
FD_ZERO(&rfds);  
FD_SET(sd, &rfds);  
FD_SET(STDIN_FILENO, &rfds);  
for (;;) {  
    rfd = rfds;  
    int ret = select(sd + 1, &rfd, NULL, NULL, NULL);  
    (...)  
}  
```

a) *Briefly describe what function the source code snippet serves.*  
(Note: A detailed explanation line by line is not necessary. 2-3 bullet points are sufficient.)  
- A UDP socket is created and bound to port 6112.  
- Incoming datagrams on this socket or input on STDIN are expected.  

b) *What function does the function htons() in line 5 serve?*  
Conversion of the port number 6112 from host byte order to network byte order.  

c) *What is the difference between the two socket types SOCK_DGRAM and SOCK_STREAM?*  
SOCK_DGRAM are datagram-oriented sockets (connectionless, generally no guarantee of order or arrival of datagrams).  
SOCK_STREAM are stream-oriented sockets, i.e., connection-oriented, acknowledgment of individual bytes, no preservation of message boundaries, retransmission in case of errors, etc.  

d) *Describe the function of the syscall select(), as far as it is relevant for the printed source code. Explain, among other things, what happens with the argument rfd.*  
select() monitors the file descriptors in the file descriptor set rfd for readiness to read. Once at least one descriptor is ready, select() returns. The file descriptor set rfd is modified so that it only contains the file descriptors that are ready to read.  

### Task 6  
**TCP (10 Points)**  
The most commonly used transport protocol is TCP, which implements mechanisms for flow and congestion control. These differ in detail depending on the TCP variant. Specifically, we will consider TCP "Reno" as introduced in the lecture and exercises.  

a) *What is the purpose of flow control?*  
To avoid overload at the receiver.  

b) *What is the purpose of congestion control?*  
To avoid overload in the network.  

c) *What is the purpose of the "Window" field in the TCP header?*  
It indicates the size of the receive window (flow control), i.e., the maximum amount of data in bytes that the receiver can accept at once.  

d) *Sketch a typical course of the send window for TCP by hand in the solution field. Assume that the TCP connection was just established at time \( t = 0 \).*

e) *Mark and name the individual congestion control phases in your solution to sub-task d).*  

f) *What triggers the transition between the phases?*  
3 Duplicate ACKs ⇒ Transition from Slow Start to Congestion Avoidance.  

g) *Under what circumstances does the congestion control mechanism start over within a connection?*  
When a timeout occurs.  

h) *How does the receiver recognize the loss of a segment?*  
By an out-of-order received sequence number.  

i) *Briefly explain what happens when TCP is used in a network with a high data rate but a packet error probability of 1%.*  
Since TCP interprets segment loss as a result of congestion situations, the congestion control mechanism will incorrectly limit the data rate continuously.  

### Additional Space for Solutions  
Mark clearly the assignment to the respective sub-task.  
Do not forget to cross out invalid solutions.  
Additional template for sub-task 4i). Do not forget to cross out invalid solutions.  
```  
dns1.lrz.de. www.tum.de.  
Internet a.root-servers.net.  
Client Router  
ns.tele.com. f.nic.de.