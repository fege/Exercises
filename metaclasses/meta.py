'''
Created on 23/set/2011

@author: fede
'''
from metaclassi.person import *

def deco(func):
    print('entro deco')
    count=0
    def onCall(*args,**kargs):
        nonlocal count
        count+=1
        print('chiamata numero %s' %count)
        if count ==3:
            return func(*args,**kargs)
    return onCall

class Meta(type):
    def __new__(cls,classname,super,classdict):
        print('cls',cls,'clname',classname,'super',super,'dict',classdict)
        classdict['n_eta']=deco(classdict['n_eta'])
        return type.__new__(cls,classname,super,classdict)

Perso = Meta('EWRERTER', (), dict(Person.__dict__))
       
if __name__ == "__main__":
    p=Perso('tizio','caio','3')
    print(p)
    p.n_eta(5)
    print(p)
    p.n_eta(8)
    print(p)
    p.n_eta(7)
    print(p)
    