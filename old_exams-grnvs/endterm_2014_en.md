Name First Name  
Grade  
Degree Program (Major) Field of Study (Minor)  
I II  
Student ID Number  
Signature of Candidate  

TECHNICAL UNIVERSITY OF MUNICH  
Faculty of Computer Science  

Midterm  
× Endterm  
Repetition  

Subject of Examination: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle Date: 22.07.2014  
Lecture Hall: Row: Seat:  

To be filled out by the supervisor only:  
Lecture hall left from: until:  
Submitted early at:  
Special remarks:  

Endterm Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
Tuesday, 22.07.2014  
11:30 – 13:00  

- This exam consists of 23 pages and a total of 6 tasks. Additionally, a supplementary sheet with protocol headers will be distributed. Please check now whether you have received a complete set of materials.  
- Please write your name and student ID number in the header of each page.  
- Do not write in red/green ink or with a pencil.  
- The total number of points is 85.  
- Allowed aids are a double-sided handwritten DIN A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Do not spend too long on a (sub-)task. If you cannot solve the task immediately, it is better to move on to the next task.  
- Only results where a solution path is recognizable will be graded. Text tasks must be justified unless explicitly stated otherwise in the respective sub-task.  

Task 1 Fourier Series (10 Points)  
Given is the periodic triangular pulse shown in Figure 1.1. This signal is to be represented as a Fourier series:  
s(t) = a₀ + Σ (a_k cos(kωt) + b_k sin(kωt))  
k=1 to ∞  

The coefficients for all integers k > 0 can be determined as follows:  
a_k = (1/T) ∫ (s(t) cos(kωt) dt) from -T/2 to T/2,  
b_k = (1/T) ∫ (s(t) sin(kωt) dt) from -T/2 to T/2.  

s(t)  
π  
− − − t  
3π 2π π π 2π 3π  
Figure 1.1: Periodic Triangular Pulse  

a) Provide an analytical expression for the sending base pulse, i.e., for the signal in the interval t ∈ [-π; π].  
b) Determine the period duration and angular frequency of the signal.  
T ω = 2π/T  
c) Determine the DC component a₀.  
d) Justify why b_k = 0 for all k ∈ N (no calculation necessary).  
e) Show that for the cosine components the following holds:  
a_k = 4/(k²π) for k = 1, 3, 5,...,  
a_k = 0 otherwise.  

Hint: Depending on the solution path, one of the following hints may be helpful:  
∫ (t sin(kt) + cos(kt)) dt = (1/k²) cos(kt) + const  
∫ f(t) g'(t) dt = [f(t) g(t)] - ∫ f'(t) g(t) dt  

f) Draw the approximated signal s'(t) = a₀ + a₁ cos(ωt) in Figure 1.1.  

Task 2 PHY and MAC in PCIe (16 Points)  
The ISO/OSI model is not only applicable to communication processes on the Internet. Rather, it is an abstract model for any communication processes. In this task, we consider the application to PCIe (Peripheral Components Interconnect Express), which today represents the standard for fast data exchange between devices within a computer. For example, in modern computers, practically all internal expansion cards (graphics cards, network cards, sound cards, etc.) as well as many integrated devices such as SATA controllers are connected via this interface. PCIe itself is a serial, switched network between these devices.  

a) Justify the advantage of switched connections over a bus system.  
At the physical layer, PCIe uses two data lines per direction per lane, on which signals are transmitted differentially encoded. An example is shown in Figure 2.1. The received signal results from the addition of both individual signals, i.e., s(t) = s⁺(t) + s⁻(t).  

s⁺(t)  
400mV  
t  
t  
−400mV  
s⁻(t)  
s(t)  
400mV  
t  
−400mV  
Figure 2.1: Differentially encoded signals s⁺(t) and s⁻(t) as well as the received signal s(t) = s⁺(t) + s⁻(t).  

b) Draw the received signal in Figure 2.1.  
c) What sending base pulse does PCIe obviously use?  
d) Indicate the transmitted bit sequence in Figure 2.1. Enter your solution directly in Figure 2.1. Hint: There are two equivalent solutions.  
e) Name one advantage of differential transmission in this specific case.  
f) PCIe uses 8B10B encoding as a line code. Name two advantages that arise from this.  
g) The gross data rate is 2.5 Gbit per lane and transfer direction. Determine the net data rate considering the 8B10B encoding.  

At the data link layer, PCIe uses 32-bit long CRC checksums. For simplicity, we assume that each frame carries an 8-bit long sequence number, which is incremented by the sender for each sent frame. The send and receive buffers on both sides hold 4 frames. Go-Back-N is used for flow control. The receiver acknowledges (ACK) successfully transmitted frames, with acknowledgments always containing the next expected sequence number. Furthermore, the sender is explicitly informed about incorrectly transmitted frames via negative acknowledgments (NACK). Subsequent correctly transmitted frames with a higher sequence number are ignored and not acknowledged according to Go-Back-N.  

