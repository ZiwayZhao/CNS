Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

Confirmation of Conduct Rules  
I hereby assure that I will solve this exam exclusively using the resources listed below and submit it under my name.  
Sticker will be generated  
Signature or full name if no pen input is available  

Basics: Computer Networks and Distributed Systems  
Exam: IN0010/Quiz2 Date: Wednesday, June 11, 2025  
Examiner: Prof. Dr.-Ing. Georg Carle Time: 19:00–19:15  

Instructions for Processing  
- This exam consists of 6 pages with a total of 3 tasks. Please check now that you have received a complete set of information.  
- The total score for this exam is 15 points.  
- The removal of pages from the exam is prohibited.  
- The following aids are permitted:  
  - everything except group work, plagiarism, and any form of AI (e.g., ChatGPT)  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be graded where the solution path is recognizable. Also, text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  

---  

### Task 1  
Multiple Choice (6 points)  
The following tasks are multiple choice/multiple answer, meaning at least one answer option is correct.  
Subtasks with only one correct answer will be graded with 1 point if correct. Subtasks with more than one correct answer will be graded with 1 point for each correct answer and 1 point for each incorrect mark. Missing marks have no effect. The minimum score per subtask is 0 points.  

Mark the correct answers  
Marks can be crossed out by complete filling  
Crossed out answers can be marked next to be newly crossed  

**Figure 1.1: Network Topology**  

a) *How many collision domains are there in the network in Figure 1.1?*  
1 7 5 3 4 2 0 6  

b) *How many broadcast domains are there in the network in Figure 1.1?*  
5 6 1 4 2 0 7 3  

c) *Given the CRC polynomial 11011 and the message 1101100. What is the CRC checksum for the message?*  
1101 Another value 1110 1001  
1011 u 1111 0000 1000  

d) *Which statement(s) apply to the MAC address 74:9C:8F:4F:1E:DD?*  
Multicast Locally administered Bicast  
× ×  
Unicast Globally unique Broadcast  

e) *A notebook NB1 sends a frame to notebook NB2 over WLAN. Both are connected to the access point AP. Which Layer 2 addresses are contained in the header of the frame sent by NB1?*  
NB1, NB2 and AP NB1 and NB2 NB1 and AP NB2 and AP  

---  

### Task 2  
Transmission Time (3 points)  
You send a radio message from the space station INTERPLANAR XII to Earth. The distance between Earth and INTERPLANAR XII is currently 300 light-seconds. The 5MB large message is transmitted at a rate of 10 kbit/s.  
Note: 1 light-second (Ls) is the distance that light travels in a vacuum in exactly one second. Specifically, it holds that  
1 Ls = 1 s c = 3 × 10^5 km.  

How many minutes does it take until the message has completely arrived on Earth?  
t = L / r = 5 × 10^6 / 10^3 = 4,000 s  
d = 300 Ls = 300 s c  
t = d / v = 300 s / c0 ≈ 300 s  
t = t + t = 4,300 s ≈ 71.67 min  

---  

### Task 3  
Switching ARP (6 points)  
We consider the following topology where PC1 wants to communicate with PC3. Since PC1 only knows the IPv4 address of PC3, address resolution with ARP is necessary. Assume that the ARP caches of the PCs and the switching table of the switch are empty.  
Decide in the following subtasks whether a PC is affected (yes) or not (no) and briefly justify your decision in bullet points. The justification can be identical for several PCs!  

**Figure 3.1: Network Topology**  

a) *Which PCs receive the ARP request sent by PC1?*  
1 Receive yes/no Justification  
2 PC1 no Sender of the request  
PC2 yes Switch Broadcast (ARP request to broadcast address)  
PC3 yes Switch Broadcast & a collision domain through hub  
PC4 yes Switch Broadcast & a collision domain through hub  

b) *Which PCs respond to the ARP request from PC1 with an ARP reply?*  
1 Respond yes/no Justification  
2 PC1 no Sender of the request  
PC2 no Not addressed with Target Protocol Address → Discarded  
PC3 yes Addressed with Target Protocol Address → Responds  
PC4 no Not addressed with Target Protocol Address → Discarded  

c) *Which PCs receive the ARP reply from PC3?*  
1 Receive yes/no Justification  
2 PC1 yes Switch has PC1 in switching table, target of the ARP reply  
PC2 no Switch has PC1 in switching table, PC1 not at port 2  
PC3 no Sender of the message  
PC4 yes Collision domain through hub  

---  

Additional space for solutions. Clearly mark the assignment to each subtask. Do not forget to cross out invalid solutions.