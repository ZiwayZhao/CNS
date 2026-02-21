Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during attendance control by sticking a code.
- This only contains a continuous number, which is also noted on the attendance list next to the signature field.  
- Stick the code with SRID here.  
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Midterm  
Date: Friday, June 14, 2019  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 17:30–18:15  

### Instructions for Processing
- This exam consists of 8 pages with a total of 4 tasks.
- Please check now that you have received a complete set of instructions.
- The total score for this exam is 45 points.
- It is prohibited to tear out pages from the exam.
- The following aids are permitted:
  - The formula collection accompanying the instructions (Cheatsheet)
  - A non-programmable calculator
  - An analog dictionary in your native language without annotations
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be counted where the solution method is recognizable. Text problems must also be justified unless explicitly stated otherwise in the respective task.
- Do not write with red/green colors or with pencil.
- Turn off all electronic devices you carry completely, store them in your bag, and close it.

---

### Task 1  
Short Tasks (10 Points)  
The following sub-tasks can each be solved independently of one another.  

a) *What is meant by ARP Spoofing?*  
- Malicious redirection of data traffic at layer 2 by sending forged ARP replies.  

b) *What is the purpose of the Identification field in the IPv4 header?*  
- For reassembly of fragments of a packet.  

c) *Given a memoryless source Q that emits symbols. How should the occurrence probability of the symbols be chosen so that the entropy of the source is maximized (without justification)?*  
- Uniformly distributed with occurrence probability 1/n.  

d) *Briefly explain the difference between ASK and PSK.*  
- In ASK, only the amplitude is modulated, while in PSK, the phase is modulated.  

e) *The channel capacities according to Shannon and Hartley yield different values. Briefly explain which external factors are considered in each case.*  
- Shannon only considers (additive, white) noise in relation to the signal power, but not quantization errors that arise from signal levels.  
- Hartley only considers signal levels and thus quantization noise, but no channel influences. Both consider the respective channel bandwidth.  

f) *Name two ways in which frame boundaries can be recognized (without justification).*  
- Code rule violation, length specification in the header, control characters.  

g) *Describe the difference between N-SDU and N-PDU.*  
- N refers to the N-th layer of the ISO/OSI model. The SDU is, from the perspective of this layer, the payload (or the (N+1)-PDU). The PDU is the SDU supplemented with header information of layer N.  

---

### Task 2  
CRC (7 Points)  
We consider CRC in IEEE 802.15.1 (Bluetooth). Here, the reduction polynomial r(x) = x^5 + x^4 + x^2 + 1 is used. This is not an irreducible reduction polynomial.  

a) *Briefly explain what an irreducible reduction polynomial is.*  
- An irreducible polynomial of degree n cannot be expressed as a product of two polynomials of degree < n.  

b) Given the data block 0000011011 consisting of 10 bits, which is to be secured using r(x).  
*Determine the secured data block (data including checksum).*  
- 0000011011 00000 : 110101 = 0000010001  
- 11010 1  
-------  
- 00001 10000  
- 1 10101  
-------  
- 0 00101  
⇒  
- Remainder: 00101  
⇒  
- Secured data block: 0000011011 00101  

c) *Briefly describe how a receiver can detect a transmission error.*  
- Modulo division of the received message (m(x) + c(x) + e(x)) mod r(x). If the remainder is not zero, a transmission error has occurred.  

d) *Name an error pattern that cannot be detected by CRC.*  
- All multiples of r(x).  

---

### Task 3  
Data Link Layer (14 Points)  
Given the network topology known from the lecture in Figure 3.1. We assume that initially all caches are empty (both ARP tables of the clients and the switching table of S). However, the two wireless clients (connected via IEEE 802.11n) are already associated with the AP.  

**Figure 3.1: Network Topology**  
Note: The MAC addresses of all stations in Figure 3.1 can be abbreviated by stating the name, e.g., PC1 for the MAC address of PC1.  

a) *Briefly justify whether S needs a MAC address for its normal functions in the network.*  
- No, a switch makes forwarding decisions based on MAC addresses but is not addressed itself.  

b) *Briefly justify whether the AP needs a MAC address for its normal functions in the network.*  
- Yes, the AP is directly addressed within the wireless network.  

