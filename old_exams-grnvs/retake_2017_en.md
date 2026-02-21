Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during attendance control by affixing a code.
- This only contains a sequential number, which is also noted on the attendance list next to the signature field.
- This will be used as a pseudonym to allow a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Retake  
Date: Friday, October 6, 2017  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 13:30–15:00  

### A1 A2 A3 A4 A5 A6  
I  
II  

### Instructions for Completion
- This exam consists of:
  - 16 pages with a total of 6 tasks as well as
  - a double-sided formula collection.  
Please check now that you have received a complete set of documents.
- The removal of pages from the exam is prohibited.
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be counted where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-task.
- Do not write with red/green colors or with pencil.
- The total score for this exam is 90 points.
- The following aids are permitted:
  - an analog dictionary German native language without annotations
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.

---

### Task 1  
Short Tasks (17 Points)  
The following sub-tasks can each be solved independently of one another.

a) *Cross out all terms that do not designate a layer of the ISO/OSI model.  
b) *Explain in detail how Traceroute works.  
c) *What is the purpose of ARP?  
d) *Explain the difference between sampling and quantization.  
e) *Explain the difference between a resolver and a nameserver.  
f) *Explain the media access method Token Passing.  
g) *Summarize the 5 network areas 203.0.113.208/29, 203.0.113.216/29, 203.0.113.192/28, 203.0.113.224/29, and 203.0.113.160/27 as much as possible without including additional network areas.  
h) *Given the network topology depicted below. G represents the router provided by your provider (e.g., a FritzBox!). Since you would prefer to use your own router, but your provider refuses to provide you with the access data, you quickly install your own router R directly behind G. On R, configure the private IP of G as the Default Gateway. No further configurations will be made. Subsequently, you can reach hosts on the Internet from R. However, a client behind R in the local network, which uses R as the Default Gateway, cannot establish a connection to hosts on the Internet. Explain the problem.

---

### Task 2  
NAT and Static Routing (13 Points)  
Given is the network topology from Figure 2.1. PC1 and PC2 are parts of a private network that is connected to the Internet via R1. PC1 sends a message to the server SRV1. The figure shows relevant header parts of this message at three different points in the network.  

| SrcMAC | 00:53:00:be:ef:01 | SrcMAC | 00:53:01:be:ef:02 | SrcMAC | 00:53:03:be:ef:02 |  
|--------|-------------------|--------|-------------------|--------|-------------------|  
| DstMAC | 00:53:01:be:ef:01 | DstMAC | 00:53:02:be:ef:01 | DstMAC | 00:53:04:be:ef:01 |  
| SrcIP | 172.16.0.1 | SrcIP | 203.0.113.128 | SrcIP | 203.0.113.128 |  
| DstIP | 198.51.100.81 | DstIP | 198.51.100.81 | DstIP | 198.51.100.81 |  
| TTL | 63 | TTL | TTL |  
| SrcPort | 6814 | SrcPort | SrcPort |  
| DstPort | DstPort | DstPort |  

**Figure 2.1: Network Topology (grayed fields do not need to be filled out)**  

a) *Determine the L2 and L3 addresses of the devices in Figure 2.1. Enter the corresponding addresses completely in the table below. Addresses that do not emerge from Figure 2.1 should be marked with a dash (—).  

| L2 Addresses | L3 Addresses |  
|--------------|--------------|  
| PC1.eth0    | PC1.eth0    |  
| S.eth0      | S.eth0      |  
| S.eth1      | S.eth1      |  
| R1.eth0     | R1.eth0     |  
| R1.eth1     | R1.eth1     |  
| R2.eth0     | R2.eth0     |  
| R3.eth1     | R3.eth1     |  
| SRV1.eth0   | SRV1.eth0   |  

b) *Complete the Time-to-Live in Figure 2.1.  
c) *Complete the Destination Port in Figure 2.1 assuming that PC1 is trying to establish an encrypted connection to a website on SRV1 with the sent message.  

**Table 2.1 shows the content of the NAT table of R1 before the connection attempt by PC1.**  
d) *Add the resulting entry to the table as soon as PC1 sends the first packet to SRV1.  
Note: Take another look at Figure 2.1. If an entry cannot be clearly determined, make a sensible choice.  

| Private IP | Private Src Port | Public Src Port |  
|------------|------------------|-----------------|  
| 172.16.0.2 | 6812             | 6812            |  
| 172.16.0.2 | 6813             | 6813            |  
| 172.16.0.2 | 6814             | 6814            |  

**Table 2.1: NAT Table of R1**  

e) Provide the Destination IP, Source Port, and Destination Port of the response from SRV1.  
Note: If a value cannot be clearly determined, make a sensible choice.  
f) Explain in detail how R1 distinguishes whether the response is intended for PC1 or PC2.  
g) Explain in detail what modifications R1 must make to the response from SRV1.  

---

