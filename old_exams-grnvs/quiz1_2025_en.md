Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  
__ __ __ __ __ __ __ __  
1  
2 Signature  
3  
4  
Notes:  
5  
• Mark your student ID. This will be evaluated automatically.  
6  
• Sign in the designated signature field.  
7  
8 Note: Only a calculator and an analog dictionary in your native language without annotations are allowed as aids.  
9 × Student ID •• The questions are printed on the back of this sheet.  
This quiz contains multiple choice/multiple answer sub-tasks, i.e., there is at least one correct answer option for each. These sub-tasks are graded with 1 point for a correct mark and -1 point for an incorrect mark. Missing marks have no impact. The minimum score per sub-task is 0 points.  
×  
Mark the correct answers  
■  
Marks can be crossed out by completely filling them in.  
×■  
Crossed-out answers can be marked again by adjacent markings.  
a)* What was the earliest predecessor of today’s Internet?  
BITNET ARPANET NetBIOS DECnet CYCLADES  
b)* In which step of message transmission is redundancy removed?  
Source coding Modulation Channel decoding  
Channel coding Line coding In no step  
Source decoding Detection Demodulation  
c)* Given is a memoryless source Q, which statistically emits symbols independently and uniformly from an alphabet of length 42. What is the entropy of the source rounded to two decimal places?  
42.00 5.39 10.85 3.58 0.00 0.02  
d)* Given is another memoryless source Q with the alphabet = τ. What is the information content of the symbol τ rounded to two decimal places?  
0.50 0.00 2.71 3.14 5.75 1.00  
e)* We consider an encoder that adds 14 bits of redundancy to data words and thus generates channel words with a length of 332 bits. How much useful data can be sent in 5 channel words?  
1,646 bits 318 bits 1,660 bits 1,590 bits 388 bits 332 bits  
f)* Given is the baseband signal depicted below, which encodes the bit sequence 0100 0101. Which line code presented in the lecture is it?  
NRZ  
s(t)  
Manchester  
RZ t  
MLT-3  
PAM-4  
–Page 1/2–  
g)* Which functional unit or units correspond to the payload that is passed from layer 3 to layer 2 in a layered model?  
3-PCI 2-PDU 3-SDU 3-PDU 2-SDU 1-PDU  
h)* Name and briefly describe two advantages of Manchester line coding compared to Non-Return-to-Zero line coding.  
1  
2  
0 i)* Given is the spectrum of a periodic time signal s(t) below. Here, ω = 2π, with T = 1s.  
T  
Draw s(t) in the solution field on Form 1. If you make a mistake, use Form 2 and clearly cross out Form 1.  
Note: Your drawing does not have to be perfect. Make sure that the properties of the signal are clearly recognizable.  
1  
1  
4  
ak 0.5 bk 0.5  
nt nt  
e e  
zi zi  
fi fi  
ef 0 ef 0  
o o  
k k  
er er  
uri−0.5 uri−0.5  
o o  
F F  
− −  
1 1  
0 1 2 3 4 5 0 1 2 3 4 5  
Harmonics Harmonics  
Form 1 Form 2  
1 1  
) )  
(t (t  
s s  
e e  
d d  
u u  
plit 0 plit 0  
m m  
a a  
al al  
n n  
g g  
Si− Si−  
1 1  
0 0.5 1 0 0.5 1  
Time [s] Time [s]  
∈X  
Information content and entropy: A memoryless source emits symbols x, expressed through ZVX:  
X  
∈X −  
Information content of x: I(x) = log (Pr[X=x])  
2  
−  
Entropy of the source: H(X) = Pr[X=x] log (Pr[X=x])  
2  
x∈X  
X Z Z  
Fourier series: Angular frequency ω = 2π/T  
∞  
a 2 T/2 2 T/2  
s(t) = 20 + k=1 ak cos(kωt) + bk sin(kωt) with ak = T − T/2 s(t) cos(kωt) dt, bk = T − T/2 s(t) sin(kωt) dt.  
Channel coding: Example Block codes: A block of length k bits is mapped to n bit long channel words (n > k). For each channel word, k bits can be corrected (depending on the code).  
−  
k n Code rate: R = k/n  
x C x′  
–Page 2/2–