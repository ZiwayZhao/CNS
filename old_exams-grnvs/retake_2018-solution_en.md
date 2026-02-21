Chair of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  

### Personalization Notes:
- Your exam will be personalized by affixing a code during the attendance check.
- This contains only a sequential number, which is also noted on the attendance lists next to the signature field.
- This will be used as a pseudonym to allow a unique assignment of your exam.

### Basics of Computer Networks and Distributed Systems  
Exam: IN0010/Retake  
Date: Saturday, September 29, 2018  
Examiner: Prof. Dr. Uwe Baumgarten  
Time: 10:30–12:00  

### Instructions for Processing
- This exam consists of:
  - 20 pages with a total of 5 tasks and
  - a double-sided formula collection.
- Please check now that you have received a complete set of documents.
- The removal of pages from the exam is prohibited.
- Tasks marked with *g can be solved without knowledge of the results of previous tasks.
- Only those results will be counted where the solution path is recognizable. Text problems must also be justified unless explicitly stated otherwise in the respective subtask.
- Calculation results must be given rounded to two significant decimal places unless otherwise stated in the respective subtask.
- Do not write with red/green colors or with a pencil.
- The total score for this exam is 90 points.
- Allowed aids:
  - a non-programmable calculator
  - an analog dictionary in the native language without annotations
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.

---

### Task 1  
Short Tasks (13 Points)  
The following subtasks are to be answered independently of each other.

a) *Mark all collision domains in the network below.  
**Important:** When marking, ensure that only the interfaces that are included in the respective collision domain are marked!

b) *Mark all broadcast domains in the network below.  
**Important:** When marking, ensure that only the interfaces that are included in the respective broadcast domain are marked!

c) *How many different MAC addresses are theoretically possible with Ethernet?  
**Answer:** 1,248 = 281,474,976,710,656

d) *Name two routing protocols. (No justification required)  
**Answer:** RIP, OSPF (ISIS, IGRP, EIGRP, BGP,...)

e) *Briefly describe a significant difference between TCP and UDP.  
**Answer:** TCP is connection-oriented, while UDP is connectionless. (TCP is stream-oriented, while UDP is message-oriented.)

f) *Explain the difference between the syscalls recv() and recvfrom().  
**Answer:** Both syscalls can be used with both connectionless and connection-oriented sockets. However, unlike recv(), recvfrom() also provides information about where (source IP and source port) a message was received. Therefore, recv() is usually used with connection-oriented sockets, where the other side is implicitly known, while recvfrom() is mostly used with connectionless sockets.

g) *Name only the necessary syscalls in the correct order to create a socket and connect to a peer.  
**Answer:** socket(), connect()

h) *Give the 32-bit data 0x01 23 45 67 in Little Endian in network byte order.  
**Answer:** 0x67 45 23 01

i) *Convert 10 GiB into Mbit. (Calculation!)  
**Answer:**  
10 GiB = 10^30 B = 85899.35 Mbit

j) *Determine the network and broadcast address of the largest possible subnet that encompasses the addresses 203.0.113.17 and 203.0.113.46.  
**Answer:**  
Network address: 0.0.0.0  
Broadcast: 255.255.255.255

k) *Name the layers (in English or German) of the ISO/OSI model in ascending order starting from layer 1.  
**Answer:**  
Physical Layer, Data Link Layer, Network Layer, Transport Layer, Presentation Layer, Application Layer.

---

### Task 2  
Data Compression (22 Points)  
In this task, we consider a simplified version of the ITU T.30 protocol, better known as fax. Figure 2.1 shows a 9x50 pixel excerpt of a page that is to be transmitted via fax.

**Figure 2.1:** Excerpt from a black/white fax page. The numbers on the left margin indicate the line number, and the numbers on the top margin indicate the column number.

**Solution Field for Subtask f)**  
A simple way is to encode black pixels as a logical 0 and white pixels as a logical 1. We will refer to this type of encoding as simple code.

