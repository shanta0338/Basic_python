#x = dict(input().split() for _ in range(4))
#print(x)

y = {}
for _ in range(2):
    key = input()
    value = input()
    y[key] = value
y['university'] = 'Daffodil international university'
print(y)
del y['roll']
print(y)