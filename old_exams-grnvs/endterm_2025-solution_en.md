Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

### Personalization Notes:
- Your exam will be personalized by affixing a code sticker during the attendance check.
- This contains only a continuous number, which is also noted on the attendance sheet with SRID to be affixed next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Basics: Computer Networks and Distributed Systems  
**Exam:** IN0010/Endterm  
**Date:** Monday, August 4, 2025  
**Examiner:** Prof. Dr.-Ing. Georg Carle  
**Time:** 08:00–09:30  

### Instructions for Completion:
- This exam comprises 16 pages with a total of 6 tasks and includes an attached cheat sheet. Please check now that you have received a complete set of materials.
- The total score for this exam is 90 points.
- It is prohibited to tear pages from the exam.
- The following aids are allowed:
  - A non-programmable calculator
  - An analog dictionary German ↔ native language without annotations
  - The cheat sheet attached to the exam
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only results where the solution path is recognizable will be graded. Text tasks must be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write with red/green colors or with pencil.
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.

### Task 1  
**Multiple Choice (18 Points)**  
Please mark the correct answers.  
Crosses can be removed by completely filling them in.  
Struck-out answers can be marked again with adjacent markings.  

The following sub-tasks are Multiple Choice/Multiple Answer, meaning there is at least one correct answer for each. Sub-tasks with only one correct answer are graded with 1 point if correct. Sub-tasks with more than one correct answer are graded with 1 point for each correct answer and -1 point for each incorrect mark. Missing crosses have no effect. The minimum score per sub-task is 0 points.  

1. *You are calling a website over HTTPS, and the server wants to authenticate itself via an X.509 certificate. What does your browser check to prevent man-in-the-middle attacks?  
   - The private key used for signing must be contained in the transmitted certificate's chain of trust.  
   - The requested domain must be present in the X.509 certificate.  
   - The requested URL must be present in the X.509 certificate.  
   - It queries the certificate issuer to see if they actually issued the certificate.  

2. *How long is the time between two sampling points when a continuous signal is sampled at a sampling frequency of f = 20 kHz?  
   - 20 ms  
   - 50 kHz  
   - 20 µs  
   - 20 kHz  
   - 50 µs  
   - 50 ms  

3. *Given the above network with NAT router R. PC2 sent an HTTP request to the server. What is the source IP address in the IP packet at position P2?  
   - 192.168.1.2  
   - 192.168.1.254  
   - 127.0.0.1  
   - 185.86.235.241  
   - 131.159.20.19  
   - 192.168.1.1  

4. *Given the above network with NAT router R. The server sends an HTTP reply to PC2 within the already established connection. What is the destination IP address in the IP packet at position P2?  
   - 131.159.20.19  
   - 192.168.1.254  
   - 127.0.0.1  
   - 192.168.1.1  
   - 192.168.1.2  
   - 185.86.235.241  

5. *Given the above network with NAT router R. The server sends an HTTP reply to PC2 within the already established connection. What is the destination port in the segment at position P1?  
   - 1024  
   - 65535  
   - 80  
   - 8005  
   - 443  
   - 4657  
   - 8006  
   - 4486  

6. *Whose MAC address does a wired PC write in an Ethernet frame that is sent to a notebook (NB)? The notebook is connected via an access point (AP).  
   - AP, NB  
   - NB, PC  
   - PC, AP  
   - PC, AP, NB  

7. *On which layer(s) of the ISO-OSI model does Ethernet operate?  
   - 3  
   - 6  
   - 5  
   - 4  
   - 2  
   - 1  
   - 7  

8. *You are transmitting a 1500B large packet over a 1500 km long copper cable with a bitrate of 100 Mbit/s. What is the propagation delay?  
   - 7.66 ms  
   - 0.75 ms  
   - 160 µs  
   - another value  
   - 12.0 ms  
   - 0.16 ms  
   - 7.5 ms  
   - 9.6 ms  

9. *What statement(s) regarding the types of connection partners in autonomous systems meeting at Tier 1 autonomous systems do you have? They have...  
   - Peering partners  
   - Providers  
   - Customers  

10. *Which POSIX Socket API function call marks a socket as passive?  
    - send  
    - select  
    - socket  
    - bind  
    - connect  
    - close  
    - listen  
    - recv  

11. *Which POSIX Socket API function call sets the protocol to be used?  
    - socket  
    - bind  
    - listen  
    - recv  
    - close  
    - connect  
    - send  
    - select  

