Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during the attendance check by affixing a code.
- This contains only a sequential number, which is also noted on the attendance lists next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Basics of Computer Networks and Distributed Systems (GRNVS)  
Module: IN0010  
Examiner: Prof. Dr.-Ing. Georg Carle  
Exam: Repetition  
Date: Friday, September 30, 2016, 15:30–17:00  

### Instructions for Processing
- This exam consists of:
  - 19 pages with a total of 6 tasks as well as
  - a double-sided printed formula collection.  
  Please check now that you have received a complete set of information.
- The removal of pages from the exam is prohibited.
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only those results will be considered where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-task.
- Please do not write in red/green colors or with a pencil.
- The total score for this exam is 85 points.
- The following aids are permitted:
  - a non-programmable calculator
  - an analog dictionary German native language without annotations
- Please turn off all electronic devices you have with you completely, store them in your bag, and close it.

---

### Task 1  
Short Tasks (20 Points)  
The following sub-tasks can be solved independently of each other.

a) *Name two essential services provided by the transport layer of the ISO/OSI model.  
1. Control of media access (under what circumstances a node may send)  
2. Next-Hop addressing (addressing within a broadcast domain based on physical addresses)  

b) *Given is the 64-bit long date 0x0123456789abcdef in Network Byte Order. What is the representation in Big Endian?  
0x0123456789abcdef, since Network Byte Order already corresponds to Big Endian.

c) *Given is the following network. Draw all broadcast domains.  

d) *Explain the main advantage of OSPF over RIP.  
OSPF has accurate information about the network topology, which prevents loops at layer 3.

e) *What is meant by Classless Interdomain Routing?  
The flexible division (or aggregation) of IP subnets using subnet masks (or by specifying the prefix length).

f) *What is the difference between a resolver and an authoritative nameserver?  
A resolver resolves arbitrary DNS queries possibly by forwarding to another resolver (recursive name resolution) or iterative queries to the responsible nameserver. An authoritative nameserver only answers queries for zones for which it is authoritative.

g) *Justify whether a resolver must be located in the same subnet as the querying client.  
No, because resolvers are addressed at layer 3/4 (IP + UDP/TCP 53).

h) *Determine the IP address for the reverse FQDN 60.50.66.128.in-addcr.arpa.  
128.66.50.60  

i) *To have a server read incoming UDP datagrams on a specific port, the system calls socket(), bind(), and recvfrom() are required. Briefly explain the function of the three system calls.  
socket() creates a new socket of the specified type.  
bind() associates the socket with one (or all) IP addresses of the server and a specific port.  
recvfrom() attempts to read data from the socket and stores information about the respective sender (IP address and port number) in a corresponding data structure.

j) *Determine the factor by which the size of the IPv6 address space differs from the IPv4 address space.  
Number of IPv6 addresses: 2^128  
L = 2^128 / 2^32 = 2^96  

k) *What is the difference between private IPv4 addresses and Link-Local addresses in IPv6?  
Private IPv4 addresses are routable within a group of networks as long as they are unique within those networks (e.g., between different networks of a company). Link-Local addresses are only valid within a broadcast domain and are generally not routable.  
(Alternative: Link-Local addresses are assigned statelessly via SLAAC, while private IPv4 addresses must either be assigned statically or via DHCP server.)

l) *What is the difference between Interior and Exterior Gateway Protocols regarding their use?  
IGPs are a class of routing protocols used within an autonomous system (e.g., RIP, OSPF, IS-IS).  
EGPs are used to exchange routing information between different autonomous systems (the only practical example is BGP).

m) *Give two reasons why modern IEEE 802.3 networks operate collision-free.  
1. Modern networks are usually fully switched, meaning that within a collision domain, there is at most one host and the respective switch port.  
2. Since the networks also allow full-duplex, data can be sent and received simultaneously.

n) *Given a transmission channel with a bandwidth of 20 MHz. Calculate the maximum achievable data rate with a signal-to-noise ratio of 30 dB.  
30 dB = 10 log(SNR) → SNR = 10^3  
max data rate = 20 * 10^6 Hz * log2(1 + SNR) bits  
≈ 199.34 Mbit  

