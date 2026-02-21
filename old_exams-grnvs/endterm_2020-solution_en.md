Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during attendance control by affixing a code.
- This code contains only a continuous number, which should also be pasted on the attendance lists marked with the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Basics of Computer Networks and Distributed Systems  
**Exam: IN0010/Endtermonsite**  
**Date: Thursday, July 30, 2020**  
**Examiner: Prof. Dr.-Ing. Georg Carle**  
**Time: 08:00–09:30**  

### Instructions for Completion
- This exam consists of 12 pages with a total of 6 tasks. Please check now that you have received a complete set of documents.
- The total score for this exam is 90 points.
- The tearing out of pages from the exam is prohibited.
- Allowed aids:  
  - all electronic and non-electronic aids  
  - explicitly not allowed are internet and teamwork  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results are counted where the solution path is recognizable. Text tasks must generally be justified unless otherwise noted in the respective sub-tasks.
- Please do not write with red/green colors or with pencil.  
- Additional space for solutions. Clearly mark the assignment to the respective sub-task. Do not forget to cross out invalid solutions.

### Task 1  
**Multiple Choice (18 Points)**  
The following sub-tasks are multiple-choice multiple-answer with 1 point for each correct answer and -1 point for each incorrect answer (exception sub-tasks c) and d) with 0.5 points per cross). Multiple answers may be correct.  
The minimum score per sub-task is 0 points, i.e., negative points do not carry over to other sub-tasks.

**Instructions for completion on paper or if your PDF editor does not support the checkbox function:**  
- Cross the correct answers.  
- Crosses can be erased by completely filling them in.  
- Erased answers can be crossed again by the adjacent markings.

a) *Which of these IP addresses are public routable addresses?  
- 10.0.0.1  
- fe80::95:13:42  
- 2001:db8::921:2e11:d2c6:938b  
- 10.11.12.13  
- 192.168.36.2  
- 172.32.0.5  

b) *How many recursive DNS queries must a client send at a minimum to resolve the domain net.in.tum.de? The DNS cache is empty.  
- 3  
- 0  
- 2  
- 1  
- 5  
- 4  

c) *Which edges are included in the minimum spanning tree of the adjacent graph?  
- (A,B)  
- (C,D)  
- (B,D)  
- (B,C)  
- (A,C)  

d) *Which edges are included in the shortest path tree with root D of the adjacent graph?  
- (A,C)  
- (A,B)  
- (C,D)  
- (B,C)  
- (B,D)  

e) *Given is a link with a bandwidth of 872 Mbit/s and a propagation delay of 96 ms. Determine the bandwidth-delay product.  
- 9.0 s  
- 83.71 Mbit  
- 41.86 Mbit  
- 18.17 Mbit  

f) *Given is the 2-byte long data 0100101000110111 in Little Endian. What is the representation in Network Byte Order?  
- 0100101000110111  
- 1110110001010010  
- 0011011101001010  
- 1101110010100001  
- 0111001110100100  
- none of these  

g) *Given is a binary message source that emits symbols from an alphabet consisting of 34 characters, whose occurrence probabilities are independent and uniformly distributed. What is the average codeword length when using a Huffman code?  
- = 5 bit  
- < 5 bit  
- > 5 bit  
- Huffman codes are not applicable  

h) *Given is a wireless transmission with a frame error probability of α = 0.125. Determine the probability that 2 transmissions are not sufficient to successfully transmit the frame.  
- 0.99805  
- none of these  
- 0.23438  
- 0.01563  
- 0.98438  

i) *Given is the time signal below, which is to be developed as a Fourier series.  
What statements about the Fourier coefficients are correct?  
- ak > 0  
- a0 = 0  
- bk = 0  
- a0 ≠ r0  
- bk ≠ 0  
- ak > 0 ≠ 0  

j) *Given is the IPv4 address 117.201.134.85. What would the corresponding PTR record in DNS be?  
- 117.201.134.85.in-addr.arpa.  
- 117.201.134.85.  
- 85.134.201.117.in-addr.arpa.  
- none of these  
- 85.134.201.117.  
- an FQDN like tum.de.  

