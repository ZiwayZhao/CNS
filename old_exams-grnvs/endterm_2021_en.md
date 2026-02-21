Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized by attaching a code during the attendance check.  
- This contains only a continuous number, which is also noted in the attendance list next to the signature field.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Exam: IN0010/Endterm  
Date: Tuesday, July 27, 2021  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 08:00–09:30  

Please sign the code of conduct at the top right next to your sticker. Otherwise, your electronic exercise performance will not be counted!

**Instructions for Completion**  
- This exam consists of 16 pages with a total of 6 tasks.  
- The total score for this exam is 90 points.  
- It is prohibited to tear pages from the exam.  
- The following aids are allowed:  
  - a non-programmable calculator (no calculator app!)  
  - the cheat sheet provided by the chair in printed form without modifications  
  - a dictionary in paper form without any annotations  
- Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only such results will be counted where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Please write with black/red/green colors or with pencil.  
- To print and scan your exam (if applicable), you may leave the room. Whether you take your camera with you or not is up to you. As already announced on Moodle, it may be beneficial to have a means of communication in case of any problems.  
- If you need to go to the toilet during the exam, please inform the supervisor beforehand via private message in BB and wait for confirmation. Please do not take your smartphone/webcam with you.  

---

**Task 1**  
Multiple Choice (12 points)  
The following tasks are multiple choice/multiple answer, meaning there is at least one correct answer for each.  
Tasks with only one correct answer are scored with 1 point if correct. Tasks with more than one correct answer are scored with 0.5 points for each correct mark and 0.5 points for each incorrect mark. The minimum score per task is 0 points.  

Please mark the correct answers.  
Marked answers can be crossed out by completing the filling in.  
Crossed-out answers can be marked again by adjacent markings.  

a) *Which PTR record belongs to the IP address 133.35.3.31?  
- 35.133.31.3.in-addr.arpa.  
- 133.35.3.31.in-addr.arpa.  
- 31.3.35.133.in-addr.arpa.  
- 8.8.4.4.in-addr.arpa.  
- 4.4.8.8.in-addr.arpa.  
- 31.3.35.31.in-addr.arpa.  

b) *Which of the following terms does not fit?  
- RZ  
- NRZ  
- SDF  
- MLT3  
- Manchester  

c) *Which are not regulated media access methods?  
- Token Passing  
- CSMA/CD  
- CSMA/CA  
- CSMA/CA with ALOHA  
- RTS/CTS  

d) *Which resource record types contain IP address information?  
- AAAA  
- NS  
- MX  
- CNAME  
- PTR  
- TXT  

e) *In a URL, the query allows...  
- ...to reference sections in a document  
- ...the relative specification of a locality at the destination  
- ...the passing of variables  
- ...the specification of the application protocol  

f) *Which are not valid HTTP commands?  
- POST  
- DELETE  
- SET  
- PUT  
- GET  

g) *How many DNS zones must be created under the zones 251 and 23 at a minimum to enable a reverse lookup of all IP addresses in the network 251.23.224.0/19?  
- 172  
- 1  
- 184  
- 194  
- 246  
- 32  
- 34  
- 256  

h) *How many PTR records must be created to enable a reverse lookup of all IP addresses in the network 251.23.224.0/19?  
- 256  
- 1  
- 2356  
- 65536  
- 4495  
- 38  
- 8192  

i) *The source Q emits the symbols S, C, P, G with the given probabilities. Determine the entropy of Q.  
- S: 0.06  
- C: 0.26  
- P: 0.32  
- G: 0.36  
- 0.00  
- 2.79  
- 0.21  
- 2.75  
- 1.55  
- 1.66  
- 1.81  

j) *Which of the following factors can influence a signal in a transmission channel?  
- Low-pass filtering  
- Interference  
- Distortion  
- Attenuation  
- Noise  
- Creepy factor  

---

**Task 2**  
Short Tasks (12 points)  

a) *Briefly describe what is meant by a DNS server.  

b) *Briefly describe the process of iterative name resolution.  