c) *What does the first frame sent by PC1 contain (without justification)?*  
- ARP Request  

d) *Provide the Source Address (SA) and Destination Address (DA) of this frame in sections 1 and 2.*  
- SA: PC1 DA: ff:ff:ff:ff:ff:ff  

e) *Directly indicate in Figure 3.1 all entries that are created in the switching table of S by this frame.*  

IEEE 802.11 recognizes up to four MAC addresses for data frames with the following meanings:  
- Source Address (SA)  
- Destination Address (DA)  
- Transmitter Address (TA)  
- Receiver Address (RA)  

In infrastructure mode, data frames have three MAC addresses, depending on the direction in which a frame is sent, two addresses are identical. Thus, in this case, one address has two different meanings.  

f) *Provide for the frame in section 3 from the AP towards the wireless clients all three addresses and the meaning of the third address.*  
- TA: AP RA: ff:ff:ff:ff:ff:ff = DA  
- SA: PC1  

g) *Provide for the response from NB1 to PC1 in section 3 all three addresses and the meaning of the third address.*  
- TA: NB1 = SA  
- RA: AP DA: PC1  

h) *Mark in the solutions of sub-tasks f) and g) each address that has a double meaning.*  

i) *Briefly explain how the meaning of the individual address fields in the header is determined.*  
Note: It is sufficient to explain the underlying principle.  
- In the header, there is a field (Frame Control) in which two bits (FromDS and ToDS) encode the meaning.  

j) *Provide the MAC addresses for the response to PC1 in section 2.*  
- SA: NB1 DA: PC1  

k) *Provide all entries directly in Figure 3.1 that are created in the switching table of S by this response to PC1.*  

---

### Task 4  
Multiple Choice (14 Points)  
Please mark the correct answers (×).  
Crosses can be marked by completing the fill-in.  
Struck-out answers can be marked anew by adjacent markings.  

The following sub-tasks can each be solved independently of one another and come from the accompanying quizzes of the lecture. The grading scheme also corresponds to that of the quizzes:  
- Tasks with only one correct answer are scored with 1 point for the correct answer and 0 points otherwise.  
- Tasks with more than one correct answer are scored with 1 point for a completely correct answer, 0.5 points for a missing or incorrect answer, and 0 points otherwise.  

a) *Given the rectangular pulse (t) and the cosine^2 pulse (t). The figure below shows four different spectra. Which statements are correct?*  

b) *Given a signal s(t) with power P = 100 mW and a noise power of P = 10 mW. What is the signal-to-noise ratio in this case?*  
- 10 dB  

c) *A value-continuous signal is to be quantized in the interval I = [-2;2] so that the maximum quantization error within I is at most 1/2. How many quantization levels are required at a minimum?*  
- 6  

d) *What modulation method does the adjacent signal space assignment represent?*  
- 2-PSK  

e) *Cross out the matrix that represents the adjacency matrix for the adjacent network according to the lecture.*  

f) *Given the distance matrix D for the adjacent network. For which minimum n does Dn = Dn+1 hold?*  
- n = 4  

g) *Given the binary message 10101010 00000000 in Little Endian. What is it in Network Byte Order?*  
- 0x00 0x55 0x00 0xaa  

h) *How many broadcast domains does the adjacent network consist of?*  
- 2  

i) *How many collision domains does the adjacent network consist of?*  
- 4  

j) *What is the essential difference between CSMA/CD and CSMA/CA?*  
- There are only differences in collision handling, not in media access. CSMA/CA requires a minimum frame length of 64B.  

k) *Which statements about Manchester codes are correct?*  
- Automatic clock recovery, always DC-free  

l) *Given a baseband signal with 16 distinguishable symbols and a transmission channel with a bandwidth of 1 MHz and an SNR of 7. Determine the achievable data rate.*  
- 4 Mbit/s  

m) *The serialization time...*  
- is the quotient of frame length and data rate.  

n) *The propagation delay...*  
- is independent of the frame length.  

### Additional Space for Solutions  
Please clearly mark the assignment to the respective sub-task.  
Do not forget to strike out invalid solutions.