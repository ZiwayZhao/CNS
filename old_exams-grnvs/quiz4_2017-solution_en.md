Chair for Network Architectures and Network Services  
Faculty of Computer Science  
Technical University of Munich  
__ __ __ __ __ __ __ __  
0  
1 Signature  
2 g  
3  
4  
5  
a  
6 Notes on Personalization:  
7 Please mark your student ID (with leading zero). This will be processed automatically in the designated signature field.  
Instructions for completion:  
- Please use a blue or black ballpoint pen to fill out.  
- Do not use red or green ink and no pencils.  
- No aids are allowed.  
  
Check the box Do not check again  
Cross out Color the field but do not press through  
→  
Re-check no automatic detection Insight  
s  
a) Under the term "stream-oriented" one understands...  
Transmission of data with message boundaries. Transmission technology based on electrical current.  
×  
Transmission of messages of fixed length. Transmission of data without message boundaries.  
n  
b) The transport layer is in the ISO/OSI model layer...  
×  
1. 8. 4. 7. 2. 6. 3. 5.  
u  
c) Flow control aims to...  
×  
Confirm connections. Not overload the receiver.  
Not overload the network. None of the above.  
ö  
Maximize the data rate. Detect message loss.  
d) Congestion control aims to...  
×  
Not overload the network. Confirm connections.  
Detect message loss. None of the above.  
×  
Maximize the data rate. Not overload the receiver.  
e) Which statements about TCP are correct?  
×  
Acknowledgments give the segment number. TCP interprets segment loss always as a result of congestion situations in the network.  
TCP is the only datagram-oriented protocol. ×  
TCP acknowledges transmitted data per byte.  
f) Which statements about TCP are correct (#2)?  
×  
TCP is connection-oriented. TCP encrypts communication.  
TCP authenticates the communication partners. TCP operates according to the "Best Effort" principle.  
–Page 1/2–  
g) The path MTU is 1500 bytes. IPv4 is used at layer 3. How large should the MSS be chosen?  
×  
1452 bytes 1520 bytes 1540 bytes 1500 bytes 1460 bytes 1480 bytes  
h) Which statements about the Slow Start of TCP Reno are correct?  
×  
The send window is increased by 1/MSS for each acknowledged segment. The send window is increased by 1 MSS for each acknowledged segment.  
× × g  
The send window increases exponentially. The size of the send window is doubled with each fully acknowledged send window.  
a  
i) The syscall select()...  
×  
blocks until at least one socket is ready or selects a socket for transmission.  
(if specified) a timeout occurs.  
is only useful for TCP sockets.  
creates a new socket. ×  
monitors a set of sockets.  
c  
j) Which of the specified addresses are private IPv4 addresses?  
× × ×  
172.20.16.1 192.168.255.0 10.10.10.10  
s  
×  
172.16.20.1 192.169.1.1 127.0.0.1  
r  
k) What is meant by an ephemeral port?  
×  
A temporarily, randomly chosen port. o Any port greater than 1023.  
Any port less than 1024. The destination port of a specific protocol at the application layer, e.g., HTTP.  
l) Which statements about NAT are correct?  
s ×  
NAT can translate TCP ports into UDP ports. NAT replaces the source IP of outgoing packets.  
×  
NAT replaces the destination IP of outgoing data packets. NAT replaces the destination IP of incoming packets.  
NAT offers a high degree of protection against unauthorized access. NAT replaces the source IP of incoming packets.  
n  
m) Which statements about NAT in relation to ICMP are correct?  
×  
ICMP does not use port numbers. The ICMP ID can be used instead of port numbers, which is why there are no problems with ICMP.  
Depending on the respective type of an ICMP packet, different mechanisms for address translation may need to be used. Not all NAT implementations fully support ICMP.  
ö ICMP may not be supported by NAT.  
n) What is meant by port forwarding?  
L × ×  
A technique that allows, for example, to operate a web server behind a NAT. A manual entry in the NAT table for forwarding specific incoming packets to a private IP address/port number.  
A dynamically generated entry in the NAT table.  
None of the above.  
o) Which information is essential for the basic functionality of a simple NAT?  
×  
Source IP of outgoing packets Source port of incoming packets  
Source IP of incoming packets Destination IP of outgoing packets  
×  
Source port of outgoing packets Destination IP of incoming packets  
×  
Destination port of incoming packets Destination port of outgoing packets  
–Page 2/3–