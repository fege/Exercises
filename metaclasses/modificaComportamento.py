'''
Created on 31/mag/2012

@author: fede
Often objects during their life cycle evolves sometimes changing their interface. 
Stack clearly shows this point: initially the stack is empty and pop() operation 
is unacceptable and similarly when it is full it cannot accept push() operations. 

Normally an object begins with a type and cannot change it without a complete 
re-instantiation. Python being a dynamic language is a little bit more flexible 
and permits to have instances of the same class that accept different messages, 
such as empty and full stacks.

The exercise consists of writing a metaclass Skin that provides an object with 
the method become() that receives two sets of methods to be added to and to be 
removed from the object respectively. The following shows the expected behavior 
for a stack whose methods pop() and push() are added/removed when acceptable/unacceptable.
'''

class Skin(type):
    def __new__(cls,classname,super,classdict):
        classdict['become']=become
        return type.__new__(cls, classname,super, classdict)
    
    '''def add(self, method):  
        self.__dict__[method.__name__] = lambda *a: method(self, *a)  
  
    def remove(self, method):  
        try:  
            del self.__dict__[method.__name__]  
        except KeyError:  
            print 'method not in class' '''    

def become(self,add,remove):
    #import types
    for a in add:
        self.__dict__[a.__name__]= lambda *c: a(self, *c)
        #types.MethodType(a, self)
    for b in remove:
        try:
            del self.__dict__[b.__name__]
        except KeyError: pass

def pop(self):
    p=self.data[-1]
    self.data=self.data[:-1]
    self.tot -=1
    return p

def push(self,a):
    self.data.append(a)
    self.tot +=1 

class stack(metaclass=Skin):
    def __init__(self,a):
        self.dimm = a
        self.tot = 0
        self.data = []
    
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def is_full(self):
        if len(self.data)+1 == self.dimm:
            return True
        else:
            return False
    
    def __str__(self):
        return 'stack top {}, stack dim {}, stack data {}'.format(self.tot,self.dimm,self.data)

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
