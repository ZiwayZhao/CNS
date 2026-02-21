Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized during the attendance check by affixing a code.  
- This contains only a sequential number, which is also noted on the attendance list next to the signature field.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Endterm  
Date: Monday, July 29, 2019  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 10:30–11:30  

**Instructions for Processing:**  
- This exam consists of 12 pages with a total of 6 tasks and the included formula collection. Please check now that you have received a complete set of documents.  
- The total score for this exam is 90 points.  
- The removal of pages from the exam is prohibited.  
- The following aids are permitted:  
  - A non-programmable calculator  
  - An analog dictionary in the native language without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be counted where the solution method is recognizable. Text problems must also be justified unless explicitly stated otherwise in the respective task.  
- Do not write with red/green colors or with pencil.  
- Turn off all electronic devices you have brought, store them in your bag, and close it.  

**Additional space for solutions. Please refer to this in the respective task. Do not forget to cross out invalid solutions.**  

**Leaving the lecture hall from until / Early submission until**  
– Page 1/12 –  

**Task 1**  
Packet Pair Probing (11.5 points)  
Given the network depicted in Figure 1.1. Nodes 1 and 4 are connected to their routers via a full-duplex-capable network. The symmetric data rates on the links are \( r_{12} \) and \( r_{34} \). The connection between nodes 2 and 3 is significantly slower, i.e., \( r_{23} < r_{34}, r_{12} \). The distances \( d_{12} \) and \( d_{23} \) are negligible in relation to \( d_{34} \).  

![Figure 1.1: Simplified Network Topology](#)  

Node 1 should determine the data rate \( r_{23} \) so that as little load as possible is generated on the already slow connection. It is assumed that all nodes have a standard IP stack and that ICMP packets can be exchanged between nodes 1 and 4.  

a) *Specify the serialization time and propagation delay between two neighboring nodes \( i \) and \( j \) as a function of the packet size \( p \), data rate \( r \), and distance \( d \).*  
\[
t_{s(i,j)} = \frac{p}{r_{ij}}, \quad t_{p(i,j)} = \frac{d_{ij}}{c}
\]  

Node 1 sends two ICMP Echo Requests of length \( p \) to node 4 one after the other. The length \( p \) is chosen such that no fragmentation is necessary along the path to node 4. Node 4 will respond to each Echo Request with an Echo Reply of the same size. For simplification, processing times at the nodes are to be neglected.  

b) *Complete the path-time diagram depicted in the solution field.*  

**Note:** If necessary, you will find a replacement form at the end of the exam.  

Through the low transmission rate between nodes 2 and 3, a reception pause \( \Delta t \) occurs at node 1. This can be measured by node 1 and used to determine the sought transmission rate between nodes 2 and 3.  

c) Mark \( \Delta t \) in your solution from part task b).  

d) What quantities does \( \Delta t \) depend on if \( r_{23} < r_{34} \) holds? (without justification)  
\( p, r_{12}, r_{23} \)  

e) Explain what would change in comparison to the previous task if \( r_{23} > r_{34} \) holds.  
For \( r_{23} < r_{34} \), the serialization time at node 4 is limited instead of at node 3, which is why \( \Delta t \) becomes independent of \( r_{23} \) and dependent on \( r_{34} \).  

f) Determine \( \Delta t \) generally for \( r_{23} < r_{12}, r_{34} \). Simplify the result as much as possible.  
\[
\Delta t = t_{(2,3)} - t_{(1,2)} = \frac{p}{r_{23}} - \frac{p}{r_{12}} = p \left( \frac{1}{r_{23}} - \frac{1}{r_{12}} \right)
\]  

g) Provide an expression for the sought data rate \( r_{23} \). Simplify the result as much as possible.  
\[
r_{23} = \frac{p}{\Delta t + p} \cdot r_{12}
\]  
– Page 3/12 –  

**Task 2**  
Wireshark (20 points)  
Given the network from Figure 2.1a. The depicted packet is addressed from PC1 to Srv.  

