Name First Name  
Grade  
Degree Program (Major) Field of Study (Minor)  
I II  
Student ID Number  
Signature of the Candidate  

TECHNICAL UNIVERSITY OF MUNICH  
Faculty of Computer Science  

Midterm  
Endterm  
Repeat  

Exam Subject: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle  
Date: 22.09.2014  
Lecture Hall: Row: Seat:  

To be filled out by the supervisor only:  
Lecture hall left from: to:  
Submitted early at:  
Special Remarks:  

Repeat Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
Monday, 22.09.2014  
11:30 AM – 1:00 PM  

- This exam consists of 19 pages and a total of 6 tasks, as well as an additional distributed aid sheet with protocol headers. Please check now that you have received a complete set of materials.  
- Please write your name and student ID number in the header of each page.  
- Do not write in red/green ink or with a pencil.  
- The total number of points is 85.  
- Allowed aids are a handwritten double-sided DIN A4 sheet and a non-programmable calculator. Please remove all other materials from your desk, turn off your mobile phones, and put them away.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Do not spend too long on any (sub-)task. If you cannot solve the task immediately, rather continue with the next task.  
- Only results where a solution path is recognizable will be counted. Text tasks must be justified unless explicitly stated otherwise in the respective sub-task.  

Task 1: Fourier Series Again (13 Points)  
Given is the periodic signal shown in Figure 1.1, which is to be represented as a Fourier series:  
\[ s(t) = a_0 + \sum_{k=1}^{\infty} (a_k \cos(k\omega t) + b_k \sin(k\omega t)) \]  
The coefficients for all integer \( k > 0 \) can be determined as follows:  
\[ a_k = \frac{1}{T} \int_{-T/2}^{T/2} s(t) \cos(k\omega t) dt, \quad b_k = \frac{1}{T} \int_{-T/2}^{T/2} s(t) \sin(k\omega t) dt. \]  

a)* Justify why this basic impulse is not free of direct current.  
The impulse only takes non-negative values within a period. Therefore, the positive contributions cannot balance out.  

b)* Determine the period duration and angular frequency of the signal.  
\[ T = 2\pi, \quad \omega = 1 \]  

c)* Provide an analytical expression for the sending basic impulse, i.e., for \( s(t) \) in the interval \( t \in [-\pi, \pi) \).  
\[
s(t) = 
\begin{cases} 
-1 & \text{for } t < -\pi \\ 
0 & \text{for } 0 \leq t < \pi 
\end{cases} 
\]  

d)* Determine the DC component \( a_0 \).  
\[ a_0 = \frac{1}{2} \int_{-\pi}^{\pi} s(t) dt = \frac{1}{4} \]  

e)* What can be said about \( a_k \) and \( b_k \) for \( k > 0 \)? (Justification!)  
Neither \( a_k \) nor \( b_k \) is zero, as both contributions are not symmetric about the ordinate.  

f)* Determine the cosine components for \( k > 0 \).  
Hint: Depending on the solution path, one of the following hints may be helpful:  
\[
\int t \sin(kt) dt + \cos(kt) dt = \text{const} 
\]  
\[
\int f(t) g(t) dt = [f(t) g(t)]_b - \int f(t) g'(t) dt 
\]  

g)* Determine the sine components for \( k > 0 \).  
Hint: Depending on the solution path, one of the following hints may be helpful:  
\[
\int t \sin(kt) dt + k t \cos(kt) dt = \text{const} 
\]  

