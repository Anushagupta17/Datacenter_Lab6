import grpc

# import the generated classes
import service1_pb2
import service1_pb2_grpc
import sys
import time

ip = sys.argv[1]
endpoint_name = sys.argv[2]
iterations = int(sys.argv[3])
queries = iterations

# open a gRPC channel
channel = grpc.insecure_channel(ip + ':50051')

# create a stub (client)
stub = service1_pb2_grpc.Service1Stub(channel)

if endpoint_name == 'add':
    # create a valid request message
    numbers = service1_pb2.Numbers(x=1, y=1)
else:
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    img_data = service1_pb2.ImgInput(img=img)

start_time = time.time()
while iterations > 0:
    # make the call
    if endpoint_name == 'add':
        response = stub.AddNumbers(numbers)
        print(response.z)
    else:
        response = stub.ProcessImg(img_data)
        print(response.width, response.height)
    iterations = iterations - 1

print("Time taken = ", ((time.time() - start_time) * 1000)/queries, " millisecs")
