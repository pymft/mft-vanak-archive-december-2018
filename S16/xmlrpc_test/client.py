import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://10.10.201.12:8000/")
print("3 is even: %s" % str(proxy.is_even(3)))
print("fib" % str(proxy.fib(20)))

# logger design pattern
# mastring the art design pattern python
# packt pub