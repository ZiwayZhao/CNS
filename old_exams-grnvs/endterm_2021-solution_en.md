Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during the attendance check by sticking a code.
- This contains only a sequential number, which is also noted in the attendance list next to the sticker in the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Endterm  
Date: Tuesday, July 27, 2021  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 08:00–09:30  

Please sign the code of conduct in the upper right corner next to your sticker.  
Otherwise, your electronic exercise performance will not be counted!

### Instructions for Processing
- This exam consists of 16 pages with a total of 6 tasks.
- The total score for this exam is 90 points.
- The tearing out of pages from the exam is prohibited.
- The following aids are permitted:
  - A non-programmable calculator (no calculator app!)
  - The cheat sheet provided by the chair without modifications in printed form
  - A dictionary in paper form without any annotations
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be counted where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write with red/green colors or with pencil.
- To print and scan your exam (if applicable), you may leave the room. Whether you take your camera with you or not is up to you. As already communicated on Moodle, it may be advantageous to have a means of communication in case of any problems.
- If you need to go to the toilet during the exam, please inform the supervisor beforehand via private message in BB and wait for confirmation. Please do not take your smartphone/webcam with you.

---

### Task 1  
Multiple Choice (12 points)  
The following tasks are multiple choice/multiple answer, meaning that at least one answer option is correct for each.  
Tasks with only one correct answer are scored with 1 point if correct. Tasks with more than one correct answer are scored with 0.5 points for each correct tick and 0.5 points for each incorrect tick. The minimum score per task is 0 points.

Please tick the correct answers.  
Ticked answers can be crossed out by completely filling them in.  
Crossed out answers can be ticked again by adjacent markings.

1. **Which PTR record belongs to the IP address 133.35.3.31?**  
   - 35.133.31.3.in-addr.arpa.  
   - 133.35.3.31.in-addr.arpa.  
   - 31.3.35.133.in-addr.arpa.  
   - 8.8.4.4.in-addr.arpa.  
   - 4.4.8.8.in-addr.arpa.  
   - 31.3.35.31.in-addr.arpa.  

2. **Which of the following terms does not fit?**  
   - RZ  
   - NRZ  
   - SDF  
   - MLT3  
   - Manchester  

3. **Which are not regulated media access methods?**  
   - Token Passing  
   - CSMA/CD  
   - CSMA/CA  
   - CSMA/CA with RTS/CTS  

4. **Which resource record types contain IP address information?**  
   - AAAA  
   - NS  
   - MX  
   - CNAME  
   - PTR  
   - TXT  

5. **In a URL, the query...**  
   - ...allows referencing sections in a document  
   - ...provides the relative specification of a location on the target  
   - ...passes variables  
   - ...specifies the application protocol  

6. **Which are not valid HTTP commands?**  
   - POST  
   - DELETE  
   - SET  
   - PUT  
   - GET  

7. **How many DNS zones must be created under the zones 251 and 23 at a minimum to enable a reverse lookup of all IP addresses in the network 251.23.224.0/19?**  
   - 172  
   - 1  
   - 184  
   - 194  
   - 246  
   - 32  
   - 34  
   - 256  

8. **How many PTR records must be created to enable a reverse lookup of all IP addresses in the network 251.23.224.0/19?**  
   - 256  
   - 1  
   - 2356  
   - 65536  
   - 4495  
   - 38  
   - 8192  

9. **The source Q emits the characters S, C, P, G with the given occurrence probabilities. Determine the entropy of Q.**  
   - S: 0.06  
   - C: 0.26  
   - P: 0.32  
   - G: 0.36  

10. **Which of the following factors can influence a signal in a transmission channel?**  
    - Low-pass filtering  
    - Interference  
    - Distortions  
    - Attenuation  
    - Noise  
    - Creepy factor  

---

### Task 2  
Short Tasks (12 points)  

1. **Briefly describe what is meant by a DNS server.**  
   - Either a resolver or a nameserver.  

2. **Briefly describe the process of iterative name resolution.**  
   - A resolver resolves DNS requests zone by zone starting from the root by iteratively querying each authoritative nameserver, which either provides the authoritative nameservers of the next zone or (if ultimately known) the answer to the query.  

3. **How should the Domain Name System be evaluated regarding user privacy?**  
   - DNS operates unencrypted, allowing all parties who can intercept network traffic to create extensive usage profiles. In particular, the respective ISP and the operator of the used resolver are trivially able to create user profiles of their customers. With relatively simple methods, this is also possible for other users in the same (private) network.  

