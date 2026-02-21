Name First Name  
..................  
Grade  
Degree Program (Major) Specialization (Minor)  
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
Consent to Release Grades  
by Email / Internet  

Subject of Examination: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle Date: 20.06.2013  
Room: .................... Row: .................... Seat: .....................  
To be filled out by the supervisor only:  
Room exited from ...... : ...... to ...... : ......  
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

- This exam consists of 8 pages and a total of 3 tasks. Please check now that you have received a complete set of documents.  
- Please write your name and student ID in the header of each page.  
- Do not write in red/green ink or with a pencil.  
- The total number of points is 15.  
- Allowed materials include a double-sided handwritten A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only results where a solution method is recognizable will be counted. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-task.  

1 Name:  
Task 1  
Voyager (5 Points)  

In 1977, the two space probes Voyager 1 & 2 were launched at intervals of just over a month (see Figure 1.1a). They were to explore the outer planets of our solar system for the first time. Both probes passed Jupiter in 1979 and about 18 months later Saturn. Voyager 1 has since been on a course out of our solar system and is currently at the boundary of interstellar space. Voyager 2, on the other hand, passed the two distant gas giants Uranus and Neptune and has also been on a course leading out of the solar system.  

(a) Schematic Representation (b) Flight Plan  
Figure 1.1: Schematic representation (a) and flight plan (b) of the Voyager 1 & 2 space probes  

On June 12, 2013, the two probes were at a distance of about 18,502,189,000 km (Voyager 1) and 15,136,706,000 km (Voyager 2) from Earth. Below, we will examine some of the challenges—then and now—regarding communication with the two space probes.  

a)* Determine the time between sending a signal to Voyager 1 until it arrives on Earth.  
1  
It is currently not fully clarified whether Voyager 1 has already left the so-called heliosphere and is thus in interstellar space.  
2  
http://voyager.jpl.nasa.gov/where/index.html  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2013  
Student ID: 2  
Data was Manchester encoded, using only two signal levels. Figure 1.2 shows an example of a short excerpt of such a signal that Voyager 1 sent to Earth.  

s(t)  
t  
Δt  
Figure 1.2: Manchester-encoded baseband signal from Voyager 1  

1/2 b)* Provide the transmitted bit sequence in the time domain Δt.  
Note: There are two valid solutions.  

The color images transmitted to Earth had a resolution of 800×800 pixels at 24 bits per pixel. The images were then sent back to Earth over a 360 kHz wide downlink in the range of 2295 MHz.  

1/2 c)* Determine the size of a single image in MB.  
To reduce the bit error rate to an acceptable level, the so-called Golay code was used as channel coding. This maps a block of 12 bits of payload data to a 24-bit long code word. Within such a code word, 3 arbitrary bit errors can be corrected.  

d)* Provide the code rate of the Golay code.  

1/2  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013  
3 Name:  
e)* Generally state the probability p for a block transmitted with errors.  

p,block  
Notes: You can simplify by assuming that bit errors occur independently and uniformly with probability p.  

By using the Golay code, images of Saturn could be transmitted at a payload data rate of 29 kbit/s with an average bit error rate of 5·10^-3.  

f) Determine the necessary time to send a single image towards Earth.  

1/2  
g)* Justify why the transmission of compressed images was not possible without further modifications.  

1/2  
h)* Determine the necessary SNR at the ground station in dB so that the given data rate can be achieved with a 360 kHz wide bandpass signal.  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2013  
Student ID: 4  
Task 2  
Slotted ALOHA (6 Points)  

In this task, we consider a transmission channel that operates using the multiple access method Slotted ALOHA. We assume that all stations transmit independently with the same transmission probability p. Furthermore, all messages are of constant size (transmission duration T per message). We further assume that the number of participating stations N is sufficiently large and the transmission probability p is small enough that the Poisson distribution can be used as an approximation for the binomial distribution. The probability density of the Poisson distribution is given by:  

P(X = k) = (λ^k * e^(-λ)) / k! (1)  

1 a)* During a measurement over a sufficiently long period, it was found that the transmission channel is unused 10% of the time. Determine the packet rate as a numerical value.  
For the remainder of the task, we assume that the network consists of a total of 50 stations.  

1 b) Now determine the transmission probability p of the stations as a numerical value.  

1 c) Now determine the probability p as a numerical value that a collision occurs.  

K  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013  
5 Name:  

1  
ALOHA  
)  
n Slotted ALOHA  
e  
n  
sio0.8  
olli  
K  
e0.6  
n  
h  
o  
(  
g  
un0.4  
t  
s  
a  
sl  
u  
a0.2  
al  
n  
a  
K  
0  
0 1 2 3 4 5 6 7 8 9 10  
Δ  
Figure 2.1: Channel utilization with ALOHA vs. Slotted ALOHA  

We now consider Figure 2.1, which illustrates the relationship between channel utilization and the number of stations ready to send in ALOHA and Slotted ALOHA.  

d)* Justify why the throughput is higher in Slotted ALOHA.  

1  
e)* Draw the utilization curve of an ideal multiple access method in Figure 2.1.  

1/2  
f) Provide a brief justification for your solution to part e).  

1/2  
g)* What problems can arise when using Slotted ALOHA if the time slots are chosen to be very large compared to the message length?  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2013  
Student ID: 6  
Task 3  
Short Tasks (4 Points)  

The following short tasks are independent of each other. Bullet-point answers are sufficient!  

a)* What does half-duplex mean in the context of message transmission?  

1/2  
b)* Briefly explain the principle of frequency multiplexing.  

1/2  
1 c)* Name two header fields and the corresponding header that a router must modify when forwarding packets.  

d)* How many TCP connections can a client maintain simultaneously to the same server if both client and server have only one IP address?  

1/2  
e)* Briefly explain the difference between a switch and a hub.  

1/2  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013  
7 Name:  
f)* Provide the binary message 11000101101 with a CRC checksum using the generator polynomial g(x) = x^4 + x^2 + x + 1. Give the message secured by CRC!  

1  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2013  
Student ID: 8  
Additional space for solutions – please clearly mark the association with the respective task and cross out invalid solutions!  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2013