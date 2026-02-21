# Chair of Network Architectures and Services
School of Computation, Information and Technology  
Technical University of Munich

## Notes on Personalization:
- Your exam will be personalized during attendance control by affixing a code sticker.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID to be affixed next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

## Basics of Computer Networks and Distributed Systems
### Exam: IN0010/Endterm-90 
Date: Tuesday, August 8, 2023  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 16:30–18:00  

Before we proceed with reading the instructions for processing, we kindly ask you to answer the following questions. With this information, you help us to examine the learning success depending on individual components of the lecture. The information is voluntary and does not influence the grading. To exclude any influence, this page will not be accessible during the correction.

a) Did you attend the lecture?  
1 (regularly) 2 3 4 (never)  

b) Did you watch the recording of the previous year?  
1 (regularly) 2 3 4 (never)  

c) Did you attend the tutorial exercises?  
1 (regularly) 2 3 4 (never)  

d) Did you participate in the live programming session (TCP UDP Chat)?  
Yes (both dates) At one date No  

## Instructions for Processing
- This exam consists of 12 pages with a total of 6 tasks.
- Please check now that you have received a complete set of information.
- The total score for this exam is 90 points.
- It is prohibited to tear out pages from the exam.

### Allowed Aids:
- A non-programmable calculator
- An analog dictionary (German native language) without notes

- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be graded where the solution path is identifiable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write with red/green colors or with pencil.
- Turn off all electronic devices you carry completely, store them in your bag, and close it.

## Task 1
### Wireshark (19 Points)
Given is the network topology from Figure 1.1. The computer PC attempts to establish an SSH connection via IPv4 to the server SRV. The MAC and IP addresses of the devices are specified in Figure 1.1.

```
04:7b:cb:b7:08:00  04:7b:cb:b7:08:01  f8:52:fb:84:4d:ee  04:7b:cb:b7:08:01
192.168.0.8       95.157.26.64       131.159.252.145   131.159.20.214
```

```
Internet
SRV
PC  SW  R1  R2
192.168.0.254  131.159.20.254
3c:a6:2f:78:08:00  l34:3a:f7:18:d0:6c
```

**Figure 1.1: Network Topology**  
We consider the frame sent from R1 to PC (see Figure 1.1). This is the first message from SRV after the TCP handshake.  
The hex dump of this frame should be reconstructed based on the information from Figure 1.1 and the following sub-tasks.  
The solutions to the following sub-tasks are to be entered directly in Figure 1.2 (see next page). Clearly indicate which sub-task an entry belongs to, e.g., by color highlighting or indicating the respective sub-task above your solution. As an example for a (non-existent) sub-task x), the L2 destination address is already entered.

**Notes:** In the finished hex dump, some gaps may remain, as we will not reconstruct all contents of the frame. The cheat sheet distributed with this exam contains all necessary headers and translations.

a) * Enter the sender address at Layer 2 in Figure 1.2.  

b) * Fill in the field in Figure 1.2 that specifies the type of the L3 PDU.  

Before we continue with filling in, the boundaries of various headers should be marked. We assume that:  
- The L3 header does not use options,  
- The L4 header has exactly 12 bytes of options, and  
- The total length of the frame (including checksum) is 111 bytes.  

c) * Mark the end of the L3 and L4 headers as well as the end of the frame. As an example, the end of the L2 header is already marked.  

d) The checksum of the frame is given as 42 0a f1 73. Enter this in Figure 1.2.  

```
(x) (a) (b) end of (eL)2
00xx0000 0044 77bb ccbb bb77 0088 0000 3c a6 2f 78 08 00 08 00 45
```

```
d)
```

```
00xx1100 06 83 9f 14 d6 c0 a8
```

```
00xx2200 00 08 00 16 8e 6a 8?
```

```
00xx3300
```

```
00xx4400 53 53 48 2d 32
```

```
00xx5500
```

```
(d) end of frame
```

**Figure 1.2: Template for the Hex Dump of the Frame**  

We now begin to fill in the various fields of the L3 header. The start of the L3 header is already given in Figure 1.2. Do not forget to indicate which sub-task each entry belongs to.

e) * Fill in the field that indicates the type and length of the L3 header.  

f) * Fill in the L3 source address.  

g) * Fill in the L3 destination address.  

h) * Fill in the field that specifies the type of the L3 SDU.  

We then continue to fill in various fields of the L4 header. If a value is not uniquely defined, make a sensible choice (no justification necessary). Do not forget to indicate which sub-task each entry belongs to.

i) Fill in the source port.  

j) Fill in the destination port.  

k) Fill in the field that specifies the offset.  

Now we come to the actual payload, which consists of the ASCII-encoded string “SSH-2.0-OpenSSH_9.2p1 Debian-2”.  

l) Fill in the first 5 bytes of the L7 PDU.  