### Task 3  
Dynamic Routing (19 Points)  
Given is the network shown in Figure 3.1. The routing protocol used is RIP. The tables next to/above the routers represent the routing table of the respective router. Here, Dst stands for the respective destination router, NH for the respective next hop, and Cost for the cost to the respective destination.  

| Dst | NH | Cost |  
|-----|----|------|  
| A   | A  | 0    |  
| B   | B  | 0    |  
| C   | A  | 1    |  
| D   | C  | 1    |  
| E   | E  | 1    |  

**Figure 3.1: Topology**  

a) *What metric does RIP use? (No justification required)  
b) *RIP is a distance-vector protocol. Explain the difference to link-state protocols.  
c) *RIP belongs to the class of interior gateway protocols. Explain the difference to exterior gateway protocols.  
d) *In what way are networks whose routers exclusively use RIP as a routing protocol limited in size?  
e) *What information is contained in routing updates with RIP?  
f) *Justify whether RIP always chooses the shortest route (in terms of routers between source and destination).  
g) *Justify whether RIP always chooses the fastest route (in terms of transmission rate) to a destination.  
h) Complete the routing table of the router in Figure 3.1 (without indicating intermediate steps) so that a network of the shortest paths according to the metric of RIP is created.  

Now, the link between router D and E fails. Router D notices the failure immediately. Answer the following questions in the given order.  
i) Router D sends a periodic update. Describe the effects on routers A, B, and C.  
j) Router A now sends a periodic update. Describe the effects on routers B, C, and D.  
k) Describe the problem that arises and its solution.  

---

### Task 4  
Huffman (22 Points)  
In this task, we consider a simplified version of the ITU T.30 protocol, known as Telefax. This uses a combination of run-length encoding (RLE) and Huffman coding. The run-length encoding should start with "white" alternating the number of white and black pixels. We first consider the pixel graphic in Figure 4.1.  

**Figure 4.1: Pixel Graphic**  

a) *Determine the result of the run-length encoding.  
b) Determine the occurrence probabilities p of the individual RLE code words.  
c) Create a suitable binary Huffman code. Label the leaves with the corresponding RLE code words, all nodes with the corresponding probabilities, and assign the edges the corresponding sections of the Huffman code words.  
d) Create a codebook for the Huffman code.  
e) Encode the pixel graphic with the created Huffman code.  
f) Determine the compression factor compared to a direct transmission where each pixel is transmitted with 1 bit ("black" or "white").  

Now we consider the Huffman tree from Figure 4.2. We assume that it is used to encode a memoryless source with the alphabet A = {a, b, c}. The occurrence probabilities p of the characters are also indicated in the figure.  

**Figure 4.2: Huffman Tree**  

g) *Justify how many bits a uniform code requires on average to encode a character.  
h) *Determine the information content I(p) of the character.  
i) Determine the entropy of the source.  
j) *Determine the average Huffman code word length.  

---

### Task 5  
Wireshark (12 Points)  
Given is the network from Figure 5.1. PC1 and PC2 are connected via the Ethernet switch S with router R.  

Srv sends a packet to PC1. The corresponding Ethernet frame is captured immediately after the Ethernet interface of Srv and is shown in Figure 5.2.  

**Figure 5.1: Network Topology**  

**Figure 5.2: Ethernet Frame between Srv and R**  

To all sub-tasks, a brief justification must be provided, e.g., indicating or marking the relevant header field, pointing out the significance of the respective field, any scaling of fields, etc.  
Note: Use the headers and information printed on the cheatsheet for the solution.  

a) *Mark and label all fields of Layer 2 in Figure 5.2.  
b) *Determine the L2 addresses of the devices from Figure 5.1, as far as they emerge from the L2 header.  
c) *The Ethertype is 0x86dd, the IP version field indicates IPv6. Justify why it cannot be concluded that it is IPv6 based solely on the version field without knowledge of the Ethertype.  
d) Determine the source and destination address at Layer 3 of the packet in their usual notation.  
e) Justify whether the destination address from sub-task d) is the address of PC1 or R.  
f) Determine the length of the L3 header including any options or extension headers.  
g) Determine the total length of the packet, i.e., Layer 3 header including payload.  
h) *Assuming the packet from Srv to PC1 is an ICMP Echo Reply. There are two instances of an application running on PC1 that are waiting for such a packet sent by Srv. How is it distinguished which of the two instances the packet is intended for?  

---

### Task 6  
CRC (7 Points)  
Given is the CRC polynomial x^2 + x and the binary message m = 00110001.  

a) *Provide the CRC polynomial in binary notation.  
b) Determine the corresponding checksum.  
c) Provide the secured bit sequence that will be transmitted.  
d) *Explain what "secured" means in sub-task c).  

---

### Additional space for solutions. Clearly mark the assignment to each sub-task.  
Do not forget to cross out invalid solutions.