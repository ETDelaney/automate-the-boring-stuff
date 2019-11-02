# global versus local variables

# 1) Global scope cannot use local variables - they only exist
# in the local scope and are destroyed after

# 2) Local scope can grab from the global variables

# 3) One function's local scope cannot use variables in another local scope

# 4) Same name can be used in different scopes


# you should use pythontutor.com ...visualize

# try out these codes and see how they work:

eggs = 42

def spam():
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
    ham = 101
    eggs = 0
    
spam()
print(eggs)

# notice how there will be three eggs variables...
# global eggs, local spam eggs, and bacon eggs...
# notice how bacon eggs variable gets destroyed and never seen by spam()...
# but see spam() also does not touch the global variable

# we could override the global variable by saying global eggs, but if this
# is not given, the eggs variables will be local scopes

def spam():
    global eggs
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
    ham = 101
    eggs = 0
    
spam()
print(eggs)