o) *Given an alphabet with a total of 64 different characters whose occurrence probability is uniformly distributed. Justify whether the average codeword length when using Huffman coding is greater than, equal to, or less than 7 bits.  
Since the occurrence probability of the characters is uniformly distributed, all codewords have the same length. A complete binary tree of height log2(64) = 6 is created, which results in the average codeword length being less than 7 bits.

---

### Task 2  
Packet Pair Probing (11 Points)  
Given is the network depicted in Figure 2.1. Nodes 1 and 4 are connected to their routers via a full-duplex capable network. The symmetric data rates on the links are r12 and r34. The connection between nodes 2 and 3 is significantly slower, i.e., r23 < r34, r12. The distances d12 and d23 are negligible in relation to d34.

Node 1 should determine the data rate r23 so that as little load as possible is generated on the already slow connection. It is assumed that all nodes have a standard IP stack and can exchange ICMP packets between nodes 1 and 4.

a) *Give the serialization time and propagation delay between two neighboring nodes i and j as a function of packet size p, data rate r, and distance d.  
t(i,j) = p / r + d / v  

Node 1 sends two ICMP Echo Requests of length p to node 4 immediately one after the other. The packet size p is chosen such that fragmentation is not necessary along the path to node 4. Node 4 will respond to each Echo Request with an Echo Reply of the same size. For simplification, processing times at the nodes are to be neglected.

b) *Complete the path-time diagram depicted in the solution field.  
Note: If necessary, you will find a replacement form at the end of the exam.

Due to the low transmission rate between nodes 2 and 3, a reception pause ∆t occurs at node 1. This can be measured by node 1 and used to determine the sought transmission rate between nodes 2 and 3.

c) Mark ∆t in your solution from part b.  

d) What factors does ∆t depend on if r34 > r23?  

e) Justify what would change in comparison to the previous sub-task if r34 < r23.  
For r34 < r23, the serialization time at node 4 limits ∆t instead of at node 3, making ∆t independent of r23 and dependent on r34.

f) Determine ∆t generally for r23 < r12, r34. Simplify the result as much as possible.  
∆t = ts(2,3) - ts(1,2) = p / r23 + p / r12  

g) Provide an expression for the sought data rate r23. Simplify the result as much as possible.  
r23 = p / ∆t + p / r12  

---

### Task 3  
IP Fragmentation (24 Points)  
We consider the network from Figure 3.1. PC1 and PC2 communicate via IPv4 through the two routers R1 and R2.

The three network segments are independent of each other and use different transmission methods at layers 1 and 2, so the MTUs visible in the figure are given.

a) *Explain the general difference between MTU and MSS.  
The MTU is the maximum size of an L3 PDU (IP packet including header) that can be transmitted at layer 2.  
MSS, on the other hand, is the maximum size of a TCP data segment (layer 4, without header), so that the MTU is not exceeded.

b) How should MSS for TCP generally be chosen in relation to MTU (justification or calculation)?  
MSS = MTU - TCP header - IPv4 header = MTU - 40B  

c) *Justify whether an already fragmented packet can be fragmented again.  
Yes, if the DF flag is not set and a minimum payload size of 8B is not exceeded.  
The assignment is done via identifier and fragment offset.

d) *Explain where fragments can generally be reassembled.  
Only at the destination host, as fragments are routed independently of each other and generally only meet at the final recipient.

e) How does the recipient recognize that its packet is a fragment of a larger packet?  
1. The fragment offset is 0 and the MF bit is set, or  
2. The fragment offset = 0  

f) What happens at layer 3 if one or more fragments do not arrive?  
All fragments of the respective packet are discarded (and a corresponding ICMP error message is sent to the sender).  
A retransmission does not occur automatically. This must be initiated by higher layers if necessary.

---

### Task 4  
Data Compression (10 Points)  
In this task, we consider a simplified version of the ITU T.30 protocol, better known as fax. This uses a combination of Huffman coding and run-length encoding (RLE). The corresponding Huffman tree is shown in Figure 4.1a. Figure 4.1b shows the codebook, which maps the binary Huffman codewords (to be determined in part b) to RLE codewords.

