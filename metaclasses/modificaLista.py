'''
Created on 13/mag/2012

@author: fede
'''
def setItemMio(obj,key,item):
    obj.insert(key,round(item))

def appendMio(obj,item):
    obj.insert(len(obj),round(item))

def sortMio(obj):
    print('SORT')

class metacl(type):
    def __new__(meta,classname,supers,classdict):
        classdict['__setitem__'] = setItemMio
        classdict['append'] = appendMio
        classdict['sort'] = sortMio
        return type.__new__(meta,classname,supers,classdict)
           
class list(list, metaclass = metacl): pass

if __name__ == "__main__":
    print(list.__dict__)
    print(dir(list))
    l=list()
    l[0]=1.7
    l[1]=1.3
    print(l)
    l.append(7.3)
    l.sort()
    print(l)