Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

Confirmation of Code of Conduct  
I hereby assure that I will solve this exam exclusively using the resources listed below and submit it under my name.  
Sticker will be generated  
Signature or full name if no pen input is available  

Basics of Computer Networks and Distributed Systems  
Exam: IN0010/Quiz4 Date: Thursday, June 27, 2024  
Examiner: Prof. Dr.-Ing. Georg Carle Time: 19:00–19:15  

Do not forget to confirm the code of conduct (see above) by signing or entering your name (if no pen input is available). Submissions without confirmation will not be graded.  

Instructions for Processing  
- This exam consists of 6 pages with a total of 2 tasks. Please check now that you have received a complete set of information.  
- The total score for this exam is 16 points.  
- It is prohibited to tear pages out of the exam.  
- The following resources are allowed:  
  - everything except group work, plagiarism, and any form of AI (e.g., ChatGPT)  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Always answer open-ended questions in your own words. Foreign or copied answers will not be accepted.  
- Violations of the code of conduct will lead to exclusion from the bonus procedure.  
- Do not write with red/green colors or with a pencil.  

---  
**Task 1**  
Multiple Choice (11 points)  
The following tasks are multiple choice/multiple answer, meaning at least one answer option is correct.  
Sub-tasks with only one correct answer will be awarded 1 point if correct. Sub-tasks with more than one correct answer will be awarded 1 point for each correct and 1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

Mark the correct answers  
- Marks can be crossed out by complete filling.  
- Crossed out answers can be marked again by adjacent markings.  

a) *Which of the following addresses is/are a correct valid representation(s) of the IPv6 address 2001:0100:f8e:0000:0:090:0000:0000?  
- 2001:0100:f8e:0000:0:090:0000:0000  
- 2001:100:f8e::0:090::  
- 2001:100:0f8e:0:0:0:0:0000  
- 2001:0100:0f8e:0000:0000:0090:0000:0000  
- 2001:0100:f8e:0000:0:090:0000:0000  
- 2001.0100.0f8e.0000.0000.0090.0000.0000  
- 2001:100:f8e::90:0:0  

b) *Which of the following addresses is/are a correct compact/shortened representation(s) of the IPv6 address 2001:0db8:11ab:0000:0000:0070:0000:0000?  
- 2001:db8:11ab::70::  
- 21:db8:11ab:::7::  
- 2001:db8:11ab:0:0:70::  
- 2001:db8:11ab:0:0:070:0:0  
- 2001:db8:11ab::70:0:0  
- 2001:db8:11ab:0000:0:070:0000:0000  

c) *A PC sent an IP packet to the destination address ff02::1 (LL All-Nodes Multicast IPv6). What values can the Destination MAC Address field in the Ethernet header take?  
- 33:33:ff:00:00:01  
- 33:33:08:15:01:01  
- 08:15:08:15:01:01  
- 33:33:00:00:00:01  

```
PC2
Internet
R1
PC3
PC1
S1 S2
```
Figure 1.1: Network Topology  

d) *In Figure 1.1, a network topology is depicted. Assuming PC1 is the sender of the IP packet to the destination address ff02::1 (LL All-Nodes Multicast IPv6), which device(s) receive the packet?  
- PC3  
- R1  
- S1  
- none  
- PC2  
- S2  

e) *What value is in the Next Header field of the IPv6 header of its UDP datagram if there are no extension headers?  
- 59  
- 0x3b  
- 0x3a  
- 0x2c  
- (10)  
- 58  
- 17  
- 44  
- 0x06  
- (10) (10) (10)  

**Table 1.1: Routing Tables**  
(a) Routing Table A  
(b) Routing Table B  

| Entry | Destination      | Next-Hop    | Iface | Entry | Destination      | Next-Hop    | Iface |
|-------|------------------|--------------|-------|-------|------------------|--------------|-------|
| 1     | 10.0.0.0/24      | 0.0.0.0      | eth1  | 5     | 172.0.0.0/28     | 0.0.0.0      | eth1  |
| 2     | 192.168.55.0/24  | 0.0.0.0      | eth2  | 6     | 192.168.128.0/25 | 0.0.0.0      | eth2  |
| 3     | 192.168.128.0/17 | 0.0.0.0      | eth3  | 7     | 192.168.0.0/17   | 0.0.0.0      | eth3  |
| 4     | 0.0.0.0/0       | 72.168.2.2    | eth0  |       |                  |              |       |

f) A router receives an IP packet for 192.168.192.77. Which entry does the router choose for forwarding this IP packet when Routing Table A (Table 1.1a) is used?  
- 1  
- 2  
- 3  
- 4  
- none  
- all  

g) A router receives an IP packet for 192.168.129.95. Which entry does the router choose for forwarding this IP packet when Routing Table B (Table 1.1b) is used?  
- 5  
- 6  
- 7  
- none  
- all  

---  
**Task 2**  
Short Tasks (5 points)  

a) *What is the function and purpose of Hop Limits in IPv6?  
- 0  
- 1  
- 2  

b) *What is the equivalent in IPv4? (no justification)  
- 0  
- 1  

c) *Where can fragmentation and reassembly of IP packets occur in IPv4 and IPv6? (no justification)  
- 0  
- 1  
- 2  
- IPv4  
- IPv6  
- Fragmentation  
- Reassembly  

---  
Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.  
---  
---