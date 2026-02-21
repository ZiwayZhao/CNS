Faculty of Computer Science  
Technical University of Munich  

**Fundamentals of Computer Networks and Distributed Systems**  
Module: IN0010  
Date: 28.07.2015  
Examiner: Prof. Dr. Uwe Baumgarten  
Exam: Endterm  

**Exam Details**  
First Correction  
Second Correction  

**Lecture Hall**  
Leave from: __________ to: __________  
Leave from: __________ to: __________  
Submitted early at: __________  
Other: __________  

**Endterm**  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr. Uwe Baumgarten  
Department of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  
Tuesday, 28.07.2015  
11:00–12:30  

- This exam consists of:
  - 20 pages with a total of 5 tasks as well as
  - a double-sided printed formula collection.
- Please check now that you have received a complete set of information.
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only such results will be graded where a solution path is recognizable. Explanations for tasks are generally required unless explicitly stated otherwise in the respective sub-task.
- Do not write with red/green colors or with pencil.
- The total number of points is 85.
- The following aids are permitted:
  - a non-programmable calculator
  - a dictionary in the native language without annotations
- Please turn off your mobile phones completely and pack them, as well as all other electronic devices and other documents, into your bags and close them.

**Note:**  
Unless otherwise stated, we assume that 1 B = 8 bits.

---

**Task 1**  
New Horizons (16 points)  

New Horizons is a NASA space probe that reached its main target, Pluto, two weeks ago after a travel time of more than nine years, which was considered the outermost planet of our solar system until 2012. Communication with it is a technical challenge due to the great distance to Earth, which we will examine more closely below.

**Pluto**  
**New Horizons**  
Velocity Relative to Pluto (km/s): 13.80  

*Figure 1.1: Trajectory of the New Horizons probe since its launch*  

(a) A signal sent by the probe on July 14, 2015, took almost 4 hours and 25 minutes to arrive on Earth. Determine the distance between the space probe and Earth in km.  

1. \( t_p = \nu c \)  
2. \( d = t_p \nu c = \nu = 1(4 \cdot 60 + 25) \cdot 60 \text{s} \cdot 3 \cdot 10^8 \text{s} \)  
   \( \approx 4.77 \cdot 10^9 \text{km} \)  

(b) Assume that the probe will take 60 days to transmit 5 Gbit of collected data to Earth. Determine the average transmission rate in the unit bit/s.  

1. \( r = \frac{5 \cdot 10^9 \text{Gbit}}{60 \cdot 24 \cdot 3600 \text{s}} \)  
   \( \approx 965 \text{bit/s} \)  

(c) Justify which modulation method is being used.  
Phase Shift Keying, as the signal space points are always arranged on the unit circle around the coordinate origin.  
Alternatively, the exclusion method: (b) is not ASK, as a quadrature component is obviously included. (c) is not QAM, as the energy (magnitude of the vector from the origin to the respective signal space point) is always constant. Thus, it remains PSK.

(d) How many bits per symbol can be represented in the signal spaces (a)–(c) from Figure 1.2?  
With \( N \) signal space points, each of the \( N \) symbols encodes \( \log_2(N) \) bits. Thus, it is 1 bit, 2 bits, or 3 bits per symbol.

(e) Explain which of the three options generally has the lowest bit error rate.  
BPSK (a) is the most robust modulation in this case, as only two signal space points need to be distinguished, whose distance from each other is maximal.

To still be able to transmit images to Earth, an error-correcting code is now used. This forms blocks of 251 bits into 255-bit long code words and allows the correction of up to 2 arbitrary single-bit errors per code word.

(f) How many code words will each frame be divided into?  
\( N = \frac{8000 \text{bit}}{251 \text{bit}} = 32 \)

(g) Determine the probability of a correctly transmitted code word.  
Let \( X \) be a random variable that counts the number of bit errors per code word. Then the probability for a successfully transmitted code word is:  
\( Pr[X \leq 2] = \sum_{i=0}^{2} \binom{n}{i} p^i (1-p)^{n-i} \)  
Where \( p = 0.001 \) and \( n = 255 \).  
Thus, the probability is approximately 99.80%.

