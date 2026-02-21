Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during attendance control by affixing a code.
- This contains only a continuous number, which is also to be pasted on the attendance lists marked with the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam to you.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Retake  
Date: Tuesday, September 29, 2020  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 11:30–13:00  

### Instructions for Processing
- This exam consists of 16 pages with a total of 6 tasks. Please check now that you have received a complete set of information.
- The total score for this exam is 90 points.
- The removal of pages from the exam is prohibited.
- The following aids are allowed:
  - All electronic and non-electronic aids
  - Internet and teamwork are explicitly not allowed.
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless otherwise explicitly noted in the respective sub-tasks.
- Copying solution proposals from previous exams or other sources does not constitute independent work. We reserve the right to grade the respective task with 0 points in such cases.
- Do not write with red/green colors or with pencil.

### Task 1  
Multiple Choice (19 Points)  
The following sub-tasks are multiple choice with multiple answers, with 1 point for each correct answer and -1 point for each incorrect answer. Multiple answers may be correct.  
The minimum score per sub-task is 0 points, i.e., negative points do not carry over to other sub-tasks.  

Instructions for processing on paper or if your PDF editor does not support the checkbox function:  
- Mark the correct answers with an X.  
- Crossed answers can be marked again with adjacent markings.  

1. **For a segment, it is a...**  
   - L3-SDU  
   - L2-SDU  
   - L4-PDU  
   - L3-PDU  
   - L1-PDU  
   - L4-SDU  
   - L2-PDU  
   - L1-SDU  

2. **Which statements about Fourier transformations are correct?**  
   - The spectrum is continuous.  
   - The spectrum is discrete.  
   - The spectrum is always complex.  
   - The spectrum is always bounded.  
   - Used for the analysis of periodic signals.  
   - Used for the analysis of non-periodic signals.  

3. **Given is a continuous signal that is to be quantized linearly with 3 bits in the interval I = [7;16]. Determine the maximum quantization error within I rounded to two decimal places.**  
   - 1.00  
   - 3.00  
   - 1.13  
   - 0.56  
   - Other value  

4. **Given is a continuous signal that is to be quantized linearly with 2 bits in the interval I = [0;15]. Determine the maximum quantization error outside of I rounded to two decimal places.**  
   - 3.75  
   - 1.88  
   - 7.50  
   - 2.50  
   - Other value  

5. **Given is a line code that encodes 3 bits per symbol. It should achieve a data rate of 8 Mbit/s. Determine the minimal necessary bandwidth under the given conditions rounded to two decimal places.**  
   - Other value  
   - 1.33 MHz  
   - 5.33 MHz  
   - 4.43 MHz  
   - 17.72 MHz  

6. **What is meant by source coding?**  
   - Representation of data by sequences of sending basic impulses.  
   - Removal of redundancy.  
   - Targeted addition of redundancy.  

7. **Given is a microwave link that has the same conditions in both directions. The transmission rate is given as 20 Mbit/s. The distance is 126 km. Determine the RTT of a 1091 B large frame (e.g., Echo Request/Reply) rounded to two decimal places. Assume that no further time delays occur due to media access and processing at the nodes.**  
   - 420 ms  
   - 840 ms  
   - 873 ms  
   - 436 ms  
   - 1,713 ms  
   - 856 ms  

8. **If the notebook (NB) wants to send a frame to one of the PCs, which MAC address(es) will be used to specify the destination?**  
   - PC  
   - NB  
   - Switch  
   - AP  

9. **If the notebook (NB) wants to send a frame to one of the PCs, which IP address(es) will be used to specify the destination?**  
   - PC  
   - AP  
   - Switch  
   - NB  

10. **What is the binary representation of the number 0x474802?**  
    - 001011010001001100011011  
    - 100010001111011011110000  
    - 010001110100100000000010  
    - 101101011110011100101000  
    - 100101001101100100011101  
    - 011111001011101101100011  

