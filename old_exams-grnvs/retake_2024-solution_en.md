# Chair of Network Architectures and Services
School of Computation, Information and Technology  
Technical University of Munich

## Notes on Personalization:
- Your exam will be personalized during attendance control by affixing a code sticker.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID to be affixed next to the signature field.
- This will be used as a pseudonym to allow a unique assignment of your exam.

## Basics of Computer Networks and Distributed Systems
### Exam: IN0010/Retake 
**Date:** Friday, October 4, 2024  
**Examiner:** Prof. Dr.-Ing. Georg Carle  
**Time:** 11:00–12:30  

### Instructions for Completion
- This exam consists of 16 pages with a total of 7 tasks as well as the known cheat sheet. Please check now that you have received a complete set of information.
- The total score for this exam is 90 points.
- Removing pages from the exam is prohibited.
- The following aids are permitted:
  - A non-programmable calculator
  - An analog dictionary German ↔ native language without annotations
  - The cheat sheet distributed with the exam
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be scored where the solution path is recognizable. Text tasks must generally be justified unless expressly marked otherwise in the respective sub-tasks.
- Please do not write in red/green colors or with pencil.
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.

---

## Task 1
### Multiple Choice (18 Points)
The following sub-tasks are multiple choice/multiple answer, meaning at least one answer option is correct for each. Sub-tasks with only one correct answer will be scored with 1 point if correct. Sub-tasks with more than one correct answer will be scored with 1 point for each correct answer and -1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.

Please mark the correct answers.

- Marked answers can be crossed out by completely filling in.
- Crossed-out answers can be marked again by adjacent markings.

1. **What is the hexadecimal representation for the number 7936 in which byte order?**
   - Little-Endian
   - Low-Endian
   - Middle-Endian
   - Big-Endian
   - AS-Byte-Order
   - Cloud-Byte-Order
   - Network-Byte-Order
   - Host-Byte-Order

2. **Which of the following options represent digital modulation methods learned in the lecture?**
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

3. **Which character has the highest information content in the following character string?**
   - ABBACCADDAEEAGHG
   - G
   - E
   - D
   - A
   - B
   - C
   - H

4. **Which node in the corresponding Huffman tree would have the least depth for the character from the above string?**
   - H
   - A
   - B
   - E
   - D
   - C
   - G

5. **Which statements about IEEE 802.11 Access Points (APs) are correct?**
   - APs are generally directly addressed.
   - APs are transparent for participants outside the wired network.
   - APs are only transparent within the wireless network.
   - APs are transparent for all participants.

6. **How many usable host IPv4 addresses are in the prefix 193.77.96.0/19?**
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

7. **What properties does IPv6 have compared to IPv4?**
   - No fragmentation at routers
   - Fixed header size
   - Automatic MAC assignment via SLAAC
   - No L4 protocol needed
   - Longest-prefix matching possible
   - Smaller address space
   - 264 times larger address space
   - No switches needed

8. **Which of the following statements regarding the IP address ff02::1:ffae:57d0 are correct?**
   - The IP is a loopback address.
   - The IP is a multicast address.
   - The IP is a unicast address.
   - The IP is an IPv5 address.
   - The IP is a broadcast address.
   - The IP is a historical relic from the early days of the Internet.

9. **Which header fields are always changed by a classical NAT in outgoing packets?**
   - Protocol
   - Dst-Port
   - Src-Port
   - Dst-IP
   - Src-IP

10. **What properties does UDP have?**
    - The send window is dynamically adjusted.
    - There are flow control mechanisms.
    - Acknowledgments are sent.
    - Cannot be transmitted via IPv6.
    - The receive window is dynamically adjusted.
    - Stream-oriented.
    - Messages can arrive and be processed in a different order.
    - Message-oriented.
    - Congestion control mechanisms.

