Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by affixing a code during the attendance check.
- This contains only a sequential number, which is also noted in the attendance list next to the signature field.
- This will be used as a pseudonym to ensure a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Midterm  
Date: Tuesday, June 8, 2021  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 10:45–11:30  

Please sign the code of conduct in the upper right next to your sticker.  
Otherwise, your electronic exercise performance will not be counted!

### Instructions for Completion
- This exam consists of 8 pages with a total of 4 tasks.
- The total score for this exam is 46 points.
- The exam must be submitted completely, i.e., no missing or duplicate pages.
- The working time is 45 minutes. If you continue to work after the end of the working time, it will be considered as cheating.
- The following aids are permitted:
  - A non-programmable calculator (no calculator app!)
  - The cheat sheet provided by the chair without modifications in printed form
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be counted where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.
- Please write with red/green colors or with pencil.
- To print and scan your exam (if applicable), you may leave the room. Whether you take your camera with you or not is up to you. As already announced on Moodle, it may be beneficial to have a means of communication in case of any problems.
- If you need to go to the toilet during the exam, please inform the supervisor beforehand via a private message in BB and wait for a confirmation. Please do not take your smartphone/webcam with you.

---

### Task 1  
Multiple Choice (12 Points)  
The following tasks are multiple choice/multiple answer, i.e., there is at least one correct answer option for each.  
Tasks with only one correct answer are scored with 1 point if correct. Tasks with more than one correct answer are scored with 0.5 points per correct mark and -0.5 points per incorrect answer. The minimum score per task is 0 points.

Please mark the correct answers.  
Marked answers can be crossed out by filling in completely.  
Crossed-out answers can be marked again by adjacent markings.

a) In the first programming homework, the network plan for the Collatz subway was presented. Mark the last stop that was reached. You entered the subway at stop 547. (Note: The next stop corresponds either to half or to the predecessor of three times.)  
- 1640  
- 205  
- 820  
- 410  

b) Mark all word groups that describe the user data from layer 3 of the ISO/OSI model.  
- Data Link Layer  
- Network Layer  
- Network Layer  
- Data Link Layer  
- SDU  
- PDU  
- SDU  
- PDU  

c) The Internet traces back to the:  
- Usenet  
- ARPANET  
- Sneakernet  
- DARPANetwork  

d) The Protocol Data Unit of the Network Layer is also referred to as:  
- Messages  
- Packets  
- Segments  
- Frames  

e) Which of the following CIDR notations can also be realized with Classful Routing?  
- 10.0.0.0/1  
- 10.0.0.0/2  
- 10.0.0.0/16  
- 10.0.0.0/25  

f) Given a binary message source that emits the characters 0 and 1. The probability of emitting a 0 is Pr[X = 0] = 0.44. Determine the entropy of the source in bits.  
- 0.52  
- 0.99  
- 0.37  
- 0.30  
- 0.16  
- 0.11  

g) Given a time-continuous and value-continuous signal s(t). Mark the applicable statements.  
- Sampling of s(t) results in a time-discrete and value-continuous signal.  
- Sampling of s(t) results in a value-discrete and time-continuous signal.  
- Quantization of s(t) results in a time-discrete and value-continuous signal.  
- Quantization of s(t) results in a value-discrete and time-continuous signal.  

h) Given a channel with independent bit error probability of p = 0.05. Determine the probability that a codeword of length 2 bits is transmitted error-free.  
- 0.03  
- 0.90  
- 0.47  
- 0.00  
- Other value  

i) Given the date 0xf0e64b81 in Little Endian. What is the representation in Big Endian?  
- 0x6e0f18b4  
- 0x814be6f0  
- 0x18b46e0f  
- 0x0f6eb418  
- 0xf0e64b81  

j) A uniformly distributed signal is to be quantized with 2 bits so that the quantization error is minimized within the interval I = [0;8]. How should the quantization levels be chosen?  
- 4  
- 6  
- 5  
- 7  
- 0  
- 2  
- 1  
- 3  

k) Which of the following IPv4 addresses are not routed on the Internet?  
- 128.133.3.4  
- 172.16.164.118  
- 131.159.85.159  
- 169.254.26.159  
- 57.245.199.192  
- 170.85.164.118  

---

### Task 2  
What does the elephant say? (12 Points)  
In preparation for a "GRNVS of the Air," the GRNVS exercise management wants to realize the wireless transmission of exam answers. Based on existing technologies, frames are to be sent according to the schema shown in Figure 2.1. To save resources, a low-energy wide-area network is set up, which sends at 868.236 MHz (bandwidth 79 kHz) using 4-ASK and Manchester code. The SDU of a frame is secured by CRC-4 (check polynomial b^3 + b + 1). As More Frames (MF) is set, at least one additional frame is necessary to transport the layer 3 payload. The following address is to be assumed as the recipient address. For testing purposes, the message "toot" is to be transmitted.

a) Provide the binary representation of the 8-bit ASCII representation of the test message.  
- 0b01110100 01101111 01101111 01110100  

b) Determine the number of frames necessary for the transmission of the message.  
The 8-bit ASCII representation of the test message (length: 4 characters) is 4 * 8 bits = 32 bits long. A frame contains exactly 6 bits of user data. Therefore, 32 bits require 6 frames.  

