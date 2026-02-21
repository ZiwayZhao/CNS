Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized during the attendance check by affixing a code sticker.  
- This contains only a sequential number, which is also noted on the attendance sticker with SRID here.  
- This will be used as a pseudonym to allow a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Retake  
Date: Thursday, October 5, 2023  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 17:00–18:30  

Before we proceed with reading the instructions for processing, please answer the following questions. With this information, you help us examine the learning success depending on individual components of the lecture. The information is voluntary and does not flow into the evaluation. To exclude any influence, this page will not be accessible during the correction.  

a) Did you attend the lecture?  
1 (regularly) 2 3 4 (never)  

b) Did you watch the recording from last year?  
1 (regularly) 2 3 4 (never)  

c) Did you attend the tutorial exercises?  
1 (regularly) 2 3 4 (never)  

d) Did you participate in the review session?  
1 (regularly) 2 3 4 (never)  

e) Did you participate in the live programming (TCP UDP Chat)?  
Yes (both dates) At one date No  

**Instructions for Processing**  
- This exam consists of 16 pages with a total of 6 tasks. Please check now that you have received a complete set of information.  
- The total score for this exam is 90 points.  
- It is prohibited to tear out pages from the exam.  
- The following aids are allowed:  
  - a non-programmable calculator  
  - an analog dictionary in the native language without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be evaluated where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  
- Turn off all electronic devices you carry, store them in your bag, and close it.  

**Task 1**  
Multiple Choice (18 points)  
The following tasks are Multiple Choice/Multiple Answer, meaning at least one answer option is correct. Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 1 point for each correct and -1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

Please mark the correct answers.  
Marks can be crossed out by completely filling them in.  
Crossed-out answers can be re-marked by adjacent markings.  

a) *How many broadcast domains does the adjacent network consist of?  
3 6 1 5 2 4  

b) *How many collision domains does the adjacent network consist of?  
4 2 3 1 6 5  

c) *Given the following character stream:  
YAFFKAFPUAoYYUKAUPK  
Which character has the highest information content?  
P K F A Y U  

d) *A source emits characters from the alphabet = “a”. What is the entropy of the source?  
∞ other value 1 0 2  

e) *Which statement(s) about Huffman codes are correct?  
Frequently occurring characters are represented with shorter code words.  
It is a lossless compression method.  
Huffman codes always produce shorter code words than a uniform code.  
If all characters occur with equal probability, the shortest average code word length is achieved.  
All code words have the same length.  

f) *A packet of length 1500B is transmitted over a channel with (independent) bit error probability p = 10^-4. Determine the probability that the packet is transmitted error-free.  
86.07% 0.01% 30.12% 99.99% other value  

g) *What modulation method does the adjacent signal space assignment represent?  
3-PSK 4-QAM 2-ASK 8-PSK 8-ASK  

h) *Given the number z = 123456 in decimal representation. 0x01e240 is the hexadecimal representation of z in:  
Network- Wireless- Big- Little- Internet- Wired-  
Byte- Byte- Endian Endian Byte- Byte-  

i) *What property(ies) does IPv6 have compared to IPv4?  
No DNS needed. Hop count in seconds. Fragmentation also possible in routers.  
Improved line coding. Fixed header size. 128 times larger address space.  

j) *Given a baseband signal with 4 distinguishable symbols and a transmission channel with a bandwidth of 1MHz and an SNR of 15. Determine the achievable data rate(s).  
0.125MB/s 0.5MB/s 15.00Mbit/s 3.125MB/s 4.00Mbit/s 3.33Mbit/s other value 2.00Mbit/s 3.75Mbit/s  

k) *What is the essential difference(s) between CSMA/CD and CSMA/CA?  
CSMA/CD uses acknowledgments, while CSMA/CA does not.  
There are only differences in collision handling, not in media access.  
CSMA/CA requires a minimum frame length of 64B.  

l) *Which feature(s) does an analog signal have?  
time continuous value continuous time discrete value discrete  

m) *Which of the following IP addresses will not be globally routed?  
128.128.128.128 2001:1.0.13 fec0::1 2001::abcd:1  
feb0::1 192.169.24.25 192.192.1.1 127.255.1.2  

**Task 2**  
Wireshark (17 points)  
Given are the first 96 bytes of the Ethernet frame from Figure 2.1, which will be analyzed below.  

