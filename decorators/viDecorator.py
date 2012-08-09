'''
Created on 01/giu/2012

@author: fede
As you can imagine in the previous exercise, to debug the editor class is not easy. 
In particular is difficult to find out which operation has changed the text and where the 
cursor is in any moment. To this respect write a decorator debug (to be applied to the editor 
class of the previous exercise) that, when you print the line of text prints also who has performed 
the operation and where the cursor is as in the following example.
'''
from viEditor import *

def deco(aClass):
    class wrapper:
        def __init__(self,*args,**kwargs):
            self.wrapped=aClass(*args,**kwargs)
            self.command='p'
        
        def __getattr__(self,attrname):
            self.command=attrname
            #print(self.command, self.wrapped.pos,self.wrapped.__str__())
            return getattr(self.wrapped,attrname)
        
        def __str__(self):
            return '{} {} :- {}'.format(self.command,self.wrapped.pos,self.wrapped.__str__())
       
    return wrapper

editor=deco(editor)

if __name__ == "__main__":
    ed = editor()
    print(ed)
    ed.x()
    print(ed)
    ed.dw()
    print(ed)
    ed.i('a')
    print(ed)
    ed.x()
    print(ed)
    ed.i('a')
    print(ed)
    ed.i('b')
    print(ed)
    ed.i('c')
    print(ed)
    ed.h()
    ed.dw()
    print(ed)
    ed.iw(" ...")
    print(ed)
    ed.i('z')
    print(ed)
    ed.h(5)
    print(ed)
    ed.x()
    print(ed)
    ed.iw("(Z) ... 1 2 3")
    print(ed)
    ed.iw("Supercalifragilisticexpialidocious")
    print(ed)
    ed.h(len("Supercalifragilisticexpialidocious")+1)
    ed.i('X')
    print(ed)
    ed.l(len("Supercalifragilistic")+1)
    print(ed)
    ed.dw()
    print(ed)