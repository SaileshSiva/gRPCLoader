import grpc
from concurrent import futures
import time

# import generated classes
import loaderConnector_pb2
import loaderConnector_pb2_grpc

#import python file loads models
import calculator

class ModelLoaderServicer(loaderConnector_pb2_grpc.LoaderConnectorServicer):
    def ModelLoader(self, request, context):
        reading1 = getattr(request, 'reading1')
        reading2 = getattr(request, 'reading2')

        #addition and subraction
        output1 = calculator.doAdd(reading1, reading2)
        output2 = calculator.doSub(reading1, reading2)

        #create response and set the attributes
        response = loaderConnector_pb2.OutputReading()
        setattr(response, 'firstOutput', output1)
        setattr(response, 'secondOutput', output2)
        return response

#create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


loaderConnector_pb2_grpc.add_LoaderConnectorServicer_to_server(
    ModelLoaderServicer(), server)

#listen the server on port 50055
print('Starting server. Listening on port 50055.')
server.add_insecure_port('[::]:50055')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
