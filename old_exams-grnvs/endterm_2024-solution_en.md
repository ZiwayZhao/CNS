Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

### Personalization Notes:
- Your exam will be personalized during attendance control by affixing a code sticker.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID to be affixed next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Endterm  
Date: Monday, July 29, 2024  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 08:30–10:00  

### Instructions for Completion
- This exam comprises 16 pages with a total of 5 tasks as well as the known cheat sheet. Please check now that you have received a complete set of information.
- The total score for this exam is 90 points.
- The removal of pages from the exam is prohibited.
- The following aids are permitted:
  - A non-programmable calculator
  - An analog dictionary German ↔ native language without notes
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only such results will be evaluated where the solution path is recognizable. Text tasks must generally be justified unless otherwise expressly noted in the respective sub-tasks.
- Do not write with red/green colors or with pencil.
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.
- MC tasks are multiple choice/multiple answer, meaning at least one answer option is correct. Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 1 point for each correct and -1 point for each incorrect tick. Missing ticks have no effect. The minimum score per sub-task is 0 points.

---

### Task 1  
Multiple Choice (18 Points)  
Please tick the correct answers.  
- Ticks can be crossed out by completely filling them in.  
- Crossed-out answers can be ticked again by marking them next to it.

1. **(a)** By which operation(s) was the signal in Figure 1.1b generated from the signal in Figure 1.1a?  
   - Sampling  
   - Quantization  
   - Aliasing  
   - Anti-aliasing  
   - Channel coding  
   - Source coding  

2. **(b)** You modulate a signal with 1024-QAM. How many bits are transmitted per symbol?  
   - 21024  
   - 1  
   - 210  
   - 1000  
   - 10  
   - 1024  
   - 2  
   - 100  

3. **(c)** A frame with a total length of 1500B requires a serialization time of 12µs. What transmission rate does the link have?  
   - 125MB/s  
   - 1Mbit/s  
   - 125Mbit/s  
   - 1GB/s  
   - 2Gbit/s  
   - 1Gbit/s  

4. **(d)** A frame with a total length of 1500B is transmitted over a copper line of length 50km. What propagation delay occurs approximately?  
   - 250ns  
   - 250µs  
   - 166.67µs  
   - 2.38ms  
   - 166.67ns  
   - 2.38µs  

5. **(e)** Given the value 0x12345678 in Network Byte Order. What is the corresponding value in Little Endian?  
   - 0x34127856  
   - 0x78125623  
   - 0x87654321  
   - 0x78563412  
   - 0x56781234  
   - 0x12345678  

6. **(f)** A switch receives a frame for which the destination MAC address has no entry in the switching table. What happens?  
   - The switch waits until the information about the position of the receiver is known.  
   - The frame is sent back to the sender.  
   - The frame is forwarded to all other ports.  
   - The switch sends an ARP request with the corresponding destination MAC address.  
   - The frame is discarded.  

7. **(g)** How many broadcast domains does the adjacent network consist of?  
   - 2  
   - 6  
   - 5  
   - 4  
   - 1  
   - 3  
   - 7  

8. **(h)** How many collision domains does the adjacent network consist of?  
   - 1  
   - 4  
   - 6  
   - 2  
   - 5  
   - 7  
   - 3  

9. **(i)** Determine the network address for 10.32.43.45/22.  
   - 10.32.42.0  
   - 10.32.41.0  
   - 10.32.40.0  
   - Other  
   - 10.32.43.45  

10. **(j)** Which statements about NAT are correct?  
    - NAT replaces the source port of incoming packets.  
    - NAT replaces the source IP of outgoing packets.  
    - NAT can translate TCP ports into UDP ports.  
    - NAT replaces the destination port of outgoing packets.  
    - NAT replaces the destination IP of incoming packets.  
    - NAT replaces the destination IP of outgoing data packets.  
    - NAT provides a very high level of protection against unauthorized access.  
    - NAT replaces the source IP of incoming packets.  

