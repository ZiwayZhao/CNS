# Chair of Network Architectures and Services
School of Computation, Information and Technology  
Technical University of Munich  

## Notes on Personalization:
- Your exam will be identified during attendance control by attaching a code persona sticker.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID to be affixed next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

## Fundamentals of Computer Networks and Distributed Systems
Exam: IN0010/Retake  
Date: Friday, October 4, 2024  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 11:00–12:30  

### Instructions for Processing
- This exam consists of 16 pages with a total of 7 tasks as well as the known cheatsheet. Please check now that you have received a complete set of documents.
- The total score for this exam is 90 points.
- It is prohibited to tear out pages from the exam.
- The following aids are permitted:
  - A non-programmable calculator
  - An analog dictionary German ↔ native language without annotations
  - The cheatsheet distributed with the exam
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be graded where the solution path is recognizable. Text tasks must be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write in red/green colors or with pencil.
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.

## Task 1
### Multiple Choice (18 Points)
The following sub-tasks are multiple choice/multiple answer, meaning that at least one answer option is correct for each. Sub-tasks with only one correct answer are graded with 1 point if correct. Sub-tasks with more than one correct answer are graded with 1 point for each correct answer and -1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.

### Mark the correct answers
- Answers can be crossed out by complete filling.
- Crossed-out answers can be re-marked with adjacent markers.

a) *1f 00 is the hexadecimal representation for the number 7936 in which byte order?  
- Little-Endian  
- Low-Endian  
- Middle-Endian  
- Big-Endian  
- AS-Byte-Order  
- Cloud-Byte-Order  
- Network-Byte-Order  
- Host-Byte-Order  

b) *Which of the following options represent digital modulation methods learned in the lecture?  
- ASP  
- NRZ  
- QAP  
- QRM  
- Low-pass filter  
- None  
- QMP  
- ASF  
- TSA  
- Carrier pigeon  

c) *Which character has the highest information content in the following character string?  
- ABBACCADDAEEAGHG  
- G  
- E  
- D  
- A  
- B  
- C  
- H  

d) *Which node corresponding to the characters in the above string would have the least depth in the associated Huffman tree?  
- H  
- A  
- B  
- E  
- D  
- C  
- G  

e) *Which statements about IEEE 802.11 Access Points (APs) are correct?  
- APs are generally addressed directly.  
- APs are transparent for participants outside the wired network.  
- APs are only transparent within the wireless network.  
- APs are transparent for all participants.  

f) *How many usable host IPv4 addresses are in the prefix 193.77.96.0/19?  
- 524286  
- <32  
- 1022  
- 510  
- 524288  
- >1032  
- 1024  
- 512  
- 8190  
- 8192  

g) *What properties does IPv6 have compared to IPv4?  
- No fragmentation at routers  
- Fixed header size  
- Automatic MAC assignment via SLAAC  
- No L4 protocol needed  
- Longest-prefix matching possible  
- Smaller address space  
- 264 times larger address space  
- No switches needed  

h) Which of the following statements regarding the IP address eff02::1:ffae:57d0 are correct?  
- The IP is a loopback address.  
- The IP is a multicast address.  
- The IP is a unicast address.  
- The IP is an IPv5 address.  
- The IP is a broadcast address.  
- The IP is a historical relic from the early days of the Internet.  

i) *Which header fields are always modified by a classic NAT for outgoing packets?  
- Protocol  
- Dst-Port  
- Src-Port  
- Dst-IP  
- Src-IP  

j) *What properties does UDP have?  
- The send window is dynamically adjusted.  
- There are flow control mechanisms.  
- Acknowledgments are sent.  
- Cannot be transmitted via IPv6.  
- The receive window is dynamically adjusted.  
- Stream-oriented.  
- Messages can arrive and be processed in a different order.  
- Message-oriented congestion control.  

