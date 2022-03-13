import time
a=input("enter a:")
b=input("enter b:")
print(f"before conversion: a={a},b={b}")
try:
    a=float(a)
    b=float(b)
    time.sleep(50)# this stops the execution 2 seconds
    print(f"after conversion: a={a},b={b}")
    res=a/b
    print("result:",res)
except ZeroDivisionError as err:
    print("ERROR:",err)
    print("not expected zero value to b")
except ValueError as err:
    print("Error:",err)
    print("Enter 0-9 values, not expected alphabets")
except Exception as err:
    print("ERROR: %s"%err)
except:
    print("THIS IS EXCEPT")
print("End")
