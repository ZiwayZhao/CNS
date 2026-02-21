Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

### Personalization Notes:
- Your exam will be identified during the attendance check by attaching a code sticker.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID to be attached next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Basics of Computer Networks and Distributed Systems  
Exam: IN0010/Retake  
Date: Thursday, October 5, 2023  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 17:00–18:30  

Before we proceed with reading the processing instructions, please answer the following questions. With this information, you help us investigate the learning success depending on individual lecture components. The information is voluntary and does not affect the grading. To exclude any influence, this page will not be accessible during correction.

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

### Processing Instructions
- This exam consists of 16 pages with a total of 6 tasks.  
Please check now that you have received a complete set of instructions.  
- The total score for this exam is 90 points.  
- Cutting pages from the exam is prohibited.  
- Allowed aids:  
  - a non-programmable calculator  
  - an analog dictionary (German native language) without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results are counted where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write in red/green colors or with pencil.  
- Turn off all electronic devices completely, store them in your bag, and close it.  

### Leaving the Lecture Hall by / Early Submission by  

---

### Task 1  
Multiple Choice (18 Points)  
The following tasks are multiple-choice/multiple-answer, meaning there is at least one correct answer for each. Subtasks with only one correct answer are scored with 1 point if correct. Subtasks with more than one correct answer are scored with 1 point for each correct and -1 point for each incorrect mark. Missing marks have no effect. The minimum score per subtask is 0 points.  

Please mark the correct answers:  
Marks can be crossed out by completely filling them in.  
Crossed-out answers can be re-marked by adjacent markings.  

a) * How many broadcast domains does the adjacent network consist of?  
3 6 1 5 2 4  

b) * How many collision domains does the adjacent network consist of?  
4 2 3 1 6 5  

c) * Given the following character stream:  
YAFFKAFPUAYYUKAUPK  
Which character has the highest information content?  
P K F A Y U  

d) * A source emits characters from the alphabet = “a”. What is the entropy of the source?  
∞  
other value 1 0 2  

e) * Which statement(s) about Huffman codes are correct?  
Frequently occurring characters are represented with shorter code words.  
It is a lossless compression method.  
Huffman codes always produce shorter code words than uniform codes.  
If all characters occur with equal probability, the shortest average code word length is achieved.  
All code words have the same length.  

f) * A packet of length 1500 B is transmitted over a channel with (independent) bit error probability p = 10^-4. Determine the probability that the packet is transmitted error-free.  
86.07% 0.01% 30.12% 99.99% other value  

g) * The adjacent signal space assignment represents which modulation method(s)?  
Q  
3-PSK 4-QAM 2-ASK 8-PSK 8-ASK  

h) * Given the number z = 123456 in decimal representation. 0x01e240 is the hexadecimal representation of z in:  
Network- Wireless- Big- Little- Internet- Wired-  
Byte- Byte- Endian Endian Byte- Byte-  
Order Order Order Order  

i) * What property(ies) does IPv6 have compared to IPv4?  
No DNS needed. Hop count in seconds. Fragmentation also possible in routers.  
Improved line coding. Fixed header size. 128 times larger address space.  

j) * Given a baseband signal with 4 distinguishable symbols and a transmission channel with a bandwidth of 1 MHz and an SNR of 15. Determine the achievable data rate(s).  
0.125 MB/s 0.5 MB/s 15.00 Mbit/s  
3.125 MB/s 4.00 Mbit/s 3.33 Mbit/s  
other value 2.00 Mbit/s 3.75 Mbit/s  

k) * What is the essential difference(s) between CSMA/CD and CSMA/CA?  
CSMA/CD uses acknowledgments, while CSMA/CA has only a contention phase for media access.  
There are only differences in collision handling, not in media access.  
CSMA/CA requires a minimum frame length of 64 B.  

l) * What feature(s) does an analog signal have?  
Time continuous value continuous time discrete value discrete  

m) * Which of the following IP addresses will not be globally routed?  
128.128.128.128 2001:1.0.13 fec0::1 2001::abcd:1  
feb0::1 192.169.24.25 192.192.1.1 127.255.1.2  

---

### Task 2  
Wireshark (17 Points)  
Given are the first 96 bytes of the Ethernet frame from Figure 2.1, which will be analyzed below.  

```
0x0000 90 e2 ba 2a 8d 97 90 e2 ba 08 00 45 86 dd 60 04  
0x0010 1a 84 01 a3 06 40 20 01 0d b8 00 00 00 00 92 e2  
0x0020 ba ff fe 08 00 45 2a 00 47 00 00 00 00 09 00 0f  
0x0030 00 00 00 00 00 00 c8 30 00 50 2e e7 4a d0 f5 17  
0x0040 f1 8d 80 18 08 00 ea 9a 00 00 01 01 08 0a 68 9b  
0x0050 63 a0 34 86 78 2e 47 45 54 20 2f 20 48 54 54 50  
```

