Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by attaching a code during attendance control.
- This contains only a continuous number, which is also noted on the attendance lists next to the signature field.
- This will be used as a pseudonym to allow a unique assignment of your exam.

### Basics of Computer Networks and Distributed Systems  
Exam: IN0010/Retake  
Date: Friday, October 6, 2017  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 13:30–15:00  

### Instructions for Processing
- This exam comprises:
  - 16 pages with a total of 6 tasks as well as
  - a double-sided printed formula collection.  
  Please check now that you have received a complete set of information.
- The tearing out of pages from the exam is prohibited.
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only results where the solution method is recognizable will be counted. Text problems must also be justified unless explicitly stated otherwise in the respective task.
- Do not write in red/green colors or with pencil.
- The total score for this exam is 90 points.
- The following aids are permitted:
  - An analog dictionary German native language without notes.
- Please turn off all electronic devices you carry completely, store them in your bag, and close it.

---

### Task 1  
Short Tasks (17 Points)  
The following sub-tasks can be solved independently of each other.

a) *Cross out all terms that do not designate a layer of the ISO/OSI model.  
- TCP/IP Layer  
- Encryption Layer  
- Security Layer  
- User Layer  

b) *Explain in detail how Traceroute works.  
1. The host sends an IP packet with incrementally increasing TTL starting at 1 to a specific target.  
2. Routers decrement the TTL.  
3. If a router receives a packet with TTL=1, it discards the packet and sends an ICMP Time Exceeded / TTL Exceeded in Transit Message back to the host.  
From the error message, the host can infer the IP addresses of the routers between itself and the target.

c) *What is ARP used for?  
1. Given an IPv4 address, it queries the corresponding MAC address within the local broadcast domain.

d) *Explain the difference between sampling and quantization.  
1. Sampling is the discretization in the time domain, quantization is the discretization in the value domain.

e) *Explain the difference between a resolver and a nameserver.  
1. Nameservers are authoritative for one or more zones and only answer queries regarding those zones.  
2. Resolvers resolve queries iteratively to the respective responsible nameserver (or forward them recursively to another resolver) and return the final result to the requester.

f) *Explain the media access method Token Passing.  
1. Hosts are connected in a ring. A token circulates in the ring. The host that currently possesses the token is allowed to send. After sending or after a certain time, the token is forwarded.

g) *Summarize the 5 network areas 203.0.113.208/29, 203.0.113.216/29, 203.0.113.192/28, 203.0.113.224/29, and 203.0.113.160/27 as much as possible without including additional network areas.  
- 203.0.113.160/27, 203.0.113.192/27, 203.0.113.224/29  

h) *Given the following network topology. G represents the router provided by your provider (e.g., a FritzBox!). Since you would prefer to use your own router, but your provider refuses to provide you with the access data, you quickly install your own router R directly behind G.  
On R, you configure the private IP of G as the default gateway. No further configurations are made.  
Subsequently, you can reach hosts on the internet from R. However, a client behind R in the local network, which uses R as the default gateway, cannot connect to hosts on the internet. Explain the problem.  
- Local Network  
- Internet  
- R  
- G  
- G is missing an entry for the local network via R in its routing table.

---

### Task 2  
NAT and Static Routing (13 Points)  
Given the network topology from Figure 2.1. PC1 and PC2 are parts of a private network that is connected to the internet via R1. PC1 sends a message to the server SRV1. The figure shows relevant header parts of this message at three different points in the network.

| SrcMAC | DstMAC | SrcIP | DstIP | TTL | SrcPort | DstPort |
|--------|--------|-------|-------|-----|---------|---------|
| 00:53:00:be:ef:01 | 00:53:01:be:ef:01 | 172.16.0.1 | 198.51.100.81 | 63 | 6814 | 443 |
| 00:53:01:be:ef:02 | 00:53:02:be:ef:01 | 203.0.113.128 | 198.51.100.81 | 62 | | 443 |
| 00:53:03:be:ef:02 | 00:53:04:be:ef:01 | 203.0.113.128 | 198.51.100.81 | 56 | | 443 |

a) *Determine the L2 and L3 addresses of the devices in Figure 2.1. Enter the corresponding addresses completely in the table below. Addresses that do not appear in Figure 2.1 should be marked with a dash (—).  

| L2 Addresses | L3 Addresses |
|--------------|--------------|
| PC1.eth0    | 00:53:00:be:ef:01 | PC1.eth0 | 172.16.0.1 |
| S.eth0      | — | S.eth0 | — |
| S.eth1      | — | S.eth1 | — |
| R1.eth0     | 00:53:01:be:ef:01 | R1.eth0 | — |
| R1.eth1     | 00:53:01:be:ef:02 | R1.eth1 | 203.0.113.128 |
| R2.eth0     | 00:53:02:be:ef:01 | R2.eth0 | — |
| R3.eth1     | 00:53:03:be:ef:02 | R3.eth1 | — |
| SRV1.eth0   | 00:53:04:be:ef:01 | SRV1.eth0 | 198.51.100.81 |

b) *Complete the Time-to-Live in Figure 2.1.