k) *Which of the following system calls only make sense with connection-oriented sockets?  
- bind()  
- sendto()  
- accept()  
- listen()  
- close()  
- select()  

l) *Which of the following terms does not describe a specific routing protocol, but an entire class of routing protocols?  
- IS-IS  
- IGRP  
- EGP  
- RIP  
- BGP  
- OSPF  
- EIGRP  
- IGP  

### Task 2  
**Design Your Own Smart Home (28 Points)**  
You want to set up your own smart home. From various sources, you have learned that many providers of "smart" devices do not take the topic of security very seriously. Therefore, you decide to assign your private computers and the smart home devices to different IPv4 subnets. The network topology is given in Figure 2.1. Both routers use NAT on interface eth0.  
All devices should be able to communicate with other devices in the same subnet and the internet. However, the smart home devices (in the Smartnet) should not be able to connect to the private computers (in the home network) on their own. Conversely, this should work, for example, to access the smart home controller with the laptop.

a) *Assign a meaningful IPv4 address to all interfaces in your network topology. To follow the convention, routers must always receive one of the highest possible IPs.  
- eth0: 131.159.32.42  
- eth2: 10.0.2.2  
- R1  
- R2  
- 10.0.2.0/30  
- 131.159.32.0/24  
- Internet  
- eth0: 10.0.2.1  
- reth1: 10.0.1.254  
- Smart Home Controller  
- eth1: 10.0.0.14  
- eth0: 10.0.1.1  
- MAC: 79:ea:fc:b7:86:c8  
- Home Network  
- Smartnet  
- 10.0.0.2/28  
- 10.0.1.0/24  
- Temperature Sensor  
- eth0: 10.0.1.2  
- MAC: 17:6f:04:ac:01:9c  
- Laptop  
- Smart-Toaster  
- eth0: 10.0.0.2  
- eth0: 10.0.1.3  
- MAC: 6e:4a:ba:f7:b5:91  
- MAC: d1:78:66:8f:2e:41  

**Figure 2.1: Network topology and IPv4 addressing**  

b) *Argue briefly whether this specific network topology, together with the NAT functionality, is sufficient to secure your home network.  
- No, the goal of NAT is not security, but to save IP addresses. Additionally, a firewall should be used.  

c) *Explain which IP address appears to a server on the internet as a communication partner when you surf the internet with the laptop.  
- 131.159.32.42, as this is the global IP address of the router that is recorded as the sender by NAT.  

d) *Provide the routing tables of routers R1 and R2. Provide the minimal set of routes and sort the entries in descending order by the length of the prefix. Note the desired reachability of the subnets from each other from the specification.  
**Routing Table of R1**  
| Destination       | Next Hop       | Iface  |
|-------------------|----------------|--------|
| 10.0.2.0/30      | 0.0.0.0       | eth0   |
| 10.0.0.0/28      | 0.0.0.0       | eth1   |
| 0.0.0.0/0        | 10.0.2.1      | eth0   |

**Routing Table of R2**  
| Destination       | Next Hop       | Iface  |
|-------------------|----------------|--------|
| 10.0.2.0/30      | 0.0.0.0       | eth2   |
| 10.0.1.0/24      | 0.0.0.0       | eth1   |
| 131.159.32.0/24  | 0.0.0.0       | eth0   |
| 0.0.0.0/0        | 131.159.32.254 | eth0   |

e) *You want to call the HTTP web interface of your smart home controller to make a "smart" toast. Your laptop sends a TCP SYN segment to the smart home controller. Sketch a simple path-time diagram that considers all frames that must be transmitted over the respective connections. Indicate which Layer 2, 3, and 4 headers are contained. (The diagram does not need to be to scale. Serialization times and propagation delays can be neglected.) Assume that there are currently no mappings cached between IP and MAC addresses.  
**Smart Home**  
**Laptop**  
**R1**  
**R2**  
**Controller**  
- ARP  
- ARP  
- Ethernet, IPv4, TCP  
- ARP  
- ARP  
- Ethernet, IPv4, TCP  
- ARP  
- ARP  
- Ethernet, IPv4, TCP  

