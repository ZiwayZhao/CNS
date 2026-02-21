Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by attaching a code during the attendance check.
- This code only contains a continuous number, which is also noted in the attendance list next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Retake onsite  
Date: Tuesday, September 29, 2020  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 11:30 AM – 1:00 PM  

### Instructions for Processing
- This exam consists of 16 pages with a total of 6 tasks.  
Please check now that you have received a complete set of information.  
- The total score for this exam is 90 points.  
- It is prohibited to tear out pages from the exam.  
- The following aids are allowed:  
  - all electronic and non-electronic aids  
  - explicitly not allowed are the Internet and teamwork  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only results where the solution path is recognizable will be counted. Text problems must also be justified unless otherwise stated in the respective subtask.  
- Copying solution proposals from old exams or other sources does not constitute independent performance. We reserve the right to evaluate the respective task with 0 points in such cases.  
- Do not write with red/green colors or with pencil.  

### Task 1  
Multiple Choice (19 points)  
The following subtasks are Multiple Choice Multiple Answer with 1 point for each correct answer and -1 point for each incorrect answer. Multiple answers may be correct.  
The minimum score per subtask is 0 points, i.e., negative points do not carry over to other subtasks.  

Instructions for processing on paper or if your PDF editor does not support the checkbox function:  
- Check the correct answers.  
- Checked boxes can be crossed out by completely filling them in.  
- Crossed-out answers can be checked again by marking next to them.  

a) * In a segment, it is a...  
- L3-SDU  
- L2-SDU  
- L4-PDU  
- L3-PDU  
- L1-PDU  
- L4-SDU  
- L2-PDU  
- L1-SDU  

b) * Which statements about Fourier transformations are correct?  
- The spectrum is discrete.  
- The spectrum is continuous.  
- The spectrum is always complex.  
- The spectrum is always limited.  
- Used for the analysis of non-periodic signals.  
- Used for the analysis of periodic signals.  

c) * Given is a continuous signal that is to be quantized linearly with 3 bits in the interval I = [7; 16]. Determine the maximum quantization error within I rounded to two decimal places.  
- 1.00  
- 3.00  
- 1.13  
- 0.56  
- other value  

d) * Given is a continuous signal that is to be quantized linearly with 2 bits in the interval I = [0; 15]. Determine the maximum quantization error outside of I rounded to two decimal places.  
- 3.75  
- 1.88  
- 7.50  
- 2.50  
- other value  

e) * Given is a line code that encodes 3 bits per symbol. It should achieve a data rate of 8 Mbit/s. Determine the minimum necessary bandwidth under the given conditions rounded to two decimal places.  
- other value  
- 1.33 MHz  
- 5.33 MHz  
- 4.43 MHz  
- 17.72 MHz  

f) * What is meant by source coding?  
- Representation of data by sequences of signal impulses.  
- The removal of redundancy.  
- Purposeful addition of redundancy.  

g) * Given is a microwave link that has the same conditions in both directions. The transmission rate is given as 20 Mbit/s. The distance is 126 km. Determine the RTT of a 1091 B large frame (e.g., Echo Request/Reply) rounded to two decimal places. Assume that no further time delays occur due to media access and processing at the nodes.  
- 420 ms  
- 840 ms  
- 873 ms  
- 436 ms  
- 1.713 ms  
- 856 ms  

h) * If the notebook (NB) in the adjacent illustration wants to send a frame to one of the PCs, which MAC address(es) will be used to specify the target?  

i) * If the notebook (NB) in the adjacent illustration wants to send a frame to one of the PCs, which IP address(es) will be used to specify the target?  

j) * What is the binary representation of the number 0x474802?  

k) * You receive a message from the IPv6 address fd00:32:15:8:e7be:0dff:fe56:23a4. What is most likely the MAC address of the sending interface?  

l) * How many broadcast domains does the adjacent network consist of?  

m) * How many collision domains does the adjacent network consist of?  

n) * You observe the following data stream from an unknown source. At which character(s) is the information content maximal?  

### Task 2  
Short Tasks (7 points)  
a) * Give a bit sequence that matches the signal depicted below, where the duration of a single symbol is 1 s. Note: There are two equivalent solutions. Provide one of them.  

b) * From the lecture, the following relationship is known for the transmission time of a message of length L split into packets of size p with header length L per packet over a distance d with a total of n hops and constant data rate r:  
\[ T = \frac{1}{r} \left( L + L_h + d + n \cdot \frac{L}{p} \right) \]  
Determine the optimal packet size p such that the transmission time is minimized. Assume that L is an integer multiple of the packet size.  

c) * Sketch by hand a typical course of the send window size for TCP (Reno). Assume that at time t = 0 the connection has just been established. Label and name different phases of congestion control.  

### Task 3  
I Spy (15 points)  
A neighbor of Mrs. Roberts sits in the café and excitedly looks at the wall next to him. He notices the nearby RJ45 port. Quickly, he connects his own laptop, with interface eth0, to this port using a special patch cable. Shortly thereafter, the frame shown in Figure 3.1 can be observed.  

a) * Name the Layer 2 SDU present in Figure 3.1. (Justification!)  

b) * Specify the type of Layer 2 SDU depicted in Figure 3.1. (Justification!)  

c) * Provide for the 7th header field of the Layer 2 SDU from Figure 3.1 the name, value, and function description. Use the usual representation form. (Justification!)  

d) * From further observation, it is noted that one of the observed Ethernet frames contains the IPv4 addresses 10.29.13.53 and 10.53.37.17. Provide the smallest network that contains these two IPv4 addresses. (Justification!)  

