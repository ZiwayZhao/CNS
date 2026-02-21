Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized during the attendance check by attaching a code sticker.  
- This contains only a continuous number, which is also noted on the attendance sticker with SRID here.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Midterm  
Date: Friday, June 10, 2022  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 18:15–19:00  

**Instructions for Completion:**  
- This exam consists of 8 pages with a total of 4 tasks as well as a formula collection (cheat sheet). Please check now that you have received a complete set of information.  
- The total score for this exam is 45 points.  
- The removal of pages from the exam is prohibited.  
- The following aids are permitted:  
  - A non-programmable pocket calculator  
  - An analog dictionary German ↔ native language without notes  
  - The cheat sheet distributed with this exam  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.  

**Task 1**  
Multiple Choice (13 Points)  
The following tasks are multiple choice/multiple answer, meaning that there is at least one correct answer option for each. Sub-tasks with only one correct answer are awarded 1 point if correct. Sub-tasks with more than one correct answer are awarded 1 point for each correct answer and -1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

**Mark the correct answers:**  
- Answers can be crossed out by filling them completely.  
- Crossed-out answers can be marked next to them to be re-crossed.  

a) *Given are the rectangular impulse s1(t) and the cos2 impulse s2(t) from the lecture. The figure below shows four different spectra. Which statements are correct?*  

(b) Sa(f) (c) Sb(f) (d) Sc(f) (e) Sd(f)  

1. a 1. d 1. b 1. c  
2. d 2. c 2. b 2. a  

b) *Given is the time signal below, which is to be developed as a Fourier series.*  
s(t)  
```
π
n
u
t
−3π −2π −π π 2π 3π
```
Which statements about the Fourier coefficients are correct?  
- a0 ≠ 0  
- bk ≠ 0  
- ak > 0 ≠ 0  
- ak > 0 = 0  
- bk = 0  
- a0 = 0  

c) *Given is a baseband signal with 16 distinguishable symbols as well as a transmission channel with a bandwidth of 1 MHz and an SNR of 7. Determine the achievable data rate.*  
- 5 Mbit/s  
- 3 Mbit/s  
- 7 Mbit/s  
- 4 Mbit/s  
- 8 Mbit/s  
- 6 Mbit/s  

d) *Mark all code words that have a Hamming distance of three or more from the code word 0011.*  
- 1111  
- 0001  
- 0000  
- 1110  
- 1001  
- 1100  

e) *A value-continuous signal is to be quantized in the interval I = [-3;3] so that the quantization error within I is at most 0.4. How many quantization levels are required at a minimum?*  
- 8  
- 10  
- 12  
- more  
- 2  
- 6  
- 4  

f) *Cross out the matrix that represents the adjacency matrix for the network next to it according to the lecture.*  
```
1
     
     
1 −1 0 0 0  0 1 1 0 0 1 1 0 0 0
     
1 0 −1 0 0 × 1 0 1 0 0 1 0 1 0 0
0 1 −1 0 0 1 1 0 1 0 0 1 1 0 0  
1
0 0 1 −1 0 0 0 1 0 1 0 0 1 1 0  
3
0 0 0 1 −1 0 0 0 1 0 0 0 0 1 1  
```

g) *Given is the distance matrix D for the network next to it. For which minimal n does Dn = Dn+1 hold?*  
- n = 5  
- n = 4  
- n = 2  
- n = 7  
- n = 1  
- n = 6  
- n = 0  
- n = 3  

h) *How many broadcast domains does the network next to it consist of?*  
- 4  
- 3  
- 2  
- 1  
- 6  
- 5  

i) *How many collision domains does the network next to it consist of?*  
- 5  
- 6  
- 1  
- 3  
- 2  
- 4  

**Task 2**  
Short Tasks (5 Points)  
a) *Why are usually three MAC addresses used in IEEE 802.11 (WLAN), but only two MAC addresses in IEEE 802.3 (Ethernet)?*  
Because the AP for WLAN clients is not transparent, meaning it must be explicitly addressed as an intermediate station between sender and receiver. Switches, on the other hand, are transparent.  

b) *Briefly describe the essential difference between CSMA/CD and CSMA/CA.*  
CSMA/CA randomizes media access even in free medium (fixed contention window with optional backoff interval), while CSMA/CD only does so after a collision has occurred. Alternatively: Because CSMA/CA cannot reliably detect collisions, acknowledgments are expected at layer 2. In contrast, a frame is considered successfully transmitted in CSMA/CD if no collision was detected during transmission.  

c) *Briefly describe the essential difference between a hub and a switch.*  
Switches forward frames over the port to which the receiver is connected (if an entry is available in the switching table). Hubs forward frames to all ports, regardless of where the frame was received.  

d) *What is meant by source coding?*  
The removal of unwanted redundancy from the data to be sent. (Lossless compression)  

e) *What is meant by channel coding?*  
Deliberate addition of redundancy for later detection and correction of transmission errors.  

**Task 3**  
CRC (11 Points)  
We consider CRC with the (binary) generator polynomial r(x) = x^4 + x^2.  

a) *Show that r(x) is irreducible.*  
No, since x^4 + x^2 = (x^2 + 1)·x^2 = (x + 1)^2·x^2 holds.  

