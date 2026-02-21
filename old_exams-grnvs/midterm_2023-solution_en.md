Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized during the attendance check by affixing a code sticker.  
- This contains only a continuous number, which is also noted on the attendance sticker with SRID here.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Midterm  
Date: Tuesday, June 6, 2023  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 19:00–19:45  

Before we proceed with reading the processing instructions, please answer the following questions. With this information, you help us to investigate the learning success depending on individual components of the lecture. The information is voluntary and does not flow into the evaluation. To exclude any influence, this page will not be accessible during or after correction.  

a) Did you attend the lecture?  
1 (regularly) 2 3 4 (never)  

b) Did you watch the recording from last year?  
1 (regularly) 2 3 4 (never)  

c) Did you attend the tutorial exercises?  
1 (regularly) 2 3 4 (never)  

**Processing Instructions**  
- This exam consists of 8 pages with a total of 4 tasks and the known cheat sheet. Please check now that you have received a complete set of information.  
- The total score for this exam is 45 points.  
- The tearing out of pages from the exam is prohibited.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - an analog dictionary (German native language) without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be evaluated where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  
- Turn off all electronic devices completely, store them in your bag, and close it.  

**Task 1**  
Multiple Choice (9 Points)  
The following tasks are multiple choice/multiple answer, meaning that at least one answer option is correct. Subtasks with only one correct answer are scored with 1 point if correct. Subtasks with more than one correct answer are scored with 1 point per correct answer and 1 point per incorrect check. Missing checks have no effect. The minimum score per subtask is 0 points.  

Please mark the correct answers:  
Marked answers can be crossed out by complete filling.  
Crossed-out answers can be marked again by adjacent markings.  

a) The signals from Figure 1.1 (a)–(d) are given. Which of the signals are time discrete?  
(a) (b) (c) (d)  

b) The signals from Figure 1.1 (a)–(d) are given. Which of the signals are value continuous?  
(a) (b) (c) (d)  

c) What is the essential difference between CSMA/CD and CSMA/CA?  
There are only differences in collision handling, not in media access.  
CSMA/CA always has a contention phase.  
CSMA/CD, in contrast to CSMA/CA, uses acknowledgments.  

d) Which character from the following character stream has the greatest information content?  
Y C B B Y C B Q R C Y Y R Z C R Q  
Z Y C R B Q  

e) Which methods are suitable for recognizing frame boundaries?  
L3 header length, code rule violation, ALOHA, code transparency, checksums, slotted ALOHA  

f) What properties exist in WLAN (IEEE 802.11a/g) compared to classic wired Ethernet (IEEE 802.3a/i/u)?  
Adapted Layer 3 protocols must be used.  
Acknowledgment procedures are used at Layer 2.  
Different numbers of MAC addresses in the header.  
Special cables are required.  
Transmission occurs via light waves.  
The MAC addresses are longer.  
CSMA is used for media allocation.  

**Task 2**  
Frequency Analysis (6 Points)  
The periodic signal from Figure 2.1 is given.  

a) Briefly justify whether s(t) has a period - if yes, which?  
Since s(t) is constant, the period duration T is not defined (f = 0).  

b) Briefly justify whether a Fourier series can be used for frequency analysis.  
If a constant signal is the boundary case of a periodic signal, which obviously only has a DC component, the Fourier series can be used.  

c) Determine the spectrum of s(t).  
Initially, all components are 0, s(t) is axis-symmetric (b = 0 k).  
The DC component a0/2 = A can be directly read as a0 = 2A.  
Alternatively, any period T can be chosen, and the integral can be solved.  

**Task 3**  
CRC (14 Points)  
The binary message 00100110 is given, which is to be secured using CRC (as introduced in the lecture for Ethernet-based networks). The reduction polynomial is given as r(x) = x^2 + 1.  

a) Briefly describe what CRC is used for in Ethernet.  
Detection of bit errors at the receiving node.  

b) What is the purpose of the reduction polynomial?  
Mapping a message of arbitrary length to a fixed-length checksum.  

c) What does it mean if a reduction polynomial is irreducible?  
It cannot be represented as the product of two polynomials of degree < deg(r(x)).  

d) Justify whether an irreducible reduction polynomial is needed for CRC.  
If an irreducible polynomial is used, all possible checksums will belong to a finite field. However, this property is not needed for CRC.  
Since CRC is primarily used for error detection, even a reducible polynomial can be advantageous, as it can reliably detect certain types of bit errors. For example, all odd-length bit errors are detected if the polynomial contains the factor (x + 1).  

e) Show whether r(x) is irreducible.  
r(x) = x^2 + 1 = (x + 1)^2, it is reducible.  

f) How does the receiver react in Ethernet when a bit error is detected?  
The frame is discarded without further action.  

g) Determine the CRC checksum for the given message (see beginning of the task).  
00100110 00 : 101 = 101101  
00111  
0100  
Checksum is 01.  

h) Explicitly state the transmitted message.  
00100110 01  
Assume that another message (including checksum) is given: 111011010010111001. Assume that this message is transmitted and received as 111011010010111100.  

i) Justify whether the error is detected.  
The error is not detected, as the error 101 is a multiple of the reduction polynomial.  

**Task 4**  
Data Link Layer (16 Points)  
Figure 4.1 shows a Layer 2 topology with 4 PCs, along with their assigned MAC addresses. All caches and switching tables are initially empty.  

a) Briefly justify what MAC addresses are used for.  
For addressing in a direct connection network.  

b) What is the fundamental difference between a switch and a hub?  
Hub: incoming frames are output to all other ports.  
Switch: manages a switching table and outputs frames only to the learned ports (if possible).  

c) What usually happens when a PC receives a frame that is not intended for it?  
The recipient address of the frame is not equal to the MAC address of the host, the host discards the frame.  

d) Briefly justify whether a switch needs a MAC address for its normal functions in the network.  
No, a switch makes forwarding decisions based on MAC addresses but is not addressed itself.  

e) Mark all collision domains in Figure 4.1. Ensure it is clear which interface of the device is in which collision domain!  

PC1 now sends a frame to PC4.  

f) Briefly justify whether PC4 has a globally unique MAC address.  
LG bit: 1 global non-unique address.  

g) Justify for each of the links marked 1 to 5 in Figure 4.1 whether the frame is placed on the line during the process.  
1 Yes (this is the only link to which PC1 is connected).  
2 - 3 Yes, as there is no corresponding entry in the switching table of S, the frame is output to all ports.  
4 - 5 Yes, as a hub outputs the frame to all ports.  

h) State the content of the switching table of S.  
PC1-1  
PC4 now responds and addresses directly back to PC1.  

i) Justify for each of the links marked 1 to 5 in Figure 4.1 whether the frame is placed on the line during the process.  
5 Yes (this is the only link to which PC4 is connected).  
3 and 4: Yes, as a hub outputs the frame to all ports.  
1 Yes, as there is a corresponding entry for PC1 in the switching table of S, it is forwarded only on this port.  
2 No, see above.  

j) Complete the content of the switching table of S.  
(PC1-1)  
PC4-3  

k) What security problem arises in the example due to the use of hubs?  
PC3 can eavesdrop on the communication between PC1 and PC4.  

**Additional space for solutions. Clearly mark the assignment to each subtask. Do not forget to cross out invalid solutions.**