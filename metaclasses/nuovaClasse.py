'''
Created on 08/apr/2012

@author: fede
'''
MyShinyClass = type('MyShinyClass', (), {})

print(MyShinyClass)

print(MyShinyClass())

Foo = type('Foo', (), {'bar':True})
f=Foo()
print(f.bar)


FooChild = type('FooChild', (Foo,), {})
print(FooChild.bar)


def echo_bar(self):
    print('PLUTO')
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
FooChild().echo_bar()