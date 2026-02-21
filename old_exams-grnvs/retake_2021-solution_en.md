Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during the attendance check by affixing a code sticker.
- This contains only a continuous number, which is also noted on the attendance sticker with SRID here.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Basics of Computer Networks and Distributed Systems  
Exam: IN0010/Retake onsite  
Date: Friday, October 15, 2021  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 11:30–13:00  

### Instructions for Processing
- This exam consists of 16 pages with a total of 5 tasks.  
Please check now that you have received a complete set of information.  
- The total score for this exam is 90.5 points.  
- The removal of pages from the exam is prohibited.  
- The following aids are permitted:  
  - The cheat sheet provided by the chair  
  - A non-programmable calculator  
  - An analog dictionary in German without annotations  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be counted where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Do not write in red/green colors or with a pencil.  
- Turn off all electronic devices you carry, store them in your bag, and close it.  

### Task 1  
Multiple Choice (13 points)  
The following tasks are multiple choice/multiple answer, meaning that at least one answer option is correct for each. Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 0.5 points per correct tick and 0.5 points per incorrect tick. The minimum score per sub-task is 0 points.  

Please mark the correct answers.  
Marked answers can be crossed out by complete filling.  
Crossed-out answers can be marked again by adjacent markings.  

a) *Mark the applicable properties of the information content of a memoryless source:  
- The information content of a predictable symbol is 0 bit.  
- The information content is maximized when each of the N symbols occurs with a probability of 1/N.  
- The more frequently a symbol occurs, the higher its information content.  
- The information content of a string of symbols is the product of the information contents of the individual symbols.  

b) *Let the rectangular impulse \( s(t) \) and the cosine squared impulse \( s(t) \) be given. Figure 1.1 shows four different spectra. Which statements are correct?  
- (a) \( S_1(f) \)  
- (b) \( S_2(f) \)  
- (c) \( S_3(f) \)  
- (d) \( S_4(f) \)  

c) *What conversions are applicable for 1,000,000 bits?  
- 1 MsB  
- 128 KiB  
- 100 KiB  
- 1 Mbit  
- 125 kB  
- 1 MiB  
- 1 Mibit  
- 1000 kbit  

d) *The syscall select()...  
- blocks until at least one socket is ready or a monitored set of sockets.  
- (if specified) a timeout occurs.  
- is only meaningful for TCP sockets.  
- creates a new socket.  
- selects a socket for transmission.  

e) *Which statements about the Routing Information Protocol (RIP) are correct?  
- In case of a route failure, "Count to infinity" occurs.  
- It may take several "rounds" for each router to determine the best next hop.  
- RIP is not used as an Exterior Gateway Protocol (EGP).  
- Since updates are only sent every 15 seconds, a maximum delay of 17 1g5s = 4.25 minutes results.  
- The maximum distance in RIP is 15 hops.  
- RIP supports more complex metrics than hop count depending on the application case.  

f) *Which of the following DNS Resource Records have correct syntax?  
- net.in.tum.de A 89.163.225.145  
- asciiart.grnvs.net. A 89.163.25.145  
- secret.grnvs.net. TXT "Hello World"  
- 145.25.163.89.in-addr.arpa. PTR www.grnvs.net.  
- asciiart.grnvs.net. A 2001:4ba0:ffec:93::0  
- www2.grnvs.net. AAAA www.grnvs.net.  

g) *How many DNS zones must be created below the zone 247.180.180.0/22 to enable a reverse lookup of all IP addresses in the network?  

h) *How many PTR records must be created to enable a reverse lookup of all IP addresses in the network 247.180.180.0/22?  

i) *Which PTR record belongs to the IP address 714::8cf8:9d6?  

j) *What is assigned to the session layer?  

k) *What is assigned to the presentation layer?  

l) *What is assigned to the application layer?  

### Task 2  
Short Tasks (16.5 points)  
a) *Briefly explain the task of channel coding.  
- Purposeful addition of redundancy so that transmission errors can be compensated within certain limits.  

b) *Draw a meaningful signal space assignment for QAM below that cannot be confused with any other modulation method. Ensure a sufficient and sensible number of signal space points!  
- PSK: 8 signal space points on the unit circle around the origin.  
- QAM: 8 signal space points equidistant as a grid around the origin.  

c) *Briefly explain how simplex and half-duplex differ.  
- Simplex is the unidirectional use of a medium. In contrast, half-duplex allows the medium to be used bidirectionally but not simultaneously by both communication partners.  

d) *Name one advantage of packet switching over message switching.  
- Packet switching exhibits lower delays due to serialization times over multiple hops.  

e) *From the lecture, the expression  
\[ T = |1 L \{z \cdot L + L\} + |{dz} + n| \cdot Lh{+zpmax} \]  
is known for calculating the transmission time in packet switching. Briefly explain the three summands.  
- Serialization time of all fragments/packets at the source including headers.  
- Propagation delay over the entire distance.  
- Serialization time of a fragment/packet that occurs at hops.  

