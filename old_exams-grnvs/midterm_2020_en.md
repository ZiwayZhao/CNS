Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

### Notes on Personalization:
- Your exam will be personalized during attendance control by attaching a code.
- This contains only a continuous number, which should also be pasted on the attendance list next to the signature field marked with SRID.
- This will be used as a pseudonym to enable a unique assignment of your exam.

### Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Midterm  
Date: Tuesday, June 16, 2020  
Examiner: Prof. Dr.-Ing. Georg Carle  
Time: 10:15–11:05  

This exam can be processed digitally (tablet with stylus input, computer with PDF annotator with support for freehand drawing) and subsequently submitted via TUMexam. Please strictly observe the already valid notes for the homework at [https://grnvs.net.in.tum.de/homework_submission_details.txt](https://grnvs.net.in.tum.de/homework_submission_details.txt).

### Instructions for Processing
- This exam consists of 8 pages with a total of 4 tasks. Please check now that you have received a complete set of information.
- The total score for this exam is 45 points.
- It is prohibited to tear pages from the exam.
- The following aids are allowed:
  - All individual aids (lecture materials, exercises, calculators, etc.)
  - Group work of any kind and copy & paste are not allowed.
- Tasks marked with * can be solved without knowledge of the results of previous tasks.
- Only those results will be counted where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-tasks.
- Do not write with red/green colors or with pencil.

---

### Task 1  
Multiple Choice (7 Points)  
The following sub-tasks are multiple-choice single-answer questions worth 1 point if answered correctly and 0 points otherwise.  

**Instructions for processing on paper or if your PDF editor does not support the checkbox function:**  
- Check the correct answers.  
- Checked boxes can be crossed out by completely filling them in.  
- Crossed-out answers can be rechecked by marking them next to.

a) Which layer of the ISO/OSI model is ICMP assigned to?  
- Layer 3: Network Layer  
- Layer 1: Physical Layer  
- Layer 4: Transport Layer  
- Layer 2: Data Link Layer  

b) If one of the PCs in the adjacent image wants to send a frame to the notebook (NB), which MAC address(es) will be used to specify the destination?  
- AP SW and NB  
- NB AP and NB  

c) *If one of the PCs in the adjacent image wants to send a frame to the notebook (NB), which IP address(es) will be used to specify the destination?  
- NB AP SW and NB  
- AP and NB  

d) Given a signal power of 12 mW and noise power of 18 mW. Determine the SNR in dB.  
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

f) Given a binary message source that emits a character with a probability of p = 0.7. Determine the entropy of the source.  
- 0.52 bit  
- 0.36 bit  
- 0.88 bit  
- 0.15 bit  
- 1.22 bit  

g) *Which statement about traceroute applies to the paths between two hosts?  
- All paths are revealed  
- A possible path is revealed  
- No real paths are revealed  
- A path is revealed  

---

### Task 2  
Short Tasks (16 Points)  
a) *Explain in your own words the difference between channel capacity according to Shannon and Hartley.  

b) *A signal is to be quantized within the interval I = [3;3] with a step size of 2 bits, so that the quantization error within I is minimized. Specify the quantization levels.  

c) *Given the bit sequence 0001 0011. Draw the baseband signal when MLT-3 is used as the line code. It holds that s(t) = 0 for t < 0.  

d) *Draw all broadcast domains in the diagram below. Make sure to clearly indicate the membership of each interface to the respective domain.  

e) *What is the specific difference between CSMA/CD and CSMA/CA regarding the Binary Exponential Backoff?  

f) *Why do IEEE 802.11 frames often have three fields for MAC addresses?  

g) *Given the schematically represented Ethernet frame below. Mark the L3-PDU in it.  

h) *Assign the following terms to the respective layer of the ISO/OSI model.  
- L1: Frame  
- L2: Packet  
- L3: Segment  

i) *Provide a typical, unique, and especially meaningful signal space assignment for ASK, PSK, and QAM. An additional brief justification is required to distinguish between PSK and QAM!  

j) *Mark all fields in the following IPv4 header that a router modifies when the packet is forwarded and not fragmented.  
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
IPoAC (IP over Avian Carriers) is an alternative to conventional Ethernet. It was published under RFC 1149 on April 1, 1990. In this method, Layer 2 data packets are hand-hexadecimally encoded, written on a piece of paper, transported to the destination on the foot of a pigeon, and reloaded into a computer for further processing through an ocular scan. This is very cumbersome. To keep up with the times, the advantages over Ethernet should be explained when using high-performance USB sticks.  

To write and read from a USB stick, a serialization time (t_s) of 256 seconds must be taken into account. The USB sticks all have a capacity of 8 GiB. The avian carriers have an extraordinary propagation speed of 120 km/h!  

a) *How many bits can be sent with a USB stick?  

b) Show that a higher transmission rate is possible than with an average good 100 Mbit/s Ethernet line.  

c) *Messages are sent over a distance of 50 km. Determine the propagation delay (in seconds).  

d) Sending a 50 GiB archive file over Ethernet over the same distance takes about 4300 seconds. How long would it take in the given case with IPoAC (in seconds)?  

---

### Task 4  
News from the General Post Office (16 Points)  
To enable crisis-proof message transmission, rumors suggest that the Chair for Network Architectures and Network Services will use a system based on POCSAG (GRNVS-POCSAG). GRNVS-POCSAG is a protocol that transmits information in 16-bit packets including a 4-bit CRC checksum wirelessly to so-called pagers.  

Depending on the message text, either BCD or ASCII is used for encoding the message:  
1. BCD, if the message consists only of numbers  
2. ASCII otherwise  

To inform the GRNVS exercise management about the start of the midterm, the following message should be sent:  
QRV?  

a) *Provide the message to be transmitted in binary representation.  

b) Mark in the above answer all places where the bit sequence to be transmitted must be divided for transmission with GRNVS-POCSAG.  

c) Provide the ratio of useful data to transmitted data.  

An important part of a GRNVS-POCSAG packet is the included checksum. This is the remainder of the SDU to be transmitted after polynomial division in F[x] with x^4 + x^2 + 1.  

d) *Name two types of errors that cannot be reliably detected in GRNVS-POCSAG.  

e) *After some time, a packet with the GRNVS-POCSAG-SDU 0x515 should be transmitted. Determine the corresponding checksum.  

GRNVS-POCSAG is transmitted at a frequency of 433.975 MHz with 512 bit/s. At the beginning of the exam, after confirming the examiner's readiness, the exam readiness (n = 840 ASCII characters) will be read out.  

f) *Determine the transmission duration of sending the exam readiness via GRNVS-POCSAG. The propagation delay can be neglected.  

g) *Provide the message flow between the two existing GRNVS-POCSAG sending stations and the four pagers of the exercise management as a graph.  

h) Is it a directed or undirected graph?  

To increase the area coverage with GRNVS-POCSAG, a repeater should be set up. This repeats GRNVS-POCSAG packets that reach it on the same frequency.  

i) *What challenge regarding media access arises from the use of a repeater?  

j) Name two ways to address the resulting problem.  

### Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.