h)* Sketch the approximated signal \( s'(t) = a_0 + a \cos(\omega t) + b \sin(\omega t) \) in Figure 1.1.  
Note: The amplitude does not need to match exactly. It is important that the signal is drawn in phase correctly. It may be helpful to first draw the two components separately and then sketch their sum.  

Task 2: Framed Slotted ALOHA (15 Points)  
We will now consider Framed Slotted ALOHA, an extension of Slotted ALOHA, which can be used as a media access method in RFID systems. We assume that a set of stations, referred to as Tags, communicate with a so-called Reader. In this task, we will only consider one application case, namely the detection of the various Tags by the Reader. This occurs as follows:  
- The Reader sends the frame length to all Tags within range. The frame length is a natural number indicating the number of slots.  
- Each Tag \( i \) randomly and uniformly chooses a slot \( S_j \) during which its identifier is sent to the Reader.  
- If multiple Tags send in the same slot, a collision occurs. This is detected by the Reader through checksum verification.  
- A slot in which identification succeeds, i.e., exactly one Tag sends, is referred to as a Discovery Slot.  

a)* What type of multiplexing method is this?  
Time Division Multiplexing (TDM)  

b)* Determine the probability that a Tag sends in slot \( S_j \).  
\[ p = \frac{1}{s} \]  
Let \( X_j \) be the random variable representing the number of Tags sending simultaneously during slot \( S_j \). This is dependent on the number of slots in the frame and the number of Tags \( n \).  
\[ \Pr[X = k] \] describes the probability that exactly \( k \) Tags send in slot \( S_j \).  

c)* Determine the probability that slot \( S_j \) is a Discovery Slot.  
\[ \Pr[X = 1] = n p (1 - p)^{n-1} \]  

d) Calculate the probability from part c) as a numerical value for \( n = 10 \) and \( s = 20 \).  
\[ \Pr[X = 1] = \frac{10}{20} \cdot (1 - \frac{10}{20})^{9} = 0.315 \]  

e)* Determine the maximum number of identifiable Tags in a frame as a function of frame length and number of Tags.  
\[ m(n, s) = \begin{cases} 
s & \text{if } n \leq s \\ 
n & \text{if } n > s 
\end{cases} \]  

f)* Justify the problem that arises when \( n \ll s \), i.e., the number of Tags is significantly smaller than the number of slots.  
The transmission medium is not effectively utilized, as many slots remain unused.  

g)* Justify the problem that arises when \( n \gg s \), i.e., the number of Tags is significantly larger than the number of slots.  
The collision probability is very high, thus the channel is not effectively utilized. Alternatively: Not all Tags can be identified in a frame due to the pigeonhole principle.  

h)* Determine the duration of a slot given a data rate of \( r = 2400 \) bit and the size of a sent identifier with checksum \( l = 12B \).  
\[ t_{slot} = \frac{l}{r} = \frac{12 \times 8}{2400} = 0.04s \]  

i)* Provide the general probability that no Tag sends in slot \( S_j \).  
\[ \Pr[X = 0] = \left(1 - \frac{1}{s}\right)^{n} \]  

j)* Determine the expected time in seconds within a frame during which no Tag sends.  
\[ t_{idle} = s \cdot \Pr[X = 0] \cdot t_{slot} = 20 \cdot \left(1 - \frac{1}{20}\right)^{10} \cdot 0.04s = 0.479s \]  

k)* Determine the probability density function.  
\[ \Pr[X = k] = \binom{n}{k} p^k (1 - p)^{n - k} \]  

l)* What distribution is underlying?  
Binomial distribution (conclusion from k))  

Task 3: Hexdump (21 Points)  
Given is the hex dump from Figure 3.1, which represents an 86B long frame (Ethernet without FCS). The left column indicates the offset (hexadecimal) in multiples of bytes. The two subsequent columns represent the data (hexadecimal) in blocks of 8 bytes in Network Byte Order.  

0x0000: 08 60 6e 45 dc e6 00 1c 14 01 4e 18 86 dd 60 00  
0x0010: 00 00 00 20 06 40 2a 01 04 f8 0d 16 19 43 00 00  
0x0020: 00 00 00 00 00 02 2a 02 02 e0 03 fe 10 01 77 77  
0x0030: 77 2e 00 02 00 85 ce 44 00 50 9b 94 59 c9 2f e7  
0x0040: 5d 10 50 10 65 00 85 88 00 00 47 45 54 20 2f 68  
0x0050: 65 78 0d 0a 0d 0a  