k) *The simplified TCP Reno congestion control algorithm presented in the lecture is in the Congestion Avoidance Phase. All segments of the send window have been acknowledged. What happens?  
- The congestion control window remains unchanged.  
- The congestion control window is set to the threshold for congestion avoidance.  
- The threshold for congestion avoidance is set to half the current window size.  
- The congestion control window is set to an MSS.  
- The congestion control window is halved.  
- The algorithm enters slow start.  
- The congestion control window is increased by an MSS.  
- The algorithm remains in the CA phase.  

l) *The simplified TCP Reno congestion control algorithm presented in the lecture is in the Congestion Avoidance Phase. A timeout occurs. What happens?  
- The congestion control window is set to the threshold for congestion avoidance.  
- The algorithm remains in the CA phase.  
- The congestion control window is halved.  
- The algorithm enters slow start.  
- The congestion control window is set to an MSS.  
- The congestion control window remains unchanged.  
- The congestion control window is increased by an MSS.  
- The threshold for congestion avoidance is set to half the current window size.  

## Task 2
### EKG Frequency Analysis (14 Points)
We want to determine the spectrum of a signal. The signal \( s(t) \) consists of periodic repetitions of the basic pulse \( g(t) \) with a period duration \( T = 2 \).

\[
g(t) = 
\begin{cases} 
2At + A & -1 \leq t \leq 0 \\ 
2At - A & 0 < t \leq 1 \\ 
0 & \text{otherwise} 
\end{cases}
\]

a) *Sketch the periodic signal \( s(t) \) in the following coordinate system.  

b) *Indicate which method can be used to determine the spectrum of \( s(t) \). Justify your decision.  
- Fourier series  
- Fourier transformation  

c) *Determine the DC component of \( s(t) \) through calculation or justification.  

d) *Mark the correct statements and justify your choice in the following box.  
**Note:** Without justifications, there are no points for the marks!  
- \( \forall N \, a_k = 0 \)  
- \( \exists N \, a_k \neq 0 \)  

\[
b_k = 2A \int_{-1}^{1} \sin(k\pi t) dt - 2 \int_{0}^{1} \sin(k\pi t) dt \tag{2.1}
\]

When calculating the sine components, the intermediate result from formula 2.1 is achievable.  

e) *Provide the calculation path to the intermediate result 2.1 and briefly explain non-obvious calculation steps.  

## Task 3
### Addressing (5 Points)
Given is the following topology. The PC sends a request to the server, and we consider the response from the server to the PC and the three points P1, P2, and P3. Router R2 operates NAT and changes addresses and ports accordingly when forwarding to the private network to the PC.

```
S 
R1 R2(NAT) 
PC
eth0 eth1 wan5 wan3 eth2 eth0
P1 P2 P3
```

#### Figure 3.1: Network Topology

a) *Fill in the following table with the Ethernet and IP addresses of the frame or packet as they would be observed at each point. Use the notation Device.Interface.Address for MAC and IP addresses, e.g., PC3.eth0.MAC.

| SRC-MAC | DST-MAC | SRC-IP | DST-IP |
|---------|---------|--------|--------|
| P1      |         |        |        |
| P2      |         |        |        |
| P3      |         |        |        |

b) *Assuming TTL is set to 4. Briefly justify whether the packet will arrive at the PC.  

c) *The networks 10.222.15.128/26 and 10.222.15.192/26 are summarized. Name the resulting network address in CIDR notation.  

## Task 4
### Legend of the Galactic High-Speed Satellite Communication (12 Points)
You work in intergalactic telecommunications and are to plan the dimensioning of a new satellite transmission link between the planets Odin and Fezzan. Your competitor FezzSat has already realized this connection with satellites of the same type.

The following information is known:
- The satellites support a maximum frame size including header of 2304B.
- The distance between Odin and Fezzan is 7000 Lj (1 year is 365 days). [a]

### Determination of the Error Rate
Your boss wants to save money and plans to use \( N = 99 \) satellites equidistantly between the sending and receiving station. Thus, there will be a total of 100 transmissions. Let \( p(d) \) be the bit error probability for the transmission from one satellite to another, which is defined as a function of the satellite distance \( d \).

a) *Let \( X \) be the random variable that indicates the number of bit errors in the transmission of a maximum-sized packet between two satellites. Provide the distribution of the random variable \( X \) including distribution parameters as a function of \( p(d) \).  