h) What goal is pursued by the checksums?  
i) Name another transmission technique you know that also uses acknowledgments at the data link layer.  
j) Describe the goal pursued with flow control.  

k) Given is the message exchange printed in the solution field. In the frame marked by a lightning bolt (SEQ=2), an error is detected at the receiver. Complete the message exchange until SEQ=4 has been successfully transmitted. Assume that no further errors occur.  
Hint: You will find another template on page 20 if needed. Please clearly cross out invalid solutions.  

Device 1 Device 2  
SEQ=0  
SEQ=1  
ACK=1  
SEQ=2  
ACK=2  

l) How would the result of sub-task k) change if Selective Repeat were used?  

Task 3 IP Fragmentation and Path-MTU Discovery (19 Points)  
In this task, we first consider fragmentation in IPv4. The network topology is given in Figure 3.1.  

MTU:1500B MTU:1280B MTU:576B  
PC1 R1 R2 PC2  

Figure 3.1: Network Topology  

Routers R1 and R2 are configured so that hosts PC1 and PC2 can communicate with each other. The three network segments are independent of each other and use different transmission technologies, resulting in the MTUs visible in the figure.  

a) Distinguish between the terms MTU and MSS.  
b) How should the MSS be chosen in relation to the MTU (formula)?  
c) Can fragments be fragmented again?  
d) At which point in the network are fragments reassembled (justification)?  

e) How can you tell that it is a complete (unfragmented) IP packet?  
f) What problem occurs at the receiver when individual fragments are lost?  

Now assume that PC1 has established a TCP connection to PC2. PC1 wants to send 1460B of payload over this TCP connection to PC2. PC1 sends this data considering the necessary minimal IP and TCP headers. Router R1 cannot forward the resulting packet directly and must first fragment it.  

g) Indicate the respective size of all IP packets sent from R1 to R2.  
h) Router R2 must now process these packets in an appropriate manner. Indicate the respective size of all IP packets sent from R2 to PC2.  

As an alternative to IP fragmentation, we now consider Path-MTU Discovery. We continue to use the network topology from Figure 3.1. PC1 still wants to send payload of length 1460B to PC2 over an already established TCP connection. Path-MTU Discovery is used to prevent fragmentation in the network. So that the sender does not have to perform IP fragmentation either, it can adjust the TCP MSS accordingly. Path-MTU Discovery works as follows:  
- The sender first sends packets of the size of the local MTU.  
- These packets must not be fragmented in the network.  
- If a router receives such a packet but cannot forward it directly due to the MTU in the subsequent network segment, it sends an ICMP Destination Unreachable, Fragmentation Needed (Type 3, Code 4) message to the sender.  
- This message contains the MTU of the subsequent network segment, and the router discards the original packet.  
- The sender must resend the data while adhering to this MTU. In TCP, this is possible by adjusting the MSS.  
- The sender stores the MTU for subsequent packets with the same destination.  

i) How does the sender ensure that its packets may not be fragmented in the network?  
j) How can the sender generally assign an ICMP message (Type 3, Code 4) during simultaneous Path-MTU Discovery to multiple destinations?  

k) Calculate the respective size of all required IP packets to transmit TCP payload of length 1460B from PC1 to PC2 without any fragmentation. Consider all necessary headers in their minimal size.  
l) Now draw a simplified time-distance diagram (serialization time and propagation delay can be neglected) for the Path-MTU Discovery and the sending of the message (1460B TCP payload). Indicate the total size of the IP packet for data packets ("IP packet, 128B"). ICMP Fragmentation Needed packets should be marked as such, and the returned MTU should be indicated ("ICMP Frag. needed, 256B"). Note: The initial congestion window for TCP is 10 MSS. Neglect TCP acknowledgments and any Layer 2 messages.  

Task 4 Routing in IP Networks (13 Points)  
Figure 6.1 shows an IPv4-based network. It consists of several hosts (H1, H2, ...), routers R1, R2, and R3, and switch S1. Table 1 shows the routing tables of R1 and R2.  

Internet  
192.0.2.34  
203.0.  
188.95.234.2  
R3 H5  
H1  
eth2: 188.95.234.7 eth1: 192.0.2.33  
203.0.113.9 eth1: 203.0.113.253  
eth0: 203.0.113.11 eth0: 203.0.113.254 eth2: 192.0.2.65  
H2 S1 R1 R2 H4  
203.0.  
H3  

Figure 4.1: Network Topology  

a) Name the network address and the broadcast address of the network 203.0.113.8/29.  
Network address:  
Broadcast address:  

