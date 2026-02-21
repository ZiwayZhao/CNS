# Chair of Network Architectures and Services
School of Computation, Information and Technology  
Technical University of Munich

## Personalization Notes:
- Your exam will be identified during the attendance check by affixing a code personal exam sticker.
- This contains only a sequential number, which is also noted on the attendance sticker with SRID to be affixed next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

## Basics: Computer Networks and Distributed Systems
Exam: IN0010/Endterm  
Date: Monday, August 4, 2025  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 08:00–09:30  

### Instructions for Processing
- This exam consists of 16 pages with a total of 6 tasks and includes an attached cheat sheet. Please check now that you have received a complete set of materials.
- The total score for this exam is 90 points.
- The removal of pages from the exam is prohibited.
- The following aids are permitted:
  - A non-programmable calculator
  - An analog dictionary German ↔ native language without annotations
  - The cheat sheet attached to the exam
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write with red/green colors or with pencil.
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.

## Task 1
Multiple Choice (18 points)

Please mark the correct answers.

The following sub-tasks are Multiple Choice/Multiple Answer, meaning at least one answer option is correct. Sub-tasks with only one correct answer are scored with 1 point if correct. Sub-tasks with more than one correct answer are scored with 1 point for each correct answer and -1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.

a) *You are accessing a website via HTTPS, and the server wants to authenticate itself through an X.509 certificate. What does your browser ensure to prevent man-in-the-middle attacks?
- The private key used for signing must be contained in the transmitted certificate’s chain of trust to a pre-installed root certificate.
- It performs a TLS 1.2 handshake to confuse the attacker.
- The requested domain must be present in the X.509 certificate.
- It queries the certificate issuer to check if this actually issued the certificate.

b) *How long is the time between two sampling points when a continuous signal is sampled with a sampling frequency of f = 20 kHz?
- 20 ms
- 50 kHz
- 20 µs
- 20 kHz
- 50 µs
- 50 ms

NAT Table of Router R
| Local IP Addr   | Local Port | Global Port   |
|------------------|------------|----------------|
| 192.168.1.1      | 4486       | 8005           |
| PC1              | 192.168.1.2| 4657           | 8006           |
| 192.168.1.1      |              |                |

c) *Given the network above with NAT router R. PC2 sent an HTTP request to the server. What is the source IP address in the IP packet at position P2?
- 192.168.1.2
- 192.168.1.254
- 127.0.0.1
- 185.86.235.241
- 131.159.20.19
- 192.168.1.1

d) *Given the network above with NAT router R. The server sends an HTTP reply to PC2 within the already established connection. What is the destination IP address in the IP packet at position P2?
- 131.159.20.19
- 192.168.1.254
- 127.0.0.1
- 192.168.1.1
- 192.168.1.2
- 185.86.235.241

e) *Given the network above with NAT router R. The server sends an HTTP reply to PC2 within the already established connection. What is the destination port in the segment at position P1?
- 1024
- 65535
- 80
- 8005
- 443
- 4657
- 8006
- 4486

f) *Which MAC address does a wired PC write in an Ethernet frame that is sent to a notebook (NB)? The notebook is connected via an access point (AP).
- AP, NB
- NB, PC
- PC, AP
- PC, AP, NB

g) *On which layer(s) of the ISO-OSI model does Ethernet operate?
- 3
- 6
- 5
- 4
- 2
- 1
- 7

h) *You are transmitting a 1500B packet over a 1500 km long copper cable with a bitrate of 100 Mbit/s. What is the propagation delay?
- 7.66 ms
- 0.75 ms
- 160 µs
- other value
- 12.0 ms
- 0.16 ms
- 7.5 ms
- 9.6 ms

i) *Which statement(s) regarding the types of connection partners from autonomous systems apply to Tier 1 autonomous systems? They have...
- Peering partners
- Providers
- Customers

j) *Which POSIX socket API function call marks a socket as passive?
- send
- select
- socket
- bind
- connect
- close
- listen
- recv

k) *Which POSIX socket API function call specifies the protocol to be used?
- socket
- bind
- listen
- recv
- close
- connect
- send
- select

l) *Which POSIX socket API function call closes a TCP connection?
- listen
- socket
- select
- send
- recv
- connect
- bind
- close

m) *Given the topology above. How many collision domains does the topology possess?
- 1
- 6
- 5
- 4
- 3
- 2
- 7

