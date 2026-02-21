Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

Confirmation of Conduct Rules  
I hereby assure that I will solve this exam exclusively using the resources listed below and submit it under my name.  
Sticker will be generated  
Signature or full name, if no pen input is available  

Basics of Computer Networks and Distributed Systems  
Exam: IN0010/Quiz5 Date: Friday, July 12, 2024  
Examiner: Prof. Dr.-Ing. Georg Carle Time: 19:00–19:15  

Do not forget to confirm the conduct rules (see above) by signing or entering your name (if no pen input is available). Submissions without confirmation will not be graded.  

Instructions  
- This exam consists of 4 pages with a total of 1 task. Please check now that you have received a complete set of information.  
- The total score for this exam is 15 points.  
- It is prohibited to tear pages from the exam.  
- The following aids are permitted:  
  - everything except group work, plagiarism, and any form of AI (e.g., ChatGPT)  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Always answer free-text tasks in your own words. Foreign or copied answers will not be accepted.  
- Violations of the conduct rules will lead to exclusion from the bonus procedure.  
- Do not write with red/green colors or with a pencil.  

---  

Task 1  
HTTPS GET (Multiple Choice) (15 points)  
The following tasks are multiple choice/multiple answer, meaning that at least one answer option is correct for each.  
Sub-tasks with only one correct answer will be graded with 1 point if correct. Sub-tasks with more than one correct answer will be graded with 1 point for each correct answer and 1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

Please mark the correct answers.  
Marks can be crossed out by complete filling.  
Crossed-out answers can be marked with adjacent markers.  

Given is the topology drawn in Figure 1.1. We consider a packet of an HTTPS (v1.1) GET request from PC1 to SRV.  
PC1 has a private IPv4 address, SRV has a global one. R1 has NAT capability, the NAT table is given in Table 1.1a. Some header fields of the packet when sent from PC1 are (partially) given in Table 1.1b.  
Addresses are specified in the format Device.[Interface.]Address.  
Header fields in the format: Layer/Protocol.Field  

```
Home Network
R1
eth0 eth1
(NAT)
PC1
SRV
P1 P2 P3
Internet
S1
eth0 eth1
```
Figure 1.1: Topology  

| Field          | Value          |
|----------------|----------------|
| L2.SrcAdr      | PC1.MAC       |
| L2.DstAdr      | 1              |
| L2.EtherType   | 0x0800        |
| Local Port     | Global Port    | Local IP  | L3.SrcAdr     | 10.0.0.1     |
| L3.DstAdr      | 2              |
|                | 1234          | 5678       | 10.0.0.2     |
| L3.TTL         | 64             |
|                | 1235          | 1235       | 10.0.0.1     |
| L3.Protocol     | 3              |
|                | 1235          | 5679       | 10.0.0.2     |
|                | 5678          | 1236       | 10.0.0.1     |
| L4.SrcPort     | 1235          |
|                | 5679          | 1234       | 10.0.0.3     |
| L4.DstPort     | 4              |

(a) NAT Table R1 (b) Packet  
Table 1.1  

---  

Complete the missing header fields as they will be set by PC1 when sending the packet.  
a) *What values are valid for 1 when sending the packet from PC1?  
PC1.MAC, S1.eth1.MAC, R1.eth1.MAC,  
S1.eth0.MAC, R1.eth0.MAC, SRV.MAC  

b) *What values are valid for 2 when sending the packet from PC1?  
PC1.IP, S1.eth1.IP, R1.eth1.IP,  
S1.eth0.IP, R1.eth0.IP, SRV.IP  

c) *What values are valid for 3 when sending the packet from PC1?  
0x06, 0x11, 0x443, 443, 0x86dd, 0x8000, 10  

d) *What values are common for 4 when sending the packet from PC1?  
443, 80, 1023, 1024, 1235, 65535  

We now consider the processing of the packet at different points (P1, P2, P3) in the network.  
e) *Which of the header fields considered here change between P1 and P2?  
L2.SrcAddr, L3.SrcAddr, L3.TTL, L4.SrcPort, none,  
L2.DstAddr, L3.DstAddr, L3.Protocol, L4.DstPort, all  

f) *Which of the considered header fields change between P2 and P3?  
L2.SrcAddr, L3.SrcAddr, L3.TTL, L4.SrcPort, none,  
L2.DstAddr, L3.DnstAddr, L3.Protocol, L4.DstPort, all  

To conclude, we briefly consider the protocols associated with an HTTPS (v1.1) connection.  
g) *Which protocol is normally used over the transport layer for an HTTPS (1.1) request?  
TCP, TLS, SSH, POP3,  
UDP, ARP, SMTP, NAT  

h) *Which statement(s) about TCP flow control are correct?  
avoids congestion in the network, avoids congestion at the sender,  
avoids congestion at the receiver, shares the sending window with,  
adjusts the sending window, shares the receiving window with  

i) *Which statement(s) about TCP congestion control are correct?  
avoids congestion in the network, avoids congestion at the sender,  
avoids congestion at the receiver, shares the sending window with,  
adjusts the sending window, shares the receiving window with  

---  

Additional space for solutions. Clearly mark the assignment to each sub-task.  
Do not forget to cross out invalid solutions.