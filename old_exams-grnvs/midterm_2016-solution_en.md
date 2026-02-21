Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by attaching a code during attendance control.
- This contains only a sequential number, which is also noted on the attendance list next to the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems (GRNVS)  
Module: IN0010  
Date: June 10, 2016  
Examiner: Prof. Dr.-Ing. Georg Carle  
Exam Type: Midterm  

**Room Exit**  
From: __________ to: __________  
Early Submission: __________  

### Comments

---

### Midterm  
Fundamentals of Computer Networks and Distributed Systems (GRNVS)  
Prof. Dr.-Ing. Georg Carle  
Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Date:** Friday, June 10, 2016  
**Time:** 18:30 – 19:15  

- This exam consists of:
  - 8 pages with a total of 3 tasks as well as
  - a double-sided printed formula collection.
  
Please check now that you have received a complete set of information.
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.
- Only those results will be counted where the solution method is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-task.
- Do not write with red/green colors or with pencil.
- The total score for this exam is 20 points. These will be weighted with a factor of 0.5. In the case of quarter points, round to the nearest multiple of 0.5.
- The following aids are allowed:
  - a non-programmable calculator
  - an analog dictionary in the native language without annotations
- Turn off all electronic devices you have with you completely, store them and all other documents in your bag, and close it.

---

### Task 1  
Network (6 Points)  
We consider the network in Figure 1.1. Client 3 wants to send an ICMP message to the server with the address 8.8.8.8. Ethernet is used at Layer 2. The caches of the various devices are empty at the beginning. The router is configured as the default gateway for all devices in the local network.

**Broadcast Domain**  
**Collision Domain**  
Server 1 8.8.8.8  
eth0  
Client 1  
eth0  
eth0  
Client 2  
eth1  
eth0  
Internet  
Hub  
eth0  
Switch  
Router  
Client 3  

**Figure 1.1: Network Topology**  

a) *Mark and label the collision domain in which Client 1 is located. Make the markings directly in Figure 1.1.*  
**0.5 Points**

b) *Mark and label the broadcast domain in which Server 1 is located. Make the markings directly in Figure 1.1.*  
**0.5 Points**

c) *Justify how the L2 and L3 header fields of the message are changed by Hub, Switch, and Router.*  
- Hub, Switch: none  
- Router: decrements TTL, (Checksum), new MACs (FCS)  
**1 Point**

d) *Draw a simplified time-distance diagram from the perspective of Client 3 for sending the ICMP message. Label all messages with their respective type. Note: Serialization time and propagation delay can be neglected.*  
**1 Point**

Client 3 Hub Switch Router 8.8.8.8  
ARP Request  
ARP Reply  
IPv4 + ICMP  

e) *On the interface eth1 of the router, the address 198.51.100.99 is configured. Provide the network address and prefix length for the minimally required subnet so that all clients and the server can be assigned an address from it.*  
**1 Point**  
198.51.100.96/29  

f) *Assign suitable addresses from the subnet in part e) to Client 3 and Server 1.*  
Client 1: 198.51.100.97  
Server 1: 198.51.100.98  
**0.5 Points**

g) *Name the algorithm and explain what information a router uses to decide where to forward a packet.*  
Longest Prefix Matching  
Depending on the destination IP address, the appropriate entry (longest prefix match) is selected from the routing table. This entry then contains the next hop as well as the interface to be used.  
**1 Point**

---

### Task 2  
Cyberchicks (7.5 Points)  
The miners of Cyberhausen operate the deepest chicken coops in the world. At a depth of 3 km, brown and white eggs are hatched. We simplify by assuming that brown eggs hatch brown chickens and white eggs hatch white chickens.

To communicate with the surface, chickens are used. If the miner wants to transmit a message to the surface, he lets formations of four chickens fly upwards. Within a formation, the chickens fly in pairs, where a brown chicken is followed by a white one and vice versa. Individual formations follow each other with a time gap of 10 seconds. Chickens ascend at a constant speed of 50 km/h, meaning they accelerate infinitely fast to their maximum speed.