n) *Given the topology above. How many broadcast domains does the topology possess?
- 1
- 2
- 7
- 3
- 4
- 5
- 6

o) *The memoryless source Q emits symbols from the alphabet X according to the occurrence probabilities of the excerpt given below. What entropy does Q have rounded to two decimal places?
- X
- Q
- AABABACADE... 
- X ∈ {A, B, C, D, E}
- -1.30
- 0
- other
- 1.96
- 1.30
- -1.96

## Task 2
Dormitory Network Goes IPv6 (12 points)

Given is a network of a dormitory, as shown in Figure 2.1. This has been infinitely switched to IPv6. The dormitory is connected to the Internet via the gateway router R. All caches are initially empty. However, all participants know the IP address of the gateway router. The router/dormitory network has been assigned the global prefix 2001:db8:2::/64, and the network between router R and H has the network 2001:db8:1234::/64. Privacy extensions are disabled.

```
PC1
Server
eth0
grnvs.net
MAC: 00:53:f1:ab:10:11
MAC: 00:53:15:10:11:12
IPv6 GU: 2001:db8:1234::2

R H
eth0 wan1 wan0
Internet
MAC: 00:53:12:23:34:45
MAC: 00:53:15:10:11:12
IPv6 LL: fe80::1
IPv6 GU: 2001:db8:1234::1

PC2
IPv6 GU: 2001:db8:2::1
eth1
MAC: 00:53:14:3b:21:10
```

**Figure 2.1: Network**

a) *Assign appropriate Link-Local addresses (LL) and Global-Unique addresses (GU) to PC1 via SLAAC.
- PC1 LL:
- PC1 GU:

b) *Name two other possibilities/procedures for address assignment in IPv6.

c) *What problem regarding data protection arises from the use of SLAAC?

d) *The server grnvs.net is reachable under the following IPv6 address: 2001:0db8:00a0:0000:0000:0001:0000:0011. Provide the address in fully shortened notation.

PC1 now wants to establish a connection with the server grnvs.net over the Internet. Since all caches are still empty, PC1 must first find out the MAC address of the eth0 interface of the router.

e) *What request will be used for this, and what is the corresponding protocol?

f) *To which IP address is this request addressed? Name the address type and provide the specific IPv6 address.

g) *To which MAC address is this request addressed? Name the address type and provide the specific MAC address.

h) *This type of request is also used during the SLAAC mechanism. Briefly explain when in the process this is sent and why.

i) *The gateway router R has set the router H as the default (next) gateway. Create corresponding entries in the routing table of R.

| Destination | Next Hop | Iface |
|--------------|----------|-------|
| Routing Table of R |

## Task 3
Transmission Control Protocol Record (14 points)

Given is the Ethernet frame (including FCS) from Figure 3.1, which is to be analyzed.

```
0x0000 b4 96 91 43 45 60 52 54 00 00 18 00 08 00 45 00
0x0010 00 3c 2b 9a 00 00 02 01 67 7c bc 5f e8 22 81 bb
ICMP Header
0x0020 ff 6d 08 00 07 c6 7a ad 00 07 48 49 4a 4b 4c 4d
0x0030 4e 4f 50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d
0x0040 5e 5f 60 61 62 63 64 65 66 67 c4 f1 e5 c4
```

**Figure 3.1: Ethernet Frame (including FCS)**

Note that justifications are generally required for the following sub-tasks as well. Ensure that markings can be uniquely assigned to individual sub-tasks. Non-verifiable statements will not be graded.

a) *Mark the sender address in Figure 3.1 on Layer 2. (without justification)

b) *Mark the recipient address in Figure 3.1 on Layer 2. (without justification)

c) *Mark the Frame Check Sequence (FCS) in Figure 3.1. (without justification)

d) *Briefly describe the purpose and effect of the FCS.

e) *What type is the L3-PDU?

Type: Justification:

f) *Provide the sender address on Layer 3 in its usual, possibly shortened notation.

g) *Provide the TTL or the Hop Limit on Layer 3.

Value: Justification:

**Figure 3.2 shows the network topology of the involved network elements. The packet from Figure 3.1 was sent from the PC to the L3 address of S and recorded at point P. It is an ICMP packet. The beginning of the ICMP header is marked in Figure 3.1.**

```
PC R1 R2 S
eth0 eth1 wan2 wan3 eth4 eth5
P Q T
```

**Figure 3.2: Network Topology**

h) *What function does this ICMP packet serve?

Function: Justification:

