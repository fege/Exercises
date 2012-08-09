'''
Created on 18/apr/2012

@author: fede

Given a boolean expression f with n unknowns write a function pretty(f, n) 
that pretty prints the table of truth for the given expression.

Note, solutions that use itertools are considered wrong, decorators, 
recursion, generators and iterators are allowed and suggested.

The following is a possible main with its execution

'''

def pretty(f,r):
    for i in range(2**r):
        for i in converti(i,r):
            print('{}:- {}'.format(i, f(*i)))

def converti(num,r):
    lista=[]
    while num > 0:
        lista.insert(0,num%2)
        num >>= 1
    a=[0]*(r-len(lista))+lista
    yield a




if __name__ == "__main__":
    f0 = lambda x: 1-x
    f1 = lambda x,y: x&y
    f2 = lambda x,y: x|y
    f3 = lambda x,y,z: (x&y)|(x&z)
    f4 = lambda x1,x2,x3,x4,x5,x6,x7: f1(f0(x1),x2)| \
    (f2(x3,f0(x4))&x5)|f3(x5,x6,x7)
    pretty(f0, 1)
    pretty(f1, 2)
    pretty(f2, 2)
    pretty(f3, 3)
    pretty(f4, 7)