# Chair of Network Architectures and Services
School of Computation, Information and Technology  
Technical University of Munich  

## Notes on Personalization:
- Your exam will be analyzed during attendance control by affixing a code personal to you.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID to be affixed next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

## Basics of Computer Networks and Distributed Systems
Exam: IN0010/Endterm-90  
Date: Tuesday, August 8, 2023  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 16:30–18:00  

Before we proceed with reading the instructions, please answer the following questions. With this information, you help us to investigate the learning success depending on individual components of the lecture. The information is voluntary and does not influence the grading. To exclude any influence, this page will not be accessible during the correction.

a) Did you attend the lecture?  
1 (regularly) 2 3 4 (never)  

b) Did you watch the recording from last year?  
1 (regularly) 2 3 4 (never)  

c) Did you attend the tutorial exercises?  
1 (regularly) 2 3 4 (never)  

d) Did you participate in the live programming session (TCP UDP Chat)?  
Yes (both dates) At one date No  

## Instructions for Processing
- This exam consists of 12 pages with a total of 6 tasks.  
Please check now that you have received a complete set of information.  
- The total score for this exam is 90 points.  
- It is prohibited to tear out pages from the exam.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - an analog dictionary in German without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  
- Turn off all electronic devices completely, store them in your bag, and close it.  

## Leaving the Auditorium from until / Early Submission by

---

### Task 1
Wireshark (19 Points)  
Given is the network topology from Figure 1.1. The computer PC attempts to establish an SSH connection via IPv4 to the server SRV. The MAC and IP addresses of the devices are specified in Figure 1.1.

```
04:7b:cb:b7:08:00 04:7b:cb:b7:08:01 f8:52:fb:84:4d:ee 04:7b:cb:b7:08:01  
192.168.0.8 95.157.26.64 131.159.252.145 131.159.20.214  
```

Internet  
SRV  
PC SW R1 R2  
192.168.0.254 131.159.20.254  
3c:a6:2f:78:08:00 34:3a:f7:18:d0:6c  

Figure 1.1: Network Topology  

We consider the frame sent from R1 to PC (see Figure 1.1). This is the first message from SRV after the TCP handshake.  
In the following, the hex dump of this frame should be reconstructed based on the information from Figure 1.1 and the subsequent sub-tasks.  
The solutions to the subsequent sub-tasks should be entered directly in Figure 1.2 (see next page). Clearly indicate which sub-task an entry belongs to, e.g., through color highlighting or by indicating the respective sub-task above your solution. As an example for a (non-existent) sub-task x), the L2 recipient address has already been entered.

Notes: In the completed hex dump, some gaps may remain, as we will not reconstruct all contents of the frame. The cheat sheet distributed with this exam contains all necessary headers and translations.

a) * Enter the sender address at layer 2 in Figure 1.2.  
0  

b) * Fill in the field in Figure 1.2 that indicates the type of the L3 PDU.  
0  
1  

Before we continue with filling in, the boundaries of various headers should be marked. We assume that  
- the L3 header does not use options,  
- the L4 header has exactly 12 bytes of options, and  
- the total length of the frame (including checksum) is 111 bytes.  

---

c) * Mark the end of the L3 and L4 headers as well as the end of the frame. As an example, the end of the L2 header is already marked.  
0  
1  

d) The checksum of the frame is given as 42 0a f1 73. Enter this in Figure 1.2.  
2  

```
(x) end of L2  
0x00 04 7b cb b7 08 00  
d)  
0  
½  
0x10  
0x20  
0x30  
0x40  
e)  
0  
0x50  
1  
f)  
0  
0x60  
1  
```

Figure 1.2: Template for the Hex Dump of the Frame  
2  
g)  
0  

We begin by filling in the various fields of the L3 header. The beginning of the L3 header is already given in Figure 1.2. Do not forget to indicate which sub-task each entry belongs to.  
2  

h) e) * Fill in the field that indicates the type and length of the L3 header.  
0  

f) * Fill in the L3 source address.  
1  

