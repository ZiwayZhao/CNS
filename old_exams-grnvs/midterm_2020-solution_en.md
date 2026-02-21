Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized by attaching a code during the attendance check.
- This contains only a continuous number, which should also be pasted on the attendance lists marked with the signature field.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Midterm  
Date: Tuesday, June 16, 2020  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 10:15–11:05  

This exam can be processed digitally (tablet with stylus input, computer with PDF annotator with support for freehand drawing) and subsequently submitted via TUMexam. Please pay attention to the instructions that are also valid for the homework at  
[https://grnvs.net.in.tum.de/homework_submission_details.txt](https://grnvs.net.in.tum.de/homework_submission_details.txt).

### Instructions for Processing
- This exam consists of 8 pages with a total of 4 tasks. Please check now that you have received a complete set of information.
- The total score for this exam is 45 points.
- It is prohibited to tear out pages from the exam.
- The following aids are allowed:
  - All individual aids (lecture materials, exercises, calculators, etc.)
  - Group work of any kind and copy & paste are not allowed.
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only results where the solution method is recognizable will be counted. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write with red/green colors or with pencil.

---

### Task 1  
Multiple Choice (7 Points)  
The following sub-tasks are multiple-choice single-answer questions with 1 point for a correct answer and 0 points otherwise.  
Instructions for processing on paper or if your PDF editor does not support the checkbox function:  
- Mark the correct answers.  
- Checkboxes can be crossed out by completely filling them in.  
- Crossed-out answers can be marked next to them to indicate they are no longer selected.  

a) To which layer of the ISO/OSI model does ICMP belong?  
- Layer 3: Network Layer  
- Layer 1: Physical Layer  
- Layer 4: Transport Layer  
- Layer 2: Data Link Layer  

b) If one of the PCs in the adjacent image wants to send a frame to the notebook (NB), which MAC address(es) will be used to specify the destination?  
- AP SW and NB  
- NB AP and NB  

c) If one of the PCs in the adjacent image wants to send a frame to the notebook (NB), which IP address(es) will be used to specify the destination?  
- NB AP vSW and NB  
- AP and NB  

d) Given a signal power of 12 mW and noise power of 18 mW. Determine the SNR in dB.  
- Other value  
- 0.67 dB  
- 1.76 dB  
- 1.17 dB  
- 0.18 dB  
- 0.58 dB  

e) Given the date 0xb3416879 in Little Endian. What is the representation in Big Endian?  
- 0x3b148697  
- 0x143b9786  
- 0x9786143b  
- 0xb3416879  
- 0x796841b3  

f) Given a binary message source that emits a character with a probability p = 0.7. Determine the entropy of the source.  
- 0.52 bit  
- 0.36 bit  
- 0.88 bit  
- 0.15 bit  
- 1.22 bit  
- Other value  

g) Which statement about trace routes applies to the paths between two hosts?  
- All paths are revealed  
- A possible path is revealed  
- No real paths are revealed  
- A path is revealed  

---

### Task 2  
Short Tasks (16 Points)  

a) Explain in your own words the difference between channel capacity according to Shannon and Hartley.  
Shannon defines channel capacity based on physical effects (SNR), Hartley based on distinguishable symbols.  

b) A signal is to be quantized within the interval I = [-3;3] with a step size of 2 bits, so that the quantization error within I is minimized. Specify the quantization levels.  
- 4 levels equally distributed on [-3;3]: -2.25, 0.75, 2.25  

c) Given the bit sequence 0001 0011. Draw the baseband signal when MLT-3 is used as the line code. It holds that s(t) = 0 for t < 0.  

d) Draw all broadcast domains in the diagram below. Make sure to clearly indicate the membership of an interface to the respective domain.  

e) What is the concrete difference between CSMA/CD and CSMA/CA regarding the binary exponential backoff?  
In CSMA/CA, there is a lower limit > 0 slot times for the backoff (called contention window), while in CSMA/CD the backoff interval only exists if a collision has occurred beforehand.  

f) Why do IEEE 802.11 frames often have three fields for MAC addresses?  
Clients do not communicate directly with each other in IEEE 802.11 but always through an AP, which is not transparent within the wireless network. Therefore, both the destination and the AP must be addressable at Layer 2.  

g) Given the schematically represented Ethernet frame below. Mark the L3-PDU in it.  

h) Assign the following terms to the respective layer of the ISO/OSI model.  
- L1: Frame  
- L2: Packet  
- L3: Segment  
- L4:  

i) Provide a typical, unique, and above all meaningful signal space assignment for ASK, PSK, and QAM. An additional short justification is required to distinguish between PSK and QAM!  

j) Mark all fields in the following IPv4 header that a router modifies when the packet is forwarded and not fragmented.  
- Version  
- IHL  
- TOS  
- Total Length  
- Identification  
- R  
- DF  
- MF  
- Fragment Offset  
- TTL  
- Protocol  
- Header Checksum  
- Source Address  
- Destination Address  