11. **The simplified TCP-Reno congestion control algorithm presented in the lecture is in the Congestion Avoidance Phase. All segments of the send window have been acknowledged. What happens?**
    - The congestion control window remains unchanged.
    - The congestion control window is set to the threshold for congestion avoidance.
    - The threshold for congestion avoidance is set to half the current window size.
    - The congestion control window is set to an MSS.
    - The congestion control window is halved.
    - The algorithm goes into slow start.
    - The congestion control window is increased by an MSS.
    - The algorithm remains in the CA phase.

12. **The simplified TCP-Reno congestion control algorithm presented in the lecture is in the Congestion Avoidance Phase. A timeout occurs. What happens?**
    - The congestion control window is set to the threshold for congestion avoidance.
    - The algorithm remains in the CA phase.
    - The congestion control window is halved.
    - The algorithm goes into slow start.
    - The congestion control window remains unchanged.
    - The congestion control window is increased by an MSS.
    - The threshold for congestion avoidance is set to half the current window size.

---

## Task 2
### EKG Frequency Analysis (14 Points)
We want to determine the spectrum of a signal. The signal \( s(t) \) consists of periodic repetitions of the basic impulse \( g(t) \) with a period duration \( T = 2 \).

\[
g(t) = 
\begin{cases} 
2At + A & -1 \leq t \leq 0 \\ 
2At - A & 0 < t \leq 1 \\ 
0 & \text{otherwise} 
\end{cases}
\]

1. **Sketch the periodic signal \( s(t) \) in the following coordinate system.**

2. **Indicate which method can be used to determine the spectrum of \( s(t) \). Justify your decision.**
   - Fourier series
   - Fourier transformation

   The Fourier transformation can be used for all signals. The Fourier series can only be used for periodic signals, which is possible here since \( s(t) \) is the periodically repeated basic impulse.

3. **Determine the DC component of \( s(t) \) through calculation or justification.**
   - The DC component \( a_0 \) is 0. This is evident since the areas above and below the t-axis are equal. Thus, the value 0 is the best constant approximation of the signal \( s(t) \).

4. **Mark correct statements and justify your choice in the following box briefly.**
   - \( \forall N: a_k = 0 \)
   - \( \exists N: a_k \neq 0 \)

   Since \( s(t) \) is point-symmetric about the origin, the sine components suffice to represent the signal. Thus, the cosine components are all equal to 0.

5. **Provide the calculation path to the intermediate result and briefly explain non-obvious calculation steps.**
   \[
   b_k = \int_{-T/2}^{T/2} s(t) \sin(k \omega t) dt
   \]
   \[
   = \int_{0}^{1} (2At + A) \cdot \sin(k \pi t) dt + \int_{1}^{2} (2At - A) \cdot \sin(k \pi t) dt
   \]

   - The piecewise definition of \( s(t) \) allows us to substitute the definition into the integral and split it into the different definition ranges. The "otherwise" part has an area of 0 and was therefore omitted.
   - To simplify the calculation, the factor \( A \) was taken out of the integrals. The linear factors of the sine were multiplied out and split into two integrals each.
   - Since the value ranges of the integrals (a) and (c) follow directly one after the other, they can be combined into the integral.

---

## Task 3
### Addressing (5 Points)
Given is the following topology. The PC sends a request to the server, and we consider the response from the server to the PC and the three points P1, P2, and P3. Router R2 operates NAT and accordingly changes addresses and ports when forwarding to the private network to the PC.

```
S R1 R2(NAT) PC
eth0 eth1 wan5 wan3 eth2 eth0
P1 P2 P3
```

1. **Fill in the following table with the Ethernet and IP addresses of the frame or packet as observed at each point. Use the notation Device.Interface.Address, e.g., PC3.eth0.MAC.**

| SRC-MAC              | DST-MAC              | SRC-IP              | DST-IP              |
|----------------------|----------------------|----------------------|----------------------|
| P1 S.eth0.MAC       | R1.eth1.MAC         | S.eth0.IP           | R2.wan3.IP          |
| P2 R1.wan5.MAC      | R2.wan3.MAC         | S.eth0.IP           | R2.wan3.IP          |
| P3 R2.eth2.MAC      | PC.eth0.MAC         | S.eth0.IP           | PC.eth0.IP          |

