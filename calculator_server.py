from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc
import argparse

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.Result(value=result)

    def Subtract(self, request, context):
        result = request.num1 - request.num2
        return calculator_pb2.Result(value=result)

    def Multiply(self, request, context):
        result = request.num1 * request.num2
        return calculator_pb2.Result(value=result)

    def Divide(self, request, context):
        if request.num2 == 0:
            context.set_details("Division by zero")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return calculator_pb2.Result()
        result = request.num1 / request.num2
        return calculator_pb2.Result(value=result)

def serve():
    parser = argparse.ArgumentParser(description='gRPC API for basic calculator')
    parser.add_argument('--port', required=True, type=int)
    args = parser.parse_args()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port(f'[::]:{args.port}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