![Figure 2.1a: Network Topology](#)  

```
0x0000 90 e2 ba 2a 8d 97 90 e2 ba 86 dd 60 08 00 45 10
0x0010 00 3c b0 95 40 00 40 06 f) 77 37 c0 a8 f0 06 0a 35
0x0020 57 fb e0 da 0d 3d 81 8b e4 cc 00 00 00 00 a0 02
0x0030 6a 40 bb f7 00 00 02 04 05 50 04c02 08 0a 66 83
0x0040 54 59 00 00 00 00 01 03 03 07
```

**Figure 2.1b: Ethernet Frame between R1 and R2**  
The offset is the index into the byte array and must be specified in 0-based indexing (as in Java code). Provide interpreted data such as addresses or ports in their usual and shortened notation.  

**Note:** Use the header and information printed on the cheat sheet for the solution.  

Example: Determine the Layer 2 address of the recipient.  
Offset: 0x0000 Length: 6  
Address: 90:e2:ba:2a:8d:97 belongs to node: <Name>  

a) *Determine the Layer 2 address of the sender.*  
Offset: 0x0006 (6) Length: 6  
Address: 90:e2:ba:86:dd:60 belongs to node: R1  

b) *Justify which Layer 3 protocol is used.*  
Ethertype 0x0800 = IPv4  

c) Determine the Layer 3 address of the recipient.  
Offset: 0x001e (30) Length: 4  
Address: 10.53.87.251  

d) Determine the Layer 3 address of the sender.  
Offset: 0x001a (26) Length: 4  
Address: 192.168.240.6  

e) *Justify how you can tell that the L3 header has a length of 20B.*  
The lower nibble of the IHL is 0x5, which indicates the length of the IPv4 header in multiples of 4 bytes.  

f) *Clearly mark the position in Figure 2.1b that indicates that the IPv4 payload is TCP.*  
The L4 header (TCP) starts at index 0x0022.  

g) *Provide the destination port. (without justification)*  
3389  

h) *Provide the exact position (offset and position within the respective byte) of the TCP flags, the flags themselves, and their respective values.*  
Offset: lower 6 bits of the byte at position 0x002f (47)  
Flag – – URG ACK PSH RST SYN FIN  
Value 0 0 0 0 1 0  

i) *Provide the minimum length of the TCP header. (without justification)*  
20B  

j) *Determine the exact length of the TCP header from Figure 2.1b. (with justification)*  
0xa0 at offset 0x002e contains in the most significant 4 bits the field offset (0xa), which indicates the total length of the TCP header in multiples of 4 bytes.  
The header length is therefore \( 10 \times 4B = 40B \).  

k) What causes the length difference in this case?  
The TCP header contains options.  
– Page 5/12 –  

**Task 3**  
IPv6 (19 points)  
Given the network topology in Figure 3.1. Router R is connected to the network NET1 via GW and to the Internet, and supplies the networks NET2 and NET3. NET3 is used for WLAN clients.  

![Figure 3.1: Topology](#)  

a) *How does R receive the IP address 2001:db8:1:a:200:5eff:fe00:5512 at the interface ppp0?*  
It is likely an automatically configured address. The router generates this via Stateless Address Autoconfiguration (SLAAC) from the prefix announcement and the MAC address of the interface.  

b) *Name the fundamental difference in fragmentation between IPv4 and IPv6.*  
In IPv4, fragmentation can occur in the network, while in IPv6, it can only occur on the hosts.  

c) *Show that NET2 and NET3 cannot be aggregated on GW.*  
NET2 and NET3 are not in the same /63 prefix. For bits 61 to 64: \( b = 1010, c = 1100 \).  

d) *Justify why NET1 and NET2 cannot be aggregated on GW.*  
NET2 is not directly reachable and is routed via R. NET1 is directly connected to GW.  

e) *Name the method by which a router decides where to forward a packet.*  
Longest-Prefix-Matching  

f)  
| Destination | Next Hop | Interface |  
|--------------|----------|-----------|  
| 2001:db8:1:a::/64 | :: | ppp0 |  
| 2001:db8:1:b::/64 | :: | eth0 |  
| 2001:db8:1:c::/64 | :: | wlan0 |  
| ::/0 | 2001:db8:1:a:10e4:4eff:fe71:1337 | ppp0 |  

**Table 3.1: Routing table on R**  

g) *Fill in the usual column names in the routing table 3.1.*  
h) Complete the routing table 3.1 for R so that the connected networks can reach the Internet and can be reached from there. Aggregate as much as possible.  
**Note:** Additional empty lines are provided. Clearly cross out invalid entries.  

i) Argue where router R forwards a packet with the destination address fe80::1:2ff:fe03:405.  
The router does not forward the packet because it is a link-local address.  

