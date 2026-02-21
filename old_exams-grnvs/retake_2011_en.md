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
Subject of Examination: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr. Uwe Baumgarten Date: 12.10.2011  
Auditorium: MW 1801 Row: .................... Seat: .....................  
To be filled out by the supervisor only:  
Auditorium left from ...... : ...... to ...... : ......  
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
• Allowed aids are a double-sided sheet of DIN A4 paper and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
• Tasks marked with * can be solved without knowledge of the results of preceding sub-tasks.  
• Only those results will be counted where a solution path is recognizable. Text tasks must be justified unless otherwise stated in the respective sub-task.  

1 Name:  
Task 1 Bandwidth Estimation Using Packet-Pair Training (20 Points)  
20  
Given the network from Figure 1.1. Nodes i and j are connected via an asynchronous link. Consequently, the data rates differ in upstream and downstream, i.e. \( r_{ij} \neq r_{ji} \). Node i could, for example, be the router of a home network. Node j would in this case be the access point operated by a service provider.  

Home Network Public Network  
\( r_{ji} \)  
PC i j Internet  
\( r_{ij} \)  
Figure 1.1: Logical Network Topology  
In this task, a method is to be developed that enables node i to determine the upstream bandwidth. However, this should not be done by saturating the connection \( r_{ij} \). Instead, we want to achieve our goal with as few packets as possible.  
In sub-tasks a) – h), the method is derived step by step through general calculations (without numerical values!). Subsequently, the developed method will be applied to concrete numerical values obtained from an actual measurement.  
We neglect layer 2 headers in this task. The packet size therefore refers to a layer 3 PDU. You can also assume that no further communication occurs between the involved nodes.  

a)* Specify the serialization time on the link from i to j as a function of the packet size \( s_1(x) \).  
b) Show or disprove: \( s_1(x) = s_1(x) \).  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
Student ID: 2  
c)* Specify the propagation delay on the link from i to j as a function of the length \( p(l) \) of the physical connection (cable length) between i and j.  
d) Show or disprove: \( p(l) = p(l) \).  
(On the next page, it continues)  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
3 Name:  
Typically, the upstream bandwidth for internet connections does not exceed the achievable downstream bandwidth. We therefore assume that \( r_{ij} \leq r_{ji} \). The following packets are now exchanged:  
1. Node i sends a packet of length \( x_1 \) to node j (e.g., an ICMP Echo Request).  
2. Node j replies to this packet with a packet of the same length \( x_1 \).  
3. After a short pause, node i sends another packet – this time of length \( x_2 > x_1 \).  
4. This is answered by node j with a packet of the original length \( x_1 \).  
Processing times at the nodes themselves can be neglected.  

e)* Draw a time-path diagram of the above-described message exchange. The serialization times and propagation delays should be qualitatively indicated. Ensure complete labeling of the diagram!  
The round-trip time (RTT) between two nodes i and j is defined as the time between sending the first bit of a message and the complete reception of a response – including any processing delays at node j. From the diagram of sub-task e), two such RTTs should be evident, which we will refer to as \( RTT_1 \) (for packets 1 and 2) and \( RTT_2 \) (for packets 3 and 4).  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
Student ID: 4  
f) Mark \( RTT_1 \) and \( RTT_2 \) in your solution from sub-task e).  
g) Specify the round-trip times \( RTT_1 \) and \( RTT_2 \) between i and j as a function of the packet sizes \( x_1 \) and \( x_2 \). Use the results from sub-tasks a), c), and e). Ensure that node j always sends packets of length \( x_1 \)!  
h) Calculate \( \Delta := RTT_2 - RTT_1 \). Simplify the expression as much as possible!  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
5 Name:  
For the following sub-tasks, you need the intermediate result from sub-task h):  
\( \Delta = \frac{x_2 - x_1}{r_{ij}} \).  
The RTT between i and j is now measured three times for two different packet sizes. The results are summarized in Table 1.  

Measurement  
\( x_1 = 48b \) \( x_2 = 1328b \)  
1  
68.62ms 91.47ms  
2  
65.57ms 92.14ms  
3  
65.06ms 93.33ms  
Table 1: RTT Measurements with Different Packet Sizes.  
i)* Why was the RTT measured multiple times for each packet size?  
j)* Determine the upstream bandwidth \( r_{ij} \) from these measurements.  
Note: Use the average of the RTTs from Table 1.  
1 For interest: The measurement was carried out on a T-DSL 3000.  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
Student ID: 6  
Additional space for solutions to Task 1 – please clearly mark the affiliation with the respective sub-task and strike out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
7 Name:  
Task 2 Routing and NAT (20 Points)  
20  
Given the network topology from Figure 2.1. A PC and a notebook (NB) are connected via an Ethernet switch to router R1, which provides access to the internet. The switch is the cheapest model available and has no special capabilities. Since the three devices are connected via a private network, R1 must support NAT.  

