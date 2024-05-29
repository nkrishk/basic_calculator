import argparse

import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    parser = argparse.ArgumentParser(description='gRPC API client for basic calculator')
    parser.add_argument('--port', required=True, type=int)
    args = parser.parse_args()
    with grpc.insecure_channel(f'localhost:{args.port}') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        # Add
        response = stub.Add(calculator_pb2.TwoNumbers(num1=10, num2=5))
        print("Add: 10 + 5 =", response.value)

        # Subtract
        response = stub.Subtract(calculator_pb2.TwoNumbers(num1=10, num2=5))
        print("Subtract: 10 - 5 =", response.value)

        # Divide
        response = stub.Divide(calculator_pb2.TwoNumbers(num1=10, num2=5))
        print("Divide: 10 / 5 =", response.value)


if __name__ == '__main__':
    run()