f) *Fill out the Layer 3 packet sent from the laptop in sub-task e) with the IPv4 header. Assume that the headers contain no options. It should be clear whether the fields are to be interpreted as binary, decimal, hexadecimal, or as an IP address.  
| 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0x4 | 0x5 | 40 (10) (Length IP + TCP Header) | 0x1 | 0 | 0 | 0 | 0 | 128 (10) | 0x06 | 10.0.0.2 (IP Laptop) | 10.0.1.1 (IP Smart Home Controller) |

g) *Now consider all three path segments from sub-task e) and enter the required information for each path segment along with the TCP SYN payload in the solution field.  
| Src. IP: | Src. IP: | Src. IP: |
|----------|----------|----------|
| 10.0.0.1 | 10.0.2.1 | 10.0.2.1 |
| Src. Port: | Src. Port: | Src. Port: |
| 3608 | 3608 | 3608 |
| Dst. IP: | Dst. IP: | Dst. IP: |
| 10.0.1.1 | 10.0.1.1 | 10.0.1.1 |
| Dst. Port: | Dst. Port: | Dst. Port: |
| 80 | 80 | 80 |
| Laptop → R1 | R1 → R2 | R2 → Smart Home Controller |

h) *Out of curiosity, you activate IPv6 support on both routers and want to test if everything still works properly. Using the program Wireshark, you promptly capture the following hex dump of an IP packet that a device in your Smartnet has sent. Mark the different fields of the header.  
| Traffic Class | Payload Length | Hop Limit |  
|---------------|----------------|-----------|  
| Vers. | Flow Label | Next Header | Source ... |  
| 0x0000 | 60 | 04 | 02 | 14 | 00 | 2c | 06 | 40 | 20 | 01 | 0d | d8 | 00 | 00 | 00 | 00 |  
| ... Address | Destination ... |  
| 0x0010 | d3 | 78 | 66 | ff | fe | 8f | 2e | 41 | 20 | 01 | 4c | a0 | 20 | 01 | 00 | 13 |  
| ... Address |  
| 0x0020 | 02 | 50 | 56 | ff | fe | ba | 37 | ac |  

i) Using the information from sub-task h): Explain what the global /64 prefix assigned to your internet connection by your provider appears to be. Provide it in shortened notation.  
- The source address appears to be a globally unique address generated by SLAAC. This contains the global prefix. Generally, and in this case, it is a /64 network and can thus be derived from the first 64 bits of the source address:  
⇒ 2001:db8::/64  

j) Justify which device is most likely the sender of this packet.  
- Probably the toaster. Since it is a SLAAC-generated address, it contains the MAC address of the toaster in the suffix.  

### Task 3  
**Playing Sys-Admin for Your Own DNS Zone (8 Points)**  
You are the system administrator of a small company that has secured the domain grnvs.tips. Your task is now to fill out the following zone file so that the requirements of the individual sub-tasks are met. The beginning of the zone file is already given.  
```
$TTL 86400 ; 1 day  
grnvs.tips. IN SOA ns.grnvs.tips. (  
hostmaster.grnvs.tips.  
164160 ; serial  
1800 ; refresh (30 minutes)  
300 ; retry (5 minutes)  
604800 ; expire (1 week)  
1800 ; nxdomain (30 minutes)  
)  
NS ns.grnvs.tips.  
NS ns2.grnvs.tips.  
A 134.102.13.8  
AAAA 2001:db8::1  
$ORIGIN grnvs.tips.  
ns A 134.102.12.1  
ns2 A 134.102.12.2  
www A 134.102.13.8  
AAAA 2001:db8::1  
backend A 134.102.16.1  
AAAA 2001:db20::af  
$TTL 7200  
content CNAME ads.big-muscles.fit.  
```

a) *You have already set up two nameservers. These must still be entered in the zone file. The server with IP 134.102.12.1 should be the primary nameserver and 134.102.12.2 should act as fallback.  

