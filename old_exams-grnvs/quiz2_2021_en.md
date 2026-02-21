Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized during attendance control by affixing a code.  
- This contains only a sequential number, which is also noted in the attendance list next to the sticker in the signature field.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Quiz2  
Date: Monday, July 5, 2021  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 11:30–11:45  

Please sign the rules of conduct at the top right next to your sticker.  
Otherwise, your electronic exercise performance will not be counted!  

**Instructions for Processing**  
- This exam consists of 4 pages with a total of 2 tasks. Please check now that you have received a complete set of information.  
- The total score for this exam is 15 points.  
- Detaching pages from the exam is prohibited.  
- The following aids are allowed:  
  - all electronic and non-electronic aids  
  - group work of any kind is not permitted  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be counted where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  

---

### Task 1  
**Multiple Choice (11.5 points)**  
The following tasks are multiple choice/multiple answer, meaning that at least one answer option is correct for each.  
Sub-tasks with only one correct answer are rated with 1 point if correct. Sub-tasks with more than one correct answer are rated with 0.5 points for each correct tick and 0.5 points for each incorrect answer. The minimum score per sub-task is 0 points.  

Please tick the correct answers.  
Ticked answers can be crossed out by complete filling.  
Crossed out answers can be ticked again by adjacent markings.  

a) *Which syscalls are necessary on the client side in any case to exchange messages via UDP with the respective counterpart? Note: Not all syscalls necessary for actual communication may be available for selection.  
- send  
- sendto  
- select  
- listen  
- accept  
- connect  
- socket  

b) *Which statements about UDP chats are correct?  
- Two clients cannot communicate with each other without a server.  
- The server does not know whether a client is still online or not.  
- Messages are repeated in case of loss.  
- The server is notified when a client ends the application.  
- Two clients can also communicate with each other without a server.  
- It is unclear whether a sent message also arrives.  

c) *Given the following code snippet. Does it work as intended?  
```c
struct sockaddr_in sa;  
sa.sin_addr = INADDR_LOOPBACK;  
sa.sin_port = htons(port);  
sa.sin_family = AF_INET;  
```  
- Yes, but only the unspecified IP 0.0.0.0 is used.  
- No, the IP address must be translated into network byte order.  
- Yes, there is no error contained.  
- No, not all members of the sockaddr_in struct are initialized.  

d) *Which factors influence the size of the send window in TCP Reno?  
- Acknowledgements  
- Receive window  
- None of these  
- Max. data rate on layer 1  
- RTT  
- Timeout  

e) *Which of the following protocols are link-state protocols?  
- EIGRP  
- IS-IS  
- OSPF  
- AODV  
- HWMP  
- IGRP  

f) *Given the known example for BGP from the lecture. Which statements are correct?  
1. Peering  
   - AS7018  
   - AS1239  
   - (AT&T)  
   - (Sprint)  
2.  
   - AS3209  
   - AS5511  
   - AS1257  
   - AS7922  
   - (Vodafone)  
   - (Orange)  
   - (Tele2)  
   - (Comcast)  
3.  
- Orange announced its own routes to Tele2.  
- AT&T and Sprint do not charge each other for the use of peering.  
- AT&T charges money from Tele2.  
- Orange announced the routes from Vodafone to Tele2.  

g) *Determine the MAC address corresponding to the IPv6 address FFB8::7DB2:8744:24BC.  
- FF:B8:7D:B2:87:44  
- FF:FF:FF:FF:FF:FF  
- 33:33:87:44:24:BC  
- 7D:B2:87:44:24:BC  

h) *Which MAC address belongs to the automatically configured IPv6 address FF80::EDB4:BCFF:FEB0:8760?  
- EF:B4:BC:B0:87:60  
- ED:B4:BC:B0:87:60  
- FF:80:ED:B4:BC:B0  
- 33:33:BC:B0:87:60  

---

### Task 2  
**Short Tasks (3.5 points)**  
a) *What is meant by an Autonomous System?  
- 0  
- 1  

b) *What is meant by bit-stuffing?  
- 0  
- 1  

c) *You have the following network architecture. The respective MTU is given for the path segments. Determine the maximum payload that you can transmit with ICMP over IPv4 between the two clients so that the packet does not need to be fragmented. IP header options can be neglected.  
- 0  
- 1  
- 2312 B  
- 1 5 0 0 B  
- 9000 B  
- 576 B  

---

**Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.**