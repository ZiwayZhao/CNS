Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by attaching a code during attendance control.  
- This code contains only a sequential number, which is also noted on the attendance list next to the signature field.  
- This will be used as a pseudonym to allow a unique assignment of your exam.  

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Endterm  
Date: Monday, July 29, 2019  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 10:30–11:30  

### Instructions for Completion
- This exam consists of 12 pages with a total of 6 tasks and the included formula collection. Please check now that you have received a complete set of documents.  
- The total score for this exam is 90 points.  
- It is prohibited to tear pages out of the exam.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - an analog dictionary in the native language without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be counted where the solution path is recognizable. Text problems must also be justified unless otherwise stated in the respective task.  
- Do not write with red/green colors or with a pencil.  
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.  

### Additional space for solutions. Refer to this in the respective task. Do not forget to cross out invalid solutions.  
Leaving the auditorium from until / Early submission until  

---

### Task 1  
Packet Pair Probing (11.5 points)  
Given the network depicted in Figure 1.1. Nodes 1 and 4 are connected to their routers via a full-duplex-capable network. The symmetric data rates on the links are \( r_{12} \) and \( r_{34} \). The connection between nodes 2 and 3 is significantly slower, i.e., \( r_{23} < r_{34}, r_{12} \). The distances \( d_{12} \) and \( d_{23} \) are negligible in comparison to \( d_{34} \).

```
1  2  3  4
```

**Figure 1.1: Simplified Network Topology**  
Node 1 is to determine the data rate \( r_{23} \) such that as little load as possible is generated on the already slow connection. It is assumed that all nodes have a standard IP stack and that ICMP packets can be exchanged between nodes 1 and 4.

a) *Provide the serialization time and propagation delay between two neighboring nodes \( i \) and \( j \) as a function of the packet size \( p \), data rate \( r \), and distance \( d \).  

Node 1 sends two ICMP Echo Requests of length \( p \) to node 4 one after the other. The value of \( p \) is chosen such that no fragmentation is necessary along the path to node 4. Node 4 will respond to each Echo Request with an Echo Reply of the same size. For simplification, processing times at the nodes can be neglected.

b) *Complete the path-time diagram depicted in the solution field.  
**Note:** If necessary, you will find a replacement form at the end of the exam.  

Due to the low transmission rate between nodes 2 and 3, a reception pause \( \Delta t \) occurs at node 1. This can be measured by node 1 and used to determine the sought transmission rate between nodes 2 and 3.

c) Mark \( \Delta t \) in your solution from part task b).  

d) What quantities does \( \Delta t \) depend on if \( r_{23} < r_{34} \) holds? (without justification)  

e) Explain what would change in comparison to the previous part task if \( r_{23} > r_{34} \) holds.  

f) Determine \( \Delta t \) generally for \( r_{23} < r_{12}, r_{34} \). Simplify the result as much as possible.  

g) Provide an expression for the sought data rate \( r_{23} \). Simplify the result as much as possible.  

---

### Task 2  
Wireshark (20 points)  
Given the network from Figure 2.1a. The depicted packet is directed from PC1 to Srv.  

```
Srv
PC1 R1 R2
```

**Figure 2.1a: Network Topology**  
```
0x0000 90 e2 ba 2a 8d 97 90 e2 ba 86 dd 60 08 00 45 10
0x0010 00 3c b0 95 40 00 40 06 77 37 c0 a8 f0 06 0a 35
0x0020 57 fb e0 da 0d 3d 81 8b e4 cc 00 00 00 00 a0 02
0x0030 6a 40 bb f7 00 00 02 04 05 50 04 02 08 0a 66 83
0x0040 54 59 00 00 00 00 01 03 03 07
```

**Figure 2.1b: Ethernet Frame between R1 and R2**  
The offset is the index into the byte array and must be specified as 0-based (as in Java code). Provide interpreted data such as addresses or ports in their usual and shortened notation.  
**Note:** Use the header and information printed on the cheat sheet for the solution.  

Example: Determine the Layer 2 address of the recipient.  
Offset: 0x0000 Length: 6  
Address: 90:e2:ba:2a:8d:97 belongs to node: <Name>  

a) *Determine the Layer 2 address of the sender.  
Offset: Length:  
Address: belongs to node:  

b) *Justify which Layer 3 protocol is used.  

c) Determine the Layer 3 address of the recipient.  
Offset: Length:  
Address:  

d) Determine the Layer 3 address of the sender.  
Offset: Length:  
Address:  

e) *Justify how to recognize that the Layer 3 header has a length of 20B.  

