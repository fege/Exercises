'''
Created on 04/mag/2012

@author: fede
Traditionally python has some limitations towards the support of the object-oriented concept of data hiding. 
You can't define a field that is really private also the _ provides just a palliative to the privateness based 
on name mangling but the name is still there and can be accessed without big troubles.

Normal good manners in object-oriented programming establishes that an object status should be private to 
the object itself and can be accessed only through special methods called selectors (getters and setters). 
A getter grants the access to the content of a given field and the corresponding setter permits to modify 
its content.

The exercise consists of providing a mechanism based on two decorators: @private, @selectors. 
The @private decorator permits to list the names (both fields and methods) that should be made private 
whereas the @selectors decorator permits to specify which selectors to create (a dictionary of fields 
indexed on 'get' and 'set' is passed to the decorator). Note that a selector can be created only for 
private fields defined by the @private decorator. Of course selector are created dynamically and not 
written by the programmer and their name is after the name of the field, e.g., if x is the private field, 
the getter is named getX and the setter setX with the first letter of the attributed replaced by the 
corresponding capital letter.

'''

def getter_builder(self,name):
    getter_name='get'+name
    
    def getter():
        return getattr(self, name.lower()) 
    
    self.__dict__[getter_name] = getter

def setter_builder(self,name):
    setter_name='set'+name
    
    def setter(value):
        return setattr(self, name.lower(), value)
    
    self.__dict__[setter_name] = setter

def private(*privates):
    def onDecorator(aClass):
        class privateInstance:
            def __init__(self,*args,**kargs):
                self.wrapped = aClass(*args,**kargs)
                self.privates = privates
            def __getattr__(self,attr):
                if attr in privates:
                    raise TypeError('private attribute fetch :' +attr)
                else:
                    return getattr(self.wrapped , attr)
            def __setattr__(self, attr, value):
                if attr == 'wrapped' or attr == 'privates':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError("private attribute change: "+attr)
                else:
                    return setattr(self.wrapped, attr, value)    
        return privateInstance
    return onDecorator

def selectors(*sel):
    def onDecorator(aClass):
        class selInstance:
            def __init__(self,*args,**kargs):
                self.selector = aClass(*args,**kargs)
                
                for i in sel[0].keys():
                    for k in sel[0][i]:
                        if k in self.privates:
                            valore=k[0].upper()+k[1:]
                            if i == 'get':
                                getter_builder(self.selector.wrapped ,valore)
                            if i == 'set':
                                setter_builder(self.selector.wrapped, valore)
                        else: raise TypeError('attempt to add a selector for a non private attribute: ' + k)
                        
            def __getattr__(self, attr):
                return getattr(self.selector, attr)

            def __setattr__(self, attr, value):
                if attr == 'selector':
                    self.__dict__[attr] = value
                else: setattr(self.selector, attr, value)
          
        return selInstance
    return onDecorator

@selectors({'get': ['data','size'], 'set':['data', 'label']})
@private('data', 'size')
class E:
    def __init__(self, label, start):
        self.label = label
        self.data = start
        self.size = len(self.data)
        
@selectors({'get': ['data','size'], 'set':['data', 'label']})
@private('data', 'size', 'label')
class D:
    def __init__(self, label, start):
        self.label = label
        self.data = start
        self.size = len(self.data)
    def double(self):
        for i in range(self.size):
            self.data[i] = self.data[i] * 2
    def display(self):
        print('{0} => {1}'.format(self.label, self.data))
        
if __name__ == "__main__":
    try:
        Y = E('Wrong Label', ['a', 'b'])
    except Exception as e: print("{0}: {1}".format(type(e).__name__, e))
    X = D('X is', [1, 2, 3])
    X.display(); X.double(); X.display()
    try:
        print(X.size)
    except Exception as e: print("{0}: {1}".format(type(e).__name__, e))
    try:
        print(X.data)
    except Exception as e: print("{0}: {1}".format(type(e).__name__, e))
    print(X.getData())
    X.setData([25])
    print(X.getSize())
    try:
        X.setSize(25)
    except Exception as e: print("{0}: {1}".format(type(e).__name__, e))
    try:
        print(X.getLabel())
    except Exception as e: print("{0}: {1}".format(type(e).__name__, e))
    X.setLabel('It has worked!!!')
    X.display()