Name First Name
.................
Grade
Course of Study (Major) Field of Study (Minor)
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
Consent for Grade Announcement 8
via E-Mail / Internet
n
9
u
10
s
Exam Subject: Fundamentals of Computer Networks and Distributed Systems
ö
L
Examiner: Prof. Dr.-Ing. Georg Carle Date: 24.09.2012 (cid:80)
Lecture Hall: .................... Row: .................... Seat: .....................
To be filled out only by the supervisor:
Lecture hall left from ...... : ...... to ...... : ......
Submitted early at ....... : ......
Special Remarks:
Make-up Exam
Fundamentals of Computer Networks and Distributed Systems
Prof. Dr.-Ing. Georg Carle
Chair of Network Architectures and Network Services
Faculty of Computer Science
Technical University of Munich
Monday, 24.09.2012
11:00 – 12:30
• This exam consists of 23 pages and a total of 5 tasks, as well as an additional distributed
help sheet on protocol headers. Please check now that you have received a complete set of
materials.
• Please write your name and student ID in the header of each page.
• Do not write in red/green ink or with a pencil.
• The total number of points is 85.
• Allowed aids are a double-sided handwritten A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.
• Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
• Only results where a solution path is recognizable will be graded.
Text problems must generally be justified unless explicitly stated otherwise in the respective sub-task.
1 Name:
Task 1 NAT and Static Routing (Points)
15
Given the network topology from Figure 1.1. PC1 and PC2 are connected via a regular Ethernet switch to router R1, which provides access to the internet.
PC1
IP Address 10.0.0.1
Subnet Mask 255.255.240.0
eth0
Gateway 10.0.1.0
R1 R2 R3 SW2
10.0.1.0/20 87.186.224.45/30
P0
SW1 P1 eth0 wan0 wan0 eth0 P0
P2 87.186.224.46/30 P1
IP Address 10.0.0.2
eth0 Subnet Mask 255.255.240.0 eth0
Gateway 10.0.1.0
PC2 SRV
(www.google.de)
Figure 1.1: Network Topology
a)* Justify whether the address 10.0.1.0 is usable for the given prefix. If not, assign
1
a meaningful address to R1 in the same network.
10.0.1.0 is a valid host address in the network 10.0.0.0/20, as it is neither the first nor the last
(cid:88)
address in the subnet (immediately evident from the small prefix and the 1 in the 3rd octet).
b)* Determine the network address and broadcast address of the network in which PC1, PC2, and
1
R1 are located.
(cid:88) (cid:88)
Network address 10.0.0.0 and broadcast address 10.0.15.255
c)* How many IP addresses are available in this network for addressing devices?
1
(cid:88)
−
212 2 = 4094
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 2
d) Assign each PC1 and PC2 a meaningful IP address, subnet mask, and gateway address
so that they can establish a connection to the internet. Enter the values directly in
1 Figure 1.1.
e)* How many /20 subnets are there in the network 10.0.0.0/8?
1
(cid:88)
− −
220 8 = 224 12 = 4096
f)* Justify why R1 must support NAT for PC1 and PC2 to communicate with hosts on the internet.
PC1 and PC2 are in a private network, and their IP addresses are therefore not globally
(cid:88)
unique.
g)* What information must R1 at least hold in its NAT table?
1
Local IPs of the PCs, local port numbers, and global source port numbers. (global IP not necessary,
as R1 only has one global IP address; destination port numbers are not required for the basic tasks)
In the following, we will abbreviate IP and MAC addresses according to the scheme
<DeviceName>.<Interface>
, e.g. . Note that for the two following sub-tasks,
R1.wan0
there are three additional routers between R2 and R3. PC1 is now accessing the website
http://www.google.de.
h) Complete the header fields for the request from PC1 to www.google.de in the three empty boxes
4
in Figure 1.2. If a field is not clearly defined, make a reasonable choice.
i) Complete the header fields for the response from www.google.de to PC1 in the three empty boxes
4
in Figure 1.3. If a field is not clearly defined, make a reasonable choice.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
3 Name:
)
e
d
.
e
l
W2 RVoog
S 1 0 Sg
P h .
t w
0 e
P w
w
0 0
0h0h (
htnt
teae 0
e.w. 0 0
.V.V 0 th
3R1R800 e
RSRS528
3
R
tt
CC rr
AAPP oo
MMII PP
ctctLct
rsrsTrs
SDSDTSD
e
gi
o
ol
p
o
2 zt
R et
N
n0 1.2:
a g
w n
u
d
0 bil
b
000h A
nnnt
aaae 0
www. 0
...V 0
121R300 0
RRRS628 an 0 00
w h0hh
thtt
ACACPP ortort R1 1.e.et1.eV.e 000
MMII PP C1CR400
rcstrcstTLrcst h0 PRPS628
SDSDTSD t
e
tt
CC rr
AAPP oo
MMII PP
ctctLct
rsrsTrs
SDSDTSD
1
0 P 0
h h
1 et P0 P2 et 2
C C
P P
1
W
S
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 4
)
e
d
.
e
l
W2 RVoog
S 1 0 Sg
P h .
t w
0 e
P w
w
0 0
h0h0 (
thtn
etea 0
.e.w 0 0
V.V. 0 th
R3R1400 e
SRSR682
3
R
tt
CC rr
AAPP oo
MMII PP
ctctLct
rsrsTrs
SDSDTSD
e
gi
o
ol
p
o
2 zt
R et
N
n0 1.3:
a g
w n
u
d
0 bil
b
00h0 A
nntn
aaea 0
ww.w 0
..V. 0
21R1900 0
RRSR582 an 000
w 0hhh
httt
ACACPP ortort R1 .et1.eV.e1.e 000
MMII PP 1CRC800
rcstrcstTLrcst h0 RPSP582
SDSDTSD t
e
tt
CC rr
AAPP oo
MMII PP
ctctLct
rsrsTrs
SDSDTSD
1
0 P 0
h h
1 et P0 P2 et 2
C C
P P
1
W
S
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
5 Name:
Task 2 Packet Pair Probing (Points)
15
Given the simplified network topology from Figure 2.1. Nodes 1 and 4 are connected to their routers
15
via a full-duplex capable local network. The symmetric data rates are
r r d d
12 34 12 34
and . The two distances and are negligible. The connection between
r < r ,r d
23 12 34 23
routers 2 and 3 is significantly slower. Thus, it holds that . The distance cannot be
r
23
neglected.
The transmission rate is to be determined from node 1, generating as little load as possible on the
r
23
already slow connection. The method should work with all nodes that have a regular IP stack.
r r r
12 23 34
1 2 3 4
Figure 2.1: Simplified Network Topology
In this task, we will first derive a general method that allows node 1 to determine the
transmission rate in question. Subsequently, we will evaluate the method for specific numerical values.
a)* Provide the serialization time and propagation delay between two
ts(i,j) tp(i,j) 1
nodes generally as a function of packet size , data rate, and distance.
p r d
ij ij
p (cid:88)
t (i,j) =
s
r
ij
d (cid:88)
ij
t (i,j) =
p
νc
For a successful and as accurate as possible determination of the rate, it is important that packets sent from 1 to 4
r
23
are as large as possible but not fragmented.
b)* Briefly explain how node 1 can determine the maximum MTU on the entire path to node 4.
1 sends a packet with the MTU of the local segment and sets the DF bit (do not fragment) in the
IP header. If this MTU is larger than on the segment between 2 and 3, then 2 will discard the packet
and send an appropriate ICMP message back to 1. This contains the maximum
(cid:88)(cid:88)
MTU on the segment from 2 to 3.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 6
Node 1 then sends two ICMP Echo Requests of length to node 4 one after the other. You
p
can assume that no other traffic influences the transmission. The length is chosen so that no fragmentation is necessary. Any processing times at the nodes are neglected.
c)* How will node 4 respond when it receives the ICMP Echo Requests from node 1?
1
(cid:88)
For each request, a reply (of the same size) is sent back (immediately).
d) Complete the path-time diagram shown in the solution field.
3
1 2 3 4
∆t
(cid:88)
(e)
(cid:88) (cid:88) (cid:88)
t
Due to the low transmission rate between nodes 2 and 3, a reception pause occurs at node 1
. This can be measured by node 1 and used to determine the transmission rate between nodes 2
∆t
and 3.
e) Mark in your solution from sub-task d).
1 ∆t
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
7 Name:
f) Describe in words the general influence of on the reception pause .
r ∆t
34
If is too low (i.e., large), a send pause can occur at node 3 on the return path between the two packets. This occurs only when is smaller than
(cid:88)(cid:88) r
3,4
than . Otherwise has no influence.
r r
2,3 3,4
g) What condition must be exactly fulfilled for the method to work? (Formula!)
r34 1
(cid:88)
r > r
34 23
h) Provide an expression for . Simplify this as much as possible.
∆t 2
(cid:88)(cid:88)
− p − p
∆t = t (2,3) t (1,2) =
s s
r r
23 12
i) Provide an expression for the sought data rate. Simplify this as much as possible.
r23 1
(cid:88)
p
r =
23 ∆t+ p
r12
Repeated measurements from node 1 yield an average value for a packet size
∆t = 108µs
of . The transmission rate is .
p = 1500Byte r 1Gbit/s
12
j) Determine the numerical value in .
r23 Mbit/s 1
(cid:88)
p
r = = 100Mbit/s
23 ∆t+ p
r34
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 8
Task 3 IP Fragmentation (Points)
18
In Figure 3.1, an arrangement of network components with their IP and MAC addresses is shown. The two computers PC1 and PC2 use their respective local router as the default gateway. The MTU on the WAN link between R1 and R2 is . Within the local networks, the common MTU for Ethernet is
580Byte
1500Byte
PC1 PC2
L2: af:fe:14:af:fe:20 L2: af:fe:14:af:fe:25
L3: 192.168.1.1/24 L3: 192.168.2.1/24
eth0 wan0 wan0 eth0
L2: af:fe:14:af:fe:21 L2: af:fe:14:af:fe:22 L2: af:fe:14:af:fe:23 L2: af:fe:14:af:fe:24
SW1 L3: 192.168.1.254/24 R1 L3: 192.168.5.33/30 L3: 192.168.5.34/30 R2 L3: 192.168.2.254/24 SW2
Figure 3.1: Network Topology
a)* Justify whether the switches SW1 and SW2 need their own MAC address for their basic tasks. If necessary, add these to Figure 3.1.
No device communicates directly with(cid:88) the switch – switches operate at layer 2 and are transparent to the
connected devices.
b)* What is the significance of the two header fields "Identifier" and "Fragment Offset"?
2
(cid:88)
• Identifier: Unique identification of all fragments belonging to a packet.
• Fragment Offset: Allows the reassembly of fragments in the correct order.
(cid:88)
c)* Which protocol is used to translate IP addresses into MAC addresses?
1
(cid:88)
ARP
d)* Justify whether PC1 needs the MAC address of PC2 to send a packet to PC2.
No, it only needs the IP address of PC2. MAC addresses are only used for addressing within
(cid:88)
a subnet, not for end-to-end addressing.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
9 Name:
In the following, the transmission of the IP packet schematically represented in Figure 3.2 will be traced with all necessary intermediate steps. Use the protocol headers and additional information depicted on the supplementary sheet if needed.
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031
ToS
0x4 0x5 1220(10)
7261 0 0 0 0
(10) (10)
Protocol Header Checksum
64
(10)
192.168.1.1
192.168.2.1
Payload
Figure 3.2: Schematic Representation of the IP Packet Sent by PC1
e)* What is the size of the IP header of the packet shown in Figure 3.2?
1
(cid:88)
20Byte
f)* How large is the payload of the packet shown in Figure 3.2?
1
(cid:88)
−
1220Byte 20Byte = 1200Byte
g)* Which parts of the layer-2 PDU count towards the MTU?
1
(cid:88)
The entire payload (layer-2 SDU), i.e., the IP packet including the IP header.
h)* At what point in the network does fragmentation occur?
1
(cid:88)
At R1.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 10
i) Into how many fragments is the sent packet divided?
(cid:24) (cid:25)
1
− (cid:88)
1220Byte 20Byte
N = − = 3
580Byte 20Byte
j)* Justify why fragments can be forwarded independently of each other.
1
Each fragment receives its own IP header and thus has all the necessary information, so
(cid:88)
that routers can forward fragments independently of each other.
(cid:88)
(Argumentation about identifier without mentioning address information)
k) For what reason can the reassembly of packets generally only take place at the receiver?
1
Individual fragments can generally be forwarded via different paths to the receiver.
(cid:88)
Reassembly is therefore only possible again at the receiver.
Figure 3.3 shows the headers of the individual IP fragments (there may be more fragments printed than are actually needed). The header fields ToS, Protocol, and Header Checksum can be ignored.
l) Fill in the omitted header fields for all fragments that are sent over the connection between R1 and R2 in
4
Figure 3.3.
m)* What changes (with justification!) were made in IP fragmentation with IPv6?
(cid:88)
No fragmentation during forwarding, only at the sender itself. This has efficiency reasons:
Instead of potentially fragmenting each packet multiple times on the way to the receiver, the sender
(cid:88)
is informed about the problem once. This allows the sender to adjust its MTU accordingly.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
11 Name:
Fragment 1
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031
ToS
0x4 0x5 580(10)
7261 0 0 1 0
(10) (10)
Protocol Header Checksum
63
(10)
192.168.1.1
192.168.2.1
Payload
Fragment 2
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031
ToS
0x4 0x5 580(10)
7261 0 0 1 70
(10) (10)
Protocol Header Checksum
63
(10)
192.168.1.1
192.168.2.1
Payload
Fragment 3
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031
ToS
0x4 0x5 100(10)
7261 0 0 0 140
(10) (10)
Protocol Header Checksum
63
(10)
192.168.1.1
192.168.2.1
Payload
Fragment 4
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031
ToS
Protocol Header Checksum
Payload
Figure 3.3: Solution Template for Subtask l)
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 12
Task 4 Protocol Dissemination (Points)
23
We consider the network from Figure 4.1, which does not include switches for clarity. You can assume that all the connections drawn represent Fast Ethernet segments. You are trying to establish a TCP connection from PC1 to the server. This fails, although you assume that routers RA - RD are correctly configured and that the server accepts incoming TCP connections. An error on PC1 is excluded.
RD
PC1 RA RC Server
173.194.35.152
RB
Figure 4.1: Simplified Network Topology (Switches between the devices are not drawn for clarity)
You decide to check the network traffic at PC1 with a sniffer while you try to connect to the server again. You record the message addressed to PC1 as shown in Figure 4.1. This message is printed as a hex dump in Figure 4.2. The left column indicates the offset (hexadecimal) in multiples of bytes. The next two columns represent the data (hexadecimal) in blocks of 8 bytes in network byte order.
0000 28 37 37 02 32 41 00 25 90 57 1f dc 08 00 45 00
0010 00 38 b2 40 00 00 3f 01 b1 57 83 9f fc 95 83 9f
0020 14 59 0b 00 5e a4 00 00 00 00 45 00 00 40 16 17
0030 40 00 01 06 fa 4e 83 9f 14 59 ad c2 23 98 e8 fc
0040 01 bb 22 67 a5 d2
Figure 4.2: Hex Dump of the Message Shown in Figure 4.1 (including L2 header) in Network Byte Order.
In the following, we will examine this message step by step to find out why the server is unreachable. Use the protocol headers and additional information depicted on the supplementary sheet to solve the problem.
1 a)* Explain the terms "Little-Endian" and "Big-Endian".
Difference: Position of the most significant byte within a datum that is longer than 1 byte. Little-Endian = least significant byte at the least significant address, Big-Endian = least significant byte
(cid:88)
at the most significant address.
1 Program for recording traffic, e.g., Wireshark or tcpdump
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
13 Name:
b) Which byte order corresponds to network byte order and which is used by x86-based computers?
1
(cid:88) (cid:88)
Network byte order = Big-Endian, x86 host byte order = Little-Endian.
For the following sub-tasks, it will be helpful if you mark the beginning and end of each header in Figure 4.2. Please note that the following sub-tasks will only be graded if it is clear how you arrived at the answer (e.g., indicating the values of the relevant header fields).
c)* Provide the offset for the first and last byte of the Ethernet header from the start of the frame 1
(cid:88)
–
0x0000 0x000D
d) Determine the MAC address of RA. 1
(cid:88)
00:25:90:57:1f:dc
e) Determine the MAC address of PC1. 1
(cid:88)
28:37:37:02:32:41
f) Which L3 protocol is in use (with justification for how you recognize this). 1
(cid:88)
Type field in the Ethernet header: (Big-Endian) = IPv4
08 00
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 14
g) Provide the offset for the first and last byte of the L3 header from the start of the frame.
1 (cid:88)
–
0x000E 0x0021
1 h) Provide the L3 address of PC1 in the usual notation.
(cid:88)
PC1 = = 131.159.20.89
83 9f 14 59
1 i) Does the message come from the server?
(cid:88)
(cid:54)
No, = 131.159.252.149 173.194.35.152
83 9f fc 95 =
1 j) Determine the TTL of the message.
(cid:88)
TTL field = 63
0x3f
1 k) From which device does the message most likely originate?
Assuming that packets are sent with the default value TTL=64, RB or
(cid:88)
RD are possible. (also correct: RA, if argued with default value TTL=63)
1 l) Which protocol follows the L3 header?
(cid:88)
IP Protocol = ICMP
0x01
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
15 Name:
m) Specify the message type that follows the L3 header as precisely as possible.
1
ICMP Type 11 Code 0 (TTL exceeded in transit)
n) Describe in words (or by sketch) the general content of the message that follows the L3 header.
Directly from the supplementary sheet: IP header and the first 8 bytes of the payload of the packet that triggered the ICMP message.
After the previous investigation, there is a suspicion that this message is a response to another message that was previously sent by PC1. This suspicion will be confirmed in the following.
o) Determine the recipient of this previous message. 1
(cid:88)
Destination address = (Big-Endian) = 173.194.35.152 = Server
ad c2 23 98
p) What was the length of this message in bytes? 1
(cid:88)
−
Total-Length - IP-Header-Length =
64Byte 20Byte = 44Byte
q) What TTL did this message have last? 1
(cid:88)
TTL = = 1
0x01
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 16
r) What L4 protocol was used in this message?
1 (cid:88)
IP Protocol = TCP
0x06
1 s) Provide the source port number of this message.
(cid:88)
Source port = (Big-Endian) = 52567
e8 fc
1 t) Provide the destination port number of this message.
(cid:88)
Destination port = (Big-Endian) = 443
01 bb
1 u) What protocol was used at the application layer?
(cid:88)
TCP 443 = HTTPS
2 v) Describe the problem that prevents PC1 from establishing a connection to the server.
The server is only four hops away from PC1. The only reason (aside from a TTL that is set too low, which is excluded by the task) is a routing loop between the four routers. The packet is forwarded in a circle until the TTL expires. PC1 is informed about this by an ICMP message from the respective router.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
17 Name:
Task 5 Short Questions (Points)
14
The following short questions are independent of each other. Bullet-point answers 14
are sufficient!
a)* Describe the key exchange using DH76 between two communication partners Alice
3
and Bob. Explain what information is exchanged. It is not necessary to provide formulas. If you use variable names, explain their meaning!
• Alice and Bob agree in advance on a prime number and a generator (primitive congruence
(cid:88) p g
root).
• Alice and Bob each generate a random number and calculate using and these random
a,b p,g (cid:88)
numbers nonces , which can be exchanged over the insecure channel.
A,B
(cid:88)
• Alice can now calculate the shared secret with and Bob with the shared secret.
a,B,p,g b,A,p,g K
b)* Justify whether an attacker who observes the DH76 key exchange can also calculate the key.
and are not transmitted in clear text. With the correct choice of not (too complex / discrete
A B (cid:88) g,p
logarithm).
c)* Justify whether Alice can generally be sure that she is really communicating with Bob after the key exchange.
No. An attacker can impersonate Alice and Bob to each other during the key exchange (Man-in-the-Middle).
(cid:88)
d)* What are CRC checksums used for?
1
(cid:88)
Detection (not correction) of transmission errors.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 18
e)* What is the difference between circuit switching and packet switching?
1 Circuit switching = reservation of a dedicated line (physically or logically) between sender and receiver.
(cid:88)
Packet switching = sending independent packets with their own addressing information.
f)* Given the message to be sent in binary notation and the generator polynomial
00101101
2
. Determine the message secured by CRC.
g(x) = x3+x2+1
g(x) = 1101
00101101 000 : 1101 = 0011001, Remainder: 010
⇒
to be sent is
00101101 010
(cid:88)
• Approach (appending zeros + division by in binary notation)
g(x)
(cid:88)
• Correct remainder (calculation)
(cid:88)
• Indication of the entire message to be sent
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
19 Name:
g)* Sketch the TCP connection establishment (indicating sequence numbers and flags) as a simplified path-time diagram (serialization time and propagation delay can be neglected).
3
SYN,SEQ=N
SYN,SEQ=M,ACK=N+1
SEQ=N+1,ACK=M+1
(cid:88)
It is recognizable that(cid:88) this is a 3-way handshake
Correct flags (cid:88)
Correct sequence and acknowledgment numbers
h)* Briefly describe (two bullet points are sufficient) the principle of token passing.
1
(cid:88)
• Token is passed from one station to the next.
(cid:88)
• Only the station that currently holds the token is authorized to send.
i)* What are routing protocols used for?
1
Automated determination of the shortest paths (according to a certain metric) between all nodes
(cid:88)
in a network and exchange of this information between routers.
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 20
Additional space for solutions – please clearly mark the affiliation with the respective task and cross out invalid solutions!
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
21 Name:
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
Student ID: 22
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012
23 Name:
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012