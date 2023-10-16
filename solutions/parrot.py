text = input("Enter some text:")

print(text)

with open('parrot.txt', 'w') as file:
    file.write(text + '\n')