b) What is the probability that a maximum-sized packet arrives perfectly at the next satellite? Use the following definition of \( p(d) \) and provide the result in percentage.  

\[
p(d) = 10^{-320/d} \text{ Lj}
\]

c) Is it therefore sensible to operate with a failure probability from sub-task b) with 99 satellites? Justify briefly.  
**[a]** 1 Lj is the distance light travels in a vacuum in exactly one year.

### Structure of Transmission Duration in Packet Switching
To better understand how the total transmission duration of a data volume \( L \) in packet switching comes about, you should illustrate this with a concrete example with 5 packets and 4 satellites.

The following times are relevant for the total transmission duration:
1. Serialization time \( t_s \)
2. Propagation delay \( t_p \)
3. Delay of data transmission at each satellite \( t_z \)

d) Mark the above durations at appropriate places in the schematic representation of packet transmission in Figure 4.1.  

```
Start rs1 rs2 ... rs3 rs4 Target
```

#### Figure 4.1: Schematic Representation of the Transmission of 5 Packets over 4 Satellites. If you use both templates, do not correct the strikethroughs!

### Estimation of the Number of Satellites
Your boss wants to know how many satellites FezzSat is approximately using. To determine this, your acquaintance sent a test file of size \( L = 6 \text{ MiB} \) over the satellite network of FezzSat, which was exclusively booked for this test.

From this test and further research, you could find the following information:
- The distance between Odin and Fezzan is 7000 Lj (1 year is 365 days).
- The total transmission took \( T = 26755.66 \text{ s} \) according to your measurements.
- The data was divided into a total of \( N = 3101 \) packets.
- The delay of data transmission for each satellite is \( t_z = 384 \text{ s} \).
- The relative propagation delay of the connections is \( \nu = 8.76 \times 10^6 \). [b]
- The header size of the packets is \( L_H = 275 \text{ B} \).
- Each transmission link sends at a transmission rate of \( r = 42 \text{ kbit/s} \).

e) *Calculate the propagation delay over the entire communication path.  

f) How long does the serialization of all packets at the sender take?  

g) How many satellites does FezzSat approximately use? Round to the nearest whole number.  
**[b]** Thus, this is a superluminal transmission.

## Task 5
### Wiretap Shark (15 Points)
Given is the Ethernet frame (without FCS) from Figure 5.1, which is to be analyzed.

```
0x0000 b4 96 f4 ae 80 6c 30 61 08 06 08 00 86 dd 60 07
0x0010 45 3d 00 30 06 40 20 01 4c a0 20 01 00 00 07 32
0x0020 00 00 00 00 dc 91 20 01 4c a0 20 01 00 00 02 16
0x0030 3e ff fe 52 ed 14 e2 74 00 19 e9 07 92 c5 5b 0b
0x0040 53 5a 80 18 01 fb ee b8 00 00 01 01 08 0a b8 ba
0x0050 4a 00 2b cf d4 80 45 48 4c 4f 20 67 72 6e 76 73
0x0060 2e 6e 65 74 0d 0a
```

#### Figure 5.1: Ethernet Frame (without FCS)

Note that justifications are required for the following sub-tasks. Ensure that markings can be uniquely assigned to individual sub-tasks. Unsubstantiated statements will not be graded.

a) *Mark the sender address in Figure 5.1 at Layer 2. (without justification)  

b) *Mark the recipient address in Figure 5.1 at Layer 2. (without justification)  

c) What type is the L3-PDU?  
- Type:  
- Justification:  

d) Provide the sender address at Layer 3 in its usual, possibly shortened notation.  

e) Provide the recipient address at Layer 3 in its usual, possibly shortened notation.  

f) Justify through which mechanism the recipient address at Layer 3 was presumably assigned.  

g) What type is the L4-PDU?  
- Type:  
- Justification:  

h) At which point in the frame does the L4-PDU begin?  
- Offset:  
- Justification:  

i) What L7 protocol is likely being used?  
- Protocol:  
- Justification:  