11. **You receive a message from the IPv6 address fd00:32o:15:8:e7be:0dff:fe56:23a4. What is the most likely MAC address of the sending interface?**  
    - e5:be:0d:56:23:a4  
    - 0d:ff:fe:56:23:a4  
    - e7:be:0d:56:23:a4  
    - 32:00:16:00:08:27  

12. **How many broadcast domains does the adjacent network consist of?**  
    - 1  
    - 6  
    - 4  
    - 2  
    - 3  
    - 5  

13. **How many collision domains does the adjacent network consist of?**  
    - 6  
    - 4  
    - 5  
    - 3  
    - 2  
    - 1  

14. **You observe the following data stream from an unknown source. At which character is the information content maximal?**  
    - G  
    - H  
    - B  
    - B  
    - A  
    - A  
    - B  
    - F  
    - B  
    - H  
    - G  
    - F  
    - H  
    - A  
    - G  
    - B  
    - A  
    - H  
    - B  
    - H  
    - F  
    - A  
    - G  
    - F  

### Task 2  
Short Tasks (7 Points)  
1. **Provide a bit sequence that matches the signal depicted below, where the duration of a single symbol is 1 s. Note: There are two equivalent solutions. Provide one of them.**  
   - 1 0 1 0 0 0 0 1 1  
   - 1 2 3 4 5 6 7 8 9 t[s]  

2. **From the lecture, the transmission time of a message of length L divided into packets of size pmax with header length Lh per packet over a distance of d with n hops and constant data rate r is known by the following relationship:**  
   - T = 1/r * (L/pmax + Lh + d + n * Lh)  
   Determine the optimal packet size p such that the transmission time is minimized. Assume for simplification that L is an integer multiple of the packet size.  

3. **Sketch by hand a typical course of the send window size for TCP (Reno). Assume that at time t = 0 the connection has just been established. Mark and name different phases of congestion control.**  

### Task 3  
I Spy (15 Points)  
A neighbor of Mrs. Roberts sits in a café and enthusiastically observes the wall next to him. He notices the nearby RJ45 port. Quickly, his own laptop, with interface eth0, is connected to this port using a patch cable for special cases. Shortly thereafter, the frame depicted in Figure 3.1 can be observed.  

**Figure 3.1: Randomly observed Ethernet frame**  
- Ethertype: 0x0000  
- 52 54 00 e7 b2 31 52 54 00 40 83 6c 08 06 00 01  
- Operation: Sender Protocol Address: 0x0010  
- 08 00 06 04 00 02 52 54 00 40 83 6c 0a 05 3d 35  
- 52 54 00 e7 b2 31 0a 05 3d 07  

1. **Name the Layer 2 SDU occurring in Figure 3.1. (Justification!)**  
   - ARP, as the header field EtherType has the value 0x0806. See marking in Figure 3.1.  

2. **Specify the type of Layer 2 SDU represented in Figure 3.1. (Justification!)**  
   - ARP Reply, as it is an ARP message (see Ethertype) and the Operation field has the value 0x002. See marking in Figure 3.1.  

3. **Provide the name, value, and function description for the 7th header field of the Layer 2 SDU from Figure 3.1. Use the usual representation form. (Justification!)**  
   - Sender Protocol Address with value 10.5.61.53. Function description: Layer 3 address (here: Type IPv4) of the sender of the message. See marking in Figure 3.1.  

Through further observation, it is noted that some of the observable Ethernet frames contain the IPv4 addresses 10.17.29.47 and 10.47.31.23.  

4. **Provide the smallest network for the two IPv4 addresses. (Justification!)**  
   - 10.0.0.0/10, as the broadcast address is 10.0.0.0/1110.31.255.255 and thus two adjacent /11 networks are needed. Additionally, smaller networks containing the addresses are not adjacent.  

5. **Using the information collected during this task, provide a valid static IPv4 configuration for an additional network participant.**  
   - Network address: 10.0.0.0  
   - Default Gateway: 10.63.255.254  
   - Broadcast Address: 10.63.255.255  
   - Laptop Address eth0: 10.17.29.6  

