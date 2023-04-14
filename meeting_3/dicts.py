dict = {"pn":1, "wt":2, "sr":3}

print(dict.keys())
print(dict.values())
print(dict.items())


for sth in dict.keys():
    print(sth)

for sth in dict.values():
    print(sth)

for sth in dict.items():
    print(sth)
    print(type(sth))


for k,v in dict.items():
    print("klucz:" + k)
    print("wartosc:" + str(v))

