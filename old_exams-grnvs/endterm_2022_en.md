Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be analyzed during the attendance check by sticking a code persona on it.  
- This contains only a continuous number, which is also noted on the attendance sticker with SRID here.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Endterm  
Date: Monday, August 1, 2022  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 10:45–12:15  

**Instructions for Completion:**  
- This exam consists of 12 pages with a total of 7 tasks as well as a formula collection (cheat sheet). Please check now that you have received a complete set of information.  
- The total score for this exam is 91 points.  
- The removal of pages from the exam is prohibited.  
- Allowed aids include:  
  - a non-programmable calculator  
  - an analog dictionary in the native language without notes  
  - the cheat sheet distributed with this exam  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.  

**Additional space for solutions. Clearly mark the assignment to the respective sub-task. Do not forget to cross out invalid solutions.**  
**Leave the lecture hall by / Early submission until**  

---

**Task 1**  
Multiple Choice (19 points)  
The following tasks are multiple choice/multiple answer, meaning that at least one answer option is correct for each. Sub-tasks with only one correct answer will be graded with 1 point if correct. Sub-tasks with more than one correct answer will be graded with 1 point for each correct and 1 point for each incorrect cross. Missing crosses have no effect. The minimum score per sub-task is 0 points.  

**Cross out the correct answers**  
Crosses can be crossed out by fully filling them in.  
Crossed-out answers can be crossed out again by adjacent markings.  

a)* A frame with a total length of 1500 B requires a serialization time of 2 µs. What is the transmission rate of the link?  
6000 GB/s 2 Gbit/s 750 MB/s 2 Mbit/s 750 Mbit/s 1500 Mbit/s  

b)* A frame with a total length of 1500 B is transmitted over a copper line of length 10 km. What propagation delay occurs approximately?  
50 ns 476 µs 33.3 µs 50 µs 33.3 ns 476 ns  

c)* Which of the following properties apply to UDP?  
must not be fragmented stream-oriented  
≥  
works on the transport layer only ports 1024 usable  
datagram-oriented works on the network layer  
only ports <1024 usable connection-oriented  

d)* What is the essential difference between CSMA/CD and CSMA/CA?  
In media access using CSMA/CA, CSMA/CA requires a minimum frame length of 64 B.  
CSMA/CD uses acknowledgments in contrast to CSMA/CA. There are only differences in collision handling, not in media access.  

e)* Which statement(s) about Fourier series and Fourier transformations regarding time-continuous signals are false?  
Using Fourier transformation, the spectrum of non-periodic signals cannot be determined.  
Using Fourier series, the spectrum of non-periodic signals can be determined.  
Using Fourier transformation, the spectrum of periodic signals can be determined.  
Using Fourier series, the spectrum of periodic signals can be determined.  

f)* A packet is a...  
L4-SDU L2-PDU L4-PDU L3-SDU  
L1-PDU L3-PDU L1-SDU L2-SDU  

g)* An interface has the link-local IPv6 address fe80:0000:0000:0000:0312:23ff:fe34:4556. What L2 address does this interface most likely have?  
01:02:03:04:05:06 56:45:34:23:12:01 03:12:23:34:45:56 31:22:3f:ff:e3:44  
23:ff:fe:34:45:56 fe:80:03:12:23:ff 01:12:23:34:45:56 06:05:04:03:02:01  

h)* Which of the following IP addresses are loopback addresses?  
fe80::1234 127.0.0.2 :: 2001:db8::1234  
0.0.0.0 ::2 128.0.0.1 ::1  

i)* How long is an IPv6 address?  
16 B 2128 bit 128 B 2128 B  

j)* Ethernet is a protocol for... in the ISO-OSI model.  
Layer 4 Layer 7 Layer 3 Layer 5  
Layer 6 Layer 1 Layer 2  

k)* Which protocol is not part of the application layer?  
DNS HTTP FTP SNMP  
ICMP HTTPS SSH SMTP  

l)* You observe the following data stream from an unknown source. At which character is the information content maximal?  
H G A A B B A F A G H F G B H A B G A G F B H F  
G B F I A H  

m)* Given the following data in Big-Endian: 0xf3b68745. Which of the following data corresponds to this in Network Byte Order?  
0x4587b6f3 0x3f6b7854 0xf3b68745 0x54786b3f  

n)* What is meant by source coding?  
The removal of redundancy Targeted addition of redundancy  
Representation of data through sequences of signal impulses  
None of the above  

---

**Task 2**  
Short Tasks (6.5 points)  
a)* Name four different multiplexing methods discussed in the lecture regarding media access control (without explanation).  
0  
1  
2  