f) *Clearly mark the point in Figure 2.1b that indicates that the IPv4 payload is TCP.  
**Re-entry:** Layer 4 header (TCP) starts at index 0x0022.  

g) *Provide the destination port. (without justification)  

h) *Provide the exact position (offset and position within the respective byte) of the TCP flags, the flags themselves, and their respective values.  
Offset:  
Flag  
Value  

i) *Provide the minimum length of the TCP header. (without justification)  

j) *Determine the exact length of the TCP header from Figure 2.1b. (with justification)  

k) What causes the length difference in this case?  

---

### Task 3  
IPv6 (19 points)  
Given the network topology in Figure 3.1. The router R is connected to the network NET1 via GW and to the Internet and supplies the networks NET2 and NET3. NET3 is used for WLAN clients.  

```
eth0: 00:00:5e:00:55:11 
eth0: 12:e4:4e:71:13:37
2001:db8:1:b::1:0/64 
2001:db8:1:a:10e4:4eff:fe71:1337/64
C S R GW
NET2 NET1
Internet
2001:db8:1:b::/64 
2001:db8:1:a::/64
eth0: 00:00:5e:00:55:00 
ppp0: 00:00:5e:00:55:12
2001:db8:1:b::1 
2001:db8:1:a:200:5eff:fe00:5512/64
wlan0: 00:00:5e:00:55:13
NET3 2001:db8:1:c::1:0/64
2001:db8:1:c::/64
```

**Figure 3.1: Topology**  
a) *How does R receive the IP address 2001:db8:1:a:200:5eff:fe00:5512 on interface ppp0?  

b) *Name the fundamental difference in fragmentation between IPv4 and IPv6.  

c) *Show that NET2 and NET3 cannot be aggregated on GW.  

d) *Justify why NET1 and NET2 cannot be aggregated on GW.  

e) *Name the procedure by which a router decides where to forward a packet.  

f)  
g)  
h)  

**Table 3.1: Routing table on R**  
f) Fill in the usual column names in the routing table 3.1.  

g) Complete the routing table 3.1 for R so that the connected networks can reach the Internet and can be reached from there. Aggregate as much as possible.  
**Note:** Additional empty lines are provided. Clearly cross out invalid entries.  

h) Argue where router R forwards a packet with the destination address fe80::1:2ff:fe03:405.  

i) *Differentiate between L2 and L3 addresses regarding their use.  

j) *By what method is the MAC address resolved in IPv4?  

k) *By what method is the MAC address resolved in IPv6?  

l) Provide the respective L2 and L3 addresses in the header of the sent packet for address resolution in IPv6 and IPv4. If certain addresses are not present or needed, mark these entries in the solution field as "not applicable".  

| Address | IPv6 | IPv4 |  
|---------|------|------|  
| L2 Sender |      |      |  
| L2 Receiver |      |      |  
| L3 Sender |      |      |  
| L3 Receiver |      |      |  

---

### Task 4  
Sampling and Quantization (11 points)  
Given is the baseband signal depicted in Figure 4.1a. The signal is to be sampled, quantized, and the transmitted bit sequence reconstructed.  

```
s(t)
```

**Figure 4.1a: Baseband Signal \( s(t) \)**  
**Figure 4.1b: Assignment**  

a) *Sample the signal \( s(t) \) with the sampling frequency \( f = 500 \) Hz. Enter the sample values as a time-discrete signal directly into Figure 4.1a. Choose the first sampling time point \( t = 1.0 \) ms.  

The signal is to be quantized in the interval \([-2; 2]\) with four levels, so that the maximum quantization error within the interval is minimized.  

b) *Provide the numerical values of the quantization levels in Table 4.1b sorted in ascending order (smallest value first).  

The quantization levels are assigned binary code words, where the code words are interpreted as decimal values assigned to the levels in ascending order. The smallest code word interpreted as a decimal value is assigned to the lowest quantization level.  

c) *Complete Table 4.1b with the corresponding code words.  

d) *Determine the maximum quantization error within the interval \([-2, 2]\). (Calculation or justification)  

e) Provide the quantized sample values in the table below.  

f) Provide the received message in binary representation per symbol in the table below.  

| Numerical | Binary |  
|-----------|--------|  
|           |        |  

g) Derive the achievable data rate based on the relevant theorem.  

---

### Task 5  
Short Tasks (13.5 points)  
The following sub-tasks are each independently solvable.  

a) *In the lecture, the term "WLAN router" was discussed. Which devices of layers 1–3 are typically combined in such a device?  

b) *How is the frequently used MSS of 1460B established?  

c) *What is the purpose of bit stuffing?  

d) You operate a web server behind a NAT. Briefly describe what you need to do for this web server to be accessible from the Internet.  

