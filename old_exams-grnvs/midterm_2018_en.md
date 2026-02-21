Chair of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  

### Personalization Notes:
- Your exam will be personalized by attaching a code during the attendance check.
- This code contains only a sequential number, which is also noted on the attendance list next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Midterm  
Date: Friday, June 8, 2018  
Examiner: Prof. Dr. Uwe Baumgarten  
Time: 16:30–17:15  

---

### Instructions for Processing
- This exam consists of:
  - 8 pages with a total of 4 tasks, as well as
  - a double-sided printed formula collection.
- Please check now that you have received a complete set of documents.
- The removal of pages from the exam is prohibited.
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be counted where the solution path is recognizable. Text problems must also be justified unless explicitly stated otherwise in the respective task.
- Do not write in red/green colors or with a pencil.
- The total score for this exam is 45 points, which will be scaled according to the bonus system.
- The following aids are allowed:
  - a non-programmable calculator
  - an analog dictionary German native language without annotations
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.

---

### Task 1  
Short Tasks (6 Points)  
The following sub-tasks are to be answered independently of each other.  
a) *What is the goal of source coding?  
b) *Given the address 172.16.121.71/18. Determine the corresponding network and broadcast address.  
   - Network address:  
   - Broadcast address:  
c) *Given a channel code with the mapping rule 0 → 00 and 1 → 11. The bit error probability of the transmission channel is 0 < p < 1. Show that the chance for a wrongly decoded channel word does not change compared to the unencoded transmission.  

---

### Task 2  
HF Trading and the Dilemma of Propagation Speed (7 Points)  
High-Frequency Trading (HF Trading) is a part of global stock trading. Here, short-term price differences between different trading venues are exploited.  
As reported by heise.de on April 1, 2018, the startup Shortwave Traders "has found a new way to reduce latency on the transatlantic route between Frankfurt and New York." In this task, the limits of the new method should be uncovered.  
The transatlantic route has a distance of about 6200 km. Traditionally, fiber optic cables are used for this route. The computers are connected to the Internet with 1 Gbit/s. We simplify by assuming packets of size 1500 B.  
a) *Determine the propagation delay on the transatlantic route over conventional fiber optic cables.  
b) Briefly justify why the serialization time at the interface between the continental and transatlantic sections probably plays no role.  
The startup attempts to reduce the propagation delay by using shortwave radio instead of conventional fiber optic cables, whose signals propagate at nearly the speed of light. However, since shortwave radio is not suitable for high data rates, the maximum data rate is reduced to 2.4 kbit/s.  
c) *Determine the propagation delay on the transatlantic route when using shortwave radio.  
d) Determine the frame size from which the method no longer offers an advantage over conventional fiber optic cables.  

---

### Task 3  
Hex Fun (19 Points)  
Figure 3.1 shows an Ethernet frame (including header but without FCS). This should be examined more closely.  
```
0x0000 f8 63 3f 16 e7 6b 40 4e 36 8a ae 37 86 dd 60 00  
0x0010 00 00 00 58 3a 2e 20 01 4c a0 20 01 00 00 00 00  
0x0020 00 00 00 00 00 01 2a 01 05 98 b8 82 59 76 b5 20  
0x0030 f0 68 70 07 04 f3 03 00 ...  
```  
**Figure 3.1:** Ethernet frame including header but without FCS  
**Note:** Use the accompanying cheatsheet for this task.  
If no justifications are provided for the following sub-tasks, they will be scored with 0 points.  
a) *Mark and name all fields of the Ethernet header directly in Figure 3.1.  
b) Which protocol is used at layer 3?  
   - Protocol:  
   - Justification:  
c) Mark the end of the layer 3 header in Figure 3.1.  
   - Justification:  
d) Provide the source and destination addresses of layer 3 in their usual and (if applicable) fully abbreviated form. Remember to make the source and destination addresses recognizable as such.  
   - Source:  
   - Destination:  
e) What follows after the layer 3 header?  
   - Protocol/Header:  
   - Justification:  
**Figure 3.2** shows an ICMPv6 message starting with the ICMPv6 header.  
```
0x0000 03 00 93 78 00 00 00 00 60 0c e6 67 00 28 3a 01  
0x0010 2a 01 05 98 b8 82 59 76 b5 20 f0 68 70 07 04 f3  
0x0020 2a 00 47 00 00 00 00 09 02 16 3e ff fe 4d 5e 04  
0x0030 80 00 3d 1e 62 3d 00 35 48 49 4a 4b 4c 4d 4e 4f  
0x0040 50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e 5f  
0x0050 60 61 62 63 64 65 66 67  
```  
**Figure 3.2:** ICMPv6 message  
f) *What type of ICMPv6 message is it in detail?  
   - Type of message:  
   - Justification:  
g) What does an ICMPv6 message like that from sub-task f) generally mean?  
h) Name a possible scenario in which ICMPv6 messages like those from sub-task f) are intentionally provoked. (No justification)  
i) Mark the end of the ICMPv6 header in Figure 3.2.  
   - Justification:  
j) What is generally the payload of such an ICMPv6 message?  

---

### Task 4  
Line Codes (13 Points)  
In this task, we consider the RZ basic pulse  
```
g(t) = { 1, for 0 ≤ t ≤ T/2  
          0, otherwise.  
```  
a) *Draw g(t) in the coordinate system. Pay attention to complete labeling!  
b) It should transmit the bit sequence 1100 1011. Provide the resulting baseband signal s(t). Note: There are two valid solutions.  
c) *Justify why a series expansion of g(t) using Fourier series is not possible.  
d) *Justify whether G(f) is exclusively real or imaginary or contains both real and imaginary parts.  
e) *Calculate the spectrum G(f).  

---

### Additional space for solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to cross out invalid solutions.