c) *How should the Domain Name System be assessed in terms of user privacy?  

d) *How should an iterative name resolution be assessed in terms of trustworthiness and resistance to manipulation?  

e) *What impact could complete encryption of DNS traffic have on the various parties on the internet?  

f) *What are Glue Records used for in DNS?  

g) Given the following network topology. You receive three fragments of an IPv4 data packet of the specified sizes on your PC. The Do-Not-Fragment bit is not set. Assume that the server knows the MTU on segment 1 and adjusts segment sizes accordingly to avoid having to fragment itself. Determine the MTU of each path segment as accurately as possible. Provide a traceable calculation method.  
- Fragment 1: 5888B Offset: 0  
- Fragment 2: 2056B Offset: 736  
- Fragment 3: 1047B Offset: 993  

h) *Explain why OSPF could be assigned to Layer 3 of the ISO/OSI model.  

---

**Task 3**  
IPv4+ (16 points)  
Address scarcity is a problem with IPv4. To solve this problem, IPv4+ was developed as an IPv4-compatible solution. IPv4+ extends IPv4 with the concept of a "Door" with an associated "Door Address".  

```
Offset 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
Door Region  
0B Version IHL TOS Total Length  
4B Identification Flags Fragment Offset 0.00 Reserved  
8B TTL Protocol Header Checksum 1.23 Burundi  
12B Source Address 1.50 Cuba  
1.56 Germany  
16B Destination Address  
1.69 EU  
20B Source Door Address Destination Door Address  
1.99 Haiti  
24B Options / Padding (optional)  
```

**Figure 3.1:** IPv4+ Header and a selection of Door Address assignment proposals.  
The IPv4+ header and some door addresses are depicted in Figure 3.1. Behind each IPv4+ door is an independent IPv4 address range. Door addresses are specified in Dotted Decimal Notation, just like IPv4 addresses.  
Notation example: The IPv4+ address of the IPv4 address 2.3.4.5/30 behind Door 0.1 is 0.1|2.3.4.5/30.  

a) *How many IPv4+ addresses are there? (Justification!)  

b) *What does IHL stand for and what does it mean?  

c) *How can an IPv4+-capable router recognize whether a message is about IPv4+?  
RFC791 (Title: "Internet Protocol") states:  
No Operation  
```
+−−−−−−−−+
|00000001|
+−−−−−−−−+
Type=1  
This option may be used between options, for example, to align the beginning of a subsequent option on a 32-bit boundary.  
May be copied, introduced, or deleted on fragmentation, or for any other reason.  
```

d) *Why is it problematic to use the door addresses 1.0/8?  

e) *Why is the door address 0.00 reserved?  

f) *What is one advantage of IPv4+ over IPv6?  

g) *What is one advantage of IPv6 over IPv4+?  

Next, the IPv4/IPv4+ mixed network in Figure 3.2 will be considered.  
```
eno1:10.3.1.254/23  
SRV1  
eno1:1.50|10.3.1.254/23  
10.3.1.1/23  
PC1 S R1  
R2  
1.50|10.3.1.1/23  
eno0:10.5.2.2/30  
SRV2  
eno0:10.3.2.2/23  
1.99|10.3.2.1/23  
```

**Figure 3.2:** IPv4/IPv4+ mixed network  

h) *Draw all collision domains that do not simultaneously represent a broadcast domain in Figure 3.2. (The cloud representing the internet can be ignored, but the two routers R1 and R2 cannot.)  

i) *Draw all broadcast domains that are also collision domains in Figure 3.2. (The cloud representing the internet can be ignored, but the two routers R1 and R2 cannot.)  

j) *What routing entries does the IPv4 router R2 need to reach the networks of SRV1 and SRV2?  
```
Destination NextHop Interface  
```  

k) *PC1 sends an IPv4+ packet to 1.99|10.3.2.1. This reaches the IPv4 router R2. What happens?  

l) *SRV2 sends an IPv4+ packet to 1.50|10.3.1.1. This packet reaches the IPv4 router R2. What happens?  