j) *Differentiate between L2 and L3 addresses regarding their usage.*  
L2: Next Hop addressing, L3: End-to-End addressing  

k) *By which method is the MAC address resolved in IPv4?*  
ARP  

l) *By which method is the MAC address resolved in IPv6?*  
Neighbor Discovery  

m) Provide the L2 and L3 addresses in the header of the sent packet for address resolution in IPv6 and IPv4. If certain addresses are not present or needed, mark these entries in the solution field as "not applicable."  
| Address | IPv6 | IPv4 |  
|---------|------|------|  
| L2 Sender | 00:00:5e:00:55:11 | 00:00:5e:00:55:11 |  
| L2 Recipient | 33:33:ff:00:00:01 | ff:ff:ff:ff:ff:ff |  
| L3 Sender | 2001:db8:1:b::1:0 | not applicable |  
| L3 Recipient | ff02::1:ff00:1 | not applicable |  
– Page 7/12 –  

**Task 4**  
Sampling and Quantization (11 points)  
Given the baseband signal depicted in Figure 4.1a. This signal should be sampled, quantized, and the transmitted bit sequence reconstructed.  

![Figure 4.1: Baseband Signal and Mapping](#)  

a) *Sample the signal \( s(t) \) with a sampling frequency \( f = 500Hz \). Enter the sample values as a time-discrete signal directly into Figure 4.1a. Choose the first sampling time point \( t = 1.0ms \).*  
The signal should be quantized in the interval \([-2; 2]\) with four levels, so that the maximum quantization error within the interval is minimized.  

b) *Provide the numerical value of the quantization levels in Table 4.1b sorted in ascending order (smallest value first).*  
The quantization levels are assigned binary code words, with the code words interpreted as decimal values assigned to the levels in ascending order. The smallest code word interpreted as a decimal value is assigned to the lowest quantization level.  

c) *Complete Table 4.1b with the corresponding code words.*  

d) *Determine the maximum quantization error within the interval \([-2, 2]\). (Calculation or justification)*  
The maximum quantization error is \( \Delta/2 \). With \( \Delta = 1 \), this results in a maximum error of 0.5.  

e) *Provide the quantized sample values in the table below.*  

f) *Provide the received message in binary representation per symbol in the table below.*  
| Numerical | 1.5 | 0.5 | 1.5 | 0.5 | 1.5 | 1.5 |  
|-----------|-----|-----|-----|-----|-----|-----|  
| Binary    | 11  | 10  | 00  | 01  | 00  | 00  |  

**Table 4.1: Quantized Sample Values and Binary Representation of the Message**  

g) *Derive the achievable data rate based on the relevant theorem.*  
\[
r = 2B \log_2(M), \text{ with } 2B = f_a = 500Hz: 500Hz \log_2(4) = 1kbit/s
\]  
– Page 8/12 –  

**Task 5**  
Short Tasks (13.5 points)  
The following sub-tasks can be solved independently of each other.  

a) *In the lecture, the term "WLAN router" was discussed. Which devices of layers 1–3 are typically combined in such a device?*  
Router (L3), Switch (L2), Media Converter (L1) (or WLAN AP), Modem (L1)  

b) *How is the frequently used MSS of 1460B established?*  
1500B MTU (Ethernet) minus 20B IPv4 header and 20B TCP header.  

c) *What is the purpose of bit stuffing?*  
Prevention of the occurrence of frame delimiters in the payload.  

d) *You operate a web server behind a NAT. Briefly describe what you need to do for this web server to be reachable from the Internet.*  
Port forwarding on the NAT from TCP 80 or TCP 443 to the port on which the local web server expects incoming connections.  

e) *Draw a simplified path-time diagram (flowchart) for DHCP. Assume a network with a DHCP server and a previously unconfigured client. Ensure complete labeling of the diagram.*  
```
Client          Server  
DHCP Discover  
                DHCP Offer  
DHCP Request  
                DHCP ACK/NACK  
```  
– Page 9/12 –  

f) *Explain the function and result of the syscall select() in bullet points.*  
- Monitors multiple sets of file descriptors for activity  
- Modifies the sets so that only activated file descriptors are included  
- Returns the number of activated file descriptors (-1 on error and 0 on timeout)  