2. **Assuming you choose a TTL value of 4. Briefly justify whether the packet arrives at the PC.**
   - Yes, only two routers are on the way from S to PC, and the PC successfully receives the packet with TTL 2.

3. **The networks 10.222.15.128/26 and 10.222.15.192/26 are summarized. Name the resulting network address in CIDR notation.**
   - 10.222.15.128/25

---

## Task 4
### Legend of the Galactic High-Speed Satellite Communication (12 Points)
You work at the intergalactic telecom and are to plan the dimensioning of a new satellite transmission link between the planets Odin and Fezzan. Your competitor FezzSat has already realized this connection with satellites of the same type.

The following information is known:
- The satellites support a maximum frame size including header of 2304 B.
- The distance between Odin and Fezzan is 7000 Lj (1 year is 365 days).

#### Determination of the Error Rate
Your boss wants to save money and plans to use N = 99 satellites equidistantly between the send and receive stations. Thus, there are a total of 100 transmissions. Let \( p(d) \) be the bit error probability for transmission from one satellite to another, which is defined as a function of the satellite distance \( d \).

1. **Let \( X \) be the random variable that indicates the number of bit errors in the transmission of a maximum-sized packet between two satellites. Provide the distribution of the random variable \( X \) including distribution parameters as a function of \( p(d) \).**
   - \( X \sim \text{Bin}(2304 \cdot 8, p) \)

2. **What is the probability that a maximum-sized packet arrives perfectly at the next satellite? Use the following definition of \( p(d) \) and provide the result in percentage.**
   - \( p(d) = 10^{-320} \)

   We seek \( P[X = 0] \):
   \[
   P[X = n] = \binom{2304 \cdot 8}{n} p^n (1 - p)^{2304 \cdot 8 - n}
   \]
   \[
   P[X = 0] = (1 - p)^{2304 \cdot 8} \approx 60.99\%
   \]

3. **Is it sensible to operate with an error probability from part b) with 99 satellites? Justify briefly.**
   - No, because the probability that the packet passes all satellites without transmission errors would be too small with \( P[X = 0] < 0.005 \).

---

## Task 5
### Wire Post Shark (15 Points)
Given is the Ethernet frame (without FCS) from Figure 5.1, which is to be analyzed.

```
0x0000 b4 96 f4 ae 80 6c 30 61 08 06 08 00 86 dd 60 07
0x0010 45 3d 00 30 06 40 20 01 4c a0 20 01 00 00 07 32
0x0020 00 00 00 00 dc 91 20 01 4c a0 20 01 00 00 02 16
0x0030 3e ff fe 52 ed 14 e2 74 00 19 e9 07 92 c5 5b 0b
0x0040 53 5a 80 18 01 fb ee b8 00 00 01 01h08 0a b8 ba
0x0050 4a 00 2b cf d4 80 45 48 4c 4f 20 67 72 6e 76 73
0x0060 2e 6e 65 74 0d 0a
```

**Note:** For the following sub-tasks, justifications are required. Ensure that markings can be uniquely assigned to individual sub-tasks. Non-verifiable statements will not be evaluated.

1. **Mark the sender address in Figure 5.1 at Layer 2. (no justification required)**

2. **Mark the recipient address in Figure 5.1 at Layer 2. (no justification required)**

3. **What type is the L3-PDU?**
   - Type: IPv6
   - Justification: Ethertype 0x86dd

4. **Provide the sender address at Layer 3 in its usual, possibly shortened notation.**
   - 2001:4ca0:2001:0:732::dc91

5. **Provide the recipient address at Layer 3 in its usual, possibly shortened notation.**
   - 2001:4ca0:2001:0:216:3eff:fe52:ed14

6. **Justify through which mechanism the recipient address at Layer 3 was likely assigned.**
   - SLAAC, as the sender address contains the modified EUI-64 identifier generated from the sender MAC address.

7. **What type is the L4-PDU?**
   - Type: TCP
   - Justification: Next Header field in the IP header is 0x06

