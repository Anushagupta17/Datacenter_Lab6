from concurrent import futures
import time
import logging
from PIL import Image
import io

import grpc

import service1_pb2
import service1_pb2_grpc


def add(x, y):
    return x+y


def img_dim(data):
    ioBuffer = io.BytesIO(data)
    img = Image.open(ioBuffer)
    return img.size[0], img.size[1]


class Service1Servicer(service1_pb2_grpc.Service1Servicer):

    def AddNumbers(self, request, context):
        response = service1_pb2.Result()
        response.z = add(request.x, request.y)
        return response

    def ProcessImg(self, request, context):
        response = service1_pb2.ImgOutput()
        response.width, response.height = img_dim(request.img)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service1_pb2_grpc.add_Service1Servicer_to_server(
        Service1Servicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    # since server.start() will not block,
    # a sleep-loop is added to keep alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()