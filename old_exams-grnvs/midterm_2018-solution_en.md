Chair of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  

### Personalization Notes:
- Your exam will be personalized by affixing a code during the attendance check.
- This code contains only a sequential number, which is also noted on the attendance lists next to the signature field.
- This will be used as a pseudonym to allow for a unique association of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Midterm  
Date: Friday, June 8, 2018  
Examiner: Prof. Dr. Uwe Baumgarten  
Time: 16:30–17:15  

### Instructions for Processing
- This exam consists of:
  - 8 pages with a total of 4 tasks, and
  - a double-sided formula collection.
- Please check now that you have received a complete set of documents.
- It is prohibited to detach pages from the exam.
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be counted where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective subtask.
- Do not write with red/green colors or with pencil.
- The total score for this exam is 45 points, which will be scaled according to the bonus system.
- Allowed aids:
  - a non-programmable calculator
  - an analog dictionary in the native language without annotations
- Please turn off all electronic devices you have with you completely, store them in your bag, and close it.

### Task 1  
Short Tasks (6 Points)  
The following subtasks are to be answered independently of each other.  

a) *What is the goal of source coding?  
**Answer:** Elimination of redundancy.  

b) *Given the address 172.16.121.71/18. Determine the associated network and broadcast address.  
**Network Address:** 172.16.64.0  
**Broadcast Address:** 172.16.127.255  

c) *Given a channel code with the mapping rule 00 and 11. The bit error probability of the transmission channel is 0 < p < 1. Show that the chance for a wrongly decoded channel word does not change compared to the uncoded transmission.  
**Answer:** The probability for a wrong code word during bitwise transmission is obviously p. In the given block code, it is certainly decoded incorrectly if two bit errors occur, and with a probability of 0.5 for a single bit error (rate probability), it results in:  
\[ p \cdot (1 - p)^2 + p^2 = p \]

### Task 2  
HF Trading and the Dilemma of Propagation Speed (7 Points)  
High-Frequency Trading (HF Trading) is a sector of global stock trading. It exploits short-term price differences between various trading venues. As reported by Heise.de on April 1, 2018, the startup Shortwave Traders "has found a new way to reduce latency on the transatlantic route between Frankfurt and New York." In this task, the limits of the new method should be uncovered.  
The transatlantic route covers a distance of approximately 6200 km. Traditionally, fiber optic cables are used for this route. The computers are connected to the Internet with 1 Gbit/s. We simplify by assuming packets of size 1500 bytes.

a) *Determine the propagation delay on the transatlantic route over conventional fiber optic cables.  
**Calculation:**  
\[ t = \frac{d}{v} = \frac{6200 \text{ km}}{(2/3) \cdot 3 \cdot 10^8 \text{ m/s}} = 31 \text{ ms} \]  

b) Briefly justify why the serialization time at the interface between the continental and transatlantic sections probably plays no role.  
**Answer:** The serialization time at 1 Gbit/s is just 1/2583 of the propagation delay over the entire route. Since the data rate at the relevant interface will not be orders of magnitude smaller (rather the opposite), it can thus be neglected.  

The startup attempts to reduce the propagation delay by using shortwave radio instead of conventional fiber optic cables, whose signals propagate nearly at the speed of light. However, since shortwave radio is not suitable for high data rates, the maximum data rate is reduced to 2.4 kbit/s.  

c) *Determine the propagation delay on the transatlantic route when using shortwave radio.  
**Calculation:**  
\[ t = \frac{d}{v} = \frac{6200 \text{ km}}{3 \cdot 10^8 \text{ m/s}} \approx 20.67 \text{ ms} \]  

d) *Determine the frame size from which the method no longer offers an advantage over conventional fiber optic cables.  
**Calculation:**  
\[ L^* = 31 \text{ ms} - 20.67 \text{ ms} \cdot 2400 \text{ bit/s} \]  
\[ L^* \approx 24.80 \text{ bit} \]  

### Task 3  
Hex Fun (19 Points)  
Figure 3.1 shows an Ethernet frame (including header but excluding FCS). This should be examined more closely.  

Receiver Address | Transmitter Address | Ethertype  
--- | --- | ---  
0x0000 f8 63 3f 16 e7 6b 40 4e 36 8a ae 37 86 dd 60 00  
IPv6 Source Address  
0x0010 00 00 00 58 3a 2e 20 01 4c a0 20 01 00 00 00 00  
IPv6 Destination Address  
0x0020 00 00 00 00 00 01 2a 01 05 98 b8 82 59 76 b5 20  
End of L3 Header  
0x0030 f0 68 70 07 04 f3 03 00 ...  