12. *Which POSIX Socket API function call closes a TCP connection?  
    - listen  
    - socket  
    - select  
    - send  
    - recv  
    - connect  
    - bind  
    - close  

13. *Given the above topology. How many collision domains does the topology have?  
    - 1  
    - 6  
    - 5  
    - 4  
    - 3  
    - 2  
    - 7  

14. *Given the above topology. How many broadcast domains does the topology have?  
    - 1  
    - 2  
    - 7  
    - 3  
    - 4  
    - 5  
    - 6  

15. *The stateless source Q emits symbols from the alphabet X according to the occurrence probabilities of the excerpt given below. What entropy does Q have rounded to two decimal places?  
    - -1.30  
    - 0  
    - another value  
    - 1.96  
    - 1.30  
    - -1.96  

### Task 2  
**Dormitory Network Goes IPv6 (12 Points)**  
Given a network of a dormitory, as shown in Figure 2.1. This has been infinitely converted to IPv6. The dormitory is connected to the Internet via the gateway router R. All caches are initially empty. However, all participants know the IP address of the gateway router. The router/dormitory network has been assigned the global prefix 2001:db8:2::/64, and the network between router R and H is 2001:db8:1234::/64. Privacy extensions are disabled.  

- **PC1**  
  - MAC: 00:53:f1:ab:10:11  
  - IPv6 GU: 2001:db8:1234::2  

- **Router R**  
  - MAC: 00:53:12:23:34:45  
  - IPv6 LL: fe80::1  
  - IPv6 GU: 2001:db8:1234::1  

- **PC2**  
  - MAC: 00:53:14:3b:21:10  
  - IPv6 GU: 2001:db8:2::1  

### Task 2 Subtasks:
1. *Assign appropriate link-local addresses (LL) and global-unique addresses (GU) to PC1 via SLAAC.  
   - PC1 LL: fe80::253:f1ff:feab:1011  
   - PC1 GU: 2001:db8:2:0:253:f1ff:feab:1011  
   (Note: Individual blocks of zeros cannot be shortened by ::.)

2. *Name two further possibilities/procedures for address assignment in IPv6.  
   - Manual  
   - DHCPv6  

3. *What problem regarding data protection arises from the use of SLAAC?  
   - There is a risk of tracking across different networks even with different global prefixes, as the persistent MAC address can be traced back from the IPv6 generated by SLAAC.

4. *The server grnvs.net is reachable under the following IPv6 address:  
   - 2001:0db8:00a0:0000:0000:0001:0000:0011  
   - Provide the address in fully shortened notation.  
   - 2001:db8:a0::1:0:11  

PC1 now wants to establish a connection with the server grnvs.net over the Internet. Since all caches are still empty, PC1 must first find out the MAC address of the eth0 interface of the router.  

5. *What request will be used for this, and what is the corresponding protocol?  
   - Neighbor Solicitation  
   - Neighbor Discovery Protocol (NDP)  

6. *To which IP address will this request be addressed? Name the address type and provide the specific IPv6 address.  
   - Solicited Node Multicast Address  
   - ff02::1:ff00:1  

7. *To which MAC address will this request be addressed? Name the address type and provide the specific MAC address.  
   - Multicast MAC Address  
   - 33:33:ff:00:00:01  

8. *This type of request is also used during the SLAAC mechanism. Briefly explain when it is sent in the process and why.  
   - After generating the LL and GU address, a duplicate address detection is performed to ensure that the address has not already been assigned. If there is no response to the Neighbor Solicitation, the address can be used. If there is a corresponding Neighbor Advertisement, the generated address is already in use, and another must be chosen.  

9. *The gateway router R has set the router H as the default (next) gateway. Create corresponding entries in the routing table of R.  
   - Destination | Next Hop | Iface  
   - fe80::/64 | :: | eth0  
   - 2001:db8:1234::/64 | :: | wan1  
   - 2001:db8:2::/64 | :: | eth0  
   - ::/0 | 2001:db8:1234::2 | wan1  

### Task 3  
**Transmission Control Protocol Transcript (14 Points)**  
Given is the Ethernet frame (including FCS) from Figure 3.1, which is to be analyzed.  

```
0x0000 b4 96 91 43 45 60 52 54 00 00 18 00 08 00 45 00
0x0010 00 3c 2b 9a 00 00 02 01 67 7c bc 5f e8 22 81 bb
0x0020 ff 6d 08 00 07 c6 7a ad 00 07 48 49 4a 4b a4 c4 d
0x0030 4e 4f 50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d
0x0040 5e 5f 60 61 62 63 64 65 66 67 c4 f1 e5 c4
```

