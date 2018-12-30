import pickle

f = open('data.p', 'rb')
data = pickle.load(f)

print("HELLO FROM load_data.py", data)