c) *Complete the Destination Port in Figure 2.1 under the assumption that PC1 is trying to establish an encrypted connection to a website on SRV1 with the sent message.

Table 2.1 shows the content of the NAT table of R1 before the connection attempt by PC1.

d) *Add the table with the resulting entry as soon as PC1 sends the first packet to SRV1.  
Note: Take another look at Figure 2.1. If an entry cannot be uniquely determined, make a sensible choice.

| Private IP | Private Src Port | Public Src Port |
|------------|------------------|-----------------|
| 172.16.0.2 | 6812             | 6812            |
| 172.16.0.2 | 6813             | 6813            |
| 172.16.0.2 | 6814             | 6814            |
| 172.16.0.1 | 6814             | 6815            |

Table 2.1: NAT table of R1

e) *Provide the Destination IP, Source Port, and Destination Port of the response from SRV1.  
Note: If a value cannot be uniquely determined, make a sensible choice.  
- Destination IP: 203.0.113.128  
- Source Port: 443  
- Destination Port: 6815  

f) *Explain in detail how R1 distinguishes whether the response is intended for PC1 or PC2.  
Based on the destination ports of the response, which must correspond to the public source port in the NAT table, R1 can determine the correct private IP address.

g) *Explain in detail what modifications R1 must make to the response from SRV1.  
(The specification of specific values if uniquely determined)  
The destination IP of the response is replaced by the private address 172.16.0.1, the destination port by the private source port 6814.  
(The checksum must be adjusted, TTL is decremented.)

---

### Task 3  
Dynamic Routing (19 Points)  
Given the network shown in Figure 3.1. The routing protocol used is RIP. The tables next to/above the routers represent the routing table of the respective router. Here, Dst stands for the respective destination router, NH for the respective next hop, and Cost for the cost to the respective destination.

| Dst | NH | Cost |
|-----|----|------|
| A   | A  | 0    |
| B   | B  | 0    |
| C   | A  | 0    |
| D   | C  | 1    |
| E   | D  | 1    |

a) *What metric does RIP use? (No justification)  
- Hop Count  

b) *RIP is a distance-vector protocol. Explain the difference to link-state protocols.  
- DV protocols only know next hop and distance to the destination, LS protocols have knowledge of the network topology.

c) *RIP belongs to the class of interior gateway protocols. Explain the difference to exterior gateway protocols.  
- IGPs are used within autonomous systems, EGPs between autonomous systems.

d) *In what way are networks whose routers exclusively use RIP as a routing protocol limited in size?  
- RIP interprets destinations that are 15 hops or further away as unreachable. Accordingly, networks are limited in diameter (i.e., the maximum path length).

e) *What information do routing updates contain in RIP?  
- Reachable destinations of a neighbor and distance to the respective destination.

f) *Justify whether RIP always chooses the shortest route (in terms of routers lying between source and destination).  
- Yes, since the only metric for RIP is the number of hops between itself and the destination routers.

g) *Justify whether RIP always chooses the fastest route (in terms of transmission rate) to a destination.  
- No, because the number of hops says nothing about the data rate between them.

h) *Complete the routing table of the router in Figure 3.1 (without specifying intermediate steps) so that a network of shortest paths according to the metric of RIP is created.  
Now the link between router D and E fails. Router D obviously notices the failure immediately. Answer the following questions in the given order.

i) Router D sends a periodic update. Describe the effects on routers A, B, and C.  
- C is informed about the failure, whereupon C deletes the route to E. A and B have not yet been informed.

j) Router A now sends a periodic update. Describe the effects on routers B, C, and D.  
- Since A still has a route to E via C, this is propagated to C. (Only destination and distance are considered, C does not know that this route runs through itself.)  
C accepts this and thinks it can reach E via A. The update has no effect on B, as B (just like A) still knows the old route to E via C. It does not forward the update from A.

k) Describe the problem that arises and its solution.  
- Count-to-Infinity: The faulty route to E will circulate between A, B, and C until the cost reaches 15 (RIP Tombstone).  
The solution is only conditionally possible with RIP, e.g., using Split Horizon (do not propagate a route to its own next hop for this route).

---

### Task 4  
Huffman (22 Points)  
In this task, we consider a simplified version of the ITU T.30 protocol, known as Telefax. This uses a combination of run-length encoding (RLE) and Huffman coding. The run-length encoding should alternately indicate the number of white and black pixels starting with "white." We first consider the pixel graphic in Figure 4.1.

a) *Determine the result of the run-length encoding.  
- 11, 2, 1, 2, 3, 7, 2, 7, 2, 7, 3, 5, 5, 3, 7, 1, 13  

b) *Determine the occurrence probabilities p of the individual RLE code words.  

| RLE | p |
|-----|---|
| 1   | 2/17 |
| 2   | 4/17 |
| 3   | 3/17 |
| 5   | 2/17 |
| 7   | 4/17 |
| 11  | 1/17 |
| 13  | 1/17 |

c) *Create a suitable binary Huffman code. Label the leaves with the corresponding RLE code words, all nodes with the corresponding probabilities, and assign the edges the corresponding section of the Huffman code words.

