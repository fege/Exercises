'''
Created on 23/set/2011

@author: fede
'''
class Person:
    def __init__(self,n,c,e):
        self.nome=n
        self.cognome=c
        self.eta=e
    
    def n_eta(self,a):
        self.eta=int(self.eta)+a
        return(self.eta)
    
    def __str__(self):
        return "il mio nome e' {0} cognome {1} eta' {2} ".format(self.nome,self.cognome,self.eta)
    
'''if __name__ == "__main__":
    persona=Person("andrea","tizio","15")
    print(persona)
    persona.n_eta(3)
    print(persona)'''