g) *Given the binary data word 1100110010101010 in Big Endian. Provide it in Network Byte Order.*  
1100110010101010  

h) *Explain the terms stream-oriented and message-oriented regarding layer 4.*  
- Stream-oriented: Sending/receiving data occurs byte-wise without guarantee that message boundaries are preserved.  
- Message-oriented: Message boundaries are preserved. (Whether there is a guarantee that messages also arrive does not imply this.)  

**Task 6**  
Multiple Choice (15 points)  
The following sub-tasks can be solved independently of each other and are derived from the pre-lecture quizzes. The grading scheme also corresponds to that of the quizzes: 1 or 0 points for tasks with only one correct answer or a gradation of 0.5 points for a missing or incorrect answer, provided more than one answer is correct.  

a) *What is the result of the definite integral \( \int_0^{T/2} \sin(2\pi ft) dt \) (for \( f, T \in \mathbb{R} \))?*  
-1 1 (1 - cos(πfT)) 1 + cos(πfT)  

b) *Given the rectangular pulse \( s_1(t) \) and the cosine pulse \( s_2(t) \). The figure below shows four different spectra. Which statements are correct?*  
(a) \( S_1(f) \) (b) \( S_2(f) \) (c) \( S_3(f) \) (d) \( S_4(f) \)  

c) *Which modulation methods does the adjacent signal-space mapping represent?*  
1-PSK, 2-ASK, 2-QAM, 2-PSK, 1-QAM, 1-ASK  

d) *Given the Manchester-encoded transmission signal depicted below. Which bit sequence(s) fit(s) this signal?*  
11010001, 1010011001010110, 0101  

e) *Which statements about MLT-3 are correct?*  
- There are three different signal levels. It is a channel code.  
- It is a line code. 01 always generates a level change.  
- DC freedom is guaranteed. One symbol encodes 3 bits.  

f) *Which statements about CSMA are correct?*  
CSMA belongs to non-deterministic time-division multiplexing methods.  
CSMA is the underlying media access method for Ethernet.  
CSMA guarantees each of the N participants an average of \( \frac{1}{2N} \) of the channel bandwidth.  
CSMA allows multiple stations simultaneous access to the medium.  
CSMA is a frequency multiplexing method.  

g) *What are the tasks of the data link layer?*  
- Addressing between direct connection networks  
- Congestion control when forwarding messages  
- Protection against unauthorized eavesdropping of messages  
- Checking messages for transmission errors  
- Addressing in a direct connection network  
- Control of media access  

h) *What is the essential difference between CSMA/CD and CSMA/CA?*  
CSMA/CD uses acknowledgments, while media access with CSMA/CA always has a contention phase.  
There are only differences in collision handling, not in media access.  
CSMA/CA requires a minimum frame length of 64B.  

i) *Given a baseband signal with 16 distinguishable symbols and a transmission channel with a bandwidth of 1MHz and an SNR of 7. Determine the achievable data rate.*  
5Mbit/s, 6Mbit/s, 4Mbit/s, 3Mbit/s, 8Mbit/s, 7Mbit/s  

j) *The signal power is 1mW, and the SNR is 20dB. Determine the noise power.*  
10µW, 100µW, 500mW, 10mW, 50µW, 5mW, 1mW, 50mW, 100mW, 500µW  

k) *Which of the following IP addresses are not public addresses?*  
10.10.10.10, 192.169.1.1, 192.168.255.0, 8.8.8.8, 172.16.20.1, 127.0.0.1  

l) *Which of the mentioned routing protocols are Interior Gateway Protocols?*  
RIP, ISIS, OSPF, BGP, IGRP, EIGRP  

m) *What fields are present in the TCP header?*  
Window, Sequence Number, Source Address, Protocol, Destination Port, Push Flag, Fragment Offset, TTL/Hop Limit  

n) *In which of the following described networks (based on Ethernet) with at least three hosts are collision and broadcast domains identical?*  
Hosts connected via a router. Hosts connected via a hub. Hosts connected via a switch. Hosts and a router connected via a hub.  

o) *What is the FQDN for the PTR record of the IP address 203.0.113.42?*  
42.113.0.203.in-addr.arpa. 203.0.113.42.in-addr.arpa. 24.311.0.302.in-addr.arpa. 302.0.311.21.in-addr.arpa.  

**Additional form for Task 1b)**  
– Page 12/12 –