11. **(k)** Why does TCP not work well on connections with high packet loss?  
    - TCP mistakenly assumes a network congestion and reduces the data rate too much.  
    - Too many bit errors occur that the CRC can no longer correct.  
    - The TCP flow control reduces the data rate to a realistically usable value.  
    - Data integrity can no longer be ensured because too many packets fail.  

12. **(l)** What is the reverse DNS FQDN that belongs to the IPv4 address 188.95.232.10?  
    - 10.232.95.188.in-addr.arpa.  
    - 10.232.95.188.ip6.arpa.  
    - 188.95.232.10.in-addr.arpa.  
    - 188.95.232.10.ip6.arpa.  
    - bc5f.e80a.in-addr.arpa.  
    - 0a.e8.5f.bc.ip6.arpa.  

13. **(m)** Why might it make sense to store multiple IPv4 addresses for the same domain in DNS?  
    - Note: Clients then receive a list of addresses instead of a single one during name resolution.  
    - To save resources, a server should serve multiple domains for higher availability.  
    - Higher availability in case a DNS server fails.  
    - A server has multiple interfaces and is reachable via different paths.  
    - Support for both IPv4 and IPv6.  
    - It makes no sense.  

14. **(n)** The authoritative nameserver for grnvs.net is ns.grnvs.net. Thus, the nameserver is in the same zone that it manages itself. An iterative resolver, however, needs the IP address of ns.grnvs.net to resolve any domain under grnvs.net. In a way, a deadlock. Why does DNS still work?  
    - The .net nameserver responds to the resolver with the nameserver ns.grnvs.net and attaches the IP address to the DNS response.  
    - It does not work. Nameservers must always lie outside the managed zone.  
    - The .net nameserver only sends the IP address of ns.grnvs.net to the resolver.  
    - The .net nameserver responds to the resolver with an IP address and informs it via glue records which domain is meant.  

---

### Task 2  
Roller Shutter Transmission (25.5 Points)  
The GRNVS tutors want to transmit messages between the student workroom and the GBS exercise leader room. The roller shutters of the rooms are to be used for transmission. Help the tutors with the individual steps of message transmission.

**Step A: Huffman Coding**  
In the first step, unnecessary redundancy should be removed from the data to be transmitted. The messages consist of characters from the alphabet A = {A, E, N, M, S, ?}, whose occurrence probabilities are listed in Table 2.1.

**Table 2.1: Occurrence probabilities of the characters of the alphabet A**  
| z ∈ A | Pr[X = z] |
|-------|-----------|
| E     | 0.4       |
| A     | 0.2       |
| N     | 0.16      |
| M     | 0.09      |
| S     | 0.08      |
| ?     | 0.07      |

1. **(a)** Construct the Huffman tree for alphabet A and note the corresponding probabilities and edge labels.  

2. **(b)** Encode the character sequence of the first message N "MENSA?" using the Huffman tree from part (a). Separate bit sequences that belong to different characters.  

3. **(c)** Name the name of this step in message transmission (no justification).  
   - Source coding  

---

**Step B: Baseband Signal**  
To transmit the bit sequence over the roller shutter, the basic impulse g(t) of length T is used, which is defined in Figure 2.1b.

**(a)** Draw the basic impulse g(t) in one of the templates in Figure 2.1. Clearly mark which version should be graded.  

**(b)** Determine the DC component of the basic impulse g(t) between -12T and 12T. Explain your approach.  
Note: No integration is necessary. The result can be read graphically.  

**(c)** The two slopes can be viewed from an area perspective as the drawn dashed orange lines at 1A. The plateau between -1T and 1T is already the perfect DC component for its part.  
When weighting, the individual parts are weighted according to their lengths, which corresponds to the average between 1 and 1 here. Thus, the DC component is 3A.  

---

**(f)** What is the modulation method whose signal space is depicted in Figure 2.2? Justify your answer briefly.  
   - 2-ASK (or 2-PSK)  
   - Since only in-phase components are present, it is amplitude modulation. Since there are two symbols, it is 2-ASK.  

**(g)** The GBS exercise leaders ask you to transmit the message N = 100111 over the roller shutter to the student workroom. Draw the position of the roller shutter over time for the transmission of the message N. Use the signal space assignment from Figure 2.2 and the basic impulse g(t).  

