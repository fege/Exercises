'''
Created on 09/apr/2012

@author: fede
'''
class UpperAttrMetaclass(type):
 
    def __new__(meta, classname,supers, classdict):
 
        attrs = ((name, value) for name, value in classdict.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        return type.__new__(meta, classname,supers, uppercase_attr)

class Foo(metaclass=UpperAttrMetaclass):
    # we can define __metaclass__ here instead to affect only this class
    bar = 'bip'
 
print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
# Out: True
 
f = Foo()
print(f.BAR)