Name First Name  
Grade  
Degree Program (Major) Specialization (Minor)  
I II  
Student ID  
Signature of the Candidate 1  
2  
TECHNICAL UNIVERSITY OF MUNICH  
a 3  
Faculty of Computer Science  
l  
h 4  
c  
5  
s  
r  
Midterm 6  
o  
× Endterm  
v  
Retake 7  
s  
g 8  
n  
9  
u  
10  
s  
Exam Subject: Fundamentals of Computer Networks and Distributed Systems  
ö  
L  
Examiner: Prof. Dr.-Ing. Georg Carle Date: 22.07.2014 (cid:80)  
Lecture Hall: Row: Seat:  
To be filled out by the supervisor only:  
Lecture hall left from: to:  
Submitted early at:  
Special Remarks:  
Endterm Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
Tuesday, 22.07.2014  
11:30 – 13:00  
• This exam consists of 23 pages and a total of 6 tasks. Additionally, a supplementary sheet with protocol headers will be distributed. Please check now if you have received a complete set of materials.  
• Please write your name and student ID in the header of each page.  
• Do not write in red/green ink or with a pencil.  
• The total number of points is 85.  
• Allowed aids are a double-sided handwritten A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
• Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
• Do not spend too much time on a (sub-)task. If you cannot solve the task immediately, it is better to move on to the next task.  
• Only results where a solution path is recognizable will be graded. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-task.  
1 Name:  
Task 1 Fourier Series (10 Points)  
10  
Given is the periodic triangular pulse shown in Figure 1.1. This signal is to be represented as a Fourier series (cid:88)  
∞  
a  
0  
s(t) = + (a cos(kωt)+b sin(kωt))  
k k  
2  
k=1  
The coefficients for all integer k > 0 can be determined as follows:  
(cid:90) (cid:90)  
2 T/2 2 T/2  
a = s(t)cos(kωt)dt, b = s(t)sin(kωt)dt.  
k T − k T −  
T/2 T/2  
s(t)  
(cid:88)(cid:88)  
π (f)  
− − − t  
3π 2π π π 2π 3π  
Figure 1.1: Periodic Triangular Pulse  
s(t)  
a)* Provide an analytical expression for the sending base pulse, that is, for the signal in the interval .  
t [ π;π]  
(cid:40)  
− ≤ (cid:88)  
for  
π+t π t < 0,  
s(t) = − ≤ (cid:88)  
for  
π t 0 t < π.  
b)* Determine the period duration and angular frequency of the signal.  
1  
T ω = 2π/T  
(cid:88) (cid:88)  
T = 2π , ω = 1  
c)* Determine the DC component.  
1  
a  
0  
(cid:88)  
a π ⇔  
0  
= a = π  
0  
2 2  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 2  
d)* Justify why b = 0 ∀ k ∈ N. (no calculation necessary)  
1  
The sine components are zero. This must be the case since one function is odd and the other is even.  
b (cid:88) sin(t) s(t)  
k  
is.  
  
