'''
Created on 11/apr/2012

@author: fede
Often objects during their life cycle evolves sometimes changing their interface. 
Stack clearly shows this point: initially the stack is empty and pop() operation 
is unacceptable and similarly when it is full it cannot accept push() operations. 
Another example is Person that grows to a Student (with the method average()) and 
then to a Worker (with the method salary()).

Normally an object begins with a type and cannot change it without a complete 
re-instantiation. Python being a dynamic language is a little bit more flexible 
and permits to have instances of the same class that accept different messages, 
such as empty and full stacks.

The exercise consists of writing a metaclass Skin that provides an object with 
the method become() that receives two sets of methods to be added to and to be 
removed from the object respectively. The following shows the expected behavior 
for a stack whose methods pop() and push() are added/removed when acceptable/unacceptable.
'''
def become(self, adds, removes):
    import types
    for x in adds:
        print(x)
        self.__dict__[x.__name__] = types.MethodType(x, self)
    for x in removes:
        try:
            del self.__dict__[x.__name__]
        except KeyError: pass

def push(self,v):
    self.top+=1
    self.dat+=[v]

def pop(self):
    top=self.dat[-1]
    self.dat=self.dat[:-1]
    self.top-=1
    return top

class Skin(type):
    def __new__(cls,classname,supers,classdict):
        classdict['become']=become
        return type.__new__(cls,classname,supers,classdict)

class stack(metaclass=Skin):
    def __init__(self,dim):
        self.dim = dim
        self.top = 0
        self.dat = []
    
    def is_empty(self):
        if self.top == 0:
            return True
        return False
    
    def is_full(self):
        if self.top == self.dim-1:
            return True
        return False
    
    def __str__(self):
        return "Stack top :- {0} Stack dim :- {1} Stack data :- {2}".format(self.top, self.dim, self.dat)        

if __name__ == "__main__":
    s = stack(5) # 5 is the stack dimension
    print(s)
    trend = True
    for i in range(-1,14):
        if s.is_empty():
            s.become({push}, {pop})
            trend = True
        elif s.is_full():
            s.become({pop}, {push})
            trend = False
        s.push(i) if trend else s.pop()
        print(s)
    print(s.__dict__)