b) *Why can it make sense in the context of CRCs to choose a non-irreducible generator polynomial?*  
The choice of the polynomial has a direct influence on which types of errors can be detected. The properties of a finite field, on the other hand, are not a prerequisite for error detection. The chosen polynomial is, for example, divisible by x + 1, which means it detects all even-numbered error bursts.  

Now we consider the binary message m(x) = x^7 + x^4 + x + 1, which is to be secured with CRC and r(x).  

c) *Determine the checksum.*  
```
10010011 0000 : 10100
```
```
10100||| ||||
3 0011001| ||||  
10100| ||||
011011 ||||
10100 ||||  
01111 0|||
1010 0|||
0101 00u||
101 00||
000 0000
```
⇒ 0000  

d) *Specify the message to be transmitted.*  
10010011 0000 (= m(x)·x^4)  

During transmission, an error e(x) = x^11 occurs.  

e) *Show that the error is detected.*  
The bit error affects the most significant bit of the transmitted message. Therefore, the receiver receives:  
```
00010011 0000  
```
```
00010011 0000 : 10100  
10100 ||||
00111 00||
101 00||
010 000|
10 100|  
00 1000  
```
The remainder is 10006 = 0000. Consequently, the error was detected.  

f) *What types of errors cannot be detected?*  
All multiples of the reduction polynomial.  

**Task 4**  
Crowning Transmission (16 Points)  
On June 2, 1953, Elizabeth II was officially crowned Queen of England. Since she is also the head of state of Canada, an attempt was made in the so-called Operation Pony Express to transmit film footage of this coronation to Canada with as little latency as possible.  

As part of Operation Pony Express by the British and Canadian broadcasting organizations BBC and CBC, the coronation was filmed in several parts. Each completed part could be quickly developed during the ceremony, flown by helicopter to London Airport, and from there flown to Montreal, Canada. This allowed the residents of Canada to watch the coronation on TV on the same day, a unique event for that time.  

a) The straight-line distance between London and Montreal is 5200 km. We assume that the entire film has a duration of 6 hours and is evenly divided into 6 parts. Even if this film was naturally sent as an analog film roll, we will compare it with an average video data rate of 3000 kbit/s for the film.  

t is the duration of one part of the film. Determine t.  
t = 6h / 6 = 1h = 3600s  

b) How much data in bytes does one part of the film contain?  
L_part = 3000 kbit/s · 3600 s = 10.8 Gbit = 1.35 GB  

c) How much data does the entire film contain?  
L_total = L_part · 6 = 1.35 GB · 6 = 8.1 GB  

For the following tasks, we assume that it takes 15 minutes after the film of a part is completely shot until the corresponding part is brought to the airport by helicopter and loaded onto the plane. The unloading and further transport to the TV studio in Montreal takes the same amount of time.  
The airplane flies at an average speed of 500 km/h.  

d) How much time passes until a part of the film arrives at the TV studio in Montreal after it has been completely shot?  
t_film = 5200 km / 500 km/h = 10.4 h  
t = t_film + t_shoot + t_transport = 10.4 h + 0.25 h + 0.25 h = 10.9 h  
(alternatively: t = t_film + t_shoot + t_transport + t_further_transport = 11.15 h)  

e) How much time passes from the beginning of the ceremony until the first part of the film arrives at the TV studio in Montreal?  
t = t_film + t_latency = 11.9 h  

f) How much time passes from the beginning of the ceremony until the last part of the film arrives at the TV studio in Montreal?  
t = 6h + t_latency = 16.9 h  

g) With what data rate (in kbit/s) does the transmission of the entire film take place?  
r_stream = L_total / t_total = 8.1 GB / 16.9 h ≈ 6640.88 kbit/s  

In today's time, events are filmed purely digitally. A live stream is often possible directly over the Internet. We now want to compare the streaming approach with the analog transmission.  
We assume that there is a direct physical fiber optic connection between London and Montreal. The data rate is 200 Mbit/s with a total frame length of 1518 B. UDP over IP over Ethernet is used as the transmission protocol. The corresponding headers are a total of 46 B long.  

h) *How many bytes of film data can a frame contain at maximum?*  
S_film_data = S_frame - S_header = 1518 B - 46 B = 1472 B  

i) *How many frames must the entire film be divided into?*  
L_total = 8.1 GB = 8.1 * 1024 * 1024 * 1024 B = 8,748,034,560 B  
Number of frames = L_total / S_film_data = 8,748,034,560 B / 1472 B ≈ 5,935,000 frames  

We assume that no processing time is required and recorded images can be sent immediately.  

j) *Specify the serialization time for one frame.*  
t_serialization = S_frame / r_frame = 1518 B / 200 Mbit/s = 60.72 µs (≈ 0.06 ms)  

k) *Specify the transmission time for one frame.*  
t_transmission = d / v_c = 5200 km / (2/3 * 3 * 10^8 m/s) = 0.026 s  
t_d_stream = t_serialization + t_transmission ≈ 26 ms + 0.06 ms ≈ 26.06 ms  

l) *How much faster could the residents of Canada have seen the transmission ceremony via live streaming? Give the result in seconds.*  
t_latency_film - t_latency_stream = t_0 + t_film - t_d_stream ≈ 42839.97 s  

**Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.**