On the transmission path through the network, the packet is discarded due to a timeout, and an ICMP Time Exceeded error message is sent back to the original sender. 

All following sub-tasks refer to this ICMP packet. This will also be considered at point P.

i) *Determine the specific value of the sender and recipient address on Layer 2. (without justification)

Sender: Recipient:

j) *Name the sender address on Layer 3 in the notation Device.Interface.Address Type (for example, R3.eno0.IP) and justify why this node is the sender.

Address: Justification:

k) *Complete the missing entries in the first 12 bytes of the ICMP packet of the response. Fill in the fields in hexadecimal.

```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
2
Checksum
0x00000000
```

l) *What procedure was the originally sent ICMP packet likely part of? Name this and briefly describe how this procedure works.

## Task 4
Resolutions in the Domain Name System (13.5 points)

Your fellow student Dieter is to write a paper on DNS resolvers and their infrastructure for the IITM seminar and is setting up a special nameserver (special.m0000.net). This nameserver is to be authoritative for the zone mirror.m0000.net. To realize this, Dieter has received access from his supervisors to the authoritative nameserver (ns.m0000.net) for the parent zone m0000.net to make the corresponding entries in the zone file.

Delegates requests for the zone mirror.m0000.net to ns.m0000.net.  
Nameserver special.m0000.net.  
IPv4: 138.246.253.9  
IPv4: 138.246.253.25  
IPv6: 2001:4ca0:108:42::9  
IPv6: 2001:4ca0:108:42::25  

**Figure 4.1: Information regarding delegation and IP addresses**

Help Dieter complete the zone file of ns.m0000.net. The domain names and IP addresses of the nameservers are given in Figure 4.1. In the following sub-tasks, provide the entries in the zone file such that the task requirements are met.

a) *Ensure that the special nameserver is reachable via both IPv4 and IPv6 under its domain name.

b) *Ensure that requests for the zone mirror.m0000.net are delegated to the special nameserver.

c) *Ensure with only one entry that an info website hosted on the special nameserver is fully reachable under info.m0000.net.

d) *Dieter's supervisors want emails sent to m0000.net to be directed to the chair's mail server (mail.net.in.tum.de). The preference should be 100.

e) *Before the change, the SOA resource record had the following value:  
ns.m0000.net. hostmaster.net.in.tum.de. (250730 1800 30 604800 1800).  
Update the serial number in the SOA RR.

```
$TTL 3600
$ORIGIN m0000.net.
m0000.net. IN SOA ns.m0000.net. hostmaster.net.in.tum.de. ( 1800 30 604800 1800)
ns A 138.246.253.9
ns AAAA 2001:4ca0:108:42::9
```

Dieter wants to know if there is already a reverse DNS entry for the IPv4 address of special.m0000.net.

f) *What name must be resolved and of what type to find this out?

Domain name:  
Type:

| Abbreviation | Server | Note |
|--------------|--------|------|
| PC           | Client |
| F            | 86.54.11.100 | Forwarding Resolver (Stub Resolver) |
| R            | 79.127.216.19 | Resolver |
| ROOT         | a.root-servers.net | authoritative for . |
| NET          | a.gtld-servers.net | authoritative for net. |
| AUTH         | ns.m0000.net | authoritative for m0000.net. |
| SPEC         | special.m0000.net | Special Nameserver |
| QUERY        | query.mirror.m0000.net | Target Host |

**Table 4.1: Abbreviations and Information about potentially involved servers**

Dieter is to describe in his seminar paper which DNS messages are exchanged when a client PC sends a DNS query for query.mirror.m0000.net to the forwarding resolver F (86.54.11.100). This sends requests recursively to the resolver R (79.127.216.19), which resolves requests iteratively. Once the special nameserver finally receives a request regarding the domain query.mirror.m0000.net, it responds with two A resource records (RRs) containing the control address 10.0.77.77 and the IP address of the requesting node.

g) Draw the DNS requests and responses with arrows in the time-path diagram that are sent when sending a recursive DNS request for query.mirror.m0000.net starting from the client PC. Note the type of resource records that are queried or returned on each arrow. Table 4.1 contains information and abbreviations of potentially involved servers. All caches are empty.

```
PC F R ROOT NET AUTH SPEC QUERY
A
```

h) *What records with what values are ultimately returned to the PC? 

## Task 5
TCP & TLS (12 points)