---

### Task 3  
IPoAC (IP over Avian Carriers) (6 Points)  
IPoAC (IP over Avian Carriers) is an alternative to conventional Ethernet. It was published under RFC 1149 on April 1, 1990. In this method, Layer 2 data packets are manually hexadecimally encoded, written on a piece of paper, transported to the destination by a pigeon, and reloaded into a computer for further processing through an ocular scan. This is very labor-intensive. To keep up with the times, the advantages over Ethernet will be explained below when high-performance USB sticks are used.  

To write and read a USB stick, a serialization time (t_s) of 256 seconds must be taken into account. The USB sticks all have a capacity of 8 GiB. The avian carriers have an extraordinary propagation speed of 120 km/h!  

a) How many bits can be sent with a USB stick?  
- L = 8 GiB = 8 GiB * 2^30 B/GiB * 8 bit/B = 2^36 bit  

b) Show that a higher transmission rate is possible than with an average good 100 Mbit/s Ethernet line.  
- t_s = 256 s = 2^8 s  
- L/t_s = 2^36 bit / 2^8 s = 2^28 bit/s  
- 2^28 bit/s = 268,435,456 bit/s  
- 268,435,456 bit/s > 268.43 Mbit/s > 100 Mbit/s  

c) Messages are sent over a distance of 50 km. Determine the propagation delay (in seconds).  
- t_p = 50 km / 120 km/h = 50 / (120 / 3600) = 1500 s  

d) Sending a 50 GiB archive file over Ethernet over the same distance takes about 4300 s. How long would it take in the given case with IPoAC (in seconds)?  
- 50 GiB ⇒ 50 GiB / 8 GiB = 6.25, so 7 USB sticks are needed.  
- Therefore, 7 USB sticks must be serialized, i.e., t_s = 7 * 256 s.  
- Since multiple pigeons can fly through the air simultaneously, t_p = 1500 s.  
- t_d = t_s + t_p = 7 * 256 s + 1500 s = 3292 s  

---

### Task 4  
News from the General Post Office (16 Points)  
To enable crisis-resistant message transmission, a system based on POCSAG is reportedly being used at the Chair of Network Architectures and Network Services (GRNVS-POCSAG). GRNVS-POCSAG is a protocol that wirelessly transmits information in 16-bit packets including a 4-bit CRC checksum to so-called pagers.  

Depending on the message text, either BCD or ASCII is used for encoding the message:  
1. BCD if the message consists only of numbers  
2. ASCII otherwise  

To inform the GRNVS exercise management about the start of the midterm, the following message is to be sent:  
QRV?  

a) Provide the message to be transmitted in binary representation.  
- 0b 01010001 01010010 01010110 00111111  

b) Mark in the above answer all positions where the bit sequence to be transmitted must be divided for transmission with GRNVS-POCSAG.  

c) Provide the ratio of useful data to transmitted data.  
- The bit sequence is 4 * 8 bit = 32 bit long. Packets can contain up to 12 bits of payload. Therefore, 3 packets are needed for transmission, each with a length of 16 bits (including PCI).  
- Code rate: k = 32 / (3 * 16)  

An important part of a GRNVS-POCSAG packet is the included checksum. This is the remainder from the SDU to be transmitted after polynomial division in F2[x] with x^4 + x^2 + 1.  

d) Name two types of errors that cannot be reliably detected in GRNVS-POCSAG.  
- Errors that are longer than the degree of the reduction polynomial  
- Errors that are multiples of the reduction polynomial  

e) After some time, a packet with the GRNVS-POCSAG-SDU 0x515 is to be transmitted. Determine the corresponding checksum.  
- 0101 0001 0101 0000 : 10101  
- 10101  
- Remainder: 0101  

f) Determine the transmission duration of sending the exam readiness over GRNVS-POCSAG. The propagation delay can be neglected.  
- Number of packets needed: 840 * 8 bit = 560.  
- Transmission duration for all packets: 560 * 16 bit / 512 bit/s = 17.5 s  

g) Provide the message flow between the two existing GRNVS-POCSAG sending stations and the four pagers of the exercise management as a graph.  
- G = (V, E) where V = {s0, s1, p0, p1, p2, p3} and E = (si, pj) for i = 0,1 and j = 0,1,2,3. Nodes represent sending stations and nodes p represent pagers.  

h) Is it a directed or undirected graph?  
- Directed, as the pagers do not interact with the sending stations.  

To increase area coverage with GRNVS-POCSAG, a repeater is to be set up. This repeats GRNVS-POCSAG packets that reach it on the same frequency.  

i) What challenge regarding media access arises from the use of a repeater?  
- Now there are two transmitters on the same frequency, so collisions can occur during transmissions.  

j) Name two ways to address the resulting problem.  
- Time multiplexing  
- Repeater transmits on a different frequency  

---

Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.