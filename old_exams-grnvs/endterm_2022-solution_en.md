Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during attendance control by affixing a code sticker.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID here.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Basics of Computer Networks and Distributed Systems  
**Exam: IN0010/Endterm**  
**Date: Monday, August 1, 2022**  
**Examiner: Prof. Dr.-Ing. Georg Carle**  
**Time: 10:45–12:15**  

### Instructions for Completion
- This exam consists of 12 pages with a total of 7 tasks as well as a formula collection (cheat sheet). Please check now that you have received a complete set of documents.
- The total score for this exam is 91 points.
- Removing pages from the exam is prohibited.
- The following aids are permitted:
  - A non-programmable pocket calculator
  - An analog dictionary (German native language) without annotations
  - The cheat sheet distributed with this exam
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only results where the solution path is recognizable will be scored. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write in red/green colors or with a pencil.
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.

### Additional Space for Solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to cross out invalid solutions.

### Task 1  
**Multiple Choice (19 Points)**  
The following tasks are multiple choice/multiple answer, i.e., at least one answer option is correct for each. Sub-tasks with only one correct answer will be scored with 1 point if correct. Sub-tasks with more than one correct answer will be scored with 1 point for each correct and 1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.

**Mark the correct answers**  
- Marks can be crossed out by completely filling them in.  
- Crossed-out answers can be marked again by adjacent markings.  

a)* A frame with a total length of 1500 B requires a serialization time of 2 µs. What is the transmission rate of the link?  
- 6000 GB/s  
- 2 Gbit/s  
- 750 MB/s  
- 2 Mbit/s  
- 750 Mbit/s  
- 1500 Mbit/s  

b)* A frame with a total length of 1500 B is transmitted over a copper line of length 10 km. What propagation delay occurs approximately?  
- 50 ns  
- 476 µs  
- 33.3 µs  
- 50 µs  
- 33.3 ns  
- 476 ns  

c)* Which of the following properties apply to UDP?  
- must not be fragmented  
- stream-oriented  
- works on the transport layer only ports 1024 usable  
- datagram-oriented  
- works on the network layer only ports <1024 usable  
- connection-oriented  

d)* What is the essential difference between CSMA/CD and CSMA/CA?  
- In media access with CSMA/CA, there is always a contention phase of 64 B.  
- CSMA/CD uses acknowledgments, unlike CSMA/CA. There are only differences in collision handling, not in media access.  

e)* Which statement(s) about Fourier series and Fourier transformations regarding time-continuous signals are false?  
- Using Fourier transformation, the spectrum of non-periodic signals cannot be determined.  
- Using Fourier series, the spectrum of non-periodic signals can be determined.  
- Using Fourier transformation, the spectrum of periodic signals can be determined.  
- Using Fourier series, the spectrum of periodic signals can be determined.  

f)* A packet is a ...  
- L4-SDU  
- L2-PDU  
- L4-PDU  
- L3-SDU  
- L1-PDU  
- L3-PDU  
- L1-SDU  
- L2-SDU  

g)* An interface has the link-local IPv6 address fe80:0000:0000:0000:0312:23ff:fe34:4556. What L2 address does this interface most likely have?  
- 01:02:03:04:05:06  
- 56:45:34:23:12:01  
- 03:12:23:34:45:56  
- 31:22:3f:ff:e3:44  
- 23:ff:fe:34:45:56  
- fe:80:03:12:23:ff  
- 01:12:23:34:45:56  
- 06:05:04:03:02:01  

h)* Which of the following IP addresses are loopback addresses?  
- fe80::1234  
- 127.0.0.2  
- ::  
- 2001:db8::1234  
- 0.0.0.0  
- ::2  
- 128.0.0.1  
- ::1  

i)* How long is an IPv6 address?  
- 16 B  
- 2128 bit  
- 128 B  
- 2128 B  

j)* Ethernet is a protocol for ... in the ISO-OSI model.  
- Layer 4  
- Layer 7  
- Layer 3  
- Layer 5  
- Layer 6  
- Layer 1  
- Layer 2  

k)* Which protocol is not part of the application layer?  
- DNS  
- HTTP  
- FTP  
- SNMP  
- ICMP  
- HTTPS  
- SSH  
- SMTP  

l)* You observe the following data stream from an unknown source. At which character is the information content maximal?  
- H  
- G  
- A  
- A  
- B  
- B  
- A  
- F  
- A  
- G  
- H  
- F  
- G  
- B  
- H  
- A  
- B  
- G  
- A  
- G  
- F  
- B  
- H  
- F  

m)* Given the following date in Big-Endian: 0xf3b68745. Which of the following data corresponds to this in Network Byte Order?  
- 0x4587b6f3  
- 0x3f6b7854  
- 0xf3b68745  
- 0x54786b3f  