**Note:** Use the accompanying cheat sheet for this task.  
If no justifications are provided for the following subtasks, they will be graded with 0 points.

a) *Mark and name all fields of the Ethernet header directly in Figure 3.1.  

b) Which protocol is used at layer 3?  
**Protocol:** IPv6  
**Justification:** Ethertype 0x86dd  

c) Mark the end of the layer 3 header in Figure 3.1.  
**Justification:** The IPv6 header has a fixed length of 40 bytes.  

d) Provide the source and destination addresses of layer 3 in their usual and (if applicable) fully shortened notation. Remember to make the source and destination addresses recognizable as such.  
**Source:** 2001:4ca0:2001::1  
**Destination:** 2a01:598:b882:5976:b520:f068:7007:4f3  

e) What follows the layer 3 header?  
**Protocol/Header:** ICMPv6  
**Justification:** Next Header 0x3a  

Figure 3.2 shows an ICMPv6 message starting with the ICMPv6 header.  

End of ICMPv6 Header  
0x0000 03 00 93 78 00 00 00 00 60 0c e6 67 00 28 3a 01  
0x0010 2a 01 05 98 b8 82 59 76 b5 20 f0 68 70 07 04 f3  
0x0020 2a 00 47 00 00 00 00 09 02 16 3e ff fe 4d 5e 04  
0x0030 80 00 3d 1e 62 3d 00 35 48 49 4a 4b 4c 4d 4e 4f  
0x0040 50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e 5f  
0x0050 60 61 62 63 64 65 66 67  

f) *What type of ICMPv6 message is it in detail?  
**Type of Message:** Time Exceeded/Hop Limit Exceeded in Transit  
**Justification:** Type=0x3, Code=0  

g) What does an ICMPv6 message like from subtask f) generally mean?  
**Answer:** The hop limit (maximum number of hops from source to destination) was exceeded before the destination was reached. The packet was thus discarded by a router.  

h) Name a possible scenario in which ICMPv6 messages like from subtask f) are intentionally provoked. (No justification)  
**Answer:** Traceroute  

i) Mark the end of the ICMPv6 header in Figure 3.2.  
**Justification:** Time Exceeded has a fixed length of 8 bytes.  

j) What is generally the payload of such an ICMPv6 message?  
**Answer:** The IP header and the first 8 bytes of the subsequent payload of the packet that caused the timeout. (Alternatively according to RFC 4443: as much as possible from the triggering packet, without exceeding the minimum IPv6 MTU.)  

### Task 4  
Line Codes (13 Points)  
In this task, we consider the RZ basic impulse  
\[ g(t) = \begin{cases}  
A & \text{for } -T/2 \leq t < 0 \\  
0 & \text{otherwise.}  
\end{cases} \]  

a) *Draw \( g(t) \) in the coordinate system. Pay attention to complete labeling!  

b) The bit sequence 1100 1011 is to be transmitted. Provide the resulting baseband signal \( s(t) \). Note: There are two valid solutions.  

c) *Justify why a series expansion of \( g(t) \) using Fourier series is not possible.  
**Answer:** \( g(t) \) is not periodic; however, Fourier series can only represent periodic signals.  

d) *Justify whether \( G(f) \) is exclusively real or imaginary or contains both real and imaginary parts.  
**Answer:** \( g(t) \) is neither point nor axis symmetric, which is why \( G(f) \) must contain both real and imaginary parts.  

e) *Determine the spectrum \( G(f) \) mathematically.  
**Calculation:**  
\[ G(f) = \int_{-\infty}^{\infty} g(t)e^{j2\pi ft} dt \]  
\[ = \sqrt{A} \int_{-T/2}^{T/2} e^{j2\pi ft} dt \]  
\[ = \sqrt{A} \left[ \frac{\sin(2\pi fT/2)}{2\pi f} \right]_{-T/2}^{T/2} + j \left[ \frac{\cos(2\pi fT/2)}{2\pi f} \right]_{-T/2}^{T/2} \]  

### Additional Space for Solutions. Clearly mark the assignment to the respective subtask.  
Do not forget to cross out invalid solutions.