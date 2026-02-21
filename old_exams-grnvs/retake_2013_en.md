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
Diploma Preliminary Exam  
Bachelor Exam  
............................  
Consent to Grade Disclosure  
by E-Mail / Internet  

Exam Subject: Fundamentals of Computer Networks and Distributed Systems  
Examiner: Prof. Dr.-Ing. Georg Carle  
Date: 23.09.2013  
Lecture Hall: .................... Row: .................... Seat: .....................  
To be filled out by the supervision only:  
Lecture Hall left from ...... : ...... to ...... : ......  
Submitted early at ....... : ......  
Special Remarks:  
Repeat Exam  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
Monday, 23.09.2013  
11:00 – 12:30  

- This exam consists of 23 pages and a total of 6 tasks. Please check now that you have received a complete set of materials.  
- Please write your name and student ID in the header of each page.  
- Do not write in red/green ink or with a pencil.  
- The total number of points is 85.  
- Allowed aids are a double-sided handwritten DIN A4 sheet and a non-programmable calculator. Please remove all other materials from your desk and turn off your mobile phones.  
- Tasks marked with * can be solved without knowledge of the results of preceding sub-tasks.  
- Do not spend too long on a (sub-)task. If you cannot solve the task immediately, it is better to move on to the next task.  
- Only results where a solution method is recognizable will be graded. Text tasks must be justified unless explicitly stated otherwise in the respective sub-task.  

1 Name:  
Task 1 Short Tasks (7 Points)  
The following short tasks are independent of each other. Bullet-point answers are sufficient!  
a)* How is the network portion of an IP address known in class-based routing?  
b)* Describe what problem can arise when a server that provides important services obtains its IP address via DHCP.  
c)* Justify to what extent the Diffie-Hellman method can protect against a Man-in-the-Middle attack.  
d)* Differentiate lossless compression from transcoding in general.  
e)* Justify which transport protocol you consider suitable for streaming services.  
f)* Explain why line 4 in the following pseudo-code (after lines 1-3) cannot be correct.  
Note: This concerns the fundamental operation of sockets and not the syntax.  
```
s ← new-tcp-socket()  
bind(s, address, port)  
listen(s)  
buffer ← recv(s)  
```  

Task 2 Modulation and Media Access (17 Points)  
On the planet Gliese 581c, a water world with about 5 times the mass of Earth, lives an extraterrestrial people - the Moepis. This somewhat backward people is just entering the age of wireless communication. However, the Moepis face a serious problem: Electromagnetic waves, as known to be used for wireless transmission on Earth, are heavily attenuated underwater, which is why conventional radio techniques do not work on their home planet.  
Instead, the Moepis rely on sound waves that propagate underwater on their planet at approximately  
```
v = 1480 m/s  
```  
As a modulation method, the Moepis use 2-ASK with a signal bandwidth of  
```
B = 1 kHz  
```  
a)* Explain in words how the modulation method 2-ASK works.  
b) Calculate how many bits per symbol can be represented using 2-ASK.  
c) Determine the achievable data rate as a function of the signal bandwidth and the number of signal levels.  
Note: If you could not solve sub-tasks b) or c), assume from now on a transmission rate of  
```
r = 1 kbit/s  
```  
The new transmission method is being tested by the Moepis on a test track, which is schematically represented in Figure 2.1. A long test packet of size 16B is sent from A to C.  

```
A ----100m---- B ----100m---- C  
```  
Figure 2.1: Test setup for the new transmission method.  
d)* Calculate the serialization time for the test packet.  
e)* Calculate the propagation delay between A and C.  
f)* Draw a complete path-time diagram for sending the test packet.  
Scale: 1 cm = 100 ms  
g) Mark both t_s and t_p in your solution from part f).  