6. **How can it be validated that the IPv4 address chosen in sub-task e) does not collide with the IPv4 address of another participant? (Justification!)**  
   - By performing an ARP request for the desired address. If no response to this ARP request occurs, then the address is presumably not currently in use.  

**Figure 3.2: Beginning of another observed Ethernet frame**  

After a while, the Ethernet frame depicted in Figure 3.2 can be observed.  

7. **Determine the protocols used on layers 3 and 4 in the above frame. (Justification!)**  
   - IPv6 (see Ethertype) and UDP (see Next Header). See marking in Figure 3.2.  

8. **Provide the destination addresses used on layers 2, 3, and 4 in their usual representations. (Justification!)**  
   - Layer 2: 33:33:00:01:00:02, Layer 3: ff02::1:2 and Layer 4: 547. See marking in Figure 3.2.  

### Task 4  
NAT and Routing (18 Points)  
Given is the network topology from Figure 4.1. PC1 and PC2 are connected via the WLAN Access Point AP to Router R, which provides access to the Internet.  

**Figure 4.1: Network topology**  
- PC1 wlan0  
  - IP 10.0.1.1  
  - Subnet Mask 255.255.240.0  
  - Gateway 10.0.1.0  
- AP R1 R2 R3  
- PC2 wlan0  
  - IP 10.0.1.2  
  - Subnet Mask 255.255.240.0  
  - Gateway 10.0.1.0  

1. **Justify whether the address 10.0.1.0 is usable for the given prefix. If not, assign a meaningful address to R1 in the same network.**  
   - 10.0.1.0 is a valid host address in the network 10.0.0.0/20, as it is neither the first nor the last address in the subnet (immediately evident from the small prefix and the 1 in the 3rd octet).  

2. **Determine the network address and broadcast address of the network in which PC1, PC2, and R1 are located.**  
   - Network address: 10.0.0.0  
   - Broadcast address: 10.0.15.255  

3. **How many IP addresses are available in this network for addressing devices? Also provide the calculation method!**  
   - The first and last address cannot be used for devices and must be subtracted.  
   - 2^20 - 2 = 4094  

4. **Assign a meaningful IP address, subnet mask, and gateway address to PC1 and PC2 so that they can establish a connection to the Internet. Enter the values directly into Figure 4.1. Note any differing IP from R1 in task a).**  

5. **How many /20 subnets are there in the network 10.0.0.0/8? Also provide the calculation method!**  
   - 2^(20-8) = 4096  

6. **Justify why R1 must support NAT so that PC1 and PC2 can communicate with hosts on the Internet.**  
   - PC1 and PC2 are in a private network, whose IP addresses are not globally unique and therefore cannot be routed.  

7. **What information must R1 maintain in its NAT table at a minimum?**  
   - Local IPs of the PCs, local port numbers, and global source port numbers. (Global IP is not necessary, as R1 only has one global IP address; also, destination port numbers are not required for basic tasks.)  

In the following, we will abbreviate IP and MAC addresses according to the following schema: <Device name> or <Device name>.<Interface> if the interface is not unique, e.g., PC1 or R1.wan0. Note that there are several routers between R2 and R3 for the processing of the following two sub-tasks.  

PC1 is now accessing the website https://www.grnvs.tips.  

8. **Complete the header fields for the request from PC1 to www.grnvs.tips in the three empty boxes in Figure 4.2. If a field cannot be uniquely determined, make a sensible choice.**  
   - RecvMac: AP.wlan0  
   - SrcMAC: R3.eth0  
   - TransMac: PC1  
   - DstMAC: SRV1  
   - SrcIP: R1.wan0  
   - DstIP: SRV1  
   - TTL: 59  
   - SrcPort: 2001  
   - DstPort: 443  

**Figure 4.2: Network topology**  

