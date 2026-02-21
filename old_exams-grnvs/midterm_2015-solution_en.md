Faculty of Computer Science  
Technical University of Munich  
Exam supervision by  
Only by  
Matriculation number  
Basics of Computer Networks and Distributed Systems  
Module: IN0010 Date: 12.06.2015  
Examiner: Prof. Dr. Uwe Baumgarten Exam: Midterm  

First correction  
0 1 2 3 4 5 6 7 8 9  
A1  
0 1 2 3 4 5 6 7  
A2  
0 1 2 3 4  
A3  

Second correction  
0 1 2 3 4 5 6 7 8 9  
A1  
0 1 2 3 4 5 6 7  
A2  
0 1 2 3 4  
A3  

To be filled out only by the supervisor  
Lecture hall left from to  
from to  
Submitted early at  
Miscellaneous  

1  
0  
/  
6  
0  
/  
1  
0  
0  
2  
[  
e  
2  
X  
e  
T  
a  
L  
g  
a  
l  
h  
c  
s  
r  
o  
v  
s  
g  
n  
u  
s  
L  
Matriculation number:  
Midterm  
Basics of Computer Networks and Distributed Systems  
Prof. Dr. Uwe Baumgarten  
Department of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  
Friday, 12.06.2015  
18:00–18:45  

- This exam consists of  
  - 9 pages with a total of 3 tasks as well as  
  - a double-sided printed formula collection.  
- Please check now that you have received a complete set of information.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be graded where a solution path is recognizable. Text tasks must be justified unless explicitly stated otherwise in the respective sub-task.  
- Please write only with red/green colors or with pencil.  
- The total number of points is 20. These will be weighted with a factor of 0.5. In the case of quarter points, round up to the next multiple of 0.5.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - a dictionary German ↔ native language without annotations  
- Please turn off your mobile phones completely and pack them as well as all other electronic devices and other documents into your bags and close them.  

**Page 1/9**  
Matriculation number:  

**Problem 1**  
IPv6 and Routing (9 points)  
The network topology is given in Figure 1.1. The router R is connected to the Internet via GW and supplies the networks NET1 and NET2. NET2 is used for WLAN clients.  

```
eth0: 00:00:5e:00:55:11  
C S 2001:db8:1:d::1:0/64  
NET1  
2001:db8:1:d::/64 eth0: 12:e4:4e:71:13:37  
fe80::10e4:4eff:fe71:1337/64  
GW  
eth0: 00:00:5e:00:55:00  
2001:db8:1:d::1 R Internet  
ppp0: 00:00:5e:00:55:12  
NET2 fe80::200:5eff:fe00:5512/64  
2001:db8:1:e::/64  
wlan0: 00:00:5e:00:55:13  
2001:db8:1:e::1:0/64  
```  

**Figure 1.1: Topology**  

a) Justify why NET1 and NET2 cannot be aggregated at GW.  
NET1 and NET2 are not in the same /63 prefix. For bits 61 to 64: d = 1101, e = 1110.  

b) Explain how a router decides through which interface a packet is forwarded.  
Longest Prefix Matching. The routing table is searched with descending prefix length. If the destination IP falls within the prefix, this entry (with interface) is chosen.  

c) Provide the complete routing table for R so that NET1 and NET2 can reach the Internet and can be reached from there. Aggregate as much as possible.  
Note: Additional blank lines are provided. Cross out invalid entries clearly.  

```
Destination          Next Hop               Interface  
2001:db8:1:d::/64    ::                      eth0  
2001:db8:1:e::/64    ::                      wlan0  
fe80::/64            ::                      ppp0  
::/0                 fe80::10e4:4eff:fe71:1337 ppp0  
```  

**Page 2/9**  
PPP122::: GW.eth0.MAC: 12:e4:4e:71:13:37 R.ppp0.MAC: 00:00:55:00:55:12 0x86dd  
PPP121::: R.eth0.MAC: 00:00:55:00:55:11 C.eth0.MAC: 00:00:55:00:55:00 0x86dd  
PPP122:::  
0x6 0x00 0x00000  
0x0040 0x3a 0x3f  
C.eth0.IPv6: 2001:db8:1:d::1  
2001:db8::1  
PPP121:::  
0x6 0x00 0x00000  
0x0040 0x3a 0x40  
C.eth0.IPv6: 2001:db8:1:d::1  
2001:db8::1  

Matriculation number:  

d) How does R receive the IP address fe80::200:5eff:fe00:5512 at interface ppp0?  
This is a link-local address. The router generates this via Stateless Address Autoconfiguration (SLAAC) from the MAC address of the interface.  

e) Argue where router R forwards a packet with the destination address fe80::1:2ff:fe03:405.  
The router does not forward the packet because it is a link-local address.  

Client C sends an ICMPv6 Echo Request to the IPv6 address 2001:db8::1. The ICMPv6 header and payload are a total of 64 octets long.  

f) Provide the specific values of the header fields for the Ethernet header of the sent Echo Requests at points P1 and P2 (see Figure 1.1). The number system used must be clearly indicated. Addresses can be referenced in the format <Device>.<Interface>.<AddressType> (e.g., R.wlan0.MAC). If a field cannot be uniquely determined, make a reasonable choice.  
Note: On page 8, an additional form can be found if needed.  

