# import f1, f2
# print(f1.x)
# print(f1.y)
# f1.fun()
# print(f2.x)
# print(f2.y)
# f2.fun()

#import f1
#print(f1.x)
#import f2 
#print(f2.x)
#from f2 import x
#print(x)
import f2
# if we import any file, it's going execute __pycace__/filename.compilename-version.pyc file.
# it has to take decission to create compile file or not.
#1. it checks in __pycace__/filename.compilename-version.pyc file available or not.
#if not 
#       it will create the file and execute it.
#else
#         it will check the modified date and time of .py and .pyc files
#         if modifed date and time of .py > .pyc file.
#                     it will recompile the .py file and execute the newly created pyc file.
#         else:
#          	it will execute the existing compiled file. 
print(f2.x) 
import f1
print(f1.x)
