item = 0
while item < 3:
    print("while miau")
    item += 1

print("weird miau \n" * 3, end="")

while True:
    number = int(input("Gimme a number... "))
    if number > 0:
        break

for _ in range(3):
    print("for miau")