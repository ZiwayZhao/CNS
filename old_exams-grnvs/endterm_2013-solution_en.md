Name First Name
.................
Grade
Degree Program (Major) Field of Study (Minor)
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
Diploma Preliminary Examination 6
o
Bachelor Examination
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
Examination Subject: Fundamentals of Computer Networks and Distributed Systems
ö
L
Examiner: Prof. Dr.-Ing. Georg Carle Date: 09.08.2013 (cid:80)
Lecture Hall: .................... Row: .................... Seat: .....................
To be filled out by the supervisor only:
Leave the lecture hall from ...... : ...... to ...... : ......
Submitted early at ....... : ......
Special Remarks:
Final Exam
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
• Do not spend too long on a (sub-)task. If you cannot solve the task immediately, please move on to the next task.
• Only those results will be counted where a solution path is recognizable. Text tasks must be justified unless explicitly stated otherwise in the respective sub-task.
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
Figure 1.1: Time and value continuous signal on the receiver side
g (t)
s
Q
1
00 01 11 10
I
0.5
− −
0.75 0.25 0.25 0.75
[ ]
t s
− −
0.50 0.25 0 0.25 0.50
(a) Signal space assignment (b) Return-to-Zero transmission pulse
Figure 1.2: Transmission pulse and signal space assignment
It is known that Figure 1.1 shows an RZ-coded (Return-to-Zero) signal. The modulation alphabet used is represented in Figure 1.2a.
a)* Name two channel influences that are visible in the signal progression of Figure 1.1. 1
(cid:88) (cid:88)
Low-pass, noise (no attenuation, as it is unknown within which interval the transmitted signal moves)
b)* What modulation method is used according to Figure 1.2a? 1
(cid:88)
4-ASK
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 2
c)* Draw the Return-to-Zero transmission pulse with normalized amplitude in the time domain in Figure 1.2b.
1 t [ 0.5,0.5]
d) Assume the basic pulse from Figure 1.2b is to be sampled with the sampling frequency 
1 f = 2Hz
a
. Mark the sampling time points directly in Figure 1.2b.
∈
2 e) Sample the signal from Figure 1.1 with the sampling frequency in the range 
f = 2Hz t [0,4]
a
. Enter the time-discrete signal directly into Figure 1.1.
Note: Pay attention to correct sampling time points according to your solution from sub-task c). The use of a ruler is allowed.
The quantization interval, within which the quantization error is to be minimized, is 
−
. The step size is . Arithmetic rounding is used for quantization. 
I = [ 1,1] ∆ = 0.5
1 f)* Calculate the number of quantization levels.
− (cid:88)
b a 2
M = = = 4
∆ 0.5
1 g)* Provide the quantization levels as numerical values. Enter these directly into Figure 1.2a below the respective codewords.
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
(cid:88)(cid:88) (cid:88)
( )
11 10 00 11
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
3 Name:
j)* Justify whether Return-to-Zero is a DC-free line code.
1
No, as it is not guaranteed that positive and negative signal components balance out in the time average, regardless of the transmitted bit sequence. 
(cid:88)
k)* Justify whether automatic clock recovery is possible with Return-to-Zero. 1
(cid:88)
Yes, as at least one signal change (return to zero) occurs per symbol.
The received bit sequence is protected by a very simple channel code. To this end, the sender appends a so-called parity bit to each group of 3 bits, which is 0 if the preceding 3 bits contain an even number of ones. Otherwise, the parity bit is 1.
3 bits
l)* Justify which bit errors can be detected by the parity bit. 1
An odd number of bit errors is detected (the parity bit flips), while an even number is not, as the parity bit becomes valid again. 
(cid:88)
m)* Justify which bit errors can be corrected by the parity bit. 1
(cid:88)
None, as the parity bit gives no indication of the location of the bit error.
n) Mark the parity bits in your solution from sub-task i). 1
o) Check the received bit sequence for transmission errors. 1
At least one bit error has occurred, as in the first group the 4th bit should be 0 instead of 1. 
(cid:88)
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 4
Task 2 Time Synchronization (11 points)
11
A hypothetical pico-satellite is in a low Earth orbit. We consider the moment when it is at a distance of 
to the ground station on the Earth's surface. It is 
1500km A
located directly between the ground station and another identical satellite in a higher orbit, which is at a distance of 
from the ground station. 
3000km
Earth
A B C
1500km 1500km
The modems of the satellites can send at and receive at . The ground station sends and receives at the maximum data rates supported by the satellites. Assume 
≈
the speed of light on all paths · 
c 3 108m/s
The satellite wants to synchronize its onboard clock with the time of the ground station. To do this, the following simple protocol is executed: 
B
sends a long request to the ground station. It responds 
B 64B
with a long frame containing the current time of the ground station. Processing times at the endpoints are to be neglected in this task.
1 a)* Determine the serialization times and between the ground station and 
t (A,B) t (B,A) A
the satellite . 
B
L (cid:88) 64B 512bit
t (A,B) = = = = 9.2ms
s
r 56.0kbit/s 56000bit/s
L 64B 512bit (cid:88)
t (B,A) = = = = 36ms
s
r 14.4kbit/s 14400bit/s
1 b)* Determine the propagation delay between the ground station and the 
t (A,B) A
satellite . 
B
d (cid:88) 1500km (cid:88)
t (A,B) = = = 5.0ms
p
c 300000km/s
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
5 Name:
c) Draw the request from the satellite and the response from the ground station in the following 
B A
time-distance diagram. The request is sent at the time.
t = 0ms 2
0
(Scale: horizontal (cid:44) , vertical (cid:44) )
1cm 250km 1cm 10ms
A B C
t = 0ms
0
t (B,A)
s
RTT
t (A,B)
s
t (A,B)
p
t
d) Mark the serialization times and the propagation delay 
t (A,B) t (B,A)
s s
and the round-trip time (RTT) in your solution from sub-task c).
t (A,B)
p
Due to the serialization and propagation delays, the time sent by the ground station at the time of receipt by the satellite is no longer exact. The satellite estimates the actual 
B
time by adding half the RTT to the received time. This results in an error 
∆t
which is to be determined below.
e) Calculate the RTT from the satellite's perspective . 1
B
(cid:88)
·
t = t +2 t +t
RTT s,B p s,A
(cid:88)
·
= 36ms+2 5.0ms+9.2ms = 55ms
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 6
f)* Justify why the correct time is not calculated here when half the RTT is added to the received time.
1
The RTT is asymmetrically distributed over the up and down link, as the serialization times differ in both directions. 
(cid:88)
1 g) In the described method, the satellite adds the correction to the received time. 
t
c,S
Calculate . 
t
c,S
(cid:88) (cid:88)
tc,S = tRTT/2 = 29ms
1 h) Calculate the correct correction value that the satellite should use to determine the current 
t
c
time. 
(cid:88) (cid:88)
t = t +t = 5.0ms+9.2ms = 14ms
c p s,A
1 i) Calculate the absolute error that the satellite makes with the described method.
∆t
− (cid:88) − (cid:88)
∆t = t t = 29ms 14ms = 15ms
c,S c
⇒
( The clock on the satellite is ahead by .)
15ms
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
7 Name:
Task 3 NAT and Static Routing (15 points)
15
Given is the network topology from Figure 3.1. PC1 and PC2 are connected via a regular Ethernet switch SW1 to router R1, which provides access to the Internet.
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
Figure 3.1: Network topology
a)* Justify whether the address 10.0.1.0 is usable for the given prefix. If not, assign 
1
a meaningful address in the same network to R1.
10.0.1.0 is a valid host address in the network 10.0.0.0/20, as it is neither the first nor the last address in the subnet, i.e., it is neither a network nor a broadcast address (immediately evident from the small prefix and the 1 in the 3rd octet). 
(cid:88)
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
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 8
d) Assign each of PC1 and PC2 a meaningful IP address, subnet mask, and gateway address so that they can establish a connection to the Internet. Enter the values directly in 
1 Figure 3.1.
e)* How many /20 subnets are there in the network 10.0.0.0/8? 
1
(cid:88)
− −
220 8 = 224 12 = 4096
f)* Justify why R1 must support NAT so that PC1 and PC2 can communicate with hosts on the Internet. 
PC1 and PC2 are in a private network, and their IP addresses are therefore not globally unique. 
(cid:88)
g)* What information must R1 at least maintain in its NAT table? 
1
Local IPs of the PCs, local port numbers, and global source port numbers. (global IP not necessary, as R1 only has one global IP address; destination port numbers are not required for the basic tasks). 
(cid:88)
In the following, we abbreviate IP and MAC addresses according to the scheme 
<DeviceName>.<Interface>
, e.g. . Note that for the two following sub-tasks, there are three other routers between R2 and R3. PC1 now accesses the website 
http://www.google.de.
h) Complete the header fields for the request from PC1 to www.google.de in the three empty boxes 
4
in Figure 3.2. If a field is not clearly defined, make a reasonable choice.
i) Complete the header fields for the response from www.google.de to PC1 in the three empty boxes 
4
in Figure 3.3. If a field is not clearly defined, make a reasonable choice.
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
n0 3.2:
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
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
11 Name:
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
n0 3.3:
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
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
13 Name:
Task 4 Wireshark (11 points)
11
Given is the network from Figure 4.1. A packet is sent from PC1 towards PC2. The traffic is captured by PC1 using Wireshark. The decoded trace is shown in Table 1. Unfortunately, the timestamps have gotten a bit mixed up – which is why we have not printed them. The frames are therefore not presented in the order they were seen by PC1. This trace is to be analyzed and put in the correct order in the following sub-tasks.
90:e2:ba:2a:d2:a3 90:e2:ba:2a:8d:0f - - - - - - - - - -
MAC MAC MAC MAC
fc00::10 fc00::1 - - - - - fc00::2:10
IP IP IP IP
PC1 RA RB PC2
- - - - - - - - - -
MAC MAC
- - - - - fc00::1:2
IP IP
Figure 4.1: Network topology
a)* First, explain the difference between MAC and IP addresses in terms of their usage. 1
(cid:88)
MAC addresses are used for local addressing (within a broadcast domain). 
(cid:88)
IP addresses are used for end-to-end addressing.
As mentioned at the beginning, the frames in Table 1 are not in the correct order. The identifiers A – H in the first column serve to refer to individual frames in the following sub-tasks.
b)* Briefly explain the purpose of frames B and G. 1
Note: The MAC address in frame G can be considered a broadcast address ( 
33:33:ff:00:00:01
). 
(cid:88)
ff:ff:ff:ff:ff:ff
(cid:88)
Address resolution, i.e., finding the MAC address for a given IPv6 address. (equivalent to ARP in IPv4)
Frame G makes the request. Frame B contains the corresponding response.
c)* Explain how frame H can occur. 1
PC1 sent a packet (frame D) towards PC2, which was larger than the MTU allowed on one of the link segments (between RB and PC2). Since fragmentation in IPv6 is only allowed at the sender, RB sent an error message back to PC1 with the corresponding MTU. 
(cid:88)
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 12
Id. in out Nr. Output
Ethernet II, 90:e2:ba:2a:d2:a3 -> 90:e2:ba:2a:8d:0f, Length: 1294
A X 5
fc00::10 -> fc00::2:10, IPv6, Length: 1294
IPv6 fragment (nxt=ICMPv6 (58) off=0 id=0x7c0d6306)
Ethernet II, 90:e2:ba:2a:8d:0f -> 90:e2:ba:2a:d2:a3, Type: IPv6 (0x86dd)
B X 2
fc00::1 -> fc00::10, ICMPv6, Length: 86
Neighbor Advertisement: fc00::1 (rtr, sol, ovr) is at 90:e2:ba:2a:8d:0f
Ethernet II, 90:e2:ba:2a:8d:0f -> 90:e2:ba:2a:d2:a3, Length: 238
C X 8 fc00::2:10 -> fc00::10, ICMPv6, Length: 238
IPv6 fragment (nxt=ICMPv6 (58) off=154 id=0x7aef85b4)
Echo (ping) reply id=0x1dd7, seq=2
Ethernet II, 90:e2:ba:2a:d2:a3 -> 90:e2:ba:2a:8d:0f, Type: IPv6 (0x86dd)
D X 3
fc00::10 -> fc00::2:10, ICMPv6, Length: 1462
Echo (ping) request id=0x1dd7, seq=1
Ethernet II, 90:e2:ba:2a:d2:a3 -> 90:e2:ba:2a:8d:0f, Length: 238
E X 6 fc00::10 -> fc00::2:10, ICMPv6, Length: 238
IPv6 fragment (nxt=ICMPv6 (58) off=154 id=0x7c0d6306)
Echo (ping) request id=0x1dd7, seq=2
Ethernet II, 90:e2:ba:2a:8d:0f -> 90:e2:ba:2a:d2:a3, Length: 1294
F X 7
fc00::2:10 -> fc00::10, IPv6, Length: 1294
IPv6 fragment (nxt=ICMPv6 (58) off=0 id=0x7aef85b4)
Ethernet II, 90:e2:ba:2a:d2:a3 -> 33:33:ff:00:00:01, Type: IPv6 (0x86dd)
G X 1
fc00::10 -> ff02::1:ff00:1, ICMPv6, Length: 86
Neighbor Solicitation: whois fc00::1 from 90:e2:ba:2a:d2:a3
Ethernet II, 90:e2:ba:2a:8d:0f -> 90:e2:ba:2a:d2:a3, Type: IPv6 (0x86dd)
H X 4
fc00::1:2 -> fc00::10, ICMPv6, Length: 1294
Packet Too Big, MTU: 1280
Table 1: Capture of network traffic on PC1 in unsorted order.
d) Explain the relationship between frames A, D, and E. 
2 (cid:88)
Frame D was the packet that triggered the ICMPv6 error message in sub-task c). Frames A (first fragment) and E (second fragment) represent the same ICMP Echo Request, which is now fragmented by PC1 according to the determined MTU. 
(cid:88)
1 e)* Determine the MTU on the link between RB and PC2. 
(cid:88)
According to frame H, the MTU is 
1280B.
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
13 Name:
f)* Determine for all frames from Table 1 whether they are incoming or outgoing frames from the perspective of PC1. Check the corresponding field in the "in" or "out" columns in Table 1.
g) Now arrange the frames from Table 1 in a meaningful order. Note the number of the packet starting from 1 in the "Nr." column.
h) Now enter all MAC and IP addresses of the devices in Figure 4.1 as far as this is evident from Table 1. If an entry from Table 1 is not evident, clearly cross out the corresponding field.
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
Figure 5.1: Excerpt of a black/white fax page. The numbers on the left indicate the line number.
Solution field for sub-task f)
(cid:88)(cid:88)
4w 1s 1w 1s 4w 2s 8w 1s 7w 2s 9w 2s 8w
A simple but inefficient way is to encode black pixels as a logical 0 and white pixels as a logical 1. We refer to this type of encoding as simple code.
1 a)* Determine the length of the data to be transmitted in bits when the page excerpt is encoded with this simple code.
(cid:88)
· ·
L = 50 9 1bit = 450bit
2 b)* Determine the information content of the two codewords used.
Note: The page excerpt consists of 55 black pixels.
(cid:18) (cid:19)
(cid:88)
− (cid:18) 55 ≈ (cid:19)
I (0) = log 3.03bit
E 2 450
− (cid:88)
− 450 55 ≈
I (1) = log 0.19bit
E 2 450
1 c) Determine the entropy of the page excerpt.
−
55 450 55 ≈ (cid:88)
H = I (0)+ I (1) 0.54bit
E E
450 450
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
15 Name:
d) What can be concluded from the result of sub-task (c)? 
1
(cid:88)
The message contains redundancy and can therefore be compressed.
For lossless compression, ITU T.30 uses a combination of run-length encoding (RLE) and subsequent Huffman coding. To do this, the number of consecutive pixels of the same color along with the respective color value (black or white) is first encoded line by line, for example, for three consecutive white or four consecutive black pixels. 
3w 4s
e)* Explain what is meant by lossless compression. 1
(cid:88)
Removal of redundancy without giving up the possibility of reconstructing the original data exactly. 
(cid:88)
f)* Provide the third line of the page excerpt in Figure 5.1 encoded in run-length in the solution field below Figure 5.1.
g)* The Huffman code is a so-called prefix-free code. Explain what this means. 1
(cid:88)
No codeword is a true prefix of another codeword.
h) How does the use of prefix-free codes facilitate decompression? 1
Data can be reconstructed immediately when a matching codeword is found (no "look ahead" is necessary). 
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 16
Across the entire page excerpt, the RLE codewords with their corresponding absolute frequencies are listed in Table 2. The total number of RLE codewords for the complete excerpt is 95.
RLE Word Frequency Huffman Codeword
1s 35 0
2w 13 110
2s 10 1001
3w 9 1010
4w 7 1110
7w 5 10000
8w 4 10001
50w 4 10110
9w 3 10111
6w 3 11110
(cid:80)
1w 2 11111
— —
=95
Table 2: RLE codewords, sorted by frequency in the page excerpt from Figure 5.1.
4 i)* Construct a Huffman code from the information in Table 2. Start with the printed leaves of the tree in the solution field.
Note: There are multiple possible solutions.
(cid:88)(cid:88)(cid:88)(cid:88)
1
1 0
60/95 35/95
1 01s
25/95 35/95
1 0 1 0
12/95 13/95 16/95 19/95
1 0 2w 1 0 1 0
5/95 7/95 7/95 9/95 10/95 9/95
4w 3w 2s
1 0 1 0 1 0
2/95 3/95 3/95 4/95 4/95 5/95
1w 6w 9w 50w 8w 7w
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
17 Name:
j) Provide the codewords of the code you constructed. Enter them in Table 2.
2
k) Determine the total length of the compressed page excerpt in bits.
1
(cid:88)
· · · ·
L = 35 1+13 3+(10+9+7) 4+(5+4+4+3+3+2) 5 = 283bit
H
l) By what percentage is the compressed page excerpt shorter compared to the simple encoding? 1
(cid:88)
− 283
η = 1 = 37.11%
450
m)* Explain what information (aside from the compressed data) is still needed on the receiver side for decoding. 1
(cid:88)
The receiver must know the code alphabet.
n) Provide two ways in which the problem from sub-task m) can be solved in practice. 1
(cid:88) (cid:88)
Send the alphabet along or agree in advance on a common alphabet.
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 18
Task 6 Short Tasks (10 points)
10
The following short tasks are independent of each other. Bullet point answers are sufficient!
1 a)* Justify whether a CRC checksum generated from the generator polynomial 
g(x) = 
can detect burst errors of length 4.
x5+x2+1
(cid:88)
Yes, since the degree of 5 is (and irreducible) can detect burst errors up to length 5.
g(x)
1 b)* Provide the integer value 240 as a long hexadecimal value in Little Endian and Network Byte Order.
(cid:88)
Little Endian:
0xF0 0x00
(cid:88)
Network Byte Order (Big Endian):
0x00 0xF0
1 c)* Name two different reasons why a service is implemented as a distributed system instead of a single, central server.
(cid:88) (cid:88)
Performance, fault tolerance
(other answers: censorship resistance, availability, interoperability between different providers)
3 d)* Describe in 3-4 bullet points how the traceroute program works.
(cid:88) (cid:88)
The sender sends ICMP Echo Requests with increasing TTL starting at 1, which provoke ICMP TTL Exceeded messages from hop to hop, allowing the path between the sender and receiver to be recorded.
(cid:88)
(Possible balancing point: it stops when an ICMP Echo Reply is received from the target)
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
19 Name:
e)* What are two fundamental differences between IPv4 and IPv6? 
1
(cid:88) (cid:88)
Longer addresses, headers have fixed length 
16B
(other answers: no more fragmentation on the way between source and destination, extension headers for extensibility, features for automated configuration, address assignment, local gateway discovery, etc.)
f)* Explain why a program running in parallel on 10 computers can be less than 10 times faster than running on one. 
Scalar portions that cannot be parallelized have a significant impact on performance (Amdahl’s Law).
(cid:88)
g)* Explain the consistency problem that arises when multiple nodes of a distributed application access shared memory. 
The nodes overwrite each other's data unnoticed, so that the local information no longer matches the global one. 
(cid:88)
h)* An attacker wants to inject data into an existing TCP connection. Name the information about the TCP state that he needs for this. 
(cid:88)
The expected sequence number from the receiver (or at least one that is within the receive window, as the receiver would otherwise discard the packet), port number.
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 20
Additional space for solutions – please clearly mark the affiliation with the respective task and cross out invalid solutions!
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
21 Name:
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
Student ID: 22
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013
23 Name:
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013