## Task 2
### IP Routing (17 Points)
You want to measure the performance of a new Layer 7 network protocol. For this, you need to configure your own experimental setup. You have already reserved three servers. Ethernet cables are connected to the corresponding interfaces (see Figure 2.1). For each measurement, servers are always completely reinstalled (this means nothing is configured). All servers are connected to a management network (10.1.176.0/20), and the router R has the address 10.1.176.1.

```
Switch R
Internet
eth0: 7e:e2:84:02:d2:b7  eth0: 26:a0:0c:22:b1:b9
eth0: aa:5b:85:b2:57:d8
eth1: a2:ff:cf:ae:24:0f  eth2: ce:e1:43:c0:11:8a
eth1: b2:60:19:84:d0:27  eth1: a6:94:a7:36:6a:f5
```

**Figure 2.1: Network Topology**  

**Table 2.1: Interfaces and their IP Addresses as well as Connected Subnets**  

| Interface (e.g., S1.eth1) | IP Address       | Subnet              |
|----------------------------|------------------|---------------------|
| S1.eth0                    | 10.1.176.2       | 10.1.176.0/20       |
| S2.eth0                    | 10.1.184.0       | 10.1.176.0/20       |
| S3.eth0                    | 10.1.176.4       | 10.1.176.0/20       |
| S1.eth1                    | 192.168.1.1      | 192.168.1.0/24      |
| S2.eth1                    | 192.168.1.2      | 192.168.1.0/24      |
| S2.eth2                    | 192.168.2.1      | 192.168.2.0/24      |
| S3.eth1                    | 192.168.2.2      | 192.168.2.0/24      |

a) * Assign all servers a random IP address from the management network via DHCP and configure the default gateway. Servers should always receive the same address, so consider previously assigned addresses from Table 2.2. Fill in Table 2.1 for the affected interfaces.

**Table 2.2: IP Addresses that have already been assigned to servers (identified by MAC)**  

It seems that S2.eth2 was once connected to the management network, which is why it has an entry in the DHCP table. However, since R is not connected to S2.eth2, it cannot assign an IP address to this interface! R will also not assign an IP address to any other interface (e.g., S3.eth0) since these IP addresses are already occupied and instead distribute a new (random) one.

b) * For your measurements, the testbed servers must communicate directly with each other (to eliminate interference factors). Configure the interfaces of connections A and B so that the servers can communicate over them (in Table 2.1). The network traffic of your measurement should not go through the management network and should not restrict any other communication (e.g., the call of a website). For A and B, you need to think of two new subnets (and assign correct IP addresses) that come from a private address range and do not overlap with the management network.

c) Fill in the resulting static routing table of S2 after configuring all interfaces.

| Destination         | Next Hop      | Iface   |
|---------------------|---------------|---------|
| 192.168.1.0/24      | 0.0.0.0      | eth1    |
| 192.168.2.0/24      | 0.0.0.0      | eth2    |
| 10.1.176.0/20       | 0.0.0.0      | eth0    |
| 0.0.0.0/0           | 10.1.176.1    | eth0    |

d) * For the protocol to work, multiple processes must communicate with each other. Provide an IP address with which you can reach processes on the same server (no justification needed).  
127.0.0.1  

e) * Explain how you can address a specific process on the same server.  
By addressing using the ports of the Layer 4 protocol.  

f) * The configuration of addresses was cumbersome. With IPv6, this happens automatically. Provide the link-local addresses (and associated subnet) that S3 assigns to its interfaces via SLAAC.

```
eth0: 26:a0:0c:22:b1:b9  fe80::24a0:0cff:fe22:b1b9 (fe80::/64)
eth1: a6:94:a7:36:6a:f5  fe80::a494:a7ff:fe36:6af5 (fe80::/64)
```

g) Through this link-local address, S3 reaches through the NDP. Through a Router Advertisement, the server learns the global-unique prefix (2a5e:82ac::/64). Provide the global-unique addresses of all interfaces of S3 that result from this (or justify if this is not possible).

```
eth0: 2a5e:82ac::24a0:0cff:fe22:b1b9
```

The prefix from the router only affects the management network and not link B. This is in a different broadcast domain than R (and would therefore not receive the advertisement at all).

h) * The addresses in the management network (10.1.176.0/20) are running out. Expand the network so that it remains as small as possible, but has space for 10,000 addresses and the existing addresses still function. Provide the new network in CIDR notation and justify your choice.  
New network size:  
`⌈log2(10000)⌉ = 14`  
Resulting subnet mask: 255.255.192.0  
`176 = 0b10111000` and `192 = 0b11000000`  
`0b10111000 AND 0b11000000 = 128`  
`⇒ 10.1.128.0/18`  

## Task 3
### Multiple Choice (9 Points)
The following tasks are multiple choice/multiple answer, meaning there is at least one correct answer option for each. Tasks with only one correct answer are scored with 1 point if correct. Tasks with more than one correct answer are scored with 1 point for each correct and -1 point for each incorrect tick. Missing ticks have no effect. The minimum score per task is 0 points.

Please tick the correct answers.  
Ticks can be crossed out by completely filling them in.  
Crossed-out answers can be re-ticked by adjacent markings.

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
- prevent the network from becoming overloaded.  
- detect message loss.  
- confirm connections.  
- prevent the receiver from becoming overloaded.  