(h) Determine the probability of a correctly transmitted frame using the described channel coding.  
Analogous to sub-task 1f):  
\( Pr[Y = 0] = (1 - p')^N \approx 93.80\% \)

---

**Task 2**  
Ethernet (14 points)  

Given is a hex dump in network byte order of an Ethernet frame, which is to be analyzed.  

**Ethernet Header**  
```
0x0000 d0 e1 40 97 ec ea 00 0d 2e 00 40 01 08 00 45 00
0x0010 00 38 00 00 00 00 f1 01 8c 2b 3e 9a 59 2e ac 13
0x0020 f9 bd 0b 00 bf 50 00 00 00 00 45 00 00 3c 15 b2
0x0030 00 00 01 11 ea 81 ac 13 f9 bd 81 bb 91 f1 d4 0f
0x0040 82 be 00 28 de b8
```

*Figure 2.1: Hex dump of an Ethernet frame in network byte order*  

(a) Mark the beginning and end of the Ethernet header in Figure 2.1.  

(b) Justify which protocol is used at layer 3.  
EtherType 0x0800 stands for IPv4.

(c) Determine the length of the header at layer 3 (justification) and mark its end in Figure 2.1.  
In IPv4, the header length is encoded as a multiple of 4 bytes in the lower nibble of the first byte (IHL). Specifically: 0x45 → 5 = 20B.

(d) Provide TTL or Hop Count in decimal and hexadecimal notation, if contained in the packet.  
TTL is 0xf1 = 241.

(e) Justify to which protocol the layer 3 SDU belongs.  
Protocol number is 0x01 = ICMPv4.

Given is the SDU of layer 3 of another packet shown in Figure 2.2. It is known that this is ICMPv4.

*Figure 2.2: ICMP message including ICMP header in network byte order*  

(f) Determine the type and code of the ICMP message.  
Time Exceeded / TTL expired in transit.

(g) What causes such a message?  
If a router receives a packet with TTL=1 (or with Hop Count 1 in IPv6) that is to be forwarded, it will be discarded and a Time Exceeded / TTL expired in transit will be sent back to the original sender of the discarded packet.

(h) Mark the end of the ICMP header in Figure 2.2.  

(i) Explain what the payload of such a message generally contains.  
The payload contains the IP headers and the first 8 bytes of the layer 3 SDU of the packet that triggered the ICMP TTL Exceeded message.

(j) Explain how NAT must differentiate between TCP/UDP and ICMP.  
ICMP has no port numbers but rather ICMP identifiers, which can instead be used by a NAT.

(k) Explain how a NAT-capable router can determine the recipient of this specific ICMP message.  
The last 8 bytes of the payload contain the IP address of the sender of the original message (which was discarded) as well as either the ICMP identifier or, in this specific case, the UDP port numbers (especially the source port).

---

**Task 3**  
Domain Name System (DNS) (16 points)  

*Figure 3.1: DNS Namespace*  

Figure 3.1 shows an excerpt from the DNS namespace. The zone grnvs.net. is hosted on the authoritative nameserver bifrost.grnvs.net. The IP addresses assigned to the FQDNs are provided by the depicted servers.

(a) Briefly explain what DNS is used for.  
Mapping between FQDNs and IP addresses.

(b) Mark and name all name components for the FQDN playground.grnvs.net. as precisely as possible.  
- Second Level Domain: playground  
- Top Level Domain: grnvs.net.  
- Hostname/Sublevel domain: playground.grnvs.net.  

(c) Complete the given zone file for the zone grnvs.net. The SOA record is already fully provided. Mark FQDNs clearly by suitable writing style.  
**Note:** Additional blank lines are provided. Strike out invalid entries clearly.  

```
FQDN                Record Type   Value
grnvs.net.         SOA           bifrost.grnvs.net. root.grnvs.de. 130m 5m 7d 1m
grnvs.net.         NS            bifrost.grnvs.net.
playground.grnvs.net.  AAAA      2001:db8::1
www.grnvs.net.    A             188.95.235.253
bifrost.grnvs.net. A             78.47.25.36
```

We now consider the network topology shown in Figure 3.2. Client 1 and Client 2 use the router as an access point to the internet and as a resolver. The router uses resolver-a.google.com as a resolver for recursive name resolution. Its IP addresses are known to the router. The authoritative nameservers do not allow recursion. The authoritative nameservers for the respective zones are listed in Table 3.1.

*Figure 3.2: Network topology*  

| Zone                        | Authoritative Nameserver          |
|-----------------------------|-----------------------------------|
| .                           | a.root-servers.net.               |
| com., net.                  | a.gtld-servers.net.               |
| google.com.                 | ns1.google.com.                   |
| grnvs.net.                  | bifrost.grnvs.net.                |

Assume for the following sub-tasks that all DNS caches are initially empty.

(d) Client 1 wants to access playground.grnvs.net. Draw all necessary DNS messages in Figure 3.2 using arrows and number them in the order. The first message is already given as assistance.  
**Note:** If necessary, you will find another template of Figure 3.2 on page 9. Strike out invalid solutions clearly.

(e) Immediately afterwards, Client 2 wants to resolve the address of www.grnvs.net. Briefly explain how this resolution differs from sub-task 3d).  
Request to the router, then to resolver-a.google.com (as far as identical), from there directly to bifrost.grnvs.net. since the authoritative nameserver for grnvs.net is already cached.

(f) Explain the difference between recursive and iterative name resolution.  
In recursive resolution, only one request for a resource record is made to a configured resolver, which returns the final answer. In iterative resolution, the FQDN is resolved starting from the root zone (or at the last known SOA) by querying the authoritative nameservers for the respective zones. Their responses either include the FQDN of an authoritative nameserver of the next lower zone or the final resource record if the queried nameserver is authoritative for it.

(g) Which message pairs from sub-task 3d) involve iterative name resolution?  