**Note:** Justifications are generally required for the following sub-tasks. Ensure that markings can be uniquely assigned to individual sub-tasks. Non-verifiable statements will not be graded.

1. *Mark the sender address in Figure 3.1 on Layer 2. (No justification required)  

2. *Mark the recipient address in Figure 3.1 on Layer 2. (No justification required)  

3. *Mark the Frame Check Sequence (FCS) in Figure 3.1. (No justification required)  

4. *Briefly describe the purpose and effect of the FCS.  
   - The Frame Check Sequence serves for error detection. If errors occur on the transmission path, this can be detected by the FCS. The corresponding packet will then be discarded.  

5. *What type is the L3-PDU?  
   - Type: IPv4  
   - Justification: Ethertype 0x0800  

6. *Provide the sender address on Layer 3 in its usual, possibly shortened notation.  
   - 188.95.232.34  

7. *Provide the TTL or Hop Limit on Layer 3.  
   - Value: 0x02=2  
   - Justification: IPv4 TTL, at offset 0x0016  

Figure 3.2 shows the network topology of the involved network elements. The packet from Figure 3.1 was sent by the PC to the L3 address of S and recorded at point P. It is an ICMP packet. The beginning of the ICMP header is marked in Figure 3.1.  

### Task 3 Subtasks:
1. *What function does this ICMP packet serve?  
   - Function: Echo Request  
   - Justification: Type: 8; Code: 0  

2. *On the transmission path through the network, the packet is discarded due to a timeout, and an ICMP Time Exceeded error message is sent back to the original sender.  

3. *Determine the specific value of the sender and recipient address on Layer 2. (No justification required)  
   - Sender: b4:96:91:43:45:60  
   - Recipient: 52:54:00:00:18:00  

4. *Name the sender address on Layer 3 in the notation Device.Interface.AddressType (for example, R3.eno0.IP) and justify why this node is the sender.  
   - Address: R2.wan3.IP  
   - Justification: The TTL is reduced by router R1 to 1 and by R2 to 0. Subsequently, an ICMP Time Exceeded ICMP error message is sent to the sender of the original packet.  

5. *Fill in the missing entries in the first 12 bytes of the ICMP packet of the response. Fill in the fields in hexadecimal.  
   ```
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
   0x0b 0x00 Checksum  
   0x00000000  
   0x4500003c  
   ```

6. *What procedure was the originally sent ICMP packet likely part of? Name it and briefly describe how this procedure works.  
   - The packet was sent by PC1 with a low TTL. This indicates that this packet is used for traceroute. During traceroute, packets are sent with increasing TTL to determine the path through the network based on the received ICMP error messages.  

### Task 4  
**Resolutions in the Domain Name System (13.5 Points)**  
Your fellow student Dieter is to write a paper on DNS resolvers and their infrastructure in the IITM seminar and is setting up a special nameserver (special.m0000.net). This nameserver is to be authoritative for the zone mirror.m0000.net. To achieve this, Dieter has received access from his supervisors to the authoritative nameserver (ns.m0000.net) for the parent zone m0000.net to make the corresponding entries in the zone file.  

- Delegates requests for the zone mirror.m0000.net to  
  - ns.m0000.net. Nameserver special.m0000.net.  
  - IPv4: 138.246.253.9  
  - IPv4: 138.246.253.25  
  - IPv6: 2001:4ca0:108:42::9  
  - IPv6: 2001:4ca0:108:42::25  

### Task 4 Subtasks:
1. *Ensure that the special nameserver is reachable via both IPv4 and IPv6 under its domain name.  

2. *Ensure that requests for the zone mirror.m00r00.net are delegated to the special nameserver.  

3. *Ensure with only one entry that an info website hosted on the special nameserver is completely reachable under info.m0000.net.  

4. *Dieter's supervisors want emails sent to m0000.net to be directed to the chair's mail server (mail.net.in.tum.de). The preference should be 100.  

5. *Before the change, the SOA resource record had the following value:  
   - ns.m0000.net. hostmaster.net.gin.tum.de. (250730 1800 30 604800 1800).  
   - Update the serial number in the SOA RR.  
   - $TTL 3600  
   - $ORIGIN m0000.net.  
   - m0000.net. IN SOA ns.m0000.net. hostmaster.net.in.tum.de.  
   - (250804 1800 30 604800 1800)  
   - ns A 138.246.253.9  
   - ns AAAA 2001:4ca0:108:42::9  
   - special A 138.246.253.25  
   - special AAAA 2001:4ca0:108:42::25  
   - mirror NS special.m0000.net.  
   - info CNAME special.m0000.net.  
   - m0000.net. MX 100 mail.net.in.tum.de.  

