x=int(input('enter first number'))
y=int(input('enter second number'))
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x%y

print("Add:", add(x,y))
print("Subtract:", subtract(x,y))
print("Product:",multiplication(x,y))
print("Remainder",division(x,y))
