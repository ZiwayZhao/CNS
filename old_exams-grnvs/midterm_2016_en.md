Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized by affixing a code during the attendance check.  
- This contains only a sequential number, which is also noted on the attendance lists next to the signature field.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
(GRNVS)  
Module: IN0010 Date: June 10, 2016  
Examiner: Prof. Dr.-Ing. Georg Carle Midterm  

**A1 A2 A3**  
First Correction  
Second Correction  
Leave Lecture Hall from to  
from to  
Early Submission by  
Comments  

Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Midterm**  
Fundamentals of Computer Networks and Distributed Systems  
(GRNVS)  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
Friday, June 10, 2016  
18:30 – 19:15  

- This exam consists of  
  - 8 pages with a total of 3 tasks as well as  
  - a double-sided printed formula collection.  
  Please check now that you have received a complete set of information.  
- Tasks marked with * can be solved without knowledge of the results of previous subtasks.  
- Only those results will be counted where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective subtask.  
- Do not write with red/green colors or with pencil.  
- The total score for this exam is 20 points. These will be weighted with a factor of 0.5. In the case of quarter points, rounding will be to the next multiple of 0.5.  
- The following aids are permitted:  
  - a non-programmable calculator  
  - an analog dictionary German native language without annotations  
- Turn off all electronic devices you have with you completely, store them and all other documents in your bag and close it.  

---

**Task 1**  
Network (6 points)  
We consider the network in Figure 1.1. Client 3 wants to send an ICMP message to the server with the address 8.8.8.8. Ethernet is used at layer 2. The caches of the various devices are empty at the beginning. The router is configured as the default gateway for all devices in the local network.  

```
Server1 8.8.8.8
eth0
Client1
eth0
eth0
Client2
eth1 eth0
Internet
Hub
eth0 Switch Router
Client3
```
**Figure 1.1: Network Topology**  

a) *Mark and label the collision domain in which Client 1 is located. Make the markings directly in Figure 1.1.  
0.5  

b) *Mark and label the broadcast domain in which Server 1 is located. Make the markings directly in Figure 1.1.  
0.5  

c) *Justify how the L2 and L3 header fields of the message are changed by the hub, switch, and router.  
1  

d) *Draw a simplified time-distance diagram from the perspective of Client 3 for sending the ICMP message. Label all messages with their respective type. Note: Serialization time and propagation delay can be neglected.  
1  

e) *On the interface eth1 of the router, the address 198.51.100.99 is configured. Provide the network address and prefix length for the minimally required subnet so that all clients and the server can be assigned an address from it.  
1  

f) Assign suitable addresses from the subnet in part e) to Client 3 and Server 1.  
1  

g) Name the algorithm and explain what information a router uses to decide where to forward a packet.  
1  

---

**Task 2**  
Cyberchicks (7.5 points)  
The miners of Cyberhausen operate the deepest chicken coop in the world. At a depth of 3 km, brown and white eggs are hatched. For simplification, we assume that brown chickens hatch from brown eggs and white chickens hatch from white eggs.  

To communicate with the surface, chickens are used. If the miner wants to transmit a message to the surface, he lets formations of four chickens fly up. Within a formation, the chickens fly in pairs, where a brown chicken is followed by a white one and vice versa. Individual formations follow each other at a time interval of 10 seconds. Chickens ascend at a constant speed of 50 km/h, meaning they accelerate infinitely quickly to their maximum speed.  

a) *What term from message transmission corresponds to a formation of four chickens?  
0.5  

b) *How many bits can be represented with a formation?  
0.5  

c) *Determine the propagation delay to the surface of the shaft.  
0.5  

d) *Determine the achievable data rate in bits/s.  
0.5  

e) *Calculate the transmission time for a message of 1 KiB.  
1  

The surface can communicate with the chicken coop by throwing eggs into the shaft. An egg represents a single bit on the "line."  

f) *What property must the line code have so that there is neither a shortage nor an excess of eggs of one color in the mine?  
0.5  

The 8b/10b code is used as the line code. Thus, channel words of length 8 bits (1B) fit exactly into a dozen egg carton. When an egg carton hits the mine, on average 2% of the eggs break.  

g) *Calculate the probability that a channel word (dozen carton) arrives faulty.  
1  

A message consists of a palette of up to 1000 dozen cartons, which are thrown into the shaft one after the other.  

h) *How many bytes fit on a palette?  
0.5  

As a channel code, a block code is used, which maps data blocks of k = 223B to n = 250B long channel words. In each channel word, up to 16 incorrectly transmitted bytes can be corrected.  

i) *Calculate the information content of a full palette.  
0.5  

j) *Calculate the frame error probability for a frame of length 223B. Note: a specific numerical value is not required.  
1  

---

**Task 3**  
Short Tasks (6.5 points)  

a) *How does the recipient of a frame recognize whether the payload is an IPv6 packet?  
0.5  

b) *Match. Note: Multiple assignments are possible.  
0.5  
20:7f::45:13:7e:a3  IPv4 Layer  
87.125.45.62  Ethernet Layer  
34:82:a3:23:3c:65  IPv6 Layer  

c) *Briefly explain two multiplexing methods.  
1  

d) *Draw the minimum spanning tree. Pay attention to the given edge costs.  
1  

e) *Explain the shortest-path tree.  
1  

f) *Briefly explain the difference between link-state and distance-vector algorithms.  
1  

g) *Under what conditions can 2 subnets be aggregated?  
1  

Additional space for solutions. Clearly mark the assignment to the respective subtask. Do not forget to cross out invalid solutions.