f) *From the lecture, the adjacent figure regarding IPv4 address classes is known. Provide the first IP address for each class.  
- A: 0.0.0.0  
- B: 128.0.0.0  
- C: 192.0.0.0  
- D: 224.0.0.0  
- E: 240.0.0.0  

g) *What is the task of TCP congestion control?  
- Prevention of overload in the network.  

h) *What problem occurs with NAT when an ICMP Echo Reply is received, and how is this solved?  
- NAT is based on port numbers, which do not exist in ICMPvP. Instead, the ICMP identifier can be used here.  

i) *What problem occurs with NAT when an ICMP Destination Unreachable/Time Exceeded in Transit is received, and how is this solved?  
- Since this ICMP message is not the response to a request, no entry with an identifier can exist via NAT yet. Instead, the payload of this message contains the IP header as well as the first 8 bytes of the packet that caused the problem. This contains the required IP addresses and port numbers that NAT needs for mapping.  

### Task 3  
Data Compression (22 points)  
In this task, a simplified version of the ITU T.30 protocol, better known as Telefax ("Fax"), is considered. Figure 3.1 shows a 9 x 45 pixel excerpt of a page to be transmitted via fax.  
A simple way is to encode black pixels as a logical 0 and white pixels as a logical 1. We will refer to this type of encoding as a simple code.  

a) *Calculate the length of the data to be transmitted in bits when the page excerpt is encoded with this simple code.  
\[ L = 45 \times 9 \times 1 \text{ bit} = 405 \text{ bit} \]  

b) *Determine the information content of the two code words used.  
- Note: The page excerpt consists of 58 black pixels.  
\[ I(0) = -\log_2 \left( \frac{58}{405} \right) \approx 2.80 \text{ bit} \]  
\[ I(1) = -\log_2 \left( \frac{405 - 58}{405} \right) \approx 0.22 \text{ bit} \]  

c) *Determine the entropy of the page excerpt.  
\[ H = \frac{58}{405} \cdot I(0) + \frac{405 - 58}{405} \cdot I(1) \approx 0.59 \text{ bit} \]  

d) What can be concluded regarding data compression from the result of sub-task c)?  
- The message contains redundancy and can thus be compressed.  

For lossless compression, ITU T.30 uses a combination of run-length encoding (RLE) and subsequent Huffman coding. Initially, the number of consecutive pixels of the same color is encoded along with the respective color value (black or white), for example, 3w or 4s for three consecutive white or four consecutive black pixels.  

e) *Provide the second line of the page excerpt in Figure 3.1 run-length encoded in the solution field below Figure 3.1 (see page 6).  
- 33w 3s 6w 1s 2w s 2  

f) *The Huffman code is a so-called prefix-free code. Explain what is meant by this.  
- No code word is a true prefix of another code word.  

g) *How does the use of prefix-free codes facilitate decompression?  
- Data can be reconstructed immediately when a suitable code word is found (no "lookahead" is necessary).  

h) *Explain what is meant by lossless compression.  
- Removal of redundancy without giving up the ability to reconstruct the original data exactly.  

Across the entire page excerpt, the RLE code words listed in Table 3.1 with specified absolute frequencies result. The total number of RLE code words for the page excerpt is 93.  

| RLE Word | Frequency | Code Word Length [bit] |
|----------|-----------|-------------------------|
| 1s       | 31        | 2                       |
| 2w       | 15        | 3                       |
| 2s       | 8         | 3                       |
| 6w       | 7         | 4                       |
| 1w       | 6         | 4                       |
| 4w       | 5         | 4                       |
| 3w       | 4         | 4                       |
| 5w       | 3         | 5                       |
| 7w       | 2         | 5                       |
| 45w      | 2         | 5                       |
| 33w      | 2         | 5                       |
| 5s       | 1         | 6                       |
| 8w       | 1         | 6                       |

Table 3.1: RLE code words, sorted by frequency in the page excerpt from Figure 3.1.  

i) *Complete the Huffman tree in the solution field. In particular, also consider the missing code words 2s, 2w, and 1s. Provide the corresponding occurrence probabilities for each code word and each internal node.  

j) *Enter the lengths of the code words of the code you constructed in Table 3.1.  

k) *Provide the code words for the symbols 2w, 7w, and 11w of the code you constructed.  
- 2w: 001  
- 7w: 10001  
- 11w: 1111  

l) *Determine the total length of the compressed page excerpt in bits.  
- The result is obtained from the frequency-weighted sum of the code word lengths in Table 3.1:  
\[ L = 2 \text{ bit} (31) + 3 \text{ bit} (15 + 8) + 4 \text{ bit} (7 + 6 + 5 + 4 + 4) + 5 \text{ bit} (3 + 2 + 2 + 2 + 2) + 6 \text{ bit} (1 + 1) = 302 \text{ bit} \]  

