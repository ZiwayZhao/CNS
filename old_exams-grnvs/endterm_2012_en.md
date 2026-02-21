Name First Name  
..................  
Grade  
Study Program (Major) Field of Study (Minor)  
I II  
Student ID  
Signature of the Candidate  
1  
2  
TECHNICAL UNIVERSITY OF MUNICH  
3  
Faculty of Computer Science  
Midterm Exam  
4  
× Final Exam  
5  
Semester Exam  
Diploma Preliminary Exam  
6  
Bachelor Exam  
............................  
7  
Consent for Grade Disclosure  
8  
via Email / Internet  
9  
10  
Exam Subject: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle Date: 10.08.2012  
Hearing Room: .................... Row: .................... Seat: .....................  
To be filled out by the supervisor only:  
Exited the hearing room from ...... : ...... to ...... : ......  
Submitted early at ....... : ......  
Special Remarks:  
Final Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
Friday, 10.08.2012  
11:00 – 12:30  
• This exam consists of 23 pages and a total of 6 tasks. Please check now that you have received a complete set of materials.  
• Please write your name and student ID in the header of each page.  
• The total number of points is 85.  
• Allowed materials include a double-sided handwritten A4 sheet and a non-programmable calculator. Please remove all other documents from your desk and turn off your mobile phones.  
• Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
• Only those results will be counted where a solution path is recognizable. Text problems must generally be justified unless explicitly stated otherwise in the respective sub-task.  
1 Name:  
Task 1 Frame Error Probability (Points)  
9  
We consider a wireless connection between two computers A and B (see Figure 1.1). We simplify by assuming that bit errors occur independently with probability  
0 < p < 1.  
A frame of length xbit is transmitted correctly if it has no bit errors. The probability of a successfully transmitted frame therefore depends on the frame length and the bit error probability.  
f(x,p)  
A B  
Figure 1.1: Network Topology  
a)* Determine the probability that a frame is transmitted successfully.  
f(x,p)  
1  
If a frame is transmitted correctly, this corresponds to successfully transmitted bits. If at least one bit error occurs, the entire frame must be repeated, which corresponds to successfully transmitted bits.  
0  
b) Determine the average number of successfully transmitted bits per frame.  
g(x,p)  
1  
c) Determine the optimal frame length ∗ that maximizes.  
∀ x g(x,p)  
2  
Note: d (cx) = ln(c)cx, c > 0.  
dx  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 2  
The bit error probability is now given by −.  
p = 10^-4  
d) Determine ∗ explicitly for the given bit error rate.  
1 x  
e) What is the probability under these circumstances that a frame of optimal length  
1 pR  
is transmitted incorrectly?  
Next, we assume a frame error probability of  
p = 60%  
R  
which is too high for higher layer protocols to function correctly. For this reason, the frame error probability should be reduced using link-layer acknowledgments. We assume the so-called "Stop and Wait" principle, i.e., Computer A sends exactly one frame to B and waits for an acknowledgment if B has received the frame correctly. If the acknowledgment is not received, A repeats the frame. The procedure terminates after a total number of retry attempts.  
N  
For simplicity, we assume that acknowledgments cannot be lost.  
f)* Determine the probability that the procedure fails.  
1  
g) Determine the minimum number of retries per frame such that the probability of a failure falls below  
2 Nmin  
0.1%.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
3 Name:  
Task 2 NAT and Static Routing (Points)  
17  
Given the network topology from Figure 2.1. PC1 and PC2 are connected via a standard Ethernet switch with router R1, which provides access to the Internet.  
PC1  
IP Address  
Subnet Mask  
eth0  
Gateway  
R1 R2 R3 SW2  
10.0.35.134/23 87.186.224.45/30  
P0  
SW1 P1 eth0 wan0 wan0 eth0 P0  
P2 87.186.224.46/30 P1  
IP Address  
eth0 Subnet Mask eth0  
Gateway  
PC2 SRV  
(www.google.de)  
Figure 2.1: Network Topology  
a)* Determine the network address and broadcast address of the network in which PC1, PC2, and R1 are located.  
1  
b)* How many IP addresses are available in this network for addressing devices?  
1  
c) Assign PC1 and PC2 a sensible IP address, subnet mask, and gateway address so that they can establish a connection to the Internet. Enter the values directly in Figure 2.1.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 4  
d)* How many /23 subnets are there in the network 10.0.0.0/8?  
1  
e)* Which header fields does switch SW1 change, which connects PC1 and PC2 to R1?  
1  
f)* Justify why R1 must support NAT for PC1 and PC2 to communicate with hosts on the Internet.  
1  
g)* Which transport protocol and which destination port number are typically used for (unencrypted) HTTP connections?  
Next, we abbreviate IP and MAC addresses according to the scheme  
<DeviceName>.<Interface>  
e.g. R1.wan0. For the following two sub-tasks, also note that there are a total of three additional routers between R2 and R3. PC1 is now accessing the website  
http://www.google.de.  
h) Complete the header fields for the request from PC1 to www.google.de in the three empty boxes in Figure 2.2. If a field cannot be determined unambiguously, make a sensible choice.  
Note: If you could not solve sub-task g), assume destination port 80.  
i) Complete the header fields for the response from www.google.de to PC1 in the three empty boxes in Figure 2.3. If a field cannot be determined unambiguously, make a sensible choice.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
5 Name:  
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
n0 2.2:  
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
1 CC rr  
R AAPP oo  
MMII PP  
ctctLct  
h0 rsrsTrs  
t SDSDTSD  
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
Student ID: 6  
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
n0 2.3:  
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
1 CC rr  
R AAPP oo  
MMII PP  
ctctLct  
h0 rsrsTrs  
t SDSDTSD  
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
7 Name:  
In contrast to the lecture, R1 stores not only the triple consisting of local IP and local and global source port, but also the used protocol as well as destination port and destination IP. Table 1 shows exemplarily how such a NAT table might have looked before the two sub-tasks h) and i).  
Protocol Local IP Local Port Global IP Global Port Destination IP Destination Port  
TCP PC1.eth0 50034 R1.wan0 50034 83.133.105.60 22  
TCP PC1.eth0 49985 R1.wan0 49985 213.165.65.50 443  
Table 1: NAT table of R1 before sub-task h)  
j) According to Table 1, specify the entries that were created by the connection establishment from PC1 to the web server in sub-tasks h) and i).  
Protocol Local IP Local Port Global IP Global Port Destination IP Destination Port  
k) Now assume that PC2 also wants to establish a connection to www.google.de. By chance, PC2 chooses the same source port as PC1. Provide a valid entry in the NAT table that could be newly created by the connection establishment from PC2 to the web server.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 8  
Task 3 Packet Pair Probing (Points)  
15  
Given the simplified network topology from Figure 3.1. A and D are connected to their routers via Gigabit Ethernet. However, the connection between routers B and C is significantly slower. A and D should determine this transmission rate while generating as little load as possible on the already slow connection.  
r  
BC  
r r r  
AB BC CD  
A B C D  
Figure 3.1: Simplified Network Topology  
In this task, we will first derive a general method by which A and D can determine the relevant transmission rate. Subsequently, we will evaluate the method for specific numerical values and discuss potential problems that may arise in practice.  
a)* Provide the serialization time between two nodes and as a function of the packet size  
1 ts(i,j) i j  
and the transmission rate.  
p r  
ij  
b)* Provide the propagation delay between two nodes and as a function of the  
1 tp(i,j) i j  
distance.  
d  
ij  
For a successful and as accurate as possible determination of the rate, it is important that packets sent from A to D are as large as possible but not fragmented.  
c)* Briefly explain how A can determine the maximum MTU on the path to D.  
2  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
9 Name:  
A now sends two packets of length p directly one after the other to D. You can assume that no other traffic influences the transmission. The length should be chosen so that no fragmentation is necessary. You may neglect any processing times at the node.  
d)* Draw a time-distance diagram that qualitatively represents the transmission of the two packets. Pay particular attention to how it was mentioned at the beginning.  
r < r = r  
BC AB CD  
A B C D  
t  
Due to the low transmission rate between B and C, a sending pause ∆t occurs at node C between the two forwarded packets. This can be measured by D and used to determine the transmission rate between B and C.  
e) Mark in your solution from sub-task d).  
∆t  
1  
f) What does ∆t depend on?  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 10  
g) Provide an expression for ∆t.  
2  
h) Provide an expression for the sought data rate.  
1 rBC  
Repeated measurements at D yield an average value with a packet size of  
∆t = 1.20 ms.  
p = 1500 Byte  
i) Determine the numerical value of rBC in Mbit/s.  
1  
j) Provide two reasons why the method may be inaccurate in practice.  
2  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
11 Name:  
Task 4 Dynamic Routing (Points)  
15  
Given the simplified network shown in Figure 4.1. All routers use RIP as the routing protocol. The tables below routers A – E in Figure 4.1 represent the routing table of each router before RIP is started.  
Dst GW Cost TA  
A - 0 -  
C - 0 -  
D  
A B C E  
Dst GW Cost TA Dst GW Cost TA Dst GW Cost TA Dst GW Cost TA  
B - 0 - A - 0 - B - 0 - C - 0 -  
D - 0 - C - 0 - D - 0 -  
E - 0 -  
Figure 4.1: Network Topology  
a)* What metric does RIP use?  
1  
b)* To which class of routing protocols does RIP belong?  
1  
c) In what way are networks whose routers use only RIP as a routing protocol limited in size?  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 12  
d) Briefly explain how RIP works. (2 – 3 bullet points are sufficient!)  
3  
e) Justify whether RIP always chooses the fastest (in terms of transmission rate) route to a destination.  
2  
The routers now start RIP. After some time delay, the routers send updates to each other. The chronological order of the updates is given by the following three sub-tasks. The column "TA" (Sub-task) in the routing tables in Figure 4.1 indicates the sub-task (i.e., the time step) in which the respective entry is added.  
Enter all changes in the routing tables in Figure 4.1 (including the "TA" column as described above), ...  
f) ...after B has sent its first update.  
1  
g) ...after C has sent its first update.  
2  
h) ...after D has sent its first update.  
1  
i)* Briefly describe the problem that can occur with RIP when the link between C and E fails. (2 – 3 bullet points are sufficient!)  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
13 Name:  
Task 5 TCP Flow and Congestion Control (Points)  
19  
The most widely used transport protocol on the Internet is TCP. It implements mechanisms for flow and congestion control. Specifically, we assume TCP "Reno" in this task.  
a)* What is the purpose of flow control?  
1  
b)* What is the purpose of congestion control?  
1  
c) What role does the receive window play in flow control?  
1  
We assume that the receive windows are always larger than the send windows.  
d)* Sketch by hand in the solution area a typical course of the send window size for TCP.  
2  
Assume that the TCP connection has just been established at time t = 0.  
Send Window / Byte  
0 t/RTT  
0  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 14  
e) Mark and name the two phases of congestion control in the solution to sub-task d).  
1  
f) What triggers the transition between the two congestion control phases?  
1  
g)* Under what circumstances does the congestion control mechanism start over?  
1  
To analyze the TCP data rate, we consider the course of a continuous data transmission, where the first phase of congestion control has already been completed. Since the receive window is assumed to always be sufficiently large, the size of the send window always corresponds to the size of the congestion control window. No losses occur as long as the send window is smaller than a maximum value, i.e., . Once the send window reaches the value, exactly one of the  
x w < x x  
sent TCP segments is lost.  
h)* How does the receiver detect the loss of a segment?  
1  
i)* How does a single lost segment affect the send or congestion control window?  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
15 Name:  
As specific numerical values, we assume that the maximum TCP segment size (MSS) is 1460 Bytes and the RTT is 200 ms. The serialization time of segments is negligible compared to the propagation delay. Segment loss occurs at a send window size of  
w x = 16 MSS.  
s  
j)* Create a diagram in which the current size of the send window measured in multiples of the MSS is plotted over the time axis measured in multiples of the RTT. In your diagram, it should hold true at time t = 0. Draw the diagram in the time interval  
t = 0s w = x/2  
{ } 0 s  
t = 0,...,14  
w /MSS  
s  
16  
15  
14  
13  
12  
11  
10  
9  
8  
7  
6  
5  
4  
3  
2  
1  
0  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 t/RTT  
k) Determine the period duration between the reduction of the send window and the next segment loss generally as a function of x.  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 16  
l) Determine the number of segments transmitted per period duration (including the lost segment at the end) generally as a function of x.  
3  
m) Determine the loss rate generally and as a numerical value.  
1 θ  
n) Determine the average achievable transmission rate in the considered TCP transmission phase in kbit/s using the results from sub-tasks k) – m).  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
17 Name:  
Task 6 Short Tasks (Points)  
10  
The following short tasks are independent of each other. Bullet-point answers are sufficient!  
a)* The graphic below shows the send signal and the receive signal after transmission over a non-ideal channel. What two channel influences are visible?  
1.5 1.5  
1 (t) 1  
x  
y(t) 0.5 signal 0.5  
esignal 0 ngssig 0  
d a  
en−0.5 pf−0.5  
S m  
E  
−1 −1  
−1.5 0 1 2 3 4 5 6 7 8 −1.5 0 1 2 3 4 5 6 7 8  
Time t/Ts Time t/Ts  
b)* In the lecture, a simple block code was presented, which maps:  
k = 1 bit n = 3 bits  
0 000, 1 111.  
To further improve error correction, the following modification is proposed:  
0 0000, 1 1111.  
How do you evaluate this change in terms of error correction and efficiency?  
c)* What metric is optimized to generate a Shortest Path Tree?  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 18  
d)* What metric is optimized to generate a Minimum Spanning Tree?  
1  
e)* Given . To which protocol does this address belong?  
fe80::222:b0ff:febc:1fe2/64  
1  
f)* Given an alphabet with a total of different characters, whose occurrence probability is uniformly distributed. Justify whether the average codeword length when using Huffman code is greater than, equal to, or less than 5 bits.  
2  
32  
g)* Why can the original of a JPEG-compressed image not be reconstructed exactly?  
1  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
19 Name:  
h)* Justify (either argumentatively or by calculation) whether the time signal s(t) shown below has a DC component.  
2  
s(t)  
A  
− − −  
t  
3T 2T T T 2T 3T  
−  
A  
Note: The signal can be represented as a Fourier series, i.e., it holds  
∞  
a  
0  
s(t) = + (a cos(kωt)+b sin(kωt))  
k k  
2  
k=1  
with the coefficients  
2 T · and 2 T ·  
a = s(t) cos(kωt) dt b = s(t) sin(kωt) dt.  
k k  
T T  
0 0  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 20  
Additional space for solutions – please clearly mark the affiliation with the respective task and strike out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
21 Name:  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
Student ID: 22  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012  
23 Name:  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2012