b) *If someone calls grnvs.tips or www.grnvs.tips in their browser, the same web server should respond in both cases.  

c) *The backend programmers want their own subdomain for their server. This subdomain should be reachable at backend.grnvs.tips and already has the IPs 134.102.16.1 and 2001:db20::af.  

d) *You have signed a contract with big-muscles.fit and want to display their ad tracker on your page. To ensure that this does not immediately catch users' attention, the subdomain content.grnvs.tips should point to the domain ads.big-muscles.fit. However, since you do not trust the company very much, you want to reduce the maximum validity of this entry to 2 hours to be able to react quickly to changes.  

### Task 4  
**WEIRDER—Space Traffic Between Inter-Space Stations (21 Points)**  
After admiring the technologies from Space Patrol Orion, parts of the exercise management began to ponder this. In particular, the possibilities of text message transmission led to the question: What could go wrong when trying to implement this transmission using GRNVS methods? It is assumed that TCP and IPv4 will be used for the transmission of the messages. A variant of the Advanced Orbiting Systems (AOS) Space Data Link Protocol is used at Layer 2 – see Figure 4.1.  

| Field Length |  
|--------------|  
| Transfer Frame Primary Header 6–9 octets |  
| Operational Control Field 4 octets |  
| Frame Error Control Field 2 octets |  

**Table 4.1: PCI of the AOS Space Data Link Protocol**  

a) *What possibility does an application have to prevent data buffering by the TCP stack?  
- An application with this goal has the ability to set the TCP PSH flag.  

b) *When can preventing buffering by the TCP stack be sensible? (Justification!)  
- For example, in interactive applications, as buffering after input completion would otherwise lead to additional, unwanted transmission delays.  

c) *Why is it generally sensible for TCP to attempt to buffer data? (Justification!)  
- To maximize the ratio of payload to segment size, buffering is generally sensible. By buffering, the overhead caused by headers should be minimized as much as possible.  

d) *Determine the maximum length of a TCP header. (Justification!)  
- In this context, the TCP header field Data Offset (length: 4 bits; maximum value: 15) is relevant. This indicates the TCP header size in multiples of 32 bits. Thus, the maximum to be determined is: 60 B.  

e) *Provide the maximum size of an IPv4 header in bytes. (Justification!)  
- In this context, the IPv4 header field IHL (length: 4 bits; maximum value: 15) is relevant. This indicates the IPv4 header size in multiples of 32 bits. Thus, the maximum to be determined is: 60 B.  

f) *Determine the minimum ratio of Layer 4 SDU to Layer 2 PDU for a data-containing segment of an established TCP connection. (Justification!)  
- For Layer 4 SDU to be minimal, the Layer 4 SDU should contain as little as possible, and the Layer 2 PDU should be as large as possible. The Layer 4 SDU consists of the payload of a data-containing segment of an established TCP connection. This is at least 1 B in size. At the same time, the Layer 2 PDU contains the PCI of Layer 2 (here: AOS SDLP), 3 (here: IPv4), and 4 (here: TCP), as well as the above-described SDU from Layer 4. To maximize the Layer 2 PDU, the PDUs of Layers 2, 3, and 4 should be as large as possible. The maximum size of the PDUs is (9 B + 4 B + 2 B) + 60 B + 60 B = 135 B. Thus, the minimum ratio is: 135:1 ≈ 0.00735  

g) In RFC791 Section 3.2, the following statement can be found: "Every internet module must be able to forward a datagram of 68 octets without further fragmentation." (The word datagram describes a packet here.)  
*Justify the above statement of RFC791.  
- In the wording of the cited RFC791: "This is because an internet header may be up to 60 octets, and the minimum fragment is 8 octets."  

h) *Justify how many packets are maximally needed, assuming a minimal MTU, to transport a 61 B TCP SDU.  
- 61 B TCP Payload, 8 B per fragmented packet. The number of packets needed is therefore: 61 B / 8 B = 8.  

