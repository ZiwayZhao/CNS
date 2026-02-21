Name First Name  
..................  
Grade  
Study Program (Major) Specialization (Minor)  
I II  
Student ID  
Signature of the Candidate  

TECHNICAL UNIVERSITY OF MUNICH  
Faculty of Computer Science  
Midterm Exam  
× Final Exam  
Semester Exam  
Diploma Preliminary Examination  
Bachelor Examination  
............................  
Consent for Grade Announcement  
by E-Mail / Internet  
Examination Subject: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle  
Date: 10.08.2012  
Lecture Hall: .................... Row: .................... Seat: .....................  
To be filled out by the supervision only:  
Lecture hall exited from ...... : ...... to ...... : ......  
Submitted early at ....... : ......  
Special Remarks:  
Endterm Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
Friday, 10.08.2012  
11:00 – 12:30  

- This exam consists of 23 pages and a total of 6 tasks. Please check now that you have received a complete set of materials.  
- Please write your name and student ID in the header of each page.  
- The total number of points is 85.  
- The allowed aids are a double-sided handwritten A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be counted where a solution method is recognizable. Text tasks must be justified unless explicitly stated otherwise in the respective sub-task.  

### Task 1 Frame Error Probability (Points)  
We consider a wireless connection between two computers A and B (see Figure 1.1). We simplify by assuming that bit errors occur independently with probability \(0 < p < 1\). A frame of length \(x_{bit}\) is transmitted correctly if it has no bit errors. The probability of a successfully transmitted frame thus depends on the frame length and the bit error probability.  

**a)** Determine the probability that a frame is transmitted successfully.  
\[ f(x,p) = (1 - p)^x \]  
If a frame is transmitted correctly, it corresponds to successfully transmitted bits. If at least one bit error occurs, the entire frame must be repeated, which corresponds to successfully transmitted bits.  

**b)** Determine the average number of successfully transmitted bits per frame.  
\[ g(x,p) = x(1 - p)^x + 0(1 - (1 - p)^x) = x(1 - p)^x \]  

**c)** Determine the optimal frame length \(x^*\) that maximizes \(g(x,p)\).  
\[ \frac{d}{dx} g(x,p) = (1 - p)^x + x \ln(1 - p)(1 - p)^x = 0 \]  
This leads to:  
\[ (1 - p)^x(1 + x \ln(1 - p)) = 0 \]  
Thus,  
\[ x^* = -\frac{1}{\ln(1 - p)} \]  

The bit error probability is now given as \(p = 10^{-4}\).  

**d)** Determine \(x^*\) explicitly for the given bit error rate.  
\[ x^* \approx -\frac{1}{\ln(1 - 10^{-4})} \approx 1250B \]  

**e)** What is the probability under these circumstances that a frame of optimal length is transmitted incorrectly?  
\[ p_R = 1 - f(x^*, p) = 1 - (1 - 10^{-4})^{1250} \approx 63.21\% \]  

Next, we assume a frame error probability of \(p_R = 60\%\), which is too high for higher-layer protocols to function correctly. Therefore, the frame error probability should be reduced using link-layer acknowledgments. We assume the "Stop and Wait" principle, meaning computer A sends exactly one frame to B and waits for an acknowledgment if B has received the frame correctly. If the acknowledgment is not received, A repeats the frame. The process stops after a total number of retry attempts \(N\).  

**f)** Determine the probability that the procedure fails.  
\[ Pr[X > N] = p_R^N \]  

**g)** Determine the minimum number of retries per frame so that the probability of a failure is below \(0.1\%\).  
\[ p_R^N < 10^{-3} \]  
This leads to:  
\[ N > \frac{\log(10^3)}{\log(p_R)} \approx 13.52 \Rightarrow N_{min} = 14 \]  

### Task 2 NAT and Static Routing (Points)  
Given the network topology from Figure 2.1. PC1 and PC2 are connected via a regular Ethernet switch with router R1, which provides access to the Internet.  

**a)** Determine the network address and broadcast address of the network in which PC1, PC2, and R1 are located.  
Network address: 10.0.34.0 and broadcast address: 10.0.35.255  

**b)** How many IP addresses are available in this network for addressing devices?  
\[ 2^{29} - 2 = 510 \]  

**c)** Assign PC1 and PC2 a meaningful IP address, subnet mask, and gateway address so that they can establish a connection to the Internet. Fill in the values directly in Figure 2.1.  

**d)** How many /23 subnets are there in the network 10.0.0.0/8?  
\[ 2^{23} - 2 = 32768 \]  

**e)** Which header fields does switch SW1 change, which connects PC1 and PC2 to R1?  
None, switches are transparent to connected devices.  

**f)** Justify why R1 must support NAT for PC1 and PC2 to communicate with hosts on the Internet.  
PC1 and PC2 are in a private network, and their IP addresses are therefore not globally unique.  

**g)** Which transport protocol and which destination port number are typically used for (unencrypted) HTTP connections?  
TCP 80  

