Name First Name  
..................  
Grade  
Degree Program (Major) Field of Study (Minor)  
I II  
Student ID  
Signature of the Candidate  
1  
2  
TECHNICAL UNIVERSITY OF MUNICH  
3  
Faculty of Computer Science  
4  
× Midterm Exam  
Final Exam  
5  
Semester Exam  
6  
Diploma Preliminary Examination  
Bachelor Examination  
7  
............................  
8  
Consent to Release of Grades  
via Email / Internet  
9  
10  
Examination Subject: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr. Uwe Baumgarten Date: 27.06.2011  
P  
Lecture Hall: MW 0001 Row: .................... Seat: .....................  
To be filled out by the supervisor only:  
Lecture hall exited from ...... : ...... to ...... : ......  
Submitted early at ....... : ......  
Special Remarks:  
Midterm Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr. Uwe Baumgarten  
Chair of Operating Systems and System Software  
Faculty of Computer Science  
Technical University of Munich  
Monday, 27.06.2011  
14:30 – 15:15  
• This exam consists of 12 pages and a total of 3 tasks. Please check now that you have received a complete set of information.  
• Please write your name and student ID in the header of each page.  
• The total number of points is 15.  
• Allowed materials include a double-sided A4 sheet with any notes and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
• Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
• Only results where a solution method is recognizable will be graded.  
1 Name:  
Task 1 Bluetooth Physical Layer (5 points)  
Bluetooth is a wireless transmission method over short distances (usually up to 10m). It is often used for wireless connections between headsets and mobile phones. Sometimes mobile phones can also communicate with computers via Bluetooth, enabling mobile internet access.  
In this task, we consider the physical layer of Bluetooth connections. Figure 1a shows the frequency range used by Bluetooth. This is divided into a total of 79 channels. Each channel has a (bidirectional) bandwidth of 1MHz. Phase-Shift-Keying can be used as a modulation method, among others. The signal space is represented in Figure 1b.  
Q  
f  
... I  
2401.5MHz 2480.5MHz  
1MHz  
(a) Frequency range and channels (b) Signal space  
Figure 1: Bluetooth Physical Layer  
a)* How many bits are transmitted per symbol?  
b) What is the maximum achievable data rate per channel?  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
Student ID: 2  
The Bluetooth standard specifies a maximum bit error rate of p = 0.1%. A Bluetooth frame consists of a maximum of 2871 bits. We will assume a frame of maximum size in the following. We also assume that bit errors occur independently of one another.  
c)* Determine the frame error probability p.  
R  
To reduce the frame error probability, Bluetooth supports the following two mechanisms:  
1. Channel coding with a block code of length n = 3 and coderate R = 1/3, which can correct any bit error per channel word.  
2. Automated Repeat Request (ARQ), which is aborted after a timeout.  
d)* We will first consider Case 1. Determine the probability p that a channel word is transmitted incorrectly.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
3 Name:  
e) Using the result from part d), determine the frame error probability p when using channel coding.  
f) Now determine the frame error probability p using the result from part c) when using ARQ with a maximum of 5 transmission attempts.  
g) Under better circumstances, the bit error probability is now p' = 10−6. Would you use channel coding or ARQ under these circumstances? (Justification!)  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
Student ID: 4  
Task 2 Media Access Control (5 points)  
Given is a network consisting of three computers connected via a hub (see Figure 2). The distances between the computers are approximately d = 300m and d = 200m. The transmission rate is r = 100Mbit/s. The relative propagation speed is as usual ν = 2/3. The speed of light is given as c = 3·10^8 m/s.  
!"# !"$ !"%  
d d  
12 23  
Figure 2: Network topology (not to scale)  
At time t = 0s, no transmission is taking place and none of the computers has data to send.  
At time t = 1µs, PC1 begins to send a frame of total length 25b (including header).  
At t = 3µs, PC2 and PC3 also have frames of total length 25b ready to send. (Note: b = Byte)  
a)* Calculate the serialization time t for a message.  
s  
b)* Calculate the propagation delays t (1,2) and t (2,3) on the two segments.  
p p  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
5 Name:  
c) Draw a time-space diagram for 1-persistent CSMA/CD that represents the sending process in the time interval t ∈ [0µs, 8µs). Neglect that 1-persistent CSMA/CD usually uses slot times. Scale: 100m = 2cm and 1µs = 1cm.  
PC1 PC2 PC3  
t0 = 0µs  
1cm  
d) Justify why CSMA/CD does not work correctly under the given circumstances.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
Student ID: 6  
e) The maximum length of a Fast Ethernet segment is d = 500m. Determine the minimum length l of a frame so that collision detection in Fast Ethernet works.  
min  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
7 Name:  
Task 3 Short Questions (5 points)  
The following short questions are independent of each other. Bullet-point answers are sufficient!  
a)* What goal is pursued with source coding?  
b)* What goal is pursued with channel coding?  
c)* The graphic below shows the transmitted signal y(t) as well as the received signal x(t) after transmission over a non-ideal channel. What two channel influences are visible?  
1.5 1.5  
1 ) 1  
(t  
x  
y(t) 0.5 signal 0.5  
esignal 0 ngssig 0  
d a  
en−0.5 pf−0.5  
S m  
E  
−1 −1  
−1.5 0 1 2 3 4 5 6 7 8 −1.5 0 1 2 3 4 5 6 7 8  
Time t/T Time t/T  
s s  
d)* What is a Shortest Path Tree?  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
Student ID: 8  
e)* In the lecture, a simple block code was presented that maps k = 1 bit to n = 3 bits:  
0 → 000, 1 → 111.  
To further improve error correction, the following modification is proposed:  
0 → 0000, 1 → 1111.  
How do you evaluate this change in terms of error correction and efficiency?  
f)* What is a Minimum Spanning Tree?  
g)* What are MAC addresses used for?  
h)* What are IP addresses used for (as opposed to MAC addresses)?  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
9 Name:  
Additional space for solutions – please clearly mark the affiliation to the respective task and cross out invalid solutions!  
PC1 PC2 PC3  
t0 = 0µs  
1cm  
PC1 PC2 PC3  
t0 = 0µs  
1cm  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
Student ID: 10  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
11 Name:  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011  
Student ID: 12  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2011