PC  
IP  
Subnet  
eth0  
Gateway  
eth0 wan0 wan1 Internet eth0 eth0  
172.16.34.134 87.186.224.45 87.186.224.46 131.159.15.254 131.159.15.49  
255.255.255.248 R1 255.255.255.252 255.255.255.252 R2 R3 255.255.255.0 255.255.255.0  
SRV  
eth0  
IP  
Subnet  
Gateway  
NB  
Figure 2.1: Network Topology  
a)* Complete the binary representation of the subnet mask of the private network in the solution field below. Which part of the subnet mask defines, together with an IP address, the network portion and which defines the host portion?  
11111111 . 11111111 . 11111111 .  
b) How many IP addresses are available in the private network for addressing hosts (including the IP of R1)?  
c) Specify the network and broadcast address for the private network.  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
Student ID: 8  
d) How many such subnets are in the network 172.16.34.0/24?  
e) Assign a sensible combination of IP address, subnet mask, and gateway to both PC and NB. Enter these directly into Figure 2.1.  
Notes:  
f) Which header fields of forwarded frames does the switch change that connects PC, NB, and R1? Indicate the layer to which the changed fields belong if applicable.  
g) Which transport protocol and which destination port number is typical for (unencrypted) HTTP connections?  
In the following, we will abbreviate IP and MAC addresses of known devices according to the schema IP.<Name>.<IF> or MAC.<Name>.<IF>, e.g., IP.R1.eth0 and MAC.R1.WAN0.  
Please also note that there should be two additional routers between R2 and R3, as indicated in the figures.  

h)* Complete the header fields for the request from the PC to the web server SRV in the three empty boxes in Figure 2.2. If a field is not clearly defined, make a sensible choice.  
Note: If you could not solve sub-task g), assume destination port 80.  
i) Complete the header fields for the response from the web server SRV to the PC in the three empty boxes in Figure 2.3. If a field is not clearly defined, make a sensible choice.  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
9 Name:  
V  
R  
S  
090  
eth15.4255.  
9.5.  
55  
12  
1.5.  
35  
12  
CC  
AA rtrt 540  
SrcMDstMSrcIPDstIPSrcPoDstPoTTL 59.15.255.255.  
12  
eth0131.255.  
3  
R  
)  
h  
3  
e  
t b  
e a  
n g  
r uf  
e A  
t  
n u  
I z  
k  
c  
u  
r  
d  
r  
o  
V  
CC 2 2:  
AA rtrt R 2.  
SrcMDstMSrcIPDstIPSrcPoDstPoTTL wan124.465.252 bildung  
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
22  
6.255.  
082  
wan87.1255.  
1  
R  
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
eth15.4255.  
9.5.  
55  
12  
1.5.  
35  
12  
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
ild  
u t  
n e  
g n  
2 r  
.3 e  
:V nt  
o I  
r  
d  
r  
u  
c  
k  
z  
u  
A CC 2  
Task 3 i) SrcMADstMASrcIPDstIPSrcPortDstPortTTL wan1224.4655.252R  
86.5.2  
15  
87.5.2  
5  
2  
2  
5  
52  
4.455.  
22  
6.255.  
082  
wan87.1255.  
1  
R  
048  
h34  
CC et4.15.2  
SrcMADstMASrcIPDstIPSrcPortDstPortTTL 172.16.3255.255.25  
C B  
P h0 h0 N  
et et  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
11 Name:  
In contrast to the lecture, R1 stores not only the triple consisting of local IP and local and global source port, but also the used protocol as well as destination port and destination IP. Table 2 shows an example of how such a NAT table might have looked before sub-tasks h) and i).  

Protocol Local IP Local Port Global IP Global Port Destination IP Destination Port  
TCP IP.PC 50034 IP.R1.wan0 50034 83.133.105.60 22  
TCP IP.PC 49985 IP.R1.wan0 49985 213.165.65.50 443  
Table 2: NAT Table of R1 before sub-task h)  
j) Specify the entries according to Table 2 that were created by the connection establishment from the PC to the web server in sub-tasks h) and i).  

Protocol Local IP Local Port Global IP Global Port Destination IP Destination Port  
k) Now assume that the notebook NB also wants to establish a connection to this web server. Coincidentally, NB chooses the same source port as the PC. Provide valid entries in the NAT table that arise from the connection establishment of the notebook to the web server.  

Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
Student ID: 12  
Task 3 Transport Protocols (23 Points)  
23  
Two computers PC1 and PC2 communicate with each other over the internet. In this task, we will examine a TCP connection between these two computers:  
• the connection establishment,  
• an exemplary message exchange,  
• the behavior in case of message loss, and  
• the connection teardown.  
We assume that a very simple chat application runs on PC1 and PC2, which uses TCP as the transport protocol. PC2 is to act as the server. When the application is started on PC1, it establishes a connection to PC2. Subsequently, bidirectional communication is possible until one of the two sides tears down the connection.  

