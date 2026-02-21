Faculty of Computer Science  
Technical University of Munich  
Fundamentals of Computer Networks and Distributed Systems  
Module: IN0010 Date: 28.07.2015  
Examiner: Prof. Dr. Uwe Baumgarten Exam: Endterm  

**A1 A2 A3 A4 A5**  
First Correction  
Second Correction  
Exit from Lecture Hall from to  
from to  
Submitted Early by  
Miscellaneous  
Endterm  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr. Uwe Baumgarten  
Department of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  
Tuesday, 28.07.2015  
11:00–12:30  

- This exam consists of  
  - 20 pages with a total of 5 tasks as well as  
  - a double-sided formula collection.  
Please check now that you have received a complete set of information.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be graded where a solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-task.  
- Please write with red/green colors or with a pencil.  
- The total number of points is 85.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - a dictionary German native language without annotations  
- Please turn off your mobile phones completely and pack them as well as all other electronic devices and other documents into your bags and close them.  

Note:  
- Unless stated otherwise, we assume that 1B = 8 bits applies.  

---

**Task 1**  
New Horizons (16 points)  
New Horizons is a NASA space probe that reached its primary target Pluto today after a travel time of more than nine years, which until 2012 was considered the outermost planet of our solar system. The communication with it is a technical challenge due to the great distance to Earth, which we will examine more closely below.  

**Pluto**  
**New Horizons**  
**Velocity Relative to Pluto (km/s): 13.80**  

*Image 1.1: Trajectory of the New Horizons probe since its launch*  

a)* A signal sent by the probe on July 14, 2015, took just under 4h 25min to arrive on Earth. Determine the distance between the spacecraft and Earth in km.  

b)* Assume that the probe will take 60 days to transmit 5 Gbit of collected data to Earth. Determine the average transmission rate in the unit bit/s.  

1 Due to its small size, some anomalies in its orbit around the sun, and numerous similar objects suspected in the Kuiper Belt, Pluto is no longer officially considered a planet today. The common designation is "dwarf planet."  
2 Image source: http://pluto.jhuapl.edu/Mission/Where-is-New-Horizons/index.php  

The probe uses only a modulation method with different signal space assignments, which are shown in Image 1.2. Depending on the signal quality, one of these assignments is selected.  

*Image 1.2: Possible signal spaces*  

c)* Justify which modulation method must be used.  

d)* How many bits per symbol can be represented in the signal spaces (a) – (c) from Image 1.2?  

e)* Explain which of the three options generally exhibits the lowest bit error rate.  

Assuming simplistically that the probe transmits data in frames of fixed length of 1000B to Earth, due to the great distance, a bit error rate of α = 10^-3 is to be expected without further measures. It is assumed that bit errors occur independently of each other and are uniformly distributed.  

f)* Determine the probability that a frame transmitted by the probe is transmitted error-free.  

To still be able to transmit images to Earth, an error-correcting code is now used. This forms 251-bit long blocks on 255-bit long codewords and allows the correction of up to 2 arbitrary single bit errors per codeword.  

g)* Into how many codewords is each frame divided?  

h)* Determine the probability for a correctly transmitted codeword.  

i)* Determine the probability for a correctly transmitted frame using the described channel coding.  

---

**Task 2**  
Ethernet (14 points)  
Given is a hex dump in Network Byte Order of an Ethernet frame shown in Image 2.1, which is to be analyzed.  

```
0x0000 d0 e1 40 97 ec ea 00 0d 2e 00 40 01 08 00 45 00
0x0010 00 38 00 00 00 00 f1 01 8c 2b 3e 9a 59 2e ac 13
0x0020 f9 bd 0b 00 bf 50 00 00 00 00 45 00 00 3c 15 b2
0x0030 00 00 01 11 ea 81 ac 13 f9 bd 81 bb 91 f1 d4 0f
0x0040 82 be 00 28 de b8
```

*Image 2.1: Hex dump of an Ethernet frame in Network Byte Order*  

a)* Mark the beginning and end of the Ethernet header in Image 2.1.  

b) Justify which protocol is used at Layer 3.  

c) Determine the length of the header at Layer 3 (justification) and mark its end in Image 2.1.  

d) Provide - if contained in the packet - TTL or Hop Count in decimal and hexadecimal notation.  

e) Justify to which protocol the Layer 3 SDU belongs.  

*Type Code End ICMPv4 Header*  
*ICMPv4 Header*  
*IPv4 Header of the discarded packet UDP Header*  

Given is the SDU of Layer 3 of another packet shown in Image 2.2. It is known that this is ICMPv4.  

```
0x0000 0b 00 bf 50 00 00 00 00 45 00 00 3c 15 c6 00 00
0x0010 01 11 ea 6d ac 13 f9 bd 81 bb 91 f1 ec 38 82 c4
0x0020 00 28 c6 89
```

*Image 2.2: ICMP message including ICMP header in Network Byte Order*  

f)* Determine the type and code of the ICMP message.  

g) What causes such a message?  

h)* Mark the end of the ICMP header in Image 2.2.  

i) Explain what the payload of such a message generally contains.  

j)* Explain how NAT must differentiate between TCP/UDP and ICMP.  

k) Explain how a NAT-capable router can determine the recipient of this specific ICMP message.  

---

**Task 3**  
Domain Name System (DNS) (16 points)  