---

**(h)** Name the name of the step of message transmission from part (g) (without justification).  
   - Line coding  

---

**Step C: Cyclic Redundancy Check (CRC)**  
To detect transmission errors, we append M bits of checksum to every N bits of payload data. Assume that the payload data is selected independently and uniformly. The GRNVS tutors receive the response N = 100111 from the GBS exercise leader room. The message N contains payload data with an appended checksum, which was determined using CRC with reduction polynomial r(x) = x² + 1.

1. **(i)** Does the checksum fit for N with the actual message? Document your calculations and justify.  

2. **(j)** Calculate the entropy of source Q using the above checksum method with a 3-bit checksum per 5 bits of payload data. Explain your approach.  
Note: Interpret entire character groups as characters of a new alphabet AG.  
You can define a new alphabet AG = x + chksum(x) | x ∈ {0,1}⁵, which contains entire character groups as characters, and then normalize the entropy based on the number of characters per character group.  

---

### Task 3  
Routing (12 Points)  
Your fellow student has written a chat program himself. You now notice that the messages do not always arrive in the same order, although they were sent in the correct order.

1. **(a)** Which transport protocol was probably used here? Justify your answer.  
   - Since chat messages arrive partially in the wrong order, TCP cannot be used as the transport protocol under the above assumptions. Therefore, UDP must be used here.  

2. **(b)** With which transport protocol would this problem not occur? Justify your answer.  
   - To solve the problem, TCP can be used instead of UDP. Since TCP is a connection-oriented transport protocol, segments can be reassembled in the correct order using sequence numbers.  

3. **(c)** Your Internet Service Provider (ISP) has assigned your home router (Nr AT-Router) the IPv4 address 10.165.76.54 as well as the IPv6 prefix 2001:236:73:22::/64. You now want to offer a publicly accessible web server from your home network. Justify whether you can sensibly offer your service globally over IPv4, IPv6, or both protocols.  
   - Since the IPv4 address is not globally routable compared to the IPv6 prefix, you can only sensibly offer the service globally over IPv6 (your provider thus uses Dual Stack Lite).  

4. **(d)** Justify whether you must necessarily set up port forwarding.  
   - Port forwarding is not necessary, as the /64 prefix provides enough IPv6 addresses for your home network that are globally routable (under certain circumstances, you may still need to reconfigure the firewall on your home router, which, however, is not part of the question).  

---

**(e)** Given the network topology in part (e). You will find the routing tables of routers R1–R4 in Table 3.1. To present this more compactly, next-hop and interface have been replaced by the name of the next router or network, and transport networks have been omitted.  

1. **(f)** Draw the path of an IPv4 packet from computer PC1 to the destination IPv4 address 10.39.97.199 as far as possible into the network topology. Write in the box next to each router which entry is chosen in the context of LPM (Longest Prefix Matching) for this router.  

2. **(g)** Are there entries in the routing table of R1 (Figure 3.1a) that can be summarized? Justify your answer.  
   - Entries 3 and 5 in routing table 3.1a (Router R1) can be summarized. Entry 3 can simply be removed, as prefix 3 is in 5 and they have the same next hop.  

---

### Task 4  
Wireshark (17 Points)  
Given the Ethernet frame (without FCS) from Figure 4.1, which is to be analyzed below.

1. **(a)** Mark the sender address at Layer 2 in Figure 4.1 (without justification).  
2. **(b)** Mark the recipient address at Layer 2 in Figure 4.1 (without justification).  
3. **(c)** What type is the L3-PDU?  
   - Type: IPv6  
   - Justification: Ethertype 0x86dd  

4. **(d)** Provide the sender address at Layer 3 in its usual, possibly shortened form.  
   - 2a02:2455:189d:0:67b:cbff:fec1:806  

5. **(e)** Justify through which mechanism the sender address at Layer 3 was probably assigned.  
   - SLAAC, as the sender address contains the modified EUI-64 identifier generated from the sender MAC address.  