a) *What term from message transmission corresponds to a formation of four chickens?*  
**0.5 Points**  
Formation = Channel symbol / Send pulse  

b) *How many bits can be represented with one formation?*  
**0.5 Points**  
Due to the requirement of color change, there are only 4 different formations for four chickens per formation. Therefore, log(4) = 2 bits are transmitted per formation.  

c) *Determine the propagation delay to the surface of the shaft.*  
**0.5 Points**  
3 km · (1 s / 3600) = 216 s at 50 km/h  

d) *Determine the achievable data rate in bits/s.*  
**0.5 Points**  
2 bits / 10 s = 0.2 bits/s  

e) *Calculate the transmission time for a message of size 1 KiB.*  
**1 Point**  
1 KiB · (8 bits / B) / 0.2 bits/s + 216 s = 1024 B / 0.2 bits/s + 216 s = 41176 s  

The surface can communicate with the chicken coop by throwing eggs into the shaft. An egg represents a single bit on the "line."

f) *What property must the line code have so that neither a shortage nor an excess of eggs of one color occurs in the mine?*  
**0.5 Points**  
DC-free  

g) The 8b/10b code is used as the line code. Thus, channel words of length 8 bits (1 B) fit exactly into a ten-egg carton. When an egg carton hits the mine shaft, on average, 2% of the eggs break.  

h) *Calculate the probability that a channel word (ten carton) arrives faulty.*  
**0.5 Points**  
P = 1 - (1 - 0.02)¹⁰ ≈ 1 - 0.981⁰ = 18.29%  

A message consists of a pallet of up to 1000 ten cartons, which are thrown into the shaft one after the other.  

h) *How many bytes fit on a pallet?*  
**0.5 Points**  
1000 cartons * 10 bits / 8 bits = 1000 B  

As a channel code, a block code is used, which maps data blocks of k = 223 B to n = 250 B long channel words. In each channel word, up to 16 incorrectly transmitted bytes can be corrected.  

i) *Calculate the information content in one pallet.*  
**0.5 Points**  
n = 1000 B / 250 B = 4  
l = 4 * 223 B = 892 B  

j) *Calculate the frame error probability for a frame of length 223 B. Note: a specific numerical value is not required.*  
**0.5 Points**  
P = 1 - Σ (from i=0 to 16) (16 choose i) * (0.02)ⁱ * (0.98)^(16-i)  

---

### Task 3  
Short Tasks (6.5 Points)  

a) *How does the receiver of a frame recognize whether the payload is an IPv6 packet?*  
**0.5 Points**  
By the EtherType of the Ethernet header  

b) *Match the following. Note: Multiple assignments are possible.*  
**0.5 Points**  
1. 20:7f::45:13:7e:a3 - IPv6  
2. 87.125.45.62 - IPv4  
3. 34:82:a3:23:3c:65 - Ethernet  

c) *Briefly explain two multiplexing methods.*  
**0.5 Points**  
- Time Division Multiplexing: Division in the time domain, different clients send at different times  
- Frequency Division Multiplexing: Different clients use different frequencies that do not overlap  
- Space Division Multiplexing: Different transmission paths  
- Code Division Multiplexing: Orthogonal alphabets, assignment of alphabets to communication partners  

d) *Draw the Minimum Spanning Tree. Note the specified edge costs.*  
**1 Point**  

e) *Explain the Shortest-Path Tree.*  
**1 Point**  
Shortest connection to all nodes for a specific root node  

f) *Briefly explain the difference between Link-State and Distance-Vector algorithms.*  
**1 Point**  
- Distance-Vector: Only next hop known, e.g., Bellman-Ford, no complete topology, distributed implementation possible  
- Link-State: Complete path information known, e.g., Dijkstra, complete topology known, more complex implementation  

g) *Under what conditions can two subnets be aggregated?*  
**0.5 Points**  
Equal size, adjacent, same prefix except for the last bit being 1  

---

Additional space for solutions. Clearly mark the assignment to the respective sub-task.  
Do not forget to cross out invalid solutions.