a) *Briefly explain the structure of the Huffman tree from Figure 4.1a.  
The characters to be encoded are the leaves of the tree, which are grouped into subtrees according to their occurrence probabilities. The differences in weights (sum of the probabilities of all leaves) of internal nodes of the tree are minimal at the same depth.  
The path from the root to a leaf describes the codeword, where the individual bit positions can be read from the edges of the tree. More frequently occurring characters receive shorter codewords, i.e., are higher up in the tree.

b) Complete the codebook in Figure 4.1b.  
You receive the binary message shown in Figure 4.2. This is initially encoded using Huffman coding.  

c) Provide the corresponding RLE codewords for the black-printed part of the data stream.  
Note: The first bit of the second black-printed block indicates the beginning of a Huffman codeword.

The RLE codewords are always structured according to the schema <number><w|s>, indicating the number of consecutive white (w) or black (s) pixels in a line, thus creating a pixel representation of the message line by line.

d) Complete the pixel representation of the message.  

e) By what factor is the uncompressed message, where each pixel is binary coded (0=black, 1=white), longer than the compressed message?  
Note: The compressed message from Figure 4.2 has a total length of 127 bits.  
η = (11 * 30 bits) / 127 bits ≈ 2.60  

---

### Task 5  
Wired Network (13 Points)  
Given is the hex dump in Network Byte Order of the beginning of an Ethernet frame, which is to be analyzed below.

**Ethernet Header**  
0x0000 00 16 3e c7 6d 64 00 25 90 57 22 4a 86 dd 60 00  
**TTL**  
0x0010 00 00 00 58 3a 38 26 06 28 00 42 00 3f ff 00 00  
**Next Header**  
0x0020 00 00 00 00 00 15 20 01 4c a0 20 01 00 1a3 02 16  
0x0030 ...  

a) *Mark the beginning and end of the Ethernet header in Figure 5.1.  

b) Justify which protocol is used at layer 3.  
EtherType 0x86dd stands for IPv6.  

c) Determine the length of the header at layer 3 (justification).  
Fixed header length of 40 bytes for IPv6.  

d) Provide TTL or Hop Limit in decimal and hexadecimal notation, if present in the packet.  
TTL is 0x38 = 56  

e) Provide the sender address of layer 3 in the usual notation.  
2606:2800:4200:3fff::15 (compressed)  

f) How can it be recognized that the payload of the packet belongs to ICMPv6?  
Next Header is 0x3a = ICMPv6.  

We will now consider the payload of the packet depicted in Figure 5.2. It is known that it is ICMPv6.  

g) Determine the type and code of the ICMP message.  
Time Exceeded / Hop limit exceeded in transit  

h) What causes such a message?  
When a router receives a packet with TTL=1 (or with Hop Count 1 in IPv6) that is to be forwarded, it is discarded, and a Time Exceeded / Hop limit exceeded in transit message is sent back to the original sender of the discarded packet.  

i) *Mark the end of the ICMP header in Figure 5.2.  

j) Explain what the payload of such a message generally contains.  
The payload contains the IP header and the first 8 bytes of the L3 SDU of the packet that triggered the ICMP TTL Exceeded message.  

k) *The packet was recorded as part of a traceroute. Briefly explain how traceroute works.  
Packets are sent with their own Hop Limit, which are then discarded by the routers. In this process, HL Exceeded ICMP messages are sent. Based on the sender addresses of the HL Exceeded ICMP message, the "path" of the packet through the network can be traced.

---

### Task 6  
CRC (7 Points)  
In this task, the two-octet long message 01101011 10101111 is to be secured using the CRC method presented in the lecture. The reduction polynomial is r(x) = x^4 + x^2 + 1.

a) *Determine the secured message s(x).  
s(x) = 01101011 10101111 1110  

b) During transmission, the error pattern 00000000001010100000 occurs. Show or justify whether the error is detected.  
The error e(x) = r(x)x^6 is a multiple of the reduction polynomial, which is why the error cannot be detected.  

c) *Briefly explain which errors can be corrected using CRC.  
None. CRC is an error-detecting code.  

---

### Additional Form for Task 2:  
Additional space for solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to strike out invalid solutions.