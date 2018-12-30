import json

data = {
    'number': 123345,
    'text': 'hello world',
    'something': 1.234345345,
    'none-obj': None,
    'true value': True,
    'false-val': False,
    'nested':  {
        'number': 123345,
        'text': 'hello world',
        'something': 1.234345345,
        'none-obj': None,
        'true value': True,
        'false-val': False,
        'nested': {
            'number': 123345,
            'text': 'hello world',
            'something': 1.234345345,
            'none-obj': None,
            'true value': True,
            'false-val': False
        }
    }
}

f = open('data.json', 'w')
json.dump(data, f)
print("HELLO FROM dump_data.py", data)
