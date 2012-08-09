'''
Created on 02/giu/2012

@author: fede
'''
'''
First In First Out (FIFO) which simply queues processes in the order that they arrive in the ready queue.
Round-Robin which assigns a fixed time unit per process, called CPU quantum, and cycles through them until 
the termination
Let us consider a single CPU computer with a list of process to schedule. The goal of the exercise is to 
implement a naive scheduler class whose instances will model and simulates the scheduler work with a given 
scheduling algorithm and a list of processes in the ready queue. A process is characterized by a name, 
the time of arrival in the ready queue (a non negative integer) and how long it lasts. Each process has 
only one operation (named run) which simply prints the process name, process execution is represented by 
the execution of this operation: every time the process get the CPU it class run(). Note that the time 
of arrival is necessary to implement the FIFO scheduling algorithm whereas how long the process last is 
necessary to the round-robin algorithm. Process are all in the queue at beginning even if they have different 
arrival time. The class implementing the FIFO algorithm will hardwire the CPU quantum.

The assignment solution should include the scheduler class, two classes respectively representing the FIFO 
(named `` fifo``) and round-robin (named round_robin) scheduling algorithms and the process class. 
Note that, the easiest way to realize the two scheduling algorithms is to use iterators.
'''

class scheduler:
    def __init__(self,lista,name):
        self.lista = lista
        self.name  = name
    
    def scheduling(self):
        if self.name==fifo:
            for i in fifo(self.lista):
                i.run()
        elif self.name==round_robin:
            for j in round_robin(self.lista):
                j.run()

class process:
    def __init__(self,name,t_s,t_a=0):
        self.name = name
        self.t_a = t_a
        self.t_s = t_s
    
    def run(self):
        print(self.name,self.t_a,self.t_s)

class fifo:
    def __init__(self,lista):
        self.lista=sorted(lista, key = lambda x: x.t_a)
    
    def __iter__(self):
        self.c = 0
        return self
    
    def __next__(self):
        if self.c == len(self.lista): raise StopIteration
        self.c +=1
        return self.lista[self.c-1]
        

class round_robin:
    def __init__(self,lista):
        self.lista=lista
    
    def __iter__(self):
        self.cpu = 5
        return self
    
    def __next__(self):
        if not self.lista : raise StopIteration
        rr = self.lista.pop(0)    
        if rr.t_s <= self.cpu :
            return rr 
        rr.t_s -= self.cpu       
        self.lista.append(rr)
        return rr

if __name__ == "__main__": 
    pl = [process("one", 10), process("two", 3, 5), process("three", 15), \
    process("four", 30, 5), process("five", 10), process("six", 6, 10), process("seven", 10), process("eight", 25, 5)]
    print("fifo scheduling") 
    s = scheduler(pl, fifo) 
    s.scheduling() 
    print("round-robin scheduling") 
    s = scheduler(pl, round_robin) 
    s.scheduling()