"""Importing time"""
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
def reversestring(string):
    """Function  to  reverse the String"""
    text=string.split()
    text=text[::-1]
    str2=" "
    print(str2.join(text))
str1=input("Enter a String : ")
reversestring(str1)
