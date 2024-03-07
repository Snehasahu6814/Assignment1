"""IMporting counter to create a dictionary"""
from collections import Counter
import time
def log_execution_time(func):
    """log exceution"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        with open("execution_logs.txt", "a",encoding="utf-8") as f:
            f.write(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds\n")
        return result
    return wrapper
@log_execution_time
def stringoccurence(string):
    """Function to check the Occurence of the String"""
    charcount=Counter(string)
    # print(charcount.items())
    sort=sorted(charcount.items(),key=lambda x: (-x[1],x[0]))
    # print(sort)
    for i,s in sort[:3]:
        print(f"{i}:{s}")
string="HAPPIESTMINDS"
stringoccurence(string)
