"""Importing time to see the execution time"""
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
def fibonacci(n):
    """Function  for fibonacci Series"""
    a=0
    b=1
    if n==1:
        print(a,end=" ")
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=" ")
Number=int(input("Enter a Number "))
print("The fibonacci series of a Number is :")
fibonacci(Number)
