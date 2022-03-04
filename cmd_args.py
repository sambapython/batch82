import sys
print(sys.argv)
print(sys.argv[1:])
data = []
for i in sys.argv[1:]:
	data.append(float(i))
print(data)
print(sum(data))