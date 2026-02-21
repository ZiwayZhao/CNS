Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

Confirmation of Behavioral Rules  
I hereby assure that I will solve this exam exclusively using the resources listed below and submit it under my name.  
Sticker will be generated  
Signature or full name, if no pen input is available  

Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Quiz4 Date: Wednesday, July 19, 2023  
Examiner: Prof. Dr.-Ing. Georg Carle Time: 19:30–19:45  

Instructions for Processing  
- This exam consists of 4 pages with a total of 2 tasks. Please check now that you have received a complete set of information.  
- The total score for this exam is 15 points.  
- The tearing out of pages from the exam is prohibited.  
- The following aids are allowed:  
  - everything except group work, plagiarism, and any form of AI (e.g., ChatGPT)  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Please do not write with red/green colors or with pencil.  

---  

**Task 1**  
Multiple Choice (11 Points)  
The following tasks are Multiple Choice/Multiple Answer, meaning at least one answer option is correct.  
Sub-tasks with only one correct answer will be awarded 1 point if correct. Sub-tasks with more than one correct answer will be awarded 1 point for each correct answer and 1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

Mark the correct answers  
Marks can be crossed out by complete filling  
Crossed out answers can be marked with adjacent markings  

a) *Which statements about NAT are correct?  
- NAT can translate TCP ports into UDP ports.  
- NAT replaces the destination port of outgoing packets.  
- NAT replaces the source IP of incoming packets.  
- NAT replaces the source IP of outgoing packets.  
- NAT offers a high level of protection against unauthorized access.  
- NAT replaces the source port of incoming packets.  
- NAT replaces the destination IP of outgoing data packets.  
- NAT replaces the destination IP of incoming packets.  

b) *The path MTU is 1500 B. IPv4 is used at layer 3. How large should the MSS be chosen if no TCP options are used?  
- 1500 B  
- 1520 B  
- 1540 B  
- 1452 B  
- 1480 B  
- 1460 B  

c) *Which PTR record belongs to the IP address 105.2.11.5?  
- 5.11.2.5.in-addr.arpa.  
- 2.105.5.11.in-addr.arpa.  
- 8.8.4.4.in-addr.arpa.  
- 105.2.11.5.in-addr.arpa.  
- 5.11.2.105.in-addr.arpa.  
- 4.4.8.8.in-addr.arpa.  

d) *You observe a TCP segment. The first 8 bytes of the TCP header are given in Figure 1.1. What service is the sender likely to use?  
```
0x0000 16 00 00 19  
0x0004 73 63 b0 f0  
```  
Figure 1.1: Hex dump of the first 8 bytes of a TCP header, in Network Byte Order  
- HTTPS  
- DHCP  
- SSH  
- SMTP  
- POP3  
- HTTP  

e) *Which of the following system calls only make sense with connection-oriented sockets?  
- accept()  
- select()  
- close()  
- bind()  
- sendto()  
- listen()  

f) *Which statements about congestion and flow control are correct?  
- Flow control tries to avoid overload at the receiver.  
- Congestion control adjusts the send window.  
- Flow control tries to avoid overload at the sender.  
- Congestion control tries to avoid overload at the receiver.  
- Congestion control tries to avoid overload at the sender.  
- Flow control adjusts the receive window.  
- Congestion control tries to avoid overload in the network.  
- Flow control adjusts the send window.  

---  

**Task 2**  
Short Tasks (Code Demos) (4 Points)  
a) *What does connect() do on a UDP socket?  
- 0  
- 1  
- 2  

b) *Describe two advantages that the TCP chat (from the code demo) offers over the UDP chat.  
- 0  
- 1  
- 2  

Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.