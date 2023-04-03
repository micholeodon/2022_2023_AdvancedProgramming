
print("Hi! Let's divide some numbers.")
a = float(input("Enter a: "))
b = float(input("Enter b: "))

try:
    c = a/b
    print(f"a/b = {a}/{b} = {c}")
except ZeroDivisionError as E:
    print(E)