a)* What is the difference between "Host Byte Order" and "Network Byte Order"?  
Host Byte Order is the native byte order of a host, either Little- or Big-Endian (determined by the CPU architecture). Network Byte Order is always Big-Endian.  

b)* Justify why it is necessary to distinguish between Host Byte Order and Network Byte Order.  
Since it is unclear which byte order a host uses, the Network Byte Order must be defined.  

c)* The value 0x12 has Little-Endian byte order. Provide the value in Big-Endian.  
0x12  

d)* Provide the offset in bytes from the start of the frame for the first and last byte of the Ethernet header.  
0x0000 0x000D  

e)* What protocol is used at Layer 3?  
Type field (Ethertype) in the Ethernet header: (Big-Endian) = IPv6 0x86dd  

f)* Provide the function and value of the Layer 3 header fields that must be changed during transport by routers.  
Hop Limit, function: to prevent endless forwarding in loops, here: = 64 Hops 0x40  

g)* What is the length of the Layer 3 SDU?  
Payload Length field in the IPv6 header: = 32B 0x0020  

h)* Mark the sender and receiver address in the Layer 3 header. (Draw it directly in Figure 3.1 and indicate which address belongs to the sender and which to the receiver.)  

i)* How can you tell that TCP is used as the Layer 4 protocol?  
Next Header field in the IPv6 header: = TCP 0x06  

j)* Provide the source port of the message in decimal representation.  
(Big-Endian) = 52804 0xce44  

k)* Provide the destination port of the message in decimal representation.  
(Big-Endian) = 80 0x0050  

l)* For which application layer protocol is the message evidently intended?  
TCP 80 (well-known Port) = HTTP  

m)* Provide two reasons why you cannot determine how many bytes have been exchanged over this TCP connection up to this point based on the information you have.  
- The initial sequence numbers exchanged during connection setup are unknown. Therefore, there is no reference point for the sequence and acknowledgment numbers.  
- It is possible that the sequence numbers have already wrapped around, meaning more than 4GiB of data has been exchanged.  

n)* What is the size of the TCP payload for the application layer?  
The TCP header has no options (Offset field is 5), meaning 32B - 20B of the TCP header results in a 12B payload.  

o)* Can data still be transmitted in the same direction after this segment within the ongoing TCP connection?  
Yes, as the FIN flag in the TCP header is not set.  

p)* Can data still be transmitted in the opposite direction after this segment within the ongoing TCP connection?  
Unknown, as the other side may have already closed the TCP connection with a previous FIN.  

Task 4: Domain Name System (15 Points)  
Initially, the DNS structure shown in Figure 4.1 is given.  

a)* Briefly explain what DNS is used for.  
Mapping between FQDNs and IP addresses.  

b)* Assign DNS to a layer in the ISO/OSI model. (No justification necessary)  
Layer 7.  

c)* Mark and name all name components for the FQDN www.tum.de.  
Second Level Domain: tum, TLD: de, Hostname: www.tum.de. Root  

d)* Mark the lines in Figure 4.2 that contain the address records for hosts.  

e)* What function does the MX record have?  
Points to the FQDN of a mail server for the domain in.tum.de.  

f)* Complete Figure 4.1 based on the information from the zone file in Figure 4.2.  

g)* What possibilities arise when multiple FQDNs point to the same IP address?  
For example, multiple websites on the same server or under the same IP address.  

h)* What advantages can there be when multiple IP addresses are assigned to one FQDN?  
Load balancing (alternatively: IP dual-stack, i.e., simultaneous accessibility via IPv4 and IPv6).  

i)* Explain the difference between recursive and iterative name resolution.  
In recursive resolution, only one request is made to the configured DNS server, which returns the final answer. In iterative resolution, the FQDN is resolved starting from the root zone by querying the authoritative name servers for the respective zones.  

