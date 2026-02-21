Name First Name  
..................  
Grade  
Study Program (Major) Specialization (Minor)  
I II  
Student ID  
Signature of the Candidate  

TECHNICAL UNIVERSITY OF MUNICH  
Faculty of Computer Science  
× Midterm Exam  
Final Exam  
Semester Exam  
Diploma Preliminary Examination  
Bachelor Examination  
............................  
Consent to Grade Disclosure  
via Email / Internet  

Exam Subject: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle  
Date: 18.06.2012  
Lecture Hall: .................... Row: .................... Seat: .....................  
To be filled out by the supervisor only:  
Lecture Hall left from ...... : ...... to ...... : ......  
Submitted early at ....... : ......  
Special Remarks:  

Midterm Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
Monday, 18.06.2012  
19:15 – 20:00  

- This exam consists of 8 pages and a total of 3 tasks. Please check now that you have received a complete set of materials.  
- Please write your name and student ID in the header of each page.  
- The total number of points is 15.  
- Allowed aids are a double-sided handwritten A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be counted where a solution path is recognizable. Text problems must be justified unless explicitly stated otherwise in the respective sub-task.  

1 Name:  
Task 1  
Waternet (5 points)  
Figure 1.1 shows a hypothetical network that uses water-filled pipes as a transmission medium instead of copper wires. The distributor V essentially consists of a water-filled sphere without further logic. For simplicity, we assume that reflections do not play a role. The distance between PC1 and V is 20m, and the distance between PC3 and V is 10m. The distance between V and PC2 is so small that it can be neglected.  

V  
PC1 PC3  
20m PC2 10m  
Figure 1.1: Waternet network consisting of 3 computers and a distributor.  
The propagation speed of sound in water at 20°C is approximately 1500m/s. This technique, called Waternet, uses CSMA/CD as a media access method, just like regular Ethernet. The transmission rate is r = 1MBit/s.  

a)* What device corresponds to the distributor V in a regular Ethernet?  
b)* Determine the serialization time  
c)* Determine the propagation delay between PC1 and PC3  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2012  
Student ID: 2  
At time t = 15ms, PC2 and PC3 also have 1500 bytes of data ready to send.  

d) Draw a time-distance diagram that represents all events starting from the time t0 = 0ms. If any of the computers sends a jam signal, it is sufficient to indicate its start time. Do not forget to label the diagram correctly!  
(Scale: horizontal (cid:44), vertical (cid:44))  
1cm 2.5m 1cm 10ms  
t = 0ms  

e) Justify why CSMA/CD does not function correctly under the given circumstances?  
f) Propose a modification so that CSMA/CD functions correctly. (Calculation!)  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2012  
3 Name:  
Task 2  
Digital Modulation Techniques (4 points)  
In this task, the processes of pulse shaping in baseband and subsequent modulation will be worked out. For this purpose, the signal space of a digital modulation technique is given in Figure 2.1. The bit sequence to be transmitted is given as 01111001. The rectangular pulse will be used as the basic pulse for the baseband signal.  

a)* What modulation technique is being used?  
b)* Enter a valid assignment of codewords to symbols in Figure 2.1a.  
c)* Draw the basic pulse in Figure 2.1b.  
d) Now draw the baseband signal corresponding to the given bit sequence in Figure 2.2.  
The baseband signal from the previous sub-task will now be used to modulate the cosine carrier.  
s(t) = cos(2πt/T)  
e) Also draw the modulated signal in Figure 2.2.  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2012  
Student ID: 4  
t  
T  
4  
T  
3  
T  
2  
T  
1  
2 1 1 2  
− −  
T  
1  
−  
Figure 2.2: Solution sheet for sub-tasks d) and e)  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2012  
5 Name:  
Task 3  
Short Tasks (6 points)  
The following short tasks are independent of each other. Bullet-point answers are sufficient!  

a)* Figure 3.1 shows measured RTTs from two different computers A and B to the same destination. Computer A is connected to the Internet via a broadband connection, while Computer B has a UMTS connection. Justify which of the two measurements was taken from Computer B.  

b)* In Programming Task 1, we found that Hamming codes are susceptible to burst errors. Briefly explain whether this susceptibility can be reduced through permutations.  
c)* What goal is pursued with channel coding?  
d)* What goal is pursued with source coding?  
e)* Given the address block 131.159.20.64/26. Provide the network address, broadcast address, and the number of usable addresses for hosts.  
f)* You receive the binary message, which has been secured using CRC. The generator polynomial is g(x) = x^3 + 1. Check if an error occurred during transmission.  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2012  
7 Name:  
g)* Given the data block shown in the solution field (L4-PDU). Add header/trailer schematically if IP is used over Ethernet. Detailed information on individual fields within the header is not necessary!  
Data  
h)* Given the network topology from the solution field. Draw all broadcast and collision domains.  
Switch Router Hub  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2012  
Student ID: 8  
Additional space for solutions – please clearly mark the affiliation to the respective task and cross out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2012