a)* What information does the chat application on PC1 need to successfully establish a connection to PC2?  
b)* What information do PC1 and PC2 exchange during the connection establishment?  
c) Are the chat application or the operating systems of the PCs responsible for exchanging the information from sub-task b)? (Justification)  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
13 Name:  
In the following, several time-path diagrams are to be created that represent the message exchange between PC1 and PC2:  
• You can neglect serialization time and propagation delay.  
• Note the sequence number above each exchanged message, e.g., SEQ=N.  
• If the ACK flag is set, additionally note the acknowledgment number, e.g., ACK=N.  
• Other flags (SYN, FIN, PSH) should only be indicated if they are set.  

d) Sketch a simplified time-path diagram for the connection establishment.  
Between PC1 and PC2, the following chat messages are exchanged:  
→  
1. PC1: “The great thing about TCP jokes is that you always get them.”  
PC2  
→  
2. PC2: “Nerd!”  
PC1  
We assume that the messages are transmitted in ASCII encoding.  

e) How long will the TCP segments be with which the two messages are exchanged?  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
Student ID: 14  
f) Now draw another time-path diagram that represents the exchange of the two messages. Consider that the user at PC2 needs a few seconds to input their message.  
g) Briefly describe what happens if the acknowledgment for the second message (i.e., the one from PC2 to PC1) is lost.  
h) How can PC1 distinguish a repeated message from a new message?  
i) What happens if a message is recognized as a duplicate?  
j) Immediately after the exchange of the above messages, PC2 initiates the connection teardown. Sketch the connection teardown as a time-path diagram.  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
Student ID: 16  
Additional space for solutions to Task 3 – please clearly mark the affiliation with the respective sub-task and strike out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
17 Name:  
Task 4 Domain Name System (12 Points)  
12  
In this task, the Domain Name System (DNS) is to be examined. Table 3 lists fully qualified domain names of some hosts and DNS servers.  

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
• dns1.lrz.de: Zone tum.de. and all subzones  
• bitsy.mit.edu: Zone mit.edu. and all subzones  

a)* What is the purpose of DNS?  
b)* Name the individual components that make up the fully qualified name www.in.tum.de.  
c)* Create a tree from the fully qualified names in Table 3, starting at the root “.” of the namespace. All names belonging to the same domain should be on the same level in the tree.  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
19 Name:  
We assume that all DNS caches are empty. The computer slacky.net.in.tum.de uses the DNS server dns1.lrz.de for name resolution. We assume that it accepts recursive queries from clients and resolves names iteratively.  

d) In your solution to sub-task c), draw all DNS messages that are exchanged when the command is executed on slacky.net.in.tum.de. Number the messages according to their chronological order. Further details are not necessary.  
Notes:  
e) Can slacky.net.in.tum.de resolve the name luise.nws.ei.tum.de if the root server ns.internic.net fails?  
f) Can slacky.net.in.tum.de resolve the name www.econ.mit.edu if the root server ns.internic.net fails?  
Since DNS operates hierarchically, multiple messages may need to be sent to resolve a name. For the following two sub-tasks, assume that a single request (between client and server or between two arbitrary servers) takes 100ms and that there is a separate authoritative name server for each zone.  

g)* How long does it take slacky.net.in.tum.de at a minimum to resolve the name www.google.com?  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
Student ID: 20  
Task 5 Short Questions (10 Points)  
10  
The following short questions are independent of each other. Bullet-point answers are sufficient!  

a)* You receive the binary message 1011101101. The generator polynomial is \( g(x) = x^2 + 1 \). Check whether an error occurred during transmission.  
b)* Briefly describe (2-3 bullet points are sufficient) how the traceroute program works.  
c)* Why can problems with ICMP messages occur when using NATs?  
Note: Think about how a NAT can assign incoming ICMP messages to a private IP address.  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
21 Name:  
d)* Justify or refute the claim that using token-passing as an access protocol results in largely deterministic transmission times in the local network.  
e)* Justify (argumentatively or through calculation) whether the time signal \( s(t) \) depicted below has a DC component.  
\( s(t) \)  
A  
− − − t  
3T 2T T T 2T 3T  
−  
A  
Note: The signal can be represented as a Fourier series, i.e.,  
\[
s(t) = a_0 + \sum_{k=1}^{\infty} (a_k \cos(k\omega t) + b_k \sin(k\omega t)).
\]  
with the coefficients  
\[
a_k = \frac{1}{T} \int_0^T s(t) \cos(k\omega t) dt, \quad b_k = \frac{1}{T} \int_0^T s(t) \sin(k\omega t) dt.
\]  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
Student ID: 22  
Additional space for solutions – please clearly mark the affiliation with the respective task and strike out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011  
23 Name:  
Fundamentals of Computer Networks and Distributed Systems – WiSe 2011