9. **Complete the header fields for the response from www.grnvs.tips to PC1 in the three empty boxes in Figure 4.3. If a field cannot be uniquely determined, make a sensible choice.**  
   - RecvMac: PC1  
   - SrcMAC: SRV1  
   - TransMac: AP.wlan0  
   - DstMAC: R3.eth0  
   - SrcIP: SRV1  
   - DstIP: R1.wan0  
   - TTL: 64  
   - SrcPort: 443  
   - DstPort: 2001  

**Figure 4.3: Network topology**  

### Task 5  
Lossless Data Compression (10.5 Points)  
To utilize your internet connection more efficiently and transfer more data faster, you use a lossless compression: a Huffman code. Since you do not know in advance which data will be transmitted, you orient yourself to the data transmitted in the past and have already learned code words.  

Given is the alphabet A = {A, B, C, D, E, F, G, H, I} and the following table with the learned code words for each character x:  
| x | Codeword | x | Codeword |
|---|----------|---|----------|
| A | 00       | F | 0111     |
| B | 10       | G | 0101     |
| C | 110      | H | 01001    |
| D | 111      | I | 01000    |
| E | 0110     |

1. **How long is each code word if they used a uniform code instead of the Huffman code? Provide the calculation method!**  
   - 9 code words log(9) bits = 4 bits  

2. **You want to compress the following word (20 characters) with the above code:**  
   - G D A B A A C B E B H F A C B C D E H A  

3. **Let X be the random variable of a memoryless source that generates the word. Derive the occurrence probability P[X = x] for all x from the set A. It is sufficient to provide the probability as a reduced fraction.**  
   - A: 5/20 = 1/4  
   - B: 4/20 = 1/5  
   - C: 3/20  
   - D: 2/20 = 1/10  
   - E: 2/20 = 1/10  
   - F: 1/20  
   - G: 1/20  
   - H: 2/20 = 1/10  
   - I: 0/20 = 0  

4. **What is the average code word length if the probabilities from part b) were representative for the source? Provide a traceable calculation method.**  
   - The average code word length of the source is:  
   - X P[X = z] c(z) = 2 + 2 + 3 + 3 + 4 + 4 + 4 + 5 + 5 = 2.95  

5. **The actual average code word length is 2.9 bits/character. How does this value differ from the calculated value from part c)?**  
   - Such a small set of characters is not sufficient to find representative occurrence probabilities.  

6. **How large is the expected saving when compressing many words from this source with this code compared to a uniform code? Provide a traceable calculation method.**  
   - An average saving of:  
   - (4 bits - 2.9 bits) / 4 bits = 27.5%  

7. **Encode the first 6 characters of the word with the given Huffman code.**  
   - G D A B A A: 010111100100000  

### Task 6  
IPv6 (20.5 Points)  
Given is the network topology in Figure 6.1. Router R is connected to the network NET1 via GW and to the Internet and supplies the networks NET2 and NET3. NET3 is used for WLAN clients.  

**Figure 6.1: Topology**  
- eth0 e9:dd:2f:00:55:11  
- eth0 b4:ee:1a:30:c8:ed  
- 2001:b98:3:b::1:0/64  
- 2001:b94:7:4::1:1/64  
- NET2 NET1 Internet  
- 2001:b98:3:b::/64  
- 2001:b94:7:4::/64  
- eth0 e9:dd:2f:00:55:00  
- ppp0 e9:dd:2f:00:55:12  
- wlan0 e9:dd:2f:00:55:13  
- NET3 2001:b98:3:c::1:0/64  
- 2001:b98:3:c::/64  

1. **Which IP address will R receive at the interface ppp0 through SLAAC?**  
   - 2001:bcb:7:f:e255:d9ff:fe00:5512  

2. **Explain where the individual parts of this IP address come from.**  
   - SLAAC generates the IPv6 address from the Prefix Announcement and the MAC address of the interface, inserting ff:fe between the manufacturer identifier and device ID. The second-to-last bit of the first octet of the OUI is flipped.  

