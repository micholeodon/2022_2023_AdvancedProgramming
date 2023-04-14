# LIST COMPREHENSION
# Składnia:
# - bez wykorzystania if-a: 
# nowaLista = [expression for item in iterable]
# - z wykorzystaniem if-a: 
# nowaLista = [expression for item in iterable if condition == True]


# Tworzenie listy BEZ wykorzystania mechanizmu "list comprehension"
lista = []
for x in range(1,11):
    if(x % 2 == 0):
        lista.append(x*x)

print("Zwyczajnie: ", lista)


# Tworzenie listy Z WYKORZYSTANIEM mechanizmu "list comprehension"
lista = [ x*x for x in range(1,11) if x%2 == 0]
print("List comprehension: ", lista)


# Wiecej przykładów:
# https://www.w3schools.com/python/python_lists_comprehension.asp