(h) Justify why DNS messages are generally transmitted over UDP and not over TCP.  
TCP is a connection-oriented protocol, while UDP is connectionless. For data (here DNS messages) to be exchanged, a connection must first be established. This takes additional time due to the necessary 3-way handshake.

(i) To which IP address does the reverse DNS FQDN 4.4.8.8.in-addr.arpa. belong?  
Reverse-Lookup-Zone 8.8.4.4 (the term "reverse" does not mean that the address is read from behind...).

---

**Task 4**  
IPv4 and Routing (20 points)  

Given is the network topology from Figure 4.1. R connects the networks NET1 and NET2 and the internet. R is connected to the internet via GW. The network 188.95.233.96/27 is used for the connection to GW.

*Figure 4.1: Topology*  

(a) Provide the network address, broadcast address, and the number of usable addresses for the address blocks 131.159.40.0/21 and 188.95.233.96/27.  
- 131.159.40.0/21  
  - Network Address: 131.159.40.0  
  - Broadcast Address: 131.159.47.255  
  - Number of Usable Addresses: 2046  
- 188.95.233.96/27  
  - Network Address: 188.95.233.96  
  - Broadcast Address: 188.95.233.127  
  - Number of Usable Addresses: 30  

(b) Enter the respective IPv4 address in the connected network in the solution fields in Figure 4.1. R should receive the highest usable IPv4 address, C and GW should receive the lowest usable IPv4 address in their respective subnets.

(c) Justify whether NET1 and NET2 can be summarized in the routing table of GW.  
No. NET1 and NET2 are not in the same /20 prefix. For bits 17 to 24: 40 = 00101000, 48 = 00110000.

(d) Name and explain the procedure by which a router decides through which interface a packet is forwarded.  
Longest Prefix Matching. The routing table is searched in descending order of prefix length. If the destination IP matches the entry's subnet mask, this entry (with the associated interface) is chosen.

(e) Provide the complete routing table for R, including all directly connected networks, so that NET1 and NET2 can reach the internet and be reached from there. Summarize as much as possible.  
**Note:** Additional blank lines are provided. Strike out invalid entries clearly.  

| Destination               | Next Hop       | Interface |
|---------------------------|----------------|-----------|
| 188.95.233.96/27         | 0.0.0.0       | eth1      |
| 131.159.40.0/21          | 0.0.0.0       | eth0      |
| 131.159.48.0/21          | 0.0.0.0       | wlan0     |
| 0.0.0.0/0                 | 188.95.233.97 | eth1      |

Client C now sends an Echo Request to the server with the IPv4 address 192.0.2.13. The ICMP header and payload are a total of 64 octets long. The header fields for this packet at points P1 and P2 (see Figure 4.1) are to be specified. If a field cannot be uniquely determined, make a sensible choice. The number system used is to be clearly indicated. Addresses are to be specified in the form <Device>.<Interface>.<Address Type> (e.g., R.wlan0.MAC).

(f) Enter the specific value of the Ethernet header in the solution field.  
P1: R.eth0.MAC C.eth0.MAC 0x0800 Payload FCS  
P2: GW.eth0.MAC R.eth1.MAC 0x0800 Payload FCS  

(g) Enter the specific value of the IP header in the solution field.  
P1:  
```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
0B 4 5 0 84 1
4B 0 0 1 0 0
8B 64 1 (Header Checksum)
12B C.eth0.IPv4
16B Server.eth0.IPv4
20B ICMP Header and Payload
```
P2:  
```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
0B 4 5 0 84
4B 0 0 1 0 0
8B 64 1 (Header Checksum)
12B C.eth0.IPv4
16B Server.eth0.IPv4
20B ICMP Header and Payload
```

(h) Through which procedure could the IPv4 address at interface C.eth0 be automatically configured?  
DHCP (Dynamic Host Configuration Protocol).

(i) Argue why the router should not forward the packet with the destination address 10.0.0.1.  
The router should not forward the packet as it concerns a private IP address which is not unique on the internet.

---

**Additional space for solutions – please clearly mark the affiliation with the respective task and strike out invalid solutions!**