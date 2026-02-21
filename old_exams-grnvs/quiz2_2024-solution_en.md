Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

Confirmation of Code of Conduct  
I hereby assure that I will solve this exam exclusively using the resources listed below and submit it under my name.  
Sticker will be generated  
Signature or full name, if no pen input is available  

Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Quiz2 Date: Tuesday, May 28, 2024  
Examiner: Prof. Dr.-Ing. Georg Carle Time: 19:00–19:15  

Do not forget to confirm the code of conduct (see above) by signing or entering your name (if no pen input is available). Submissions without confirmation will not be graded.  

Processing Instructions  
- This exam consists of 4 pages with a total of 3 tasks. Please check now that you have received a complete set of information.  
- The total score for this exam is 15 points.  
- The tearing out of pages from the exam is prohibited.  
- The following resources are permitted:  
  - everything except group work, plagiarism, and any form of AI (e.g., ChatGPT)  
  - Tasks marked with * can be solved without knowledge of the results of previous tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Always answer free text tasks in your own words. Foreign or copied answers will not be accepted.  
- Violations of the code of conduct will lead to exclusion from the bonus procedure.  
- Do not write with red/green colors or with pencil.  

---  
**Task 1**  
Multiple Choice (7 Points)  
The following tasks are multiple choice/multiple answer, meaning at least one answer option is correct.  
Sub-tasks with only one correct answer will be awarded 1 point if correct. Sub-tasks with more than one correct answer will be awarded 1 point for each correct answer and 1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

Mark the correct answers  
- Marks can be crossed out by complete filling  
- Crossed-out answers can be marked again by adjacent markings  

a) You encode a message with the (7,4)-Hamming code, which has a code rate of R = 4, and receive an encoded message of size 1792 B. How large is the original message?  
- 1,024 KiB  
- 3,136 KiB  
- 1024 B  
- 3,063 kB  
- 1 KiB  
- 3136 B  

b) Which statement(s) apply to the MAC address 64:1D:EB:44:1E:CC?  
- Multicast  
- Unicast  
- Bicast  
- Globally unique  
- Locally administered  
- Broadcast  

c) Which statement(s) are correct regarding G1 and G2 in the network topology in Figure 1.1?  
- G1 and G2 are Access Points  
- G1 and G2 are Bridges  
- G1 and G2 are Switches  
- G1 and G2 are Hubs  

d) Which statement(s) are correct regarding G3 in the network topology in Figure 1.1?  
- G3 is an Access Point  
- G3 is a Hub  
- G3 is a Switch  
- G3 is a Bridge  

e) How many collision domains are there in the network in Figure 1.1?  
- 9  
- 5  
- 8  
- 2  
- 7  
- 6  
- 3  
- 1  
- 4  
- 10  

---  
**Task 2**  
Short Tasks (2 Points)  
The network topology in Figure 1.1 is potentially problematic. You notice that communication between PC1 and PC2 does not function as desired.  
What could be the cause of this problem? How can such problems generally be resolved or avoided?  

There is a loop between the two switches G1 and G2. Depending on the model of the switch used, this can cause sent messages to circulate between the switches.  
To solve the problem, one can either replace G1 and G2 with switches that support the Spanning Tree Protocol or remove one of the redundant connections between G1 and G2.  

---  
**Task 3**  
Legend of the Galactic High-Speed Communication (6 Points)  
In a distant future, humanity has settled hundreds of star systems. After capturing the fortress Iserlohn through a trick, they want to transmit the enemy's information database from the fortress to the capital planet Heinessen, which are exactly 4010 light years apart. The database has a total size of 958 PiB = 980,992 TiB.  

For the transmission of the 958 PiB, three different channels with the following properties are available:  
1. Laser-based transmission  
2. FTL (Faster Than Light) communication channel  
3. Transport of data carriers through the vacuum for transmission from an FTL spaceship  

- Transmission rate: r1 = 3.8 Tibit/s  
- Flight duration of the spaceship: 21 days  
- Propagation delay: tp = 64 ms  
- Relative propagation speed: ν = 1  
- Data serialization time: t = 2280.17 a  
- Copy duration of the data on the carrier: 5 days  

You are asked to determine which variant will get the data to Heinessen the fastest. Provide all time specifications and probabilities in meaningful units rounded.  

a) What is the propagation delay of Variant 1?  
Since Iserlohn and Heinessen are exactly 4010 light years apart, light takes exactly 4010 years for this distance.  
- \( t = \frac{4010 \text{ Lj}}{c} = \frac{4010 \text{ a}}{c} \)  

b) What is the serialization time of Variant 1?  
In general, the serialization time is given by \( t = \frac{L}{r} \) with \( L = 958 \text{ PiB} = 2^{10} \cdot 958 \text{ TiB} = 980,992 \text{ TiB} \).  
- \( t = \frac{980,992 \text{ TiB} \cdot 8 \text{ bit/B}}{3.8 \text{ Tibit/s}} \approx 2,065,246.316 \text{ s} \approx 23.90 \text{ d} \)  

c) Which of the variants is the fastest?  
- FTL spaceship  
- FTL communication channel  
- Laser-based transmission  

The database was transferred in 5 days to a total of 40 data carriers. The transport of the data carriers in an FTL spaceship is error-prone, as the data can be damaged due to solar storms. This occurs independently for each data carrier with a probability of \( \frac{1}{42} \).  

d) With what probability do all 40 data carriers arrive without errors?  
Let \( X \) be a random variable \( \text{Bin}(40, \frac{1}{42}) \): the number of damaged data carriers after transport.  
- \( P[X = 0] = \binom{40}{0} \cdot \left( \frac{1}{42} \right)^0 \cdot \left( 1 - \frac{1}{42} \right)^{40} \approx 1 \cdot 0.38 \)  

11 Lj is the distance light travels in a vacuum in exactly one year.  
The framework of this task is based on the sci-fi novel series "Legend of the Galactic Heroes" by Yoshiki Tanaka.  
Abbreviation for Faster Than Light, i.e., superluminal speed.  
1 a means 1 year.  

---  
Additional space for solutions. Clearly mark the allocation to each sub-task. Do not forget to cross out invalid solutions.