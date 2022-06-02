#Use of decorators
def func():
    return 1

print(func())

s = 'Global Variable'

def func():
    a=1
    print(locals())

print(func())
print(globals()['s'])

#Scope is very important
def hello1(name = 'John'):
    return 'Hi, ' + name

print(hello1())
hi1 = hello1
del hello1
print(hi1)
print(hi1())

#New function
def hello1(name = 'John'):
    print('Hi, ' + name)

    def EisOK():
        print('Everything is ok?')
    
    def HAreY():
        print('How are you?')
    
    if name == 'John':
        return EisOK
    else:
        return HAreY
    
print(hello1)
func2 = hello1
print(func2)
print(func2())
func3 = hello1()
print(func3)
print(func3())

#Another time
def hello2():
    print('Hello!')

def another1(func):
    print('Another function inside!')

print(another1(hello2))

#Now with decorator
def new_decorator(func1):
    def inside_func():
        print("Code executed before function")
        func1()
        print("Code executed after function")
    return inside_func

def need_decorate():
    print("This function needs a decorator")

new_decorator(hello1)()

need_decorate = new_decorator(need_decorate)
need_decorate()

#A decorator takes a function and changes his behavior
@new_decorator
def need_decorate():
    print("This function needs a decorator")
