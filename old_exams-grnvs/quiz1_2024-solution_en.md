Chair of Network Architectures and Services  
School of Computation, Information and Technology  
Technical University of Munich  

Confirmation of Conduct Rules  
I hereby assure that I will solve this exam exclusively using the resources listed below and submit it under my name.  
Sticker will be generated  
Signature or full name, if no pen input is available  

Fundamentals of Computer Networks and Distributed Systems  
Exam: IN0010/Quiz1 Date: Monday, May 13, 2024  
Examiner: Prof. Dr.-Ing. Georg Carle Time: 19:00–19:15  

Do not forget to confirm the conduct rules (see above) by signing or entering your name (if no pen input is available). Submissions without confirmation will not be graded.  

Instructions for Processing  
- This exam consists of 6 pages with a total of 2 tasks. Please check now that you have received a complete set of information.  
- The total score for this exam is 16 points.  
- It is prohibited to tear pages from the exam.  
- The following resources are allowed:  
  - everything except group work, plagiarism, and any form of AI (e.g., ChatGPT)  
- Tasks marked with * can be solved without knowledge of the results of previous sub-tasks.  
- Only those results will be graded where the solution path is recognizable. Text tasks must generally be justified unless explicitly stated otherwise in the respective sub-tasks.  
- Always answer free-text tasks in your own words. Foreign or copied answers will not be accepted.  
- Violations of the conduct rules will lead to exclusion from the bonus procedure.  
- Do not write with red/green colors or with pencil.  

---  

**Task 1**  
Multiple Choice (9 Points)  
The following tasks are multiple choice/multiple answer, meaning at least one answer option is correct for each.  
Sub-tasks with only one correct answer will be graded with 1 point if correct. Sub-tasks with more than one correct answer will be graded with 1 point for each correct answer and 1 point for each incorrect mark. Missing marks have no effect. The minimum score per sub-task is 0 points.  

Mark the correct answers  
Correct marks can be crossed out by complete filling.  
Crossed-out answers can be marked next to be re-checked.  

a) In which step of message transmission can a lossless (de-)compression method be meaningfully used?  
- Detection  
- Channel decoding  
- Modulation  
- Source encoding  
- Demodulation  
- Channel coding  
- In no step  
- Source decoding  
- Line coding  

b) What is the SNR if a power of 15 mW is transmitted and a noise power of 10 µW is measured?  
- 31.761 dB  
- 1500  
- 28.239 dB  
- 666.67  
- 1500  

c) What codeword length is at least required to quantize values in the interval I = [90;270] with a step size of a maximum of 0.5?  
- 7 bit  
- 1 bit  
- 8 bit  
- 9 bit  
- 360 bit  
- 180 bit  

d) What is the first signal level if a uniformly distributed signal in the interval I = [14;18] is to be quantized with 8 levels and minimal quantization errors?  
- 13.750  
- 13.250  
- 16.000  
- 14.250  
- 14.125  
- 14.000  

e) With which method could the following signal have been modulated?  
- SAK  
- AQM  
- FDM  
- KSP  
- PSK  
- QAM  
- ASK  
- LMU  

f) A source emits symbols from the alphabet = “Ψ”. What is the entropy of the source?  
- ∞  
- 2 bit  
- 1 bit  
- another value  
- 0 bit  

---  

In the following, we consider a layered model that represents the control of a digital German ticket. Layer 1 models the generation of an Aztec code from digital ticket data or the reading of the ticket data.  

g) What type of communication is involved in the control of the code?  
- Bidirectional communication  
- Unidirectional communication  
- Nondirectional communication  
- Tridirectional communication  

1 An Aztec code is a two-dimensional code similar to a QR or Data Matrix code.  

---  

**Task 2**  
Short Tasks (7 Points)  
The following sub-tasks can be solved independently of each other.  

0 a) Given the periodic time signal s(t) below. Here, ω = 2π, with T = 1 s. Draw the spectrum corresponding to s(t) including null points.  

b) Briefly describe in your own words what is meant by clock recovery.  
Clock recovery line codes allow the clock to be read from a received signal through forced level changes. This ensures that long sequences of identical bits can be reliably recognized.  

c) Name a clock recovery line code.  
Clock recovery line codes include the Manchester code and the Return-To-Zero code.  

You have the right to transmit on the frequency band from 2347 MHz to 2385 MHz at the Federal Network Agency. Now you have modulated a signal with 2-ASK onto a carrier frequency of 2366 MHz and obtained the following signal s(t):  

The signal s(t) does not fit the channel and should never be sent.  

d) What must you do with the signal to be able to send it over the channel? Justify why this is necessary.  
Note: Pay particular attention to the jumps in the signal.  
Due to the jumps and bends in s(t), the signal has many high-frequency components (thus it has a wide spectrum). Since the assigned frequency band is narrower than the spectrum of the signal, the modulated signal should be band-filtered before sending. This ensures that it does not exceed the given frequency band.  

---  

Additional space for solutions. Clearly mark the assignment to each sub-task. Do not forget to cross out invalid solutions.