c) Determine the checksum of the first sent frame.  
- Checksum calculation:  
  b8 + b7 + b6 + u0b5 + b4 + 0b3 + 0b2 + 0b + 0b3 + 0b2 + b + 1  
  The checksum corresponds to the zero-filled bit representation of the remainder.  

d) Provide the resulting frame.  
- Frame:  
  0B 510 1 See c) 0111012  

e) Represent the coded baseband signal for the SDU of the first sent frame.  

f) Draw a valid codeword assignment in the given signal space 4-ASK.  
- Codeword assignment:  
  - 00  
  - 01  
  - 10  
  - 11  

---

### Task 3  
Waves and Signals (7 Points)  
Anton Bergfried lives alone on his hill outside Hintertupfingen. However, he would like to communicate wirelessly with his neighbor, Rosia, on the neighboring hill. He knows nothing about these modern radio waves, so he prefers to rely on the good old sound waves. His sound system can produce tones from 70 Hz to 16 kHz, and the digital-to-analog converter allows for a 16-bit signal to be represented in this frequency range. Other influences on the signal, such as filtering, can be neglected.

a) How many different tones or signal levels can Anton reproduce with this system?  
- M = 2^16 = 65536  

b) What net data rate can Anton theoretically achieve with his system (neglecting noise and signal attenuation through the air)? Provide a comprehensible calculation.  
- B = 16 kHz - 70 Hz = 15930 Hz  
- C = 2 * B * log2(M) = 2 * 15930/s * 16 bit = 509760 bit/s  

Due to unforeseen reasons, Anton's other neighbor has started to turn up his music. This leads to Rosia hearing both. However, Anton's system is still listenable at double the power.

c) Determine the signal-to-noise ratio in dB that Rosia must now ascertain for Anton's signal.  
- SNR = 10 * log10(3.01 dB)  

d) Does this mean that the previously calculated data rate can no longer be achieved? If yes, provide a better upper limit with a comprehensible calculation.  
- Yes, because C_min ≤ C_max H_S  
- CS = B * log2(1 + SNR) = 15930/s * log2(1 + 1) = 25.25 kbit/s  
- Therefore, C_max = min(509.76 kbit/s; 25.25 kbit/s) = 25.25 kbit/s  

e) Anton always sends messages of size 1600B. However, far too many messages arrive faulty. For this reason, Anton decides to use a strongly error-correcting block code with a code rate of 3. Each block has a length of 300 bits. What new maximum data rate results when you calculate the redundancy introduced by the block code? For simplicity, assume C_max = 21 kbit/s. Provide a comprehensible calculation.  
- Blocks per message: n = 1600B / 300bit = 43  
- Size of a coded message: n * 300bit = 12900bit = 21500bit  
- Loss factor due to coding: v = 21500bit / 21500bit ≈  
- Data rate = 21 kbit/s / v = 12.5 kbit/s  

---

### Task 4  
WLAN (15 Points)  
Given is the network shown in Figure 4.1. We assume that NB1 and NB2 are associated (connected) with the AP, but the switching table of SW is still empty.  

a) Mark all broadcast domains in Figure 4.1.  

b) Mark all collision domains in Figure 4.1.  

c) Is the AP transparent for the NBs? Justify your answer!  
- No, the AP must be directly addressed on layer 2 in WLAN and is therefore not transparent here.  

d) Is the AP transparent for the PCs? Justify your answer!  
- Yes, from the perspective of the PCs, NB1 and NB2 are reachable via Ethernet. The AP accepts frames to its associated stations and forwards them transparently from the perspective of the wired network.  

e) Explain why IEEE 802.3 uses only two addresses, while IEEE 802.11 can have up to four addresses.  
- IEEE 802.3 addresses only the next hop, hence there are only Transmitter Address (TA) and Receiver Address (RA). (Sometimes referred to as SA and DA here, as there can be no confusion.)  
- IEEE 802.11 can use one (AP) or multiple (Mesh) intermediate stations on layer 2. Therefore, in addition to TA and RA, there are also SA (Source Address) and DA (Destination Address).  

Now we consider the network from Figure 4.1. NB1 sends a frame to the MAC address of PC1.  

f) Provide all used addresses and their four meanings in the frame transmitted from NB1 to the AP.  
- TA = SA = NB1, RA = AP, DA = PC  

g) Will this frame also be received by NB2?  
- Depending on the justification, both answers can be correct:  
  - Yes, if NB2 is within range of NB1, as IEEE 802.11 is a broadcast medium.  
  - No, because NB2 may "see" the frame but discards it due to the incorrect RA.  

h) Provide all used addresses and their four meanings in the frame forwarded by the AP to PC1.  
- TA = SA = NB1, RA = DA = PC1  

i) Will this frame also be received by NB2?  
- No, because the AP knows that NB2 is an associated station in the WLAN, but the frame is intended for another, non-associated station.  
- Note: The indication was originally intended for PC2, so the following answer is also correct: No, because it will be received by PC2 due to the empty switching table of SW but discarded due to the incorrect RA.  

j) Assume PC2 would send a frame addressed to NB2. Justify to which stations SW would forward this frame.  
- To all ports to which PC2 is connected: Since NB2 has not sent anything yet, SW cannot yet know which port this station is located on.  

---

### Additional Space for Solutions  
Please clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.