4. **How should an iterative name resolution be evaluated regarding trustworthiness and resistance to manipulation?**  
   - Since a resolver only queries trustworthy nameservers (based on the root hints that are fixed), the name resolution should also be trustworthy. However, manipulation during the transmission of requests/responses over the Internet cannot be ruled out.  

5. **What impact could complete encryption of DNS traffic have on the various parties on the Internet?**  
   - Only resolvers can create user profiles. This centralization of data makes it more valuable.  

6. **Why are glue records needed in DNS?**  
   - If a nameserver is located in the zone for which it is authoritative, it must send the corresponding zone in addition to the domain name of the nameserver (NS record) its IP address (A or AAAA record) as glue records. Otherwise, a name resolution is not possible.  

7. **Given the following network topology. You receive three fragments of an IPv4 data packet of the specified sizes on your PC. The Do-Not-Fragment bit is not set. Assume that the server knows the MTU on segment 1 and adjusts segment sizes accordingly to avoid having to fragment itself. Determine the MTU of each path segment as accurately as possible. Provide a traceable calculation method.**  
   - Fragment 1: 5888B Offset: 0  
   - Fragment 2: 2056B Offset: 736  
   - Fragment 3: 1047B Offset: 993  

   - MTU Segment 1: (5888 + 2056 + 1047)B = 8991B  
   - MTU Segment 2: (5888 + 2056)B = 7944B  
   - MTU Segment 3: max(5888, 2056, 1047)B = 5888B  

8. **Explain why OSPF could be assigned to Layer 3 of the ISO/OSI model.**  
   - Routing protocols exchange path information and thus enable path selection at Layer 3. Therefore, routing protocols are often assigned to this layer. At the same time, they define processes that are implemented by applications that expect and process incoming data at specific addresses or even ports (BGP). This does not distinguish them from application layer protocols like DHCP or SMTP, which is why they can also be assigned to Layer 7. This is particularly evident with BGP, which builds on TCP and thus strictly speaking cannot be assigned to Layer 3 at all.  

---

### Task 3  
IPv4+ (16 points)  
Address scarcity is a problem with IPv4. To solve this problem, IPv4+ was developed as an IPv4-compatible solution. IPv4+ extends IPv4 by the concept of a "Door" with an associated "Door Address".  

**IPv4+ Header and a Selection of Door Address Assignment Proposals**  
The IPv4+ header and some door addresses are depicted in the figure. Behind each IPv4+ door is an independent IPv4 address range. Door addresses are specified in Dotted Decimal Notation, just like IPv4 addresses.  
Notation example: The IPv4+ address of the IPv4 address 2.3.4.5/30 behind door 0.1 is 0.1|2.3.4.5/30.  

1. **How many IPv4+ addresses are there? (Justification!)**  
   - An IPv4+ address consists of a 32-bit IPv4 address and a 16-bit door address, thus there are 2^(32bit + 16bit) = 281474976710656 addresses.  

2. **What does IHL stand for and what does it mean?**  
   - The abbreviation stands for Internet Header Length. Meaning: Length of the IPv4(+)-header in multiples of 4B.  

3. **How can an IPv4+-capable router recognize whether a message is IPv4+?**  
   - The IHL field has the value 6B. Due to the longer addresses stored in the options, the value of IHL changes. Otherwise, the header is indistinguishable from IPv4.  

4. **Why is it problematic to use the door address 1.0/8?**  
   - Because there is already an IPv4 option that can appear at the relevant point but has nothing to do with IPv4+.  

5. **Why is the door address 0.0 reserved?**  
   - The IPv4 address range behind this door address is currently in use. To maintain compatibility with IPv4, it must not be reassigned. (Moreover, there is also an IPv4 option that can appear at the relevant point but has nothing to do with IPv4+.)  

6. **What is an advantage of IPv4+ over IPv6?**  
   - IPv4+ is theoretically transparent for existing IPv4 hardware. Existing hardware can thus continue to be used.  

7. **What is an advantage of IPv6 over IPv4+?**  
   - With IPv6, fragmentation in the network is no longer necessary. Fragmentation occurs instead by the sender. This relieves routers.  

8. **The IPv4/IPv4+ mixed network in the figure should be considered.**  
   - PC1: 10.3.1.254/23  
   - SRV1: 10.3.1.1/23  
   - R1: 1.50|10.3.1.254/23  
   - R2: 1.50|10.3.1.1/23  
   - SRV2: 10.5.2.2/30  
   - 10.3.2.2/23: 1.99|10.3.2.1/23  

