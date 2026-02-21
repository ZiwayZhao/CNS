Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized by the attachment of a code during the attendance check.  
- This contains only a continuous number, which is also noted on the attendance lists next to the signature field.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems (GRNVS)**  
Module: IN0010  
Examiner: Prof. Dr.-Ing. Georg Carle  
Exam: Endterm  
Date: Tuesday, July 26, 2016, 10:30–12:00  

**A1 A2 A3 A4 A5**  
I  
II  

**Instructions for Processing**  
- This exam comprises  
  - 20 pages with a total of 5 tasks as well as  
  - a double-sided printed formula collection.  
Please check now that you have received a complete set of information.  
- The tearing out of pages from the exam is prohibited.  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be counted where the solution path is recognizable. Text problems must also be justified unless explicitly stated otherwise in the respective sub-task.  
- Do not write with red/green colors or with a pencil.  
- The total score for this exam is 85 points.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - an analog dictionary German ↔ native language without annotations  
- Turn off all electronic devices completely, store them in your bag, and close it.  

---

**Task 1**  
Short Tasks (21.5 Points)  
The following sub-tasks can be solved independently of each other.  

a)* Name the layers (in English or German) of the ISO/OSI model in ascending order.  
b)* Given the 32-bit long date 0x81ff0010 in Network Byte Order. What is the representation in Little Endian?  
c)* Given the following network. Draw all collision domains.  
d)* Briefly explain two problems that can occur with RIP.  
e)* What is the difference between RTT and TTL?  
f)* What is the function of a resolver?  
g)* Justify whether a resolver must be located in the same broadcast domain as the requesting client.  
h)* What is meant by a "prefix-free code"?  
i)* Determine the reverse FQDN for 128.66.50.60.  
j)* Which system calls are necessary to create a UDP socket for bidirectional communication?  
k)* What is the shorthand notation of the IPv6 address 2001:0db8:0000:0000:0a00:0000:0000:000c?  
l)* Briefly explain what SLAAC is used for.  
m)* Name two routing protocols.  
n)* Justify why a minimum frame size is required in IEEE 802.3.  
o)* Calculate or justify the necessary signal power P, so that with a noise power of P_S = 1.0 mW, a signal-to-noise ratio of 6 dB is achieved.  
p)* Given an alphabet with a total of 64 different characters whose occurrence probability is uniformly distributed. Justify whether the average codeword length using Huffman coding is greater than, equal to, or less than 6 bits.  

---

**Task 2**  
Sampling and Quantization (11 Points)  
Given the time signal s(t) shown in Figure 2.1. This was created by modulating rectangular pulses onto a cosine carrier of frequency f = 1. The signal is to be sampled and quantized, and its information recovered.  

a)* Sample the signal s(t) at the time points t[n] = n + 0.5 for n = 0, 1, ... Fill in the sampled values in Figure 2.1 and provide the sampled values s[n] in the designated row with decimal precision.  
b)* Specify the quantization levels.  
c)* Determine the maximum quantization error within I.  
d)* Enter the quantized sampled values ŝ[n] in Figure 2.1 in the designated row.  
e)* How many bits are needed to represent the quantization levels?  
f)* Briefly justify which modulation method was most likely used in the generation of s(t).  
g)* Provide a valid signal space assignment.  
**Note:** There are multiple possible solutions. Providing one solution is sufficient.  

---

**Task 3**  
Data Matrix in Cornfields (15 Points)  
The Moepis from the planet Gliese 587 have made great technological advances and discovered a new planet - Earth. This, it seems, is inhabited by a strange species. To contact these beings, the Moepis use a laser beam to burn data matrix codes into cornfields.  

To transmit the i-th letter, it is first represented as a 7-bit long ASCII character, which is then encoded as an 8-bit long datum d = a + 1. A sequence of k letters is encoded as a polynomial  
d(x) = ∑(d_i * x^k) with d_i ∈ {0, 1, ..., 255} (1).  

a)* Provide d(x) for the message "Hello" (without quotation marks).  
b)* Justify whether the method described here is channel or source coding.  

**Note:** If you could not solve sub-task a), use the polynomial d(x) = 78x^4 + 112x^3 + 102x^2 + 113x + 106 for the following sub-tasks.  
The code block c(x) for a data block d(x) is calculated according to  
c(x) = d(x) · x^n_k + e(x) (2)  
where e(x) = d(x) · x^n_k mod r(x) represents the redundant information. In this case, k = 5B is mapped to n = 12B. The corresponding reduction polynomial r(x) is  
r(x) = 254x^6 + 92x^5 + 240x^4 + 134x^3 + 144x^2 + 68x + 23. (3)  

