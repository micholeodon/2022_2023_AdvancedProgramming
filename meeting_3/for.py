for litera in "Kognitywiści to my!":
    print(litera)


for litera in "Kognitywiści to my!":
    print(litera, end="")
#print()

lista = [2.3, 1, -7, True, "Bo", complex(1,8)]

for el in lista:
    print(el)

x = range(1,5)
print(x[-1]) # sprawdzamy ostatni element

print()
print()



for el in range(10,20):
    print(el)

print()

for el in range(10,20,3): # mozemy ustalic sobie dowolny skok
    print(el)

print()

for el in range(20,10,-3): # mozemy zliczac w dol
    print(el)

print()


# podwojna petla
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for col in row:
        print(col)



