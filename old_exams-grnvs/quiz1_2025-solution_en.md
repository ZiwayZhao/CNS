Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  
___  
1  
2 Signature g  
3  
4  
Notes:  
5  
• Mark your student ID. This will be evaluated automatically.  
6  
• Sign in the designated signature field.  
7  
8 Only a calculator and an unannotated analog dictionary from German to native language are allowed as aids.  
9  
! Student ID • The questions are printed on the back of this sheet.  
This quiz contains multiple-choice/multiple-answer sub-tasks, meaning there is at least one correct answer option for each. These sub-tasks will be graded with 1 point for each correct answer and -1 point for each incorrect answer. Missing marks will have no effect. The minimum score per sub-task is 0 points.  
!  
Mark the correct answers  
↭  
Marks can be crossed out by completely filling them in  
o !  
↭  
Crossed-out answers can be marked again by adjacent markings  
v  
a)* What was the earliest predecessor of today’s Internet?  
!  
BITNET ARPANET NetBIOS DECnet CYCLADES  
s  
b)* In which step of message transmission is redundancy removed?  
! !  
Source encoding Modulation Channel decoding  
Channel coding Line coding In no step  
n  
Source decoding Detection Demodulation  
u  
c)* Given is a memoryless source Q, which emits statistically independent and uniformly distributed symbols from an alphabet of length 42. What is the entropy of the source rounded to two decimal places?  
!  
42.00 5.39 10.85 3.58 0.00 0.02  
d)* Given is another memoryless source Q with the alphabet A={ω}. What is the information content of the symbol ω rounded to two decimal places?  
!  
0.50 0.00 2.71 3.14 5.75 1.00  
L  
e)* We consider an encoder that adds 14 bits of redundancy to data words, thus generating channel words with a length of 332 bits. How much useful data can be sent in 5 channel words?  
!  
1,646 bits 318 bits 1,660 bits 1,590 bits 388 bits 332 bits  
f)* Given is the baseband signal depicted below, which encodes the bit sequence 0100 0101. Which line code presented in the lecture does it correspond to?  
NRZ  
s(t)  
!  
Manchester  
RZ t  
MLT-3  
PAM-4  
–Page 1/2–  
g)* Which functional unit or units does the payload correspond to that is passed from layer 3 to layer 2 in a layered model?  
! !  
3-PCI 2-PDU 3-SDU 3-PDU 2-SDU 1-PDU  
h)* Name and briefly describe two advantages of the Manchester line code compared to the Non-Return-To-Zero line code.  
1  
2 DC-free: Due to the DC-free nature of the Manchester basic pulse, the baseband signals generated with it are always DC-free.  
Clock recovery: Due to the always occurring level change in the basic pulse, the clock can be recovered even with constant symbols.  
l  
h  
0 i)* Given is the spectrum of a periodic time signal s(t) below. Here ε = 2ω, with T = 1s.  
T  
Draw s(t) in the solution field in Form 1. If you make a mistake, use Form 2 and clearly cross out Form 1.  
Note: Your drawing does not have to be perfect. Ensure that the properties of the signal are clearly recognizable.  
s  
3  
1 1  
4 r  
ak 0.5 bk 0.5  
nt ont  
e e  
zi zi  
ﬁ ﬁ  
ef 0 ef 0  
o o  
k v k  
er er  
uri↑0.5 uri↑0.5  
o o  
F s F  
↑1 ↑1  
0 1 2 3 4 5 0 1 2 3 4 5  
g  
Harmonics Harmonics  
V Form 1 Form 2  
1 1  
u  
) )  
(t (t  
s s  
e e  
d d  
u u  
plit 0s plit 0  
m m  
a a  
al al  
ön n  
g g  
Si Si  
↑1 ↑1  
L  
0 0.5 1 0 0.5 1  
Time [s] Time [s]  
Information content and entropy: A memoryless source emits symbols x↑X, expressed by ZVX:  
Information content of x↑X: I(x)=→log2(Pr[X=x])  
!  
Entropy of the source: H(X)=→ Pr[X=x]log2(Pr[X=x])  
x↑X  
Fourier series: Angular frequency ε=2ϑ/T  
a !↓ 2" T/2 2" T/2  
s(t)= 20+ akcos(kεt)+bksin(kεt) with ak=T s(t)cos(kεt)dt, bk=T s(t)sin(kεt)dt.  
k=1 ↔T/2 ↔T/2  
Channel coding: Example block codes: A block of length k bits is mapped to n-bit long channel words (n>k). For each channel word, (depending on the code) m<n→k bits can be corrected.  
k n Code rate: R=k/n  
x C x→  
–Page 2/2–