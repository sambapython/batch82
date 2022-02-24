import file1
"""
The above statement execute the file1 from top to bottom
while it is executing it will create below memory

STACK          HEAP

 file1
    x-----------1000
    y-----------2000
    z-----------3000
    fun---------<main.fun>


in the stack it will create file1 frame, it will add all the refereces belongs to file1 in the file frame.

"""
print(file1.x)
print(file1.y)
import file2
"""
	The above statement execute the file1 from top to bottom
	while it is executing it will create below memory
	file2
    x-----------1000
    y-----------2000
    z-----------3000
    fun---------<main.fun>
"""
print(file2.x)
print(file2.y)