b)* We consider a switch that has just been put into operation, whose switching table is empty. This switch received a frame for forwarding. On which ports will the switch likely forward the frame?  
0  

c)* On which layer in the ISO-OSI model does DNS operate? (without justification)  
0  
½  
0  

d)* Given is the Fourier series of a periodic signal s(t) with a0 > 0. Justify whether the signal s(t) is DC-free during transmission or not.  
1  

e)* Given is the spectrum of a Fourier series below. Draw the corresponding time signal s(t) in the solution field in the interval [0,2]. Here, ω = 2π, with T = 1s.  
T  
1  
1.5  
1.5  
2  
ak bk  
nt 1.0 nt 1.0  
e e  
zi zi  
fi fi  
ef ef  
o o  
k k  
er 0.5 er 0.5  
uri uri  
o o  
F F  
0 0  
0 2 4 6 8 10 0 2 4 6 8 10  
Harmonics Harmonics  
1  
0.5  
)  
(t  
s  
e  
d  
u  
plit 0  
m  
a  
al  
n  
g  
Si −  
0.5  
−  
1  
0 1 2  
Time t [s]  

---

**Task 3**  
TCP Data Transmission (8.5 points)  
You want to access a website via HTTP. Your computer is currently connected via Ethernet and IPv4. Consequently, your current MTU is 1500 B. Your TCP implementation also uses the Maximum Segment Size (MSS) option, with which a receiver can inform the sender of the maximum allowed size of segments. RFC793 defines the MSS option as follows:  
Maximum Segment Size  
+--------+--------+---------+--------+  
|00000010|00000100| max seg size |  
+--------+--------+---------+--------+  
Kind=2 Length=4  

a)* Calculate the maximum MSS so that it does not need to be fragmented. Indicate where the numbers come from.  
0  

b)* How large is the receive window (in bytes) if the buffer of your computer can hold the data from 7 segments (as large as possible)?  
0  

c)* Complete the TCP handshake and the specifications for the first two segments from the client and server. Assume a 980-byte HTTP request and a 5 MB response. Client and server always try to make the segments as large as possible.  
0  
1  
2  
SEQ=4253,SYN,Data=0B  
SEQ=312,SYN,Data=0B,ACK=  
SEQ= ,Data=0B,ACK=  
SEQ= ,Data= ,ACK=  
SEQ= ,Data= ,ACK=  

d)* Fill in the following TCP header with the data from the first segment that your computer sends. The numbering system used must be clear. Note: You will find another template at the end of the exam. However, indicate which one should be graded.  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 2  
3  

---

**Task 4**  
Dormitory Network (18 points)  
Given is a student dormitory with several buildings, whose network is built over Ethernet and IPv4. Each building has its own private /24 prefix. The house network for house x is described by the prefix 10.0.x.0/24. All residents of a house are connected to each other via a switch, which is connected to the respective gateway of the house. These routers are interconnected via the transport network 10.0.255.0/24. The MAC addresses of all interfaces are constructed as follows:  
→  
IP:a.b.c.d MAC:00:53:00:00:c:d  
A snippet of the network is given in Figure 4.1. The caches of all devices are empty at the beginning.  

**Figure 4.1: Snippet of the dormitory network**  
a)* Assign IP addresses to all devices shown in Figure 4.1 according to the assigned prefixes. In the house networks, clients receive the smallest possible address lexicographically sorted, routers the largest. In the transport network, routers receive the smallest possible addresses lexicographically ascending to the house number. Draw the IP addresses directly into the above graphic.  
0  
1  
2  

We first consider internal communication within house 1. Resident 1,1 wants to ping resident 1,2 and only knows their IP address.  
b)* Why can the corresponding ICMP Echo Request not be sent directly?  
0  
1  

c)* Provide the source and destination MAC addresses of this first packet.  
0  
1  
SRC-MAC:  
DST-MAC:  

Now we consider inter-house communication. A resident from house 1 wants to send a ping to a resident from house 2. For this, the routing tables of R1 and R2 must first be configured.  
d)* What would happen if the tables were not configured?  
0  
1  

e)* Provide all necessary entries in the tables below for R1 and R2 so that all 3 houses can communicate with each other. Combine individual routes as much as possible. Note: Not all table rows may be needed.  
0  
1  
2  
Destination NextHop Iface  
Routing table of R1  
Destination NextHop Iface  
Routing table of R2  

f)* The ping should now be sent. How many ARP requests must be sent in total at a minimum?  
0  

---

We now consider the sending of the actual Echo Requests (without ARP requests).  
g)* Provide the corresponding header fields for this packet in the table at the marked points P1 to P4. You can use the following notation: MAC(k.iface) for the MAC address of interface iface of node k, similarly IP(k.iface) for the IP address. Residents can be abbreviated with Bx,y.  
0  
1  
2  
SRC-MAC DST-MAC SRC-IP DST-IP TTL  
P1  
P2  
P3  
P4  