Next, we abbreviate IP and MAC addresses according to the scheme `<DeviceName>.<Interface>`, e.g., R1.wan0. Note that there are three additional routers between R2 and R3. PC1 now accesses the website http://www.google.de.  

**h)** Complete the header fields for the request from PC1 to www.google.de in the three empty boxes in Figure 2.2. If a field is not clearly defined, make a reasonable choice.  
(Note: If you could not solve subtask g), assume destination port 80.)  

**i)** Complete the header fields for the response from www.google.de to PC1 in the three empty boxes in Figure 2.3. If a field is not clearly defined, make a reasonable choice.  

### Task 3 Packet Pair Probing (Points)  
Given the simplified network topology from Figure 3.1. A and D are connected to their routers via Gigabit Ethernet. However, the connection between routers B and C is significantly slower. A and D should determine this transmission rate while generating as little load as possible on the already slow connection.  

**a)** Specify the serialization time between two nodes as a function of the packet size and the transmission rate.  
\[ t_{s}(i,j) = \frac{p}{r_{ij}} \]  

**b)** Specify the propagation delay between two nodes as a function of the distance.  
\[ t_{p}(i,j) = \frac{d_{ij}}{v} \]  

To successfully and accurately determine the rate, it is important that packets sent from A to D are as large as possible but not fragmented.  

**c)** Briefly explain how A can determine the maximum MTU on the path to D.  
A sends a packet with the MTU of the local segment and sets the DF bit (do not fragment) in the IP header. If this MTU is larger than that on the segment between B and C, B will discard the packet and send an appropriate ICMP message back to A. This contains the maximum MTU on the segment from B to C.  

A now sends two packets of length \(p\) consecutively to D. You can assume that no other traffic affects the transmission. The length is chosen so that no fragmentation is necessary. You can neglect any processing times at the nodes.  

**d)** Draw a time-space diagram that qualitatively represents the transmission of the two packets. Pay particular attention to the points mentioned above.  

**e)** A pause in transmission occurs at node C between the two forwarded packets due to the low transmission rate between B and C. This can be measured by D and used to determine the transmission rate between B and C.  

**f)** Mark in your solution from part d).  

**g)** What does \(\Delta t\) depend on?  
Only on \(r_{BC}\) and \(r_{CD}\), not on the propagation delays.  

**h)** Provide an expression for \(\Delta t\).  
\[ \Delta t = t_{p}(B,C) + t_{p}(C,D) \]  

**i)** Provide an expression for the sought data rate.  
\[ r = \frac{p}{\Delta t} + r_{CD} \]  

Repeated measurements at D yield an average value with a packet size of \(p = 1500 \text{ Bytes}\) and \(\Delta t = 1.20 \text{ ms}\).  

**j)** Determine the numerical value of \(r_{BC}\) in Mbit/s.  
\[ r_{BC} \approx 9.99 \text{ Mbit/s} \]  

**k)** Give two reasons why the method may be inaccurate in practice.  
For example:  
- Cross-traffic disrupts the measurements  
- Processing times at the nodes are non-deterministic and cannot be neglected in practice  
- Buffering delays at the routers  

### Task 4 Dynamic Routing (Points)  
Given the simplified network depicted in Figure 4.1. All routers use RIP as the routing protocol. The tables below routers A – E in Figure 4.1 represent the routing table of each router before RIP is started.  

**a)** What metric does RIP use?  
Hop count  

**b)** To which class of routing protocols does RIP belong?  
Distance vector protocols (also correct: Interior Gateway Protocols)  

**c)** In what way are networks whose routers exclusively use RIP as a routing protocol limited in size?  
The metric 15 is interpreted as the diameter (in terms of hop count) of a network is limited to 15.  

**d)** Briefly explain how RIP works. (2 – 3 bullet points are sufficient!)  
- Routers regularly send each other the contents of their routing tables  
- The receiver increments the costs in the received table by 1  
- If it finds a cheaper path to a destination than in its own table, it updates its own table entry.  

**e)** Justify whether RIP always chooses the fastest route to a destination (in terms of transmission rate).  
No, as the only metric used is hop count, and RIP has no information about the maximum data rate along a path.  

The routers now start RIP. With some time delay, the routers send updates to each other. The chronological order of the updates is given by the following three subtasks. The column "TA" (subtask) in the routing tables in Figure 4.1 indicates the subtask (i.e., the time step) in which the respective entry is added.  

**f)** Enter all changes in the routing tables in Figure 4.1 after B has sent its first update.  

**g)** Enter all changes in the routing tables in Figure 4.1 after C has sent its first update.  

**h)** Enter all changes in the routing tables in Figure 4.1 after D has sent its first update.  

**i)** Describe briefly the problem that can occur with RIP when the link between C and E fails. (2 – 3 bullet points are sufficient!)  
- C informs B and D about the problem with the next update.  
- If A sends another update to B and D before either of them informs A, B and D will incorrectly install routes to E via A.  
- The misinformation spreads in the network, with the costs to E always being incremented by 1 ("Count to Infinity").  