e) *Draw a simplified path-time diagram (flowchart) for DHCP. Assume a network with a DHCP server and a currently unconfigured client. Ensure complete labeling of the diagram.  

f) *Explain the function and result of the syscall select() in bullet points.  

g) Given the binary data word 1100110010101010 in Big Endian. Provide it in Network Byte Order.  

h) *Explain the terms stream-oriented and message-oriented with respect to Layer 4.  

---

### Task 6  
Multiple Choice (15 points)  
The following sub-tasks are each independently solvable and come from the pre-lecture quizzes. The grading scheme also corresponds to that of the quizzes: 1 or 0 points for tasks with only one correct answer or a gradation of 0.5 points for a missing or incorrect answer, provided more than one answer is correct.  

a) *What is the result of the definite integral \( \int_{0}^{T/2} \sin(2\pi ft) dt \) (for \( f, T \in \mathbb{R} \))?  
- \( -\frac{1}{2\pi f} (1 - \cos(\pi f T)) \)  
- \( \frac{1}{2\pi f} (1 + \cos(\pi f T)) \)  
- none of the above  

b) Given the rectangular pulse \( s(t) \) and the cosine pulse \( s(t) \). The figure below shows four different spectra. Which statements are correct?  

c) The adjacent signal space assignment represents which modulation methods?  
- 1-PSK  
- 2-ASK  
- 2-QAM  
- 2-PSK  
- 1-QAM  
- 1-ASK  

d) Given the Manchester-encoded transmission signal depicted below. Which bit sequence(s) fit(s) this signal?  

e) *Which statements about MLT-3 are correct?  
- There are three different signal levels.  
- It is a channel code.  
- It is a line code.  
- 01 always generates a level change.  
- DC freedom is guaranteed.  
- One symbol encodes 3 bits.  

f) *Which statements about CSMA are correct?  
- CSMA belongs to the non-deterministic time-division multiplexing methods.  
- CSMA is the underlying media access method for Ethernet.  
- CSMA guarantees each of N participants an average of \( \frac{1}{2N} \) of the channel bandwidth.  
- CSMA allows multiple stations to access the medium simultaneously.  
- CSMA is a frequency multiplexing method.  

g) *What are the tasks of the data link layer?  
- Addressing between direct connection networks  
- Congestion control when forwarding messages  
- Protection against unauthorized eavesdropping of messages  
- Checking messages for transmission errors  
- Addressing in a direct connection network  
- Control of media access  

h) *What is the essential difference between CSMA/CD and CSMA/CA?  
- CSMA/CD uses acknowledgments, unlike CSMA/CA.  
- In media access using CSMA/CA, there is always a contention phase.  
- There are only differences in collision handling, not in media access.  
- CSMA/CA requires a minimum frame length of 64B.  

i) *Given a baseband signal with 16 distinguishable symbols and a transmission channel with a bandwidth of 1MHz and an SNR of 7. Determine the achievable data rate.  
- 5 Mbit/s  
- 6 Mbit/s  
- 4 Mbit/s  
- 3 Mbit/s  
- 8 Mbit/s  
- 7 Mbit/s  

j) *The signal power is 1mW, and the SNR is 20dB. Determine the noise power.  
- 10µW  
- 100µW  
- 500mW  
- 10mW  
- 50µW  
- 5mW  
- 1mW  
- 50mW  
- 100mW  
- 500µW  

k) *Which of the following IP addresses are not public addresses?  
- 10.10.10.10  
- 192.169.1.1  
- 192.168.255.0  
- 8.8.8.8  
- 172.16.20.1  
- 127.0.0.1  

l) *Which of the mentioned routing protocols are Interior Gateway Protocols?  
- RIP  
- ISIS  
- OSPF  
- BGP  
- IGRP  
- EIGRP  

m) *What fields are found in the TCP header?  
- Window  
- Sequence Number  
- Source Address  
- Protocol  
- Destination Port  
- Push Flag  
- Fragment Offset  
- TTL/Hop Limit  

n) *In which of the following described networks (based on Ethernet) with at least three hosts are collision and broadcast domains identical?  
- Hosts connected via a router.  
- Hosts connected via a hub.  
- Hosts connected via a switch.  
- Hosts and a router connected via a hub.  

o) *What is the FQDN for the PTR record of the IP address 203.0.113.42?  
- 42.113.0.203.in-addr.arpa.  
- 203.0.113.42.in-addr.arpa.  
- 24.311.0.302.in-addr.arpa.  
- 302.0.311.21.in-addr.arpa.  

### Additional Form for Task 1b)  
1 2 3 4  
t