Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

### Personalization Notes:
- Your exam will be analyzed by attaching a code persona sticker during attendance control.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID to be pasted here next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Endterm  
Date: Monday, July 29, 2024  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 08:30–10:00  

### Instructions for Completion
- This exam consists of 16 pages with a total of 5 tasks as well as the known cheatsheet. Please check now that you have received a complete set of information.
- The total score for this exam is 90 points.
- The removal of pages from the exam is prohibited.
- The following aids are permitted:
  - A non-programmable calculator
  - An analog dictionary German ↔ native language without annotations
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write with red/green colors or with pencil.
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.
- MC tasks are Multiple Choice/Multiple Answer, i.e., at least one answer option is correct. Sub-tasks with only one correct answer will be graded with 1 point if correct. Sub-tasks with more than one correct answer will be graded with 1 point for each correct and -1 point for each incorrect selection. Missing selections have no effect. The minimum score per sub-task is 0 points.

### Task 1  
Multiple Choice (18 points)  
×  
Please mark the correct answers.  
■  
Marked answers can be crossed out by completing the filling.  
×■  
Crossed-out answers can be marked again by adjacent markings.  

1 1  
0.5 0.5  
0 0  
−0.5 −0.5  
0 1 2 3 4 0 1 2 3 4  
(a) (b)  

**Figure 1.1**  
a)* Which operation(s) generated the signal in Figure 1.1b from the signal in Figure 1.1a?  
Sampling Quantization Aliasing  
Anti-aliasing Channel coding Source coding  

b)* You are modulating a signal with 1024-QAM. How many bits are transmitted per symbol?  
21024 1 210 1000  
10 1024 2 100  

c)* A frame with a total length of 1500B requires a serialization time of 12µs. What is the transmission rate of the link?  
125MB/s 1Mbit/s 125Mbit/s 1GB/s 2Gbit/s 1Gbit/s  

d)* A frame with a total length of 1500B is transmitted over a copper line of length 50km. What propagation delay occurs approximately?  
250ns 250µs 166.67µs 2.38ms 166.67ns 2.38µs  

e)* Given the value 0x12345678 in Network Byte Order. What is the corresponding value in Little Endian?  
0x34127856 0x78125623 0x87654321  
0x78563412 0x56781234 0x12345678  

f)* A switch received a frame for which the destination MAC address has no entry in the switching table. What happens?  
The switch waits until the information about the position of the receiver is known.  
The frame is sent back to the sender.  
The frame is forwarded to all other ports.  
The switch sends an ARP request with the corresponding destination MAC address.  
The frame is discarded.  

g)* How many broadcast domains does the adjacent network consist of?  
2 6 5 4 1 3 7  

h)* How many collision domains does the adjacent network consist of?  
1 4 6 2 5 7 3  

i)* Determine the network address for 10.32.43.45/22.  
10.32.42.0 10.32.41.0 10.32.40.0 other 10.32.43.45 address  

j)* Which statements about NAT are correct?  
NAT replaces the source port of incoming packets.  
NAT replaces the source IP of outgoing packets.  
NAT can translate TCP ports into UDP ports.  
NAT replaces the destination port of outgoing packets.  
NAT replaces the destination IP of incoming packets.  
NAT replaces the destination IP of outgoing data packets.  
NAT provides a very high level of protection against unauthorized access.  
NAT replaces the source IP of incoming packets.  

k)* Why does TCP not work well on connections with high packet loss?  
TCP mistakenly assumes there is network congestion and reduces the data rate too much.  
Too many bit errors occur that CRC can no longer correct.  
The TCP flow control reduces the data rate to a realistically usable value.  
Data integrity can no longer be ensured because too many packets are missing.  

l)* What is the reverse DNS FQDN that corresponds to the IPv4 address 188.95.232.10?  
10.232.95.188.in-addr.arpa. 10.232.95.188.ip6.arpa.  
188.95.232.10.in-addr.arpa. 188.95.232.10.ip6.arpa.  
bc5f.e80a.in-addr.arpa. 0a.e8.5f.bc.ip6.arpa.  

m)* Why might it make sense to store multiple IPv4 addresses for the same domain in DNS?  
Note: Clients then receive a list of addresses instead of a single one during name resolution.  
To save resources, a server should provide higher availability by serving multiple domains.  
Higher availability if its DNS server fails.  
A server has multiple interfaces and is reachable via different paths.  
Support for both IPv4 and IPv6.  
It makes no sense.  