```
0x0000 90 e2 ba 2a 8d 97 90 e2 ba 08 00 45 86 dd 60 04  
0x0010 1a 84 01 a3 06 40 20 01 0d b8 00 00 00 00 92 eg2  
0x0020 ba ff fe 08 00 45 2a 00 47 00 00 00 00 09 00 0f  
0x0030 00 00 00 00 00 00 c8 30 00 50 2e e7 4a d0 f5 17  
0x0040 f1 8d 80 18 08 00 ea 9a 00 00 01 01 08 0a 68 9b  
0x0050 63 a0 34 86 78 2e 47 45 54 20 2f 20 48 54 54 50  
```

**Figure 2.1: Snippet of an Ethernet frame**  
Note that for subsequent parts, justifications are required. Ensure that markings can be uniquely assigned to individual sub-tasks. Non-verifiable statements will not be evaluated.  

a) *Mark the sender address at layer 2 in Figure 2.1. (without justification)  

b) *Mark the recipient address at layer 2 in Figure 2.1. (without justification)  

c) *What type is the L3-PDU?  
Type: IPv6 Justification: Ethertype 0x86dd  

d) Provide the sender address at layer 3 in its usual and possibly shortened notation.  
2001:db8::92e2:baff:fe08:45  

e) Through which mechanism was the sender address at layer 3 presumably assigned?  
SLAAC, as the sender address contains the modified EUI-64 identifier generated from the sender MAC address.  

f) Provide the recipient address at layer 3 in its usual and possibly shortened notation.  
2a00:4700:0:9:f::  

g) What type is the L4-PDU?  
Type: TCP Justification: Next Header field in the IP header is 0x06  

h) At what point does the L4-PDU begin?  
Offset: 0x0036 Justification: Next Header = TCP ⇒ 40B IP Header/no Extension Header  

i) What L7 protocol is it likely?  
Protocol: HTTP Justification: TCP Destination Port 80  

j) At what point does the L7-PDU begin?  
Offset: 0x0056 Justification: Offset = 0x8 32B TCP Header (with options)  

k) Calculate the length of the L7-PDU in bytes.  
Payload length field in IP Header = 0x01a3 419B L3-SDU  
TCP Header length (including options) 32B  
L7-PDU = 419B - 32B = 387B  

The observed packet was transmitted in the topology shown in Figure 2.2 from PC to SRV. In this figure, the position is also marked where the packet was recorded.  

**Figure 2.2: Network topology**  

l) Assign the MAC addresses and IP addresses determinable from the recorded packet to the corresponding interfaces from Figure 2.2 (e.g., R3.eth3.MAC = ...). Provide only addresses that can be uniquely assigned.  
PC.eth0.MAC = 90:e2:ba:08:00:45  
R1.eth0.MAC = 90:e2:ba:2a:8d:97  
PC.eth0.IP = 2001:db8::92e2:baff:fe08:45  
SRV.eth0.IP = 2a00:4700:0:9:f::  

**Task 3**  
Deceptive Name Resolution (13 points)  
As a network expert, you want to test the speed and accuracy of a Large Language Model (LLM) using an example. You ask the LLM the following input:  
Explain how the DNS resolution of an IPv4 address looks for the FQDN "cit.tum.de." from a PC with a resolver in the local network. The resolution should be performed according to the lecture. In your explanation, provide the label AND the RR Type for each query and answer. Indicate for each query whether it is iterative or recursive.  

You then receive the following output:  
The DNS resolution for the FQDN "cit.tum.de." from a PC in a local network can proceed as follows:  

1. The PC in the local network sends a DNS query to obtain the IP address for the FQDN "cit.tum.de." The PC starts the DNS resolution with a recursive query.  
Query: cit.tum.de. IN A  

2. The local DNS resolver in the local network receives the request from the PC and checks its cache for already available information about "cit.tum.de." If the cache contains a corresponding entry, the resolution is completed, and the answer is sent back to the PC. If no information is available in the cache, the local DNS resolver must perform the resolution from scratch.  

3. The local DNS resolver is not authoritative for "tum.de." and does not have direct information about "cit.tum.de.". Therefore, it sends a recursive request to a root DNS server to obtain the IP address of the authoritative server for the top-level domain (TLD) "de.".  
Query: . IN NS  

