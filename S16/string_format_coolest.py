import math

for i in range(200):
    right = 30+int(20*math.sin(i/10))
    print(f"{'*':->{right}}")