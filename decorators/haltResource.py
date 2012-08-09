'''
Created on 01/giu/2012

@author: fede
The exercise consists of implementing a decorator that fixed a number of admissible steps (resources) 
will stop the computation when the used steps overcome the available resources. In our case, the 
resource limiter will have a course grain since it is quite hard to count the execution of a single 
statement through a decorator but quite easy to count the function/method calls.
'''

def deco(f):
    def wrapper(*args):
        global resource
        if resource == 0:
            print('resource run out')
            exit()
        else:
            resource -=1
            return f(*args)
    return wrapper


@deco   
def fibo(a):
    return a if a<=1 else fibo(a-1)+fibo(a-2)

@deco
def fact(a):
    return 1 if a<=1 else fact(a-1)*a

if __name__ == "__main__":
    resource = 10
    print("{0}! :- {1}".format(10,fact(10))) 
    resource = 9
    try:
        print("{0}! :- {1}".format(10,fact(10))) 
    except SystemExit: pass
    resource = 160
    try:
        print("fibo({0}) :- {1}".format(10,fibo(10))) 
    except SystemExit: pass
    resource = 177
    print("fibo({0}) :- {1}".format(10,fibo(10)))
