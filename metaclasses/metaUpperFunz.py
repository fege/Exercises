'''
Created on 09/apr/2012

@author: fede
'''
def upper_attr(future_class_name, future_class_parents, future_class_attr):

    # pick up any attribute that doesn't start with '__'
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # turn them into uppercase
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
 
    # let <code>type</code> do the class creation
    return type(future_class_name, future_class_parents, uppercase_attr)


#__metaclass__ = upper_attr # this will affect all classes in the module
 
class Foo(metaclass=upper_attr):
    # we can define __metaclass__ here instead to affect only this class
    bar = 'bip'
 
print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
# Out: True
 
f = Foo()
print(f.BAR)