Chair of Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  

**Notes on Personalization:**  
- Your exam will be personalized by attaching a code during attendance control.  
- This code contains only a sequential number, which is also noted on the attendance lists next to the signature field.  
- This will be used as a pseudonym to enable a unique assignment of your exam.  

**Fundamentals of Computer Networks and Distributed Systems**  
Module: IN0010  
Date: Friday, June 23, 2017  
Examiner: Prof. Dr.-Ing. Georg Carle  
Exam: Midterm  

**Instructions for Processing**  
- This exam consists of  
  - 8 pages with a total of 3 tasks as well as  
  - a collection of formulas.  
Please check now that you have received a complete set of information.  
- The processing time is 45 minutes.  
- It is prohibited to tear out pages from the exam.  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be counted where the solution path is recognizable. Text tasks must also be justified unless explicitly stated otherwise in the respective sub-task.  
- Do not write with red/green colors or with pencil.  
- The total score for this exam is 20 points, which will be scaled according to the bonus system.  
- The following aids are permitted:  
  - an analog dictionary in German without annotations  
- Turn off all electronic devices you have with you completely, store them in your bag, and close it.  

---

### Task 1  
**Media Access (7 Points)**  
On the planet Gliese 581c, a water world inhabited by the Moepis, global warming has been occurring for several years. As a result, a small island has formed, which is being researched by the Moepis. Since the Moepis live far away from the island on the seabed, they have built a floating relay station that is to serve for the transmission of messages between the island and the Moepi base (see Figure 1.1).  

In this process, the frame from the island or the Moepi base will be received by the relay, checked for transmission errors, and forwarded to the respective other side. Neither the island nor the Moepi base needs to explicitly address the relay.  

On the route from island I to relay R, the Moepis use an advanced method of radio transmission based on electromagnetic waves. However, since water has a strong damping effect on electromagnetic waves, sound waves are used there. These propagate in water at approximately \( v_W = 1500 \, m/s \).  

![Figure 1.1: Topological Structure of the Relay Station](#)  

a) *Justify which network component known from the lecture corresponds most closely to the relay.*  
b) *What method can the Moepis use to detect transmission errors?*  
c) *Describe the general functionality and goal of channel coding.*  

---

![Figure 1.2: Test Setup](#)  

The communication between island I via relay R to the Moepi base B is tested on a test route, which is schematically shown in Figure 1.2. A test frame of 1000 bits is sent from I via R to B. The transmission rate is 1 kbit/s.  

d) *Draw all broadcast and collision domains in Figure 1.2 (pay attention to clear labeling).*  
e) *Calculate the serialization time for the test frame.*  
f) *Calculate the propagation delay between I and R as well as between R and B.*  
g) *Draw a complete path-time diagram for the test transmission with a scale of 1 mm = 1 s.*  

---

### Task 2  
**Modulation (9 Points)**  
In this task, we consider the precursor of pulse shaping in baseband and the subsequent modulation. We use the rectangular pulse as the basic pulse in the baseband:  
\[
rect(t) = 
\begin{cases} 
1 & -\frac{T}{2} \leq t < \frac{T}{2} \\ 
0 & \text{otherwise} 
\end{cases}
\]  

The modulation method uses the signal space points shown in Figure 2.1.  

![Figure 2.1: Signal Space](#)  
![Figure 2.2: Basic Pulse](#)  

a) *What modulation method is being used?*  
b) *Assign valid code words to the symbols in Figure 2.1.*  
c) *Draw the basic pulse \( rect(t) \) in Figure 2.2.*  

We want to transmit the bit sequence 01101100.  
d) *Enter the corresponding code words for the bit sequence as well as the in-phase component I and quadrature component Q.*  

**Code Words**  
| Bit | Code Word | I | Q |
|-----|-----------|---|---|
| 0   |           |   |   |
| 1   |           |   |   |

*Note: If necessary, you will find an additional form for the following sub-tasks at the end of the exam. Clearly cross out invalid solutions.*  

e) *Draw the baseband signal of the in-phase component for the given bit sequence in Figure 2.3.*  
f) *Draw the baseband signal of the quadrature component for the given bit sequence in Figure 2.4.*  

The two baseband signals are now modulated with the frequency \( f = 1/T \). For the in-phase component, we use the cosine carrier \( cos(2\pi ft) \) and for the quadrature component, the sine carrier \( sin(2\pi ft) \).  
g) *Also draw the modulated signal of the in-phase component in Figure 2.3.*  
h) *Also draw the modulated signal of the quadrature component in Figure 2.4.*  
i) *Draw the complete modulated signal in Figure 2.5.*  

---

### Task 3  
**Short Tasks (4 Points)**  
a) *Justify whether 192.0.2.96/27 and 192.0.2.128/27 can be summarized.*  
b) *Derive the usual link-local IPv6 address from the MAC address 00:00:5e:00:53:42 using the method known from the lecture. Provide this in shortened form.*  
c) *Name two classes of routing protocols and briefly differentiate them from each other.*  
d) *What is ARP used for and how is this functionality achieved in IPv6?*  

---

**Additional Forms for Task 2**  
![Figure 3.1: In-phase Component: Baseband and Modulated](#)  
![Figure 3.2: Quadrature Component: Baseband and Modulated](#)  
![Figure 3.3: Modulated Total Signal](#)  

**Additional space for solutions. Clearly mark the assignment to the respective sub-task. Do not forget to cross out invalid solutions.**