n)* What is meant by source coding?  
- The removal of redundancy  
- Targeted addition of redundancy  
- Representation of data by sequences of impulses  
- None of the above  

### Task 2  
**Short Tasks (6.5 Points)**  

a)* Name four different multiplexing methods discussed in the lecture regarding media access control (without explanation).  
- Time Division Multiplex (TDM)  
- Frequency Division Multiplex (FDM)  
- Space Division Multiplex (SDM)  
- Code Division Multiplex (CDM)  

b)* We consider a switch that has just been put into operation, whose switching table is empty. It received a frame for forwarding. On which ports will the switch likely forward the frame?  
If the port corresponding to the recipient's L2 address is unknown, the frame will likely be broadcasted to all other ports except the one on which the frame was received.  

c)* On which layer in the ISO-OSI model does DNS operate? (without justification)  
- Application layer  

d)* Given the Fourier series of a periodic signal s(t) with a > 0. Justify whether the signal s(t) is DC-free during transmission or not.  
The parameter a of the Fourier spectrum indicates the DC component of the cosine or sine function. If this is greater than 0, it indicates a DC component, which causes a DC offset.  

e)* Given the spectrum of a Fourier series below. Draw the corresponding time signal s(t) in the solution field in the interval [0,2]. Here, ω = 2π, with T = 1 s.  

### Task 3  
**TCP Data Transmission (8.5 Points)**  
You want to call a website via HTTP. Your computer is currently connected via Ethernet and IPv4. Consequently, your current MTU is 1500 B. Your TCP implementation also uses the Maximum Segment Size (MSS) option, with which a receiver can inform the sender of the maximum allowed size of segments. RFC793 defines the MSS option as follows:  
```
Maximum Segment Size
+--------+--------+---------+--------+
|00000010|00000100| max seg size |
+--------+--------+---------+--------+
Kind=2 Length=4
```

a)* Calculate the maximum MSS so that fragmentation does not have to occur. Indicate where the numbers come from.  
1500 B (Ethernet MTU) - 20 B (IPv4 Header) - 20 B (TCP Header) - 4 B (MSS Option) = 1456 B  

b)* What is the size of the receive window (in bytes) if the buffer of your computer can hold the data from 7 segments (as large as possible)?  
7 MSS = 7 * 1456 B = 10192 B  

c)* Complete the TCP handshake and the specifications for the first two segments from the client and server. Assume a 980-byte HTTP request and a 5 MB response. Client and server always try to make the segments as large as possible.  
```
1. SEQ=4253, SYN, Data=0B  
2. SEQ=312, SYN, Data=0B, ACK=4254  
3. SEQ=4254, Data=0B, ACK=313  
4. SEQ=4254, Data=980B, ACK=313  
5. SEQ=313, Data=1456B, ACK=5234  
```

d)* Fill in the following TCP header with the data from the first segment that your computer sends. The number system used must be visible. Note: You will find another form at the end of the exam. However, indicate which one should be graded.  
```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
3645 80  
(10) (10)  
3  
4253  
(10)  
0  
6(10) 0 0 0 0 0 1 0 10192(10)  
00000010 | 00000100 | 1456(10)  
```

### Task 4  
**Dormitory Network (18 Points)**  
Given is a student dormitory with several buildings, whose network is built over Ethernet and IPv4. Each household has its own private /24 prefix. The house network for house x is described by the prefix 10.0.x.0/24. All residents of a house are connected to each other via a switch that is connected to the respective gateway of the house. These routers are interconnected via the transport network 10.0.255.0/24. MAC addresses of all interfaces are structured as follows:  
```
IP: a.b.c.d MAC: 00:53:00:00:c:d
```
A snippet of the network is given in Figure 4.1. The caches of all devices are empty at the beginning.  

```
eth0: 10.0.1.254  
eth0: 10.0.1.1 wan1: 10.0.255.1 heth0: 10.0.2.1  
Resident 1,1 10.0.2.254:eth0 2,1  
10.0.255.2:wan1  
eth0 eth0  
P1 Transport network 10.0.255.0/24  
··· eth0 wan1 rwan1 eth0 ···  
P2 P3  
R1 R2  
P4  
eth0 eth0  
wan1  
Resident 1,2 2,2  
R3  
eth0: 10.0.1.2  
eth0: 10.0.2.2  
eth0  
House 1 House 2  
···  
10.0.1.0/24 10.0.2.0/24  
House 3  
10.0.3.0/24  
eth0: 10.0.3.254 wan1: 10.0.255.3  
```
**Figure 4.1: Snippet of the dormitory network**  

a)* Assign IP addresses to all devices shown in Figure 4.1 according to the assigned prefixes. In the house networks, clients receive the smallest possible address lexicographically sorted, routers the largest. In the transport network, routers receive the smallest possible addresses lexicographically ascending to the house number. Draw the IP addresses directly into the above graphic.  

