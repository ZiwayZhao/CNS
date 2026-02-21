Name First Name  
Grade  
Degree Program (Major) Specialization (Minor)  
I II  
Student ID  
Signature of the Candidate  

TECHNICAL UNIVERSITY OF MUNICH  
Faculty of Computer Science  

Midterm  
Endterm  
× Retake  

Exam Subject: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle Date: 22.09.2014  
Lecture Hall: Row: Seat:  

To be filled out by the supervisor only:  
Lecture hall left from: until:  
Submitted early at:  
Special remarks:  
Retake Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
Monday, 22.09.2014  
11:30 AM – 1:00 PM  

- This exam consists of 19 pages and a total of 6 tasks, as well as an additional distributed aid sheet with protocol headers. Please check now that you have received a complete set of materials.  
- Please write your name and student ID in the header of each page.  
- Do not write in red/green ink or with a pencil.  
- The total number of points is 85.  
- Allowed aids are a double-sided handwritten DIN A4 sheet and a non-programmable calculator. Please remove all other materials from your desk, turn off your mobile phones, and put them away.  
- Tasks marked with * can be solved without knowledge of the results of preceding subtasks.  
- Do not spend too long on a (sub)task. If you cannot solve the task immediately, it is better to move on to the next task.  
- Only results where a solution path is recognizable will be graded. Text problems must generally be justified unless explicitly stated otherwise in the respective subtask.  

1 Name:  
Task 1 Fourier Series Again (13 Points)  

Given is the periodic signal depicted in Figure 1.1, which is to be represented as a Fourier series:  
\[ s(t) = a_0 + \sum_{k=1}^{\infty} (a_k \cos(k \omega t) + b_k \sin(k \omega t)) \]  
The coefficients for all integers can be determined as follows:  
\[ a_k = \frac{1}{T} \int_{-T/2}^{T/2} s(t) \cos(k \omega t) dt, \quad b_k = \frac{1}{T} \int_{-T/2}^{T/2} s(t) \sin(k \omega t) dt. \]  

a) * Justify why this basic impulse is not free of direct current.  
b) * Determine the period duration and angular frequency of the signal.  
c) * Provide an analytical expression for the sending basic impulse, i.e., for \( s(t) \) in the interval \( t \in [-\pi, \pi) \).  
d) * Determine the DC component \( a_0 \).  
e) * What can be said about \( a_k \) and \( b_k \) for \( k > 0 \)? (Justification!)  
f) * Determine the cosine components for \( k > 0 \).  
g) * Determine the sine components for \( k > 0 \).  
h) * Sketch the approximated signal \( s'(t) = a_0 + a \cos(\omega t) + b \sin(\omega t) \) in Figure 1.1.  

Task 2 Framed Slotted ALOHA (15 Points)  

We will now consider Framed Slotted ALOHA, an extension of Slotted ALOHA, which can be used as a medium access method in RFID. We assume that a set of stations, referred to as Tags, communicate with a so-called Reader. In this task, we will only consider one application case, namely the detection of various Tags by the Reader. This occurs as follows:  
- The Reader sends the frame length to all Tags within range. The frame length is a natural number that indicates the number of slots.  
- Each Tag \( T_i \) randomly and uniformly selects a slot \( S_j \), during which its own identifier is sent to the Reader.  
- If multiple Tags send in the same slot, a collision occurs. This is detected by the Reader through the checksum verification.  
- A slot in which identification succeeds, i.e., exactly one Tag sends, is referred to as a Discovery Slot.  

a) * What type of multiplexing method is this?  
b) * Determine the probability that a Tag sends in slot \( S_j \).  
Let \( X_j \) be the random variable that indicates the number of Tags sending simultaneously during slot \( S_j \). This depends on the number of slots in the frame and the number of Tags \( n \).  
c) * Determine the probability that slot \( S_j \) is a Discovery Slot.  

Now assume \( n = 10 \) Tags and a frame length of \( s = 20 \) slots.  
d) Calculate the probability from part c) as a numerical value.  
e) * Determine the maximum number of identifiable Tags in a frame as a function of the frame length and the number of Tags.  
f) * Justify what problem arises when \( n \ll s \), i.e., the number of Tags is significantly smaller than the number of slots.  
g) * Justify what problem arises when \( n \gg s \), i.e., the number of Tags is significantly larger than the number of slots.  

Assume a data rate of \( r = 2400 \) bit for the Tags. The size of a sent identifier with checksum is \( l = 12B \).  
h) * Determine the duration of a slot.  
i) * Provide the general probability that no Tag sends in slot \( S_j \).  
j) * Determine the expected time in seconds within a frame during which no Tag sends.  
k) * Determine the counting density (discrete probability density).  
l) * What distribution is underlying?  

Task 3 Hexfun (21 Points)  

Given is the hex dump from Figure 3.1, which represents an 86B long frame (Ethernet without FCS). The left column indicates the offset (hexadecimal) in multiples of bytes. The two subsequent columns represent the data (hexadecimal) in blocks of 8 bytes in Network Byte Order.  

0x0000: 08 60 6e 45 dc e6 00 1c 14 01 4e 18 86 dd 60 00  
0x0010: 00 00 00 20 06 40 2a 01 04 f8 0d 16 19 43 00 00  
0x0020: 00 00 00 00 00 02 2a 02 02 e0 03 fe 10 01 77 77  
0x0030: 77 2e 00 02 00 85 ce 44 00 50 9b 94 59 c9 2f e7  
0x0040: 5d 10 50 10 65 00 85 88 00 00 47 45 54 20 2f 68  
0x0050: 65 78 0d 0a 0d 0a  

