import pickle

data = {
    'number': 123345,
    'text': 'hello world',
    'something': 1.234345345
}

print("HELLO FROM dump_data.py", data)
f = open('data.p', 'wb')

pickle.dump(data, f)