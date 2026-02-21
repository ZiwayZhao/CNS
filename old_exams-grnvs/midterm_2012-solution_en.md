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
Diploma Preliminary Exam  
Bachelor Exam  
............................  
Consent for Grade Notification  
via Email / Internet  

Exam Subject: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle  
Date: 18.06.2012  
Lecture Hall: .................... Row: .................... Seat: .....................  
To be filled out by the supervisor only:  
Lecture hall exited from ...... : ...... to ...... : ......  
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

- This exam consists of 8 pages and a total of 3 tasks. Please check now that you have received a complete set of information.  
- Please write your name and student ID in the header of each page.  
- The total number of points is 15.  
- The following aids are permitted: a double-sided handwritten A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be counted where a solution path is recognizable. Text problems must generally be justified unless explicitly stated otherwise in the respective sub-task.  

### Task 1  
Waternet (5 points)  
Figure 1.1 shows a hypothetical network that uses water-filled pipes as a transmission medium instead of copper wires. The distributor V essentially consists of a water-filled sphere without further logic. For simplification, we assume that reflections play no role. The distance between PC1 and V is 20m, and the distance between PC3 and V is 10m. The distance between V and PC2 is so small that it can be neglected.  

```
V
PC1 PC3
20m PC2 10m
```
Figure 1.1: Waternet network consisting of 3 computers and a distributor.  
The speed of sound in water at 20°C is approximately 1500m/s. This technique, called Waternet, uses CSMA/CD as a medium access method, just like regular Ethernet. The transmission rate is r = 1MBit/s.  

a)* What device corresponds to the distributor V in a regular Ethernet?  
Hub  

At time t = 0ms, PC1 starts transmitting a frame of 1500Bytes.  

b)* Determine the serialization time.  
```
ts = l / r = (1500 * 8Bit) / (1 * 10^6 Bit/s) = 12ms
```  

c)* Determine the propagation delay between PC1 and PC3.  
```
tp = d(PC1,PC3) / c = (20m + 10m) / 1500m/s = 20ms
```  

At time t = 15ms, there are also 1500Bytes of data ready to send at PC2 and PC3.  

d) Draw a time-distance diagram that represents all processes from the time t0 = 0ms. If one of the computers sends a jam signal, it is sufficient to indicate its start time. Do not forget to label the diagram correctly!  
(Scale: horizontal (1cm = 2.5m), vertical (1cm = 10ms))  

```
PC1 PC2 PC3
t = 0ms
t = 15ms
Frame from PC1 Frame from PC3
No Frame from PC2 Jam Signal
```  

e) Justify why CSMA/CD does not work correctly under the given circumstances.  
PC1 does not detect the collision because the transmission is already completed when the first bit from PC3 arrives at it.  

f) Suggest a modification so that CSMA/CD works correctly. (Calculation!)  
```
l_min = 2 * t_max = 2 * 20ms * 10^6Bit/s = 5000Bytes or
d_max = c * t_min = 1500m/s * 12ms = 9m
```  

### Task 2  
Digital Modulation Techniques (4 points)  
In this task, the processes of pulse shaping in baseband and the subsequent modulation are to be worked out. Figure 2.1 shows the signal space of a digital modulation method. Additionally, the bit sequence to be transmitted is given. The rectangular pulse is to be used as the basic pulse for the baseband signal.  

```
rect(t) = { 1, -T/2 < t < T/2; 0, otherwise }
```

a)* What modulation method is being used?  
4-ASK  

b)* Enter a valid assignment of codewords to symbols in Figure 2.1a.  

c)* Draw the basic pulse in Figure 2.1b.  

d) Now draw the corresponding baseband signal for the given bit sequence in Figure 2.2.  
The baseband signal from the previous sub-task will now be used to modulate the cosine carrier.  
```
s(t) = cos(2πt/T)
```  

e) Also draw the modulated signal in Figure 2.2.  

### Task 3  
Short Tasks (6 points)  
The following short tasks are independent of each other. Bullet-point answers are sufficient!  

a)* Figure 3.1 shows measured RTTs from two different computers A and B to the same destination. Computer A is connected to the Internet via a broadband connection, while Computer B has a UMTS connection. Justify which of the two measurements was taken from Computer B.  
Measurement 2 shows a significantly higher RTT with greater variance. This indicates that Measurement 2 comes from Computer B.  

b)* In Programming Task 1, we found that Hamming codes are susceptible to multiple bit errors (especially burst errors). Briefly explain whether this susceptibility can be reduced through permutations.  
If the encoded bit stream is permuted, the probability that multiple bits of the same codeword are flipped by a burst error decreases. In other words, the goal is to spread a burst error over multiple blocks so that there is at most 1 bit error within each block.  

c)* What is the goal of channel coding?  
Purposeful addition of redundancy (error correction)  

d)* What is the goal of source coding?  
Removal of redundancy from a data stream (compression)  

e)* Given the address block 131.159.20.64/26. Provide the network address, broadcast address, and number of usable addresses for hosts.  
- Network address: 131.159.20.64  
- Broadcast address: 131.159.20.127  
- Usable addresses: 64 - 2 = 62  

f)* You receive the binary message 1011101101, which was secured using CRC. The generator polynomial is g(x) = x^3 + 1. Check whether an error occurred during transmission.  
The generator polynomial in binary notation:  
```
1001  
1011101101 : 1001 = 1010111, remainder 010
```  
Correct remainder + conclusion  

g)* Given the data block shown in the solution field (L4-PDU). Add header/trailer schematically if IP is used over Ethernet. Detailed information on individual fields within the header is not necessary!  
```
MAC-Hdr IP-Hdr Data FCS/CRC
```  

h)* Given the network topology from the solution field. Draw all broadcast and collision domains.  

```
CD
CD
Switch Router Hub
CD
BD BD = CD
```  

i)* You transmit a signal in baseband with the (one-sided) bandwidth B = 1kHz. The chosen modulation method uses 16 different signal levels. The SNR at the receiver is approximately 6dB. Determine the maximum achievable data rate.  
```
R_max = 2B * log2(M) = 8000Bit/s  
R = B * log2(1 + SNR) = 2316Bit/s  
=> R = min(R_max, R) = 2316Bit/s
```  

j)* What are MAC addresses used for?  
Identification of the next hop.  

k)* What are IP addresses used for?  
End-to-end addressing.  

Additional space for solutions – please clearly mark the affiliation with the respective task and cross out invalid solutions!