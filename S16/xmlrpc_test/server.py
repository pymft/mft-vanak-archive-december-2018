from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
    return n % 2 == 0

def fib(n):
    if n in (1, 2):
        return 1
    else:
        a, b = 1, 1
        while n > 2:
            n-=1
            a, b = a, a+b
        return b

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.register_function(fib, "fib")
server.serve_forever()