e) * Using the information collected in the course of this task, provide a valid static IPv4 configuration for an additional network participant. Note: It can be assumed that the router has the largest usable address.  

f) * How can it be validated that the IPv4 address chosen in part e) does not collide with the IPv4 address of another participant? (Justification!)  

g) * Determine the protocols used on layers 3 and 4 in the above frame. (Justification!)  

h) * Provide the destination addresses used on layers 2, 3, and 4 in their usual representation. (Justification!)  

### Task 4  
NAT and Routing (18 points)  
The network topology is given in Figure 4.1. PC1 and PC2 are connected via the WLAN Access Point AP to Router R1, which provides access to the Internet.  

a) * Justify whether the address 10.0.0.0 is usable for the given prefix. If not, assign R1 a meaningful address in the same network.  

b) * Determine the network address and broadcast address of the network in which PC1, PC2, and R1 are located.  

c) How many IP addresses are available in this network for addressing devices? Also provide the calculation method!  

d) Assign PC1 and PC2 each a meaningful IP address, subnet mask, and gateway address so that they can establish a connection to the Internet. Enter the values directly in Figure 4.1. Note any potentially differing IP from R1 from task a).  

e) * How many /21 subnets are there in the network 10.0.0.0/8? Also provide the calculation method!  

f) * Justify why R1 must support NAT so that PC1 and PC2 can communicate with hosts on the Internet.  

g) * What information must R1 at least hold in its NAT table?  

h) * Complete the header fields for the request from PC1 to www.grnvs.tips in the three empty boxes in Figure 4.2. If a field cannot be uniquely determined, make a sensible choice.  

i) * Complete the header fields for the response from www.grnvs.tips to PC1 in the three empty boxes in Figure 4.3. If a field cannot be uniquely determined, make a sensible choice.  

### Task 5  
Lossless Data Compression (10.5 points)  
To use your Internet connection more efficiently and transfer more data faster, you use a lossless compression: a Huffman code. Since you do not know in advance which data will be transmitted, you orient yourself to the data transmitted in the past and have already learned code words.  

Given is the alphabet A = {I, L, Q, A, W, G, O, Y, U} and the following table with the learned code words for each character x:  

| x | Code Word | x | Code Word |
|---|-----------|---|-----------|
| I | 00        | G | 0111      |
| L | 10        | O | 0101      |
| Q | 110       | Y | 01001     |
| A | 111       | U | 01000     |
| W | 0110      |

a) * How long is each code word if you were to use a uniform code instead of the Huffman code? Also provide the calculation method!  

b) You want to compress the following word (20 characters) with the above code:  
W I I A I Y L I G L Y W A L I Q L Q Q O  

c) Let X be the random variable of a memoryless source that generated the word. Derive the occurrence probability P[X = x] for all x from the set of respective characters. It is sufficient to provide the probability as a reduced fraction.  

d) How large is the average code word length if the probabilities from part b) were representative for the source? Provide a comprehensible calculation method.  

e) The actual average code word length is 2.9 bits/character. How does this value differ from the calculated value from part c)?  

f) How large is the expected savings when compressing many words from this source with this code compared to a uniform code?  

g) * Encode the first 6 characters of the word with the given Huffman code.  

### Task 6  
IPv6 (20.5 points)  
Given is the network topology in Figure 6.1. Router R is connected to the network NET1 via GW and to the Internet, and supplies the networks NET2 and NET3. NET3 is used for WLAN clients.  

a) * Which IP address will R receive on the interface ppp0 through SLAAC?  

b) Explain where the individual parts of this IP address come from.  

c) * Show that NET2 and NET3 cannot be aggregated on GW.  

d) * Fill in the usual column names in the routing table 6.1.  

e) Complete the routing table 6.1 for R so that the connected networks can reach the Internet and can be reached from there. Aggregate as much as possible.  

f) Argue where Router R will forward a packet with the destination address fe80::5:7:ff:fe42:3899.  

g) Client C is not IPv6 capable. To allow communication between C and the Internet, the network administrator assigned the IPv4 address 10.1.0.10/24 to C on the interface eth0.  

h) * Argue whether C can now communicate with the Internet.  

i) To solve some problems, the network administrator tries to install a mapping mechanism from IPv4 to IPv6. This should enable communication between devices configured for IPv4 and IPv6. To make Client C reachable from the Internet, a virtual IPv6 address is generated for Client C. This consists of the IPv6 prefix of the network in which C is located, with the lower bits set equal to the IPv4 address.  

j) * Provide this generated virtual IPv6 address for C and argue why this address is sensibly chosen. Use the usual notation for IPv6 addresses.  

k) The mapping mechanism now works, and incoming packets to the virtual IPv6 address are correctly translated into IPv4 packets.  

l) * A server S is located on the Internet. Can S send a message to C?  

m) What must happen in Router R for bidirectional communication between S and C to be possible?  

n) Client C now wants to send a control command to a drone with the IP address 2001:db8:1:c::c1a7:19f0, which is connected to R via WLAN through NET3. Explain what problems may arise during this communication and how these can be resolved by the network administrator. Giving the drone an IPv4 address is unfortunately not possible.  

o) To solve the problem, the administrator creates a mapping table in R. Fill in all mappings in Table 6.2 to enable seamless communication between C and the drone.  

### Additional space for solutions. Clearly mark the assignment to the respective subtask.  
Do not forget to cross out invalid solutions.