j)* The client now wants to access www.tum.de. Draw all necessary DNS messages in Figure 4.3 using arrows and number them in order. The first message is already given as assistance.  

k)* Immediately after, the client wants to resolve www.in.tum.de. Briefly explain how this resolution differs from the one in part j).  
Due to the information in the caches, the request is directed directly to ns.tele.com and dns1.lrz.de. Then, an iterative request is made to nsa.in.tum.de.  

Task 5: Encryption (12 Points)  
In this task, we consider a binary block cipher with a block size of \( n = 4 \) bits. The encryption is realized through a permutation of the bits.  

a)* Calculate the number of possible keys.  
\[ n! = 24 \]  

b)* Encrypt the plaintext using the ECB mode.  
\[ m = 1001001110110111 \]  
- \( m_1 = 1001 \rightarrow c_1 = 0011 \)  
- \( m_2 = 0011 \rightarrow c_2 = 0110 \)  
- \( m_3 = 1011 \rightarrow c_3 = 0111 \)  
- \( m_4 = 0111 \rightarrow c_4 = 1110 \)  

c)* Determine the plaintext message for the ciphertext assuming the CBC mode was used for encryption.  
\[ m = c \oplus E_1(c) = 1010 \oplus 0100 = 1110 \]  

d)* Name two weaknesses of the ECB mode.  
- Identical plaintext blocks are encrypted to the same ciphertext with the same key.  
- A change in the order of ciphertext blocks is not detected.  

e)* Calculate the number of keys that can be tested per second using a brute-force attack.  
\[ r = \frac{100 \text{ GB}}{64 \text{ bit}} = 1.25 \times 10^{10} \text{ keys} \]  

f)* Calculate the average time until the correct key is found.  
\[ t \approx \frac{2^{56}}{r} = 33 \text{ days} \]  

g)* What conclusion can you draw regarding the long-term security of the encrypted data based on the above calculation?  
Due to the short key length, it is insecure.  

h)* What criteria must a number meet to be considered a prime number?  
Prime numbers are natural numbers with exactly two divisors, namely themselves and 1.  

Task 6: Short Questions (9 Points)  
The following short questions are independent of each other. Bullet-point answers are sufficient!  

a)* A router fragments an incoming IPv4 packet of size 1280B due to a subsequent MTU of 660B. Provide the values of the IPv4 header fields in the table below. Assume minimal IPv4 headers.  
| Packet/Fragment         | Total Length | DF | MF | Fragment Offset |  
|-------------------------|--------------|----|----|-----------------|  
| Incoming Packet         | 1280         | 0  | 0  | 0               |  
| Outgoing Fragment 1     | 660          | 0  | 1  | 0               |  
| Outgoing Fragment 2     | 640          | 0  | 0  | 80              |  

b)* Describe what is meant by a collision domain.  
The part of a network within which collisions occur when two nodes send simultaneously.  

c)* Describe what is meant by a broadcast domain.  
The entire area of a network that is reachable by a broadcast at Layer 2 (i.e., everything up to the next router).  

d)* What is the essential difference between switching and routing?  
Switching makes forwarding decisions based on Layer 2 addresses, while routing is based on Layer 3 addresses (logical addresses with structure).  

e)* What is meant by a "burst error"?  
The flipping of multiple bits in succession.  

f)* Name one similarity and one difference between a bus and a hub.  
Similarity: Both form collision domains.  
Difference: A hub can amplify signals.  

g)* Provide the data rate \( r = 1 \) Gbit in the unit MiB.  
\[ r = \frac{1 \times 10^9}{2^{20} \times 8} \approx 119.21 \text{ MiB} \]  

h)* An IPv4 address is 4B long. How long is an IPv6 address?  
16B (see supplementary sheet).  

Additional space for solutions – please clearly mark the association with the respective task and strike out invalid solutions!