The method is now to be extended to more than two nodes. It must be recognized whether a data packet arrives at the receiver or not. Since there were no losses in the communication between A and C during previous tests, the Moepis decide on the following protocol:  
- A data packet is considered successfully transmitted if no error occurred during transmission.  
- If a collision, i.e., two simultaneous transmissions, is detected during transmission by any node, that node sends a jam signal of length 4B.  
- If a node receives this jam signal while still transmitting, it aborts and waits for a randomly chosen time span.  

h)* Which well-known media access method does this approach correspond to? (without justification)  
i)* Justify why the collision detection method proposed by the Moepis does not work correctly even in the test setup from Figure 2.1.  
j) Suggest two possible solutions to the problem in part i) (no calculations necessary).  
k) Propose a specific modification to the test setup from Figure 2.1 for one of the two solutions from part j). Determine the threshold of a changed parameter as a numeric value (e.g., minimum or maximum frame size).  
In further tests, the Moepis also notice the problem. However, an adjustment would require that a node can send and listen to the medium simultaneously for collision detection. This is currently technically unfeasible for the Moepis.  

l)* Describe another media access method suitable for the described scenario that does not require collision detection.  

Task 3 NAT (17 Points)  
Given is the network from Figure 3.1. The Moepi AG operates a small web server behind a NAT router, which should be accessible from the Internet. However, due to significant losses in the past quarter, Moepi AG can unfortunately only afford one public IPv4 address.  

```
Moepi AG  
R1 R2  
eth1 eth0 eth0: 10.0.0.4  
C2  
eth1  
eth0: 131.159.20.254  
eth1  
SW1 eth0: 10.0.0.3  
eth0 C1  
eth0: 131.159.20.83 wan0: 217.79.191.6  
eth0: 10.0.0.1  
eth1 eth2  
eth0 eth3  
eth0: 10.0.0.2  
PC1 R3 SW2 web  
```  
Figure 3.1: Network topology  
a)* Justify why the web server web is not readily accessible from the Internet.  
b)* Assume Moepi AG had a second public IP address available and would configure the web server with this address. Give two reasons why this would not guarantee the accessibility of the web server.  
c)* Justify whether switches need IP addresses to fulfill their normal function.  

Table 1 shows an example of the NAT table of router R3 with some dynamic entries that arise during operation. Such entries can also be created statically (Port-Forwarding).  

| Prot. | Local IP | Local Port | Global IP | Global Port | Remote IP | Remote Port |  
|-------|----------|------------|-----------|-------------|-----------|--------------|  
| tcp   | 10.0.0.4 | 2783       | 217.79.191.6 | 2783       | 131.159.20.83 | 80           |  
| tcp   | 10.0.0.4 | 6942       | 217.79.191.6 | 6942       | 131.159.20.83 | 443          |  
| tcp   | 10.0.0.3 | 2783       | 217.79.191.6 | 2784       | 131.159.20.83 | 80           |  
| tcp   | 10.0.0.2 | 2783       | 217.79.191.6 | 80         | *            | *            |  

Table 1: NAT table of router R3  
d)* Explain how R3 makes forwarding decisions based on the 7 columns in Table 1.  
e) Provide another entry in Table 1 so that R3 is forced to set a different global port than the local port.  
f) Complete the NAT table in Figure 1 with a static entry so that only the web server is accessible from the Internet on the standard port of HTTP. Ensure that NAT still allows other computers within Moepi AG to access the Internet. If an entry can take arbitrary values, simply write * as a wildcard instead of the specific value.  

In the following, we will abbreviate IP and MAC addresses according to the scheme <DeviceName>.<Interface>. For example, R3.wan0. Note that for the next two sub-tasks, there are also three other routers between R1 and R2. PC1 now accesses the website  
```
http://217.79.191.6  
```  
g) Complete the headers for the request from PC1 to http://217.79.191.6 in the three empty boxes in Figure 3.2. If a field is not clearly defined, make a sensible choice.  
h) Complete the headers for the response from http://217.79.191.6 in the three empty boxes in Figure 3.3. If a field is not clearly defined, make a sensible choice.  

