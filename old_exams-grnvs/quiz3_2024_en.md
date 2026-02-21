Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

Confirmation of Behavioral Rules  
I hereby assure that I will solve this exam exclusively using the resources listed below and submit it under my name.  
Sticker will be generated  
Signature or full name if no pen input is available  

Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Quiz3 Date: Monday, June 17, 2024  
Examiner: Prof. Dr.-Ing. Georg Carle Time: 19:00–19:15  

Do not forget to confirm the behavioral rules (see above) by signing or entering your name (if no pen input is available). Submissions without confirmation will not be graded.  

Instructions for Processing  
- This exam consists of 4 pages with a total of 2 tasks. Please check now that you have received a complete set of information.  
- The total score for this exam is 15 points.  
- It is prohibited to tear pages from the exam.  
- The following resources are permitted:  
  - everything except group work, plagiarism, and any form of AI (e.g., ChatGPT)  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Always answer free-text questions in your own words. Foreign or copied answers will not be accepted.  
- Violations of the behavioral rules will lead to exclusion from the bonus procedure.  
- Do not write with red/green colors or with a pencil.  

Multiple Choice Questions  
Some sub-tasks are multiple-choice questions, for which the following applies: These sub-tasks are multiple-choice/multiple answer, meaning at least one answer option is correct. Sub-tasks with only one correct answer will be graded with 1 point if correct. Sub-tasks with more than one correct answer will be graded with 1 point for each correct selection and 1 point for each incorrect selection. Missing selections have no impact. The minimum score per sub-task is 0 points.  

- Mark the correct answers  
- Selections can be crossed out by fully filling them in  
- Crossed-out answers can be marked with adjacent markings  

### Task 1  
Multiple Choice (8 Points)  
a) *Which headers of which protocols can immediately follow an Ethernet header in a frame?  
- ARP  
- IPv6  
- NDP  
- ICMPv4  
- DNS  
- ICMPv6  
- UDP  
- TCP  

b) *An ARP request can have the payload of which of the following protocols?  
- IPv6  
- MAC  
- Ethernet  
- ICMPv6  
- IPv4  
- NDP  
- NDPv4  
- ICMPv4  

c) *A Neighbor Advertisement can have the payload of which of the following protocols?  
- ARP  
- IPv6  
- Ethernet  
- RIP  
- ARP  
- ICMPv4  
- MAC  
- IPv4  

d) *What property(ies) does IPv6 have compared to IPv4?  
- No routing needed  
- Fragmentation also possible in routers  
- Coding rate of 6/4  
- Fixed header size  
- Improved line coding  
- 128 times larger address space  

e) *Which of the following IP addresses will not be globally routed?  
- 8.8.8.8  
- 2001::abcd:1  
- 192.192.1.1  
- 2001::1:0:13  
- 192.169.24.25  
- 127.255.1.2  
- 1.1.1.1  
- 128.128.128.128  

f) *How many collision domains are there in the network in Figure 1.1?  
- 6  
- 2  
- 5  
- 4  
- 0  
- 1  
- 3  
- 7  

g) *How many broadcast domains are there in the network in Figure 1.1?  
- 5  
- 1  
- 4  
- 6  
- 2  
- 3  
- 7  
- 0  

### Task 2  
IP Fragmentation (7 Points)  
In the following network, data is transmitted from PC1 to PC2 using IPv6 and UDP. The MTU in the local networks is 1,500 B each, the MTU on Link A is 1,456 B, and the MTU on Link B is 1,416 B.  

```
PC1 R1 R2 R3 PC2  
eno0 eth0 wan0 wan0 wan1 wan0 eth0 eno0  
Link A Link B  
```

Figure 2.1: Network topology  

a) *What is the maximum size of an L2-SDU sent from PC1 (Path MTU) so that it arrives at PC2?  
- 1,416 B  
- 1,500 B  
- 1,456 B  
- other  
- 2,872 B  
- 5,872 B  

Now we consider the first of two IPv6 fragments at point P on the link between PC1 and R1. Complete the following sub-task with the headers that occur in this fragment. Use the notation Device.Interface.Address for MAC and IP addresses, e.g., PC3.eno0.MAC. Make the number base of the used numerical values clearly recognizable. Choose sensible values for filling in the header fields if they are not defined or not clearly defined in the task statement.  

b) *Complete the Ethernet header of the first fragment.  
```
0  
1  
PC1.eno0.MAC IPv6 Fragment FCS  
```

c) *Complete the IPv6 header of the first fragment.  
```
0  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 1  
6  
Path MTU - 40  
≈ ≈  
PC1.eno0.IP  
≈ ≈  
Fragmentation Extension Header  
```

d) *Complete the IPv6 Fragmentation Extension Header of the first fragment.  
```
0  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 1  
31415  
(10)  
UDP Payload  
```

e) *Which of the following header fields change when considering the second fragment at point P compared to the first fragment in each case?  
- Next Header (IP Header)  
- Fragment Offset  
- Identifier  
- MF Bit  
- Next Header (Ext. Header)  
- Destination Address  
- Hop Limit  
- Reserved  
- Source Address  
- Version  
- DF Bit  
- Checksum (L3)  

### Additional Space for Solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.