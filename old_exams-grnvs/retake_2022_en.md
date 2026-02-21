Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be analyzed during attendance control by affixing a code persona sticker.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID here.
- This will be used as a pseudonym to allow a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Retake  
Date: Friday, October 7, 2022  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 10:45–12:15  

Before we proceed with reading the processing instructions, please answer the following questions. This information helps us to examine the learning success depending on individual lecture components. The information is voluntary and does not influence the grading. To exclude any influence, this page will not be accessible during the correction.

a) Did you attend the lecture?  
1 (always) 2 3 4 5 (never)  

b) Did you watch the recording from last year?  
1 (always) 2 3 4 5 (never)  

c) Did you attend the tutorial exercises?  
1 (always) 2 3 4 5 (never)  

d) Did you participate in the review session?  
1 (always) 2 3 4 5 (never)  

e) Did you watch the recording of the review session?  
1 (always) 2 3 4 5 (never)  

### Processing Instructions
- This exam comprises 16 pages with a total of 7 tasks and a formula collection (cheatsheet). Please check now that you have received a complete set.
- The total score for this exam is 90 points.
- It is prohibited to tear pages from the exam.
- The following aids are permitted:  
  - a non-programmable calculator  
  - an analog dictionary German ↔ native language without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only those results will be graded where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-tasks.
- Please do not write with red/green colors or with pencil.
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.

### Task 1  
Multiple Choice (18 points)  
The following tasks are multiple choice/multiple answer, meaning there is at least one correct answer option for each. Sub-tasks are graded with 1 point for each correct answer and -1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.

×  
Mark the correct answers  
■  
Marks can be crossed out by completely filling them in  
×■  
Crossed-out answers can be marked again by adjacent markings  

a)* Based on the Autonomous Systems (AS) in Figure 1.1, which routes will Vodafone communicate to Orange via the peering connection?  
1 AS7018 (AT&T)  
2 AS3209 (Vodafone)  
3 AS5511 (Orange)  

b)* Does Vodafone pass the route to Orange's customers to AT&T? Please give only the most likely answer.  
Yes, as defined in BGP.  
No, to avoid load on its own network.  
Yes, to earn more money from its customers.  
No, Vodafone does not know the customers at all.  
No, as defined in BGP.  
Yes, to better distribute the load on the Internet.  

c)* Which of the following addresses will be globally routed?  
::1  
10.11.12.13  
fec0::1  
128.0.0.1  
fea0::1  
127.8.9.10  

d)* The path MTU is 1500 B. IPv4 is used at layer 3. How large should the MSS be chosen if no TCP options are used?  
1500 B  
1452 B  
1540 B  
1520 B  
1480 B  
1460 B  

e)* Given a line code that encodes 3 bits per symbol. A data rate of 10 Mbit/s should be achieved. Determine the minimal necessary bandwidth under the given conditions.  
1.33 MHz  
0.67 MHz  
0.33 MHz  
3.33 MHz  
1.67 MHz  

f)* What is meant by channel coding?  
None of these  
Targeted addition of redundancy  
Removal of redundancy  
Representation of data by sequences of sending base impulses  

g)* Let n be the length of the checksum, i.e., n = grad(r(x)), with n > 1. Which of the following errors will always and reliably be recognized, regardless of the specific choice of the reduction polynomial?  
Errors consisting of multiple bursts  
Burst errors longer than n  
Isolated 2-bit errors  
1-bit errors  
Burst errors shorter than n  
Errors that are multiples of the reduction polynomial  

h)* With which of the following addressing types can there be more than one recipient?  
Broadcast  
Unicast  
Anycast  
Multicast  

i)* There are 30 hosts in an IPv4-based network. Which subnet mask describes the smallest possible subnet so that all hosts can be assigned an IPv4 address?  
255.255.255.248  
255.255.255.224  
255.255.255.254  
255.255.255.240  
255.255.255.192  
255.255.255.252  

j)* Which of the following properties apply to link-state routing protocols?  
The operating principle is similar to Dijkstra's algorithm.  
Routers exchange only cumulative costs among themselves.  
Routers determine a minimal spanning tree from the exchanged information.  
Routers have no information about network topology.  
Routers regularly exchange status messages.  
The operating principle is similar to Bellman-Ford's algorithm.  

k)* You want to compress the following data stream and use a Huffman code for it. Which character has the lowest depth in the corresponding Huffman tree?  
DADCCBDBCD  
A B C D  

