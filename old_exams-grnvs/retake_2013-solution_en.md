Name First Name
.................
Grade
Study Program (Major) Subject Area (Minor)
I II
Student ID
Signature of the Candidate 1
2
TECHNICAL UNIVERSITY OF MUNICH
a 3
Faculty of Computer Science
l
Midterm Exam h 4
× Final Exam
c
5
s
Semester Exam
r
Diploma Preliminary Exam 6
o
Bachelor Exam
v
............................ 7
s
Consent for Grade Notification 8
via E-Mail / Internet
n
9
u
10
s
Exam Subject: Fundamentals of Computer Networks and Distributed Systems
ö
L
Examiner: Prof. Dr.-Ing. Georg Carle Date: 23.09.2013 (cid:80)
Lecture Hall: .................... Row: .................... Seat: .....................
To be filled out by the supervisor only:
Lecture hall exited from ...... : ...... to ...... : ......
Submitted early at ....... : ......
Special Remarks:
Retake Exam
Fundamentals of Computer Networks and Distributed Systems
Prof. Dr.-Ing. Georg Carle
Chair of Network Architectures and Network Services
Faculty of Computer Science
Technical University of Munich
Monday, 23.09.2013
11:00 – 12:30
• This exam consists of 23 pages and a total of 6 tasks. Please check now that you have received a complete set of instructions.
• Please write your name and student ID in the header of each page.
• Do not write in red/green ink or with a pencil.
• The total number of points is 85.
• Allowed materials include a handwritten double-sided DIN A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.
• Tasks marked with * can be solved without knowledge of the results of preceding sub-tasks.
• Do not spend too much time on any (sub-)task. If you cannot solve the task immediately, rather move on to the next task.
• Only those results will be counted where a solution path is recognizable. Text tasks must be justified unless explicitly stated otherwise in the respective sub-task.
1 Name:
Task 1 Short Tasks (7 Points)
7
The following short tasks are independent of each other. Bullet-point answers are sufficient!
a)* How do you determine the network portion of an IP address in class-based routing? 1
(cid:88)
From the highest-order bits of the first octet.
b)* Describe the problem that can arise when a server that provides important services obtains its IP address via DHCP. 1
If the DHCP server fails, the server will no longer receive an address, making its services unreachable. 
(cid:88)
Alternative: The server could receive a different address after the lease expires, which would interrupt existing TCP connections.
c)* Justify to what extent the Diffie-Hellman method can protect against a Man-in-the-Middle attack. 1
The DH method offers no protection against MITM attacks, as it is a key exchange protocol that does not ensure that the key is negotiated with the correct partner. 
(cid:88)
d)* Distinguish lossless compression from transcoding in general. 1
Both methods change the format of the data without loss of information. Compression also aims to reduce redundancy.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Student ID: 2
e)* Justify which transport protocol you consider suitable for streaming services. 1
UDP, as packet loss is less severe than a too low data rate due to retransmissions. 
Alternative: TCP, because congestion and flow control optimize the data rate, allowing buffer filling during times of high available bandwidth (e.g., video streaming without real-time requirements). 
(cid:88)
2 f)* Explain why line 4 in the following pseudo-code (after lines 1-3) cannot be correct.
Note: This concerns the basic functionality of sockets and not the syntax.
s ← new-tcp-socket()
1
bind(s, address, port)
2
listen(s)
3
buffer ← recv(s)
4
(cid:88)
s is configured as a listening socket (lines 1-3), thus it is not connected (passive socket). Consequently, no data can be received (line 4), only incoming connection requests can be answered. 
(cid:88)
Alternative: An accept is missing between lines 3 and 4:
s ← accept(s)
3.5
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
3 Name:
Task 2 Modulation and Media Access (17 Points)
17
On the planet Gliese 581c, a water world with about 5 times the mass of Earth, lives an extraterrestrial people – the Moepis. This still somewhat backward people is just entering the age of wireless communication. However, the Moepis face a serious problem: Electromagnetic waves, as known to be used for wireless transmission on Earth, are heavily attenuated underwater, which is why common radio techniques do not work on their home world.
Instead, the Moepis rely on sound waves, which propagate underwater on their planet at about 
v =
1480m/s. They use 2-ASK as a modulation method with a signal bandwidth of 
B = 1kHz.
a)* Explain in words how the modulation method 2-ASK works. 1
(cid:88) (cid:88)
The amplitude of a carrier signal is modulated in 2 levels.
b) Calculate how many bits per symbol can be represented using 2-ASK. 1
(cid:88)
⇒
M = 2 log (2) = 1 bit/Symbol
2
c) Determine the achievable data rate as a function of signal bandwidth and the number of signal levels. 1
(cid:88)
r = 2B log (M) = 2 kbit/s
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Student ID: 4
Note: If you could not solve sub-tasks b) or c), assume from now on that 
r = 1 kbit/s.
The new transmission method is being tested by the Moepis on a test track, which is schematically represented in Figure ??. A long test packet of size is sent from 
16B A C
A B C
100m 100m
Figure 2.1: Test setup for the new transmission method.
1 d)* Calculate the serialization time for the test packet.
t
s
(cid:88)
L
t = = 64 ms
s
r
1 e)* Calculate the propagation delay between A and C.
t A C
(cid:88)
d 200m ≈
t = = 135 ms
p
νc 1480m/s
1 f) Draw a complete time-distance diagram for the sending of the test packet.
Scale: (cid:44)
1cm 100ms
A B C
t t t
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
5 Name:
g) Mark in your solution from sub-task f) both 
t t
s p
2
The method is now to be extended to more than two nodes. To do this, it must be recognized whether a data packet arrives at the receiver or not. Since there were no losses in communication between 
A C
in the previous tests, the Moepis decide on the following protocol:
• A data packet is considered successfully transmitted if no error occurred during transmission.
• If a collision, i.e., two simultaneous transmissions, is detected by any node during transmission, that node sends a jam signal of length 
4B.
• If a node receives this jam signal while still transmitting, it aborts and waits a randomly chosen time period.
h)* Which known media access method does this procedure correspond to? (no justification) 1
(cid:88)
CSMA/CD (incorrect: Ethernet, as this is not a media access method)
i)* Justify why the collision detection method proposed by the Moepis does not work correctly in the test setup from Figure ??. 2
(cid:88)
The packet length is too small in relation to the propagation delay. It must hold that 
t 2t(cid:88)
s p,max
where the maximum propagation delay between two stations is denoted as 
t
p,max.
j) Suggest two possible solutions to the problem in sub-task i) (no calculations necessary). 2
(cid:88) (cid:88)
Increase the minimum frame length or decrease the distance between nodes. (Alternatively, also reduce the data rate)
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Student ID: 6
k) Propose a specific modification to the test setup from Figure ?? for one of the two solutions from sub-task j). Determine the threshold of a changed parameter as a numerical value (e.g., minimum or maximum frame size).
(cid:88) (cid:88)
Lmin ≥ 2dmax ⇒ ≤ or ≥
d 47.36m L 271bit
max min
r νc
During further tests, the Moepis also notice the problem. However, an adjustment would require that a node can simultaneously send and listen to the medium for collision detection. This is currently not technically feasible for the Moepis.
2 l)* Describe another media access method suitable for the described scenario that does not require collision detection.
(cid:88) (cid:88)
CSMA/CA: Collision avoidance through contention phase before each transmission.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
7 Name:
Task 3 NAT (17 Points)
17
Given is the network from Figure ??. The Moepi AG operates a small web server behind a NAT router, which is to be accessible from the internet. Due to significant losses in the past quarter, Moepi AG can unfortunately only afford one public IPv4 address.
Moepi AG
R1 R2
eth1 eth0 eth0: 10.0.0.4
C2
eth1
eth0: 131.159.20.254
eth1
SW1 eth0: 10.0.0.3
eth0 C1
eth0: 131.159.20.83 wan0: 217.79.191.6
eth0: 10.0.0.1
eth1 eth2
eth0 eth3
eth0: 10.0.0.2
PC1 R3 SW2 web
Figure 3.1: Network topology
a)* Justify why the web server web is not readily accessible from the internet. 1
The address 10.0.0.1 is a private IP address, therefore not unique and not routable on the internet. 
(cid:88)
b)* Assume that Moepi AG had a second public IP address available and would configure the web server with this address. Give two reasons why this would not guarantee the accessibility of the web server. 2
It would not be sufficient because 
(cid:88)
1. the server with this address could not communicate with its gateway and 
2. without further configuration, no one on the internet knows that this second public address is accessible via 217.79.191.6. 
(cid:88)
c)* Justify whether switches need IP addresses to fulfill their normal function. 1
(cid:88)
No, as switches make forwarding decisions based solely on MAC addresses.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Student ID: 8
Table ?? shows an excerpt of the NAT table of router R3 with some dynamic entries as they arise during operation. Such entries can also be generated statically (“Port Forwarding”).
Prot. Local IP Local Port Global IP Global Port Remote IP Remote Port
tcp 10.0.0.4 2783 217.79.191.6 2783 131.159.20.83 80
tcp 10.0.0.4 6942 217.79.191.6 6942 131.159.20.83 443
tcp 10.0.0.3 2783 217.79.191.6 2784 131.159.20.83 80
tcp 10.0.0.2 2783 217.79.191.6 80 * *
Table 1: NAT table of router R3
2 d)* Explain how R3 makes forwarding decisions based on the 7 columns in Table ??. 
Packets with protocol 'Prot.', which R3 receives from 'Remote IP/Port' to 'Global IP/Port', are forwarded to 'Local IP/Port'. Packets from 'Local IP/Port' are forwarded to 'Remote IP/Port'. 
(cid:88)(cid:88)
1 e) Provide another entry in Table ?? such that R3 is forced to set a different global port than the local port. 
2 f) Complete the NAT table in Figure ?? with a static entry so that only the web server is accessible from the internet on the standard HTTP port. Ensure that NAT still allows other computers within Moepi AG to access the internet. If an entry can take any values, simply write * as a wildcard instead of the specific value.
In the following, we will abbreviate IP and MAC addresses according to the scheme 
<DeviceName>.<Interface>
, e.g. . Note that for the next two sub-tasks, R3 is located between 
R1 R2 PC1
and a total of three other routers. 
4 g) Complete the header fields for the request from PC1 to http://217.79.191.6 in the three empty boxes in Figure ??. If a field cannot be uniquely determined, make a sensible choice.
4 h) Complete the header fields for the response from http://217.79.191.6 in the three empty boxes in Figure ??. If a field cannot be uniquely determined, make a sensible choice.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
9 Name:
b
e
w
0
h
t
e
000
0hhh
httt
teee 0
e... 0
.b1b 0
3 3eCe820
h RwPw548
t
e
000 2 tt
0hhh W CC rr
httt S AAPP oo
teee 0 MMII PP
e... 0 ctctLct
3.ebC1eb8200 th0 SrDsSrDsTTSrDs
RwPw548 e
)
g
e
tt b
CC rr ga
AAPP oo uf
MMII PP a
ctctLct eil
rsrsTrs T
SDSDTSD 0 r
h ü
t f
e ck
u
r
d
2 3 r
R 1 0 R svo
h n g
0 t a un
th e w Lös
e
2:
3.
g
n
u
d
bil
b
A
0 0
h0h0
thtn
etea 0
.e.w 0
1.1. 0
C1C3420
PRPR648
tt
CC rr
AAPP oo
MMII PP
ctctLct
rsrsTrs
1 1 SDSDTSD
h W
t 0 S 0
e h h
t t
e e 1
1
C
R
1 0 P
h h
t t
e e
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Matrikelnummer: 10
b
e
w
0
h
t
e
0 00
h0hh
thtt
etee 0
.e.. 0
b.b1 0
3 e3eC402
h wRwP684
t
e
0 00 2 tt
h0hh W CC rr
thtt S AAPP oo
etee 0 MMII PP
.e.. 0 ctctLct
eb3.ebC14020 th0 SrDsSrDsTTSrDs
wRwP684 e h)
e
b
a
tt g
CC rr uf
AAPP oo a
MMII PP ail
ctctLct T
rsrsTrs r
SDSDTSD 0 fü
h k
t c
e u
r
d
r
2 3 vo
R 1 0 R ngs
h n u
h0 et wa Lös
et 3:
3.
g
n
u
d
bil
b
A
0 0
0h0h
htnt
teae 0
e.w. 0
.1.1 0
1C3C802
RPRP584
tt
CC rr
AAPP oo
MMII PP
ctctLct
rsrsTrs
1 1 SDSDTSD
h W
t 0 S 0
e h h
t t
e e 1
1
C
R
1 0 P
h h
t t
e e
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
11 Name:
Task 4 Routing (15 Points)
15
Given is the network from Figure ??. The routers have a separate IP address for each interface and receive the first usable address of the respective subnet. The hosts receive the directly following IP addresses in ascending order.
Internet
H4
eth1: 17.1.5.23
A
eth0: 192.168.0.51
eth0: 192.168.0.1
R1
eth0: 192.168.0.2 eth0: 192.168.0.3
eth2: 192.168.0.57 eth1: 192.168.0.33 eth2: 192.168.0.49
D B C
eth0: 192.168.0.58 eth1: 192.168.0.34
H1 R2 R3
eth0: 192.168.0.50
eth0: 192.168.0.35
H2 H3
Figure 4.1: Network topology
a)* Determine the missing values in Table ??. 3
Note: The first column contains the designation of the network and does not indicate the network class.
Network Network Address Broadcast Address Subnet Mask Usable Addresses
192.168.0.0 192.168.0.31 255.255.255.224 30
A
192.168.0.32 192.168.0.47 255.255.255.240 14
B
192.168.0.48 192.168.0.55 255.255.255.248 6
C
Table 2: Overview of Address Distribution
b) Assign the correct IP addresses to the routers and hosts according to Table ??. Enter your 2
results directly in Figure ??. The first two octets are already given. Assign the first usable IP addresses per subnet to the router interfaces.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Student ID: 12
Host H1 now wants to send a message to H4. Assume that all ARP caches are empty. Additionally, an excerpt of the routing table of R2 is given in Table ??. Note that some values are not provided, as you had to determine them in previous sub-tasks. These values have been replaced with a question mark. The gateway addresses have been replaced with 
<DeviceName>.<Interface-Name>, e.g. R3.eth1.
Destination Mask Gateway Metric Iface
192.168.0.0 ? - 0
eth0
192.168.0.48 ? 1
R3.eth0 eth0
0.0.0.0 0.0.0.0 1
R1.eth0 eth0
Table 3: Excerpt from the Routing Table of Router R2.
2 c) Enter all necessary ARP requests and ARP replies in the correct order in the table below. 
Note: In the following table, one row stands for a pair of ARP request and corresponding ARP reply. The last two octets of the IP addresses are sufficient. Note interfaces as 
<DeviceName>.<Interface-Name>.
ARP Request ARP Reply
Sender.Interface Sender IP Address Requested IP Address Sender.Interface
H1.eth0 0.58 0.57 R2.eth2
R2.eth0 0.2 0.3 R3.eth0
R3.eth2 0.49 0.51 H4.eth0
2 d)* Describe how a router can check if an entry in its routing table matches a given destination IP. 
R1 calculates the logical AND of the destination address of the packet and the masks (“Genmasks”) in its routing table. 
(cid:88)
(cid:88)
The result is compared with the entry in the “Destination” column.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
13 Name:
e)* Describe how a router selects the next hop from all matching entries for a given destination. 
2
Longest Prefix Match: The routing table is searched from longer prefixes (more specific routes) to shorter prefixes (less specific routes). The first matching entry provides the gateway (next hop) of a packet. 
(cid:88)
In case of equal prefix length, the entry with the lower metric is preferred.
Now consider the excerpt of the routing table of router R1 shown in Table ??. A packet coming from the internet is to be forwarded to host H2.
Destination Mask Gateway Metric Iface
192.168.0.56 255.255.255.248 1
R2.eth0 eth0
192.168.0.32 255.255.255.240 1
R2.eth0 eth0
192.168.0.32 255.255.255.224 1
R3.eth0 eth0
Table 4: Excerpt from the Routing Table of Router R1.
f)* Justify which next hop R1 will choose when forwarding the packet to H2. 1
R2, due to the Longest-Prefix-Match rule, metric does not matter in this case.
g)* What is the purpose of the last line of the routing table of R2 (see Table ??)? 1
(cid:88)
Default Route, if no other route to this subnet is known, use this entry.
So far, static routing has been considered. However, dynamic routing is often used.
h)* Name two different concepts for dynamic routing. 1
(cid:88)
Distance Vector Protocols
(cid:88)
Link-State Protocols
i)* Name two different metrics that can influence the cost determination for path selection. 1
(cid:88)
Hop Count
(cid:88)
Transmission Rates
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Student ID: 14
Task 5 Frame Boundaries and Block Check (10 Points)
10
In the following task, we will take a closer look at the so-called BISYNC protocol, which stands for Binary Synchronous Communication (BSC). It was developed by IBM in 1967. It is a communication protocol that offers services at the data link layer. The structure of a BISYNC frame is schematically represented in Figure ??.
8bit 8bit 8bit 8bit 8bit 16bit
SYN SYN SOH Header STX Payload ETX CRC
Figure 5.1: BISYNC Frame Format
A BISYNC frame is structured using control characters. Table ?? contains an excerpt of the control characters used. DLE is the escape character and is placed before the corresponding control character.
Control Character Hex Value Meaning
Start of Header
SOH 0x01
Start of Text
STX 0x02
End of Transmission
ETX 0x03
Data Link Escape
DLE 0x10
Synchronization
SYN 0x16
Table 5: Control Characters in BISYNC
1 a)* Name another way, besides using control characters, to mark frame boundaries. 
(cid:88)
Length indications of the payload, boundary fields, or violations of coding rules.
1 b)* Justify generally why an escape character is necessary when control characters are used to recognize frame boundaries. 
The control characters in the payload portion are protected from interpretation using the escape character DLE. 
(cid:88)
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
15 Name:
c)* Justify why ETX and DLE must be protected in the payload portion. 
2
ETX must be protected as it indicates the end of the message; otherwise, the message would be terminated too early. 
(cid:88)
The character DLE itself must be protected as it is used as an escape character in the payload portion.
d) Justify why escaping the other characters in the payload portion can be omitted. 1
All other characters can be interpreted directly as data, as it is known that one is already in the payload. 
e)* Correctly encode the following hexadecimal character string as a payload: 10 03 A1. 1
(cid:88)
10 10 10 03 A1
Next, we consider the hexadecimal character string 
16 16 01 AA BA F8 02 12 A9 03 00 33
which has been received as a message. It represents a complete frame.
f)* Determine the header, the payload, and the checksum of the given message. 1
Header:
AA BA F8
Payload: 12 A9 (cid:88)
Checksum:
00 33
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Student ID: 16
g)* Justify what degree a generator polynomial for BISYNC should ideally have. 1
(cid:88)
grad(g(x)) = 16, as 16 bits are reserved for the checksum.
1 h)* Justify generally which bit errors can be detected using CRC checksums. 
Burst errors up to a length corresponding to the degree of the polynomial can be detected. 
1 i)* Justify which bit errors can be corrected using CRC checksums. 
(cid:88)
It is an error-detecting method, thus no errors can be corrected.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
17 Name:
Task 6 TCP (19 Points)
19
In this task, we will examine the Transmission Control Protocol (TCP) in the "Reno" variant. A client C and a server S execute the following protocol:
1. C establishes a TCP connection to S.
2. S sends its current system time to C in an Enterprise XML formatted message, which is 
3000B long.
3. S sends another message that is 3600B long and contains a signature of the first message.
4. S and C close the connection again.
We will now take a closer look at the TCP connection. The contents of the messages are not relevant.
a)* Explain the difference between flow control and congestion control. 2
(cid:88)
Flow control: protects the receiver from overload.
Congestion control: protects the nodes on the transmission path between sender and receiver from overload. 
(cid:88)
At the beginning, C establishes a TCP connection to S. C chooses the initial sequence number 10000, and S chooses 
20000.
Note: In this task, ignore serialization times and propagation delays in all time-distance diagrams. One arrow per segment is sufficient. Indicate the set flags (SYN, FIN, RST), the sequence number (e.g., SEQ=1), and, if set, the acknowledgment number (e.g., ACK=1) for all segments.
b)* Draw the connection establishment in the following time-distance diagram. 2
C S
SYN, SEQ=10000
SYN, SEQ=20000, ACK=10001
SEQ=10001, ACK=20001
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Student ID: 18
c)* In which phase of congestion control are C and S now? 
(cid:88)
1
Since the connection has just been established, both are in the slow-start phase.
Now S begins to send the first message with a length of 3000B. The size of the receive window on both sides is . The MSS is in both directions . Both congestion control windows start with a size of 
3000B 1000B
1 MSS.
3 d) Draw all segments that occur when sending the message in the following time-distance diagram. Pay attention to the development of the congestion control window!
C S
SEQ=20001
SEQ=10001, ACK=21001
SEQ=21001
SEQ=22001
SEQ=10001, ACK=22001
SEQ=10001, ACK=23001
1 e) What are the sizes of the congestion control windows of C and S now? 
(cid:88)
w = 1
c,C
(cid:88)
w = 4
c,S
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
19 Name:
Next, we assume that "Go-Back-N" is used for congestion control. The size of the receive window is still 
3000B for both participants. S now sends the second message with a size of 3600B. However, the second segment is discarded due to a bit error.
f) Label the given segments in the following time-distance diagram and draw all 3 segments that are necessary for the successful transmission of the second message. Assume that no further packet losses occur.
C S
SEQ=23001
(cid:69) SEQ=10001, ACK=24001 SEQ=24001
SEQ=25001
SEQ=10001, ACK=24001
SEQ=24001
SEQ=10001, ACK=25001 SEQ=25001
SEQ=10001, ACK=26001 SEQ=26001
SEQ=10001, ACK=26601
g) Justify in which phase of congestion control C and S are now. 2
(cid:88)
C: Slow Start, because C has never sent data. 
(cid:88)
S: Slow Start, because it only transitions to the congestion avoidance phase after 3 duplicate ACKs.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Student ID: 20
h)* Justify what advantage "Selective Repeat" offers over "Go-Back-N". 
1
With Selective Repeat, no segments that are received out of order or after a packet loss are discarded, as long as their sequence numbers fit within the receive window. This means fewer segments need to be retransmitted. With Go-Back-N, only the next expected segment is accepted. 
(cid:88)
S now closes the TCP connection. C also closes the connection afterward.
2 i) Draw the connection teardown in the following time-distance diagram. 
C S
FIN, SEQ=26601
SEQ=10001, ACK=26602
FIN, SEQ=10001
SEQ=10001, ACK=10002
1 j)* Explain what it means when one side closes the TCP connection. Does the other side have to close the connection as well? 
(cid:88)
If, for example, S closes the connection, S can no longer send data. However, C can keep its side open and continue to send data, which can still be received by S. 
(cid:88)
1 k)* A channel has a bit error rate of 5%. Explain whether the use of TCP is an efficient solution to hide packet errors from the application layer. 
TCP is inefficient because congestion control misinterprets packet losses due to checksum errors as congestion and thus reduces the data rate much more than necessary. 
(cid:88) (cid:88)
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
21 Name:
Additional space for solutions – please clearly mark the affiliation with the respective task and strike out invalid solutions!
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
Student ID: 22
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013
23 Name: