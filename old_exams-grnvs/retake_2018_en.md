Chair of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  

**Personalization Notes:**  
- Your exam will be personalized by affixing a code during attendance control.  
- This contains only a sequential number, which is also noted on the attendance lists next to the signature field.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Retake  
Date: Saturday, September 29, 2018  
Examiner: Prof. Dr. Uwe Baumgarten  
Time: 10:30–12:00  

**A1 A2 A3 A4 A5**  
I  
II  

**Instructions for Completion**  
- This exam consists of:  
  - 20 pages with a total of 5 tasks as well as  
  - a double-sided printed formula collection.  
- Please check now that you have received a complete set of information.  
- The removal of pages from the exam is prohibited.  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be counted where the solution path is recognizable. Text problems must also be justified unless explicitly stated otherwise in the respective subtask.  
- Calculation results should be given rounded to two significant decimal places unless stated otherwise in the respective subtask.  
- Do not write with red/green colors or with pencil.  
- The total score for this exam is 90 points.  
- Allowed aids:  
  - a non-programmable calculator  
  - an analog dictionary in the native language without annotations  
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.  

**Task 1**  
Short Tasks (13 Points)  
The following subtasks are to be answered independently of each other.  

a) *Mark all collision domains in the network below.  
**Important:** Ensure that only the interfaces that are included in the respective collision domain are marked!  

b) *Mark all broadcast domains in the network below.  
**Important:** Ensure that only the interfaces that are included in the respective broadcast domain are marked!  

c) *How many different MAC addresses are theoretically possible in Ethernet?  

d) *Name two routing protocols. (no justification required)  

e) *Briefly describe one essential difference between TCP and UDP.  

f) *Explain the difference between the syscalls recv() and recvfrom().  

g) *Name only the necessary syscalls in the correct order to create a socket and connect to a peer.  

h) *Provide the 32-bit date 0x01 23 45 67 in little-endian format in network byte order.  

i) *Provide 10 GiB in Mbit. (Calculation!)  

j) *Determine the network and broadcast address of the largest possible subnet that includes the addresses 203.0.113.17 and 203.0.113.46.  

k) *Name the layers (in English or German) of the ISO/OSI model in ascending order starting from layer 1.  

**Task 2**  
Data Compression (22 Points)  
In this task, we consider a simplified version of the ITU T.30 protocol, better known as fax. Figure 2.1 shows a 950-pixel-sized excerpt of a page that is to be transmitted via fax.  

**Figure 2.1:** Excerpt of a black/white fax page. The numbers on the left margin indicate the line number, and the numbers on the top margin indicate the column number.  

**Solution Field for Subtask f)**  
A simple way is to encode black pixels as logical 0 and white pixels as logical 1. We will refer to this type of encoding as simple code.  

a) *Calculate the length of the data to be transmitted in bits when the page excerpt is encoded with this simple code.  

b) Determine the information content of the two code words used.  
**Note:** The page excerpt consists of 58 black pixels.  

c) Determine the entropy of the page excerpt.  

d) What can be inferred regarding data compression from the result of part c)?  

For lossless compression, ITU T.30 uses a combination of run-length encoding (RLE) and subsequent Huffman coding. First, the number of consecutive pixels of the same color is encoded line by line along with the respective color value (black or white), for example, 3w for three consecutive white or 4s for four consecutive black pixels.  

e) *Explain what is meant by lossless compression.  

f) *Provide the third line of the page excerpt in Figure 2.1 run-length encoded in the solution field below Figure 2.1.  

g) *The Huffman code is a so-called prefix-free code. Explain what is meant by that.  

h) How does the use of prefix-free codes facilitate decompression?  

**Table 2.1:** RLE code words sorted by frequency in the page excerpt from Figure 2.1. The total number of code words in the page excerpt is 93.  

i) *Complete the Huffman tree in the solution field. In particular, consider the missing code words 2s, 3w, and 1s. Provide the corresponding occurrence probabilities for each code word and each internal node.  

j) *Provide the code words for the symbols 1s, 13w, and 5s of the code you constructed.  

k) *Provide the lengths of the code words of the code you constructed. Enter these in Table 2.1.  

l) *Determine the total length of the compressed page excerpt in bits.  

