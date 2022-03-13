import time
import logging
# basic configuraion in the logging. the default level is warn.
# in the warn level, it wil not show info, debug messages.
# it will show error and warn messages in the warn level
#change the level
logging.basicConfig(level=logging.DEBUG, filename="log_file.txt",
    format="%(asctime)s=>%(levelname)s=>%(filename)s=>%(message)s")
#it will show, debug, info,warn,error.
a=input("enter a:")
logging.info("entered a value")
#logging.error("entered a value")

b=input("enter b:")
logging.info("enter b value")
logging.debug(f"before conversion: a={a},b={b}")
try:
    a=float(a)
    logging.info("a value converted")
    b=float(b)
    logging.info("b value converted")
    logging.debug(f"after conversion: a={a},b={b}")
    res=a/b
    print("result:",res)
    logging.debug("Result: %s"%res)
except ZeroDivisionError as err:
    logging.error("ERROR:%s",err)
    print("not expected zero value to b")
except ValueError as err:
    logging.error("ERROR:%s",err)
    print("Enter 0-9 values, not expected alphabets")
except Exception as err:
    logging.error("ERROR:%s",err)
    print("ERROR:%s",err)

except:
    logging.error("un expected error")
    print("unexpected error..")
print("End")

#info, debug,error,warn