9. **Draw all collision domains that do not also represent a broadcast domain in the figure. (The cloud representing the Internet can be ignored, but the two routers R1 and R2 cannot.)**  
   - {PC1, SRV1, R1} and {R2, SRV2}  

10. **Draw all broadcast domains that are also collision domains in the figure. (The cloud representing the Internet can be ignored, but the two routers R1 and R2 cannot.)**  
    - {R2, SRV1} and {R2, SRV2}  

11. **What routing entries does the IPv4 router R2 need to reach the networks of SRV1 and SRV2?**  
    - Destination: 10.3.0.0/23 Next Hop: 0.0.0.0 Interface: eno1  
    - Destination: 10.3.2.0/23 Next Hop: 0.0.0.0 Interface: eno0  

12. **PC1 sends an IPv4+ packet to 1.99|10.3.2.1. This reaches the IPv4 router R2. What happens?**  
    - IPv4 router R2 interprets the packet as an IPv4 packet. R2 forwards the packet to SRV2.  

13. **SRV2 sends an IPv4+ packet to 1.50|10.3.1.1. This packet reaches the IPv4 router R2. What happens?**  
    - IPv4 router R2 interprets the packet as an IPv4 packet. R2 forwards the packet to SRV1.  

14. **Explain to what extent a switch from IPv4 to IPv4+ requires changes in other layers.**  
    - Two examples:  
      - Layer 2: ARP "continues to work" as long as the IPv4 addresses are different. However, with the same IPv4 addresses with different door addresses, there would be problems. (Here, an extension of the ARP implementation for IPv4+ would be necessary.)  
      - Layer 4: Current implementations that determine a TCP/UDP 5-tuple would ignore the door address. Also, the checksum calculations.  

15. **Can the IPv4+ networks 1.56|10.2.3.0/24 and 1.59|10.2.4.0/24 be summarized? (Justification!)**  
    - No, different door addresses cannot be summarized. (Considering only IPv4: No, since 3 and 4 are in the third octet of the IPv4 addresses not in a /23 network.)  

---

### Task 4  
The WWNAT64 - World Wide NAT64 (20 points)  
You are responsible for the interplanetary Internet infrastructure on Mars. Since Earthlings have been too wasteful with IPv4 addresses, it has been decided to forgo IPv4 and only use IPv6 instead. For this, you managed to acquire the entire IPv6 prefix 1000::/4. However, for the Solarlink satellite network, which provides the entire solar system with Internet, you need a /62 prefix.  

To enable Martians to visit their outdated favorite Earth IPv4 sites, you are building a WWNAT64 to Earth. This serves as a gateway to Earth and is capable of translating IPv6 to IPv4 addresses. For a computer on Mars to communicate with an IPv4 address on Earth, it only needs to set the last 32 bits of the requested IPv4 address in the IPv6 prefix 64:ff9b::/96 and use this address instead. Your WWNAT64 is reachable from Earth at the addresses 15.23.218.93 and 982::71:898a.

**Solarlink Network Topology**  

1. **How many addresses do you have left for the IPv6 network on Mars?**  
   - 2^128 - 2^4 - 2^128 - 2^62 = 2^124 = 2^66  

2. **Determine all IP addresses of the interfaces WWNAT64.eth0, WWNAT64.eth1, Solarlink 1.eth0, Solarlink 1.eth2, and Solarlink 2.eth1. The numerically smaller interface should also receive the smaller IP address.**  
   - Interface: WWNAT64.eth0 Address: 15.23.218.93  
   - Interface: WWNAT64.eth1 Address: 982::71:898a  
   - Interface: Solarlink 1.eth0 Address: 1def::bdf5  
   - Interface: Solarlink 1.eth2 Address: 1def::56:df2  
   - Interface: Solarlink 2.eth1 Address: 1def::56:df1  

3. **There are still older devices on Mars that do not implement the translation of IPv4 to IPv6 addresses. Since your WWNAT64 also serves as a DNS resolver, how can you take advantage of this circumstance so that these old devices can still call up IPv4-capable Earth sites?**  
   - The resolver can take over the translation of the addresses. For an IPv4-capable server (recognizable by the fact that only an A record is stored in DNS), the DNS resolver can additionally deliver the translated IPv6 addresses as AAAA records from the WWNAT64.  

