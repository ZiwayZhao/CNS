Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  
__ __ __ __ __ __ __ __  
1  
2 Signature  
3  
4  
Notes on Personalization:  
5  
• Mark your student ID. This will be evaluated automatically.  
6  
• Sign in the signature field.  
7  
8 Only a calculator and an analog dictionary in the German native language without annotations are allowed as aids.  
9 × Student ID • Write with red or green ink, or with pencil.  
This quiz contains multiple-choice/multiple-answer sub-tasks, meaning there is at least one correct answer option for each. These sub-tasks will be scored with 1 point for each correct and 1 point for each incorrect mark. Missing marks have no impact. The minimum score per sub-task is 0 points.  
×  
Mark the correct answers  
■  
Marks can be crossed out by fully filling them in.  
×■  
Crossed-out answers can be re-marked by adjacent markings.  
a)* To which layer of the ISO/OSI model is an IPv6 Fragmentation Extension Header assigned?  
Layer 2 Layer 6 Layer 5 Layer 8  
Layer 1 Layer 4 Layer 3 Layer 7  
b)* In which two networks can 192.168.73.0/24 be divided?  
192.168.73.0/26 192.168.73.128/25 192.168.73.64/25 192.168.73.196/26  
192.168.73.196/25 192.168.73.0/25 192.168.73.64/26 192.168.73.128/26  
c)* What is the broadcast address of the network 10.4.8.112/28?  
10.4.8.128 10.4.8.127 10.4.8.119 10.4.8.110  
10.4.8.118 10.4.8.126 10.4.8.111 10.4.8.129  
d)* What is the network address associated with the address 10.54.2.18? The subnet mask is 255.255.0.0.  
10.54.0.0 10.54.2.18 10.0.0.0 10.54.2.0  
e)* Given the 16-bit long data 0xabcd in Little Endian. What representation corresponds to the data in Network Byte Order?  
0xabcd 0xbadc 0xcdab 0xdcda  
f)* What is the fully shortened form of the following IPv6 address according to the lecture?  
2001:4ca0:0000:0000:00e0:0000:0000:000c  
2001:4ca0::e0:0:0:c 2001:4ca0::e0::c  
Other IPv6 address 2001:4ca::e::c  
2001:4ca::e:0:0:c 2001:4ca0::00e0::000c  
2001:4ca0:0:0:e0::c 21:4ca::e:::c  
–Page 1/2–  
g)* What happens to a router when it receives a packet with Time To Live = 1?  
0  
1  
h)* You are administrators of a network and need to provide a subnet that contains the IP address 10.97.211.5 and offers space for at least 15 hosts. Provide the smallest possible subnet in the usual notation that meets these requirements. Also, provide your calculation path.  
1  
In the following network, data is transmitted from the PC to the server using IPv4. The MTU in the local networks is 1,500 B each, and the MTU on the link between the routers is 680 B. The Layer 3 payload is 986 B long. The PC sends all IPv4 packets with an initial TTL of 64 and without IPv4 options.  
PC R1 R2 Server S  
P  
eth0 eth0 wan0 wan0 eth0 eth0  
Figure 1.1: Network topology  
We consider the first of two fragments at point P on the link between R1 and R2. The Ethernet header of this fragment is shown in Figure 1.2 and the IPv4 header of the fragment in Figure 1.3.  
For MAC and IP addresses, we use the notation Device.Interface, e.g., R1.wan0 or S.eth0.  
1 Destination Address Source Address Ethertype L2-Payload FCS  
Figure 1.2: Ethernet header of the first fragment at point P  
i)* Which MAC address from which interface is in the Ethernet header in field 1 Destination Address?  
R1.wan0 R1.eth0 S.eth0 PC.eth0 R2.eth0 R2.wan0  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
Version 2 IHL TOS 3 Total Length  
Identification RES DF MF 4 Fragment Offset  
TTL Protocol Header Checksum  
Source Address  
5 Destination Address  
L3-Payload  
Figure 1.3: IPv4 header of the first fragment at point P  
j)* What value is in the IPv4 header in field 2 IHL?  
24 28 20 5 7 6  
(10) (10) (10) (10) (10) (10)  
k)* What value is in the IPv4 header in field 3 Total Length?  
986 680 966 980 660 676  
(10) (10) (10) (10) (10) (10)  
l)* What value is in the IPv4 header in field 4 Fragment Offset?  
0 120 85 660 82 123 966  
(10) (10) (10) (10) (10) (10) (10)  
m)* The IPv4 address from which interface is in the IPv4 header in field 5 Destination Address?  
PC.eth0 S.eth0 R1.eth0 R2.eth0 R2.wan0 R1.wan0  
–Page 2/2–