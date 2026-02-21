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
× Midterm Exam  
4  
Final Exam  
5  
Semester Exam  
Diploma Preliminary Exam  
6  
Bachelor Exam  
............................  
7  
Consent to Release of Grades  
8  
by E-mail / Internet  
9  
10  
Subject of Examination: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle Date: 06.06.2014  
Hearing Room: .................... Row: .................... Seat: .....................  
To be filled out only by the supervisor:  
Leave the hearing room from ...... : ...... to ...... : ......  
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
• The following aids are permitted: a double-sided handwritten DIN A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
• Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
• Only those results will be counted where a solution method is recognizable. Text problems must be justified unless explicitly stated otherwise in the respective sub-task.  

1 Name:  
Task 1  
Quantization and Noise (5 points)  
5  
In this task, a temperature curve is to be digitized, and the influence of noise on signals is to be examined. Temperatures in the range of −40°C to 70°C are to be considered. The measured values are to be mapped linearly, with a step size of at least 0.5°C to be achieved.  
a)* Explain the difference between sampling and quantization.  
1  
b)* How many bits are needed for the digitization of a single temperature value at a minimum?  
1/2  
Justify your answer.  
c) What step size can now be determined for the temperature based on the bit number used according to sub-task b)?  
1/2  
d) Determine the maximum quantization error regarding the calculated step size from task c), assuming that mathematical rounding is used.  
1/2  
The used baseband signal uses exactly one symbol for each temperature level. A channel capacity of 10 kbit/s is to be achieved.  
1 e) Determine the minimum required bandwidth for a noise-free channel if the specified channel capacity is to be achieved.  
Now assume that the temperature values are transmitted with a bandwidth of  
B = 750 Hz  
f)* To what value would the channel capacity drop at the same bandwidth if a signal-to-noise ratio of 35 dB is assumed?  
1  
g)* Justify why the channel capacity increases with a rising signal-to-noise ratio at constant bandwidth.  
1/2  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
3 Name:  
Task 2  
Optical Telegraph (5 points)  
5  
In this task, we consider an optical telegraph. The distance between two adjacent telegraph stations is 15 km. The mast of such a station (see Fig. ??) has three wings on the left and right, each of which can take on four different positions (|, (cid:31), — and (cid:30)).  
A symbol is the configuration of all wings.  
10 seconds are needed to set a symbol. Reading at the receiver occurs in parallel and therefore does not require additional time.  
Figure 2.1: Optical Telegraph  
a)* How many bits can be transmitted with each symbol?  
1/2  
b) Determine the achieved data rate in (Bytes per second).  
B/s  
1/2  
c)* The available data rate is usually not fully utilized for user data. Name two other reasonable tasks that typically consume part of the data rate in common systems.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
4  
Now a message of length 72 B is to be transmitted.  
d) Calculate the required serialization time for this message.  
1/2  
e)* Calculate the propagation delay of this message between two stations. The reduction of the speed of light ( ) through air can be neglected here.  
3 × 10^8 m/s  
We now consider a chain of a total of 4 telegraph stations, each 15 km apart.  
f)* This message of length 72 B is to be transmitted using packet switching. The protocol used at layer 2 can only transmit frames up to a size of 36 B inclusive. How many packets must the message be divided into if each packet must have a header of 4 B added?  
1  
g) Calculate the duration of a complete packet-based transmission of the message over the entire telegraph chain. Assume that the transmissions are always successful and therefore do not require confirmations.  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
5 Name:  
h) By how much does the duration differ in a continuous message transmission? Assume that no header is used in message transmission.  
1/2  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
6  
Task 3  
Short Tasks (5 points)  
5  
The following short tasks are independent of each other. Bullet-point answers are sufficient!  
a)* Determine the entropy of a memoryless binary source that emits a 0 with a probability of 30%.  
1  
b)* Distinguish between the terms symbol and signal.  
1/2  
c)* What type of multiplexing is used in the multiple access method CSMA/CD?  
1/2  
d)* Name two evaluation criteria for media access methods.  
1/2  

Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
7 Name:  
e)* A possible generator polynomial for the CRC algorithm is:  
g(x) = x^32 + x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + x^10 + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1  
1/2  
What advantage does the choice of this relatively long polynomial have?  
f)* Provide the binary message 111010 with a CRC checksum using the generator polynomial  
1  
g(x) = x^4 + x + 1  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
8  
g)* We consider a wireless connection between two nodes according to IEEE802.11n. The gross data rate (data rate while a frame is being transmitted) is 300 Mbit. A frame has a total length of 2000 B. Due to media access and the physical layer, there is an overhead of 142 µs for each transmitted frame. Determine the effectively achievable data rate in Mbit.  
s  

Additional space for solutions – please clearly mark the affiliation to the respective task and strike out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014  
9 Name:  
Additional space for solutions – please clearly mark the affiliation to the respective task and strike out invalid solutions!  
Fundamentals of Computer Networks and Distributed Systems – SoSe 2014