6. **(f)** Provide the recipient address at Layer 3 in its usual, possibly shortened form.  
   - 2a00:4700:0:9:f::b  

7. **(g)** What type is the L4-PDU?  
   - Type: TCP  
   - Justification: Next Header field in the IP header is 0x06  

8. **(h)** At what point in the frame does the L4-PDU begin?  
   - Offset: 0x0036  
   - Justification: Next Header = TCP → 40B IP Header / no Extension Header  

9. **(i)** What L7 protocol is it likely?  
   - Protocol: FTP  
   - Justification: TCP Destination Port 21  

10. **(j)** At what point in the frame does the L7-PDU begin?  
    - Offset: 0x004a  
    - Justification: Offset = 0x5 (4-bit field) → 20B TCP Header (with options)  

11. **(k)** Decode the L7 payload. Note: It is a text-based protocol (ASCII).  
    - 0x50, 0x41, 0x53, 0x56, 0x0d, 0x0a = PASV\r\n  

12. **(l)** What does this L7 payload cause on the server?  
    - The server will send the client the IP address and port number to establish a data channel.  

---

### Task 5  
Recordings (17.5 Points)  
You want to review the contents of the lecture again after hopefully passing the exam. For this, you use the lecture recordings. The lecture on TCP particularly caught your attention. The video is 512MiB in size. Your computer is currently connected to the Internet via Ethernet and IPv6. Access to the video should take place via HTTP 1.1. No options are used in the underlying TCP connection. The path MTU is 1500B.

1. **(a)** Which HTTP command (method) is used to load the video? (without justification)  
   - GET  

2. **(b)** You then receive the following HTTP response, which contains some metadata in addition to the data. It is partially shown in Figure 5.1.  
   - HTTP/1.1 200 OK  
   - Content-Length: 512 MiB = 512 · 2^20 B = 536870912 (B)  

3. **(c)** What other information can the response contain? Name two examples (without justification).  
   - Server, Content-Type, Date, ...  

4. **(d)** Show that the maximum segment size, so that fragmentation does not have to occur, is 1440B in this scenario.  
   - MTU - |IPv6-PCI| - |TCP-PCI|  
   - 1500B - 40B - 20B = 1440B  

5. **(e)** Assume that the HTTP request is 100 bytes in size. The first segment after the HTTP request contains only the HTTP metadata of the HTTP response, which is 500 bytes in size. Only the subsequent segments contain the requested data. The size of the other segments is chosen to be maximally large. Segments are confirmed as soon as possible.  

6. **(f)** Complete the details of the TCP handshake. Assume that no payload data is transmitted during the handshake.  
   - SEQ=1234, SYN  
   - SEQ=5678, SYN, ACK=1235  
   - SEQ=1235, ACK=5679  

7. **(g)** Complete the missing details for the communication after the handshake and fill in the missing arrow directions. Also, mark in the additional box of the corresponding lines the segments with an HTTP request with REQ, segments with an HTTP response with RES, and segments with the data with D.  

8. **(h)** How many segments with the requested data will the server send in total? Provide the calculation.  
   - 536870912B / 1440B = 372828  

9. **(i)** The video transmission has now started. We assume that the simplified congestion control mechanism of TCP Reno, as presented in the lecture, is used, and we are in the Congestion Avoidance (CA) phase. We assume that the bandwidth of the connection allows for 17 MSS/RTT and that no router on the way to the server has a buffer.  
   - What happens when the send window w grows above 17 MSS?  
   - There will be packet loss due to the overload situation. There will be duplicated ACKs.  

10. **(j)** How will the congestion control react to this?  
    - w is halved, CA again.  

11. **(k)** What effective throughput (in MSS/RTT) does the transmission achieve?  
    - (9+10+11+12+13+14+15+16+17) MSS = 13.4 MSS/RTT  

12. **(l)** Assuming your computer is very weak and is overloaded by the incoming segments. How can this be avoided? Name the mechanism and briefly describe how it works.  
    - Flow control  
    - The receiver communicates the size of its receive window w.  
    - The sender then adjusts its send window accordingly.  

---

### Additional Space for Solutions  
Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.