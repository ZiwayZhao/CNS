Faculty of Computer Science  
Technical University of Munich  
Exam supervision  
by  
Only to be filled out by the supervisor  
Matriculation number  
Fundamentals of Computer Networks and Distributed Systems  
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
Only to be filled out by the supervisor  
Leave the lecture hall from to  
from to  
Submitted early at  
Other  
Matriculation number:  
Midterm  
Fundamentals of Computer Networks and Distributed Systems  
Prof. Dr. Uwe Baumgarten  
Department of Operating Systems  
Faculty of Computer Science  
Technical University of Munich  
Friday, 12.06.2015  
18:00–18:45  
• This exam consists of  
  – 9 pages with a total of 3 tasks as well as  
  – a double-sided formula collection.  
Please check now that you have received a complete document.  
• Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
• Only such results will be graded where a solution path is recognizable. Text tasks must be justified unless otherwise stated in the respective sub-task.  
• Please write with red/green colors or with pencil.  
• The total number of points is 20. These will be weighted with a factor of 0.5 when counted. In the case of quarter points, round up to the next multiple of 0.5.  
• The following aids are permitted:  
  – a non-programmable calculator  
  – a dictionary German ↔ native language without annotations  
• Please turn off your mobile phones completely and pack them as well as all other electronic devices and other documents into your bags and close them.  
– Page 1/9 –  
Matriculation number:  
Problem 1  
IPv6 and Routing (9 points)  
The network topology is given in Figure 1.1. The router R is connected to the Internet via GW and supplies the networks NET1 and NET2. NET2 is used for WLAN clients.  
```
9
eth0: 00:00:5e:00:55:11
C S 2001:db8:1:d::1:0/64
NET1
2001:db8:1:d::/64 eth0: 12:e4:4e:71:13:37
fe80::10e4:4eff:fe71:1337/64
P1
GW
eth0: 00:00:5e:00:55:00
2001:db8:1:d::1 R Internet
P2
ppp0: 00:00:5e:00:55:12
NET2 fe80::200:5eff:fe00:5512/64
2001:db8:1:e::/64
wlan0: 00:00:5e:00:55:13
2001:db8:1:e::1:0/64
```
Figure 1.1: Topology  
a) *Justify why NET1 and NET2 cannot be aggregated on GW.  
1  
b) *Explain how a router decides through which interface a packet is forwarded.  
1  
c) *Provide the complete routing table for R so that NET1 and NET2 can reach the Internet and can be reached from there. Aggregate as much as possible.  
Note: Additional blank lines are provided. Strike out invalid entries clearly.  
2  
```
Destination Next Hop Interface
```
– Page 2/9 –  
```
PPP212::: CR..eptphp00..MMAACC:: 0102::0e04::543e::0701::5153::1317 GRW..eetthh00..MMAACC::0000::0000::5533::0000::5555::0102 00xx8866dddd
PPP112::: CR..eptphp00..MMAACC:: 0102::0e04::543e::0701::5153::1317 GRW..eetthh00..MMAACC::0000::0000::5533::0000::5555::0102 00xx8866dddd
PPP212:::
00xx66 00xx0000 00xx0000000000
00xx00004400 00xx33aa 00xx430f
CC..eetthh00..IIPPvv66:: 22000011::ddbb88::11::dd::::11
22000011::ddbb88::::11
PPP112:::
00xx66 00xx0000 00xx0000000000
00xx00004400 00xx33aa 00xx430f
CC..eetthh00..IIPPvv66:: 22000011::ddbb88::11::dd::::11
22000011::ddbb88::::11
```
Matriculation number:  
d) *How does R receive the IP address fe80::200:5eff:fe00:5512 on the interface ppp0?  
1  
e) *Argue where router R forwards a packet with the destination address fe80::1:2ff:fe03:405.  
1  
Client C sends an ICMPv6 Echo Request to the IPv6 address 2001:db8::1. The ICMPv6 header and payload are a total of 64 octets long.  
f) *Provide the specific values of the header fields for the Ethernet header of the sent Echo Requests at points P1 and P2 (see Figure 1.1). The number system used must be clearly indicated. Addresses can be referenced in the format <device>.<interface>.<address type> (e.g., R.wlan0.MAC). If a field cannot be uniquely determined, make a sensible choice.  
Note: An additional form can be found on page 8 if needed.  
1  
```
P1: Payload FCS  
P2: Payload FCS
```
g) *Provide the specific values of the header fields for the IPv6 header of the sent Echo Requests at points P1 and P2 (see Figure 1.1). Also note the hint in sub-task 1f).  
```
P1: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
2  
0B  
4B  
8B  
≈ ≈  
24B  
≈ ≈  
ICMPv6 Header and Payload  
P2: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
0B  
4B  
8B  
≈ ≈  
24B  
≈ ≈  
ICMPv6 Header and Payload
```
– Page 3/9 –  
Matriculation number:  
Task 2  
Google Loon – Internet via Helium Balloons (7 points)  
Providing widespread internet access to sparsely populated areas is known to be a major challenge. One of the more innovative ideas for an economical solution comes from Google and is called Project Loon: Helium-filled balloons float at an altitude of about 30 km and provide coverage of an area of about 1200 km² via radio (see Figure 2.1). The connection of the balloons to the Internet is achieved via directional radio to a ground station.  
Figure 2.1: Google Loon  
In the following, we consider one balloon and the two users A and B. For simplification, we assume that the media access method CSMA is used without further mechanisms for collision detection or avoidance. The slot time is t = 20 µs. The downlink (from the balloon to the user) has a data rate of r_down = 60 Mbit/s. The uplink (from the user to the balloon) is only r_up = 16 Mbit/s. Both transmission directions use the same frequency range. Furthermore, the distances between the balloon and all involved users are equal, i.e., d = 30 km for all connections.  
1. At time t = 0 µs, the balloon starts transmitting a 1500-byte long message N1 to a user in the target area.  
2. At time t = 120 µs, user A has a 200-byte long message N2 to send.  
3. At time t = 200 µs, user B also has a 200-byte long message N3 to send.  
a) *Determine the serialization times of the individual messages.  
1  
b) *Determine the propagation delays.  
1  
1 Image: https://www.google.com/loon/how  
– Page 4/9 –  
Matriculation number:  
c) Draw a detailed time-distance diagram of all events from t = 0 µs. Clearly mark serialization times and propagation delays as well as any collisions and sending pauses.  
Scale: 10 µs = 1 mm. Note: An additional form can be found on page 8 if needed.  
3  
```
A Balloon B  
t  
0  
t  
```
d) Explain the problems that occurred in sub-task 2c).  
1  
e) Briefly explain whether CSMA/CA avoids the problems that occurred in sub-task 2c).  
1  
– Page 5/9 –  
Matriculation number:  
Task 3  
CRC (4 points)  
In this task, the two-octet long message 01101010 10010111 is to be secured using the CRC method presented in the lecture. The reduction polynomial is r(x) = x^4 + x + 1.  
a) *Determine the secured message s(x).  
2  
– Page 6/9 –  
Matriculation number:  
b) During transmission, the error pattern 00000000001001100000 occurs. Show or justify whether the error is detected.  
1  
c) What errors can be corrected using CRC?  
1  
– Page 7/9 –  
```
PPP1212:::: CR..eptpPPPPhp001212..::::MMAACC:: 0102::0e04::543e::0701::5153::1317 GRW..eetthh00..MMAACC::0000::0000::5533::0000::5555::0102 00xx8866dddd  
00xx66 00xx0000 00xx0000000000  
00xx00004400 00xx33aa 00xx430f  
CC..eetthh00..IIPPvv66:: 22000011::ddbb88::11::dd::::11  
22000011::ddbb88::::11  
```
Matriculation number:  
Additional forms for sub-tasks 1f) and 1g). Please ensure to provide a correspondence to the observation points and clearly strike out invalid solutions.  
```
Payload FCS  
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31  
0B  
4B  
8B  
≈ ≈  
24B  
≈ ≈  
ICMPv6 Header and Payload  
```
Additional form for sub-task 2c). Please clearly strike out invalid solutions.  
```
A Balloon B  
t  
0  
t  
```
– Page 8/9 –  
Matriculation number:  
Additional space for solutions – please clearly mark the association with the respective task and strike out invalid solutions!  
– Page 9/9 –