m) *Explain to what extent a switch from IPv4 to IPv4+ requires changes in other layers.  

n) *Can the IPv4+ networks 1.56|10.2.3.0/24 and 1.59|10.2.4.0/24 be summarized? (Justification!)  

---

**Task 4**  
The WWNAT64 - World Wide NAT64 (20 points)  
You are responsible for the interplanetary internet infrastructure on Mars. Since Earthlings have been too wasteful with IPv4 addresses, it has been decided to forgo IPv4 and only use IPv6 instead. For this, you managed to acquire the complete IPv6 prefix 1000::/4. However, for the Solarlink satellite network, which provides the entire solar system with internet, you need a /62 prefix.  

In order for Martians to still be able to visit their outdated IPv4 favorite sites from Earth, you are building a WWNAT64 to Earth. This serves as a gateway to Earth and is capable of translating IPv6 to IPv4 addresses. For a computer on Mars to communicate with an IPv4 address on Earth, it only needs to set the last 32 bits of the requested IPv4 address in the IPv6 prefix 64:ff9b::/96 and use that address instead. Your WWNAT64 is reachable from Earth at the addresses 15.23.218.93 and 982::71:898a.  

```
eth0 eth1  
° WWNAT64 1def::bdf4/126 eth0 1def::56:df0/126  
eth1  
Solarlink2  
Mars  
eth2  
eth1  
Solarlink1  
```

**Figure 4.1:** Solarlink Network Topology  

a) *How many addresses remain for you for the IPv6 network on Mars?  

b) *Determine all IP addresses of the interfaces WWNAT64.eth0, WWNAT64.eth1, Solarlink 1.eth0, Solarlink 1.eth2, and Solarlink 2.eth1. The numerically smaller interface should also receive the smaller IP address.  

```
Interface Address Interface Address  
```  

c) *There are still older devices on Mars that do not implement the translation of IPv4 to IPv6 addresses. Since your WWNAT64 also serves as a DNS resolver, how can you exploit this circumstance so that these old devices can still call IPv4-capable Earthling sites?  

When you turn on your PC on Mars, it does not yet have an IP address. However, you want to communicate on the internet and need one. Thanks to IPv6 and SLAAC, this is not a problem. Your MAC address is 5d:38:20:bb:e3:0c and your router has been assigned the global prefix 1aff:e:de::/64.  

d) *What is the first IPv6 address that your computer automatically generates?  

e) *What does your computer need this address for?  

f) *Determine the first generated address.  

g) *What is the second IPv6 address that your PC automatically generates?  

h) *What is the purpose of this second address?  

i) *Determine the second automatically generated IPv6 address.  

j) *You want to access the domain iam.always.online from Earth, but you only receive the address 60.239.113.11 in response to the name resolution. Which IPv6 address must you define as the target to establish a connection? Clearly show how the individual components of the address come together.  

Assume your PC has the IPv6 address 1aff:e:de::42. You establish an HTTPS connection with the IPv4 address 60.239.113.11.  

```
eth0 eth1  
° Earth WWNAT64 1def:2:bdf4/126 eth0 1def::56:1df0/126  
eth1  
Solarlink1  
```

**Figure 4.2:** Copy of Figure 4.1 (so you don't have to flip through)  

k) Provide the required data at positions 1, 2, and 3 from Fig. 4.2 of the first segment that your computer sends.  
```
Src. IP: Src. IP: Src. IP:  
Src. Port: Src. Port: Src. Port:  
Dst. IP: Dst. IP: Dst. IP:  
Dst. Port: Dst. Port: Dst. Port:  
TTL: TTL: TTL:  
→ → →  
1: Solarlink2 Solarlink1  
2: Solarlink1 WWNAT64  
3: WWNAT64 Earth  
```  

l) *Make the necessary entries in the following NAT table of the WWNAT64 that are required for the HTTPS connection from the previous task k).  

```
Local IP Local Port Protocol Global Port Target IP Target Port  
```  

