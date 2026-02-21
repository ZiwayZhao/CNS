Name First Name  
..................  
Grade  
Course of Study (Major) Specialization (Minor)  
I II  
Student ID Number  
Signature of the Candidate 1  
2  
TECHNICAL UNIVERSITY OF MUNICH  
a 3  
Faculty of Computer Science  
l  
× Midterm Exam h 4  
Final Exam c  
5  
s  
Semester Exam  
r  
Diploma Preliminary Examination 6  
o  
Bachelor Examination  
v  
............................ 7  
s  
Consent for Grade Disclosure 8  
via E-Mail / Internet  
n  
9  
u  
10  
s  
Subject of Examination: Fundamentals of Computer Networks and Distributed Systems  
ö  
L  
Examiner: Prof. Dr.-Ing. Georg Carle Date: 20.06.2013 (cid:80)  
Lecture Hall: .................... Row: .................... Seat: .....................  
To be filled out only by the supervisor:  
Lecture hall exited from ...... : ...... to ...... : ......  
Submitted early at ....... : ......  
Special Remarks:  
Midterm Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
Thursday, 20.06.2013  
19:30 – 20:15  
• This exam consists of 8 pages and a total of 3 tasks. Please check now that you have received a complete set of information.  
• Please write your name and student ID number in the header of each page.  
• Do not write in red/green ink or with a pencil.  
• The total number of points is 15.  
• The following aids are permitted: a double-sided handwritten DIN A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
• Tasks marked with * can be solved without knowledge of the results of preceding sub-tasks.  
• Only those results where a solution method is recognizable will be counted. Text problems must be justified unless explicitly stated otherwise in the respective sub-task.  
1 Name:  
Task 1  
Voyager (5 Points)  
In 1977, the two space probes Voyager 1 & 2 were launched at intervals of just over a month (see Figure 1.1a). They were to explore the outer planets of our solar system for the first time. Both probes passed Jupiter in 1979 and about 18 months later Saturn. Voyager 1 has since been on a course out of our solar system and is currently at the boundary of interstellar space1. Voyager 2, on the other hand, passed the two distant gas giants Uranus and Neptune and has also been on a course leading out of the solar system.  
(a) Schematic Representation (b) Flight Plan  
Figure 1.1: Schematic Representation (a) and Flight Plan (b) of the Voyager 1 & 2 Space Probes  
On June 12, 2013, the two probes were at a distance2 of about  
18502189000 km (Voyager 1) and (Voyager 2) from Earth. Below, we want to examine some of the challenges – then and now – regarding communication with the two space probes.  
a)* Determine the time between sending a signal to Voyager 1 until it arrives on Earth.  
d ≈ 18502189000000 m ≈ ≈ (cid:88)  
tp = νc 3·10^8 m/s 61674 s 17h  
1 It is currently not fully clarified whether Voyager 1 has already left the so-called heliosphere and is thus in interstellar space.  
2 http://voyager.jpl.nasa.gov/where/index.html  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013  
Student ID Number: 2  
Data was Manchester encoded, using only two signal levels. Figure 1.2 shows an exemplary short excerpt of such a signal that Voyager 1 sent to Earth.  
s(t)  
t  
∆t  
Figure 1.2: Manchester-encoded Baseband Signal from Voyager 1  
/b)* Provide the transmitted bit sequence in the time domain.  
1 2 ∆t  
Note: There are two valid solutions.  
(cid:88)  
or  
10100011 01011100  
×  
The color images transmitted to Earth had a resolution of 800 x 800 pixels at 24 bits per pixel. The images were then sent back to Earth via a wide downlink in the range of  
360 kHz to 2295 MHz.  
/c)* Determine the size of a single image in MB.  
(cid:88)  
L = 800 x 800 x 24 bits = 1.92 MB  
To reduce the bit error rate to an acceptable level, the so-called Golay code was used as channel coding. This maps a block of 12 bits of payload data to a 24-bit long codeword. Within such a codeword, 3 arbitrary bit errors can be corrected.  
d)* Provide the code rate of the Golay code.  
1/2  
12 1 (cid:88)  
R = =  
24 2  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013  
3 Name:  
e)* Provide the general probability of a block being transmitted incorrectly.  
p  
e,block  
Notes: You can simplify by assuming that bit errors occur independently and uniformly with probability.  
p  
(cid:18) (cid:19)  
(cid:88)  
(cid:88)  
− 3 24 − −  
p = 1 pi(1 - p)24 i  
e,block  
i  
i=0  
By using the Golay code, images of Saturn could be transmitted at a payload data rate of  
29 kbit/s  
with an average bit error rate of · − 5 10 3.  
f) Determine the necessary time to send a single image towards Earth.  
1/2  
L 1.92 MB ≈ (cid:88)  
t = = 8.8 min  
s  
r 29 kbit/s  
g)* Justify why the transmission of compressed images was not possible without further modifications.  
The images are transmitted in a compressed format, whereby a single bit error affects multiple pixels – which would not be acceptable at the given bit error rate.  
h)* Determine the necessary SNR at the ground station in dB so that the given data rate can be achieved with a wideband signal.  
360 kHz  
1 ·  
B = 360 kHz  
2  
!  
r = Blog (1 + SNR)  
2  
⇒ − ≈ (cid:88) ≈ − (cid:88)  
SNR = 10^(r/B) 1 0.1181 9.28 dB  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013  
Student ID Number: 4  
Task 2  
Slotted ALOHA (6 Points)  
In this task, we consider a transmission channel that operates using the multiple access method Slotted ALOHA. We assume that all stations send independently with the same transmission probability. Furthermore, all messages are of constant size  
p  
(transmission duration per message). We further assume that the number of participating stations  
T  
is sufficiently large and the transmission probability is small enough that the Poisson distribution  
N p  
can be used as an approximation for the binomial distribution. The probability density of the Poisson distribution is given by  
−  
λ^k e^(-λ) (1)  
Pr[X = k] = .  
k!  
1 a)* In a measurement over a sufficiently long period, it is found that the transmission channel is not utilized 10%. Determine the packet rate as a numerical value.  
−  
λ^k e^(-λ)  
Pr[X = k] =  
k!  
−  
λ^0 e^(-λ) (cid:88)  
Pr[X = 0] = = 0.1  
0!  
−  
0.1 =! e^(-λ)  
(cid:88)  
λ = 2.30  
For the rest of the task, we assume that the network consists of a total of 50 stations.  
1 b) Now determine the transmission probability of the stations as a numerical value.  
p  
λ = Np  
(cid:88)  
λ  
p = = 0.046 = 4.6%  
N  
1 c) Now determine the probability as a numerical value that a collision occurs.  
p  
K  
− − (cid:88)  
p = 1 - Pr[X = 0] - Pr[X = 1]  
K  
− −  
= 1 - 0.10 - 0.23  
≈ (cid:88)  
0.67  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013  
5 Name:  
1  
ALOHA  
)  
n Slotted ALOHA  
e  
n  
sio 0.8  
olli  
K  
e 0.6  
n  
h  
o  
(  
g  
un 0.4  
t  
s  
a  
sl  
u  
a 0.2  
al  
n  
a  
K  
0  
0 1 2 3 4 5 6 7 8 9 10  
λ  
Figure 2.1: Channel Utilization with ALOHA vs. Slotted ALOHA  
We now consider Figure 2.1, which illustrates the relationship between channel utilization and the number of ready-to-send stations in ALOHA and Slotted ALOHA.  
d)* Justify why the throughput is higher in Slotted ALOHA.  
1  
(cid:88)  
In Slotted ALOHA, fewer collisions occur, as nodes only begin to send at specific times. The interval within which two transmissions can overlap is therefore  
(cid:88)  
only half as large.  
e)* Draw the utilization curve of an ideal multiple access method in Figure 2.1.  
1/2  
f) Provide a brief justification for your solution to part e).  
1/2  
Channel utilization increases linearly with the number of ready-to-send stations and remains at 1 if more  
(cid:88)  
than one station is on average ready to send.  
g)* What problems can arise when using Slotted ALOHA if the time slots are chosen to be very large compared to the message length?  
Too large time slots compared to the message length result in high "waste". The slots are only occupied to a small extent, and no transmissions can take place in the remaining time,  
(cid:88)  
which can reduce throughput.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013  
Student ID Number: 6  
Task 3  
Short Tasks (4 Points)  
The following short tasks are each independent of one another. Bullet-point answers are sufficient!  
a)* What does half-duplex mean in the area of message transmission?  
1/2  
On the transmission channel, messages can be transmitted in both directions, but never  
(cid:88)  
at the same time.  
b)* Briefly explain the principle of frequency multiplexing.  
1/2  
To make a channel efficiently usable by multiple participants, the channel is divided into different frequency bands (spectral decomposition) and these frequency bands are assigned to communication partners.  
1 c)* Name two header fields and the corresponding header that a router must modify when forwarding packets.  
(cid:88) (cid:88)  
Source MAC address of the Ethernet header, Destination MAC address of the Ethernet header, TTL of the IP  
(cid:88)  
Headers  
If a packet is fragmented by the router:  
(cid:88) (cid:88)  
The More Fragments flag in the IP header, The Fragment Offset in the IP header  
(The last two points require the note that the router itself fragments)  
d)* How many TCP connections can a client have open to the same server at the same time if both the client and server have only one IP address?  
Since the port number is a long field, the maximum number of connections per IP address is  
16 bits  
(cid:88)  
limited to.  
2^16 = 65536  
(Assuming that the server expects incoming connections on multiple ports, the total number of connections increases to .)  
2^32  
e)* Briefly explain the difference between a switch and a hub.  
1/2  
Hubs are merely amplifiers, while switches make forwarding decisions based on MAC addresses.  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013  
7 Name:  
f)* Provide the binary message with the help of the generator polynomial  
11000101101  
with a CRC checksum. Provide the message secured by CRC!  
g(x) = x^4 + x^2 + x + 1 1  
(cid:88)  
11000101101 0000 : 10111 = 11101101101, remainder 0011  
(cid:88)  
XOR of the padded message with the remainder yields .  
11000101101 0011  
(Detailed calculation see exercise/lecture)  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013  
Student ID Number: 8  
Additional space for solutions – please clearly mark the affiliation with the respective task and cross out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – Summer Semester 2013