b)* We first consider internal communication within house 1. Resident 1,1 wants to ping resident 1,2 and only knows their IP address.  
Why can't the corresponding ICMP Echo Request be sent directly?  
- The MAC address of resident 1,2 is not known.  

c)* Provide the source and destination MAC addresses of this first packet.  
- SRC-MAC: 00:53:00:00:01:01  
- DST-MAC: ff:ff:ff:ff:ff:ff  

Now we consider inter-house communication. A resident from house 1 wants to send a ping to a resident from house 2. For this, the routing tables of R1 and R2 must first be configured.  
d)* What would happen if the tables were not configured?  
- Since there are no entries, the router will discard the packet and send back an ICMP "Destination Unreachable".  

e)* Provide all necessary entries in the tables below for R1 and R2 so that all 3 houses can communicate with each other. Summarize individual routes as much as possible.  
**Note:** Not all table rows may be needed.  

**Routing Table of R1**  
```
Destination        Next Hop        Iface  
10.0.1.0/24       0.0.0.0        eth0  
10.0.255.0/24    0.0.0.0        wan1  
10.0.2.0/24      10.0.255.2     wan1  
10.0.3.0/24      10.0.255.3     wan1  
```

**Routing Table of R2**  
```
Destination        Next Hop        Iface  
10.0.2.0/24       0.0.0.0        eth0  
10.0.255.0/24    0.0.0.0        wan1  
10.0.1.0/24      10.0.255.1     wan1  
10.0.3.0/24      10.0.255.3     wan1  
```

f)* The ping should now be sent. How many ARP requests must be sent in total at a minimum?  
- 3: Resident 1,1 → R1, R1 → R2, Resident 2,2  

Now we consider sending the actual Echo Requests (without ARP requests).  
g)* Provide the corresponding header fields for this packet in the table at the marked points P1 to P4. You can use the following notation: MAC(k.iface) for the MAC address of interface iface of node k, similarly IP(k.iface) for the IP address. Residents can be abbreviated with Bx,y.  

```
SRC-MAC                DST-MAC                SRC-IP                DST-IP                TTL  
P1  00:53:00:00:01:01 (MAC(B1,1))  00:53:00:00:01:fe (MAC(R1.eth0))  10.0.1.1 (IP(B1,1))  10.0.2.2 (IP(B2,2))  64  
P2  00:53:00:00:01:01 (MAC(B1,1))  00:53:00:00:01:fe (MAC(R1.eth0))  10.0.1.1 (IP(B1,1))  10.0.2.2 (IP(B2,2))  64  
P3  00:53:00:00:ff:01 (MAC(R1.wan1))  00:53:00:00:ff:02 (MAC(R2.wan1))  10.0.1.1 (IP(B1,1))  10.0.2.2 (IP(B2,2))  63  
P4  00:53:00:00:02:fe (MAC(R2.eth0))  00:53:00:00:02:02 (MAC(B2,2))  10.0.1.1 (IP(B1,1))  10.0.2.2 (IP(B2,2))  62  
```

Finally, we consider house 3. It has 15 residents.  
h)* Provide the largest possible prefix length so that each resident can still be assigned an address. Provide the calculation.  
- 32 - ceil(log2(15 + 1 (network address) + 1 (broadcast address))) = 32 - 5 = 27  

### Task 5  
**Wireshark (14 Points)**  
Given is your Ethernet frame from Figure 5.1, which is to be analyzed below.  

```
0x00 00 00 0d b9 3e cb 48 0c c4 7a 80 52 5b 08 00 45 10  
0x0010 00 4d e7 79 40 00 40 06 36 bf 83 9f 14 d6 83 9f  
0x0020 00 4e c4 10 00 19 79 2e a6 0b 61 49 62 47 50 18  
0x0030 00 3f 1c a2 00 00 45 48 4c 4f 20 69 6f 77 61 2e  
0x0040 6e 65 74 2e 69 6e 2e 74 75 6d 2e 64 65 0d 0a  
```
**Figure 5.1: Ethernet frame including checksum**  

Note that justifications are required for subsequent parts. Ensure that markings can be uniquely assigned to individual sub-tasks. Unverifiable statements will not be graded.  

a)* Mark the sender address in Figure 5.1 on layer 2. (without justification)  

b)* Mark the recipient address in Figure 5.1 on layer 2. (without justification)  

c)* What type is the L3-PDU?  
- Type: IPv4  
- Justification: Ethertype 0x0800  

d)* Provide the sender address on layer 3 in its usual and possibly shortened notation.  
- 131.159.20.214  

e)* Provide the recipient address on layer 3 in its usual and possibly shortened notation.  
- 131.159.0.78  