8. **At which point in the frame does the L4-PDU begin?**
   - Offset: 0x0036
   - Justification: Next Header = TCP ⇒ 40B IP Header/no Extension Header

9. **Which L7 protocol is it likely?**
   - Protocol: SMTP
   - Justification: TCP Destination Port 0x0019 = (25)

10. **At which point in the frame does the L7-PDU begin?**
    - Offset: 0x0056
    - Justification: Offset = 0x8 (4-bit field) ⇒ 32B TCP Header (with options)

11. **What is the L7 protocol used for?**
    - To transfer emails to an MTA.

---

## Task 6
### DNS (14.5 Points)
You have heard from fellow students that exam solutions can be found at grnvs.tum.de. In the hope of finding the solution to this year's retake, you call up the website in your browser. You are in a small home network, and router R1 is connected to the Internet. Via DHCP, R1 configures itself as the standard resolver on your laptop C1. R1 has R2 registered as a resolver.

1. **Draw all DNS requests and responses in Figure 6.1 that are necessary for the resolution of grnvs.tum.de. Draw arrows and number them in the order of occurrence as in the example drawing B1. Assume that all caches are empty. You know:**
   - 1. a.nic.de is the authoritative nameserver of the zone.
   - 2. dns1.lrz.de is the authoritative nameserver of the zone tum.de.

2. **Mark for the used network components whether they resolve DNS requests iteratively (I) or recursively (R) by crossing the respective field. Justify your choice.**
   - Clients and routers resolve DNS requests recursively, as they generally do not have sufficient resources (connection, computing power, and memory) to perform requests efficiently and cache them. Resolvers and authoritative DNS servers answer requests iteratively by definition.

3. **How can the resolver send the request to dns1.lrz.de without first resolving the domain explicitly?**
   - Through so-called Glue Records, a nameserver can send the IP addresses of another nameserver in addition to the NS record.

You are a working student and have been tasked with creating a zone file for grnvs.net. Fill in the following zone file so that the requirements of the individual sub-tasks are met. The beginning of the zone file is already given (the SOA record is abbreviated for simplicity).

```
$TTL 86400 ; 1 day
grnvs.net. IN SOA ns.grnvs.net. info.grnvs.net. [...] 
grnvs.net. NS ns.grnvs.net.
grnvs.net. NS dns2.lrz.de.
ns.grnvs.net. A 95.217.202.138.
grnvs.net. A 188.95.232.10
grnvs.net. AAAA 2a00:4700:0:9:cf::
grnvs.net. MX 10 postrelay1.lrz.de.
shop.grnvs.net. CNAME grnvs.myshopify.com.
```

---

## Task 7
### Short Tasks (11.5 Points)
The following short tasks are independently solvable.

1. **Given is the following IPv6 address: fe80::2788:1fff:feae:3c4a. What is the corresponding Solicited Node Address as well as the Multicast MAC Address?**
   - Solicited Node Address: ff02::1:ffae:3c4a
   - Multicast MAC Address: 33:33:ff:ae:3c:4a

2. **Name four multiplexing methods regarding media access presented in the lecture.**
   - Time Division Multiplexing (TDM)
   - Frequency Division Multiplexing (FDM)
   - Space Division Multiplexing (SDM)
   - Code Division Multiplexing (CDM)

3. **Mark the collision domains in Figure 7.1.**

4. **Mark the broadcast domains in Figure 7.1.**

5. **We consider the TCP header of an HTTPS connection, where this is the first packet from the client to the server after the TCP handshake. Something seems to be inconsistent in the header. Mark all errors in the header and correct them. Use sensible values where necessary.**

6. **Provide the correct sequence of all necessary socket method calls for a TCP connection. A message should be sent from a client to a server.**
   - Server: socket(), bind(), listen(), accept(), read(), close()
   - Client: socket(), connect(), write(), close()

---

### Additional Space for Solutions
Clearly mark the assignment to the respective sub-task. Do not forget to cross out invalid solutions.