a) *Calculate the length of the data to be transmitted in bits when the page excerpt is encoded with this simple code.  
**Answer:**  
L = 50 * 9 * 1 bit = 450 bits

b) *Determine the information content of the two code words used.  
**Hint:** The page excerpt consists of 58 black pixels.  
**Answer:**  
I(0) = log2(450/58) ≈ 2.96 bits  
I(1) = log2(450/2) ≈ 0.20 bits

c) *Determine the entropy of the page excerpt.  
**Answer:**  
H = I(0) + I(1) = (58/450) * log2(450/58) + (392/450) * log2(450/392) ≈ 0.55 bits

d) *What can be inferred regarding data compression from the result of subtask c)?  
**Answer:**  
The message contains redundancy and can therefore be compressed.

e) *Explain what is meant by lossless compression.  
**Answer:**  
Removal of redundancy without sacrificing the ability to reconstruct the original data exactly.

f) *Provide the third line of the page excerpt in Figure 2.1 in run-length encoded format in the solution field below Figure 2.1.

g) *The Huffman code is a so-called prefix-free code. Explain what is meant by this.  
**Answer:**  
No code word is a true prefix of another code word.

h) *How does the use of prefix-free codes facilitate decompression?  
**Answer:**  
Data can be reconstructed immediately once a matching code word is found (no "lookahead" is necessary).

**Table 2.1:** RLE Code Words, sorted by frequency in the page excerpt from Figure 2.1. The total number of code words in the page excerpt is 93.

Over the entire page excerpt, the RLE code words listed in Table 2.1 are obtained with their corresponding absolute frequencies. The total number of RLE code words for the complete excerpt is 93.

i) *Complete the Huffman tree in the solution field. Pay particular attention to the missing code words 2s, 3w, and 1s. Provide the corresponding occurrence probabilities for each code word and each internal node.

j) *Provide the code words for the symbols 1s, 13w, and 5s of the code you constructed.  
**Answer:**  
1s: 01  
13w: 00000  
5s: 1011111

k) *Provide the lengths of the code words of the code you constructed. Enter these in Table 2.1.

l) *Determine the total length of the compressed page excerpt in bits.  
**Answer:**  
LH = 31 * 2 + (8 + 8) * 3 + (8 + 6 + 5 + 5) * 4 + (4 + 4 + 4 + 2 + 2 + 2 + 2) * 5 + (1 + 1) * 6 = 318 bits

m) *Determine the percentage by which the compressed page excerpt is shorter compared to a simple encoding.  
**Answer:**  
η = (450 - 318) / 450 = 29.33%

n) *Explain what information (aside from the compressed data) is still needed on the receiver's side for decoding.  
**Answer:**  
The receiver must know the code alphabet.

o) *Name two ways in which the problem from part a) can be solved in practice.  
**Answer:**  
Send the alphabet along or agree on a common alphabet in advance.

---

### Task 3  
DNS and SMTP (18 Points)  
Given is the network topology from Figure 3.1. The PC is in a private network and is connected to the Internet via a common router. The PC uses the public Google resolver to resolve FQDNs. The other servers shown in Figure 3.1 are authoritative name servers for various zones. Details can be found in Table 3.1.

a) *What is the purpose of DNS?  
**Answer:**  
Storage of information that can be retrieved via FQDNs. Mostly, it involves translating FQDNs into IP addresses (or vice versa in the case of reverse zones).

b) *What is a name server?  
**Answer:**  
Name servers store information about the zones for which they are authoritative. This includes resource records as well as information about the delegation of subordinate domains to other name servers.

c) *What is a resolver?  
**Answer:**  
A service that queries information from the DNS.

d) *What is meant by a Fully Qualified Domain Name (FQDN)? (No points for translation into German!)  
**Answer:**  
A series of labels separated by dots and terminated with a trailing dot (root).