j) At which point in the frame does the L7-PDU begin?  
- Offset:  
- Justification:  

k) Decode the first 4 bytes of the L7 payload.  
**Note:** This is a text-based protocol (ASCII).  

l) What is the L7 protocol used for?  

## Task 6
### DNS (14.5 Points)
You have heard from fellow students that solutions to exams can be found at grnvs.tum.de. In the hope of finding the solution to this year's retake, you call up the website in your browser. You are in a small home network and router R1 is connected to the Internet. Via DHCP, R1 configures itself as the standard resolver on your laptop C1. R1 has R2 registered as a resolver.

```
dns50.t-ipnet.de. a.root-servers.net.
I R I R
Client C1 Switch S1 Router R1 a.nic.de.
I R I R I R I R
Internet
```

#### Example Drawing B1
```
1 2 dns1.lrz.de.
I R
A B C
4 3 Public Resolver R2 grnvs.tum.de.
I R I R
```

#### Figure 6.1: Simplified Internet Topology

a) *Draw all DNS requests and responses in Figure 6.1 that are necessary for the name resolution of grnvs.tum.de. Draw arrows and number them in the order of occurrence as in Example Drawing B1. Assume that all caches are empty. You know:
1. a.nic.de is the authoritative nameserver for the zone.
2. dns1.lrz.de is the authoritative nameserver for the zone tum.de.  

You will find an additional template at the end of the exam in Figure 7.2.

b) Mark for the used network components whether they resolve DNS requests iteratively (I) or recursively (R) by crossing the respective field. Justify your choice.  

c) *How can the resolver make the request to dns1.lrz.de without having to resolve the domain explicitly beforehand?  

You are a working student and have been tasked with creating a zone file for grnvs.net. Fill in the following zone file so that the requirements of the individual sub-tasks are met. The beginning of the zone file is already given (the SOA record is abbreviated for simplicity).

```
$TTL 86400 ; 1 day
grnvs.net. IN SOA ns.grnvs.net. info.grnvs.net. [...]
grnvs.net. NS ns.grnvs.net.
```

d) *ns.grnvs.net is already registered as the primary nameserver of the zone. To ensure redundancy, the server dns2.lrz.de will act as a secondary nameserver. Please enter this.  

e) *The primary nameserver should be reachable at the IP address 95.217.202.138.  

f) *When someone calls grnvs.net in their browser, the GRNVS website should be displayed. The corresponding web server has the IP addresses 188.95.232.10 and 2a00:4700:0:9:f::.  

g) *To allow students to send an email to info@grnvs.net, an email server must be registered. To avoid having to operate this oneself, only the LRZ email service postrelay1.lrz.de should be used with priority 10.  

h) *In the upcoming semester, GRNVS merchandise and bonus points will be sold. To avoid having to operate one's own online shop, shop.grnvs.net should serve as an alias for grnvs.myshopify.com.  

## Task 7
### Short Tasks (11.5 Points)
The following short tasks can be solved independently of each other.

a) *Given is the following IPv6 address: fe80::2788:1fff:feae:3c4a. What is the corresponding Solicited Node Address and the Multicast MAC Address?  
- Solicited Node Address:  
- Multicast MAC Address:  

b) *Name four multiplexing methods regarding media access presented in the lecture.  

c) *Mark the collision domains in Figure 7.1.  

d) *Mark the broadcast domains in Figure 7.1.  

#### (a) Collision Domains  
#### (b) Broadcast Domains  
#### Figure 7.1: Network Topology  

e) We consider the TCP header of an HTTPS connection, where this is the first packet from the client to the server after the TCP handshake. However, something seems inconsistent in the header. Mark all errors in the header and correct them. Use sensible values where necessary.  

```
0 80
11258
521
6 Reserved URG 1 PSH RST 1 0 (Receive) Window
Checksum Urgent Pointer
HTTPS payload
```

f) Provide the correct order of all necessary socket method calls for a TCP connection. A message should be sent from a client to a server.  

### Additional Space for Solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to strike out invalid solutions.