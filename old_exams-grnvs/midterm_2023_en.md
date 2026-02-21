Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be analyzed during attendance control by affixing a code persona sticker.  
- This contains only a continuous number, which is also noted on the attendance sticker with SRID to be affixed next to the signature field.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Midterm  
Date: Tuesday, June 6, 2023  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 19:00–19:45  

Before we proceed with reading the processing instructions, we ask you to answer the following questions. With this information, you help us to examine the learning success depending on individual lecture components. The information is voluntary and does not flow into the evaluation. To exclude any influence, this page will not be accessible during the correction.  

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
  - an analog dictionary in the native language without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be evaluated where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  
- Turn off all electronic devices you carry completely, store them in your bag, and close it.  

**Leaving the auditorium from until / Early submission by**  

---

**Task 1**  
Multiple Choice (9 Points)  
The following tasks are Multiple Choice/Multiple Answer, meaning there is at least one correct answer option for each. Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 1 point for each correct answer and 1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

Please mark the correct answers ■  
Marks can be crossed out by complete filling ×■  
Crossed-out answers can be marked again by adjacent markings  

a) Given are the signals from Figure 1.1 (a)–(d). Which of the signals are time discrete?  
(a) (b) (c) (d)  

b) *Given are the signals from Figure 1.1 (a)–(d). Which of the signals are value continuous?  
(a) (b) (c) (d)  

c) *What is the essential difference between CSMA/CD and CSMA/CA?  
There are only differences in collision handling, not in media access. In media access using CSMA/CA, there is always a contention phase.  
CSMA/CA requires a minimum frame length of 64 bytes. CSMA/CD, in contrast to CSMA/CA, uses acknowledgments.  

d) *Which character from the following character stream has the greatest information content?  
Y C B B Y C B Q R C Y Y R Z C R Q  
Z Y C R B Q  

e) *Which methods are suitable for recognizing frame boundaries?  
Indication of the L3 header length  
Code rule violation  
ALOHA  
Code transparency  
Checksums  
Slotted ALOHA  

f) *What properties exist in WLAN (IEEE 802.11a/g) compared to classical wired Ethernet (IEEE 802.3a/i/u)?  
Adapted Layer 3 protocols must be used.  
Acknowledgment procedures are used at Layer 2.  
Different numbers of MAC addresses in the header.  
There is no CRC checksum.  
Special cables are required.  
Transmission takes place using light waves.  
The MAC addresses are longer.  
CSMA is used for media allocation.  

---

**Task 2**  
Frequency Analysis (6 Points)  
Given is the periodic signal from Figure 2.1.  

a) *Briefly justify whether \( s(t) \) has a period – if yes, which?  

b) *Briefly justify whether a Fourier series can be used for frequency analysis.  

c) *Determine the spectrum of \( s(t) \).  

---

**Task 3**  
CRC (14 Points)  
Given is the binary message 00100110, which is to be secured using CRC (as introduced in the lecture for Ethernet-based networks). The reduction polynomial is given as \( r(x) = x^2 + 1 \).  

a) *Briefly describe what CRC is used for in Ethernet.  

b) *What is the purpose of the reduction polynomial?  

c) *What does it mean if a reduction polynomial is irreducible?  

d) *Justify whether an irreducible reduction polynomial is needed for CRC.  

e) *Show whether \( r(x) \) is irreducible.  

f) *How does the receiver react in Ethernet when a bit error is detected?  

g) *Determine the CRC checksum for the given message (see beginning of the task).  

h) *State the transmitted message explicitly.  
Assume another message (including checksum) is given: 111011010010111001. Assume that this message is transmitted and arrives at the receiver as 111011010010111100.  

i) *Justify whether the error is detected.  

---

**Task 4**  
Data Link Layer (16 Points)  
Figure 4.1 shows a Layer 2 topology with 4 PCs, along with their assigned MAC addresses. All caches and switching tables are empty at the beginning.  

PC1 PC3  
1 4  
a6:53:f1:06:25:16 a6:53:51:16:9e:a4  
S H  
3  
PC2 PC4  
2 5  
a6:53:b3:76:ef:a1 a6:53:01:d4:00:12  

a) *Briefly justify what MAC addresses are used for.  

b) *What is the fundamental difference between a switch and a hub?  

c) *What usually happens when a PC receives a frame that is not intended for it?  

d) *Briefly justify whether S needs a MAC address for its normal functions in the network.  

e) Draw all collision domains in Figure 4.1. Ensure it is clear which interface of the device is in which collision domain!  

PC1 now sends a frame to PC4.  

f) *Briefly justify whether PC4 has a globally unique MAC address.  

g) Justify for each of the links marked 1 to 5 in Figure 4.1 whether the frame is placed on the line during the process.  

h) *State the content of the switching table of S.  

PC4 now responds and addresses PC1 directly.  

i) Justify for each of the links marked 1 to 5 in Figure 4.1 whether the frame is placed on the line during the process.  

j) *Complete the content of the switching table of S.  

k) *What security problem arises in the example due to the use of hubs?  

---

**Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.**