f)* What type is the L4-PDU?  
- Type: TCP  
- Justification: Protocol in the IP header is 0x06  

g)* At what point does the L4-PDU begin?  
- Offset: 0x0022  
- Justification: IHL = 0x5, 20 B IP header/no options  

h)* What L7 protocol is it likely?  
- TCP Destination Port = 25 SMTP  

i)* What is this protocol used for?  
- For exchanging emails between MTAs.  

j)* At what point does the L7-PDU begin?  
- Offset: 0x0036  
- Justification: Offset = 0x5, 20 B TCP header/no options  

k)* Decode the sent command (the first 4 B of the L7-SDU).  
- ASCII-encoded string from offset 0x0036: 0x45 0x48 0x4c 0x4f = EHLO  

### Task 6  
**Socket Programming (11 Points)**  
The following sub-task is ungraded. It helps us better assess practical parts of the course and their effectiveness on learning success.  

a)* Did you participate in the live programming (July 11/12) in which we implemented the UDP chat or TCP chat?  
- yes  
- no  
- Recording from 2021 viewed  
- No information  

The following sub-tasks refer to the aforementioned live programming.  

b)* What is the purpose of the syscall bind()?  
- It associates a socket with an address structure that specifies the sender port and IP for outgoing packets. In the case of a passive socket, it specifies on which port and which IP addresses packets are expected for a connection builder.  

c)* Explain what happens and why when using listen() together with a UDP socket.  
- Using listen() with connectionless protocols like UDP makes no sense, as there is no connection establishment and thus no passive socket is needed. An error will occur at runtime (-1) and errno will be set to EOPNOTSUPP.  

d)* How many sockets does a TCP server need to communicate with a single client, and what are they specifically used for?  
- 2 sockets are needed:  
  - One socket for sending and receiving data, and another (passive) socket on which the server waits for incoming connections.  

e)* What happens when using connect() with a UDP socket?  
- You specify the IP address and port to which data is sent or from which it is received. You can then particularly use a UDP socket with send().  

f)* Explain the function of the syscall select().  
- Essential parameter: monitored FD sets (maximum FD, optional timeout)  
- Return value(s): number of ready FDs or -1 in case of error, modified FD set with ready FDs  

### Task 7  
**James Webb Space Telescope (14 Points)**  
The James Webb Space Telescope (JWST) was launched on December 25, 2021, and reached its destination – the 1.5 million km distant Lagrange point L1 – on January 24, 2022.  

a)* Determine the average travel speed of the JWST in m/s. (Assume that both the launch day and the day of arrival count towards travel time.)  
- 7 days travel time in 2021 + 24 days travel time in 2022 = 31 days  
- v = (1.5 * 10^9 m) / (31 * 24 * 3600 s) ≈ 560.04 m/s  

The JWST generates 235 Gbit of research data daily, which is temporarily stored on a 68 GB SSD.  

b)* Determine the maximum time the JWST can work without transmitting data to Earth. (Assume that the full capacity of the SSD is available.)  
- T = (68 * 10^9 bits) / (235 Gbit) ≈ 2.31 days (= 55.56 hours)  

To transmit the research data to Earth, a channel in the 25.9 GHz band (so-called K-band) is used. The maximum data rate in the downlink direction to Earth is 28 Mbit/s. However, the ground stations on Earth are only reachable for 4 hours each.  

c)* Determine the daily achievable data volume in GB and GiB that can be transmitted to Earth, provided no further overhead is incurred.  
- V = 28 Mbit/s * 4 * 3600 s = 403.20 Gbit = 50.40 GB = 46.94 GiB  

d)* The modulation method used is 4-PSK. Draw a signal space assignment including labeling that can be uniquely assigned to this modulation method.  

e)* Based on the previous information, determine the minimum necessary channel bandwidth to achieve the given transmission rate.  
- 4-PSK uses M = 4 distinguishable symbols. We obtain according to Hartley:  
- B ≥ (r / (2 * log2(M)))  
- B ≥ 7 MHz  

f)* An SNR of 20 dB is expected at the ground station. Determine the minimum necessary bandwidth of the channel under this condition.  
- First, the given SNR in dB is calculated:  
- SNR = 10 * log10(SNR)  
- SNR = 10^(SNRdB/10) = 0.01  
Now we can determine the bandwidth according to Shannon/Hartley:  
- B ≥ (r / (log2(1 + SNR))) ≈ 1.95 GHz  

g)* Briefly justify which of the two channel bandwidths will be decisive.  
- Although according to Shannon a channel with 7 MHz bandwidth would be sufficient, according to Hartley it would not work with the given modulation method. Accordingly, the bandwidth determined by Hartley is the theoretical minimum.  

### Additional Form for Task 3  
- Page 12/12 -