'''
Created on 07/apr/2012

@author: fede
'''
def getTalk(type="shout"):
    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize()+"!"

    def whisper(word="yes") :
        return word.lower()+"..."
    # Then we return one of them
    if type == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        return shout  
    else:
        return whisper
# How do you use this strange beast?
# Get the function and assign it to a variable
talk = getTalk()      
# You can see that "talk" is here a function object:
print(talk)
# The object is the one returned by the function:
print(talk())
# And you can even use it directly if you feel wild:
print(getTalk("whisper")())

def doBefore(funz):
    print('prima')
    print(funz())

doBefore(talk)