n)* The authoritative nameserver for grnvs.net is ns.grnvs.net. Thus, the nameserver is in the same zone that it manages itself. An iterative resolver, however, needs the IP address of ns.grnvs.net to resolve any domain under grnvs.net. In a way, a deadlock. Why does DNS still work?  
The .net nameserver responds to the resolver with the nameserver ns.grnvs.net and attaches the IP address to the DNS response.  
It does not work. Nameservers must always lie outside the managed zone.  
The .net nameserver only sends the IP address of ns.grnvs.net to the resolver.  
The .net nameserver responds to the resolver with an IP address and informs it via glue records which domain is meant.  

### Task 2  
Roller Shutter Transmission (25.5 points)  
The GRNVS tutors want to transmit messages between the student workspace and the GBS exercise room. The roller shutters of the rooms are to be used for transmission. Help the tutors with the individual steps of message transmission.  

**Step A: Huffman Coding**  
In the first step, unnecessary redundancy should be removed from the data to be transmitted. The messages consist of characters from the alphabet A={A, E, N, M, S, ?}, whose occurrence probabilities are listed in Table 2.1.  

**Table 2.1: Occurrence probabilities of the characters from the alphabet A**  
z ∈ A | Pr[X = z]  
--- | ---  
E | 0.4  
A | 0.2  
N | 0.16  
M | 0.09  
S | 0.08  
? | 0.07  

a)* Construct the Huffman tree for alphabet A and note the corresponding probabilities and edge labels.  

b) Encode the character string of the first message N "MENSA?" using the Huffman tree from sub-task a). Separate bit sequences that belong to different characters.  

c)* Name this step of message transmission (no justification).  

**Step B: Baseband Signal**  
To transmit the bit sequence over the roller shutter, the basic pulse g(t) of length T is used, which is defined in Figure 2.1b.  

g(t)  
A  
{  
4At + 2A, −1T ≤ t < −1T  
−AT, −T ≤ t < 1T  
0, otherwise  
}  

**Figure 2.1: Templates for the drawing of the basic pulse**  

d)* Draw the basic pulse g(t) in one of the templates in Figure 2.1. Clearly mark which version should be graded.  

e)* Determine the DC component of the basic pulse g(t) between −12T and 12T. Explain your approach.  
Note: No integration is necessary. The result can be read graphically.  

f)* What is the modulation method whose signal space is depicted in Figure 2.2? Justify your answer briefly.  

g) Let A = 1, i.e., at a level of -1 the roller shutter is fully down, at 1 fully up. The GBS exercise leader asks you to transmit the message N = 100111 over the roller shutter to the student workspace.  

h) Draw the position of the roller shutter over time for the transmission of message N. Use the signal space mapping from Figure 2.2 and the basic pulse g(t).  

i)* If you used both templates, indicate which template should be graded.  

j)* Name the step of message transmission from sub-task g) (without justification).  

**Step C: Cyclic Redundancy Check (CRC)**  
To detect transmission errors, we append M bits of checksum to each N bits of payload data. Assume that the payload data is selected independently and uniformly. The GRNVS tutors receive the response N = 100111 from the GBS exercise room. The message N contains payload data with an attached checksum, which was determined using CRC with reduction polynomial r(x) = x² + 1.  

i)* Does the checksum match the actual message for N? Document your calculations and justify.  

A sample sequence of characters from a source Q (checksum characters in bold) with 3 bits of checksum for every 5 bits of payload data is as follows: 00110101 11010110 00001000 ...  

j)* Calculate the entropy of source Q using the above checksum method with 3 bits of checksum for every 5 bits of payload data. Explain your approach.  
Note: Interpret entire character groups as characters of a new alphabet AG.  

### Task 3  
Routing (12 points)  
Your fellow student has written a chat program. They now notice that the messages do not always arrive in the same order, even though they were sent in the correct order.  

a)* Which transport protocol was likely used here? Justify your answer.  

b) With which transport protocol would this problem not occur? Justify your answer.  

Your Internet Service Provider (ISP) has assigned your home router (NAT router) the IPv4 address 10.165.76.54 and the IPv6 prefix 2001:236:73:22::/64. You want to offer a publicly accessible web server from your home network.  

c)* Justify whether you can sensibly offer your service globally over IPv4, IPv6, or both protocols.  

d)* Justify whether you must set up port forwarding.  

**(a) R1 (b) R2**  
Entry | Destination | Next-Hop  
--- | --- | ---  
1 | 10.48.0.0/14 | N  
2 | 10.52.0.0/14 | PC1  
3 | 10.128.0.0/10 | R2  
4 | 10.192.0.0/10 | R3  
5 | 10.0.0.0/8 | R2  

**(c) R3 (d) R4**  
Entry | Destination | Next-Hop  
--- | --- | ---  
α | 10.56.0.0/13 | R4  
β | 10.32.0.0/12 | N  
γ | 10.192.0.0/10 | N  
δ | 10.128.0.0/10 | R4  
ϵ | 10.0.0.0/9 | R2  