g) * Fill in the L3 destination address.  
i)  
0  

h) * Fill in the field that indicates the type of the L3 SDU.  
1  
2  

We then continue to fill in various fields of the L4 header. If a value is not uniquely defined, make a sensible choice (no justification necessary). Do not forget to indicate which sub-task each entry belongs to.  
1  

i) Fill in the source port.  
2  

j) Fill in the destination port.  
k)  
0  

k) Fill in the field that indicates the offset.  
1  

Now we come to the actual payload, which consists of the ASCII-encoded string “SSH-2.0-OpenSSH_9.2p1 Debian-2”.  
l)  
0  

l) Fill in the first 5 bytes of the L7 PDU.  
1  
2  

---

### Task 2
IP Routing (17 Points)  
You want to measure the performance of a new Layer 7 network protocol. To do this, you need to configure your own experimental setup. You have already reserved three servers. Ethernet cables are connected to the respective interfaces (see Figure 2.1). For each measurement, the servers will always be completely reset (this means nothing is configured). All servers are connected to a management network (10.1.176.0/20), the router R has the address 10.1.176.1.

```
Switch R  
Internet  
eth0: 7e:e2:84:02:d2:b7 eth0: 26:a0:0c:22:b1:b9  
eth0: aa:5b:85:b2:57:d8  
eth1: a2:ff:cf:ae:24:0f eth2: ce:e1:43:c0:11:8a  
eth1: b2:60:19:84:d0:27 eth1: a6:94:a7:36:6a:f5  
A B  
S1 S2 S3  
```

Figure 2.1: Network Topology  

| Interface (e.g., S1.eth1) | IP Address | Subnet |
|----------------------------|------------|--------|

a) * R assigns all servers a random IP address from the management network via DHCP and configures the default gateway. Servers should always receive the same address, so consider previously assigned addresses from Table 2.2. Fill in Table 2.1 for the affected interfaces.  

| Table 2.2: IP Addresses that have already been assigned to servers (identified by MAC) |
|----------------------------|------------|
| MAC | IP Address |
| 7e:e2:84:02:d2:b7 | 10.1.176.2 |
| aa:5b:85:b2:57:d8 | 10.1.184.0 |
| ce:e1:43:c0:11:8a | 10.1.185.0 |

b) * For your measurements, the testbed servers must communicate directly with each other (to exclude interference factors). Configure the interfaces of connections A and B so that the servers can communicate over them (in Table 2.1). The network traffic of your measurement should not go over the management network and should not restrict any other communication (e.g., the call of a website).  

c) Fill in the resulting static routing table of S2 (after configuring all interfaces).  
0  
1  

| Destination | Next Hop | Iface |
|-------------|----------|-------|
| 2           | 3        | 4     |

d) * For the protocol to work, multiple processes must communicate with each other. Provide an IP address with which you can reach processes on the same server (no justification).  
0  
1  

e) * Explain how you can address a specific process on the same server.  
0  
1  

f) The configuration of addresses was cumbersome. With IPv6, this is done automatically. Provide the link-local addresses (and associated subnet) that S3 assigns to its interfaces via SLAAC.  
0  
1  
2  
3  

g) Through the link-local address, S3 reaches through the NDPR. Through a Router Advertisement, the server learns the global-unique prefix (2a5e:82ac::/64). Provide the global-unique addresses of all interfaces of S3 that result from this (or justify if this is not possible).  
1  
2  

h) * The addresses in the management network (10.1.176.0/20) are running out. Expand the network so that it remains as small as possible, but has space for 10,000 addresses and the existing addresses still function. Provide the new network in CIDR notation and justify your choice.  
1  

---

### Task 3
Multiple Choice (9 Points)  
The following tasks are multiple choice/multiple answer, i.e., there is at least one correct answer option for each. Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 1 point for each correct and -1 point for each incorrect tick. Missing ticks have no effect. The minimum score per sub-task is 0 points.

×  
Tick the correct answers.  
× Ticks can be crossed out by complete filling.  
× Ticked answers can be crossed out by adjacent markings.