l)* Given the time signal s(t) with s(t) = 1.5·cos(4ωt) + 3, where ω = 2π, T = 1s. Which of the following statements about the coefficients of the corresponding Fourier series is/are true?  
a = 4  
b = 4  
a = 1.5  
a = 1.5  
a = 4  
b = 1.5  
0  
0  
4  
0  
3  
4  
a = 3  
b = 6  
a = 6  
b = 1.5  
a = 1.5  
b = 4  
0  
0  
0  
3  
3  
3  

### Task 2  
Short Tasks (4.5 points)  
a)* Given the IPv4 address 203.0.113.4. Provide the corresponding FQDN of the PTR record.  

b)* Given the IPv4 subnet 192.168.240.15/20. Justify why this subnet cannot be combined with the subnet 192.168.223.15/20 into a /19 supernet.  

c)* Given the IPv4 subnet 192.168.240.15/20. With which other /20 network can this be combined into a /19 supernet?  

d)* Given the IPv6 address 2001:0db8:0000:0000:0110:0000:0000:0123. Provide the address in the usual fully shortened form.  

### Task 3  
Frequency Analysis (16.5 points)  
Given the sending pulse shown in Figure 3.1.  
a)* What is this sending pulse commonly called? (no justification)  

b)* How is a logical 0 or 1 encoded using this pulse? (Justification or sketch)  

c)* Briefly describe one advantage of this pulse.  

d)* Briefly describe one disadvantage of this pulse.  

In the following, the frequency behavior of this sending pulse should be investigated.  
e)* Justify whether a Fourier transformation or a Fourier series is used here.  

f)* Provide an analytical expression for the sending pulse shown in Figure 3.1.  

g)* Why might it be useful to provide the spectrum of a sending pulse as a magnitude?  

h)* Determine the spectrum. Simplify the result as much as possible.  

### Task 4  
The Clacks (14.5 points)  
The Clacks are a network of towers in Terry Pratchett's Discworld. They form one of the first telecommunications networks and are described as: Three stories high, built of wood, and look as if they were hastily assembled, probably because they were. An inner lantern even allows transmission at night.  

A message is transmitted by displaying individual symbols through targeted opening and closing of the 2×4 flaps (see Figure 4.1), which are observed by employees on a tower 12 km away and may be forwarded from there. It takes 5 seconds to deliver a symbol.  

a)* How many bits can be transmitted with each symbol? The calculation must be recognizable.  

b)* Calculate the information content of any symbol under the assumption that all symbols have the same probability of occurrence.  

c)* Determine the achievable data rate in B/s.  

d)* The patrician of Ankh-Morpork wants to send a 47-character message to his neighboring state. Messages are ASCII encoded and terminated with NUL. The Clacks use an additional (unused from ASCII) bit per symbol for error detection. How many bytes does the message require?  

e)* Calculate the serialization time in the case of message transmission.  

f)* The original design of the Clacks included only 2×3 flaps. What else could the additional 2 flaps have been used for, besides simply representing more symbols? Justify.  

In the following, we want to determine the transmission time if packet switching is used instead of message switching. We assume that each packet consists of 10 B of payload. A 2 B long header is added to each packet.  

g)* Calculate the number of packets required.  

To reach the destination, the message must pass 5 Clacks (including start and destination). Their distance is 12 km each. There are no confirmations, but a packet is read completely before it is forwarded.  

h)* How long does it take until the message reaches its destination?  

i)* Explain the advantage of packet switching over message switching.  

j)* Explain the advantage of packet switching over circuit switching.  

### Task 5  
DNS (7 points)  
You are the system administrator of a small company that has secured the domain grnvs.tips. Your task is to fill out the following zone file so that the requirements of the individual sub-tasks are met. The beginning of the zone file is already provided.  

```
$TTL 86400 ; 1 day  
dns.lrz.eu. IN SOA ns.grnvs.tips. (  
hostmaster.grnvs.tips.  
164160 ; serial  
1800 ; refresh (30 minutes)  
300 ; retry (5 minutes)  
604800 ; expire (1 week)  
1800 ; nxdomain (30 minutes)  
)  
NS dns.lrz.eu.  
grnvs.tips. MX 10 mail.grnvs.tips.  
```

a)* When someone calls grnvs.tips in their browser, their website should be displayed. Your web server has the IP addresses 134.102.13.9 and 2001:db8::2.  