a) * What is the difference between "Host Byte Order" and "Network Byte Order"?  
b) * Justify why it is necessary to distinguish between Host Byte Order and Network Byte Order.  
c) The value 0x12 has the byte order Little-Endian. Provide the value in Big-Endian.  

For the following subtasks, it is helpful to mark the beginning and end of the respective headers in Figure 3.1. Please note that the following subtasks will only be graded if it is clear how you arrived at the answer (e.g., indicating the values of the relevant header fields).  
d) * Provide the offset in bytes for the first and last byte of the Ethernet header from the beginning of the frame.  
e) * What protocol is used at layer 3?  
f) * Provide the function and value of the layer 3 header fields that must be changed during transport by routers.  
g) * What is the length of the layer 3 SDU?  
h) * Mark the sender and receiver address in the layer 3 header. (Draw it directly in Figure 3.1 and indicate which address belongs to the sender and which to the receiver.)  
i) * How can you tell that TCP is used as the layer 4 protocol?  

Figure 3.2 shows the layer 4 PDU (TCP) of the frame depicted in Figure 3.1. This will be further examined.  

0x0000: ce 44 00 50 9b 94 59 c9 2f e7 5d 10 50 10 65 00  
0x0010: 85 88 00 00 47 45 54 20 2f 68 65 78 0d 0a 0d 0a  

j) * Provide the source port of the message in decimal representation.  
k) * Provide the destination port of the message in decimal representation.  
l) * For which application layer protocol is the message apparently intended?  
m) * Provide two reasons why, based on the information you have, you cannot determine how many bytes have already been exchanged over this TCP connection.  
n) * What is the size of the TCP payload for the application layer?  
o) * Can data still be transmitted in the same direction after this segment within the ongoing TCP connection?  
p) * Can data still be transmitted in the opposite direction after this segment within the ongoing TCP connection?  

Task 4 Domain Name System (15 Points)  

First, consider the DNS structure shown in Figure 4.1.  

a) * Briefly explain what DNS is used for.  
b) * Assign DNS to a layer in the ISO/OSI model. (No justification necessary)  
c) * Mark and name all name components for the FQDN www.tum.de.  

Now also consider the zone file for in.tum.de shown in Figure 4.2. This zone has an authoritative DNS server named nsa.in.tum.de.  

```
$ORIGIN in.tum.de.  
$TTL 1H  
@ IN SOA nsa.in.tum.de. admin.in.tum.de. (...)  
in.tum.de. IN NS nsa.in.tum.de.  
in.tum.de. IN MX 10 gchq.in.tum.de.  
nsa.in.tum.de. IN A 131.159.0.1  
www.in.tum.de. IN A 168.144.144.106  
gchq.in.tum.de. IN A 131.159.0.76  
```

d) * Mark the lines in Figure 4.2 that contain the address records for hosts.  
e) * What function does the MX record have?  
f) * Complete Figure 4.1 based on the information from the zone file in Figure 4.2.  
g) * What possibilities arise when multiple FQDNs point to the same IP address?  
h) * What advantages can it have when multiple IP addresses are assigned to one FQDN?  

Now consider the network topology shown in Figure 4.3. The client uses the router as a gateway to the internet and as a recursive DNS server (so-called resolver). The router, in turn, uses ns.tele.com as a resolver for recursive name resolution. All other DNS servers use iterative name resolution, allowing only recursion for ns.tele.com. The authoritative name servers for the respective zones are listed in Table 4.1.  

i) * Explain the difference between recursive and iterative name resolution.  

Assuming that all DNS caches are initially empty:  
j) The client wants to access www.tum.de. Draw all necessary DNS messages in Figure 4.3 using arrows and number them in order. The first message is already provided as assistance.  
k) Immediately afterwards, the client wants to resolve www.in.tum.de. Briefly explain how this resolution differs from that in part j).  

Task 5 Encryption (12 Points)  

In this task, we consider a binary block cipher with a block size of \( n = 4 \) bits. The encryption is realized through a permutation of the bits.  
a) * Calculate the number of possible keys.  
Using the specific permutation  
\[ \pi = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 4 & 1 & 2 & 3 \end{pmatrix} \]  
as the initialization vector.  
b) * Encrypt the plaintext using the ECB mode.  
c) * Determine the plaintext message for the ciphertext assuming that the CBC mode was used for encryption.  
d) * Name two weaknesses of the ECB mode.  

A method for breaking encryption is the so-called brute-force attack. Here, all possible keys are applied to a ciphertext, and the result is compared with a known plaintext until the correct key is determined.  
Assuming a 56-bit key was used with a block size of \( n' = 64 \) bits. You have a ciphertext and the corresponding plaintext. Furthermore, you are able to encrypt or decrypt 100GB per second.  
e) * Calculate the number of keys that can be tested per second in this way.  
f) * Calculate the average time until the correct key is found.  
g) * What conclusion can you draw regarding the long-term security of the encrypted data based on the above calculation?  
h) * What criteria must a number meet to be considered a prime number?  

Task 6 Short Questions (9 Points)  

The following short questions are independent of each other. Bullet-point answers are sufficient!  
a) * A router fragments an incoming IPv4 packet of size 1280B due to a subsequent MTU of 660B. Provide the values of the IPv4 header fields in the following table. Assume minimal IPv4 headers.  
b) * Describe what is meant by a collision domain.  
c) * Describe what is meant by a broadcast domain.  
d) * What is the essential difference between switching and routing?  
e) * What is meant by a "burst error"?  
f) * Name one similarity and one difference between a bus and a hub.  
g) * Provide the data rate \( r = 1 \) Gbit in the unit MiB.  
h) * An IPv4 address is 4B long. How long is an IPv6 address?  

Additional space for solutions – please clearly mark the affiliation with the respective task and cross out invalid solutions!