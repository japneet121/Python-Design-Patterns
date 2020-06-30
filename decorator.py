'''
Decorator pattern is used when we want to extend the fucntionality of a function of we want to perform some steps before or after a function call.
'''



def add_suffix(func):
    def inner(name):
        print("Mr.",end=' ')
        func(name)
    return inner

@add_suffix
def print_name(name):
    print(name)


print_name("Japneet")
