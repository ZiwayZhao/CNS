Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

Confirmation of Conduct Rules  
I hereby assure that I will solve this exam exclusively using the resources listed below and submit it under my name.  
Sticker will be generated  
Signature or full name, if no pen input is available  

Basics: Computer Networks and Distributed Systems  
Exam: IN0010/Quiz4 Date: Thursday, July 10, 2025  
Examiner: Prof. Dr.-Ing. Georg Carle Time: 19:00–19:15  

Instructions for Completion  
- This exam consists of 4 pages with a total of 3 tasks.  
- Please check now that you have received a complete set of information.  
- The total score for this exam is 15 points.  
- The tearing out of pages from the exam is prohibited.  
- The following resources are permitted:  
  - everything except group work, plagiarism, and any form of AI (e.g., ChatGPT)  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  

Multiple Choice Tasks  
The following tasks are Multiple Choice/Multiple Answer, meaning at least one answer option is correct.  
Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 1 point per correct answer and 1 point per incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

Please mark the correct answers  
Marks can be crossed out by complete filling  
Crossed-out answers can be marked again by adjacent markings  

--- Page 1/4 ---  

Task 1  
Static Routing (4 points)  
Given is the following routing table of a router.  

| Entry | Destination      | Next-Hop        | Interface |
|-------|------------------|------------------|-----------|
| 1     | 10.4.32.0/22     | 0.0.0.0          | eth0      |
| 2     | 10.4.36.0/22     | 10.4.35.255      | eth0      |
| 3     | 10.4.40.0/22     | 0.0.0.0          | eth1      |
| 4     | 10.4.0.0/17      | 10.4.35.255      | eth0      |
| 5     | 0.0.0.0/0        | 10.4.43.255      | eth1      |

a) Which entry will be chosen for forwarding when the router receives a packet with the destination IP address 10.15.3.7?  
- Entry 4  
- Entry 2  
- Entry 3  
- Entry 1  
- None  
- Entry 5  

b) Which entry will be chosen for forwarding when the router receives a packet with the destination IP address 10.4.34.7?  
- Entry 4  
- Entry 1  
- Entry 3  
- Entry 2  
- None  
- Entry 5  

c) Which entry will be chosen for forwarding when the router receives a packet with the destination IP address 10.4.119.103?  
- Entry 5  
- Entry 4  
- Entry 3  
- Entry 2  
- Entry 1  
- None  

d) Which entry of the routing table can be omitted without changing the routing of packets?  
- Entry 4  
- Entry 5  
- Entry 2  
- Entry 1  
- None  
- Entry 3  

--- Page 2/4 ---  

Task 2  
Dynamic Routing (2 points)  
Given is the following topology of routers. At router Z, the respective subnet/prefix z hangs, for example, the subnet with prefix a is reachable via router A. The various routers determine their routing tables based on an optimal dynamic routing protocol. The costs are indicated on the respective edges.  

a) We consider the routing table of router A: Which router will be entered as the next hop for prefix d?  
- D  
- C  
- B  
- A  
- None  
- E  

b) We consider the routing table of router E: Which router will be entered as the next hop for prefix b?  
- E  
- None  
- A  
- C  
- B  
- D  

--- Page 3/4 ---  

Task 3  
Misc (9 points)  
a) Which of the following mechanisms is not a mechanism for configuring IPv4 addresses?  
- Automatic Private IP Addressing  
- Dynamic Host Configuration Protocol  
- Manual Configuration  
- Stateless Address Autoconfiguration  

b) Which parameters can or must be negotiated in TLS 1.3 between client and server?  
- The Chain of Trust  
- The Private Key  
- TLS Version  
- Supported Groups  

c) How does a router proceed when it has no suitable entry in its routing table for the destination IP address of a packet?  
- Send the packet back to the sender  
- Send an ICMP error message to the sender  
- Forward using the last entry of the routing table  
- Discard the packet  

d) A PC sends an IP packet to the destination address ff02::1 (LL All-Nodes Multicast IPv6). What values can the Destination MAC Address field in the Ethernet header take?  
- 33:33:fe:00:00:01  
- 33:33:ff:02:00:01  
- ff:02:00:00:00:01  
- ff:ff:ff:02:00:01  
- 00:00:00:00:00:00  
- 33:33:00:00:00:01  

e) What is the PTR record for the IPv6 address 2001:db8::7756?  
- 2.0.0.1.0.d.b.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.7.7.5.6.ip6.arpa.  
- 6577.0000.0000.0000.0000.8bd0.1002.ip6.arpa.  
- 2001.0db8.0000.0000.0000.0000.7756.ip6.arpa.  
- 6.5s.7.7.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa.  

f) How many PTR records must be created to enable a reverse lookup of all IP addresses in the network 131.159.32.0/23?  
- 256  
- 9  
- 2048  
- 512  
- 65536  
- 1024  

g) How many zones must be created under the zones 131 and 159 to enable a reverse lookup of all IP addresses in the network 131.159.32.0/23?  
- 4  
- 8  
- 0  
- 512  
- 2  
- 256  

--- Page 4/4 ---