d) *Create a codebook for the Huffman code.  

| RLE | Huffman |
|-----|---------|
| 1   | 001     |
| 2   | 0      |
| 3   | 101     |
| 5   | 100     |
| 7   | 11     |
| 11  | 0000    |
| 13  | 0001    |

e) *Encode the pixel graphic with the created Huffman code.  
- 000001001011011101110111101100100101110010001  

f) *Determine the compression factor compared to a direct transmission, where each pixel is transmitted with 1 bit ("black" or "white").  
- 81 bits / 45 bits = 1.8  

g) We now consider the Huffman tree from Figure 4.2. We assume that it is used to encode a memoryless source with the alphabet A = {a, b, c}. The occurrence probabilities p of the characters are also indicated in the figure.

h) *Justify how many bits a uniform code requires on average for the encoding of a character.  
- log(3) = 2 bits  

i) *Determine the information content I(p) of the character i.  
Note: All results must be calculated completely. Use the plots on the cheatsheet to determine numerical values.  
- I = log(4) = 2 bits  

j) *Determine the entropy of the source.  
Note: All results must be calculated completely.  
- I(p) = 2 bits + 1.4 bits = 1.55 bits  

k) *Determine the average Huffman code word length.  
Note: All results must be calculated completely.  
- pi' = 2 bits + 2 bits + 1 bit = 1.625 bits  

---

### Task 5  
Wireshark (12 Points)  
Given the network from Figure 5.1. PC1 and PC2 are connected via the Ethernet switch S with router R.  
SRV sends a packet to PC1. The corresponding Ethernet frame is captured immediately after the Ethernet interface of SRV and is shown in Figure 5.2.

| Receiver Address | Transmitter Address | Ethertype |
|------------------|---------------------|-----------|
| 0x000f863f16e76b | 0x58 23 8c 26 b2 c4 | 0x86dd    |

| Payload Len | NH | Source IP |
|--------------|----|-----------|
| 0x010       | 00 | 0x00 00 00 40 3a 38 2a 01 04 f8 0d 16 19 43 00 00 |

| Destination IP |
|-----------------|
| 0x020 00 00 00 00 00 02 20 01 4c 50 04 ac 9e 00 fa 63 |

| Type Code |
|-----------|
| 0x030 3f ff fe 16 e7 6b 81 00 20 e3 52 cf 00 0e 0d ba |

| Checksum |
|----------|
| 0x070 32 33 34 35 36 37 89 a7 1f fe |

### Note:  
For all sub-tasks, a brief justification must be provided, e.g., specification or marking of the relevant header field, indication of the meaning of the respective field, any scaling of fields, etc.  
Note: Use the header and information printed on the cheatsheet for the solution.

a) *Mark and label all fields of Layer 2 in Figure 5.2.

b) *Determine the L2 addresses of the devices from Figure 5.1, as far as they are derived from the L2 header.  
- Srv: 58:23:8c:26:b2:44  
Since the internet lies between Srv and R, the Receiver Address certainly does not belong to R but to the gateway of Srv.

c) *The Ethertype is 0x86dd, the IP version field indicates IPv6. Justify why it can be concluded that it is IPv6 solely from the version field without knowledge of the Ethertype.  
- Given a packet that starts with 0x60, it cannot be concluded to be IPv6. It could be any packet of any type that happens to have the first byte as 0x06.

d) *Determine the source and destination address at Layer 3 of the packet in their usual notation.  
- Source: 2a01:4f8:d16:1943::2  
- Destination: 2001:4c50:4ac:9e00:fa63:3fff:fe16:e76b  

e) *Justify whether the destination address from part d) is the address of PC1 or R.  
- PC1, since IPv6 is used and thus R does not use NAT.

f) *Determine the length of the L3 header including options or extension headers.  
- The IPv6 header has a fixed length of 40B. Next Header is 0x3a, which is not an extension header.

g) *Determine the total length of the packet, i.e., Layer 3 header including payload.  
- Payload Length = 0x0040 = 64B plus the L3 header = 104B.

h) *Assuming the packet from SRV to PC1 is an ICMP Echo Reply. Two instances of an application running on PC1 are waiting for such a packet sent by SRV. How is it distinguished which of the two instances the packet is intended for?  
- ICMP Identifier, as the payload following the IP header contains ICMPv6 with Type=0x81, Code=0x00, which is an Echo Reply.

---

### Task 6  
CRC (7 Points)  
Given the CRC polynomial x^2 + x and the binary message m = 00110001.

a) *Provide the CRC polynomial in binary notation.  
- x^2 + x = 110  

b) *Determine the corresponding checksum.  

| Step | Calculation |
|------|-------------|
| 1    | 00110001 00 110 |
| 2    | 000001 00 |
| 3    | 0 10 |

c) *Provide the secured bit sequence that is transmitted.  
- 00110001 10  

d) *Explain what "secured" means in part c).  
- "Secured" in this context simply means that the message is secured against transmission errors. This does not mean that no such errors occur, but rather that they are likely to be detected by the receiver.  
Correction is not possible.