d) * The syscall select()...  
- selects a socket for transmission.  
- is only meaningful for TCP sockets.  
- monitors a set of sockets.  
- blocks until at least one socket is ready or (if specified) a timeout occurs.  
- creates a new socket.  

**NAT Table of R**  

| Local IP Addr       | Local Port | Global Port |
|---------------------|------------|-------------|
| 185.86.235.241      | 192.168.1.1| 4657        |
| PC1                 | 192.168.1.2| 4657        |  
| 8005                 |            |             |

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

## Task 4
### Multiple Choice (9 Points)
The following tasks are multiple choice/multiple answer, meaning there is at least one correct answer option for each. Tasks with only one correct answer are scored with 1 point if correct. Tasks with more than one correct answer are scored with 1 point for each correct and -1 point for each incorrect tick. Missing ticks have no effect. The minimum score per task is 0 points.

Please tick the correct answers.  
Ticks can be crossed out by completely filling them in.  
Crossed-out answers can be re-ticked by adjacent markings.

a) * Given are the rectangular impulse (t) and the cosine 2-impulse (t). The figure below shows four different spectra. Which statements are correct?  

b) * Given is a signal s(t) with power P = 10mW and a noise power of P = 10mW. What is the value of the signal-to-noise ratio in this case?  
- 10 bit  
- 1 bit  
- 0 dB  
- 1  
- 1 dB  
- 10 dB  

c) * A value-continuous signal is to be quantized in the interval I = [-2; 2] such that the maximum quantization error within I is at most 1/2. How many quantization levels are minimally required for this?  

d) * The adjacent signal space assignment represents which modulation methods?  
- 1-ASK  
- 2-PSK  
- 2-QAM  
- 2-ASK  
- 1-PSK  

e) * How many broadcast domains does the adjacent network consist of?  

f) * How many collision domains does the adjacent network consist of?  

## Task 5
### Frequency Analysis (18 Points)
Given is the basic impulse g(t) = 1 - t^2, which is periodically repeated at intervals of T = 2s.

a) * Draw the resulting periodic signal s(t) in Figure 5.1.  

b) * Determine the angular frequency ω of the signal.  
`ω = 2π/T = π`  

c) * Briefly justify whether a Fourier series can be used for frequency analysis.  
Yes, since s(t) is periodic, it can be represented as a sum of weighted sine and cosine components.  

d) * Determine the DC component of s(t). Simplify the result as much as possible.  

e) * Determine the spectrum of s(t). Simplify the result as much as possible.  
**Hints:**  
1. Use symmetries.  
2. The even function is zero at all odd harmonics.  

## Task 6
### Channel and Line Coding (18 Points)
a) * Briefly explain in your own words what channel codes are and where they are used.  
Channel codes add targeted (structured) redundancy to transmitted data. This enables error detection and correction.  

b) * Briefly explain in your own words what line codes are and where they are used.  
Line codes are mapping rules to convert channel words (or individual bits) into a physical representation.  

c) Given the string LOL as the message.  
d) * Provide the string ASCII-encoded in binary representation. Use 8 bits per character.  
**Note:** It is recommended to provide the binary message in groups of 4 bits.  

e) * What is the purpose of the 4B5B code?  
To add control characters.  

f) * Justify whether the 4B5B code is a channel code or a line code.  
Strictly speaking, it is neither a channel nor a line code, but simply a block code:  
1. Line codes define how bits (or bit groups) are represented by physically measurable quantities. The 4B5B code does not do this. Only in combination with a line code like MLT-3 (which can also be used without the 4B5B code) does a translation into physical quantities occur. Nevertheless, the 4B5B code is mostly referred to in literature as a line code.  
2. Channel codes add structured redundancy to enable error detection and correction. The 4B5B code only provides control characters that may contain relevant information for transmission and thus do not add redundancy. In particular, the 4B5B code does not serve to detect or correct transmission errors.  

g) * Provide the binary message from sub-task c) after it has been encoded using 4B5B.  

h) * To transmit the message, the symbol J/K is added at the beginning of the message and the symbol T at the end of the message.  

g) * What is the purpose of the two symbols?  
To indicate the beginning and end of the message to the receiver.  

h) * Provide the first 10 bits of the resulting message.  
The first 10 bits are the J/K symbol, so `11000 10001`.  

i) As a line code, MLT-3 is used. Draw the signal waveform s(t) for the first 10 bits of the transmitted message. At time t = 0, s(t) = 0.  

j) * A memoryless source emits characters of the 4B5B code. The occurrence probability of all 24 characters is equally high, but the 0 (Hex data 0) and Quiet (Q) occur twice as often as the others. Calculate (with calculation steps) the entropy H of X.  
`H(X) = log2(24) - (1/24) * log2(1/24) - (1/12) * log2(1/12)`  

## Additional Space for Solutions
Clearly mark the assignment to each sub-task.  
Do not forget to cross out invalid solutions.