b)* To enable employees to collaborate better, two services, calendar and contacts, should be set up as subdomains. Both run on the server with the address 2005:db1::affe.  

c)* You do not want to operate your own mail server and have booked the mail service from adzone.com. For this, all incoming mails must be sent to the IP address of mail.adzone.com. Since you might want to change this in the future, the maximum validity of this entry should be 90 minutes.  

d)* To prove to the provider of adzone.com that you really own the domain grnvs.tips, the text secret123 should be stored under challenge.grnvs.tips.  

### Task 6  
Dormitory Network Goes Internet (15.5 points)  
Given is a student dormitory with several buildings, whose network is built over Ethernet and IPv4. Each household has its own private /24 prefix. The house network for house x is described by the prefix 10.0.x.0/24. All residents of a house are connected to each other via a switch, which is connected to the respective gateway of the house. These routers are interconnected via the transport network 10.0.255.0/24. A snippet of the network is shown in Figure 6.1.  

The dormitory has been assigned the public IP address 203.0.113.23. For the mapping between public and private IP addresses, the NAT-capable router has a mapping table that stores the relationship between local and global ports, as well as the IP addresses of the internal hosts. The NAT router is connected to the "Internet." This is represented as a cloud and has an unspecified number of hops between R and R.  

a)* Name two possibilities to assign IP addresses to the hosts/residents.  

b) What additional possibility of assignment is there in IPv6?  

c)* Why must there be a NAT-capable router?  

d) What advantage does this architecture provide with NAT?  

e)* How many entries can the mapping table of the NAT router have for TCP at most?  

A resident now wants to access the website with the URL https://grnvs.net and knows its IP address 198.41.0.4.  

f)* To which TCP port will the request likely be addressed? (no justification)  

g)* Which HTTP method will likely be used? (no justification)  

h) We consider the sending of the requests. Provide the corresponding header fields in the table at the points marked P1 to P6 in the graphic. Use the following notation: MAC(k.iface) for the MAC address of the interface iface of node k, e.g., MAC(R7.eth9) for the MAC address assigned to the interface eth9 at router R7; similarly, IP(k.iface) for the IP address. You can abbreviate residents with R. The ports should be given as numbers.  

| SRC-MAC | DST-MAC | SRC-IP | DST-IP | SRC-PORT | DST-PORT |  
|---------|---------|--------|--------|----------|----------|  
| P1      |         |        |        |          |          |  
| P2      |         |        |        |          |          |  
| P3      |         |        |        |          |          |  
| P4      |         |        |        |          |          |  
| P5      |         |        |        |          |          |  
| P6      |         |        |        |          |          |  

i)* Now assume that the host is unreachable due to connection problems and router R sends an ICMP error message back. Will this arrive at resident R? Justify.  

j)* In house 2, a resident operates their own server (Server Z). A client from outside the dormitory wants to reach this web server in house 2. Justify why this is not possible.  

k) How can this problem be circumvented?  

### Task 7  
Congestion in the Flow (14 points)  
In this task, we consider the effects of disturbances in the network on the transport layer. A simplified form of TCP Reno is considered, as presented in the lecture.  

a)* Explain the goal of congestion control in TCP and its implementation.  

b)* Explain the goal of flow control in TCP and its implementation.  

We now consider a sequence of events and how they affect the size of the receive window. In the diagram below, the window size w is given in multiples of the MSS, and the time c is given in multiples of the RTT between the communicating hosts.  

```
wc/MSS
20
18
16
14
12
10
8
6
4
2
0 t/RTT
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28
```

It holds that w(0) = 1. We assume that the bandwidth on the path in the network is a maximum of 15 MSS/RTT. Initially, there are no timeouts.  

c)* Draw the course of w_c for t < 18 RTT and justify.  

d) Ignoring the beginning, with what effective transmission rate can communication take place if no other disturbances occur? Provide the result as a function of the MSS.  

At t = 18 RTT, a timeout occurs.  

e)* What could be a cause for this?  

f) After that, there are no further disturbances. Complete the diagram until t ≤ 28 RTT and justify.  

g)* What problem arises with an unreliability from layer 1 to 3 when using TCP?  

### Additional Template for Task 7:
```
wc/MSS
20
18
16
14
12
10
8
6
4
2
0 t/RTT
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28
```
Additional space for solutions. Clearly mark the assignment to each sub-task.  
Do not forget to cross out invalid solutions.