m) *Determine the percentage by which the compressed page excerpt is shorter compared to a simple encoding.  

n) *Explain what information (apart from the compressed data) is still needed on the receiver's side for decoding.  

o) Name two ways in which the problem from part a) can be solved in practice.  

**Task 3**  
DNS and SMTP (18 Points)  
Given is the network topology from Figure 3.1. The PC is in a private network and is connected to the Internet via a regular router. The PC uses the public Google resolver to resolve FQDNs. The other servers shown in Figure 3.1 are authoritative name servers for different zones. Details can be found in Table 3.1.  

**Figure 3.1:** Network topology  

| Zone | Authoritative Name Server |  
|------|---------------------------|  
| .    | a.root-servers.net., b.root-servers.net. |  
| de.  | f.nic.de., n.de.net. |  
| tum.de. | dns1.lrz.de., dns2.lrz.bayern. |  
| lrz.de. | dns1.lrz.de., dns2.lrz.bayern. |  
| in.tum.de. | dns1.lrz.de., dns2.lrz.bayern. |  
| net.in.tum.de. | dns1.lrz.de., dns2.lrz.bayern. |  

a) *What is the purpose of DNS?  

b) *What is a name server?  

c) *What is a resolver?  

d) *What is meant by a Fully Qualified Domain Name (FQDN)? (no points for translation into German!)  

From the PC, an attempt is made to send an email to grnvs@net.in.tum.de. The MX record for the domain net.in.tum.de is mailrelay1.lrz.de. We assume that all caches are empty at the beginning.  

e) *What is meant by an MX record?  

f) *Directly draw all exchanged DNS messages in the form of arrows between the respective end devices in Figure 3.1. Number the messages in order starting from 1.  

g) Which messages from part f) belong to a recursive name resolution?  

h) Which messages from part f) belong to an iterative name resolution?  

i) Justify which transport protocol is used for the exchanged messages.  

The PC then receives the IP address 129.187.255.133 for mailrelay1.lrz.de. The following commands are executed manually on the PC (gray lines are server responses):  

1 ~ # telnet 129.187.255.133 25  
2 220 mailrelay1.lrz.de ESMTP Postfix  
3 HELO  
4 250 mailrelay1.lrz.de  
5 MAIL FROM:<moepi@moepi.net>  
6 250 2.1.0 Ok  
7 RCPT TO:<grnvs@net.in.tum.de>  
8 250 2.1.5 Ok  
9 DATA  
10 354 End data with <CR><LF>.<CR><LF>  
11 Subject: [GRNVS] Klausur  
12 Dear Mr. Baumgarten, (...)  
13  
14 .  
15 250 2.0.0 Ok: queued as 42Jnd62QzjzyYs  

j) *What exactly does the command in line 1 do?  

k) Create a simple time-delay diagram from the perspective of the transport layer, which represents the communication process caused by the above commands from line 1 to including line 4. Notes:  
- Commands (messages) are triggered by a line break.  
- Characters are transmitted in ASCII encoding (line break corresponds to 1B).  
- Provide flags, sequence/acknowledgment numbers, and the length of the payload for each message.  

**Task 4**  
NAT and Static Routing (14 Points)  
We consider the network from Figure 4.1. PC1 and PC2 are connected to each other and to router R1 via switch S. In the local network, the subnet 172.29.50.0/26 is used. Router R1 is connected to R2 via a transport network with a prefix length of 30, which represents the gateway to the Internet on the side of a service provider.  

**Figure 4.1:** Network topology  

a) *Assign PC1 the smallest usable IP from the subnet. Enter this directly in Figure 4.1.  

b) *Assign R1.eth0 the largest usable IP from the subnet. Enter this directly in Figure 4.1.  

c) *Assign R1.eth1 an address from the transport network. Enter this directly in Figure 4.1.  

d) *What transport protocol and destination port are used when PC1 accesses https://www.tum.de/?  

From now on, we will abbreviate IP and MAC addresses according to the schema <Device>.<Interface>, e.g., R1.eth0 for the corresponding address at interface eth0 of router R1.  

R1 supports NAT to allow PCs to access the Internet. The mapping is done as discussed in the lecture via the global port, but R1 also stores additional data.  

PC2 has already communicated with hosts on the Internet. The NAT table of R1 is shown below.  

