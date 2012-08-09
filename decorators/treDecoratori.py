'''
Created on 08/apr/2012

@author: fede
'''
def benchmark(func):
    """
    A decorator that print the time of function take
    to execute.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock()-t)
        return res
    return wrapper



def contatempo(func): 
    import time
    def interna(*args,**kw): 
        start=time.time() 
        result=func(*args,**kw) 
        tempo=time.time()-start 
        print("Funzione: %s - tempo impiegato: %4.9f" % (func.__name__,tempo)) 
        return result 
    return interna  

def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

def counter2(func):
    def wrapped(*args, **kws):
        print('Called #%i' % wrapped.count)
        wrapped.count += 1
        return func(*args, **kws)
    wrapped.count = 0
    return wrapped

@counter2
@benchmark
@logging
def reverse_string(string):
    return (string[::-1])

print(reverse_string("Able was I ere I saw Elba"))
print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))