4. The root DNS server responds with information about the nameserver for the TLD "de.".  
Answer: . IN NS a.nic.de.  

5. The local DNS resolver now sends a recursive request to the nameserver for the TLD "de." and asks for the nameserver for "tum.de.".  
Query: de. IN A  

6. The authoritative server for the TLD "de." responds with information about the nameserver for "tum.de.".  
Answer: de. IN NS  

7. The local DNS resolver sends a request to the nameserver for "tum.de." and asks for the IP address for "cit.tum.de.".  
Query: cit.tum.de. IN A  

8. The nameserver for "tum.de." responds with the IP address for "cit.tum.de.".  
Answer: cit.tum.de. IN A <IPv4 Address>  

9. The local DNS resolver receives the answer from the nameserver for "tum.de." and stores it in the cache for future requests. The local DNS resolver sends the answer back to the PC.  

10. The PC in the local network receives the IP address for "cit.tum.de." and can now establish the desired connection to this address.  

In this process, the queries for DNS resolution are performed recursively. The resource types are indicated by the designation "A" for the IP address and "NS" for the nameserver. It should be noted that this example shows the full DNS resolution and that in practice caching and other optimizations are used to improve performance.  

a) Since you are familiar with DNS, identify a series of errors. List all errors and missing information in the table, along with the appropriate correction.  
Please note the following hints:  
- Not every step contains an error.  
- Some steps contain multiple errors.  
- Errors that occur in multiple steps should be written separately for each step.  
- Not all rows of the table will be needed.  
- It is sufficient to list 10 errors, but there are more.  

| Step | Error | Correction/Addition |
|------|-------|---------------------|
| 3 | recursive | iterative |
| 3 | Authoritative nameserver | (Authoritative) nameserver |
| 3 | Query: . IN NS | Query: cit.tum.de. IN A |
| 3 | Query: . IN NS | Query: cit.tum.de. IN A |
| 3 | the authoritative server for the TLD "de" of "cit.tum.de." | |
| 4 | Query: . IN NS a.nic.de. | Query: de. IN NS a.nic.de. |
| 4 | missing Glue Record | in addition to the NS record, an A record for NS is provided |
| 5 | recursive | iterative |
| 5 | asks for the nameserver for "tum.de" | asks for the IP address for "cit.tum.de." |
| 5 | Query: de. IN A | Query: cit.tum.de. IN A |

b) Given the following AAAA entry:  
server1.example.com. IN AAAA 2001:db8::567:89ab  
Provide the corresponding PTR entry.  
b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa.  
IN PTR server1.example.com.  

**Task 4**  
Frequency Analysis (17 points)  
Given is the basic impulse g(t) = 1 for 1/2 ≤ t < 1/2, which is repeated periodically at intervals of T = 2µs. This gives the periodic signal s(t).  

a) *Draw the periodic signal s(t) in Figure 4.1.  

**Figure 4.1: Periodic signal s(t)**  

b) *Determine the angular frequency ω of the signal.  
ω = 2π/T = π  

c) *Justify whether a Fourier series can be used to determine the spectrum of s(t).  
Yes, since s(t) is periodic, it can be represented as a weighted sum of sin and cos.  

d) *Determine the DC component of s(t). Simplify the result as much as possible.  
a = (1/T) ∫ s(t) dt from 0 to T  
= (1/2) ∫ (1) dt from 0 to 1  
= 1/2  

e) *Determine the spectrum of s(t). Simplify the result as much as possible.  
Hints:  
1. Use symmetries.  
2. ∫ x sin(cx) dx = (1/c^2)(cx cos(cx) - sin(cx)), ∫ x cos(cx) dx = (1/c^2)(sin(cx) + cx sin(cx)).  
3. No case distinction is required at the end of the calculation.  
4. Since g(t) is neither point-symmetric nor axis-symmetric, both ak and bk are generally non-zero. With the angular frequency ω = 2π/T, we get:  

ak = ∫ (t + cos(kπt)) dt from -1/2 to 1/2  
= sin(kπt) + (kπt sin(kπt) + cos(kπt))/(2kπ)  

The sine components bk are determined as follows:  
bk = ∫ (t + sin(kπt)) dt from -1/2 to 1/2  
= sin(kπt) + (t sin(kπt))/(2)  