Task 4 Routing (15 Points)  
Given is the network from Figure 4.1. The routers have a separate IP address for each interface and receive the first usable address of the respective subnet. The hosts receive the directly following IP addresses in ascending order.  

```
Internet  
H4  
eth1: 17.1.5.23  
A  
eth0: 192.168.  
eth0: 192.168.0.1  
R1  
eth0: 192.168.  
eth0: 192.168.  
eth2: 192.168.0.57 eth1: 192.168.  
D B C  
eth0: 192.168.0.58 eth1: 192.168.  
H1 R2 R3  
eth0: 192.168.  
eth0: 192.168.  
H2 H3  
```  
Figure 4.1: Network topology  
a)* Determine the missing values in Table 2.  
Note: The first column contains the designation of the network and does not indicate the network class.  

| Network | Network Address | Broadcast Address | Subnet Mask | Usable Addresses |  
|---------|-----------------|-------------------|-------------|------------------|  
| A       | 192.168.0.0     | 30                |             |                  |  
| B       | 192.168.0.47    | 255.255.255.240   |             |                  |  
| C       | 192.168.0.48    | 255.255.255.248   |             |                  |  

Table 2: Overview of Address Distribution  
b) Assign the correct IP addresses to the routers and hosts according to Table 2. Enter your results directly into Figure 4.1. The first two octets are already given. Assign the routers' interfaces the first usable IP addresses per subnet.  

Host H1 wants to send a message to H4. Assume all ARP caches are empty. Additionally, an excerpt of the routing table from R2 is given in Table 3. Note that some values are not provided, as you had to determine them in previous sub-tasks. These values have been replaced with a question mark. The gateway addresses have been replaced with <DeviceName>.<InterfaceName>, e.g., instead of the corresponding IP address.  

| Destination | Mask       | Gateway          | Metric | Iface         |  
|-------------|------------|------------------|--------|---------------|  
| 192.168.0.0 | ?          | -                | 0      | eth0          |  
| 192.168.0.48| ?          | 1                | R3.eth0| eth0          |  
| 0.0.0.0     | 0.0.0.0   | 1                | R1.eth0| eth0          |  

Table 3: Excerpt of the Routing Table from Router R2.  
c) Enter all necessary ARP requests and ARP replies in the correct order in the table below.  
Note: In the following table, one row stands for a pair of ARP request and the corresponding ARP reply. The specification of the last two octets of the IP addresses is sufficient. Note interfaces as <DeviceName>.<InterfaceName>.  

| ARP-Request | ARP-Reply |  
|--------------|-----------|  
| Sender.Interface | Sender IP Address | Requested IP Address | Sender.Interface |  

d)* Describe how a router can check if an entry in its routing table matches a given destination IP.  
e)* Describe how a router selects the next hop to a given destination from all matching entries.  

Given is now the excerpt of the routing table from Router R1 shown in Table 4. A packet coming from the Internet is to be forwarded to Host H2.  

| Destination   | Mask               | Gateway         | Metric | Iface         |  
|---------------|--------------------|------------------|--------|---------------|  
| 192.168.0.56  | 255.255.255.248    | 1                | R2.eth0| eth0          |  
| 192.168.0.32  | 255.255.255.240    | 1                | R2.eth0| eth0          |  
| 192.168.0.32  | 255.255.255.224    | 1                | R3.eth0| eth0          |  

Table 4: Excerpt of the Routing Table from Router R1.  
f)* Justify which next hop R1 will choose when forwarding the packet to H2.  
g)* What is the purpose of the last line in the routing table of R2 (see Table 3)?  

So far, static routing has been considered. However, dynamic routing is often used.  
h)* Name two different concepts for dynamic routing.  
i)* Name two different metrics that can influence the cost determination for route selection.  

Task 5 Frame Boundaries and Block Check (10 Points)  
In the following task, we will take a closer look at the so-called BISYNC protocol, which stands for Binary Synchronous Communication (BSC). It was developed by IBM in 1967. It is a communication protocol that offers services at the data link layer. The structure of a BISYNC frame is schematically represented in Figure 5.1.  