### Task 5 TCP Flow and Congestion Control (Points)  
The most widely used transport protocol on the Internet is TCP. It implements mechanisms for flow and congestion control. Specifically, we assume TCP "Reno" in this task.  

**a)** What is the purpose of flow control?  
To prevent overload situations at the receiver.  

**b)** What is the purpose of congestion control?  
To react to overload situations in the network.  

**c)** What role does the receive window play in flow control?  
It indicates the maximum amount of data in bytes that the receiver is willing to accept at once.  

**d)** Sketch a typical course of the send window size for TCP by hand in the solution field. Assume that the TCP connection has just been established.  

**e)** Mark and name the two phases of congestion control in your solution from part d).  

**f)** What triggers the transition between the two congestion control phases?  
3 Duplicate ACKs (also sufficient: a lost segment)  

**g)** Under what circumstances does the congestion control mechanism start over?  
Timeout  

To analyze the TCP data rate, we consider the course of a contiguous data transmission, where the first phase of congestion control has already been completed. Since the receive window is assumed to always be sufficiently large, the size of the send window always corresponds to the size of the congestion control window. There are no losses as long as the send window is smaller than a maximum value. When the send window reaches that value, exactly one of the sent TCP segments is lost.  

**h)** How does the receiver detect the loss of a segment?  
By an out-of-order received sequence number.  

**i)** How does a single lost segment affect the send or congestion control window?  
Initially, it does not affect it at all. Only when 3 Duplicate ACKs are received as a result of the loss will it be reduced to half of the current value. Alternatively, a timeout can also trigger another slow start. In this case, the send window is set to 1 and the congestion control window to half of the current value.  

Assuming that the maximum TCP segment size (MSS) is 1460 Bytes and the RTT is 200 ms, the serialization time of segments is negligible compared to the propagation delay. Segment loss occurs at a send window size of \(w = 16 \cdot MSS\).  

**j)** Create a diagram in which the current size of the send window measured in multiples of the MSS is plotted over the time axis measured in multiples of the RTT. In your diagram, \(t\) should hold at the moment just before the loss occurs. Draw the diagram in the time interval \(t = 0\) to \(t = 14\).  

**k)** Determine the period duration between the reduction of the send window and the next segment loss in general as a function of \(x\).  
\[ T = \frac{x \cdot RTT}{2 \cdot MSS} \approx 1.8s \]  

**l)** Determine the number of segments transmitted per period duration (including the lost segment at the end) in general as a function of \(x\).  
Using the shorthand notation, we obtain:  
\[ N = \frac{3n^2 + 3n}{8} \]  

**m)** Determine the loss rate in general and as a numerical value.  
For each "sawtooth," exactly one segment is lost. Thus, we obtain for the loss rate:  
\[ \theta \approx 9.26 \cdot 10^{-3} \]  

**n)** Using the results from subtasks k) – m), determine the average achievable transmission rate during the considered TCP transmission phase in kbit/s.  
For the data rate, we obtain:  
\[ r \approx 694 \text{kbit/s} \]  

### Task 6 Short Tasks (Points)  
The following short tasks are independent of each other. Bullet-point answers are sufficient!  

**a)** The graphic below shows the send signal and the received signal after transmission over a non-ideal channel. What two channel influences are visible?  
Low-pass filtering and attenuation  

**b)** In the lecture, a simple block code was presented, which maps:  
\(k = 1 \text{ bit} \rightarrow n = 3 \text{ bit}\)  
\(0 \rightarrow 000, 1 \rightarrow 111\).  
To further improve error correction, the following modification is proposed:  
\(0 \rightarrow 0000, 1 \rightarrow 1111\).  
How do you evaluate this change in terms of error correction and efficiency?  
The error correction property does not change; efficiency decreases.  

**c)** Which metric is optimized to produce a Shortest Path Tree?  
The sum of the edge weights from a root to each other node is minimized.  

**d)** Which metric is optimized to produce a Minimum Spanning Tree?  
The total sum of the edge weights is minimized.  

**e)** Given \(fe80::222:b0ff:febc:1fe2/64\). To which protocol does this address belong?  
IPv6  

**f)** Given an alphabet with a total of 32 different characters, whose occurrence probability is uniformly distributed. Justify whether the average codeword length when using Huffman coding is greater than, equal to, or less than 5 bits.  
Since the characters are uniformly distributed, the Huffman code results from a complete binary tree with leaves of height \(5\). The codewords result from the paths from the root to the leaves and are therefore each 5 bits long.  

**g)** Why can the original of a JPEG-compressed image not be reconstructed exactly?  
Lossy compression method  

**h)** Justify (either argumentatively or by calculation) whether the time signal \(s(t)\) shown below has a DC component.  
The signal has no DC component, as the signal is zero-mean. This is evident from the point symmetry about the origin.  

### Additional Space for Solutions  
Please clearly mark the affiliation to the respective task and cross out invalid solutions!