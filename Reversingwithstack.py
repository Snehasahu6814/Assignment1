"""IMporting time to log the execution time  """
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
def reversestack(string):
    """Function  to  reverse the String using Stack """
    text=string.split()
    stack=[]
    for i in range (0,len(text)):
        stack.append(text[i])
        print('Reversed String is :')
    for i in range(0,len(text)):
            print(stack.pop(),end=" ")
str1=input("Enter a String : ")
reversestack(str1)