4 e) Show that for the cosine components the following holds:  
  
  
4 for  
k = 1,3,5,...,  
a = k2π  
k otherwise  
0 .  
(cid:90)  
Note: Depending on the solution path, one of the following two hints may be helpful:  
(cid:90) ktsin(kt)+cos(cid:90)(kt) (1)  
tcos(kt) dt = +const  
k2  
b (cid:48) · · − b · (cid:48)  
f (t) g(t) dt = [f(t) g(t)]b f(t) g (t) dt (2)  
a  
a a  
(cid:90)  
Solution using partial integration:  
(cid:88)  
(cid:90)T/2  
a = s(t)cos(kωt) dt  
1 −  
T/2  
2 (cid:20)π − (cid:21) (cid:90)  
= (π t)cos(kt) dt  
π  
0 (cid:88)  
2 (cid:20) − (cid:21) π 2 π  
= (π t)sin(kt) + sin(kt) dt  
kπ kπ  
0 0  
(cid:40)2 − π  
= cos(kt)  
k2π 0 (cid:88)  
for  
4 k =(cid:88)1,3,5,...,  
= k2π  
otherwise  
0 .  
2 f)* Draw the approximated signal s(cid:48)(t) = a0 + a cos(ωt) in Figure 1.1.  
2 1  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
3 Name:  
Task 2 PHY and MAC in PCIe (16 Points)  
16  
The ISO/OSI model is not only applicable to communication processes on the Internet. Rather, it is an abstract model for any communication processes. In this task, we consider its application to PCIe (Peripheral Components Interconnect Express), which today represents the standard for fast data exchange between devices within a computer. For example, in modern computers, practically all internal expansion cards (graphics cards, network cards, sound cards, etc.) as well as many integrated devices like SATA controllers are connected via this interface. PCIe itself is a serial, switched network between these devices.  
a)* Justify the advantage of switched connections over a bus system.  
1  
By using a switch, multiple point-to-point connections between two devices can occur simultaneously. In a bus system, there would be competing access to a common medium, meaning only one device could send at any given time.  
On the physical layer, PCIe uses two data lines per direction per lane, on which signals are transmitted differentially. An example is shown in Figure 2.1.  
The received signal results from the addition of both individual signals, i.e. − .  
s(t) = s+(t)+s (t)  
s+(t)  
400mV  
t  
t  
−400mV  
−  
s (t)  
(cid:88)(cid:88)  
s(t) 1 0 0 1 1 0 1 0 1 0 0 0 1 0 (e)  
400mV  
t  
−400mV (cid:88)(cid:88)  
(c)  
Figure 2.1: Differentially coded signals s+(t) and s−(t) as well as the received signal s(t)=s+(t)+s−(t).  
1 We consider only PCIe with one lane, i.e., PCIe x1.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 4  
b)* Draw the received signal in Figure 2.1.  
s(t)  
2  
c) What sending base pulse does PCIe obviously use?  
1 (cid:88)  
NRZ (no return to zero)  
2 d) Specify the transmitted bit sequence in Figure 2.1. Enter your solution directly in Figure 2.1. Note: There are two equivalent solutions.  
1 e)* Name an advantage of differential transmission in this specific case.  
(cid:88)  
• No ground reference is necessary.  
• The difference between a logical '1' (400mV) and a logical '0' (−400mV) is double the amplitude on each line. It is easier to reliably distinguish the signal levels.  
1 f)* PCIe uses 8B10B encoding as a line code. Name two advantages that arise from this.  
(cid:88)  
• Clock recovery  
(cid:88)  
• Additional control characters  
• (DC-free)  
1 g)* The gross data rate is 2.5 Gbit per lane and transfer direction. Determine the net data rate considering the 8B10B encoding.  
8 · , Gbit (cid:88) , Gbit (cid:88)  
r = 2 5 = 2 0  
netto  
10 s s  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
5 Name:  
On the data link layer, PCIe uses 32-bit long CRC checksums. For simplification, we assume that each frame carries an 8-bit long sequence number, which is incremented by the sender for each sent frame. The send and receive buffers on both sides hold 4 frames. Go-Back-N is used for flow control.  
The receiver acknowledges (ACK) successfully transmitted frames, with acknowledgments always containing the next expected sequence number. Furthermore, the sender is explicitly informed about incorrectly transmitted frames via negative acknowledgments (NACK). Subsequent correctly transmitted frames with a higher sequence number are ignored and not acknowledged according to Go-Back-N.  
h)* What goal is pursued by the checksums?  
1  
(cid:88)  
Detection of bit errors in a frame.  
i)* Name another transmission technique known to you that also uses acknowledgments at the data link layer.  
1  
(cid:88)  
IEEE802.11  
j)* Describe the goal pursued with flow control.  
1  
(cid:88)  
Prevention of overload situations at the receiver.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 6  
k)* Given is the message exchange printed in the solution field. In the frame marked by a lightning strike (SEQ=2), an error is detected at the receiver. Complete the message exchange until SEQ=4 has been successfully transmitted. Assume that no further errors occur.  
Note: You will find another template on page 20 if needed. Please clearly cross out invalid solutions.  
Device 1 Device 2  
SEQ=0  
SEQ=1  
ACK=1  
SEQ=2  
ACK=2  
SEQ=3 (cid:18)  
(cid:88)  
NACK=2  
SEQ=4  
SEQ=2  
(cid:88)  
SEQ=3  
ACK=3  
SEQ=4  
(cid:88)  
ACK=4  
ACK=5  
1 l) How would the result of sub-task k) change if Selective Repeat were used?  
(cid:88)  
The frames with SEQ=3 and SEQ=4 would not need to be repeated.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
7 Name:  
Task 3 IP Fragmentation and Path-MTU Discovery (19 Points)  
19  
In this task, we first consider fragmentation in IPv4. The network topology is given in Figure 3.1.  
MTU:1500B MTU:1280B MTU:576B  
PC1 R1 R2 PC2  
Figure 3.1: Network Topology  
Routers R1 and R2 are configured so that hosts PC1 and PC2 can communicate with each other. The three network segments are independent of each other and use different transmission technologies, resulting in the MTUs visible in the figure.  
a)* Distinguish between the terms MTU and MSS.  
1  
(cid:88)  
The MSS specifies the size of TCP (Layer 4) segments without headers. The MTU specifies the size of IP (Layer 3) packets including the IP header.  
b)* How should the MSS be chosen in relation to the MTU (formula)?  
1  
(cid:88)  
MSS = MTU - 40B (20B for IP header, 20B for TCP header)  
c)* Can fragments be fragmented again?  
1  
(cid:88) (cid:88)  
Yes, the assignment of fragments is done via ID and offset.  
d)* At what point in the network are fragments reassembled (justification)?  
1  
(cid:88)  
IP fragments are reassembled only at the destination host. The fragments can be routed over different paths.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 8  
e)* How can you tell that it is a complete (unfragmented) IP packet?  
2 (cid:88)  
An unfragmented IP packet does not have the MF (More Fragments) flag set, and the fragment offset must be 0.  
1 f)* What problem occurs at the receiver when individual fragments are lost?  
(cid:88) (cid:88)  
The packet cannot be reassembled and is completely lost.  
Now assume that PC1 has established a TCP connection to PC2. PC1 now wants to send 1460B of payload over this TCP connection to PC2.  
PC1 sends this data considering the necessary minimal IP and TCP headers. Router R1 cannot forward the resulting packet directly and must first fragment it.  
1 g) Specify the size of all IP packets sent from R1 to R2.  
(cid:88)  
1276B = 20B IP header + 20B TCP header + 1236B and  
(cid:88)  
244B = 20B IP header + 224B.  
IP header for both packets, TCP header only once, the IP payload of fragments must be a multiple of 8 bytes due to the offset.  
2 h) Router R2 must now process these packets appropriately. Specify the size of all IP packets sent from R2 to PC2.  
(cid:88)  
572B = 20B IP header + 20B TCP header + 532B,  
(cid:88)  
572B = 20B IP header + 552B,  
(cid:88)  
172B = 20B IP header + 152B and  
(cid:88)  
244B = 20B IP header + 224B.  
IP header in all packets is necessary, TCP header only once, the IP payload of fragments must be a multiple of 8 bytes due to the offset, packets must not be reassembled at R2.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
9 Name:  
As an alternative to IP fragmentation, we now consider Path-MTU Discovery. We continue to use the network topology from Figure 3.1. PC1 still wants to send payload of 1460B to PC2 over an already established TCP connection.  
Path-MTU Discovery is used to prevent fragmentation in the network. So that the sender does not have to perform IP fragmentation, it can adjust the TCP MSS accordingly.  
Path-MTU Discovery works as follows:  
• The sender initially sends packets of the size of the local MTU.  
• These packets must not be fragmented in the network.  
• If a router receives such a packet but cannot forward it directly due to the MTU in the following network segment, it sends an ICMP Destination Unreachable, Fragmentation Needed (Type 3, Code 4) message to the sender.  
• This message contains the MTU of the following network segment, and the router discards the original packet.  
• The sender must resend the data while adhering to this MTU. In TCP, this is possible by adjusting the MSS.  
• The sender stores the MTU for subsequent packets with the same destination.  
i)* How does the sender ensure that its packets must not be fragmented in the network?  
1  
(cid:88) (cid:88)  
A set DF (Don't Fragment) flag instructs routers not to fragment the packets.  
j)* How can the sender generally assign an ICMP message (Type 3, Code 4) to multiple destinations during simultaneous Path-MTU Discovery?  
2  
The ICMP message contains, in addition to the ICMP header, the IP header and the first 8 payload bytes of the triggering packet. The recipient of the ICMP message can unpack the original IP header and assign the connection via the destination IP contained therein.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 10  
k) Calculate the size of all necessary IP packets to transmit TCP payload of 1460B from PC1 to PC2 without any fragmentation. Consider all necessary headers in their minimal size.  
2  
(cid:88)  
576B = 20B IP header + 20B TCP header + 536B,  
(cid:88)  
576B (cid:88)= 20B IP header + 20B TCP header + 536B and  
428B = 20B IP header + 20B TCP header + 388B.  
IP and TCP headers in each packet.  
4 l) Now draw a simplified time-path diagram (serialization time and propagation delay can be neglected) for Path-MTU Discovery and sending the message (1460B TCP payload). Indicate the total size of the IP packet for data packets ("IP packet, 128B"). ICMP Fragmentation Needed packets should be marked as such, and the returned MTU should be indicated ("ICMP Frag. needed, 256B"). Note: The initial congestion window for TCP is 10 MSS. Neglect TCP acknowledgments and any Layer 2 messages.  
PC1 R1 R2 PC2  
(1)IP packet,1500B(cid:88) (cid:88)  
(2) ICMP Frag. needed, 1280 B  
(3)IP packet,1280B(cid:88)  
(4)IP packet,260B  
(cid:88)  
(5) ICMP Frag. needed, 576 B (cid:88)  
(6)IP packet,576B  
(8)IP packet,428B((7G)oI-PB-aPcakk-eNt,),527068BB(SelectiveRepeat)  
(cid:88)  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
11 Name:  
Task 4 Routing in IP Networks (13 Points)  
13  
Figure 6.1 shows an IPv4-based network. It consists of several hosts (H1, H2, ...), routers R1, R2, and R3, and switch S1. Table 1 shows the routing tables of R1 and R2.  
Internet  
192.0.2.34  
(cid:88)  
203.0.113.10  
188.95.234.2  
R3 H5  
H1  
eth2: 188.95.234.7 eth1: 192.0.2.33  
203.0.113.9 eth1: 203.0.113.253  
eth0: 203.0.113.11 eth0: 203.0.113.254 eth2: 192.0.2.65  
H2 S1 R1 R2 H4  
(cid:88)  
203.0.113.12  
H3  
Figure 4.1: Network Topology  
a)* Name the network address and the broadcast address of the network 203.0.113.8/29.  
1  
(cid:88)  
Network address: 203.0.113.8  
(cid:88)  
Broadcast address: 203.0.113.15  
b)* How many addresses in the network 203.0.113.8/29 can be assigned to hosts?  
1  
(cid:88)  
/29 → − , usable: − addresses  
232 29 = 23 = 8 8 2 = 6  
c) Assign valid IP addresses to hosts H1 and H3. Enter your answer directly in Figure 6.1.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 12  
Router R1  
Destination Gateway Iface  
203.0.113.8/29 — eth0  
203.0.113.252/30 — eth1  
188.95.234.7/23 — eth2  
192.0.2.32/27 203.0.113.254 eth1  
192.0.2.64/26 203.0.113.254 eth1  
0.0.0.0/0 188.95.234.2 eth2  
Router R2  
Destination Gateway Iface  
192.0.2.32/27 — eth1  
192.0.2.64/27 — eth2  
192.0.2.96/27 192.0.2.34 eth1  
203.0.113.252/30 — eth0  
0.0.0.0/0 203.0.113.253 eth0  
Table 1: Static Routing Tables of Routers R1 and R2.  
(to be filled in sub-task (h))  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
13 Name:  
d)* How can a router determine whether the route with address and subnet mask is applicable to the address of a packet?  
a m  
R R  
Address of a Packet  
aP 1  
(cid:12) (cid:12)  
a m = a m  
P R R R  
(cid:12)  
: bitwise and  
e)* Which entry from the forwarding table does a router choose when multiple entries are suitable?  
1  
(cid:88)  
The one with the longest prefix (LPF)  
f)* Name two criteria that must be met for a router to aggregate two entries in its table.  
2  
(cid:88) (cid:88) (cid:88) (cid:88)  
next to each other + same size + mask «1 fits + same port/gateway (or: Default gateway + X on the same port)  
g) Aggregate the following networks as much as possible. Use a binary tree representation as shown.  
2  
(cid:88)  
192.0.2.16/28  
(cid:88)  
192.0.2.24/29 192.0.2.64/26  
192.0.2.16/29 192.0.2.24/30 192.0.2.28/30 192.0.2.32/27 192.0.2.64/27 192.0.2.96/27  
h) Complete the routing table (Table 1 on p. 12) so that  
4  
• every host can reach every other host in the given network and on the Internet.  
• all entries are aggregated as much as possible.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 14  
Task 5 Key Exchange and Applications (14 Points)  
14  
The Diffie-Hellman key exchange method is considered below. Given are the prime number and the primitive root. Alice and Bob want to apply this method.  
p = 17 g = 3  
Assume Alice chooses and Bob chooses as a random number.  
a = 9 b = 5  
3 a)* Sketch the Diffie-Hellman key exchange by drawing the necessary messages in the diagram below. Label the messages with both the general formulas and the specific values.  
Alice Bob  
(cid:88)(cid:88)  
p = 17,g = 3  
a = 9 b = 5  
(cid:88)(cid:88)  
mod  
A = ga p = 14  
(cid:88)(cid:88)  
mod = 5  
B = gb p  
1 b) Determine the shared secret ("key") that Bob and Alice can now calculate.  
(cid:88) (cid:88)  
mod  
K = Ab p = 145 mod 17 = 12  
mod p  
K = Ba = 59 mod 17 = 12  
2 c)* Justify whether a suitable choice for would also be (calculation and justification).  
g = 16 p = 17  
161 mod 17 = 16  
162 mod 17 = 1  
163 mod 17 = 16  
(cid:88)  
→  
16 is not a primitive congruence root and therefore not a suitable choice.  
161 m(cid:88)od 17 = 163 mod 17  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
15 Name:  
d)* Justify whether the Diffie-Hellman key exchange is secure against man-in-the-middle attacks.  
1  
(cid:88)  
No, the connection setup can be intercepted and manipulated, or the communication parties cannot authenticate each other.  
e) How would the public and private keys for Alice and Bob look when using El Gamal? Use your specific values from the previous tasks.  
Note: These can be directly derived from the Diffie-Hellman method.  
(cid:88)  
and  
Bob = b = 5 Bob = (p,g,B) = (17,3,5)  
priv pub (cid:88)  
and  
Alice = a = 9 Alice = (p,g,A) = (17,3,14)  
priv pub  
An independent third party now wants to send Alice an encrypted message and uses Alice's public key, which they have already determined in one of the previous sub-tasks.  
·  
Note: with , where is freely selectable by the third party, with  
c = k m mod p k = Ax mod p x  
∈ { − }. − · with − − − , if is a prime number.  
x 1,p 1 m = k 1 c mod p k 1 = Xp a 1 mod p p  
f) Alice receives the encrypted message . Determine the plaintext.  
2  
(X,c) = (9,8)  
− ·  
m = k 1 c mod p  
− − ·  
= ((Xp a 1 mod p) c) m(cid:88)od p  
·  
((97 mo(cid:88)d 17) 8) mod 17  
m = 16  
g)* Justify whether the hash function , where the message represents and ∈ N 1  
h = n mod 5 n n  
holds sufficient cryptographic strength.  
(cid:88)  
No, the given function is not even a weak hash function, so it is very easy to determine a (cid:48) such that a collision occurs, i.e., it holds: (cid:48) with  
m h = m mod 5 = m mod 5  
(cid:48) (cid:88)  
m = m  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 16  
h)* Assess the general significance of a Message Authentication Code (MAC) regarding authenticity when you have received the corresponding key along with the message.  
1  
(cid:88)  
Authenticity of the message cannot generally be guaranteed, as the coupling between the holder and the key is no longer ensured.  
1 i)* Justify whether a Message Authentication Code (MAC) is effective against replay attacks, i.e., repeated sending of the same messages.  
(cid:88) (cid:88)  
No, repeated sending of the same messages does not lead to invalid MACs.  
1 j)* Name a protection goal known from the lecture that cannot be achieved through cryptographic methods in general.  
(cid:88)  
Availability  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
17 Name:  
Task 6 Surfing the Web (13 Points)  
13  
Given is the following infrastructure. The client runs a browser that accesses the URL "http://web.lan/grnvs.html". The end-to-end messages sent over the network are marked with dashed lines, and the arrows indicate the direction of the sender. They are labeled a – f.  
Assume that the router already has the DNS server and the web server in the ARP cache; the client's caches are empty. Furthermore, assume that all services use their standard ports. You can specify MAC addresses in the style Host.Interface, e.g., C.eth0.  
k  
a  
k  
b  
DNS Server D  
192.168.2.2  
192.168.1.1 eth0: 00:30:05:79:55:D0  
eth0: 00:30:05:79:55:A1  
Switch SW Router R  
Client C  
k  
192.168.1.2  
eth0: 00:30:05:79:55:C0 192.168.2.1  
ek eth1: 00:30:05:79:55:A2  
Web Server W  
f URI: web.lan  
k 192.168.2.3  
eth0: 00:30:05:79:55:E0  
c  
k  
d  
Figure 6.1: Network Topology  
a)* What do the first three bytes of the MAC address depend on?  
1  
(cid:88)  
Each manufacturer has a unique three-byte prefix.  
b)* Which headers of the message from the client to the web server are changed by the switch? Briefly justify your answer.  
1  
(cid:88) (cid:88)  
None. The switch simply forwards the messages transparently.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: k k 18  
c)* Fill out Table 2 completely. Provide the messages a – f in chronological order and name the highest protocol used in the message (related to the layer model).  
2  
Nr Message Type Nr Message Type  
1 ek ARP 4 bk(cid:88) DNS(cid:88)  
2 fk(cid:88) ARP(cid:88) 5 ck(cid:88) HTTP(cid:88)  
3 a (cid:88) DNS(cid:88) 6 d (cid:88) HTTP(cid:88)  
Table 2: End-to-End Messages  
k  
2 d) What IP packets must be sent when sending message a? Fill in a row for each packet in the following table.  
(cid:88)  
Note: The table may contain more rows than necessary. One point per row.  
MAC IP Port  
from to from to from to  
C.eth0 R.eth0 .1.2 .2.2 1234 53  
R.eth1 D.eth0 .1.2 .2.2 1234 53  
k  
2 e) Do the same for message d.  
(cid:88)  
Note: This table may also contain more rows than necessary. One point per row.  
MAC IP Port  
from to from to from to  
Web.eth0 R.eth1 .2.3 .1.2 80 5678  
R.eth0 C.eth0 .2.3 .1.2 80 5678  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
19 Name:  
Below you will find the first TCP packet that the client sends to the web server.  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
(47562)10 (80)10  
(17542)10  
(0)10  
0 0 0 0 0 0 0 0 0 0 1 0  
(5)10 (24212)10  
1e25  
( )16 (0)10  
Figure 6.2: First TCP Packet from Client to Web Server  
f)* Fill in the white fields of the TCP header of the server's response (Fig. 6.3) correctly. Also, ensure that the flags are set correctly.  
3  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
(80)10 (47562)10  
(24568)10  
(17543)10  
0 0 0 0 0 0 0 1 0 0 1 0  
(6)10 (14480)10  
2647  
( )16 (0)10  
Options  
Figure 6.3: TCP Header of the Web Server's Response  
g)* Which end-to-end request-response pairs in representation 6.1 cannot be protected by TLS? Justify your answer for each mentioned pair.  
The connection to the DNS server cannot be protected by TLS because requests occur over UDP. The connection to the router during ARP requests cannot be protected by TLS because TLS operates at a higher layer than ARP.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 20  
Replacement template for task 2k).  
Device 1 Device 2  
SEQ=0  
SEQ=1  
ACK=1  
SEQ=2  
ACK=2  
(cid:18)  
Additional space for solutions – please clearly mark the association with the respective task and cross out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
21 Name:  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 22  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
23 Name:  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014