i) *What influence does setting the IPv4 header field DF have on the number of IPv4 packets arriving at the receiver? (Justification!)  
- DF (Don't Fragment) indicates that the IPv4 packet must not be fragmented. Fragmentation would, however, be necessary, as the packet is larger (see sub-task h)) than the link MTU specified in the task. Since it cannot be transmitted, the packet is discarded. Consequently, the number of received IPv4 packets is 0.  

j) *What challenge arises for calculating the ratio of Layer 4 SDU to Layer 2 PDU (as determined in sub-task f) when using IPv6?  
- There is no fixed upper limit for the total size of all IPv6 extension headers.  

k) Assuming the Layer 3 header can be estimated at 120 B. What follows from the cited RFC8200 passage for the number of transmitted IPv6 packets?  
- The packet size remains below the minimum link MTU, so it does not need to be fragmented. The number of IPv6 packets transmitted by the sender is therefore: 1.  

### Task 5  
**Data Network over Tin Cans (10 Points)**  
Given is the network depicted below consisting of tin cans 1 and 2, which are connected by a taut string.  
**Can 1** 10m **Can 2**  

Information is encoded in the form of the duration of a tone of a specific frequency:  
- A tone of 200 ms means a start bit  
- A tone of 100 ms means logical 1  
- A tone of 75 ms means logical 0  
- The individual tones are separated by 75 ms idle (no tone)  

The propagation delay of sound between the tin cans is assumed to be 2000 m/s.  

a) *Name the analog to the start bit in Ethernet. (No justification)  
- Prelude plus Start Frame Delimiter  

b) *Determine the propagation delay between the cans.  
- 10 m / 2000 m/s = 5 ms  

c) *From which technical aspect is the maximum achievable data rate dependent?  
- Only from the temporal resolution at the sender and receiver. The higher the resolution, the shorter the tones that can be used.  

d) *Determine the average achievable data rate in bits/s under the assumption that a redundancy-free data stream is to be sent.  
- The start bit does not count for longer transmissions.  
⇒ 1000 ms bit = 6.15 bit/s  

e) *Provide the binary representation of the string "GAD" (without quotes) to be transmitted. Mark the beginning and end of each codeword!  
- 01000111 01000001 01000100  
(ASCII has 7-bit codewords. Since the cheatsheet shows 8 bits, we will accept both variants.)  

f) *Determine the serialization time (including start bit) for this message.  
- 8·(100 ms + 75 ms) + 13·(75 ms + 75 ms) + 200 ms = 3.55 s  
With 8-bit codewords: 8·(100 ms + 75 ms) + 16·(75 ms + 75 ms) + 200 ms = 4.00 s  

g) *Justify whether full-duplex communication is possible under the given circumstances.  
- Yes, as long as different frequencies (which are not harmonics of each other) are used in both directions. (Frequency multiplex)  

### Task 6  
**Short Tasks (5 Points)**  
a) *For a path in the internet, you have determined an MTU of 1500 B. Provide a sensible MSS for TCP connections over IPv4. Assume that you do not use any TCP or IP options for the connection.  
- The MSS gives the payload without headers. Thus, the MSS is calculated as:  
MSS = MTU - IP Header - TCP Header = 1500 B - 20 B - 20 B = 1460 B  

b) *Explain why it is sensible to determine an MSS for TCP connections depending on the Layer 2 MTU and not to take an arbitrarily large value.  
- A sensible MSS should be chosen so that no potentially costly IP fragmentation for routers is necessary, but also the maximum amount of data can be transmitted.  

c) *Why is a call to connect() required when using TCP (as opposed to UDP) on Unix Sockets before data can be sent?  
- With TCP, in contrast to UDP, a connection must first be established before data can be sent.  

d) *You see several Layer 4 segments that A sends to B. Two of them are lost. Enter the correct sequence numbers that B confirms upon receiving each respective segment. The Go-Back-N method will be used.  
| A | B |  
|---|---|  
| SEQ=53 | SEQ=54 × |  
| ACK=54 | SEQ=55 |  
| SEQ=56 × |  
| ACK=54 | SEQ=54 |  
| SEQ=57 | ACK=55 |  
| ACK=55 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |