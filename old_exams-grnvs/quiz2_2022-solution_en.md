Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

Confirmation of Conduct Rules  
I hereby assure that I will solve this exam exclusively using the resources listed below and submit it under my name.  
Sticker will be generated  
Signature or full name, if no pen input is available  

Basics of Computer Networks and Distributed Systems  
Exam: IN0010/Quiz2 Date: Tuesday, July 5, 2022  
Examiner: Prof. Dr.-Ing. Georg Carle Time: 19:00–19:15  

Instructions for Processing  
- This exam consists of 4 pages with a total of 2 tasks. Please check now that you have received a complete set of information.  
- The total score for this exam is 15 points. These will be normalized according to the point system provided in the bonus system.  
- Detaching pages from the exam is prohibited.  
- The following resources are permitted:  
  - everything except group work and plagiarism  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with a pencil.  
- Turn off all electronic devices completely, store them in your bag, and close it.  

---  
**Task 1**  
Multiple Choice (9 Points)  
The following tasks are Multiple Choice/Multiple Answer, meaning that at least one answer option is correct.  
Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 1 point per correct answer and 1 point per incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

Mark the correct answers  
Correct answers can be crossed out by complete filling  
a) *Which statement(s) apply to the MAC address 33:33:fe:3b:88:3c?  
- Globally unique  
- Unicast  
- Globally administered  
- Locally administered  
- Multicast  
- Broadcast  

b) Given the date 0x5e6b137d in Little Endian. What is the representation in Big Endian?  
- 0x5e6b137d  
- 0xb6e5d731  
- 0xd731b6e5  
- 0x7d136b5e  
- 0xe5b631d7  

c) Which of the following IPv4 addresses can be used as host addresses in the subnet 192.168.255.255/18?  
- 192.168.254.254  
- 192.168.1.1  
- 192.168.186.1  
- 192.168.255.255  
- 192.168.192.25  

d) *You observe a UDP segment with the header from Figure 1.1. What service is the sender likely trying to use?  
0x0000 d0 2c 00 35  
0x0004 00 26 a9 86  
Figure 1.1: Hex dump of a UDP header, in Network Byte Order  
- DHCP  
- HTTP  
- HTTPS  
- SSH  
- DNS  
- FTP  

e) *You observe a UDP datagram with port 80 as the target. Which of the following reactions from the receiver is most likely?  
- A 3-Way Handshake  
- A response via UDP  
- Acknowledgment of the segment  
- A response with an ACK  
- The request is discarded  
- A response via TCP  

f) You have established a TCP connection that is already in the Congestion Avoidance Phase. The current size of the Congestion Window is w = 55 (MSS). You receive 3 duplicate ACKs. What applies next for Lw? Assume TCP Reno as introduced in the lecture.  
- w ≥ 110  
- w < 34  
- It remains the same  
- w ≥ 56  
- w = 18  
- w = 42  

---  
**Task 2**  
Short Tasks (6 Points)  
a) *Given the IPv6 address 2001:0bfa:0000:0001:0000:0000:0000:0001. Provide this in fully 0 compressed notation.  
→ 2001:bfa:0:1::1  

b) *Briefly explain under what circumstances IP must be fragmented.  
If a packet is larger than the MTU, it must be split/fragmented.  

c) *Where does fragmentation or reassembly take place in IPv4 and IPv6, respectively?  
- IPv4: All nodes (routers and sender) can fragment  
- IPv6: Only the sender fragments  
- Reassembly always at the destination node  

d) *Briefly explain the purpose and function of the TTL field in IPv4.  
- Time-to-Live to avoid routing loops  
- Decremented by 1 (second!) at each hop  
- If 0, then "ICMP TTL exceeded" and drop  

e) *What can NAT be used for in IPv6? Name an example. (Note: NAT does not serve as a firewall)  
Influencing routing, e.g., to analyze the response packet; hiding internal infrastructure, hiding device identifiers from IPv6 addresses; continuing to use applications written for IPv4 NAT; NAT64; etc.  

---  
Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to strike out invalid solutions.