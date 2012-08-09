'''
Created on 08/apr/2012

@author: fede
'''
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie=0):
        lie = lie - 3 
        return method_to_decorate(self, lie)
    return wrapper


class Lucy():
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I am %s, what did you think?" % (self.age + lie))

l = Lucy()
l.sayYourAge()
