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
× Final Exam c
5
s
Semester Exam
r
Diploma Preliminary Exam 6
o
Bachelor Exam
v 7
............................
s
Consent to Grade Notification 8
via Email / Internet
n
9
u
10
s
Exam Subject: Fundamentals of Computer Networks and Distributed Systems
ö
L
Examiner: Prof. Dr. Uwe Baumgarten Date: 12.10.2011
P
Lecture Hall: MW 1801 Row: .................... Seat: .....................
To be filled out by the supervisor only:
Lecture hall exit from ...... : ...... to ...... : ......
Submitted early at ....... : ......
Special Remarks:
Make-up Exam
Fundamentals of Computer Networks and Distributed Systems
Prof. Dr. Uwe Baumgarten
Chair of Operating Systems and System Software
Faculty of Computer Science
Technical University of Munich
Wednesday, 12.10.2011
14:30 – 16:00
• This exam consists of 23 pages and a total of 5 tasks. Please check now that you have received a complete set of materials.
• Please write your name and student ID in the header of each page.
• The total number of points is 85.
• Allowed materials are a double-sided A4 sheet with any notes and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.
• Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
• Only those results will be counted where a solution method is recognizable. Text problems must be justified unless explicitly stated otherwise in the respective sub-task.
1 Name:
Task 1
Bandwidth Estimation Using Packet-Pair Training (20 Points)
20
Consider the network in Figure 1.1. Nodes i and j are connected via an asynchronous link. Consequently, the data rates differ in the upstream and downstream, i.e., r ≠ r. Node i could, for example, be the router of a home network. Node j would be the access point operated by a service provider.
Home Network Public Network
r
ji
PC i j Internet
r
ij
Figure 1.1: Logical Network Topology
In this task, a method is to be developed that allows node i to determine the upstream bandwidth. However, this should not be done by saturating the connection. Instead, we want to achieve our goal with as few packets as possible.
To this end, the method will be derived step by step through general calculations (without numerical values!) in sub-tasks a) – h). Subsequently, the developed method will be applied to specific numerical values obtained from an actual measurement.
We neglect layer 2 headers in this task. The packet size x thus denotes a layer-3 PDU. You can also assume that no further communication occurs between the involved nodes.
a)* Provide the serialization time s (x) on the link from i to j as a function of the packet size x.
x
s (x) =
ij
r
ij
b) Show or disprove: s (x) = s (x). 1
ij ji
It holds that s (x) ≠ s (x), since r ≠ r.
ij ji ij ji
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 2
c)* Provide the propagation delay p (l) on the link from i to j as a function of the length l of the physical connection (cable length) between i and j.
1
l
p (l) =
ij
νc
1 d) Show or disprove: p (l) = p (l).
ij ji
It holds that p (l) = p (l), since the propagation speed νc is identical in both directions.
ij ji
(On the next page it continues)
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
3 Name:
Typically, the upstream bandwidth for internet connections does not exceed the reachable downstream bandwidth. We therefore assume that r ≤ r holds. The following packets are now exchanged:
1. Node i sends a packet of length x to node j (e.g., an ICMP Echo Request).
1
2. Node j responds to this packet with a packet of the same length x.
1
3. After a short pause, i sends another packet – this time of length x > x.
2 1
4. This is again answered by j with a packet of the original length x.
1
Any processing times at the nodes themselves can be neglected.
e)* Draw a time-path diagram of the above-described message exchange. The serialization times and propagation delays should be qualitatively correct. Ensure a complete labeling of the diagram!
i j
RTT(x )
1
RTT(x )
2
X
Looks like a time-path diagram and i,j are on the axes
X
Packets 2 and 4 are identical
X
Serialization time of packet 1 is greater than that of packet 2
X
Propagation delays are all equal (same slope)
X
Serialization time of packet 3 is greater than that of packet 1
The round-trip time (RTT) between two nodes i and j is defined as the time between sending the first bit of a message and the complete receipt of a response – including any processing delays at node j. From the diagram of sub-task e), two such RTTs should emerge, which we will refer to as RTT (for packets 1 and 2) and RTT (for packets 3 and 4).
1 2
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 4
f) Mark RTT and RTT in your solution from sub-task e).
1 2
2
XX
Notes: Correct marking in the solution of sub-task e).
2 g) Provide the round-trip times RTT and RTT between i and j as a function of the packet sizes x and x.
1 2
Use the results from sub-tasks a), c), and e). Ensure that node j always sends packets of length x!
1
X
RTT = s (x ) + 2p (l) + s (x )
1 ij 1 ij ji 1
X
RTT = s (x ) + 2p (l) + s (x )
2 ij 2 ij ji 1
3 h) Calculate Δ := RTT - RTT. Simplify the expression as much as possible!
2 1
Δ = RTT - RTT
2 1
X
= s (x ) + 2p (l) + s (x ) - s (x ) - 2p (l) - s (x)
ij 2 ij ji 1 ij 1 ij ji 1
X
= s (x ) - s (x )
ij 2 ij 1
x - x X
2 1
=
r
ij
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
5 Name:
For the following sub-tasks, you will need the intermediate result from sub-task h):
x - x
2 1
Δ = .
r
ij
The RTT between i and j is now measured three times for two different packet sizes. The results are summarized in Table 1.
Measurement x = 48b x = 1328b
1 2
1 68.62ms 91.47ms
2 65.57ms 92.14ms
3 65.06ms 93.33ms
Table 1: RTT measurements with different packet sizes.
i)* Why was the RTT measured multiple times for each packet size? 1
The measurement is subject to disturbances, which are less significant through repeated measurements and averaging.
j)* Determine the upstream r. 3
ij
Note: Use the average of the RTTs from Table 1.
68.62 + 65.57 + 65.06
RTT(x ) = ms ≈ 66.32ms
1
3
91.47 + 92.14 + 93.33
RTT(x ) = ms ≈ 92.31ms
2
3
Δ = RTT(x ) - RTT(x ) ≈ 25.90ms
2 1
x - x 1280b
2 1
r = = ≈ 395kbit/s
ij
Δ 25.90ms
X
• Averaging
X
• Difference
X
• Result
1If interested: The measurement was conducted on a T-DSL 3000.
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 6
Additional space for solutions to Task 1 – please clearly mark the affiliation to the respective sub-task and strike out invalid solutions!
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
7 Name:
Task 2
Routing and NAT (20 Points)
20
Consider the network topology from Figure 2.1. A PC and a notebook (NB) are connected via an Ethernet switch to router R1, which provides access to the internet. The switch is the cheapest model available and has no special capabilities. Since the three devices are connected via a private network, R1 must support NAT.
PC
IP 172.16.34.129
Subnet 255.255.255.248
eth0
Gateway 172.16.34.134
eth0 wan0 wan1 Internet eth0 eth0
172.16.34.134 87.186.224.45 87.186.224.46 131.159.15.254 131.159.15.49
255.255.255.248 R1 255.255.255.252 255.255.255.252 R2 R3 255.255.255.0 255.255.255.0
SRV
eth0
IP 172.16.34.130
Subnet 255.255.255.248
Gateway 172.16.34.134
NB
Figure 2.1: Network Topology
a)* Complete the binary representation of the subnet mask of the private network in the solution field below. Which part of the subnet mask defines, together with an IP address, the network part and which the host part?
11111111 . 11111111 . 11111111 . 11111 000 X
X
Network Part Host Part
b) How many IP addresses are available in the private network for addressing hosts (including the IP of R1)? 1
X
23 - 2 = 6
c) Provide the network and broadcast address for the private network. 2
X
• Network Address: 172.16.34.128
X
• Broadcast Address: 172.16.34.135
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 8
d) How many such subnets exist in the network 172.16.34.0/24? 1
The network part in the last octet consists of 5 bits. Therefore, there are a total of 2^5 = 32 such subnets.
X
2 e) Assign a sensible combination of IP address, subnet mask, and gateway to PC and NB. Enter these directly into Figure 2.1.
Notes:
1 f) Which header fields of forwarded frames does the switch modify that connects PC, NB, and R1? Specify the layer to which the modified fields belong, if applicable.
X
None.
1 g) What transport protocol and destination port number are typical for (unencrypted) HTTP connections?
TCP 80
In the following, we will abbreviate IP and MAC addresses of known devices according to the scheme IP.<Name>.<IF> or MAC.<Name>.<IF>, e.g., IP.R1.eth0 and MAC.R1.WAN0.
Also, for the following sub-tasks, note that there should be two additional routers between R2 and R3, as indicated in the figures.
4 h)* Complete the header fields for the request from the PC to the web server SRV in the three empty boxes in Figure 2.2. If a field is not clearly defined, make a sensible choice.
Note: If you could not solve sub-task g), assume destination port 80.
4 i) Complete the header fields for the response from the web server SRV to the PC in the three empty boxes in Figure 2.3. If a field is not clearly defined, make a sensible choice.
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
9 Name:
V
R
S
090
0th0 eth15.4255.
C.ethAC.ean0eth0 1.159.5.255.
AMwP. 1325
3.MRV.1.IP.RV.I000009
RSRS285
CC
AA rtrt 540
SrcMDstMSrcIPDstIPSrcPoDstPoTTL 59.15.255.255.
12
eth0131.255.
3
R
)
h
01 3
1.MAC.wan2.MAC.wan1.IP.wan0RV.IP.eth0000003 Internet uckzuTask
RRRS286 dr
r
o
V
ACAC rtrt R2 2.2:
MMPPoo g
SrcDstSrcIDstISrcPDstPTTL wan124.465.252 bildun
25 b
86.5.2 A
15
87.5.2
5
2
2
5
52
4.455.
00 22
AC.ethAC.etheth0P.eth0 wan087.186.2255.255.
MMIP.V.I00 1
C.1.C.R0004 R
PRPS286
048
h34
CC et4.15.2
SrcMADstMASrcIPDstIPSrcPortDstPortTTL 172.16.3255.255.25
C B
P h0 h0 N
et et
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 10
V
R
S
090
th00 eth15.4255.
AC.eC.etheth0an0 1.159.5.255.
MAP.w 1325
RV.3.MRV.I1.IP.000004
SRSR826
CC
AA rtrt 540
SrcMDstMSrcIPDstIPSrcPoDstPoTTL 59.15.255.255.
12
eth0131.255.
3
R
A
b
b
ild n1n0
ung2.3: AC.waAC.waP.eth0wan0 nternet
Differently from the lecture, R1 stores not only the triple consisting of local IP and local and global source port, but also the protocol used as well as destination port and destination IP. Table 2 shows an example of how such a NAT table might have looked before sub-tasks h) and i).
Protocol Local IP Local Port Global IP Global Port Destination IP Destination Port
TCP IP.PC 50034 IP.R1.wan0 50034 83.133.105.60 22
TCP IP.PC 49985 IP.R1.wan0 49985 213.165.65.50 443
Table 2: NAT table of R1 before sub-tasks h)
j) According to Table 2, provide the entries that were created by the connection establishment from the PC to the web server in sub-tasks h) and i).
Protocol Local IP Local Port Global IP Global Port Destination IP Destination Port
TCP IP.PC 20000 IP.R1.wan0 20000 IP.SRV 80
k) Now assume that the notebook NB also wants to establish a connection to this web server. By chance, NB chooses the same source port as the PC. Provide valid entries in the NAT table that arise from the connection establishment of the notebook to the web server.
Protocol Local IP Local Port Global IP Global Port Destination IP Destination Port
TCP IP.NB 20000 IP.R1.wan0 20001 IP.SRV 80
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 12
Task 3
Transport Protocols (23 Points)
23
Two computers PC1 and PC2 communicate with each other over the internet. In this task, we will examine a TCP connection between these two computers:
• the connection establishment,
• an exemplary message exchange,
• the behavior in case of message loss, and
• the connection teardown.
We assume that a very simple chat application is running on PC1 and PC2, which uses TCP as the transport protocol. PC2 is to act as the server. When the application is started on PC1, it establishes a connection to PC2. Subsequently, bidirectional communication is possible until one of the two sides tears down the connection.
2 a)* What information does the chat application on PC1 need to successfully establish a connection to PC2?
X
The IP address of PC2 and the port number on which the chat application on PC2 expects incoming connections. (The protocol is already specified by the application itself.)
2 b)* What information do PC1 and PC2 exchange during the connection establishment?
X X
The initial sequence numbers and the window size. (possibly options)
1 c) Are the chat application or the operating systems of the PCs responsible for exchanging the information from sub-task b)? (Justification)
The chat applications open sockets that are provided by the respective operating system. Connection establishment, teardown, and retransmission of lost packets is the responsibility of the operating system in the case of TCP.
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
13 Name:
In the following, several time-path diagrams are to be created that represent the message exchange between PC1 and PC2:
• You can neglect serialization time and propagation delay.
• Note the sequence number above each exchanged message, e.g., SEQ=N.
• If the ACK flag is set, also note the acknowledgment number, e.g., ACK=N.
• Other flags (SYN, FIN, PSH) should only be specified if they are set.
d) Sketch a simplified time-path diagram for the connection establishment. 4
SYN,SEQ=N
SYN,SEQ=M,ACK=N+1
SEQ=N+1,ACK=M+1
X
Recognizable that this is something like a 3-way handshake
X
SYN flags at 1 and 2, but not at 3
X
Correct sequence numbers
X
Correct acknowledgment numbers
Now the following chat messages are exchanged between PC1 and PC2:
1. PC1 ! PC2: “The great thing about TCP jokes is that you always get them.”
2. PC2 ! PC1: “Nerd!”
We assume that the messages are transmitted in ASCII encoding.
e) How long will the TCP segments be with which the two messages are exchanged? 1
Counting characters yields:
X
• 60b for message 1
X
• 5b for message 2
Also correct: +1 or +2 bytes for newline / carriage return characters.
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 14
f) Now draw another time-path diagram that represents the exchange of the two messages. Consider that the user at PC2 needs a few seconds to input his message.
4
SEQ=N+1,ACK=M+1
SEQ=M+1,ACK=N+61
SEQ=M+1,ACK=N+61
SEQ=N+61,ACK=M+6
-1 for each error
2 g) Briefly describe what happens if the acknowledgment for the second message (i.e., the one from PC2 to PC1) is lost.
X X
After a timeout (missing acknowledgment), PC2 will resend the message.
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
15 Name:
h) How can PC1 distinguish a repeated message from a new message?
1
A repeated message does not fall within the receive window (= range of expected sequence numbers) of PC1.
X
i) What happens if a message is recognized as a duplicate? 2
X X
The duplicate is discarded in this case, but the receipt is acknowledged again.
j) Immediately after the exchange of the above messages, PC2 initiates the connection teardown. 4
Sketch the connection teardown as a time-path diagram.
FIN,SEQ=M+6,ACK=N+61
FIN,SEQ=N+61,ACK=M+7
SEQ=M+7,ACK=N+62
X
Recognizable that this is something like a 3-way close
X
FIN flags at 1 and 2, but not at 3
X
Correct sequence numbers
X
Correct acknowledgment numbers
Also correct: 4-way close if message 2 is split into two messages (ACK and FIN)
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 16
Additional space for solutions to Task 3 – please clearly mark the affiliation to the respective sub-task and strike out invalid solutions!
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
17 Name:
Task 4
Domain Name System (12 Points)
12
In this task, the Domain Name System (DNS) will be examined. Table 3 lists fully qualified domain names of some hosts and DNS servers.
Hosts under tum.de. Hosts under mit.edu. DNS Servers
www.tum.de. www.mit.edu. ns.internic.net.
www.in.tum.de. www.eecs.mit.edu. f.nic.de.
www.ei.tum.de. www.econ.mit.edu. a.edu-servers.net.
www.net.in.tum.de. dns1.lrz.de.
www.nws.ei.tum.de. bitsy.mit.edu.
slacky.net.in.tum.de.
luise.nws.in.tum.de.
Table 3: Fully Qualified Domain Names
The DNS servers are authoritative for the following zones (i.e., they are responsible for fully qualified names of the respective zones):
• ns.internic.net: Root Zone (de, edu, com, net, ...)
• f.nic.de: Zone de.
• a.edu-servers.net: Zone edu.
• dns1.lrz.de: Zone tum.de. and all subzones2
• bitsy.mit.edu: Zone mit.edu. and all subzones
a)* What is the purpose of DNS? 1
X
Translation of fully qualified names into IP addresses.
b)* Name the individual components that make up the fully qualified name www.in.tum.de. 2
From right to left: Root, Top Level Domain, Second Level Domain, Third Level Domain, Hostname.
XX
2This is a simplification – in reality, there are several other DNS servers.
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 18
c)* Create a tree from the fully qualified names in Table 3, starting at the root “.” of the namespace. All names belonging to the same domain should be on the same level in the tree.
·
de net edu
nic tum lrz internic edu-servers mit
f in www ei dns1 ns a bitsy eecs econ www
www net www nws www www
www slacky www luise
·
To sub-task d):
de net edu
nic tum lrz internic edu-servers mit
7
5
3
f in www ei dns1 ns a bitsy eecs econ www
2
4
8 6
www net www nws www www
1
www slacky www luise
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
19 Name:
We assume that all DNS caches are empty. The computer slacky.net.in.tum.de uses the DNS server dns1.lrz.de for name resolution. We assume that it accepts recursive requests from clients and resolves names iteratively.
d) In your solution from sub-task c), draw all DNS messages that are exchanged when the command ping www.eecs.mit.edu is executed on slacky.net.in.tum.de. Number the messages according to their chronological order. Further details are not necessary.
Notes:
e) Can slacky.net.in.tum.de resolve the name luise.nws.ei.tum.de if the root server ns.internic.net fails? 1
X
Yes, everything within the zone tum.de or its subzones is still reachable. (If someone argues that the name of the LRZ server is also not resolvable, that is also okay.)
f) Can slacky.net.in.tum.de resolve the name www.econ.mit.edu if the root server ns.internic.net fails? 1
X
No, as it is in a different subtree. (If someone argues with caching or redundant root servers, that is also okay.)
Since DNS operates hierarchically, multiple messages may need to be sent to resolve a name. For the next two sub-tasks, assume that a single request (between client and server or between any two servers) takes 100ms and that there is a separate authoritative name server for each zone.
g)* How long does it take slacky.net.in.tum.de at minimum to resolve the name www.google.com? 2
• slacky.net.in.tum.de sends a request for recursive name resolution to dns1.lrz.de
• dns1.lrz.de immediately contacts one of the root servers
• dns1.lrz.de contacts an authoritative server for the com zone.
• dns1.lrz.de contacts an authoritative server for the google.com zone.
• dns1.lrz.de receives the response from ns.google.com
XX
) 500ms (also okay: 600ms if the return of the response is counted).
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 20
Task 5
Short Tasks (10 Points)
10
The following short tasks are independent of each other. Bullet-point answers are sufficient!
3 a)* You receive the binary message 1011101101. The generator polynomial is g(x) = x^2 + 1. Check if an error occurred during transmission.
X
The generator polynomial in binary representation: 101
1011101101 : 101 = ?, Remainder?
X X
Correct approach (no appending of zeros), Correct remainder
2 b)* Briefly describe (2-3 bullet points are sufficient) how the traceroute program works.
X
• Sends packets with incremental TTL
X
• ICMP Time-Exceeded messages are provoked by individual routers along a path
1 c)* Why can problems with ICMP messages occur when using NATs?
Note: Think about how a NAT can assign incoming ICMP messages to a private IP address.
ICMP is based directly on IP, not on a transport protocol. Therefore, there are no port numbers.
X
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
21 Name:
d)* Justify or refute the claim that using token-passing as an access protocol results in transmission times in the local network being largely deterministic.
2
With CSMA/CD, collisions can occur (almost) arbitrarily often, leading to delays. Token-passing typically guarantees a collision-free, fair, and thus deterministic operation.
X X
e)* Justify (either argumentatively or through calculation) whether the time signal s(t) shown below has a DC component.
s(t)
A
t
-3T -2T -T T 2T 3T
-A
Note: The signal can be represented as a Fourier series, i.e., it holds
X1
a
0
s(t) = + (a cos(kωt) + b sin(kωt)).
k k
2
k=1
with the coefficients
Z Z
2 T 2 T
a = s(t)·cos(kωt) dt and b = s(t)·sin(kωt) dt.
k k
T T
0 0
The signal has a DC component, as the signal is not zero-mean.
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
Student ID: 22
Additional space for solutions – please clearly mark the affiliation to the respective task and strike out invalid solutions!
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011
23 Name:
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011