Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during attendance control by sticking a code.
- This contains only a continuous number, which is also noted in the attendance list next to the sticker in the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Quiz2  
Date: Monday, July 5, 2021  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 11:30–11:45  

Please sign the code of conduct at the top right next to your sticker.  
Otherwise, your electronic exercise performance will not be counted!

### Instructions for Processing
- This exam consists of 4 pages with a total of 2 tasks. Please check now that you have received a complete set of information.
- The total score for this exam is 15 points.
- Removing pages from the exam is prohibited.
- The following aids are permitted:
  - All electronic and non-electronic aids
  - Group work of any kind is not allowed.
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be counted where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.
- Please write with red/green colors or with pencil.

---

### Task 1  
Multiple Choice (11.5 Points)  
The following tasks are Multiple Choice/Multiple Answer, meaning at least one answer option is correct.  
Tasks with only one correct answer are scored with 1 point if correct. Tasks with more than one correct answer are scored with 0.5 points for each correct tick and 0.5 points for each incorrect answer. The minimum score per task is 0 points.

Please tick the correct answers.  
Ticked answers can be crossed out by completing the fill-in.  
Crossed-out answers can be ticked again by marking them next to it.

a) Which syscalls are necessary on the client side in any case to exchange messages via UDP with the respective counterpart?  
*Note: Not all syscalls necessary for actual communication may be available.*

- send
- sendto
- select
- listen
- accept
- connect
- socket

b) Which statements about UDP chats are correct?  
- Two clients cannot communicate with each other without a server.
- The server does not know whether a client is still online or not.
- Messages are repeated in case of loss.
- The server is notified when a client terminates the application.
- Two clients can also communicate with each other without a server.
- It is unclear whether a sent message is received.

c) Given the following code snippet. Does it work as intended?  
```c
struct sockaddr_in sa;
sa.sin_addr = INADDR_LOOPBACK;
sa.sin_port = htons(port);
sa.sin_family = AF_INET;
```
- Yes, but only the unspecified IP 0.0.0.0 is used.
- No, the IP address must be translated into Network Byte Order.
- Yes, there is no error contained.
- No, not all members of the sockaddr_in struct are initialized.

d) What factors influence the size of the send window in TCP Reno?  
- Acknowledgements
- Receive window
- None of these
- Max. data rate on layer 1
- RTT
- Timeout

e) Which of the following protocols are Link State Protocol(s)?  
- EIGRP
- IS-IS
- OSPF
- AODV
- HWMP
- IGRP

f) Given the examples for BGP known from the lecture. Which statements are correct?  
1. Peering
   - AS7018 (AT&T)
   - AS1239 (Sprint)
2. AS3209 (Vodafone)
   - AS5511 (Orange)
   - AS1257 (Tele2)
   - AS7922 (Comcast)
3. Orange announced its routes to Tele2.
4. AT&T and Sprint do not charge each other for the use of the peerings.
5. AT&T charges money from Tele2.
6. Orange announced the routes from Vodafone to Tele2.

g) Determine the MAC address belonging to the IPv6 address FFB8::7DB2:8744:24BC.  
- FF:B8:7D:B2:87:44
- FF:FF:FF:FF:FF:FF
- 33:33:87:44:24:BC
- 7D:B2:87:44:24:BC

h) Which MAC address belongs to the automatically configured IPv6 address FF80::EDB4:BCFF:FEB0:8760?  
- EF:B4:BC:B0:87:60
- ED:B4:BC:B0:87:60
- FF:80:ED:B4:BC:B0
- 33:33:BC:B0:87:60

---

### Task 2  
Short Tasks (3.5 Points)  
a) What is meant by an Autonomous System?  
- A collection of networks under a unified administrative control.

b) What is meant by bit stuffing?  
- Preventing the occurrence of control characters by deliberately inserting additional bits into the payload.

c) You have the following network architecture. The respective MTU is given for the path segments. Determine the maximum payload that you can transmit with ICMP over IPv4 between the two clients so that the packet does not need to be fragmented. IP header options can be neglected.  
- 2312 B  
- 1500 B  
- 9000 B  
- 576 B  
- Headers are not part of the payload: 8 B (ICMP) + 20 B (IP)  
- Only the smallest MTU on the path is relevant: 1500 B  
- Maximum size without fragmentation = 1500 B - 8 B - 20 B = 1472 B  

---

Additional space for solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to cross out invalid solutions.