a) * Which statements about DNS are correct?  
- Every resolver is also an authoritative nameserver.  
- An SOA record contains information for synchronization with secondary nameservers.  
- A resolver contacts only a single nameserver in an iterative name resolution.  
- The TTL indicates how long a resource record may be cached.  
- PTR records must be in the same zone as the corresponding A/AAAA records.  

b) * Which are not valid DNS resource records?  
- TXT  
- CNAME  
- MX  
- IN  
- NS  
- AAAA  

c) * In TCP, flow control aims to...  
- not overload the network.  
- detect message loss.  
- confirm connections.  
- not overload the recipient.  

d) * The syscall select()...  
- selects a socket for transmission.  
- is only meaningful for TCP sockets.  
- monitors a set of sockets.  
- blocks until at least one socket is ready or (if specified) a timeout occurs.  
- creates a new socket.  

NAT Table of R Server  
| Local IP Addr | Local Port | Global Port |
|----------------|-------------|-------------|
| 185.86.235.241 | 192.168.1.1 | 4657        | 8005 |
| PC1            | 192.168.1.2 | 4657        | 8006 |
| 192.168.1.1    |             |             |      |

PC2 IF1:192.168.1.254 IF2:131.159.20.19  
192.168.1.2  

e) * Given the above network with the NAT router R. PC2 sent an HTTP request to the server. What is the source IP address in the IP packet at position P2?  
- 127.0.0.1  
- 185.86.235.241  
- 192.168.1.254  
- 192.168.1.1  
- 131.159.20.19  
- 192.168.1.2  

f) * Given the above network with the NAT router R. The server sends an HTTP reply to PC2 within the already established connection. What is the destination IP address in the IP packet at position P2?  
- 131.159.20.19  
- 127.0.0.1  
- 192.168.1.254  
- 185.86.235.241  
- 192.168.1.1  
- 192.168.1.2  

g) * Given the above network with the NAT router R. The server sends an HTTP reply to PC2 within the already established connection. What is the destination port in the segment at position P1?  
- 65535  
- 443  
- 8006  
- 4657  
- 8005  
- 80  
- 4658  
- 1024  

---

### Task 4
Multiple Choice (9 Points)  
The following tasks are multiple choice/multiple answer, i.e., there is at least one correct answer option for each. Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 1 point for each correct and -1 point for each incorrect tick. Missing ticks have no effect. The minimum score per sub-task is 0 points.

×  
Tick the correct answers.  
× Ticks can be crossed out by complete filling.  
× Ticked answers can be crossed out by adjacent markings.

a) * Given is the rectangular impulse (t) as well as the cos2 impulse (t). The figure below shows four different spectra. Which statements are correct?  
- c s c s c s c s  
- (a) S(f) (b) S(f) (c) S(f) (d) S(f)  
- 1 2 3 4  
- c s c s c s c s  
- s(t) S(f) s(t) S(f) s(t) S(f) s(t) S(f)  
- 1 1 1 3 2 1 2 3  
- s(t) S(f) s(t) S(f) s(t) S(f) s(t) S(f)  
- 1 2 1 4 2 2 2 4  

b) * Given is a signal s(t) with power P = 10mW and a noise power of P = 10mW. What is the value of the signal-to-noise ratio in this case?  
- 10 bit  
- 1 bit  
- 0 dB  
- 1  
- 1 dB  
- 10 dB  

c) * A value-continuous signal is to be quantized in the interval I = [-2;2] such that the maximum quantization error within I is at most 1/2. How many quantization levels are minimally required?  
- 12  
- 6  
- 10  
- 8  
- 4  
- 2  
- 16  
- 14  

d) * The adjacent signal space assignment represents which modulation methods?  
- 1-ASK  
- 2-PSK  
- 2-QAM  
- 2-ASK  
- 1-PSK  

e) * How many broadcast domains does the adjacent network consist of?  
- 1  
- 3  
- 2  
- 4  
- 5  
- 6  

