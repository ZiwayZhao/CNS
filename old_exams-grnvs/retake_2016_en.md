Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Personalization Notes:
- Your exam will be personalized by affixing a code during attendance control.
- This code contains only a continuous number, which is also noted on the attendance list next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Basics of Computer Networks and Distributed Systems (GRNVS)  
Module: IN0010  
Examiner: Prof. Dr.-Ing. Georg Carle  
Exam: Repetition  
Date: Friday, September 30, 2016, 15:30–17:00  

### A1 A2 A3 A4 A5 A6  
I  
II  

### Instructions for Completion
- This exam consists of:
  - 19 pages with a total of 6 tasks as well as
  - a double-sided printed formula collection.  
  Please check now that you have received a complete set of materials.
- The removal of pages from the exam is prohibited.
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only those results will be counted where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-task.
- Do not write in red/green colors or with a pencil.
- The total score for this exam is 85 points.
- The following aids are permitted:
  - a non-programmable calculator
  - an analog dictionary in the native language without annotations
- Please turn off all electronic devices completely, store them in your bag, and close it.

---

### Task 1  
Short Tasks (20 Points)  
The following sub-tasks can be solved independently of each other.  

a) *Name two essential services provided by the transport layer of the ISO/OSI model.  
b) *Given a 64-bit long date 0x0123456789abcdef in Network Byte Order. What is the representation in Big Endian?  
c) *Given the following network. Draw all broadcast domains.  
d) *Explain the main advantage of OSPF over RIP.  
e) *What is meant by Classless Interdomain Routing?  
f) *What is the difference between a resolver and an authoritative nameserver?  
g) *Justify whether a resolver must be located in the same subnet as the querying client.  
h) *Determine the IP address for the reverse FQDN 60.50.66.128.in-addr.arpa.  
i) *For a server to read incoming UDP datagrams on a specific port, the system calls socket(), bind(), and recvfrom() are required. Briefly explain the function of these three system calls.  
j) *Determine the factor by which the size of the IPv6 address space differs from the IPv4 address space.  
k) *What is the difference between private IPv4 addresses and Link-Local addresses in IPv6?  
l) *What is the difference between Interior and Exterior Gateway Protocols regarding their use?  
m) *Give two reasons why modern IEEE 802.3 networks operate collision-free.  
n) *Given a transmission channel with a bandwidth of 20 MHz. Calculate the maximum achievable data rate with a signal-to-noise ratio of 30 dB.  
o) *Given an alphabet with a total of 64 different characters, where the occurrence probability is uniformly distributed. Justify whether the average codeword length when using Huffman coding is greater than, equal to, or less than 7 bits.  

---

### Task 2  
Packet Pair Probing (11 Points)  
Given the network depicted in Figure 2.1. Nodes 1 and 4 are connected to their routers via a full-duplex-capable network. The symmetric data rates on the links are r12 and r34. The connection between nodes 2 and 3 is significantly slower, i.e., r23 < r34, r12. The distances d12 and d23 are negligible in comparison to d34.  

Node 1 should determine the data rate r23 so that as little load as possible is created on the already slow connection. It is assumed that all nodes have a standard IP stack and can exchange ICMP packets between nodes 1 and 4.  

a) *Provide the serialization time and propagation delay between two neighboring nodes i and j as a function of packet size p, data rate r, and distance d.  
b) *Node 1 sends two ICMP Echo Requests of length p to node 4 one after the other. Let p be chosen such that fragmentation is not necessary along the path to node 4. Node 4 will respond to each Echo Request with an Echo Reply of the same size p. For simplicity, processing times at the nodes can be neglected.  
c) *Mark ∆t in your solution for part b.  
d) *What factors does ∆t depend on if r23 < r34?  
e) *Justify what would change in comparison to the previous sub-task if r23 > r34.  
f) *Determine ∆t generally for r23 < r34, r12. Simplify the result as much as possible.  
g) *Provide an expression for the desired data rate r23. Simplify the result as much as possible.  

---

### Task 3  
IP Fragmentation (24 Points)  
We consider the network from Figure 3.1. PC1 and PC2 communicate via IPv4 through the two routers R1 and R2.  

The three network segments are independent of each other and use different transmission methods on layers 1 and 2, so the MTUs visible in the figure are given.  

a) *Explain the general difference between MTU and MSS.  
b) *How should MSS for TCP generally be chosen in relation to MTU (justification or calculation)?  
c) *Justify whether an already fragmented packet can be fragmented again.  
d) *Explain where fragments can generally be reassembled.  
e) *How does the receiver recognize that its packet is a fragment of a larger packet?  
f) *What happens on layer 3 if one or more fragments do not arrive?  

---

### Task 4  
Data Compression (10 Points)  
In this task, we consider a simplified version of the ITU T.30 protocol, better known as fax. This used a combination of Huffman coding and run-length encoding (RLE). The corresponding Huffman tree is shown in Figure 4.1.  

a) *Briefly explain the structure of the Huffman tree from Figure 4.1a.  
b) *Complete the codebook in Figure 4.1b.  
c) *Provide the RLE codewords corresponding to the black-printed part of the data stream.  
d) *Complete the pixel representation of the message.  
e) *By what factor is the uncompressed message, where each pixel is binary coded (0 = black, 1 = white), longer than the compressed message?  

---

### Task 5  
Hex Dump (13 Points)  
Given the hex dump in Network Byte Order of the beginning of an Ethernet frame, which will be analyzed below.  

a) *Mark the beginning and end of the Ethernet header in the hex dump.  
b) *Justify which protocol is used at layer 3.  
c) *Determine the length of the header at layer 3 (justification).  
d) *Provide the TTL or Hop Limit in decimal and hexadecimal notation if present in the packet.  
e) *Provide the source address of layer 3 in the usual notation.  
f) *How can it be recognized that the payload of the packet belongs to ICMPv6?  

---

### Task 6  
CRC (7 Points)  
In this task, the two-octet long message 01101011 10101111 is to be secured using the CRC method presented in the lecture. The reduction polynomial is r(x) = x^4 + x^2 + 1.  

a) *Determine the secured message s(x).  
b) *During transmission, the error pattern 00000000001010100000 occurs. Show or justify whether the error is detected.  
c) *Briefly explain which errors can be corrected using CRC.  

---  

Additional space for solutions. Clearly mark the assignment to the respective sub-task. Do not forget to cross out invalid solutions.