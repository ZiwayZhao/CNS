Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be analyzed during attendance control by affixing a code persona sticker.  
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
- It is prohibited to tear pages from the exam.  
- The following aids are allowed:  
  - a non-programmable calculator  
  - an analog dictionary German ↔ native language without annotations  
  - the cheat sheet distributed with this exam  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be counted where the solution path is recognizable. Text tasks must be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.  

**Leave the lecture hall by / Early submission by**  

---  

**Task 1**  
Multiple Choice (13 points)  
The following tasks are multiple choice/multiple answer, meaning that at least one answer option is correct for each. Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 1 point for each correct answer and -1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

×  
Mark the correct answers  
(cid:4)  
Marks can be crossed out by complete filling  
×(cid:4)  
Crossed-out answers can be marked again by adjacent markings  

a)* Given are the rectangular impulse \( s(t) \) and the cosine squared impulse \( s(t) \) from the lecture. The figure below shows four different spectra. Which statements are correct?  
- (a) \( S_a(f) \)  
- (b) \( S_b(f) \)  
- (c) \( S_c(f) \)  
- (d) \( S_d(f) \)  

b)* Given is the time signal below, which is to be developed as a Fourier series.  
\( s(t) \)  
\[
\begin{array}{c}
\pi \\
t \\
-3\pi \quad -2\pi \quad -\pi \quad \pi \quad 2\pi \quad 3\pi
\end{array}
\]  
Which statements about the Fourier coefficients are correct?  
\( a_0 \neq 0 \quad b_k \neq 0 \quad a_k > 0 \quad a_k \neq 0 \quad b_k = 0 \quad a_0 = 0 \)  

c)* Given is a baseband signal with 16 distinguishable symbols and a transmission channel with a bandwidth of 1 MHz and an SNR of 7. Determine the achievable data rate.  
5 Mbit/s 3 Mbit/s 7 Mbit/s 4 Mbit/s 8 Mbit/s 6 Mbit/s  

d)* Mark all code words that have a Hamming distance of three or more from the code word 0011.  
1111 0001 0000 1110 1001 1100  

e)* A value-continuous signal is to be quantized in the interval \( I = [-3;3] \) such that the quantization error within \( I \) is at most 0.4. How many quantization levels are required at a minimum?  
8 10 12 more 2 6 4  

f)* Cross out the matrix that represents the adjacency matrix for the network next to it according to the lecture.  
\[
\begin{pmatrix}
1 & -1 & 0 & 0 & 0 \\
0 & 1 & 1 & 0 & 0 \\
1 & 1 & 0 & 0 & 0 \\
1 & 0 & -1 & 0 & 0 \\
1 & 0 & 1 & 0 & 0 \\
1 & 0 & 1 & 0 & 0 \\
0 & 1 & -1 & 0 & 0 \\
1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & -1 & 0 \\
0 & 0 & 0 & 1 & -1
\end{pmatrix}
\]  

g)* Given is the distance matrix \( D \) for the network next to it. For which minimal \( n \) does \( D_n = D_{n+1} \)?  
\( n = 5 \quad n = 4 \quad n = 2 \quad n = 7 \quad n = 1 \quad n = 6 \quad n = 0 \quad n = 3 \)  

h)* How many broadcast domains does the network next to it consist of?  
4 3 2 1 6 5  

i)* How many collision domains does the network next to it consist of?  
5 6 1 3 2 4  

---  

**Task 2**  
Short Tasks (5 points)  

a)* Why are usually three MAC addresses used in IEEE 802.11 (WLAN), but only two MAC addresses in IEEE 802.3 (Ethernet)?  

b)* Briefly describe the essential difference between CSMA/CD and CSMA/CA.  

c)* Briefly describe the essential difference between a hub and a switch.  

d)* What is meant by source coding?  

e)* What is meant by channel coding?  

---  

**Task 3**  
CRC (11 points)  
We consider CRC with the (binary) polynomial \( r(x) = x^4 + x^2 \).  

a)* Show whether \( r(x) \) is irreducible.  

b)* Why might it make sense in the context of CRCs to choose a non-irreducible polynomial?  

2  
We consider \( n \) and the binary message \( m(x) = x^7 + x^4 + x + 1 \), which is to be secured using CRC and \( r(x) \).  

c)* Determine the checksum.  

d)* Provide the message to be transmitted.  

During transmission, an error \( e(x) = x^{11} \) occurs.  

e)* Show that the error is detected.  

f)* What types of errors cannot be detected?  

---  

**Task 4**  
Crowning Transmission (16 points)  
On June 2, 1953, Elizabeth II was officially crowned as Queen of England. Since she is also the head of state of Canada, an attempt was made in the so-called Operation Pony Express to transmit film footage of this coronation to Canada with as little latency as possible.  

In the course of Operation Pony Express by the British and Canadian broadcasting corporations BBC and CBC, the coronation was filmed in several parts. Each completed part could be quickly developed during the ceremony, transported by helicopter to London Airport, and flown from there by plane to Montreal, Canada. This allowed the residents of Canada to see the coronation on TV the same day, a unique event for that time.  

The air distance between London and Montreal is 5200 km. We assume that the entire film has a duration of 6 hours and was evenly divided into 6 parts. Even though this film was of course sent as an analog film roll, we take an average video data rate of 3000 kbit/s for the film for comparison.  

a)* Let \( t \) be the playing time of a part of the film. Determine \( t \).  

b)* How much data in bytes does a part of the film contain?  

c)* How much data does the entire film contain?  

For the following tasks, we assume that it takes 15 minutes after the film of a part is completely shot until the corresponding part is brought to the airport by helicopter and loaded onto the plane. The unloading and further transport in Montreal to the TV studio takes the same amount of time. The plane flies at an average speed of 500 km/h.  

d)* How much time passes until a part of the film arrives at the TV studio in Montreal after it has been completely shot?  

e)* How much time passes from the beginning of the ceremony until the arrival of the first part of the film at the TV studio in Montreal?  

f)* How much time passes from the beginning of the ceremony until the arrival of the last part of the film at the TV studio in Montreal?  

g)* At what data rate (in kbit/s) does the transmission of the entire film take place?  

In today's time, events are filmed purely digitally. A live stream is often possible directly over the Internet. We now want to compare this streaming approach with the analog transmission.  

We assume that there is a direct physical fiber optic connection between London and Montreal. The data rate is 200 Mbit/s with a total frame length of 1518 B. UDP over IP over Ethernet is used as the transmission protocol. The corresponding headers together are 46 B long.  

h)* How many bytes of film data can a frame contain at maximum?  

i)* How many frames must the entire film be divided into?  

We assume that no processing time is required and that recorded images can be sent immediately.  

j)* Provide the serialization time \( t \) for a frame.  

k)* Provide the transmission time \( t \) for a frame.  

l)* How much faster could the residents of Canada have seen the transmission ceremony via live streaming? Provide the result in seconds.  

**Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.**