Dieter now wants to know if there is already a reverse DNS entry for the IPv4 address of special.m0000.net.  

6. *What name must be resolved by which type to find this out?  
   - Domain name: 25.253.246.138.in-addr.arpa.  
   - Type: PTR  

### Abbreviations Table  
| Abbreviation | Server | Note |  
|--------------|--------|------|  
| PC           | Client |      |  
| F            | 86.54.11.100 | Forwarding Resolver (Stub Resolver) |  
| R            | 79.127.216.19 | Resolver |  
| ROOT         | a.root-servers.net | authoritative for . |  
| NET          | a.gtld-servers.net | authoritative for net. |  
| AUTH         | ns.m0000.net | authoritative for m0000.net. |  
| SPEC         | special.m0000.net | Special Nameserver |  
| QUERY        | query.mirror.m0000.net | Target Host |  

Dieter is to describe in his seminar paper what DNS messages are exchanged when a client PC sends a DNS query for query.mirror.m0000.net to the Forwarding Resolver F (86.54.11.100). This sends requests recursively to the Resolver R (79.127.216.19), which resolves requests iteratively. Once the special nameserver receives a request regarding the domain query.mirror.m0000.net, it responds with two A Resource Records (RRs), which contain the control address 10.0.77.77 and the IP address of the requesting node.  

### Task 4 Subtasks:
1. *Draw the DNS requests and responses with arrows in the path-time diagram that are sent when sending a recursive DNS request for query.mirror.m00r00.net starting from the client PC. Note the type of Resource Records that are queried or returned on each arrow. Table 4.1 contains information and abbreviations of possibly involved servers. All caches are empty.  

2. *What records with what values are ultimately returned to the PC?  
   - A 79.127.216.19, A 10.0.77.77  
   (With the response values, one can determine what kind of DNS server is queried and which server ultimately resolves the actual request.)  

### Task 5  
**TCP & TLS (12 Points)**  
You visit an HTTPS website via your browser. To establish the connection securely and reliably, several steps occur at different protocol layers. In this task, we consider TCP and TLS.  

1. *While TCP clearly belongs to the transport layer, the assignment for TLS is more difficult. Explain which layer of the ISO/OSI model TLS belongs to and provide at least one TLS function of the respective layer.  
   - Both session and presentation layer  
   - Session layer → Session management and resumption  
   - Presentation layer → Encryption function  

2. *Below are the TCP segments of a TLS 1.3 handshake. Some TLS messages are so large that they must be sent in multiple TCP segments. Fill in the TCP sequence and acknowledgment numbers.  
   ```
   SEQ=1099, SYN, payload=0B  
   SEQ=3824, SYN, ACK= 1100, payload=0B  
   SEQ=1100, ACK= 3825, payload= 0B  
   Client Hello [part 1]  
   SEQ=1100, ACK= 3825, payload= 1448B  
   Client Hello [part 2]  
   SEQ=2548, ACK= 3825, payload= 116B  
   SEQ=3825, ACK= 2664, payload= 0B  
   Server Hello, Change Cipher Spec, Encrypted Extensions  
   SEQ=3825, ACK= 2664, payload= 1448B  
   Certificate, Certificate Verify, Finished  
   SEQ=5273, ACK= 2664, payload= 980B  
   SEQ=2664, ACK= 6253, payload= 0B  
   Change Cipher Spec, Finished  
   SEQ=2664, ACK= 6253, payload= 80B  
   ```

3. *Calculate the time that TCP and TLS need in Task b) for the handshakes, measured from the first TCP segment until application data can be sent from the client.  
   - Assume...  
     - 0.03 ms serialization time per packet,  
     - an RTT of 55 ms,  
     - 2 ms for the marked cryptographic operations (2) on each client and server.  
   - 10·0.03 ms + 2·55 ms + 2·2 ms = 114.30 ms  

4. *In Task b), you see how TCP segments are also sent after the handshake often without payload. Is this necessary? What reason could this have?  
   - It is actually an acknowledgment. It is not necessary since the subsequent segment fulfills the same function. It seems to be an implementation detail that acknowledges segments as early as possible and does not wait for the calculation of the payload.  

