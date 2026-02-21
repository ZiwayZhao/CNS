Name First Name  
..................  
Grade  
Course of Study (Major) Specialization (Minor)  
I II  
Student ID  
Signature of the Candidate  
1  
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
via Email / Internet  
n  
9  
u  
10  
s  
Exam Subject: Fundamentals of Computer Networks and Distributed Systems  
ö  
L  
Examiner: Prof. Dr. Uwe Baumgarten Date: 17.08.2011 (cid:80)  
Lecture Hall: .................... Row: .................... Seat: .....................  
To be filled out by the supervisor only:  
Lecture hall exited from ...... : ...... to ...... : ......  
Submitted early at ....... : ......  
Special Remarks:  
Final Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr. Uwe Baumgarten  
Chair of Operating Systems and System Software  
Faculty of Computer Science  
Technical University of Munich  
Wednesday, 17.08.2011  
11:30 AM – 1:00 PM  
• This exam consists of 23 pages and a total of 5 tasks. Please check now that you have received a complete set of materials.  
• Please write your name and student ID in the header of each page.  
• The total number of points is 85.  
• Allowed materials include one double-sided A4 sheet of notes and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
• Tasks marked with * can be solved without knowledge of the results of previous subtasks.  
• Only results where a solution path is recognizable will be counted.  
1 Name:  
Task 1 Ethernet Physical Layer (19 points)  
19  
In this task, we examine two different implementations of the Ethernet Physical Layer. First, we discuss the (somewhat outdated) 10BASE-2. Manchester encoding is used as the line code. No additional channel coding takes place. Given is the ideally represented 10BASE-2 signal shown in Figure 1.1.  
s(t)  
A  
−  
t/10 7s  
3 6  
−  
A  
Figure 1.1: Idealized course of a 10BASE-2 signal.  
a)* Is the signal time-continuous or time-discrete?  
1  
(cid:88)  
Time-continuous  
∈  
b)* Determine the transmitted bit sequence over the time interval.  
t [0µs,0.6µs) 2  
Note: There are two variants of Manchester encoding, which differ in the assignment between logical "0" and "1". You can choose one of the two variants here.  
0 1  
(cid:88)(cid:88)  
According to the version used in IEEE 802.3:  
100111  
Alternative:  
011000  
c)* How long does it take to serialize a single bit?  
1  
(cid:88)  
From Figure 1.1: T = 1 10 7s = 0.1µs  
d)* Determine the data rate achievable with 10BASE-2 (calculation or justification).  
1  
(cid:88)  
1bit  
r = = 10Mbit/s  
T  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 2  
e) Determine the minimum necessary spectral bandwidth according to Hartley to achieve the data rate specified in subtask d) with a binary line code.  
2  
(cid:88) (cid:88)  
· ⇔ R  
r = 2B log (M) B = = 5MHz  
2  
2log (M)  
2  
f) Justify why 10BASE-2 occupies at least a bandwidth of (cid:48).  
1 B = 10MHz  
The Manchester code represents a bit through two signal changes. Therefore, it has a baud rate twice as high as, for example, NRZ at the same bit rate. The required bandwidth doubles.  
g) Justify which other binary line code can achieve a higher data rate at the same spectral bandwidth.  
1  
(cid:88)  
NRZ is suitable because here the baud rate exactly corresponds to the bit rate.  
h) What significant advantage does the Manchester code offer?  
1  
(cid:88)  
Clock recovery (or DC-free)  
Next, we consider the newer 100BASE-TX standard. This uses MLT-3 with 4B5B encoding as the line code. The effective data rate is 100Mbit/s. In Figure 1.2, an idealized signal course of a single wire is shown, which encodes the bit sequence.  
0101111101  
s(t)  
A  
1 2 3 4 5 6 7 8 9 10 t/T  
−  
A  
Figure 1.2: Idealized course of an MLT-3 signal.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
3 Name:  
i)* Describe the functionality of MLT-3.  
(cid:88)  
− 2  
The signal level always goes through the sequence. A logical "1" causes a level change, while a logical "0" does not cause a level change.  
0,+1,0, 1,0,+1(cid:88),... 1  
j) Justify whether problems arise when recognizing long sequences of zeros or ones with MLT-3 encoding.  
2  
(cid:88)  
Long sequences of zeros lead to a constant signal level. Since clock recovery is difficult here, this poses a problem.  
k)* Justify whether 4B5B encoding can be helpful in recognizing long sequences of zeros or ones.  
3  
Long inputs are mapped to long codewords by the 4B5B encoding. Each  
4bit 5bit (cid:88)  
codeword, which consists of a long input, contains at least one logical "1" and thus causes a level change of the MLT-3 code. Consequently, the length of possible zero sequences is limited, enabling clock recovery.  
l)* Can transmission errors be corrected using 4B5B encoding?  
1  
(cid:88)  
Transmission errors cannot be corrected.  
m)* What must the bitrate actually be for 100BASE-TX to achieve an effective transmission speed of 100Mbit/s?  
1  
Note: This is only about the bitrate from the perspective of the physical layer. You do not need to consider the overhead caused by protocol headers!  
(cid:88)  
r · 5  
netto  
r = = 100Mbit/s = 125Mbit/s  
brutto  
R 4  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 4  
Notes:  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
5 Name:  
Task 2 IP Fragmentation (17 points)  
17  
Consider the network topology shown in Figure 2.1. The two computers PC1 and PC2 use their respective local router as the default gateway. The routing tables of R1 and R2 are already configured, so that a connection between PC1 and PC2 is possible. The connection between R1 and R2 has an MTU of ( ). The MTU within the two local networks of PC1 and PC2 is . In Figure 2.2a you will find an overview of the fields of the IP header. The packet sent by PC1 is shown in Figure 2.2b.  
MAC addresses are abbreviated as indicated in Figure 2.1: .  
<Device>.<Interface>  
PC1 PC2  
eth0 eth0  
MAC: PC1.eth0 MAC: PC2.eth0  
IP: 192.168.1.1/24 IP: 192.168.2.1  
eth0 wan0 wan0 eth0  
MAC: R1.eth0 MAC: R1.wan0 MAC: R2.wan0 MAC: R2.eth0  
IP: 192.168.1.254/24 IP: 10.10.0.1/30 IP: 10.10.0.2/30 IP: 192.168.2.254  
SW1 R1 R2 SW2  
Figure 2.1: Topology  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
Version IHL ToS Total Length  
Identifier R D M Fragment Offset  
TTL Protocol Header Checksum  
Source IP Address  
Target IP Address  
(a) Overview of IP Header  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
ToS  
0x4 0x5 1150(10)  
0 0 0  
7261 0  
(10) (10)  
Protocol Header Checksum  
64  
(10)  
192.168.1.1  
192.168.2.1  
Payload  
(b) Packet sent by PC1  
Figure 2.2: Overview of the IP header (a) and the packet sent by PC1 (b).  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 6  
a)* Justify whether the switches SW1 and SW2 need their own MAC address for their basic tasks. If necessary, add them in Figure 2.1.  
1  
No device communicates directly with (cid:88) the switch – switches operate at layer 2 and are transparent to the connected devices.  
b)* What is the significance of the two header fields "Identifier" and "Fragment Offset" for IP fragmentation?  
2  
(cid:88)  
• Identifier: Unique identification of all fragments belonging to a packet.  
• Fragment Offset: Enables the reassembly of fragments in the correct order.  
(cid:88)  
c)* What size does the IP header have without options?  
1  
(cid:88)  
20b  
d)* What is the size of the payload of the packet shown in Figure 2.2b?  
1  
(cid:88)  
1130b  
e)* Which parts of the layer-2 PDU count towards the MTU?  
1  
(cid:88)  
The entire payload (layer-2 SDU), i.e., the IP packet including the IP header.  
f) How many fragments will R1 split the packet sent by PC1 into?  
1  
(cid:24) (cid:25)  
(cid:88)  
1130b  
N = − = 3  
580b 20b  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
7 Name:  
g)* Justify whether fragments can be forwarded independently of each other.  
Each fragment receives its own IP header and thus has all the necessary information, so  
(cid:88) 1  
that routers can forward fragments independently of each other.  
h) For what reason can the reassembly of packets generally only take place at the receiver?  
Individual fragments can generally be forwarded to the receiver via different paths.  
(cid:88)  
Reassembly is therefore only possible again at the receiver.  
Assume that no data exchange has taken place between the devices so far. PC1 now sends the packet shown in Figure 2.2b.  
i) Sketch a simple message flow diagram that considers all frames that need to be transmitted over the respective connections. Note the type of each exchanged message above it. No further details are necessary. Serialization time and propagation delay can be neglected.  
PC1 SW1 R1 R2 SW2 PC2  
ARP-Request  
ARP-Reply  
IP-Packet  
ARP-Request  
ARP-Reply  
IP-Packet  
ARP-Request  
IP-Packet  
ARP-Reply  
IP-Packet  
IP-Packet  
IP-Packet  
IP-Packet  
(cid:88) (cid:88) (cid:88)  
ARP Requests correct, IP-Packet correctly fragmented, time behavior qualitatively correct  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 8  
j)* Provide the sender and receiver addresses of layers 2 and 3 for a frame between R1 and R2 with IP payload.  
2  
(cid:88)  
→  
• Layer 2: R1.wan0 R2.wan0  
(cid:88)  
→  
• Layer 3: 192.168.1.1 192.168.2.1  
k)* What happens if PC1 sets the "D" bit in the IP header?  
2  
(cid:88)  
R1 discards the packet and sends an "ICMP Fragmentation needed but DF Bit set" (PC1 is notified, which is sufficient response).  
l)* Can a fragment be fragmented again?  
1  
(cid:88)  
Yes. (no justification required)  
Notes:  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
9 Name:  
Task 3 Routing and NAT (21 points)  
21  
We consider the network topology shown in Figure 3.1. PC1 and PC2 are located in the private network 192.168.1.208/28, which is connected to the public network via router R1. Assume that there are no other routers in the three public networks (represented by clouds). All routers except R2 are already configured. Developing the routing table for R2 is part of the task. For the entire task, assume that no communication has taken place in the network so far.  
PC1 R3  
IP: 74.125.39.254/24  
74.125.39.0/24  
wan1  
wan0 IP: 149.1.2.6/30  
eth0 IP: _1_9_2_.1_6_8_._1_.2_0_9__________________ eth0 IP: 74.125.39.24/24  
Webserver  
wan2 IP: 149.1.2.5/30  
eth0 wan0 93.233.66.0/24 wan0 R2  
IP: 192.168.1.222/28 IP: 93.233.66.23/24 IP: 93.233.66.253/24  
R1 wan1 IP: 149.1.2.1/30  
IP: 93.233.66.254/24 Mailserver  
eth0 IP: _1_9_2_.1_6_8_._1_.2_1_0__________________ G eth0 IP: 131.159.74.8/24  
wan0 IP: 149.1.2.2/30  
Internet  
wan1 131.159.74.0/24  
IP: 131.159.74.254/24  
R4  
PC2  
Figure 3.1: Topology and Addresses  
a)* How many IP addresses are usable in a /28 network?  
1  
(cid:88)  
− − −  
N = 232 28 2 = 24 2 = 14  
b)* Provide the network and broadcast address of the private network 192.168.1.208/28.  
2  
(cid:88)  
• Network address: 192.168.1.208  
(cid:88)  
• Broadcast address: 192.168.1.223  
c)* Assign IP addresses to the two computers PC1 and PC2 so that they can communicate with their gateway R1. Enter the addresses directly in Figure 3.1.  
Notes:  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 10  
d)* Which routers must support NAT so that PC1 and PC2 can communicate with the public network?  
1  
(cid:88)  
Router R1  
e)* Complete the routing table of R2 shown in the solution field so that PC1 and PC2 can communicate with the web and email servers. Also set a default gateway for R2 so that it can forward packets to the Internet.  
Destination Subnet Mask Gateway Interface  
149.1.2.0 255.255.255.252 0.0.0.0 wan1  
(cid:88)  
149.1.2.4 255.255.255.252 0.0.0.0 wan2  
(cid:88)  
93.233.66.0 255.255.255.0 0.0.0.0 wan0  
(cid:88)  
131.159.74.0 255.255.255.0 149.1.2.2 wan1  
(cid:88)  
74.125.39.0 255.255.255.0 149.1.2.6 wan2  
(cid:88)  
0.0.0.0 0.0.0.0 93.233.66.254 wan0  
(As a gateway for directly connected networks, the IP of the local interface can alternatively be specified.)  
PC1 now attempts to access a webpage on the web server 74.125.39.24. The communication process will be examined in detail at three points in the network. Assume that there are currently no NAT entries. Any ARP messages do not need to be considered further. You may abbreviate IP addresses for the remainder of the task using  
<Device Name>.<Interface>  
e.g., , or .  
PC1.eth0 Web.eth0 R2.wan0  
f)* What transport protocol and destination port number is typical for (unencrypted) HTTP connections?  
1  
(cid:88)  
TCP 80  
g)* Complete the header fields for the request from PC1 to the web server in the three empty boxes in Figure 3.2. If a field is not clearly defined, make a reasonable choice.  
Note: If you could not solve the previous subtask, assume destination port 80.  
h)* Complete the header fields for the response from the web server to PC1 in the three empty boxes in Figure 3.3.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
11 Name:  
4 4  
2 r r 2  
9.24/ server server 74.8/  
74.125.39.0/24 IP: 74.125.3 Webs 3.233.66.23 4.125.39.24Mails1 7163 IP: 131.159.0 131.159.74.0/24  
9 7 6 2 8  
SrcIP DstIP TTL SrcPort DstPort ver  
r  
e  
R2 ebs  
W  
n  
3 4 de  
R R  
n  
a  
1  
C  
P  
n  
o  
v  
e  
g  
a  
r  
nf  
3 4 A  
6.2 9.2 die  
6 3  
93.233. 74.125. 63 27163 80 6.0/24 G net ologiefür  
6 r p  
33. nte To  
SrcIP DstIP TTL SrcPort DstPort 93.2 I ereinfachte  
V  
2:  
3.  
g  
n  
u  
d  
bil  
b  
A  
9  
0 4  
2 2 1  
1. 9. R  
92.168. 4.125.3 4 2617 0  
1 7 6 3 8  
SrcIP DstIP TTL SrcPort DstPort  
1 2  
C C  
P P  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 12  
4 4  
2 r r 2  
9.24/ server server 74.8/  
74.125.39.0/24 IP: 74.125.3 Webs 4.125.39.24 3.233.66.23Mails4 0 IP: 131.159.7163 131.159.74.0/24  
7 9 6 8 2  
A SrcIP DstIP TTL SrcPort DstPort  
b  
b 2  
ild R  
u  
n  
g  
3 3 4  
.3 R R  
:  
V  
e  
r  
e  
in  
fa  
c  
h  
t  
e  
T  
o  
p  
o 4 3  
lo 2 2  
gie 39. 66.  
fürdieA 74.125. 93.233. 62 80 27163 6.0/24 G net  
n 6 r  
twort 3.233. Inte  
vomWe SrcIP DstIP TTL SrcPort DstPort 9  
b  
s  
e  
r  
v  
e  
r  
z  
u  
P  
C  
1  
9  
4 0  
2 2 1  
9. 1. R  
4.125.3 92.168. 1 0 2617  
7 1 6 8 3  
SrcIP DstIP TTL SrcPort DstPort  
1 2  
C C  
P P  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
13 Name:  
Assume that the NAT implementation used only stores the triplet consisting of local IP address, local port, and global port.  
i) Provide all entries in the table below that are present in the NAT table of router R1 after the message exchange between PC1 and the web server.  
(cid:88)  
Local IP Local Port Global Port  
192.168.1.209 32617 27163  
(The global port can also be the same as the local port)  
Now PC2 accesses the mail server (131.159.74.8, TCP 25). It chooses port number 33213 as the source port.  
j) Provide all entries in the table below that are present in the NAT table of router R1 after the message exchange between PC2 and the mail server.  
Local IP Local Port Global Port (cid:88)  
192.168.1.209 32617 27163  
192.168.1.2 33213 24713  
(The global port can also be the same as the local port, but no overlap!)  
The attacker Bob from the Internet now knows that a computer from the network behind R1 had contact with the mail server. We assume that Bob was able to intercept a message from PC1 to the mail server somewhere between R1 and the mail server. He therefore particularly knows the IP addresses and port numbers contained in the message.  
k)* Justify whether Bob can establish a connection to PC1 or PC2 with this information.  
• Bob cannot reach PC2 because he only knows the tuple of public IP and source port,  
(cid:88)  
which R1 assigns to computer PC1.  
• Bob can reach PC1, but it is unlikely that a connection will be established. The reason is that PC1 does not expect incoming connections on the relevant port.  
(cid:88)  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 14  
Notes:  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
15 Name:  
Task 4 Transport Layer (10 points)  
10  
The trace printed below represents a connection captured with Wireshark between a TCPGrnvsClient and the TCPGrnvsServer (Homework 3). Source and destination addresses are abbreviated for clarity.  
No. Source Destination Prot Info  
1 2001::9a7 2001::c968 TCP 49821 > 6112 [SYN] Seq=0 Win=14400 Len=0 MSS=1440  
2 2001::c968 2001::9a7 TCP 6112 > 49821 [SYN, ACK] Seq=0 Ack=1 Win=5712 Len=0 MSS=1440  
3 2001::9a7 2001::c968 TCP 49821 > 6112 [ACK] Seq=1 Ack=1 Win=14400 Len=0  
4 2001::c968 2001::9a7 TCP 6112 > 49821 [ACK] Seq=1 Ack=1 Win=5712 Len=80  
5 2001::9a7 2001::c968 TCP 49821 > 6112 [ACK] Seq=1 Ack=81 Win=14400 Len=0  
6 2001::9a7 2001::c968 TCP 49821 > 6112 [ACK] Seq=1 Ack=81 Win=14400 Len=7  
7 2001::c968 2001::9a7 TCP 6112 > 49821 [ACK] Seq=81 Ack=8 Win=5712 Len=0  
...  
As a reminder:  
1. After the connection is established, the server sends a welcome string, which contains a short message as well as the client's IP address.  
2. The client should then respond with "HELLO".  
The further protocol flow is not relevant for this task.  
a)* Assign packets 1 – 7 to the TCP connection phases. Which phase is not represented in the trace?  
(cid:88)  
• 3-Way Handshake: 1–3  
(cid:88)  
• Data Transfer Phase: 4–7  
(cid:88)  
• Connection Teardown: not included in the trace  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 16  
b)* Create a time-sequence diagram from messages 1–7 and supplement it with the connection teardown. Assume that the client initiates the connection teardown. Note flags, SEQ number, ACK number, and length for each exchanged message in this order. Serialization time and propagation delay can be neglected.  
2001::9a7 2001::c968  
SYN, SEQ=0, len=0  
SYN, ACK, SEQ=0, ACK=1, len=0  
ACK, SEQ=1, ACK=1, len=0  
ACK, SEQ=1, ACK=1, len=80  
ACK, SEQ=1, ACK=81, len=0  
ACK, SEQ=1, ACK=81, len=7  
ACK, SEQ=81, ACK=8, len=0  
FIN, ACK, SEQ=8, ACK=81, len=0  
FIN, ACK, SEQ=81, ACK=9, len=0  
ACK, SEQ=9, ACK=82, len=0  
(cid:88)(cid:88)  
First 7 packets  
(cid:88)(cid:88)  
Teardown  
c) Assuming the client and server would communicate via UDP. What changes would occur in the time-sequence diagram from the previous subtask?  
(cid:88)  
• No connection establishment  
(cid:88)  
• No acknowledgments  
(cid:88)  
• No connection teardown  
Also correct:  
• Connection setup and teardown must now be integrated into the protocol  
• Only data packets are exchanged (no ACKs)  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
17 Name:  
Task 5 Short Questions (18 points)  
18  
The following short questions are independent of each other. Bullet-point answers are sufficient!  
a)* The large data is given in Big Endian (Network Byte Order). Convert  
16bit 0x1234 1  
the data to Little Endian.  
(cid:88)  
0x3412  
b)* Given a noise power of . Calculate or justify the necessary  
PN = 2.0mW 2  
signal power , so that a signal-to-noise ratio of is achieved.  
P 6dB  
S (cid:18) (cid:19)  
(cid:88) (cid:88)  
· PS ⇔ SNR · 6 ·  
SNR = 10 log PS = 10 10 PN = 1010 2mW = 7.96mW  
P  
N  
≈ ⇒ ∼  
Alternative: Rule of thumb factor  
3dB 2 8.0mW  
c)* Determine the CRC sum of the message . The generator polynomial is .  
10011011 g(x) = x2+1 3  
(cid:88)  
The generator polynomial in binary notation:  
101  
10011011 00 : 101 = 1011011, remainder 010  
(cid:88) (cid:88)  
Correct remainder, appending the two zeros to the bit sequence to be transmitted  
d)* Given . Which protocol does this address belong to?  
fe80::222:b0ff:febc:1fe2/64 1  
(cid:88)  
IPv6  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 18  
e)* Given the four signal courses in Figure 5.1 (the abscissa corresponds to time, the ordinate to amplitude). Check the applicable properties for each of the four signals in the table printed below.  
2.0 2.0  
1.8 1.8  
1.6 1.6  
1.4 1.4  
1.2 1.2  
¯s(t)1.0 ˆs[n]1.0  
0.8 0.8  
0.6 0.6  
0.4 0.4  
0.2 0.2  
0 0  
0 0.1 0.2 0.3 0.4 0(.5a) 0.6 0.7 0.8 0.9 1.00 2 4 6 8 1(0b) 12 14 16 18 20  
Time t/Ta Sample time nTa  
2.0 2.0  
1.8 1.8  
1.6 1.6  
1.4 1.4  
1.2 1.2  
s(t)1.0 ¯s[n]1.0  
0.8 0.8  
0.6 0.6  
0.4 0.4  
0.2 0.2  
0 0  
0 0.1 0.2 0.3 0.4 0(.5c) 0.6 0.7 0.8 0.9 1.00 2 4 6 8 1(0d) 12 14 16 18 20  
Figure 5.1: Signal courses  
Time discrete Time continuous Value discrete Value continuous Digital Analog  
× ×  
(a)  
× ×  
(b)  
× × ×  
(c)  
× × ×  
(d)  
(cid:88)(cid:88)  
0.5 points for each correctly filled row  
f)* What is the difference between Distance-Vector and Link-State routing protocols?  
2  
• Distance-Vector: Neighboring routers only exchange distances to destinations. Each router has only a local view of the network (direction and distance).  
• Link-State: Neighboring routers exchange topology information about the part of the network they know. Each router receives a complete view of the network.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
19 Name:  
g)* Justify whether Count-to-Infinity can occur in Link-State protocols.  
(cid:88)  
No, because each router has a global view of the network. Loops like those in Distance-Vector protocols are therefore excluded.  
h)* The figure below shows a measured course of the Congestion Window and the Congestion Threshold of a TCP connection. Mark and name the individual phases of TCP congestion control in the figure below.  
(cid:88)  
Congestion Avoidance Phase (linear growth)  
(cid:88)  
Two Slow Starts (exponential growth)  
i)* What is the purpose of flow control?  
1  
(cid:88)  
To prevent overload at the receiver.  
j)* What is the purpose of congestion control?  
1  
(cid:88)  
To prevent overload in the network.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 20  
k)* Given an alphabet with a total of different characters, whose occurrence probabilities are uniformly distributed. Justify whether the average codeword length when using Huffman  
2  
codes is greater than, equal to, or less than.  
5bit  
Since the characters are uniformly distributed, the Huffman code results from a complete binary tree with  
(cid:88)  
leaves of height . The codewords arise from the paths from the root to  
32 log (32) = 5 (cid:88)  
2  
the leaves and are therefore each long.  
5bit  
Notes:  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
21 Name:  
Additional space for solutions – please clearly mark the affiliation with the respective task and cross out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011  
Student ID: 22  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011