**Task 5**  
Networks (18 points)  
We consider a typical scenario where a PC in the home network is connected to the Internet via a NAT-capable Router A, as shown in Figure 5.1. We assume that the entire network is based on IPv4.  

**Figure 5.1: Network**  

First, we take a closer look at the "Internet" section: The routers are each gateway routers represented as clouds. The various routers determine their routing tables based on an optimal dynamic routing protocol. The costs are indicated on the respective edges.  

a) *Provide the resulting routing table for Router A. You may use the respective lowercase letters of the reachable networks (represented as clouds) for the IP prefixes, and the router name (as uppercase letter) for the IP address of the router. For example, the IP prefix z is reachable via Router Z, while Router Z itself has the IP address Z in the respective transport networks. Note: Not all table rows are needed.  

| Destination | Next Hop | Iface |
|-------------|----------|-------|
| b           | B        | wan0  |
| c           | C        | wan1  |
| d           | C        | wan1  |
| e           | C        | wan1  |
| a           | -        | eth0  |

Next, we assume that all caches are initially empty. The IP address of the gateway router A and the grnvs.net server are known.  
PC1 wants to access the website behind grnvs.net and wants to send a GET request via HTTPS.  

b) *What additional information is needed to address the frame?  
MAC address of A  

c) *Through which protocol can this information be obtained?  
ARP  

d) *What is the recipient MAC address of the first sent frame?  
Broadcast Address: ff:ff:ff:ff:ff:ff  

e) *Before the actual request can be sent, handshakes must be performed. For which protocols?  
TCP and TLS  

Now we consider the sending of the first packet (the first handshake).  

f) *Draw all exchanged frames on the path between PC1 and the server that are exchanged before and during the first packet between the nodes. You may abbreviate the actual IP packet with Payload as P. Note: You will find a further template at the end of the exam.  

| PC1 | SW1 | A | B | C | D | E | G |
|-----|-----|---|---|---|---|---|---|
| (1) ARP Request |   |   |   |   |   |   |   |
| (2) ARP Reply |   |   |   |   |   |   |   |
| (3) IP Packet |   |   |   |   |   |   |   |

g) *For this first packet, provide the corresponding values of the header fields at points I to III in the table below. You may use the names of the respective nodes for the IP addresses. Choose sensible values for freely selectable entries. Also, note and complete the NAT table of Router A.  

| P | L3-Src | L3-Dst | L4-Src | L4-Dst | TTL |
|---|--------|--------|--------|--------|-----|
| I | PC1    | GRNVS  | 1234   | 443    | 64  |
| II | PC1   | GRNVS  | 1234   | 443    | 64  |
| III | A.wan1/NAT | GRNVS | 1235 | 443 | 61 |

**NAT Table of A:**  
| Local IP | Local Port | Global Port | Protocol |
|----------|------------|-------------|----------|
| PC1      | 8080       | 1234        | TCP      |
| PC1      | 1234       | 1235        | TCP      |

h) *Assuming there is a problem on the path to the server and an ICMP "Packet too big" message would be sent back to the sender. Justify whether this would arrive.  
The ICMP message contains the first 8 bytes of the payload. The TCP ports are included in it. The NAT router can accordingly forward the message.  

**Task 6**  
Video Transmission (7 points)  
You want to watch a large eSports event on a major streaming portal. Your connection runs over IPv4 and has a bitrate of 200Mbit/s. You notice (e.g., with traceroute) that there are 5 additional hops/routers between your computer and the server. The path to the server is a total of 7000 km long. The MTU is 1500B.  

a) *What is the maximum size of an Ethernet frame?  
1500B + 18B (Ethernet Header) = 1518B  

You are a bit late, but first watch the live stream of the current event. The stream is transmitted via UDP over IPv4.  

b) What latency does the transmission occur with? Provide the calculation path. Provide the final result in ms and round to 2 decimal places.  
Delay of the first packet:  
t = 6 + (1518B / (200Mbit/s)) + (7000km / (2/v))  
≈ 35.56 ms  

c) How many frames must the film be divided into? Provide the calculation path.  
⌈ 400MB / (1500 - 20 - 8)B ⌉ = 271740  

d) How much time passes until the transmission is completed? Provide the calculation path and round the result to 2 decimal places.  
Delay of the last packet:  
t = (271740 + 6) * (1518B / (200Mbit/s))  
≈ 16.53 s  

**Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.**