The PC attempts to send an email to grnvs@net.in.tum.de. The MX record for the domain net.in.tum.de is mailrelay1.lrz.de. We assume that all caches are empty at the beginning.

e) *What is an MX record?  
**Answer:**  
The specification of a mail server in the form of its FQDN for the respective domain.

f) *Draw all exchanged DNS messages in the form of arrows between the respective end devices directly in Figure 3.1. Number the messages in order starting from 1.

g) *Which messages from part f) belong to a recursive name resolution?  
**Answer:**  
Messages 1 and 8

h) *Which messages from part f) belong to an iterative name resolution?  
**Answer:**  
Messages 2–7

i) *Justify which transport protocol is used for the exchanged messages.  
**Answer:**  
UDP is usually used, as establishing individual TCP connections is not worth it (time for the 3-way handshake). (An exception is made for messages that are larger than 512 bytes. These must be transmitted over TCP in DNS.)

The PC now receives the IP address 129.187.255.133 from mailrelay1.lrz.de. The following commands are executed manually on the PC (gray lines are server responses):

1. ~ # telnet 129.187.255.133 25  
2. 220 mailrelay1.lrz.de ESMTP Postfix  
3. HELO  
4. 250 mailrelay1.lrz.de  
5. MAIL FROM:<moepi@moepi.net>  
6. 250 2.1.0 Ok  
7. RCPT TO:<grnvs@net.in.tum.de>  
8. 250 2.1.5 Ok  
9. DATA  
10. 354 End data with <CR><LF>.<CR><LF>  
11. Subject: [GRNVS] Klausur  
12. Dear Mr. Baumgarten, (...)  
13. .  
14. 250 2.0.0 Ok: queued as 42Jnd62QzjzyYs  

j) *What exactly does the command in line 1 accomplish?  
**Answer:**  
Establishes a connection from the PC to 129.187.255.133 via TCP on port 25.

k) *Create a simple time-sequence diagram from the perspective of the transport layer that represents the communication process caused by the above commands from line 1 to including line 4.  
**Hints:**  
1. Commands (messages) are triggered by a line break.  
2. Characters are transmitted in ASCII encoding (line break corresponds to 1B).  
3. Provide flags, sequence/acknowledgment numbers, and the length of the payload for each message.

---

### Task 4  
NAT and Static Routing (14 Points)  
We consider the network from Figure 4.1. PC1 and PC2 are connected to each other and to router R1 via switch S. In the local network, the subnet 172.29.50.0/26 is used. Router R1 is connected to a transport network of prefix length 30 with R2, which represents the gateway to the Internet on the side of a service provider.

a) *Assign PC1 the smallest usable IP from the subnet. Enter this directly in Figure 4.1.

b) *Assign R1.eth0 the largest usable IP from the subnet. Enter this directly in Figure 4.1.

c) *Assign R1.eth1 an address from the transport network. Enter this directly in Figure 4.1.

d) *What transport protocol and destination port are used when PC1 accesses https://www.tum.de/?  
**Answer:**  
TCP 443

In the following, we will shorten IP and MAC addresses according to the schema <Device>.<Interface>, e.g., R1.eth0 for the corresponding address at interface eth0 of router R1.  
R1 supports NAT to allow PCs access to the Internet. The mapping occurs as discussed in the lecture via the global port, but R1 also stores additional data.  
PC2 has already communicated with hosts on the Internet. The NAT table of R1 is shown below.

| Prot. | Local IP        | Local Port | Global IP       | Global Port | Remote IP       | Remote Port |
|-------|-----------------|------------|------------------|-------------|------------------|-------------|
| tcp   | 172.29.50.1     | 53050      | R1.eth1          | 53050       | tum.eth0         | 443         |
| tcp   | 172.29.50.1     | 55222      | R1.eth1          | 55222       | lmu.eth0         | 80          |
| tcp   | 172.29.50.2     | 55222      | R1.eth1          | 55223       | tum.eth0         | 443         |