Finally, we consider house 3. This house has 15 residents.  
h)* Provide the largest possible prefix length so that each resident can still be assigned an address. Provide the calculation method.  
0  
1  

---

**Task 5**  
Wireshark (14 points)  
Given is the Ethernet frame from Figure 5.1, which is to be analyzed below.  
0x0000 00 0d b9 3e cb 48 0c c4 7a 80 52 5b 08 00 45 10  
0x0010 00 4d e7 79 40 00 40 06 36 bf 83 9f 14 d6 83 9f  
0x0020 00 4e c4 10 00 19 79 2e a6 0b 61 49 62 47 50 18  
0x0030 00 3f 1c a2 00 00 45 48 4c 4f 20 69 6f 77 61 2e  
0x0040 6e 65 74 2e 69 6f 77 75 6d 2e 64 65 0d 0a  

**Figure 5.1: Ethernet frame including checksum**  
Note that justifications are required for subsequent parts. Ensure that markings can be uniquely assigned to individual sub-tasks. Unverifiable statements will not be graded.  

a)* Mark the sender address in Figure 5.1 on Layer 2. (without justification)  
0  

b)* Mark the recipient address in Figure 5.1 on Layer 2. (without justification)  
0  

c)* What type is the L3-PDU?  
0  
1  
Type: Justification:  

d)* Provide the sender address on Layer 3 in its usual and possibly shortened notation.  
0  
1  

e)* Provide the recipient address on Layer 3 in its usual and possibly shortened notation.  
0  
1  

f)* What type is the L4-PDU?  
0  
1  
Type: Justification:  

g)* At what point does the L4-PDU begin?  
0  
1  
Offset: Justification:  

h)* What L7 protocol is it likely?  
0  
1  

i)* Why is this protocol used?  
0  
1  

j)* At what point does the L7-PDU begin?  
0  
1  
Offset: Justification:  

k)* Decode the sent command (the first 4 B of the L7-SDU).  
0  
1  
2  

---

**Task 6**  
Socket Programming (11 points)  
The following sub-task is ungraded. It helps us better assess practical parts of the event and their effectiveness on learning success.  
a)* Did you participate in the live programming (July 11/12) where we implemented the UDP chat or TCP chat?  
yes no Recording of no information  

The following sub-tasks refer to the aforementioned live programming.  
b)* What is the purpose of the syscall bind()?  
0  
1  
2  

c)* Explain what happens and why when using listen() together with a UDP socket.  
0  
1  
2  

d)* How many sockets does a TCP server need to communicate with a single client, and what are they specifically used for?  
0  
1  
2  

e)* What happens when using connect() with a UDP socket?  
0  
1  
2  

f)* Explain the functioning of the syscall select().  
0  
1  
2  
Essential parameter(s):  
Return value(s):  

---

**Task 7**  
James Webb Space Telescope (14 points)  
The James Webb Space Telescope (JWST) was launched on December 25, 2021, and reached its destination – the 1.5 million km distant Lagrange point L1 – on January 24, 2022.  

a)* Determine the average travel speed of the JWST in m/s. (Assume that both the start date and the arrival date count towards the travel time.)  
0  
1  
2  

The JWST generates 235 Gbit of research data daily, which is temporarily stored on a 68 GB SSD.  
b)* Determine the maximum time the JWST can operate without sending data to Earth. (Assume that the full capacity of the SSD is available.)  
0  
1  

To transmit research data to Earth, a channel in the 25.9 GHz band (so-called K-band) is used. The maximum data rate in the downlink direction to Earth is 28 Mbit/s. However, the ground stations on Earth are only reachable for 4 hours each.  
c)* Determine the daily achievable data volume in GB and GiB that can be transmitted to Earth, provided no further overhead occurs.  
0  
1  
2  

d)* As a modulation method, 4-PSK is used. Draw a signal space allocation including labeling that can be uniquely assigned to this modulation method.  
0  
1  
2  

1 Lagrange points are locations in the solar system where the gravitational forces of Earth and the Sun balance each other, allowing spacecraft to maintain a stable position there.  

e)* Based on the information so far, determine the minimally necessary channel bandwidth to achieve the given transmission rate.  
0  
1  
2  

f)* A SNR of 20 dB is expected at the ground station. Determine the minimally necessary bandwidth of the channel under this condition.  
0  
1  
2  
3  

g)* Briefly justify which of the two channel bandwidths will be decisive.  
0  
1  
2  

**Additional template for Task 3**  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31