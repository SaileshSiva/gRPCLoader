import grpc

#import generated classes
import loaderConnector_pb2
import loaderConnector_pb2_grpc

#open a gRPC channel
channel = grpc.insecure_channel('localhost:50055')

#create a stub/client
stub = loaderConnector_pb2_grpc.LoaderConnectorStub(channel)

#create a valid request
readings = loaderConnector_pb2.InputReading()

#set attributes for request manually
setattr(readings, 'reading1', 30)
setattr(readings, 'reading2', 20)

#make the call(request)
response = stub.ModelLoader(readings)

#checking the service
print(getattr(response, 'firstOutput'))
print(getattr(response, 'secondOutput'))
