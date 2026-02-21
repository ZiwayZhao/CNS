Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be analyzed during attendance control by affixing a code sticker.
- This contains only a sequential number, which is also noted on the attendance sticker with SRID here.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Basics of Computer Networks and Distributed Systems  
Exam: IN0010/Retake onsite  
Date: Friday, October 15, 2021  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 11:30–13:00  

### Instructions for Processing
- This exam consists of 16 pages with a total of 5 tasks. Please check now that you have received a complete set of information.
- The total score for this exam is 90.5 points.
- The tearing out of pages from the exam is prohibited.
- The following aids are permitted:
  - The cheat sheet provided by the chair
  - A non-programmable calculator
  - An analog dictionary in the native language without annotations
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only those results will be counted where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write with red/green colors or with pencil.
- Turn off all electronic devices you carry, store them in your bag, and close it.

### Task 1  
Multiple Choice (13 Points)  
The following tasks are multiple choice/multiple answer, meaning that at least one answer option is correct. Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 0.5 points per correct mark and 0.5 points per incorrect mark. The minimum score per sub-task is 0 points.

Please mark the correct answers.  
Marked answers can be crossed out by filling them completely.  
Crossed-out answers can be re-marked by adjacent markings.

a) *Mark the relevant properties of the information content of a memoryless source:  
- The information content of a predictable symbol is 0 bit.  
- The information content is maximized when each of the N symbols occurs with a probability of 1/N.  
- The more frequently a symbol occurs, the higher its information content.  
- The information content of a string of symbols is the product of the information contents of the individual symbols.  

b) *Given the rectangle impulse \( s(t) \) and the cos² impulse \( s(t) \). Figure 1.1 shows four different spectra. Which statements are correct?  
- (a) \( S_1(f) \)  
- (b) \( S_2(f) \)  
- (c) \( S_3(f) \)  
- (d) \( S_4(f) \)  

c) *Which conversions are correct for 1,000,000 bits?  
- 1 MB  
- 128 KiB  
- 100 KiB  
- 1 mbit  
- 125 kB  
- 1 MiB  
- 1 Mibit  
- 1000 kbit  

d) *The syscall select()...  
- blocks until at least one socket is ready or monitors a set of sockets.  
- (if specified) a timeout occurs.  
- is only meaningful for TCP sockets.  
- creates a new socket.  
- selects a socket for transmission.  

e) *Which statements about the Routing Information Protocol (RIP) are correct?  
- In case of a route failure, "Count to infinity" occurs.  
- It may take several "rounds" for each router to determine the best next hop.  
- RIP is not used as an Exterior Gateway Protocol (EGP).  
- Since updates are only sent every 15 seconds, there is a maximum delay of 17 * 15 seconds = 4.25 minutes.  
- The maximum distance for RIP is 15 hops.  
- RIP supports more complex metrics than hop count depending on the application case.  

f) *Which of the following DNS Resource Records have correct syntax?  
- net.in.tum.de A 89.163.225.145  
- asciiart.grnvs.net. A 89.163.25.145  
- secret.grnvs.net. TXT "Hello World"  
- 145.25.163.89.in-addr.arpa. PTR www.grnvs.net.  
- asciiart.grnvs.net. A 2001:4ba0:ffec:93::0  
- www2.grnvs.net. AAAA www.grnvs.net.  

g) *How many DNS zones must be created below the zones 247 and 180 at a minimum to enable a reverse lookup of all IP addresses in the network 247.180.180.0/22?  
- 226  
- 43  
- 6  
- 4  
- 144  
- 1  
- 218  
- 256  

h) *How many PTR records must be created to enable a reverse lookup of all IP addresses in the network 247.180.180.0/22?  
- 1024  
- 256  
- 65536  
- 1062  
- 119  
- 996  
- 1  

i) *Which PTR record belongs to the IP address 714::8cf8:9d6?  
- 09d6.8cf8.0000.0000.0000.0000.0000.0714.ip6.arpa.  
- 6d90.8fc8.0000.0000.0000.0000.0000.4170.ip6.arpa.  
- 6.d.9.0.8.f.c.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.4.1.7.0.ip6.arpa.  
- 4170.0000.0000.0000.0000.0000.8fc8.6d90.ip6.arpa.  
- 0.7.1.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.c.f.8.0.9.d.6.ip6.arpa.  

j) *What is assigned to the session layer?  
- TLS  
- URL  
- HTTP methods  
- HTTP cookies  
- TCP  
- HTML  
- Encryption  
- DNS  

k) *What is assigned to the presentation layer?  
- Encryption  
- TCP  
- HTTP methods  
- DNS  
- URL  
- HTTP cookies  
- JSON  
- TLS  

l) *What is assigned to the application layer?  
- DNS  
- JSON  
- Huffman code  
- HTTP  
- UTF-8  
- UDP  
- TLS  
- ASCII  

### Task 2  
Short Tasks (16.5 Points)  
a) *Briefly explain the task of channel coding.  

b) *Draw a meaningful signal space assignment for QAM in the diagram below that cannot be confused with any other modulation method. Pay attention to a sufficient and meaningful number of signal space points!  

c) *Briefly explain how simplex and half-duplex differ.  

d) *Name one advantage of packet switching over message switching.  

