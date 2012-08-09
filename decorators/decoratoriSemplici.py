'''
Created on 08/apr/2012

@author: fede
'''
def primo(funz):
    def wrapper():
        print('ciao')
        funz()
        print('cioa2')
    return wrapper

def secondo(funz):
    def wrapper():
        print('hola')
        funz()
        print('bye')
    return wrapper

def funz_da_deco(par='goodbye'):
    print(par)

funz_da_deco=primo(secondo(funz_da_deco))
funz_da_deco()

@secondo
@primo
def funz_da_deco2(par='GIGI'):
    print(par)

funz_da_deco2()



def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("I change args! Look:", arg1, arg2)
        arg1=arg1.upper()
        arg2='B'+arg2[1:]
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

# Since when you are calling the function returned by the decorator, you are
# calling the wrapper, passing arguments to it, will let it pass them to 
# the decorated function

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("My name is", first_name, last_name)

print_full_name("Peter", "Venkman")