4. **When you turn on your PC on Mars, it does not yet have an IP address. However, you want to communicate on the Internet and need one. Thanks to IPv6 and SLAAC, this is not a problem. Your MAC address is 5d:38:20:bb:e3:0c and your router has been assigned the global prefix 1aff:e:de::/64.**  
   - What is the first IPv6 address that your computer automatically generates?  
     - The PC will certainly generate a Link-Local address.  

5. **What does your computer need this address for?**  
   - It needs it to communicate with the router in the local direct connection network and, among other things, to query the global prefix of the current subnet.  

6. **Determine the first generated address.**  
   - The Link-Local address generated by SLAAC is fe80::5f38:20ff:febb:e30c.  

7. **What is the second IPv6 address that your PC automatically generates?**  
   - The PC will certainly generate a Global-Unique address.  

8. **What is the purpose of this second address?**  
   - The PC needs the Global-Unique address to be reachable globally on the Internet and to communicate.  

9. **Determine the second automatically generated IPv6 address.**  
   - The generated Global-Unique address is 1aff:e:de::5f38:20ff:febb:e30c.  

10. **You want to call the domain iam.always.online from Earth, but you only receive the address 60.239.113.11 as a response to the name resolution. Which IPv6 address must you define as the target to establish a connection? Make clear how the individual components of the address come about.**  
    - First, the decimal representation of the IPv4 address must be converted into hex format. The hex digits can then be directly taken into the last 4 bytes of the IPv6 address.  
    - NAT64 Prefix: 64:ff9b::/96  
    - Resulting IPv6 Address: 64:ff9b::3cef:710b  

11. **Assume your PC has the IPv6 address 1aff:e:de::42. You establish an HTTPS connection with the IPv4 address 60.239.113.11.**  
    - Provide the required data at positions 1, 2, and 3 from Fig. 4.2 of the first segment that your computer sends.  
      - Src. IP: 1aff:e:de::42  
      - Src. Port: 3608  
      - Dst. IP: 64:ff9b::3cef:710b  
      - Dst. Port: 443  

12. **Make the required entries in the following NAT table of the WWNAT64 that are necessary for the HTTPS connection from the previous task.**  
    - Local IP: 1aff:e:de::42  
    - Local Port: 3608  
    - Protocol: TCP  
    - Global Port: 443  
    - Target IP: 60.239.113.11  
    - Target Port: 443  

13. **There are 2^16 = 65536 different port numbers. Does this mean that your WWNAT64 can only support a maximum of 65536 IPv6-to-IPv4 connections from Mars to Earth? Justify!**  
    - According to the NAT table, the WWNAT64 also considers the protocol, the target IPv4 address, and the target port on Earth. This means it is not limited by the maximum number of its own ports and can thus support up to 2^16 (minus reserved ports) connections from clients per target on Earth and protocol.  

---

### Task 5  
Packet Pair Probing (16 points)  
Given is the situation depicted in Figure 5.1. 1 and 2 as well as 3 and 4 form a local network with Gigabit Ethernet. The uplink of router 2 to its ISP usually represents the limiting factor and thus limits the transmission rates and therefore also the throughput.  

Now we will send ICMPv4 Echo Requests of length L from 1 to 4 and want to determine the uplink bandwidth (which corresponds to the achievable data rate) through measurement and exploitation of resulting time delays at 4.  

1. **Generally state the serialization times as well as the propagation delay p between two neighboring nodes.**  
   - s = p = d_ij / v_c, where d is the distance between i and j in m.  

2. **For the most accurate determination, it is important that the echo requests (and thus also the echo replies) are as large as possible, but the individual packets must not be fragmented.**  

3. **Briefly explain how one can determine the maximum MTU on the path from 1 to 4.**  
   - 1 sends a packet with the local MTU, with the DF bit set. If an intervening link is limiting, 1 will receive an ICMP Destination Unreachable/Fragmentation Needed. This may repeat if a subsequent link has an even smaller MTU.  

4. **Does the method from part b) also ensure that packets from 4 to 1 are not fragmented?**  
   - No, because packets from 4 to 1 could be routed over a different route on the Internet, and consequently a different Path MTU could apply.  

5. **Node 1 sends two ICMP Echo Requests of length L to 4 one after the other. We simplify by assuming that any other transmissions at routers 2 and 3 do not matter. Processing times at the nodes are neglected.**  
   - How will 4 react when it receives the request?  
     - It should respond with an ICMP Echo Reply of the same size. (Payload of the requests is usually sent back in the reply.)  

