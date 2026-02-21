Name First Name
.................
Grade
Degree Program (Major) Specialization (Minor)
I II
Student ID
Signature of the Candidate 1
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
Diploma Preliminary Exam
Bachelor Exam
7
............................
8
Consent to Release of Grades
via Email / Internet
9
10
Exam Subject: Fundamentals of Computer Networks and Distributed Systems
Examiner: Prof. Dr. Uwe Baumgarten Date: 27.06.2011
P
Lecture Hall: MW 0001 Row: .................... Seat: .....................
To be filled out by the supervisor only:
Lecture hall exited from ...... : ...... to ...... : ......
Submitted early at ....... : ......
Special Remarks:
Midterm Exam
Fundamentals
Computer Networks and Distributed Systems
Prof. Dr. Uwe Baumgarten
Chair of Operating Systems and System Software
Faculty of Computer Science
Technical University of Munich
Monday, 27.06.2011
14:30 – 15:15
• This exam consists of 12 pages and a total of 3 tasks. Please check now that you have received a complete set of materials.
• Please write your name and student ID in the header of each page.
• The total number of points is 15.
• Allowed aids are a double-sided A4 sheet of paper and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.
• Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
• Only those results will be counted where a solution method is recognizable.
1 Name:
Task 1 Media Access Control (5 Points)
5
Given a network consisting of three computers connected via a hub (see Figure 1). The distances between the computers are approximately d = 200m and d = 300m. The transmission rate is r = 100Mbit/s. The relative propagation speed is as usual ν = 2/3. The speed of light is given as c = 3·10^8m/s.
!"# !"$ !"%
d d
12 23
Figure 1: Network topology (not to scale)
At time t = 0s, no transmission occurs and none of the computers has data to send.
0
At time t = 1µs, PC1 begins to send a frame of total length 50b (including header).
1
At t = 3µs, PC2 and PC3 also have frames of total length 50b ready to send. (Note: b = Byte)
a)* Calculate the serialization time t for a message. 1/2
s
l 50·8bit X
t = = = 4.0µs
s r 100·10^6Mbit/s
b)* Calculate the propagation delays t (1,2) and t (2,3) for the two segments. 1/2
d 200m
12
t (1,2) = = = 1.0µs
p νc 2 ·3·10^8m/s
3
d 300m
12 X
t (2,3) = = = 1.5µs
p νc 2 ·3·10^8m/s
3
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
Student ID: 2
c) Draw a time-space diagram for 1-persistent CSMA/CD that represents the sending process in the time interval t ∈ [0µs,8µs). Neglect that 1-persistent CSMA/CD typically uses 2 slot times. Scale: 100m = 2cm and 1µs = 1cm.
PC1 PC2 PC3
t =0µs
0
t =1µs
1
t =3µs
2
3.5µs
3.82µs
5µs
5.5µs
6µs
7.5µs
1cm
• Sending from PC1 to PC3 X
• Sending from PC3 to PC1 aborted at t = 3.5µs X
• PC2 does not start sending X
• Indicated jam signal X
1 d) Justify why CSMA/CD does not function correctly under the given circumstances.
A sender assumes in CSMA/CD that its frame has been successfully transmitted if no collision occurs during transmission. X In this specific case, however, PC1 has completed the transmission before it receives the transmission from PC3. Therefore, PC1 does not recognize the collision and incorrectly assumes a successful transmission. X
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
3 Name:
e) The maximum length of a Fast Ethernet segment is d = 500m. Determine the minimum length l of a frame such that collision detection in Fast Ethernet works. 1
min
In the event of a collision, none of the sending nodes may terminate their sending process before they have noticed the collision. Otherwise, they would assume that the transmission was successful. This means that the minimum serialization time t of a frame must be twice the propagation delay between the two most distant stations:
! X
ts,min = 2·tp,max
l d
min max
= 2·
r νc
d
max
lmin = 2·r·
νc
bit 500m
= 2·100·10^6 · = 500bit = 62.5b X
s 2·10^8 m
s
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
Student ID: 4
Task 2 Bluetooth Physical Layer (5 Points)
5
Bluetooth is a wireless transmission method over short distances (usually up to 10m). It is often used for wireless connections between headsets and mobile phones. Sometimes mobile phones can also communicate with computers via Bluetooth, providing mobile access to the Internet.
In this task, we consider the physical layer of Bluetooth connections. Figure 2a shows the frequency range used by Bluetooth. This is divided into a total of 79 channels. Each channel has a (two-way) bandwidth of 1MHz. Phase-Shift Keying can be used as a modulation method. The signal space is illustrated in Figure 2b.
Q
f
... I
2401.5MHz 2480.5MHz
1MHz
(a) Frequency range and channels (b) Signal space
Figure 2: Bluetooth Physical Layer
1/2 a)* How many bits are transmitted per symbol?
The modulation method used is 4-PSK. Thus, we have:
X
N = log (M) = log (4) = 2bit
2 2
1/2 b) What is the maximum achievable data rate per channel?
With a channel bandwidth of 1MHz, we get
1
rmax = 10^6 ·2bit = 2Mbit/s. X
s
(Why not 2B·log (M)? It is exactly that, but the specification of 1MHz refers to a two-way bandwidth – see Exercise Sheet 5 Task c/d.)
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
5 Name:
The Bluetooth standard specifies a maximum bit error rate of p = 0.1%. A Bluetooth frame consists of a maximum of 2871 bits. We will assume a frame of maximum size in the following. Additionally, we assume that bit errors occur independently of each other.
c)* Determine the frame error probability p . 1/2
R
Let X be a random variable representing the number of bit errors per frame. Then the sought probability is given by
pR = 1−Pr[X = 0] = 1−(1−pe)2871 ≈ 94.34%. X
To reduce the frame error probability, Bluetooth supports the following two mechanisms:
1. Channel coding with a block code of length n = 3 and code rate R = 1/3, which can correct any bit error per channel word
2. Automatic Repeat Request (ARQ), which is aborted after a timeout
d)* We first consider Case 1. Determine the probability p that a channel word is transmitted incorrectly. 3/2
Let Y be a random variable representing the number of bit errors per channel word. The probability of an incorrectly transmitted channel word corresponds to the probability that two or all three bits in the channel word flip. X We get:
1
(cid:18)3(cid:19)
Pr[Y ≥ 2] = 1−Pr[Y ≤ 1] = 1−X i (1−pe)3−i·pie X
i=0
= 1−(1−pe)3−3·(1−pe)2·pe = 2.998·10−6. X
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
Student ID: 6
e) Determine the frame error probability p using the result from part d) with channel coding. 1/2
Let X′ be a random variable representing the number of bit errors per frame. Then the sought probability is given by
pR1 = 1−Pr[X′ = 0] = 1−(1−pK)2871 ≈ 8.57·10−3. X
f) Now determine the frame error probability p using ARQ with a maximum of 5 transmission attempts, using the result from part c). 1/2
The probability that a frame cannot be transmitted correctly via ARQ in a maximum of 5 attempts corresponds to the probability of 5 consecutive errors. Thus, we have
pR2 = p5R ≈ 74.74%. X
g) Under better circumstances, the bit error probability is now p′ = 10−6. Would you use channel coding or ARQ under these circumstances? (Justification!)
Under these circumstances, the frame error probability without channel coding is p ≈ 2.87·10−3. Thus, on average, only one of about 350 frames needs to be repeated. In contrast, the frame error probability with channel coding is practically zero, but the transmission rate drops to about 1/3. Therefore, ARQ is clearly preferred. X X
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
7 Name:
Task 3 Short Questions (5 Points)
5
The following short questions are independent of each other. Bullet-point answers are sufficient!
a)* What are MAC addresses used for? 1/2
Identification of the Next Hop X
b)* What are IP addresses used for (as opposed to MAC addresses)? 1/2
End-to-End Addressing X
c)* In the lecture, a simple block code was presented that maps k = 1 bit to n = 3 bits:
0 → 000, 1 → 111.
To further improve error correction, the following modification is proposed:
0 → 0000, 1 → 1111.
How do you assess this change in terms of error correction and efficiency? 1
The error correction property does not change X, the efficiency decreases X
d)* What goal is pursued with source coding? 1/2
Removal of redundancy from a data stream (compression) X
e)* What goal is pursued with channel coding? 1/2
Deliberate addition of redundancy (error correction) X
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
Student ID: 8
f)* The graphic below shows the transmitted signal y(t) and the received signal x(t) after transmission over a non-ideal channel. What two channel influences are visible?
1.5 1.5
1 ) 1
(t
x
y(t) 0.5 signal 0.5
0 ngssig 0
d a
en−0.5 pf−0.5
S m
E
−1 −1
−1.5 0 1 2 3 4 5 6 7 8 −1.5 0 1 2 3 4 5 6 7 8
Time t/T Time t/T
s s
Low-pass filtering X and attenuation X
1/2 g)* What is a Shortest Path Tree?
Spanning tree with minimal path costs from a root to all other nodes X
1/2 h)* What is a Minimum Spanning Tree?
Spanning tree with overall minimal edge costs X
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
9 Name:
Additional space for solutions – please clearly mark the affiliation to the respective task and cross out invalid solutions!
PC1 PC2 PC3
t =0µs
0
1cm
PC1 PC2 PC3
t =0µs
0
1cm
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
Student ID: 10
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
11 Name:
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011
Student ID: 12
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2011