**Table 3.1: Routing Tables**  

e)* Draw the path of an IPv4 packet from computer PC1 to the destination IPv4 address 10.39.97.199 as far as possible into the network topology. Write in the box next to each router which entry will be chosen within the framework of LPM (Longest Prefix Matching) for that router.  

f)* Are there entries in the routing table of R1 (Figure 3.1a) that can be summarized? Justify.  

### Task 4  
Wireshark (17 points)  
Given is an Ethernet frame (without FCS) from Figure 4.1, which is to be analyzed below.  

0x0000 3c a6 2f 78 3b 96 04 7b cb c1 08 06 86 dd 60 05  
0x0010 b0 03 00 1a 06 40 2a 02 24 55 18 9d 00 00 06 7b  
0x0020 cb ff fe c1 08 06 2a 00 47 00 00 00 00 09 00 0f  
0x0030 00 00 00 00 00 0b c6 cc 00 15 ec f6 4d b5 dc 28  
0x0040 38 2f 50 18 7f a9 f8 30 00 00 50 41 53 56 0d 0a  

**Figure 4.1: Ethernet Frame (without FCS)**  

Note that justifications are required for the following sub-tasks. Ensure that markings can be uniquely assigned to individual sub-tasks. Non-verifiable statements will not be graded.  

a)* Mark the sender address at Layer 2 in Figure 4.1 (without justification).  

b)* Mark the recipient address at Layer 2 in Figure 4.1 (without justification).  

c)* What type is the L3-PDU?  
Type: Justification:  

d)* Provide the sender address at Layer 3 in its usual, possibly shortened form.  

e)* Justify by which mechanism the sender address at Layer 3 was likely assigned.  

f)* Provide the recipient address at Layer 3 in its usual, possibly shortened form.  

g)* What type is the L4-PDU?  
Type: Justification:  

h)* At what point in the frame does the L4-PDU begin?  
Offset: Justification:  

i)* What L7 protocol is likely involved?  
Protocol: Justification:  

j)* At what point in the frame does the L7-PDU begin?  
Offset: Justification:  

k)* Decode the L7 payload. Note: It is a text-based protocol (ASCII).  

l)* What effect does this L7 payload have on the server?  

### Task 5  
Records (17.5 points)  
You want to review the contents of the lecture again, despite hopefully passing the exam, after some time. For this, you will use the lecture recordings. The lecture on TCP particularly caught your attention. The video is 512MiB in size. Your computer is currently connected to the Internet via Ethernet and IPv6. Access to the video should occur via HTTP 1.1. No options are used in the underlying TCP connection. The path MTU is 1500B.  

First, we take a look at the Application Layer.  

a)* Which HTTP command (method) is used to load the video? (without justification)  

You then receive the subsequent HTTP response, which contains some metadata in addition to the data. It is partially shown in Figure 5.1.  
HTTP/1.1 1\r\n  
...  
Content-Length: 2\r\n  
...  
<data>  

**Figure 5.1: Parts of the HTTP Response**  

b)* Complete the missing fields of the response in Figure 5.1. Note that the Content-Length is given in bytes.  

c)* What other information can the response contain? Name two examples (without justification).  

Now we consider the corresponding TCP connection and the transmission of the segments.  

d)* Show that the maximum segment size, so that fragmentation does not have to occur, is 1440B in this scenario.  

Assume that the HTTP request is 100 bytes in size. The first segment after the HTTP request contains only the HTTP metadata of the HTTP response, which is 500 bytes in size. Only the subsequent segments contain the requested data. The size of the other segments is maximally chosen. Segments are acknowledged as soon as possible.  

e)* Complete the information about the TCP handshake. Assume that no payload data is transmitted during the handshake.  
SEQ=1234, SYN  
SEQ=5678, SYN, ACK=  
SEQ= , ACK=  

f)* Complete the missing information for the communication after the handshake and add the missing arrow directions. Also mark segments with an HTTP request with REQ, segments with an HTTP response with RES, and segments with data with D in the additional box of the respective lines.  

g)* How many segments with the requested data will the server send in total? Provide the calculation path.  

The video transmission has now started. We assume that the simplified congestion control mechanism of TCP Reno, as presented in the lecture, is used, and we are in the Congestion Avoidance (CA) phase. We assume that the bandwidth of the connection allows for 17 MSS/RTT and no router on the way to the server has a buffer.  

h)* What happens when the send window w grows beyond 17 MSS?  

i)* How will congestion control react to this?  

j)* What effective throughput (in MSS/RTT) does the transmission achieve?  

k)* Assume your computer is very weak and is overloaded by the incoming segments. How can this be avoided? Name the mechanism and briefly describe how it works.  

### Additional space for solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to cross out invalid solutions.