```
8bit 8bit 8bit 8bit 8bit 16bit  
SYN SYN SOH Header STX Payload ETX CRC  
```  
Figure 5.1: BISYNC Frame Format  
A BISYNC frame is structured using control characters. Table 5 contains an excerpt of the control characters used. DLE is the escape character and is placed before the corresponding control character.  

| Control Character | Hex Value | Meaning                     |  
|-------------------|-----------|-----------------------------|  
| Start of Header   | SOH       | 0x01                        |  
| Start of Text     | STX       | 0x02                        |  
| End of Transmission| ETX       | 0x03                        |  
| Data Link Escape   | DLE       | 0x10                        |  
| Synchronization    | SYN       | 0x16                        |  

Table 5: Control Characters in BISYNC  
a)* Name another way, besides the use of control characters, to mark frame boundaries.  
b)* Generally justify why an escape character is necessary when control characters are used to identify frame boundaries.  
c)* Justify why ETX and DLE must be protected in the payload portion using the escape character.  
d)* Justify why escaping the other characters in the payload portion can be omitted.  
e)* Correctly encode the following hexadecimal character string as a payload: 10 03 A1.  

Next, we consider the hexadecimal character string  
```
16 16 01 AA BA F8 02 12 A9 03 00 33  
```  
which has been received as a message. It represents a complete frame.  
f)* Determine the header, the payload, and the checksum of the specified message.  
g)* Justify what degree a generator polynomial for BISYNC should ideally have.  
h)* Justify generally which bit errors can be detected using CRC checksums.  
i)* Justify which bit errors can be corrected using CRC checksums.  

Task 6 TCP (19 Points)  
In this task, we will consider the Transmission Control Protocol (TCP) in the "Reno" variant. A client C and a server S execute the following protocol:  
1. C establishes a TCP connection to S.  
2. S sends its current system time to C in an enterprise XML-formatted message that is 3000B long.  
3. S sends another message that is 3600B long and contains a signature of the first message.  
4. S and C close the connection again.  

In the following, we will take a closer look at the TCP connection. The contents of the messages are irrelevant.  
a)* Explain the difference between flow control and congestion control.  
At the beginning, C establishes a TCP connection to S. C chooses the first sequence number as 10000, and S chooses 20000.  
Note: In this task, ignore serialization times and propagation delays in all path-time diagrams. One arrow per segment is sufficient. Indicate the set flags (SYN, FIN, RST), the sequence number (e.g., SEQ=1), and, if set, the acknowledgment number (e.g., ACK=1) for all segments.  
b)* Draw the connection establishment in the following path-time diagram.  
c)* In which phase of congestion control are C and S now?  

Now S begins to send the first message with a length of 3000B. The size of the receive window is 1000B on both sides. Both congestion control windows start with a size of 1 MSS.  
d)* Draw all segments that occur during the sending of the message in the following path-time diagram. Pay attention to the development of the congestion control window!  
e)* What size do the congestion control windows of C and S have now?  

Next, we assume that "Go-Back-N" is used for congestion control. The size of the receive window remains at 3000B for both participants. S now sends the second message with a size of 3600B. However, the second segment is discarded due to a bit error.  
f)* Label the given segments in the following path-time diagram and draw all 3 segments that are necessary for the successful sending of the second message. Assume that no further packet losses occur.  
g)* Justify in which phase of congestion control C and S are now.  
h)* Justify what advantage "Selective Repeat" offers over "Go-Back-N".  

S now closes the TCP connection. C then also closes the connection.  
i)* Draw the connection teardown in the following path-time diagram.  
j)* Explain what it means when one side closes the TCP connection. Must the other side also close the connection?  
k)* A channel has a bit error rate of 5%. Explain whether the use of TCP is an efficient solution to hide packet errors from the application layer.  

Additional space for solutions - please clearly mark the affiliation with the respective task and strike out invalid solutions!