b) How many addresses in the network 203.0.113.8/29 can be assigned to hosts?  
c) Assign valid IP addresses to hosts H1 and H3. Enter your answer directly in Figure 6.1.  

Router R1  
Destination Gateway Iface  
203.0.113.8/29 — eth0  
203.0.113.252/30 — eth1  
188.95.234.7/23 — eth2  

Router R2  
Destination Gateway Iface  
192.0.2.32/27 — eth1  
192.0.2.64/27 — eth2  
192.0.2.96/27 192.0.2.34 eth1  

Table 1: Static Routing Tables of Routers R1 and R2.  

d) How can a router determine if the route with address and subnet mask is applicable for the address of a packet?  
e) Which entry from the forwarding table does a router choose when multiple entries are suitable?  
f) Name two criteria that must be met for a router to aggregate two entries in its table.  
g) Aggregate the following networks as much as possible. Use a binary tree representation as shown.  
192.0.2.24/29  
192.0.2.16/29  
192.0.2.24/30  
192.0.2.28/30  
192.0.2.32/27  
192.0.2.64/27  
192.0.2.96/27  

h) Complete the routing table (Table 1 on p. 12) so that every host can reach every other host in the given network and in the Internet, and all entries are aggregated as much as possible.  

Task 5 Key Exchange and Applications (14 Points)  
The Diffie-Hellman key exchange method is considered. Given are the prime number and the primitive root. Alice and Bob want to apply this method.  
p = 17 g = 3  
Assume Alice chooses a = 9 and Bob chooses b = 5 as random numbers.  

a) Sketch the Diffie-Hellman key exchange by drawing the necessary messages in the following diagram. Label the messages with both the general formulas and the specific values.  
Alice Bob  

b) Determine the Shared Secret ("key") that Bob and Alice can now calculate.  
c) Justify whether a suitable choice for g = 16 would also be valid (calculation and justification).  

d) Justify whether the Diffie-Hellman key exchange is secure against Man-in-the-Middle attacks.  
e) How would the public and private keys for Alice and Bob look when using El Gamal? Use your specific values from the previous tasks.  
Note: These can be directly derived from the Diffie-Hellman method.  

An independent third party now wants to send Alice an encrypted message and uses Alice's public key, which she has already determined in one of the previous sub-tasks.  

f) Alice receives the encrypted message. Determine the plaintext.  
(X,c) = (9,8)  

g) Justify whether the hash function h = n mod 5, where the message represents n ∈ N, has sufficient cryptographic strength.  
h) Assess the general significance of a Message Authentication Code (MAC) regarding authenticity when you have received the associated key along with the message.  
i) Justify whether a Message Authentication Code (MAC) is effective against replay attacks, i.e., the repeated sending of the same messages.  
j) Name a protection goal known from the lecture that cannot be achieved through cryptographic methods in general.  

Task 6 Surfing the Web (13 Points)  
Given is the following infrastructure. The client runs a browser that accesses the URL "http://web.lan/grnvs.html". The end-to-end messages sent over the network are marked with dashed lines, and the arrows indicate the direction of the sender. They are labeled a – f.  

Assume that routers already have the DNS server and the web server in their ARP cache; the caches of the clients are empty. Furthermore, assume that all services use their standard ports. You can specify MAC addresses in the style Host.Interface, e.g., C.eth0.  

a) What do the first three bytes of the MAC address depend on?  
b) Which headers of the message from the client to the web server are modified by the switch? Briefly justify your answer.  
c) Fill out Table 2 completely. Indicate the messages a – f in chronological order and name the highest protocol used in the message (related to the layer model).  

| Nr | Message | Type |  
|----|---------|------|  
| 1  | e       | ARP  |  
| 2  | 5       |     |  
| 3  | 6       |     |  

Table 2: End-to-End Messages  

d) Which IP packets must be sent when sending message a? Fill in a row for each packet in the following table.  
Note: The table may contain more rows than necessary.  

| MAC | IP | Port |  
|-----|----|------|  
|     |    |      |  

e) Do the same for message d.  
Note: This table may also contain more rows than necessary.  

| MAC | IP | Port |  
|-----|----|------|  
|     |    |      |  

Below you will find the first TCP packet that the client sends to the web server.  

f) Fill in the white fields of the TCP header of the server's response correctly. Also, make sure to set the flags correctly.  

g) Which end-to-end request-response pairs in representation 6.1 cannot be protected by TLS? Justify your answer for each mentioned pair.  

Replacement template for task 2k).  
Device 1 Device 2  
SEQ=0  
SEQ=1  
ACK=1  
SEQ=2  
ACK=2  

Additional space for solutions – please clearly mark the affiliation with the respective task and cross out invalid solutions!