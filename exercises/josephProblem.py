'''
Created on 30/apr/2012

@author: fede
Flavius Josephus was a roman historian of Jewish origin. 
During the Jewish-Roman wars of the first century AD, 
he was in a cave with fellow soldiers, 40 men in all, surrounded by enemy Roman troops. 
They decided to commit suicide by standing in a ring and counting off each third man. 
Each man so designated was to commit suicide... Josephus, not wanting to die, 
managed to place himself in the position of the last survivor.

In the general version of the problem, there are n Hebrews numbered from 1 to n 
and each k-th Hebrew will be eliminated. The count starts from the first Hebrew. 
What is the number of the last survivor?

The exercise consists of implementing a solution for the general version of the Josephs Problem 
The following are a possible main for the solution and a trace of its execution.
'''
import time
def contatempo(func): 
    def interna(*args,**kw): 
        start=time.time() 
        result=func(*args,**kw) 
        tempo=time.time()-start 
        print("Funzione: %s - tempo impiegato: %4.9f" % (func.__name__,tempo)) 
        return result 
    return interna  

class Hebrews2:
    def __init__(self,tot):
        self.tot = tot
        self.lista=[i for i in range(1,self.tot+1)]
    @contatempo
    def who_is_joseph(self,num):
        k=0
        appoggio=[]
        for i in self.lista:
            k+=1
            if k == num:
                k=0
                appoggio.append(i)
            else:
                self.lista.append(i)
            if len(appoggio)==self.tot:
                return 'In a circle of {} people, killing number {}\nJoseph is the Hebrew in position {}'.\
                    format(self.tot,num,i)            

#import sys
if __name__=="__main__":
    suicides2 = Hebrews2(40000)
    print(suicides2.who_is_joseph(30))
    suicides3 = Hebrews2(5000)
    print(suicides3.who_is_joseph(7))
    suicides4 = Hebrews2(5000)
    print(suicides4.who_is_joseph(153))
    suicides3 = Hebrews2(40)
    print(suicides3.who_is_joseph(3))