You visit an HTTPS website via your browser. To establish the connection securely and reliably, several steps occur at different protocol layers. In this task, we consider TCP and TLS.

a) *While TCP clearly belongs to the transport layer, the assignment for TLS is more difficult. Explain which layer of the ISO/OSI model TLS belongs to and provide at least one TLS function of the respective layer.

b) *Below are the TCP segments of a TLS 1.3 handshake. Some TLS messages are so large that they must be sent in multiple TCP segments. Fill in the TCP sequence and acknowledgment numbers.

```
SEQ=1099, SYN, payload=0B
SEQ=3824, SYN, ACK= , payload=0B
SEQ = , ACK = , payload = 0B
Client Hello [part 1]
SEQ = , ACK = , payload = 1448B
Client Hello [part 2]
SEQ = , ACK = , payload = 116B
SEQ = , ACK = , payload = 0B
Server Hello, Change Cipher Spec, Encrypted Extensions
SEQ = , ACK = , payload = 1448B
Certificate, Certificate Verify, Finished
SEQ = , ACK = , payload = 980B
SEQ = , ACK = , payload = 0B
Change Cipher Spec, Finished
SEQ = , ACK = , payload = 80B
```

c) *Calculate the time that TCP and TLS need in task b) for the handshakes, measured from the first TCP segment until application data can be sent from the client. Assume:
- 0.03 ms serialization time per packet,
- an RTT of 55 ms,
- 2 ms for the marked cryptographic operations (2) on each client and server.

d) *In task b), you see that TCP segments are often sent without payload even after the handshake. Is this necessary? What reason could this have?

e) *Argue how the use of TCP & TLS achieves the goals of 1 reliability, 2 confidentiality, 3 integrity, and 4 authenticity of a connection.

1 Reliability:  
2 Confidentiality:  
3 Integrity:  
4 Authenticity:  

## Task 6
Message Transmission Backward (20.5 points)

In the following, we consider a transmission protocol that transmits ASCII coded text over the physical layer. The signal space assignment used is given in Figure 6.1, and the basic pulse used is shown in Figure 6.2.

```
Q
1
1
00 01 11 10
I
-T/2 T/2
-1 1
-1
-1
```

**Figure 6.1: Signal Space Assignment**  
**Figure 6.2: Basic Pulse**

a) *Justify which modulation method was used.

In Figure 6.3, a snippet of a fully modulated signal of a message can be seen before it is band-limited and sent. The symbol duration is T = 1 µs.

```
t/T
-1 1 2 3 4 5 6 7 8
```

**Figure 6.3: Modulated Signal**

b) *Determine the frequency f of the cosine carrier signal used. Provide the result in a meaningful unit.

c) *Draw the baseband signal before the modulation step in one of the templates from Figure 6.4. Use the second template if you need to draw. In this case, clearly cross out the non-assessable template!

d) *Provide the transmitted bit sequence (no justification required).

The data was channel-coded before the line coding step. An encoder was used that adds a parity bit in front of each 7-bit ASCII character.

e) *Determine the code rate of the encoder used.

f) *What effective data rate in Mbit/s can be achieved with this combination of encoder and modulation method?

To signal the beginning and end of a message, the ASCII characters STX (Start of Text) and ETX (End of Text) are used as control characters and sent before and after the payload data.

g) *The next message to be sent consists of a total of 29 ASCII characters of payload data. How long does it take to serialize the message including the control characters?

h) *Name an alternative mechanism to control characters, how the beginning and end of a message can be signaled in line coding and describe how this could be implemented here.

Mechanism:  
Description:  

When no message is currently being sent, so that the medium is idle, the control character DEL is transmitted constantly. This results in a periodic signal, which is depicted in Figure 6.5. For this signal, a frequency analysis should now be performed using the Fourier series.

```
s(t)
1
t/T
-1 1 2 3 4 5 6 7 8
```

**Figure 6.5: Modulated, Periodic Signal s(t) while the medium is idle**

i) *Provide an analytical definition for the signal s(t) within one period in the interval [0, T].

```
s(t) = {
    ωt for ≤ t < 
    for ≤ t < 
}
```

j) *Determine the coefficients ak with k > 0 of the spectrum of the idle signal.  
**Note:** T/2 cos(nωt)·cos(mωt) dt = T/4 for n = m with n, m ∈ +, otherwise 0.

k) *Justify how the coefficients bk behave. Will all coefficients bk = 0, or will there be coefficients bk ≠ 0?

---

**Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.**