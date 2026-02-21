Name First Name
.................
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
Diploma Preliminary Examination 6
Bachelor Examination
............................ 7
Consent to Release Grades 8
via E-Mail / Internet
9
10
Subject of Examination: Fundamentals of Computer Networks and Distributed Systems
Examiner: Prof. Dr.-Ing. Georg Carle Date: 09.08.2013
Lecture Hall: .................... Row: .................... Seat: .....................
To be filled out by the supervisor only:
Lecture hall exit from ...... : ...... to ...... : ......
Submitted early at ....... : ......
Special Remarks:
Endterm Exam
Fundamentals of Computer Networks and Distributed Systems
Prof. Dr.-Ing. Georg Carle
Chair of Network Architectures and Network Services
Faculty of Computer Science
Technical University of Munich
Friday, 09.08.2013
11:30 – 13:00
• This exam consists of 23 pages and a total of 6 tasks. Please check now that you have received a complete set of materials.
• Please write your name and student ID in the header of each page.
• Do not write in red/green ink or with a pencil.
• The total number of points is 85.
• Allowed aids are a double-sided handwritten DIN A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.
• Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
• Do not spend too long on any (sub-)task. If you cannot solve a task immediately, it is better to move on to the next task.
• Only those results will be counted where a solution method is recognizable. Text tasks must be justified unless explicitly stated otherwise in the respective sub-task.
1 Name:
Task 1 Sampling and Quantization (18 points)
18
Given is the time- and value-continuous baseband signal on the receiver side from Figure 1.1. This signal is to be sampled, quantized, and finally decoded during this task.
1.00
Signals(t)
0.75
0.50
0.25
t) 0.00
(
s
-0.25
-0.50
-0.75
-1.00
0 0.25 0.50 0.75 1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75 3.00 3.25 3.50 3.75 4.00
t[s]
Figure 1.1: Time- and value-continuous signal on the receiver side
g (t)
s
Q
1
00 01 11 10
I
0.5
[ ]
t s
− −
0.50 0.25 0 0.25 0.50
(a) Signal space assignment (b) Return-to-Zero sending basic pulse
Figure 1.2: Sending basic pulse and signal space assignment
It is known that the signal in Figure 1.1 is an RZ-coded (Return-to-Zero) signal. The modulation alphabet used is shown in Figure 1.2a.
a)* Name two channel influences that are visible in the signal progression of Figure 1.1. 1
b)* What modulation method is used according to Figure 1.2a? 1
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 2
c)* Draw the Return-to-Zero sending basic pulse with normalized amplitude of 1 in the time domain in Figure 1.2b.
1 t [ 0.5,0.5]
d) Assume the basic pulse from Figure 1.2b is to be sampled with the sampling frequency 
1 f = 2Hz
a
. Mark the sampling time points directly in Figure 1.2b.
∈
2 e) Sample the signal from Figure 1.1 with the sampling frequency in the range 
f = 2Hz t [0,4]
a
. Enter the time-discrete signal directly in Figure 1.1.
Note: Pay attention to correct sampling time points according to your solution from part c). The use of a ruler is allowed.
The quantization interval, within which the quantization error is to be minimized, is 
−
. The step size is . Arithmetic rounding is used for quantization.
I = [ 1,1] ∆ = 0.5
1 f)* Calculate the number of quantization levels.
1 g)* Provide the quantization levels as numerical values. Enter these directly in Figure 1.2a below the respective codewords.
2 h) Draw the time- and value-discrete signal in the coordinate system below.
| |
Note: Signal amplitudes are interpreted as resting potential and mapped to the value 0
s(t) < 0.1
1.00
0.75
0.50
0.25
t) 0.00
(
s
-0.25
-0.50
-0.75
-1.00
0 0.25 0.50 0.75 1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75 3.00 3.25 3.50 3.75 4.00
t[s]
2 i) Provide the received bit sequence.
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
3 Name:
j)* Justify whether Return-to-Zero is a DC-free line code. 1
k)* Justify whether automatic clock recovery is possible when using Return-to-Zero. 1
The received bit sequence is protected by a very simple channel code. To this end, the sender appends a so-called parity bit to each group of 3 bits, which is 0 if the preceding 3 bits contain an even number of ones. Otherwise, the parity bit is 1.
3 bits
l)* Justify which bit errors can be detected using the parity bit. 1
m)* Justify which bit errors can be corrected using the parity bit. 1
n) Mark the parity bits in your solution from part i). 1
o) Check the received bit sequence for transmission errors. 1
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 4
Task 2 Time Synchronization (11 points)
11
A hypothetical pico-satellite is in a low Earth orbit. We consider the moment when it has a distance of 
to the ground station on the Earth's surface. It 
1500km A
is thus directly between the ground station and another identical satellite in 
C
a higher orbit, which has a distance of 
to the ground station. 
3000km
Earth
A B C
1500km 1500km
The modems of the satellites can send at and receive at . The ground 
14.4kbit/s 56.0kbit/s
station sends and receives at the maximum data rates that the satellites support. Assume 
≈
the speed of light on all paths is · 
c 3 108m/s
The satellite wants to synchronize its onboard clock with the time of the ground station. To do this, the following simple protocol is executed: 
B
sends a long request to the ground station. It responds 
B 64B
with a long frame containing the current time of the ground station. Processing times 
64B
at the endpoints are to be neglected in this task.
1 a)* Determine the serialization times and between the ground station and 
t (A,B) t (B,A) A
the satellite . 
B
1 b)* Determine the propagation delay between the ground station and the 
t (A,B) A
satellite . 
B
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
5 Name:
c) Draw the request from the satellite and the response from the ground station in the following 
B A
time-distance diagram. The request is sent at time. 
t = 0ms 2
0
(Scale: horizontal (cid:44) , vertical (cid:44) )
1cm 250km 1cm 10ms
A B C
t = 0ms
0
t
d) Mark the serialization times and as well as the propagation delay 2
t (A,B) t (B,A)
s s
and the Round-Trip Time (RTT) in your solution from part c).
t (A,B)
p
Due to the serialization and propagation delays, the time sent by the ground station does not match the time received by the satellite exactly. The satellite estimates the actual 
B
time by adding half the RTT to the received time. This results in an error , 
∆t
which is to be determined below.
e) Calculate the RTT from the perspective of the satellite . 1
B
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 6
f)* Justify why the correct time is not calculated when adding half the RTT to the received time. 1
1 g) In the described method, the satellite adds the correction to the received time. 
t
c,S
Calculate .
t
c,S
1 h) Calculate the correct correction value that the satellite should use to determine the current 
t
c
time. 
1 i) Calculate the absolute error that the satellite makes with the described method. 
∆t
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
7 Name:
Task 3 NAT and Static Routing (15 points)
15
Given is the network topology from Figure 3.1. PC1 and PC2 are connected via a regular Ethernet 
Switch SW1 with Router R1, which provides access to the Internet.
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
Figure 3.1: Network topology
a)* Justify whether the address 10.0.1.0 is usable for the given prefix. If not, assign 
1
a sensible address in the same network to R1.
b)* Determine the network address and broadcast address of the network in which PC1, PC2, and 
1
R1 are located.
c)* How many IP addresses are available in this network for addressing devices? 
1
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 8
d) Assign PC1 and PC2 a sensible IP address, subnet mask, and gateway address so that they can establish a connection to the Internet. Enter the values directly in 
1 Figure 3.1.
e)* How many /20 subnets are there in the network 10.0.0.0/8? 
1
f)* Justify why R1 must support NAT so that PC1 and PC2 can communicate with hosts on the Internet. 
1
g)* What information must R1 at least keep in its NAT table? 
1
In the following, we abbreviate IP and MAC addresses according to the scheme 
<DeviceName>.<Interface>
, e.g. . Note that for the two following sub-tasks, 
R1.wan0
there are three additional routers between R2 and R3. PC1 now accesses the website 
http://www.google.de.
h) Complete the header fields for the request from PC1 to www.google.de in the three empty boxes 
4
in Figure 3.2. If a field is not clearly defined, make a sensible choice.
i) Complete the header fields for the response from www.google.de to PC1 in the three empty boxes 
4
in Figure 3.3. If a field is not clearly defined, make a sensible choice.
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
9 Name:
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
n0 3.2:
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
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
11 Name:
Task 4 Wireshark (11 points)
11
Given is the network from Figure 4.1. A packet is sent from PC1 to PC2. The traffic is captured by PC1 using Wireshark. The decoded trace is shown in Table 1. Unfortunately, the timestamps have become a bit mixed up, which is why we have not printed them at all. The frames are therefore not presented in the order they were seen by PC1. This trace is to be analyzed and put in the correct order in the following sub-tasks.
MAC MAC MAC MAC
IP IP IP IP
PC1 RA RB PC2
MAC MAC
IP IP
Figure 4.1: Network topology
a)* First, explain the difference between MAC and IP addresses in terms of their use. 1
As mentioned at the beginning, the frames in Table 1 are not in the correct order. The identifiers 
A – H in the first column serve to refer to individual frames in the following sub-tasks.
b)* Briefly explain the purpose of frames B and G. 1
Note: The MAC address in frame G can be considered a broadcast address 
33:33:ff:00:00:01
( ).
ff:ff:ff:ff:ff:ff
c)* Explain how frame H can occur. 1
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 12
Id. in out Nr. Output
Ethernet II, 90:e2:ba:2a:d2:a3 -> 90:e2:ba:2a:8d:0f, Length: 1294
A
fc00::10 -> fc00::2:10, IPv6, Length: 1294
IPv6 fragment (nxt=ICMPv6 (58) off=0 id=0x7c0d6306)
Ethernet II, 90:e2:ba:2a:8d:0f -> 90:e2:ba:2a:d2:a3, Type: IPv6 (0x86dd)
B
fc00::1 -> fc00::10, ICMPv6, Length: 86
Neighbor Advertisement: fc00::1 (rtr, sol, ovr) is at 90:e2:ba:2a:8d:0f
Ethernet II, 90:e2:ba:2a:8d:0f -> 90:e2:ba:2a:d2:a3, Length: 238
C fc00::2:10 -> fc00::10, ICMPv6, Length: 238
IPv6 fragment (nxt=ICMPv6 (58) off=154 id=0x7aef85b4)
Echo (ping) reply id=0x1dd7, seq=2
Ethernet II, 90:e2:ba:2a:d2:a3 -> 90:e2:ba:2a:8d:0f, Type: IPv6 (0x86dd)
D
fc00::10 -> fc00::2:10, ICMPv6, Length: 1462
Echo (ping) request id=0x1dd7, seq=1
Ethernet II, 90:e2:ba:2a:d2:a3 -> 90:e2:ba:2a:8d:0f, Length: 238
E fc00::10 -> fc00::2:10, ICMPv6, Length: 238
IPv6 fragment (nxt=ICMPv6 (58) off=154 id=0x7c0d6306)
Echo (ping) request id=0x1dd7, seq=2
Ethernet II, 90:e2:ba:2a:8d:0f -> 90:e2:ba:2a:d2:a3, Length: 1294
F
fc00::2:10 -> fc00::10, IPv6, Length: 1294
IPv6 fragment (nxt=ICMPv6 (58) off=0 id=0x7aef85b4)
Ethernet II, 90:e2:ba:2a:d2:a3 -> 33:33:ff:00:00:01, Type: IPv6 (0x86dd)
G
fc00::10 -> ff02::1:ff00:1, ICMPv6, Length: 86
Neighbor Solicitation: whois fc00::1 from 90:e2:ba:2a:d2:a3
Ethernet II, 90:e2:ba:2a:8d:0f -> 90:e2:ba:2a:d2:a3, Type: IPv6 (0x86dd)
H
fc00::1:2 -> fc00::10, ICMPv6, Length: 1294
Packet Too Big, MTU: 1280
Table 1: Capture of network traffic on PC1 in unsorted order.
d) Explain the relationship between frames A, D, and E. 2
1 e)* Determine the MTU on the link between RB and PC2. 
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
13 Name:
f)* For all frames in Table 1, determine whether they are incoming or outgoing frames from the perspective of PC1. Mark the corresponding field in the columns "in" or "out" 
1
in Table 1.
g) Now put the frames from Table 1 in a sensible order. Note the number of the packet starting from 1 in the column "Nr.".
h) Now enter – as far as this is evident from Table 1 – all MAC and IP addresses of the devices in 
2 Figure 4.1. If an entry from Table 1 is not evident, clearly cross out the corresponding field.
Note: The MAC address in frame G can be considered a broadcast address 
33:33:ff:00:00:01
(ff:ff:ff:ff:ff:ff) in this task.
1
It is a so-called multicast address, which addresses a group of stations within the local broadcast domain. However, this is not relevant for this task.
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 14
Task 5 Data Compression (20 points)
20
In this task, we consider a simplified version of the ITU T.30 protocol, better known as 
×
fax ("Fax"). Figure 5.1 shows a pixel-sized excerpt of a page that is to be transmitted via fax.
1
2
3
4
5
6
7
8
9
Figure 5.1: Excerpt of a black/white fax page. The numbers on the left margin indicate the line number.
Solution field for sub-task f)
A simple but inefficient way is to encode black pixels as a logical 0 and white pixels as a logical 1. We refer to this type of encoding as simple code.
1 a)* Determine the length of the data to be transmitted in bits when the page excerpt is encoded with this simple code.
2 b)* Determine the information content of the two codewords used.
Note: The page excerpt consists of 55 black pixels.
1 c) Determine the entropy of the page excerpt.
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
15 Name:
d) What can be concluded from the result of sub-task (c)? 1
For lossless compression, ITU T.30 uses a combination of run-length encoding (RLE) and subsequent Huffman coding. To do this, the number of consecutive pixels of the same color along with the respective color value (black or white) is encoded line by line, for example, for three consecutive white or four consecutive black pixels.
e)* Explain what is meant by lossless compression. 1
f)* Provide the third line of the page excerpt in Figure 5.1 run-length encoded in the solution field below Figure 5.1.
g)* The Huffman code is a so-called prefix-free code. Explain what is meant by this. 1
h) How does the use of prefix-free codes facilitate decompression? 1
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 16
Across the entire page excerpt, the RLE codewords with their corresponding absolute frequencies are listed in Table 2. The total number of RLE codewords for the complete excerpt is 95.
RLE Word Frequency Huffman Codeword
1s 35
2w 13
2s 10
3w 9
4w 7
7w 5
8w 4
50w 4
9w 3
6w 3
(cid:80)
1w 2
— —
=95
Table 2: RLE codewords, sorted by frequency in the page excerpt from Figure 5.1.
4 i)* Construct a Huffman code from the information in Table 2. Start with the printed leaves of the tree in the solution field.
2/95 3/95 3/95 4/95 4/95 5/95
1w 6w 9w 50w 8w 7w
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
17 Name:
j) Provide the codewords of the code you constructed. Enter these in Table 2.
2
k) Determine the total length of the compressed page excerpt in bits. 
1
l) By what percentage is the compressed page excerpt shorter compared to the simple encoding? 1
m)* Explain what additional information (besides the compressed data) is needed on the receiver side for decoding. 1
n) Provide two ways in which the problem from sub-task m) can be solved in practice. 1
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 18
Task 6 Short Tasks (10 points)
10
The following short tasks are independent of each other. Bullet-point answers are sufficient!
1 a)* Justify whether a CRC checksum generated from the generator polynomial 
g(x) = 
can detect burst errors of length 4.
x5+x2+1
1 b)* Provide the integer 240 as a long hexadecimal value in Little Endian and Network Byte 
2B
Order.
1 c)* Name two different reasons why a service is implemented as a distributed system instead of a single, central server.
3 d)* Describe in 3-4 bullet points how the traceroute program works.
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
19 Name:
e)* What are two fundamental differences between IPv4 and IPv6? 
1
f)* Explain why a program running in parallel on 10 computers can be less than 10 times faster than running on one. 1
g)* Explain the consistency problem that arises when multiple nodes of a distributed application access shared memory. 1
h)* An attacker wants to inject data into an existing TCP connection. Name the information about the TCP state that he needs for this. 1
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 20
Additional space for solutions – please clearly mark the affiliation to the respective task and cross out invalid solutions!
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
21 Name:
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 22
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
23 Name:
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013