e) *PC1 is now accessing www.tum.de. A random source port of 55222 is used. Complete Table 4.1 with the entries that arise here.

**Note:** For the following subtasks, also note that there are four additional routers between R2 and R3.

f) *Complete the header fields for the request from PC1 to www.tum.de in the three empty boxes in Figure 4.2. If a field cannot be determined unambiguously, make a reasonable choice.  
**Hints:**  
1. If you could not solve subtask d), assume destination port 80.  
2. IP and MAC addresses can be abbreviated according to the schema <Device>.<Interface>, e.g., PC2.eth0.  
3. The hostname of the server hosting www.tum.de can be abbreviated as "tum".

g) *Complete the header fields for the response from www.tum.de to PC1 in the three empty boxes in Figure 4.3. If a field cannot be determined unambiguously, make a reasonable choice.  
**Hints:**  
1. IP and MAC addresses can be abbreviated according to the schema <Device>.<Interface>, e.g., PC2.eth0.  
2. The hostname of the server hosting www.tum.de can be abbreviated as "tum".

---

### Task 5  
Voyager 1 and the Moepis (Sampling and Quantization) (23 Points)  
The Moepis discovered a crater on their planet Gliese 587c one day. Inside, they find a dented aluminum shell and a golden disc. On the cover of the golden disc are some strange drawings. The Moepis are now trying to decipher the message.

A wise Moepi concludes that the drawing at the bottom right in the figure could represent the hyperfine structure transition of the hydrogen atom. This transition has a frequency of 1420 MHz. Thus, it creates both a time unit (period duration) and a length unit (wavelength). These universal units are used as a scale for all other specifications of the drawings. All numerical values are given in binary with | as 1 and – as 0.

a) *Calculate the universal time unit and provide it in seconds.  
**Answer:**  
T = 1 / 1420 MHz = 0.7 * 10^(-9) s

b) *Calculate the universal length unit and provide it in meters.  
**Answer:**  
λ = c / 1420 MHz = 3 * 10^8 m/s / 1420 MHz = 0.21 m

On the right half of the figure, it is explained how images can be reconstructed from the played sounds. The third drawing on the right side shows that images consist of vertical "scan lines," specifically 1,000,000,000 = 512 pieces (see binary representation using | and – in the drawing). The first three scan lines are schematically represented in the top drawing.

c) *How long does it take to play one scan line? (Derivation/Calculation)  
**Answer:**  
t = 11845632 * 0.7 * 10^(-9) s = 8.29 ms

d) *The images have (as depicted) an aspect ratio of 4:3. At what rate should the Moepis sample the scan lines?  
**Hint:** If you could not solve subtask c), assume t = 8.29 ms for one scan line.  
**Answer:**  
f = 512 / (4 * 8.29 ms) = 46.32 kHz

To validate the findings, another Moepi suggests first creating a preview image of lower quality (8x6 pixels). For this, only 8 representative scan lines should be examined, with only 6 pixels to be reconstructed from each. The scan lines are shown in the figure. The preview image should also only contain black and white (no grayscale).

e) *Justify how many sample values are necessary per scan line for the preview image.  
**Answer:**  
Since 6 pixels are to be reconstructed per scan line, 6 samples are also necessary.

f) *Mark all sampling time points for scan line 32 in the figure.

g) *Determine the quantization intervals and quantization levels so that the maximum quantization error in the interval [-1;1] is minimal.  
**Answer:**  
Two states (black/white) should be recognized. The quantization intervals are [-1;0] and (0;1] with quantization levels 0.5 (white) and -0.5 (black).

h) *Draw the quantized (not the sampled) signal for scan line 96 in the figure.

i) *Draw the sampled and quantized signal for scan line 160 in the figure.

j) *Create the preview image in the figure. Also mark the sample values of the other scan lines in the figure.

---

### Additional Pages  
Additional space for solutions. Clearly mark the assignment to the respective subtask.  
Do not forget to cross out invalid solutions.