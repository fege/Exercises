'''
Created on 30/mag/2012

@author: fede
'''

def memo(f):
    valori=dict()
    def wrap(*args):
        nonlocal valori
        if args not in valori.keys():
            valori[args]=f(*args)
        else:
            print('valore in cache {} ---> {}'.format(args,valori[args]))
        return valori[args]
    return wrap

@memo
def fibo(n):
    return n if n<=1 else fibo(n-1)+fibo(n-2)

@memo
def fact(n):
    return 1 if n==0 else fact(n-1)*n
    
@memo
def sum(n,m):
    return n if m==0 else sum(n+1,m-1)



if __name__ == "__main__":
    print("sum({0},{1}) => {2}".format(9,5,sum(9,5)))
    print("sum({0},{1}) => {2}".format(7,7,sum(7,7)))
    print("sum({0},{1}) => {2}".format(10,4,sum(10,4)))
    print("sum({0},{1}) => {2}".format(1,13,sum(1,13)))
    print("sum({0},{1}) => {2}".format(7,25,sum(7,25)))
    print("fibo({0}) => {1}".format(5,fibo(5)))
    print("fibo({0}) => {1}".format(7,fibo(7)))
    print("fibo({0}) => {1}".format(25,fibo(25)))
    print("fact({0}) => {1}".format(5,fact(5)))
    print("fact({0}) => {1}".format(7,fact(7)))
    print("fact({0}) => {1}".format(10,fact(10)))