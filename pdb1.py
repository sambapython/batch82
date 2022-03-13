a=1000
b=2000
c=a+b
def fun(x,y):
	import pdb;pdb.set_trace()
	print(f"x={x}, y={y}")
	return x*y
print("hi")
res = fun(10,20)
print("result:%s"%res)
for i in range(-3,3):
	try:
		print(10/i)
	except Exception as err:
		print(err)
print("done")