f) * How many collision domains does the adjacent network consist of?  
- 1  
- 3  
- 5  
- 2  
- 4  
- 6  

---

### Task 5
Frequency Analysis (18 Points)  
Given is the basic impulse g(t) = 1 for t^2, which is periodically repeated at intervals of T = 2s.

a) * Draw the resulting periodic signal s(t) in Figure 5.1.  
0  
1  
1.5  
2  
1  
)  
s(t)  
0.5  
0  
−4 −3 −2 −1 0 1 2 3 4  
Time [s]  

Figure 5.1: Periodic Signal s(t)  

b) * Determine the angular frequency ω of the signal.  
1  

c) * Briefly justify whether a Fourier series can be used for frequency analysis.  
0  
1  

d) * Determine the DC component of s(t). Simplify the result as much as possible.  
0  
1  
2  
3  
4  

e) * Determine the spectrum of s(t). Simplify the result as much as possible. Notes:  
1. Use symmetries.  
2. \( \int x^2 \cos(cx) dx = \frac{2}{c^3} \) and \( \int x^2 \sin(cx) dx = \frac{2}{c^3} \)  

---

### Task 6
Channel and Line Coding (18 Points)  
a) * Briefly explain in your own words what channel codes are and where they are used.  
0  
1  
2  

b) * Briefly explain in your own words what line codes are and where they are used.  
0  
1  
2  

We will consider the string LOL as the message.  
c) * Provide the string in ASCII encoded binary representation. Use 8 bits per character.  
0  
Note: It is recommended to present the binary message in groups of 4 bits.  
1  
2  

Before transmission, we encode the message with the 4B5B code (see Table 6.1).  
d) * What is the purpose of the 4B5B code?  
0  
1  

e) * Justify whether the 4B5B code is a channel code or a line code.  
0  
1  
2  

f) * Provide the binary message from part c) after it has been encoded with 4B5B.  
0  
Note: It is recommended to present the binary message in groups of 5 bits.  
1  
2  

| Input | Output | Meaning | Input | Output | Meaning |
|-------|--------|---------|-------|--------|---------|
| 0000  | 11110  | Hex data 0 | 1100  | 11010  | Hex Data C |
| 0001  | 01001  | Hex data 1 | 1101  | 11011  | Hex Data D |
| 0010  | 10100  | Hex data 2 | 1110  | 11100  | Hex Data E |
| 0011  | 10101  | Hex data 3 | 1111  | 11101  | Hex Data F |
| 0100  | 01010  | Hex data 4 | -     | 00000  | Quiet(Q) |
| 0101  | 01011  | Hex data 5 | -     | 11111  | Idle(I) |
| 0110  | 01110  | Hex data 6 | -     | 11000  | Start#1(J) |
| 0111  | 01111  | Hex data 7 | -     | 10001  | Start#2(K) |
| 1000  | 10010  | Hex data 8 | -     | 01101  | End(T) |
| 1001  | 10011  | Hex data 9 | -     | 00111  | Reset(R) |
| 1010  | 10110  | Hex data A | -     | 11001  | Set(S) |
| 1011  | 10111  | Hex data B | -     | 00100  | Halt(H) |

Table 6.1: 4B5B Encoding Table  

To transmit the message, the symbol J/K is inserted at the beginning of the message and the symbol T/ at the end of the message.  
g) * What is the purpose of the two symbols?  
0  
1  

h) * Provide the first 10 bits of the resulting message.  
0  
1  

i) As a line code, MLT-3 is used. Draw the signal waveform s(t) for the first 10 bits of the transmitted message. At time t = 0, s(t) = 0.  
0  
1  
2  
3  

s(t)  
1  
1 2 3 4 5 6 7 8 9 10 11 t/T  
−  
1  
Q  

j) * A memoryless source emits symbols of the 4B5B code. The occurrence probability of all 24 symbols is equally high, but the 0 (Hex data 0) and Quiet (Q) occur twice as often as the other symbols. Calculate (with calculation steps) the entropy H of this.  
1  
2  

---

### Additional Space for Solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to cross out invalid solutions.