c)* How does e(x) differ from a checksum, as used in CRC?  
d)* Justify how the first 5 bytes of the code block are composed.  
e)* For the second symbol, mark the set (logically 1) bit positions.  

The Moepi operating the laser fails with a probability 0 < ε < 1, which then leads to a faulty marking. A symbol (as shown in the solution field for sub-task e) is defective as soon as at least one of its positions is faulty.  
The Reed-Solomon code is capable of correcting up to three defective bytes within a secured message of n = 12B, regardless of how many bit errors are contained in an affected byte.  

f)* Determine the probability, depending on ε, that humans can correctly decipher the data matrix. Simplify the result as much as possible.  
g)* Explain how humans on Earth can still decode the message.  
h)* Determine the probability, depending on ε, that a data matrix can be correctly decoded using the method described in sub-task g). Simplify the result as much as possible.  

---

**Task 4**  
NAT and Static Routing (15 Points)  
We consider the network from Figure 4.1. PC1 and PC2 are connected to each other and to the router R1 via the switch S. In the local network, the subnet 10.12.121.32/28 is used. The router R1 is connected to R2 via a transport network with a prefix length of 30, which represents the gateway to the Internet on the side of a service provider.  

a)* Determine the broadcast address of the subnet 10.12.121.32/28.  
b)* Assign IP addresses from the subnet 10.12.121.32/28 to PC1, PC2, and R1. Enter these directly in Figure 4.1.  
c)* Determine the network address of the transport network between R1 and R2.  
d)* Assign R1 an address from the transport network. Enter this directly in Figure 4.1.  
e)* How many /30 subnets are there in the network 131.159.0.0/16?  
f)* Justify why R1 must support NAT to allow PC1 and PC2 access to the Internet.  
g)* Which transport protocol and which destination port are used when PC1 accesses the website www.google.de via a browser?  

Next, we abbreviate IP and MAC addresses according to the schema <Device>.<Interface>, e.g., R1.eth0 for the corresponding address on interface eth0 of router R1. Note for the following sub-tasks that there are also four other routers between R2 and R3. PC1 is now accessing the website www.google.de.  

h)* Complete the header fields for the request from PC1 to www.google.de in the three empty boxes in Figure 4.2. If a field is not uniquely determined, make a sensible choice.  
i)* Complete the header fields for the response from www.google.de to PC1 in the three empty boxes in Figure 4.3. If a field is not uniquely determined, make a sensible choice.  

---

**Task 5**  
Transport Protocols (22.5 Points)  
We consider a connection between a client C and a server S over the Internet. Processes below the transport layer can be neglected.  

a)* Explain two essential differences between TCP and UDP.  
b)* We initially consider only TCP. We assume that client C establishes a connection to server S on TCP port 80. The initial sequence numbers are N for client C and M for server S.  
c)* Sketch the connection establishment as a simplified time-space diagram. Provide the sequence number, acknowledgment number, and the set flags for each exchanged message.  
d)* What is generally meant by an MSS?  
e)* How is the frequently applicable value 1 MSS = 1460B calculated?  
f)* Name the two phases that the congestion control mechanism of TCP goes through during the transmission phase (without justification).  
g)* Briefly describe the development of the size of the send window during both congestion control phases.  

We want to determine the time required to transmit the film, which has a size of L = 600 MiB. Serialization and processing times can be neglected. The initial request for download has already been sent, i.e., S starts directly with sending the film.  
We consider the size w[k] of the send window at time points k · RTT for k = 0, 1, ..., i.e., at the beginning of the k-th time step, k · RTT seconds have passed. The RTT is 10 ms, and for k = 0 it holds that w[k] = 1 MSS. For simplification, it is assumed that exactly one segment is lost as soon as w[k] ≥ x = 128 MSS. The receiving window at C is chosen so that it has no influence on the development of the send window.  

h)* Determine the number n of segments to be transmitted.  
i)* Determine the time t until the first segment loss occurs in seconds.  
j)* Determine the number n of successfully transmitted segments until the first segment loss occurs.  

After the first segment loss, n2 = n - n1 segments remain to be transmitted.  
**Notes:**  
1. If you could not solve sub-task i), assume 430668 remaining segments.  
2. Note the information in the section "Transport Layer" in the formula collection.  
k)* Determine the duration between the occurrence of further segment losses in seconds.  
l)* Determine the remaining time t until the transmission is completed.  
m)* Determine the total time t for data transmission in seconds.  
n)* Justify whether UDP would be a sensible alternative for the download considered here.  

---

**Additional space for solutions. Clearly mark the assignment to the respective sub-task. Do not forget to cross out invalid solutions.**