| Prot. | Local IP        | Local Port | Global IP      | Global Port | Remote IP      | Remote Port |  
|-------|-----------------|------------|----------------|-------------|----------------|-------------|  
| tcp   | 172.29.50.1     | 53050      | R1.eth1       | 53050       | tum.eth0       | 443         |  
| tcp   | 172.29.50.1     | 55222      | R1.eth1       | 55222       | lmu.eth0       | 80          |  

e) *Complete Table 4.1 with the entries that arise here.  

Note for the following subtasks that there are four additional routers between R2 and R3.  

f) *Complete the header fields for the request from PC1 to www.tum.de in the three empty boxes in Figure 4.2. If a field is not clearly defined, make a sensible choice.  

**Note:**  
- If you could not solve part d), assume destination port 80.  
- IP and MAC addresses can be abbreviated according to the schema <Device>.<Interface>, e.g., PC2.eth0.  
- The hostname of the server on which www.tum.de is hosted can be abbreviated to "tum".  

g) *Complete the header fields for the response from www.tum.de to PC1 in the three empty boxes in Figure 4.3. If a field is not clearly defined, make a sensible choice.  

**Note:**  
- IP and MAC addresses can be abbreviated according to the schema <Device>.<Interface>, e.g., PC2.eth0.  
- The hostname of the server on which www.tum.de is hosted can be abbreviated to "tum".  

**Task 5**  
Voyager 1 and the Moepis (Sampling and Quantization) (23 Points)  
The Moepis discover a crater on their planet Gliese 587c one day. Inside, they find a dented aluminum shell and a golden disc. On the cover of the golden disc are some strange drawings. The Moepis now attempt to decipher the message.  

**Figure 5.1:** Voyager Golden Record Cover and Disc  
**Figure 5.2:** Drawings on the cover of the Voyager Golden Record  

It is about the space probe Voyager 1, which was launched from Earth in 1977. As a message for extraterrestrials, it carries a golden plate, the so-called "Golden Record".  

One Moepi concludes that the drawing at the bottom right in Figure 5.2 could represent the hyperfine structure transition of the hydrogen atom. This transition has a frequency of 1420 MHz. Thus, it creates both a time unit (period duration) and a length unit (wavelength). These universal units are used as a scale for all other data in the drawings.  

All numerical values are given in binary with | as 1 and – as 0.  

a) *Calculate the universal time unit and provide it in seconds.  

b) *Calculate the universal length unit and provide it in meters.  

On the right half of Figure 5.2, it is explained how images can be reconstructed from the played sounds. The third drawing on the right side shows that images consist of vertical "scan lines," namely 1,000,000,000 = 512 pieces (see binary representation with | and – in the drawing). In the topmost drawing, the first three scan lines are schematically represented.  

c) How long does it take to play one scan line? (Derivation/Calculation)  

d) *The images have (as shown) an aspect ratio of 4:3. At what rate should the Moepis sample the scan lines? Note: If you could not solve part c), assume t = 8.29 ms for one scan line.  

To validate the findings, another Moepi suggests first generating a preview image of lower quality (8 x 6 pixels). For this, only 8 representative scan lines should be examined, of which only 6 pixels should be reconstructed. The scan lines are shown in Figure 5.3. The preview image should also only contain black and white (no grayscale).  

**Figure 5.3:** Selected scan lines of the first image  

e) *Justify how many sample values per scan line are necessary for the preview image.  

f) Mark all sampling time points for scan line 32 in Figure 5.3.  

g) *Determine the quantization intervals and quantization levels so that the maximum quantization error in the interval [-1;1] is minimal.  

h) Draw the quantized (not the sampled) signal for scan line 96 in Figure 5.3.  

i) Draw the sampled and quantized signal for scan line 160 in Figure 5.3.  

j) Create the preview image in Figure 5.4. Mark the sample values of the other scan lines in Figure 5.3 as necessary.  

**Figure 5.4:** Preview of the first image  

**Additional Printout for Task 2. Invalid solutions should be clearly crossed out.**  

**Additional Printout for Task 3. Invalid solutions should be clearly crossed out.**  

**Additional space for solutions. Clearly mark the assignment to the respective subtask. Do not forget to cross out invalid solutions.**