**Figure 2.1: Snippet of an Ethernet frame**  
Note that justifications are required for subsequent parts. Ensure that markings can be uniquely assigned to individual subtasks. Unsubstantiated statements will not be graded.

a) * Mark the sender address at layer 2 in Figure 2.1. (without justification)  
0  

b) * Mark the recipient address at layer 2 in Figure 2.1. (without justification)  
0  

c) * What type is the L3-PDU?  
0 Type: Justification:  
1  

d) Provide the sender address at layer 3 in its usual and possibly shortened notation.  
0  
1  

e) By which mechanism was the sender address at layer 3 presumably assigned?  
0  
1  

f) Provide the recipient address at layer 3 in its usual and possibly shortened notation.  
0  
1  

g) What type is the L4-PDU?  
0  
1  
Type: Justification:  

h) Where does the L4-PDU begin?  
0  
1  
Offset: Justification:  

i) What L7 protocol is likely involved?  
0  
1  
Protocol: Justification:  

j) Where does the L7-PDU begin?  
0  
1  
Offset: Justification:  

k) Calculate the length of the L7-PDU in bytes.  
0  
1  
2  

The observed packet was transmitted in the topology shown in Figure 2.2 from PC to SRV. This figure also marks the position where the packet was recorded.  

**Figure 2.2: Network Topology**  
```
eth0 eth0 eth1 eth0 eth1 eth0  
Internet  
SRV  
PC R1 R2  
```

l) Assign the MAC addresses and IP addresses determinable from the recorded packet to the corresponding interfaces from Figure 2.2 (e.g., R3.eth3.MAC = ...). Only provide addresses that can be uniquely assigned.  

---

### Task 3  
Deceptive Name Resolution (13 Points)  
As a network expert, you want to test the speed and accuracy of a Large Language Model (LLM) using an example. You provide the LLM with the following input:  
Explain how the DNS resolution of an IPv4 address looks for the FQDN "cit.tum.de." from a PC with a resolver in the local network. The resolution should be performed according to the lecture. For each query and response, provide the label AND the RR type. Indicate whether each query is iterative or recursive.  

You then receive the following output:  
The DNS resolution for the FQDN "cit.tum.de." from a PC in a local network can proceed as follows:  
1. The PC in the local network sends a DNS request to obtain the IP address for the FQDN "cit.tum.de." The PC starts the DNS resolution with a recursive query.  
   Query: cit.tum.de. IN A  
2. The local DNS resolver in the local network receives the request from the PC and checks its cache for already existing information about "cit.tum.de." If the cache contains a corresponding entry, the resolution is completed and the response is sent back to the PC. If no information is available in the cache, the local DNS resolver must perform the resolution from scratch.  
3. The local DNS resolver is not authoritative for "tum.de." and has no direct information about "cit.tum.de." Therefore, it sends a recursive request to a root DNS server to obtain the IP address of the authoritative server for the top-level domain (TLD) "de."  
   Query: . IN NS  
4. The root DNS server responds with information about the name server for the TLD "de."  
   Answer: . IN NS a.nic.de.  
5. The local DNS resolver now sends a recursive request to the name server for the TLD "de." and asks for the name server for "tum.de."  
   Query: de. IN A  
6. The authoritative server for the TLD "de." responds with information about the name server for "tum.de."  
   Answer: de. IN NS  
7. The local DNS resolver sends a request to the name server for "tum.de." and asks for the IP address for "cit.tum.de."  
   Query: cit.tum.de IN A  
8. The name server for "tum.de." responds with the IP address for "cit.tum.de."  
   Answer: cit.tum.de. IN A <IPv4 Address>  
9. The local DNS resolver receives the response from the name server for "tum.de." and stores it in the cache for future requests. The local DNS resolver sends the response back to the PC.  
10. The PC in the local network receives the IP address for "cit.tum.de." and can now establish the desired connection to this address.  

In this process, the queries for DNS resolution occur recursively. The resource types are indicated by the designation "A" for the IP address and "NS" for the name server. It should be noted that this example shows the complete DNS resolution and that in practice caching and other optimizations are used to improve performance.  

a) Since you are familiar with DNS, identify a series of errors. List all errors and missing information in the table, along with the appropriate corrections.  
Please note the following:  
- Not every step contains an error.  
- Some steps contain multiple errors.  
- Errors that occur in multiple steps should be written separately for each step.  
- Not all rows of the table will be needed.  
- It suffices to list 10 errors, but there are more.  

