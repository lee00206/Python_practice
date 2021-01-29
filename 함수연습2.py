x = 1

def f1():
    x = 2
    print(x)

def increase():
    global x
    x = x + 1
    print(x)

increase()
f1()
print(x)