m) *There are 216 = 65536 different port numbers. Does this mean that your WWNAT64 can only provide a maximum of 65536 IPv6-to-IPv4 connections from Mars to Earth? Justify!  

---

**Task 5**  
Packet Pair Probing (16 points)  
Given is the situation depicted in Figure 5. The nodes 1 and 2 as well as 3 and 4 form a local network with Gigabit Ethernet. The uplink of router 2 to its ISP usually represents the limiting factor and thus limits the transmission rates and therefore also r.  

```
local network Uplink to ISP local network  
Internet  
1 2 3 4  
non-negligible spatial distance  
```

**Figure 5.1:** Network topology  

We now send ICMPv4 Echo Requests of length L from 1 to 4 and want to determine the uplink bandwidth (which corresponds to the achievable data rates) by measuring and cleverly exploiting resulting time delays at 4.  

a) *Give the serialization time and the propagation delay p between two adjacent nodes.  

b) For a possible accurate determination, it is important that the Echo Requests (and thus also the Echo Replies) are as large as possible, but the individual packets should not be fragmented.  

c) *Briefly explain how to determine the maximum MTU on the path from 1 to 4.  

d) Does the method from part b) also ensure that packets from 4 to 1 are not fragmented?  

Nodes 1 send two ICMP Echo Requests of length L to 4 immediately one after the other. We simplify by assuming that any other transmissions at routers 2 and 3 do not matter. Processing times at the nodes are neglected.  

e) *How will 4 react when it receives the request?  

f) Complete the path-time diagram below (only for packets from 1 to 4). The propagation delay within the local network can be neglected.  

g) Mark the reception pause ∆t at 4 in the solution of part e).  

h) What factors does ∆t depend on?  

i) Provide an expression for ∆t.  

j) Provide an expression for the sought data rate. Simplify the result as much as possible.  

k) Assuming r = r. Justify under what condition the method still works as desired.  

---

**Task 6**  
Wireshark (14 points)  
Given is the Ethernet frame from Figure 6, which is to be analyzed below.  

```
0x0000 0c c4 7a 80 52 58 00 25 90 57 22 4a 86 dd 60 00  
0x0010 00 00 04 d8 3a 3c 20 01 06 38 00 0c c0 71 00 00  
0x0020 00 00 00 00 00 01 20 01 4c a0 20 01 00 11 31 a0  
0x0030 6d 28 d9 38 75 0c 03 00 14 00 9a 00 00 00 60 05  
0x0040 5d d6 05 3a 11 01 20 01 4c a0 20 01 00 11 31 a0  
0x0050 6d 28 d9 38 75 0c 2a 00 14 50 40 01 08 08 00 00  
0x0060 00 00 00 00 20 03 ae 36 01 bb 05 3a 2f ef c8 ff  
0x0070 00 42  
```

**Figure 6.1:** Ethernet frame including checksum  

Please note that all subsequent parts require justification. This can be done, for example, by marking the corresponding fields in the hex dump and naming the field names. Ensure that markings can be uniquely assigned to individual tasks. Non-verifiable statements will not be graded.  

a) *Mark the sender address in Figure 6 at Layer 2.  

b) *Mark the recipient address in Figure 6 at Layer 2.  

c) *Justify what type the L3-PDU is.  

d) Provide the sender address at Layer 3 in its usual and possibly shortened form.  

e) Provide the recipient address at Layer 3 in its usual and possibly shortened form.  

f) Justify whether the addresses from tasks d) and e) are dynamically assigned or statically configured.  

From the L3-SDU it is known that it starts at offset 0x0036 and that it is ICMPv6.  

g) *Determine the type and code of the ICMP packet.  

h) Under what circumstances does a host receive such a message? Name a possible reason that likely underlies the problem!  

i) Which node is the sender of this ICMPv6 message?  
Note: Here, an address is not being asked for, but rather generally which node in the network/internet must be the sender.  

j) Justify whether it is possible to determine which packet or application triggered this message.  

---

**Additional space for solutions. Clearly mark the assignment to the respective task. Do not forget to cross out invalid solutions.**