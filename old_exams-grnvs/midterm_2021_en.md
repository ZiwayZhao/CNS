Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by attaching a code during the attendance check.  
- This code contains only a continuous number, which is also noted next to the signature field on the attendance list.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Midterm  
Date: Tuesday, June 8, 2021  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 10:45–11:30  

Please sign the behavior rules at the top right next to your sticker. Otherwise, your electronic exercise performance will not be counted!

### Instructions for Processing
- This exam consists of 8 pages with a total of 4 tasks.  
- The total score for this exam is 46 points.  
- The exam must be submitted completely, i.e., no missing or duplicate pages.  
- The working time is 45 minutes. If you continue working after the end of the working time, this will be counted as a violation.  
- The following aids are allowed:  
  - a non-programmable calculator (no calculator app!)  
  - the cheat sheet provided by the chair without modifications in printed form  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be counted where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write with red/green colors or with pencil.  
- You may leave the room to print and scan your exam (if applicable). Whether you take your camera with you or not is up to you. As already announced on Moodle, it may be beneficial to have a means of communication in case of any problems.  
- If you need to go to the restroom during the exam, please inform the supervisor beforehand via private message in BB and wait for confirmation. Please do not take your smartphone/webcam with you.  

---

### Task 1  
**Multiple Choice (12 points)**  
The following tasks are multiple choice/multiple answer, meaning at least one answer option is correct for each. Tasks with only one correct answer are scored with 1 point if correct. Tasks with more than one correct answer are scored with 0.5 points for each correct tick and -0.5 points for each incorrect answer. The minimum score per sub-task is 0 points.  

**Tick the correct answers**  
- Ticks can be crossed out by complete filling.  
- Crossed-out answers can be ticked again by adjacent markings.  

a) *In the first programming homework, the network plan for the Collatz subway was presented. Mark the last stop that was reached. You entered the subway at stop 547. (Note: The next stop corresponds either to half or the predecessor of three times.)  
1640 205 820 410  

b) *Mark all phrases that describe the user data from layer 3 of the ISO/OSI model.  
- Data Link Layer  
- Network Layer  
- Network Layer  
- Data Link Layer  
- SDU  
- PDU  
- SDU  
- PDU  

c) *The Internet dates back to:  
- Usenet  
- ARPANET  
- Sneakernet  
- DARPA Network  

d) *The Protocol Data Unit of the Network Layer is also referred to as:  
- Messages  
- Packets  
- Segments  
- Frames  

e) *Which of the following CIDR notations can also be realized with Classful Routing?  
- 10.0.0.0/1  
- 10.0.0.0/2  
- 10.0.0.0/16  
- 10.0.0.0/25  

f) *Given a binary message source that emits the characters 0 and 1. The probability that a 0 is emitted is Pr[X = 0] = 0.44. Determine the entropy of the source in bits.  
- 0.52  
- 0.99  
- 0.37  
- 0.30  
- 0.16  
- 0.11  

g) *Given a time-continuous and value-continuous signal s(t). Tick the applicable statements.  
- Sampling of s(t) results in a time-discrete and value-continuous signal.  
- Sampling of s(t) results in a value-discrete and time-continuous signal.  
- Quantization of s(t) results in a time-discrete and value-continuous signal.  
- Quantization of s(t) results in a value-discrete and time-continuous signal.  

h) *Given a channel with independent bit error probability of p = 0.05. Determine the probability that a codeword of length 2 bits is transmitted error-free.  
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
**What does the elephant say? (12 points)**  
In preparation for a "GRNVS of the Air," the GRNVS exercise management wants to realize the wireless transmission of exam answers. Based on existing technologies, frames are to be sent according to the schema in Figure 2.1. To save resources, a low-energy wide-area network is being built, which transmits at 868.236 MHz (bandwidth 79 kHz) using 4-ASK and Manchester code. The SDU of a frame is secured by CRC-4 (check polynomial b^3 + b + 1). The More Frames (MF) bit is set if at least one more frame is necessary to transport the layer 3 payload. The recipient address is to be assumed as address 5. For testing purposes, the message "toot" is to be transmitted.  

a) *Provide the binary representation of the 8-bit ASCII representation of the test message.  

b) *Determine the number of frames necessary for the transmission of the message.  

c) Determine the checksum of the first sent frame.  

d) Provide the resulting frame.  

e) Represent the coded baseband signal for the SDU of the first sent frame.  

f) *Draw the given signal space 4-ASK and assign a valid codeword.  

---

### Task 3  
**Waves and Signals (7 points)**  
Anton Bergfried lives alone on his hill outside Hintertupfingen. However, he would like to communicate wirelessly with his neighbor, Rosa, on the neighboring hill. He knows nothing about these newfangled radio waves, so he prefers to rely on the good old sound waves. His sound system can produce tones from 70 Hz to 16 kHz, and the digital-to-analog converter allows for a 16-bit signal to be represented in this frequency range. Other influences on the signal, e.g., from filters, can be neglected.  

a) *How many different tones or signal levels can Anton reproduce with this system?  

b) What net data rate can Anton theoretically achieve with his system (neglecting noise and signal attenuation through the air)? Provide a comprehensible calculation.  

c) *Determine the signal-to-noise ratio in dB that Rosa must now observe for Anton's signal due to the additional sender.  

d) Does this mean that the previously calculated data rate can no longer be achieved? If yes, provide a better upper limit with a comprehensible calculation.  

e) *Anton always sends messages of size 1600 B. Unfortunately, too many messages arrive faulty. Therefore, Anton decides to use a strongly error-correcting block code with a code rate of 3. Each block has a length of 300 bits. What new maximum data rate results when you calculate out the redundancy introduced by the block code? For simplicity, assume Cmax = 21 kbit/s. Pay attention to a comprehensible calculation.  

---

### Task 4  
**WLAN (15 points)**  
Given the network shown in Figure 4.1. We assume that NB1 and NB2 are associated (connected) with the AP, while the switching table of SW is still empty.  

a) *Mark all broadcast domains in Figure 4.1.  

b) *Mark all collision domains in Figure 4.1.  

c) *Is the AP transparent for the NBs? Justify your answer!  

d) *Is the AP transparent for the PCs? Justify your answer!  

e) *Explain why IEEE 802.3 uses only two addresses, while IEEE 802.11 can have up to four addresses.  

Now we consider the network from Figure 4.1 again. NB1 sends a frame to the MAC address of PC1.  

f) Provide all used addresses and their four meanings in the frame transmitted from NB1 to the AP.  

g) Will this frame also be received by NB2?  

h) Provide all used addresses and their four meanings in the frame forwarded by the AP to PC1.  

i) Will this frame also be received by NB2?  

j) *Assuming PC2 would send a frame addressed to NB2. Justify which stations SW would forward this frame to.  

---

### Additional Space for Solutions  
Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.