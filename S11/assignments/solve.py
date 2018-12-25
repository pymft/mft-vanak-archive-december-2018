f = open('input.txt', 'r')
text = f.read()
m, n, c = text.split('\n')
m = int(m)   # m = 10
n = int(n)   # n = 6
f.close()

out_text = '\n'.join([c * m for i in range(n)])
f = open('output.txt', 'w')
f.write(out_text)
f.close()
