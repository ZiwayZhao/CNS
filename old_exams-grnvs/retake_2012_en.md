Name First Name  
..................  
Grade  
Degree Program (Major) Field of Study (Minor)  
I II  
Student ID  
Signature of the Candidate 1  
2  
TECHNICAL UNIVERSITY OF MUNICH  
3  
Faculty of Computer Science  
Midterm Exam 4  
× Final Exam  
5  
Semester Exam  
Diploma Preliminary Exam 6  
Bachelor Exam  
............................ 7  
Consent to Release Grades 8  
via E-Mail / Internet  
9  
10  
Exam Subject: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle Date: 24.09.2012 (cid:80)  
Lecture Hall: .................... Row: .................... Seat: .....................  
To be filled out by the supervisor only:  
Lecture hall exited from ...... : ...... to ...... : ......  
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
• This exam consists of 23 pages and a total of 5 tasks, along with an additional distributed  
help sheet for protocol headers. Please check now that you have received a complete set of  
materials.  
• Please write your name and student ID in the header of each page.  
• Do not write in red/green ink or with a pencil.  
• The total number of points is 85.  
• Allowed materials include a double-sided handwritten DIN A4 sheet and a non-programmable  
calculator. Please remove all other materials from your desk and turn off your mobile phones.  
• Tasks marked with * can be solved without knowledge of the results of preceding sub-tasks.  
• Only results where a solution method is recognizable will be graded. Text problems must be  
justified unless explicitly stated otherwise in the respective sub-task.  
1 Name:  
Task 1 NAT and Static Routing (Points)  
15  
Given the network topology from Figure 1.1. PC1 and PC2 are connected via a regular Ethernet  
switch to router R1, which provides access to the Internet.  
PC1  
IP Address  
Subnet Mask  
eth0  
Gateway  
R1 R2 R3 SW2  
10.0.1.0/20 87.186.224.45/30  
P0  
SW1 P1 eth0 wan0 wan0 eth0 P0  
P2 87.186.224.46/30 P1  
IP Address  
eth0 Subnet Mask eth0  
Gateway  
PC2 SRV  
(www.google.de)  
Figure 1.1: Network Topology  
a)* Justify whether the address 10.0.1.0 is usable for the given prefix. If not, assign a  
meaningful address in the same network to R1.  
1  
b)* Determine the network address and broadcast address of the network in which PC1, PC2, and  
R1 are located.  
1  
c)* How many IP addresses are available in this network for addressing devices?  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 2  
d) Assign each PC1 and PC2 a meaningful IP address, subnet mask, and gateway address so that they can  
establish a connection to the Internet. Enter the values directly into Figure 1.1.  
1  
e)* How many /20 subnets are there in the network 10.0.0.0/8?  
1  
f)* Justify why R1 must support NAT so that PC1 and PC2 can communicate with hosts on the Internet.  
1  
g)* What information must R1 at least maintain in its NAT table?  
1  
In the following, we will abbreviate IP and MAC addresses according to the scheme  
<Device Name>.<Interface>, e.g. R1.wan0. Note that for the two following sub-tasks, there are three  
additional routers between R2 and R3. PC1 is now accessing the website  
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
(  
0  
h  
t  
e  
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
bil  
b  
A  
0  
n  
a  
w  
tt  
CC rr 1  
AAPP oo R  
MMII PP  
ctctLct  
rsrsTrs h0  
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
(  
0  
h  
t  
e  
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
bil  
b  
A  
0  
n  
a  
w  
tt  
CC rr 1  
AAPP oo R  
MMII PP  
ctctLct  
rsrsTrs h0  
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
and . The two distances and are negligible. The connection between  
12 34 12 34  
routers 2 and 3 is significantly slower. Thus, it holds that . The distance is not to  
r < r ,r d  
23 12 34 23  
be neglected.  
The transmission rate is to be determined by node 1, generating as little load as possible on the  
r  
23  
already slow connection. The method should work with all nodes that have a regular IP stack.  
r r r  
12 23 34  
1 2 3 4  
Figure 2.1: Simplified Network Topology  
In this task, we will first derive a general method that allows node 1 to determine the  
questionable transmission rate. Subsequently, we will evaluate the method for specific numerical values.  
a)* Provide the serialization time and propagation delay between two nodes in general, depending on the  
packet size , data rate, and distance .  
p r d  
ij ij  
For a successful and as accurate as possible determination of the rate, it is important that packets sent from  
1 to 4 are as large as possible but not fragmented.  
b)* Briefly explain how node 1 can determine the maximum MTU along the entire path to node 4.  
2  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 6  
Node 1 now sends two ICMP echo requests of length to node 4 one after the other. You can  
p  
assume that no other traffic affects the transmission. The length is chosen so that no fragmentation is  
necessary. Any processing times at the nodes are neglected.  
c)* How will node 4 respond when it receives the ICMP echo requests from node 1?  
1  
d) Complete the path-time diagram shown in the solution field.  
3  
1 2 3 4  
t  
Due to the low transmission rate between nodes 2 and 3, a reception pause occurs at node 1.  
This can be measured by node 1 and used to determine the transmission rate between nodes 2  
∆t  
and 3.  
e) Mark in your solution from sub-task d).  
1 ∆t  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
7 Name:  
f) Describe in words the general influence of on the reception pause .  
r ∆t  
34  
2  
g) What condition must be met for the method to work? (Formula!)  
r34 1  
h) Provide an expression for . Simplify it as much as possible.  
∆t 2  
i) Provide an expression for the sought data rate. Simplify it as much as possible.  
r23 1  
Repeated measurements from node 1 yield an average value with a packet size  
∆t = 108µs  
of . The transmission rate is .  
p = 1500Bytes r 1Gbit/s  
12  
j) Determine the numerical value in .  
r23 Mbit/s 1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 8  
Task 3 IP Fragmentation (Points)  
18  
In Figure 3.1, an arrangement of network components with their IP and MAC addresses is shown.  
The two computers PC1 and PC2 use their respective local router as the default gateway. The  
MTU on the WAN link between R1 and R2 is . Within the local networks, the  
580Bytes  
standard MTU for Ethernet is .  
1500Bytes  
PC1 PC2  
L2: af:fe:14:af:fe:20 L2: af:fe:14:af:fe:25  
L3: 192.168.1.1/24 L3: 192.168.2.1/24  
eth0 wan0 wan0 eth0  
L2: af:fe:14:af:fe:21 L2: af:fe:14:af:fe:22 L2: af:fe:14:af:fe:23 L2: af:fe:14:af:fe:24  
SW1 L3: 192.168.1.254/24 R1 L3: 192.168.5.33/30 L3: 192.168.5.34/30 R2 L3: 192.168.2.254/24 SW2  
Figure 3.1: Network Topology  
a)* Justify whether switches SW1 and SW2 need their own MAC address for their basic tasks. If necessary,  
add these in Figure 3.1.  
1  
b)* What is the significance of the two header fields "Identifier" and "Fragment Offset"?  
2  
c)* Which protocol is used to translate IP addresses into MAC addresses?  
1  
d)* Justify whether PC1 needs the MAC address of PC2 to send a packet to PC2.  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
9 Name:  
In the following, the transmission of the IP packet schematically represented in Figure 3.2 will be traced  
with all necessary intermediate steps. Use the protocol headers and additional information depicted on the  
supplementary sheet if needed.  
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
e)* What size does the IP header of the packet shown in Figure 3.2 have?  
1  
f)* How large is the payload of the packet shown in Figure 3.2?  
1  
g)* Which parts of the Layer 2 PDU count towards the MTU?  
1  
h)* At what point in the network does fragmentation occur?  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 10  
i) Into how many fragments is the sent packet divided?  
1  
j)* Justify why fragments can be forwarded independently of one another.  
1  
k) For what reason can the reassembly of packets generally only take place at the receiver?  
1  
Figure 3.3 shows the headers of the individual IP fragments (there may be more fragments printed than  
are actually needed). The header fields TOS, Protocol, and Header Checksum can be ignored.  
l) Fill in the omitted header fields for all fragments sent over the connection between R1 and R2 in  
Figure 3.3.  
4  
m)* What changes (with justification!) have been made in IP fragmentation with IPv6?  
2  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
11 Name:  
Fragment 1  
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031  
ToS  
Protocol Header Checksum  
Payload  
Fragment 2  
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031  
ToS  
Protocol Header Checksum  
Payload  
Fragment 3  
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031  
ToS  
Protocol Header Checksum  
Payload  
Fragment 4  
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031  
ToS  
Protocol Header Checksum  
Payload  
Figure 3.3: Solution Template for Sub-task l)  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 12  
Task 4 Protocol Dissemination (Points)  
23  
23 We consider the network from Figure 4.1, which does not include switches for clarity.  
You can assume that all depicted connections represent Fast Ethernet segments.  
You are trying to establish a TCP connection from PC1 to the server. This fails, although  
you assume that routers RA - RD are correctly configured and that the server accepts incoming TCP  
connections. An error on PC1 is excluded.  
RD  
PC1 RA RC Server  
173.194.35.152  
RB  
Figure 4.1: Simplified Network Topology (Switches between devices are not depicted for clarity)  
You therefore decide to check the network traffic at PC1 with a sniffer1 while you attempt to  
establish a connection to the server again. In doing so, you record the message addressed to PC1,  
which is depicted in Figure 4.1. This message is printed as a hex dump in Figure 4.2. The left column  
indicates the offset (hexadecimal) in multiples of bytes. The two subsequent columns represent the  
data (hexadecimal) in blocks of 8 bytes in Network Byte Order.  
0000 28 37 37 02 32 41 00 25 90 57 1f dc 08 00 45 00  
0010 00 38 b2 40 00 00 3f 01 b1 57 83 9f fc 95 83 9f  
0020 14 59 0b 00 5e a4 00 00 00 00 45 00 00 40 16 17  
0030 40 00 01 06 fa 4e 83 9f 14 59 ad c2 23 98 e8 fc  
0040 01 bb 22 67 a5 d2  
Figure 4.2: Hexdump of the message shown in Figure 4.1 (including L2 header) in Network Byte Order.  
In the following, we will examine this message step by step to find out why the server is not reachable.  
Use the protocol headers and additional information depicted on the supplementary sheet to solve the problem.  
1 a)* Explain the terms "Little-Endian" and "Big-Endian".  
1  
1 Sniffer program for recording data traffic, e.g., Wireshark or tcpdump  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
13 Name:  
b) Which byte order corresponds to Network Byte Order and which is used by x86-based computers?  
1  
For the following sub-tasks, it is helpful to mark the beginning and end of the respective headers in  
Figure 4.2. Please note that the following sub-tasks will only be graded if it is clear how you arrived at the answer (e.g., indicating the values of the relevant header fields).  
c)* Provide the offset from the start of the frame for the first and last byte of the Ethernet header.  
1  
d) Determine the MAC address of RA.  
1  
e) Determine the MAC address of PC1.  
1  
f) Which L3 protocol is in use (with justification for how you recognize this).  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 14  
g) Provide the offset from the start of the frame for the first and last byte of the L3 header.  
1  
h) Provide the L3 address of PC1 in the usual notation.  
1  
i) Does the message originate from the server?  
1  
j) Determine the TTL of the message.  
1  
k) From which device does the message most likely originate?  
1  
l) Which protocol follows the L3 header?  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
15 Name:  
m) Specify the type of message that follows the L3 header as precisely as possible.  
1  
n) Describe in words (or by sketch) the general content of the message that follows the L3 header.  
After the previous investigation, there is a suspicion that this message is the response to another message  
that was previously sent by PC1. This suspicion will be confirmed in the following.  
o) Determine the recipient of this previous message.  
1  
p) What length did this message have in bytes?  
1  
q) What was the last TTL of this message?  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 16  
r) Which L4 protocol was used in this message?  
1  
s) Provide the source port number of this message.  
1  
t) Provide the destination port number of this message.  
1  
u) Which protocol was used at the application layer?  
2  
v) Describe the problem that prevents PC1 from establishing a connection to the server.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
17 Name:  
Task 5 Short Questions (Points)  
14  
The following short questions are independent of each other. Bullet-point answers are sufficient!  
14  
a)* Describe the key exchange using DH76 between two communication partners Alice  
3  
and Bob. Explain what information is exchanged. It is not necessary to provide formulas. If you use  
variable names, explain their meaning!  
b)* Justify whether an attacker observing the DH76 key exchange can also compute the key.  
1  
c)* Justify whether Alice can generally be sure that she is indeed communicating with Bob after the  
key exchange.  
1  
d)* What are CRC checksums used for?  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 18  
e)* What is the difference between circuit switching and packet switching?  
1  
f)* Given the sending message in binary notation and the generator polynomial  
00101101  
2  
. Determine the message secured by CRC.  
g(x) = x3+x2+1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
19 Name:  
g)* Sketch the TCP connection establishment (indicating sequence numbers and flags) as a simplified  
path-time diagram (serialization time and propagation delay can be neglected).  
3  
h)* Briefly describe (two bullet points are sufficient) the principle of token passing.  
1  
i)* What are routing protocols used for?  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 20  
Additional space for solutions – please clearly mark the association with the respective task and strike out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
21 Name:  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 22  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
23 Name:  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012