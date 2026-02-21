Name First Name  
..................  
Grade  
Degree Program (Major) Specialization (Minor)  
I II  
Student ID  
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
Consent to Release Grades 8  
via E-Mail / Internet  
n  
9  
u  
10  
s  
Subject of Examination: Fundamentals of Computer Networks and Distributed Systems  
ö  
L  
Examiner: Prof. Dr.-Ing. Georg Carle Date: 06.06.2014 (cid:80)  
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
Friday, 06.06.2014  
16:30 – 17:15  
• This exam consists of 9 pages and a total of 3 tasks. Please check now that you have received a complete set of information.  
• Please write your name and student ID in the header of each page.  
• Do not write in red/green ink or with a pencil.  
• The total number of points is 15.  
• Allowed aids are a double-sided handwritten DIN A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
• Tasks marked with * can be solved without knowledge of the results of preceding sub-tasks.  
• Only results where a solution path is recognizable will be graded. Text problems must be justified unless explicitly stated otherwise in the respective sub-task.  

1 Name:  
Task 1  
Quantization and Noise (5 points)  
5  
In this task, a temperature curve is to be digitized and the influence of noise on signals is to be investigated. Temperatures in the range of -40°C to 70°C will be considered. The measured values should be linearly mapped, with a minimum step size of 0.5°C to be achieved.  
a)* Explain the difference between sampling and quantization. 1  
(cid:88)  
Sampling is the discretization of a continuous signal in the time domain without rounding.  
(cid:88)  
Quantization is the discretization of a signal into signal levels, i.e., in the value range with rounding.  
b)* How many bits are minimally required for the digitization of a single temperature value?  
1/2  
Justify your answer.  
In the range -40°C to 70°C with a resolution of 0.5°C, different signal levels are required.  
220  
7 bits only allow for 128 levels.  
27 = 128  
(cid:88)  
The next higher number is 256 different signal levels; therefore, 8 bits are needed.  
8  
(cid:100) (cid:101) (cid:88)  
or  
log (220)bit = 8bit  
2  
c) What step size can now be determined for the temperature based on the number of bits used according to sub-task b)?  
1/2  
≈ (cid:88)  
For 110° at 256 different signal levels, a precision of 110° ± 0.43° results.  
256  
d) Determine the maximum quantization error regarding the calculated step size from  
1/2  
Task c), assuming that mathematical rounding is used.  
· ≈ (cid:88)  
0.43°  
1.0°  
2  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 2  
The used baseband signal uses exactly one symbol for each temperature level. A channel capacity of 10 kbit/s is to be achieved.  
1 e) Determine the minimum required bandwidth in a noise-free channel if the specified channel capacity is to be achieved.  
Signal Levels  
M = 2N = 28 = 256  
· · (cid:88)  
C = 2 B log (M)  
H · ·2  
10 kbit = 2 B 8  
s (cid:88)  
B = 625Hz  
Now assume that the temperature values are transmitted with a bandwidth of.  
B = 750Hz  
f)* To what value would the channel capacity decrease at the same bandwidth if a signal-to-noise ratio of 35dB were assumed?  
·  
35 = 10 log(X)  
,  
X = 3162 28  
· (cid:88)  
SNR  
C = B log (1+ )  
S 2· ≈ (cid:88)  
,  
C = 750Hz log (3162 28+1) 8720 bit  
S 2 s  
g)* Justify why the channel capacity increases with an increasing signal-to-noise ratio at constant bandwidth.  
More symbols become distinguishable, which leads to a higher channel capacity.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
3 Name:  
Task 2  
Optical Telegraph (5 points)  
5  
In this task, we consider an optical telegraph. The distance between two neighboring telegraph stations is 15 km. The mast of such a station (see Fig. ??) has three wings on the left and right, each of which can take on four different positions (|, (cid:31), — and (cid:30)).  
A symbol is the configuration of all wings.  
For setting a symbol, 10 seconds are needed. Reading at the receiver occurs in parallel and therefore requires no additional time.  
Figure 2.1: Optical Telegraph  
a)* How many bits can be transmitted with each symbol?  
1/2  
(cid:88)  
Symbols: , Bits:  
46 = 4096 N = log 4096 = 12  
2  
b) Determine the achieved data rate in (Bytes per second).  
B  
s 1/2  
r = N· B  
8,10 s (cid:88)  
r = 0 15 B  
s  
c)* The available data rate is usually not fully used for user data. Name two other sensible tasks that typically consume part of the data rate in common systems.  
(cid:88)  
• Control symbols (Start of Frame, End of Frame, Jam Signal)  
(cid:88)  
• 5/4 Code: Clock recovery  
(cid:88)  
• Error detection (Checksum) / Error correction  
(cid:88)  
• Header information (Addressing)  
(cid:88)  
• Padding  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 4  
A message of length 72B is to be transmitted.  
d) Calculate the required serialization time for this message.  
1/2  
(cid:88)  
72B = 72B = 480s  
r 0.15B  
s  
e)* Calculate the propagation delay of this message between two stations. The reduction of the speed of light ( ) through air can be neglected here.  
3 10^8 m  
s  
(cid:88)  
, d = 15000m = 0 05ms  
vc 300000000m  
s  
Now we consider a chain of a total of 4 telegraph stations, which are each 15 km apart.  
f)* This message of length 72B is to be transmitted using packet switching. The protocol used at layer 2 can only transmit frames up to a size of 36B inclusive. How many packets must the message be split into if each packet must have a header of 4B added?  
−  
p = 36B 4B = 32B  
(cid:100)max (cid:101) (cid:100) (cid:101) (cid:88)  
L = 72B = 3  
pmax 32B  
1 g) Calculate the duration of a complete packet-based transmission of the message across the entire telegraph chain. Assume that the transmissions are always successful and thus no acknowledgments are needed.  
· · (cid:88)  
T = 1 L L +L + d +n Lh+pmax  
|APnVnumber of telegraph stations| νc r  
= n = 2  
· ·  
T = 1 (3 4+72)+ 45km +2 4+32  
PV 0,15B c 0,(cid:88)15B  
, s , s  
560s+0 15ms+480s = 1040 00015s  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
5 Name:  
h) By how much does the duration differ in a continuous message forwarding scenario? Assume that no header is used in message forwarding.  
1/2  
Each station must fully receive the message before it can forward the message.  
∗  
Total distance:  
d = 3 15km = 45km  
∗  
T = (n+1) t +t  
NV ∗ s p,total  
, ,  
(2+1) 480s+0 15ms = 1440 00015s  
− (cid:88)  
Message forwarding would be approximately , , slower.  
1440 00015s 1040 00015s = 400s  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 6  
Task 3  
Short Tasks (5 points)  
5 The following short tasks are independent of each other. Bullet-point answers are sufficient!  
a)* Determine the entropy of a memoryless binary source that emits a 0 with a probability of 30%.  
1  
· · (cid:88)  
H = 0 3 log (0 3)+0 7 log (0 7)  
2(cid:88) 2  
,  
H = 0 88bit  
b)* Distinguish between the terms symbol and signal.  
1/2  
Signals are time-dependent and measurable physical quantities.  
Defined measurable signal changes can be assigned a symbol.  
c)* What type of multiplexing is used in the multiple access method CSMA/CD?  
1/2  
Time Division Multiplexing / Time Division Multiple Access  
d)* Name two evaluation criteria for media access methods.  
1/2  
Throughput, Delay, Fairness, Implementation effort  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
7 Name:  
e)* A possible generator polynomial for the CRC algorithm is:  
g(x) = x32+x26+x23+x22+x16+x12+x11+x10+x8+x7+x5+x4+x2+x+1  
1/2  
What advantage does the choice of this relatively long polynomial have?  
• Due to the large length, correspondingly long burst errors are also detected or  
• There are, relatively, few errors that represent a multiple of the generator polynomial.  
f)* Provide the binary message 111010 with a CRC checksum using the generator polynomial.  
1  
g(x) = x4+x+1  
(cid:88)  
111010 0000 : 10011 = 111110, remainder 0010  
(cid:88)  
XOR of the padded message with the remainder results in.  
1110100010  
(Detailed calculation see exercise / lecture)  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
Student ID: 8  
g)* We consider a wireless connection between two nodes according to IEEE802.11n. The gross data rate (data rate while a frame is transmitted) is 300 Mbit. A frame has a total length of 2000B. Due to media access and the physical layer, there is an overhead of 142µs for each transmitted frame. Determine the effectively achievable data rate in Mbit.  
s  
2000B (cid:88) ≈ Mbit(cid:88)  
r = 82  
µ  
142 s+ 2000B s  
300Mbit  
s  
Additional space for solutions – please clearly mark the association with the respective task and cross out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
9 Name:  
Additional space for solutions – please clearly mark the association with the respective task and cross out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014