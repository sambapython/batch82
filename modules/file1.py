print("this is file1")
x=1000
y=2000
z=x+y
def fun():
	print("hello")


"""
RAM
stack    heap
fun---------<fun.main>
"""

"""
when we execute this file.
the main thread allocated to execute this file.
it will go with below memory managment
stack                  heap


fun----------------> <fun.main>

after the file execution completed. the main thread going to close.
While the main thread going to close, it will remove all the memory created by this thread.
i.e it will remove fun reference and <funa.main> object from memory.
"""