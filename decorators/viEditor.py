'''
Created on 23/set/2011

@author: fede
In particular you have to implement a class editor representing a line of text 
'''
class editor:
    def __init__(self):
        self.stringa=''
        self.pos=-1
    def __str__(self):
        return self.stringa
    
    def x(self):
        '''x which deletes the character under the cursor (does nothing if no characters are present) 
and move the cursor on the character on the right if present otherwise back of one;'''

        self.stringa=self.stringa[:self.pos]+self.stringa[self.pos+1:]
        self.pos=min (self.pos,len(self.stringa)-1)
        return self.stringa
    
    def dw(self):
        '''dw which deletes from the character under the cursor (included) to the next space (excluded) 
or to the end of the line and moves the cursor on the character on the right if any or backwards otherwise;'''
        posiz = self.stringa[self.pos:].find(" ") if (" " in self.stringa[self.pos:]) else len(self.stringa[self.pos:]) 
        self.stringa=self.stringa[:self.pos]+self.stringa[self.pos+posiz:]
        self.pos = min (self.pos, len(self.stringa) -1)
        return self.stringa
        
    
    def iw(self,w):
        '''iw which adds a word w followed by a blank space after the character under the 
cursor and moves the cursor under the blank space'''
        self.stringa=self.stringa[:self.pos+1]+w+' '+self.stringa[self.pos+1:]
        self.pos=self.pos+len(w)+1
    
    def i(self,c):
        '''i which adds a character c after the character under the cursor and moves the cursor under c'''
        self.stringa=self.stringa[:self.pos+1]+c+self.stringa[self.pos+1:]
        self.pos=self.pos+len(c)
        return self.stringa
    
    def h(self,n=1):
        '''h which moves the cursor n (1 as default, i.e., when nothing is specified) 
character on the left from the current position'''
        self.pos-=n
    def l(self,n=1):
        '''l which moves the cursor n (1 as default, i.e., when nothing is specified) 
characters on the right from the current position'''
        self.pos+=n