6. **Complete the following round-trip time diagram (only for packets from 1 to 4). The propagation delay within the local network can be neglected.**  

   ```
   1     2     3     4
   |-----|-----|-----|
   ∆t
   ```

7. **Mark the reception pause ∆t at 4 in the solution of part e).**  

8. **What factors does ∆t depend on?**  
   - On L and r_ij.  

9. **Provide an expression for ∆t.**  
   - ∆t = (s_23 + s_34) / r_23.  

10. **No scoring if parts e), f), and g) are not solved or solved incorrectly (as a derivation without these is not possible).**  

11. **Provide an expression for the sought data rate. Simplify the result as much as possible.**  
   - The resolving result from part h) gives: r = L / (∆t + L).  

12. **No scoring if parts e), f), and g) are not solved or solved incorrectly (as a derivation without these is not possible).**  

13. **Assuming r = r_12 = r_34. Justify under what condition the method still functions as desired.**  
   - As long as r_34 ≥ r_23, otherwise no ∆t at 4 arises, and r_12 ≥ r_23, otherwise the uplink is not fully utilized.  

---

### Task 6  
Wireshark (14 points)  
Given is the Ethernet frame from Figure 6, which is to be analyzed.  

```
0x0000 0c c4 7a 80 52 58 00 25 90 57 22 4a 86 dd 60 00
0x0010 00 00 04 d8 3a 3c 20 01 06 38 00 0c c0 71 00 00
0x0020 00 00 00 00 00 01 20 01 4c a0 20 01 00 11 31 a0
0x0030 6d 28 d9 38 75 0c 03 00 14 00 9a 00 00 00 60 05
0x0040 5d d6 05 3a 11 01 20 01 4c a0 20 01 00 11 31 a0
0x0050 6d 28 d9 38 75 0c 2a 00 14 50 40 01 08 08 00 00
0x0060 00 00 00 00 20 03 ae 36 01 bbc05 3a 2f ef c8 ff
0x0070 00 42
```

**Figure 6.1: Ethernet frame including checksum**  

Note that for all subsequent parts, justifications are required. This can be done, for example, by marking the corresponding fields in the hex dump and naming the field names. Ensure that markings can be uniquely assigned to individual tasks. Non-verifiable statements will not be evaluated.

1. **Mark the sender address in Figure 6 at Layer 2.**  

2. **Mark the recipient address in Figure 6 at Layer 2.**  

3. **Justify what type the L3-PDU is.**  
   - Ethertype: 0x86dd (IPv6)  

4. **Provide the sender address at Layer 3 in its usual and possibly shortened form.**  
   - 2001:638:c:c071::1  

5. **Provide the recipient address at Layer 3 in its usual and possibly shortened form.**  
   - 2001:4ca0:2001:11:31a0:6d28:d938:750c  

6. **Justify whether the addresses from parts d) and e) are dynamically assigned or statically configured.**  
   - Both addresses are very likely statically configured, as the usual SLAAC insertion ff:fe in octets 11 and 12 is missing.  
   - Note: The address 2001:4ca0:2001:11:31a0:6d28:d938:750c could also have been assigned via DHCPv6.  

7. **From the L3-SDU it is known that it starts at offset 0x0036 and concerns ICMPv6.**  
   - Determine the type and code of the ICMP packet.  
   - Type: 0x03 (TimeExceeded)  
   - Code: 0x00 (HopLimitExceeded)  

8. **Under what circumstances does a host receive such a message? Name a possible reason that this problem likely lies behind!**  
   - When the hop limit of a packet reaches 0 during forwarding. This usually happens only when a routing loop exists.  

9. **Which node is the sender of this ICMPv6 message?**  
   - Note: Here, an address is not asked for, but rather generally which node in the network/Internet must be the sender.  
   - A router on the way from 2001:638:c:c071::1 to an (unknown) destination.  

10. **Justify whether it can be determined which packet or which application triggered this message.**  
    - The ICMPv6 header is followed by the IPv6 header and the first 8B payload of the packet that was discarded due to the hop limit. This particularly contains the original L3 addresses (source and destination), the type of the L4 payload, and in the case of TCP/UDP, the port numbers.  

---

### Additional Space for Solutions. Clearly mark the assignment to each sub-task.  
Do not forget to cross out invalid solutions.