| Step | Error | Correction/Addition |  
|------|-------|---------------------|  
| 6    |       |                     |  
| 7    |       |                     |  
| 8    |       |                     |  
| 9    |       |                     |  
| 10   |       |                     |  

b) * Given the following AAAA entry:  
server1.example.com. IN AAAA 2001:db8::567:89ab  
Provide the corresponding PTR entry for it.  

---

### Task 4  
Frequency Analysis (17 Points)  
Given is the basic impulse g(t) = 1 for 1/2 ≤ t < 1/2, which is repeated periodically at intervals of T = 2 µs. This gives the periodic signal s(t).  

a) * Draw the periodic signal s(t) in Figure 4.1.  

**Figure 4.1: Periodic Signal s(t)**  

b) * Determine the angular frequency ω of the signal.  

c) * Justify whether a Fourier series can be used to determine the spectrum of s(t).  

d) * Determine the DC component of s(t). Simplify the result as much as possible.  

e) * Determine the spectrum of s(t). Simplify the result as much as possible.  

**Notes:**  
1. Use symmetries.  
2.  
   \[ \int_{-c}^{c} x \sin(cx) \, dx = 0 \quad \text{and} \quad \int_{-c}^{c} x \cos(cx) \, dx = 0 \]  
3. No case distinction is required at the end of the calculation.  

---

### Task 5  
Networks (18 Points)  
We consider a typical scenario where a PC in the home network is connected to the Internet via a NAT-capable router A, as shown in Figure 5.1. We assume that the entire network is based on IPv4.  

**Figure 5.1: Network**  

First, let’s take a closer look at the “Internet” section: The routers are each gateway routers of the networks represented as clouds. The different routers determine their routing tables based on an optimal dynamic routing protocol. The costs are indicated on the respective edges.  

a) * Provide the resulting routing table for router A. You can use the respective lowercase letters of the reachable networks (as represented as clouds) for the IP prefixes, and the router name (as uppercase) for the IP address of the router. For example, the IP prefix z is reachable via router Z, while the router itself has the IP address Z in the respective transport networks. Note: Not all table rows are needed.  

| Destination | Next Hop | Iface |  
|-------------|----------|-------|  
|             |          |       |  

In the following, we assume that all caches are initially empty. The IP address of gateway router A and the grnvs.net server are known.  

PC1 wants to reach the website behind grnvs.net and would like to send a GET request via HTTPS.  

b) * What additional information is missing to address the frame?  

c) Through which protocol can this information from b) be obtained?  

d) What is the recipient MAC address of the first sent frame?  

e) * Before the actual request can be sent, handshakes must be performed. For which protocols?  

We now consider the sending of the first packet (the first handshake).  

f) Draw all exchanged frames on the path between PC1 and the server that are exchanged before and during the first packet between the nodes. You may abbreviate the actual IP packet with Payload as Pab. Note: You will find another template at the end of the exam.  

| PC1 | SW1 | A | B | C | D | E | G |  

g) Provide the corresponding values of the header fields at points I to III in the table below. You can use the names of the respective nodes for the IP addresses. Choose sensible values for freely selectable entries. Also, note and complete the NAT table of router A.  

| P | L3-Src | L3-Dst | L4-Src | L4-Dst | TTL |  
|---|--------|--------|--------|--------|-----|  
| I |        |        |        |        |     |  
| II |       |        |        |        |     |  
| III |      |        |        |        |     |  

**NAT Table of A:**  
| Local IP | Local Port | Global Port | Protocol |  
|----------|------------|-------------|----------|  
| PC1     | 8080       | 1234        | TCP      |  

h) * Assuming there is a problem on the path to the server and an ICMP "Packet too big" message would be sent back to the sender. Justify whether this would arrive.  

---

### Task 6  
Video Transmission (7 Points)  
You want to watch a large sports event on a major streaming portal. Your connection runs over IPv4 and has a bitrate of 200 Mbit/s. You notice (e.g., with traceroute) that there are 5 additional hops/routers between your computer and the server. The path to the server is a total of 7000 km long. The MTU is 1500 B.  

a) * What is the maximum size of an Ethernet frame?  

b) With what latency does the transmission take place? Provide the calculation method. Give the final result in ms and round to 2 decimal places.  

c) Since you unfortunately missed the beginning, you would like to download the highlights as a separate video afterward. The film has a size of 400 MB.  
How many frames must the film be divided into? Provide the calculation method.  

d) How much time elapses until the transmission is completed? Provide the calculation method and round the result to 2 decimal places.  

---

### Additional Space for Solutions. Clearly mark the assignment to each subtask.  
Do not forget to cross out invalid solutions.  

| PC1 | SW1 | A | B | C | D | E | G |