*Image 3.1: DNS Namespace*  

Image 3.1 shows an excerpt from the DNS Namespace. The zone grnvs.net. is hosted on the authoritative name server bifrost.grnvs.net. The IP addresses assigned to the FQDNs are provided by the depicted servers.  

a)* Briefly explain what DNS is used for.  

b)* Mark and name all name components of the FQDN playground.grnvs.net. as precisely as possible.  

c)* Complete the given zone file for the zone grnvs.net. The SOA record is already fully provided. Mark FQDNs clearly with appropriate notation.  

Note: Additional blank lines are provided. Strike out invalid entries clearly.  

```
FQDN Record Type Value
grnvs.net. SOA bifrost.grnvs.net. root@grnvs.de. 130m 5m 7d 1m
```

We consider the network topology shown in Image 3.2. Client 1 and Client 2 use the router as an access point to the internet as well as a resolver. The router in turn uses resolver-a.google.com as a resolver for recursive name resolution. Its IP addresses are known to the router. The authoritative name servers do not allow recursion. The authoritative name servers for the respective zones are listed in Table 3.1.  

*Image 3.2: Network topology*  

| Zone | Authoritative Name Server |
|------|---------------------------|
| .    | a.root-servers.net.       |
| com., net. | a.gtld-servers.net.   |
| google.com. | ns1.google.com.      |
| grnvs.net. | bifrost.grnvs.net.   |

d)* Client 1 wants to access playground.grnvs.net. Draw all necessary DNS messages in Image 3.2 using arrows and number them in sequence. The first message is already provided as assistance.  

Note: If necessary, you will find another template of Image 3.2 on page 9. Strike out invalid solutions clearly.  

e) Immediately after, Client 2 wants to resolve the address of www.grnvs.net. Briefly explain how this resolution differs from sub-task 3d).  

f)* Explain the difference between recursive and iterative name resolution.  

g) Which message pairs from sub-task 3d) involve iterative name resolution?  

h)* Justify why DNS messages are generally transmitted over UDP and not over TCP.  

i)* To which IP address does the reverse DNS FQDN 4.4.8.8.in-addr.arpa. belong?  

---

**Task 4**  
IPv4 and Routing (20 points)  

Given is the network topology from Image 4.1. R connects the networks NET1 and NET2 and the internet. R is connected to the internet via GW. The network 188.95.233.96/27 is used for the connection to GW.  

*Image 4.1: Topology*  

a)* Provide the network address, broadcast address, and the number of usable addresses for the address blocks 131.159.40.0/21 and 188.95.233.96/27.  

b) Enter the respective IPv4 address in the connected network in the solution fields in Image 4.1. R should receive the highest usable IPv4 address, and C and GW should receive the lowest usable IPv4 address in their respective subnet.  

c)* Justify whether NET1 and NET2 can be summarized in the routing table of GW.  

d)* Name and explain the procedure by which a router decides through which interface a packet is forwarded.  

e)* Provide the complete routing table for R including all directly connected networks so that NET1 and NET2 can reach the internet and be reachable from there. Summarize as much as possible.  

Note: Additional blank lines are provided. Strike out invalid entries clearly.  

f)* Client C now sends an Echo Request to the server with the IPv4 address 192.0.2.13. The ICMP header and payload are a total of 64 octets long. The header fields for this packet at points P1 and P2 (see Image 4.1) are to be specified. If a field cannot be determined uniquely, make a sensible choice. The numeral system used must be clearly indicated. Addresses are to be specified in the form <device>.<interface>.<address type> (e.g., R.wlan0.MAC).  

g)* Enter the specific value of the Ethernet header in the solution field.  

h)* Enter the specific value of the IP header in the solution field.  

---

**Task 5**  
Short Tasks (19 points)  

Note: The following sub-tasks can be solved independently of each other.  

a)* Mark all collision and broadcast domains in the network shown below.  

b)* A continuous signal of unknown probability distribution is to be quantized in the value range [3,3) such that the quantization error within this range is minimal and the resulting signal levels can be represented with 2 bits. Determine the quantization levels and the maximum quantization error within the given interval.  

c)* Given is a memoryless message source that emits characters from the alphabet = a, b, c, d. Determine the occurrence probabilities of the individual characters so that the source entropy is maximized.  

d)* Briefly explain the principle of Slotted ALOHA.  

e)* Briefly explain the principle of CSMA.  

f)* Briefly explain what additions CSMA/CD has compared to plain CSMA.  

g)* Briefly explain what additions CSMA/CA has compared to plain CSMA.  

h)* What is the essential difference between addresses at Layer 2 and Layer 3 regarding their use?  

i)* What is the general difference between an octet and a byte?  

j)* Justify whether it is possible to operate two IP subnets over the same switch.  

k)* Provide a general formula for converting x GB to y MiB.  

l)* Given is a link with an MTU of 1280B. Calculate the MSS when using IPv6.  

m)* A group of people is sitting together. To decide who may speak, an object is passed around. The person who currently holds the object may either speak or pass the object to a neighbor. What media access method does this correspond to?  

n)* What is the difference between host byte order and network byte order?  

o)* Provide a significant difference between the two classes of routing protocols.  

---

**Additional space for solutions - please clearly mark the affiliation to the respective task and strike out invalid solutions!**