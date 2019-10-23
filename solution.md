Collaborated with: Tanmai Gajula (taga5342@colorado.edu) \

same host  \
REST API Add Time taken =  2.69807910919  millisecs \
REST API Image Time taken =  4.89498186111  millisecs
gRPC Add ('Time taken = ', 0.5667359828948975, ' millisecs')
gRPC Image ('Time taken = ', 4.434258937835693, ' millisecs')

Different Hosts same zone : us-central1-a
REST API Add Time taken =  2.69662594795  millisecs
REST API Image Time taken =  7.30944895744  millisecs
gRPC Add ('Time taken = ', 0.571465015411377, ' millisecs')
gRPC Image ('Time taken = ', 6.90605616569519, ' millisecs')

Different zones (server - us-central1-a, client - europe-west3-a)
REST API Add Time taken =  214.918968916  millisecs
REST API Image Time taken =  902.453479052  millisecs
gRPC Add ('Time taken = ', 106.4897289276123, ' millisecs')
gRPC Image ('Time taken = ', 120.59386587142944, ' millisecs')

Network latency using ping command:
Client to server(localhost): 0.032 millisecs 
Client to server(same zone): 0.338 millisecs
Client to server(different zones): 105.5 millisecs


Observations:

According to our analysis,gRPC is faster than REST. 

Rest uses HTTP 1.1 which is sensitive to latency. A TCP handshake is required for each individual request, 
and larger numbers of requests take a significant toll on the time needed to load a page. 

RPC uses HTTP/2. The transport layer works using HTTP/2 on top of TCP/IP. It allows for lower latency 
(faster) connections that can take advantage of a single connection from client to server 
(which makes more efficient use of connection and can result in more efficient use of server resources.

HTTP/2 also supports bidirectional connectivity and asynchronous connectivity. So it is possible for the 
server to efficiently make contact with client to send messages (async response/notifications, etc..)

One of the biggest differences between REST and gRPC is the format of the payload. REST messages typically 
contain JSON. This is not a strict requirement, and in theory you can send anything as a response, but in 
practice the whole REST ecosystem—including tooling, best practices, and tutorials—is focused on JSON. 
It is safe to say that, with very few exceptions, REST APIs accept and return JSON. 
gRPC, on the other hand, accepts and returns Protobuf messages. 

From a performance point of view, Protobuf is a very efficient and packed format. JSON, on the other hand, 
is a textual format. You can compress JSON, but then you lose the benefit of a textual format that you can easily expect.