3. **Show that NET2 and NET3 cannot be aggregated on GW.**  
   - NET2 and NET3 are not in the same /63 prefix. For bits 61 to 64: b16 = 10112, c16 = 11002. They may only differ in the last position.  

4. **Fill in the usual column names in the routing table 6.1.**  

5. **Complete the routing table 6.1 for R so that the connected networks can reach the Internet and can be reached from there. Aggregate as much as possible.**  
   - | Destination            | NextHop | Interface |  
   - |------------------------|---------|-----------|  
   - | 2001:b94:7:4::/64      | ::      | ppp0      |  
   - | 2001:b98:3:b::/64      | ::      | eth0      |  
   - | 2001:b98:3:c::/64      | ::      | wlan0     |  
   - | ::/0                   | 2001:b94:7:4::1:1 | ppp0 |  

**Table 6.1: Routing table on R**  

6. **Argue where router R will forward a packet with the destination address fe80::9:a:ff:fef1:b477.**  
   - The router will not forward the packet, as it is a link-local address.  

7. **Client C is not IPv6 capable. To allow communication between C and the Internet, the network administrator has only assigned the IPv4 address 10.1.0.10/24 to R at interface eth0.**  
   - With what method could C be automatically assigned an IPv4 address from this network?  
   - A DHCP server can be installed on Router R, which can be correctly configured to assign C a valid IPv4 address.  

8. **The network administrator now manually assigns the IP address 10.1.0.11/24 to C and sets C's default gateway to the IPv4 address of interface eth0 on R.**  
   - Argue whether C can now communicate with the Internet.  
   - C cannot communicate with the Internet. C can communicate with R, but there is no automatic translation from IPv4 to IPv6. Since no IPv4 addresses are configured in NET1, only communication via IPv6 is possible.  

To solve some problems, the network administrator attempts to install a mapping mechanism from IPv4 to IPv6. This should enable communication between devices configured for IPv4 and IPv6. To make Client C reachable from the Internet, a virtual IPv6 address is generated for Client C. This consists of the IPv6 prefix of the network in which C is located, with the lower bits set equal to the IPv4 address.  

9. **Provide the generated virtual IPv6 address of C and argue why this address is sensibly chosen. Use the usual notation for IPv6 addresses.**  
   - 2001:bc4:6:c::a01:b  
   - The IPv6 address can be routed directly from the Internet when NET2 is reachable. R can directly recognize from the IPv6 address for which IPv4 address an incoming packet is addressed.  

10. **The mapping mechanism now works, and incoming packets to the virtual IPv6 address are correctly translated into IPv4 packets.**  
    - **A server S is located on the Internet. Can S send a message to C?**  
      - Yes, a message that is to be sent from S to C arrives at C through the mapping.  

11. **What must happen in router R for bidirectional communication between S and C to be possible?**  
    - For bidirectional communication, R must, for example, automatically generate a new IPv4 address for S to be able to map a packet from C back to S's IPv6 address.  

12. **Client C wants to send a control command to a drone with the IP address 2001:bc4:6:b::c1a7:19f0, which is connected via WLAN through NET3 to R. Explain what problems may arise during communication and how these can be resolved by the network administrator. Giving the drone an IPv4 address is unfortunately not possible.**  
    - Since Client C can only communicate via IPv4, it is not possible to specify an IPv6 address as the recipient. To enable communication, the administrator could generate a virtual IPv4 address on Router R, which is mapped through a type of NAT to the IPv6 address of the drone.  

13. **To solve the problem, the administrator creates a mapping table in R. Fill in Table 6.2 with all mappings to enable frictionless communication between C and the drone.**  
    - | IPv6 Address              | IPv4 Address        |  
    - |--------------------------|---------------------|  
    - | 2001:b98:3:b::a01:b      | 10.1.0.11           |  
    - | 2001:b98:3:c::c1a7:19f0  | 193.169.25.240      |  

**Table 6.2: IPv6-to-IPv4 Mapping Table on R**  

### Additional Space for Solutions  
Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.