e) *From the lecture, the expression  
\[ T = |1 L \{ z \cdot L + L \} + | \{ dz \} + n | \cdot L h \{ + zp_{max} \} \]  
is known for calculating the transmission time in packet switching. Briefly explain the three summands.  
Note: The meaning of the individual variables is not being asked.  

f) *From the lecture, the adjacent figure on IPv4 address classes is known. Give the first IP address for each class.  

g) *What is the task of TCP congestion control?  

h) *What problem occurs with NAT when an ICMP Echo Reply is received, and how is this solved?  

i) *What problem occurs with NAT when an ICMP Destination Unreachable/Time Exceeded in Transit is received, and how is this solved?  

### Task 3  
Data Compression (22 Points)  
In this task, a simplified version of the ITU T.30 protocol, better known as fax ("Fax"), is considered. Figure 3.1 shows a 9 x 45 pixel excerpt of a page that is to be transmitted via fax.  

A simple way is to encode black pixels as a logical 0 and white pixels as a logical 1. We will refer to this type of encoding as a simple code.  

a) *Calculate the length of the data to be transmitted in bits when the page excerpt is encoded with this simple code.  

b) *Determine the information content of the two code words used.  
Note: The page excerpt consists of 58 black pixels.  

c) *Determine the entropy of the page excerpt.  

d) What can be concluded regarding data compression from the result of sub-task c)?  
For lossless compression, ITU T.30 uses a combination of run-length encoding (RLE) and subsequent Huffman coding. To do this, the number of consecutive pixels of the same color along with the respective color value (black or white) is encoded line by line, for example, 3w for three consecutive white pixels or 4s for four consecutive black pixels.  

e) *Provide the second line of the page excerpt in Figure 3.1 run-length encoded in the solution field below Figure 3.1 (see page 6).  

f) *The Huffman code is a so-called prefix-free code. Explain what is meant by this.  

g) *In what way does the use of prefix-free codes facilitate decompression?  

h) *Explain what is meant by lossless compression.  

### Task 4  
Solarlink 2.0 (19 Points)  
With the colonization of Mars, Solarlink is in demand: An interplanetary satellite network that provides our entire solar system with Internet access. Recently, Solarlink has become an Internet Service Provider with its own Autonomous System (AS).  

Solarlink has negotiated a Customer-Provider (C2P) connection to upstream providers Sprint and AT&T. Telemars on Mars and ThePirateStation in the asteroid belt have been won as customers.  

To enable TUM to conduct better network measurements, TUMAS receives direct free access to the Solarlink AS via a Solarlink satellite dish and vice versa.  

a) *What is an AS?  

b) *What is meant by Policy-Based Routing? Also provide an example of such a policy.  

c) *Justify whether Solarlink is a Tier 1 or Tier 2 provider.  

d) *What advantage does Solarlink have in operating multiple C2P connections to upstream providers?  

e) *What is the type of connection to TUMAS called?  

f) *Describe how this connection to TUMAS differs from a C2P connection.  

g) *From whom does Solarlink receive money when a connection is used? Consider Sprint, Telemars, and TUMAS. Justify!  

h) *Draw the shortest path tree starting from SL4 in Figure 4.1.  

i) *Assign the smallest possible IP address in the respective subnet to the interfaces of SL4.  

j) *Fill in the following static routing table of SL4 so that all bolded subnets and the Earth from Figure 4.1 are reachable. Take the route with the minimal costs. By default, send to Earth. Sort the entries according to Longest Prefix Matching.  

k) SL4 receives a packet at the IP address 188.52.4.40. From which interface is it forwarded?  

l) *Provide the corresponding destination from the routing table of SL4 for this packet.  

### Task 5  
Wireshark (20 Points)  
Given is the network from Figure 5.1a. The depicted packet is directed from PC1 to Srv.  

The offset is the index in the byte array and must be specified as 0-based (as in C or Java). Provide interpreted data such as addresses or ports in their usual and shortened notation.  
Note: Use the header and information printed on the cheat sheet for the solution.  
Example: Determine the Layer 2 address of the recipient.  
Offset: 0x0000 Length: 6  
Address: 90:e2:ba:2a:8d:97 belongs to node: <Name>  

a) *Determine the Layer 2 address of the sender.  
Offset: Length:  
Address: belongs to node:  

b) *Justify which Layer 3 protocol is used.  

c) *Determine the Layer 3 address of the recipient.  
Offset: Length:  
Address:  

d) *Determine the Layer 3 address of the sender.  
Offset: Length:  
Address:  

e) *Justify how to recognize that the L3 header has a length of 20 bytes.  

f) *Clearly mark in Figure 5.1b the point that indicates that the IPv4 payload is TCP.  
Re-entry: The L4 header (TCP) starts at index 0x0022.  

g) *Provide the destination port. (without justification)  

h) *Provide the exact position (offset and position within the respective byte) of the TCP flags, the flags themselves, and their respective values.  
Offset:  
Flag  
Value  

i) *Provide the minimum length of the TCP header. (without justification)  

j) *Determine the exact length of the TCP header from Figure 5.1b. (with justification)  

k) *Justify what causes the length difference.  

### Additional Space for Solutions. Clearly mark the assignment to each sub-task.  
Do not forget to cross out invalid solutions.