m) *Determine the percentage by which the compressed page excerpt is shorter compared to a simple encoding.  
\[ \eta = \frac{405 - 302}{405} = 25.43\% \]  

n) *Explain what information (apart from the compressed data) is still needed on the receiver side for decoding.  
- The receiver must know the code alphabet.  

o) *Name two ways in which the problem from part n) can be solved in practice.  
- Send the alphabet or agree on a general alphabet in advance.  

### Task 4  
Solarlink 2.0 (19 points)  
Due to the colonization of Mars, Solarlink is in demand: An interplanetary satellite network that provides our entire solar system with the Internet. Recently, Solarlink was established as an Internet Service Provider with its own Autonomous System (AS).  

Solarlink has negotiated a Customer-Provider (C2P) connection to the upstream providers Sprint and AT&T. Telemars on Mars and ThePirateStation in the asteroid belt have been won as customers.  

To enable better network measurements at TUM, TUMAS receives direct free access to the Solarlink AS via a Solarlink satellite dish and vice versa.  

a) *What is an AS?  
- A collection of networks under a unified administrative control.  

b) *What is meant by Policy-Based Routing? Provide an example of such a policy.  
- Routing decisions based on criteria other than the objectively best route. These can include costs, router load, preference/rejection of certain networks/countries, etc.  

c) *Justify whether Solarlink is a Tier 1 or Tier 2 provider.  
- Since Solarlink is both a customer of the providers Sprint and AT&T and has customers itself, Solarlink is a Tier 2 provider.  

d) *What advantage does Solarlink have by operating multiple C2P connections to upstream providers?  
- To reach arbitrary subnets on the Internet, a single C2P connection may suffice. However, greater interconnectivity means better fault tolerance, more efficient routing options, and a more even distribution of load on the Internet.  

e) *What type of connection does TUMAS have?  
- In this case, it is a peering connection.  

f) *Describe how this connection to TUMAS differs from a C2P connection.  
- It allows for direct network traffic under better conditions between the ASes. However, Solarlink would not inform the prefixes in TUMAS to avoid unnecessary load in its own network.  

g) *From whom does Solarlink receive money when a connection is used? Consider Sprint, Telemars, and TUMAS. Justify!  
- Solarlink is the upstream provider from which the customer Telemars receives money. TUMAS has a free peering connection, so no money flows there. For network traffic to Sprint, Solarlink must pay.  

### Task 5  
Wireshark (20 points)  
Given is the network from Figure 5.1a. The depicted packet is addressed from PC1 to Srv.  

The offset is the index in the byte array and must be specified as 0-based (as in C or Java). Provide interpreted data such as addresses or ports in their usual and shortened notation.  
Note: Use the printed headers and information on the cheat sheet for the solution.  

a) *Determine the Layer 2 address of the sender.  
- Offset: 0x0006 (6) Length: 6  
- Address: 90:e2:ba:86:dd:60 belongs to node: R1  

b) *Justify which Layer 3 protocol is used.  
- Ethertype 0x0800 = IPv4  

c) *Determine the Layer 3 address of the recipient.  
- Offset: 0x001e (30) Length: 4  
- Address: 10.53.87.251  

d) *Determine the Layer 3 address of the sender.  
- Offset: 0x001a (26) Length: 4  
- Address: 192.168.240.6  

e) *Justify how to recognize that the Layer 3 header has a length of 20 bytes.  
- The lower nibble of the IH field is 0x5, which indicates the length of the IPv4 header in multiples of 4 bytes.  

f) *Clearly mark in Figure 5.1b where it is evident that the IPv4 payload is TCP.  
- Entry point: L4 header (TCP) starts at index 0x0022.  

g) *Provide the destination port. (without justification)  
- 3389  

h) *Provide the exact position (offset and position within the respective byte) of the TCP flags, the flags themselves, and their respective values.  
- Offset: lower 6 bits of the byte at position 0x002f (47)  
- Flag – – URG ACK PSH RST SYN FIN  
- Value 0 0 0 0 1 0  

i) *Provide the minimum length of the TCP header. (without justification)  
- 20 bytes  

j) *Determine the exact length of the TCP header from Figure 5.1b. (with justification)  
- 0xa0 at offset 0x002e contains in the highest 4 bits the field offset (0xa), which indicates the total length of the TCP header in multiples of 4 bytes.  
- The header length thus amounts to 10 x 4 bytes = 40 bytes  

k) *Justify what causes the length difference.  
- Since the header does not have the minimum length, the only explanation is that options are included.  

### Additional Space for Solutions. Clearly mark the assignment to each sub-task.  
Do not forget to cross out invalid solutions.