5. *Argue how the use of TCP & TLS achieves the goals of 1 reliability, 2 confidentiality, 3 integrity, and 4 authenticity of a connection.  
   - 1 Reliability: TCP ensures that data arrives complete, ordered, and error-free.  
   - 2 Confidentiality: TLS protects the data from eavesdropping through encryption.  
   - 3 Integrity: TLS protects data from manipulation through signatures and checksums.  
   - 4 Authenticity: TLS verifies through X.509 certificates whether the communication partner is who they claim to be.  

### Task 6  
**Message Transmission Backwards (20.5 Points)**  
In the following, we consider a transmission protocol that transmits ASCII-coded text over the physical layer. The signal space assignment used is shown in Figure 6.1, and the used base pulse is given in Figure 6.2.  

```
Q
1
00 01 11 10
I
−1 1 −T/2 T/2
```

### Task 6 Subtasks:
1. *Justify which modulation method was used.  
   - 4-ASK, as there are 4 points in the signal space assignment where the quadrature component is 0.  

2. *In Figure 6.3, a snippet of a fully modulated signal of a message can be seen before it is band-limited and sent. The symbol duration is T = 1 µs.  

3. *Determine the frequency f of the used cosine carrier signal. Provide the result in a meaningful unit.  
   - Four repetitions of a cosine oscillation within the symbol duration:  
   - fM = 4s·T1 = 4 MHz  

4. *Draw the baseband signal before the modulation step in one of the templates from Figure 6.4. Use the second template if you want to mark it. In this case, clearly strike out the non-evaluable template!  

5. *Provide the transmitted bit sequence (no justification required).  
   - 01 01 00 11 01 00 10 11  

6. *The data was encoded before the line coding step. An encoder was used, which prefixes each 7-bit ASCII character with a parity bit.  
   - Determine the code rate of the used encoder.  
   - R = k / n = 7bit / (7bit + 1bit) = 7 / 8  

7. *What effective data rate in Mbit/s can be achieved with this combination of encoder and modulation method?  
   - reff = T · R = 1.75 Mbit/s  

8. *To signal the beginning and end of a message, the ASCII characters STX (Start of Text) and ETX (End of Text) are used as control characters and sent before and after the payload.  
   - The next message to be sent consists of a total of 29 ASCII characters of payload. How long does it take to serialize the message including the control characters?  
   - L = (29 + 2) · 7bit = 217bit  
   - t = L / reff = 217bit / 1.75Mbit/s = 124 µs  
   - Alternatively: Ltotal = (29 + 2) · 8bit = 248bit  
   - ts = Ltotal / reff = 248bit / 2Mbit/s = 124 µs  

9. *Name an alternative mechanism to control characters, how the beginning and end of a message can be signaled in line coding, and describe how this could be implemented.  
   - Mechanism: Code rule violation  
   - Description: In this case, for example, not returning to zero in a pulse (cf. NRZ) or sending a permanent invalid level (amplitude 0 or 1).  

10. *When no message is currently being sent, so that the medium is idle, the control character DEL is transmitted constantly. This results in a periodic signal, which is depicted in Figure 6.5. For this signal, a frequency analysis using the Fourier series should now be performed.  

11. *Provide an analytical definition for the signal s(t) within one period in the interval [0, T].  
   ```
   s(t) = 
   { 
     0.5·cos(4ωt) for 0 ≤ t < T/2  
     0 for T/2 ≤ t < T  
   }  
   ```

12. *Determine the coefficients ak with k > 0 of the spectrum of the idle signal.  
   - Note: ∫(0 to T/2) cos(nωt)·cos(mωt)dt = T/4 for n = m with n, m ∈ ℕ, else 0  
   - ak = (1/T) ∫(0 to T) s(t)cos(kωst)dt  
   - = (1/T) ∫(0 to T/2) 1·cos(4ωt)cos(kωt)dt + (1/T) ∫(T/2 to T) 0·cos(kωt)dt  
   - = (1/T) ∫(0 to T/2) cos(4ωt)cos(kωt)dt  
   - = (1/T)·(T/4) = 0.25 when k = 4, else 0  

13. *Argue how the coefficients bk behave. Will all coefficients bk = 0, or will there be coefficients bk ≠ 0?  
   - Since the signal is not exclusively axis or rotationally symmetric within one period, there will be both ak ≠ 0 and bk ≠ 0 for k > 0.  
   - Alternatively: ak ≠ 0 only for k = 4. However, since the signal has jumps, it has an infinite spectrum, and thus ∃k ∈ ℕ: bk ≠ 0  

### Additional Space for Solutions. Clearly mark the assignment to each sub-task.  
Do not forget to strike out invalid solutions.