```
P1: R.eth0.MAC: 00:00:55:00:55:11 C.eth0.MAC: 00:00:55:00:55:00 0x86dd Payload FCS  
P2: GW.eth0.MAC: 12:e4:4e:71:13:37 R.ppp0.MAC: 00:00:55:00:55:12 0x86dd Payload FCS  
```  

g) Provide the specific values of the header fields for the IPv6 headers of the sent Echo Requests at points P1 and P2 (see Figure 1.1). Also note the hint in sub-task 1f).  

```
P1: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
2  
0B 0x6 0x00 0x00000  
4B 0x0040 0x3a 0x40  
C.eth0.IPv6: 2001:db8:1:d::1  
≈ ≈  
24B 2001:db8::1  
≈ ≈  
ICMPv6 Header and Payload  
P2: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
0B 0x6 0x00 0x00000  
4B 0x0040 0x3a 0x3f  
C.eth0.IPv6: 2001:db8:1:d::1  
≈ ≈  
24B 2001:db8::1  
≈ ≈  
ICMPv6 Header and Payload  
```  

**Page 3/9**  
Matriculation number:  

**Task 2**  
Google Loon – Internet via Helium Balloons (7 points)  
The widespread provision of thinly populated areas with Internet poses a significant challenge. One of the more innovative ideas for an economical solution comes from Google and is called Project Loon: Helium-filled balloons float at an altitude of around 30 km and provide coverage of an area of about 1200 km² via radio (see Figure 2.1). The connection of the balloons to the Internet is done via directional radio to a ground station.  

**Figure 2.1: Google Loon**  

In the following, we consider a balloon and the two users A and B. For simplification, we assume that CSMA is used as the media access method without further mechanisms for collision detection or avoidance. The slot time is t = 20 µs. The downlink (from the balloon to the user) has a data rate of r_down = 60 Mbit/s. The uplink (from the user to the balloon) is only r_up = 16 Mbit/s. Both transmission directions use the same frequency range. Furthermore, the distances between the balloon and all participating users are equal, i.e., d = 30 km for all connections.  

1. At time t = 0 µs, the balloon begins transmitting a 1500-byte long message N1 to a user in the target area.  
2. At time t1 = 120 µs, user A has a 200-byte long message N2 to send.  
3. At time t = 200 µs, user B also has a 200-byte long message N3 to send.  

a) Determine the serialization times of the individual messages.  
```
t_s,1 = r_down * 1500 * 8 bits / 60 * 10^6 bits/s = 200 µs  
t_s,2 = t_s,3 = 200 * 8 bits / 16 * 10^6 bits/s = 100 µs  
```  

b) Determine the propagation delays.  
```
t_p = d / ν = 30 * 10^3 m / 3 * 10^8 m/s = 100 µs  
```  

c) Draw a detailed time-distance diagram of all events from t = 0 µs. Clearly mark serialization times and propagation delays as well as any collisions and send pauses. Scale: 10 µs = 1 mm. Note: If needed, you will find an additional form on page 8.  

```
A Balloon B  
t  
0  
t  
1  
t  
s,1  
t  
slot  
t  
s,2  
t  
s,3  
```  

d) Explain the problems that occurred in sub-task 2c).  
1. A collision occurs at the balloon, causing both messages to be lost.  
2. Neither A nor B knows that they are out of range.  
3. Because sending stations begin to send deterministically in the next time slot after the medium is recognized as free, a collision always occurs in such cases.  

e) Briefly explain whether CSMA/CA avoids the problems occurring in sub-task 2c).  
No, since slot < t_p and thus "send in the next slot when the medium is free" is not sufficient to avoid collisions. For this reason, the randomization using the contention window also does not work as hoped, which CA prescribes.  

**Page 5/9**  
Matriculation number:  

**Task 3**  
CRC (4 points)  
In this task, the two-octet long message 01101010 10010111 is to be secured using the CRC method presented in the lecture. The reduction polynomial is r(x) = x^4 + x + 1.  

a) Determine the secured message s(x).  
```
0 1 1 0 1 0 1 0 1 0 0 1 0 1 1 1 0 0 0 0 : 1 0 0 1 1  
1 0 0 1 1  
0 1 0 0 1 1  
1 0 0 1 1  
0 0 0 0 0 0 1 0 0 1 0  
1 0 0 1 1  
0 0 0 0 1 1 1 1 0  
1 0 0 1 1  
0 1 1 0 1 0  
1 0 0 1 1  
0 1 0 0 1 0  
1 0 0 1 1  
0 0 0 0 1 0  
```  
```
⇒ s(x) = 01101010 10010111 0010  
```  

b) During transmission, the error pattern 00000000001001100000 occurs. Show or justify whether the error is detected.  
The error e(x) = r(x)x^6 is a multiple of the reduction polynomial.  

c) What errors can be corrected using CRC?  
None. CRC is an error-detecting code.  

**Page 7/9**  
Additional forms for sub-tasks 1f) and 1g). Please ensure to provide an assignment to the observation points and clearly cross out invalid solutions.  

Payload FCS  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
0B  
4B  
8B  
≈ ≈  
24B  
≈ ≈  
ICMPv6 Header and Payload  

Additional form for sub-task 2c). Please clearly cross out invalid solutions.  

A Balloon B  
t  
0  
s  
g  
n  
u  
s  
L  

**Page 8/9**  
Matriculation number:  

Additional space for solutions – please clearly mark the affiliation to the respective task and cross out invalid solutions!  

**Page 9/9**