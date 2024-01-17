while True:
    try:
        number = int(input("Gimme a number... "))
        break
    except ValueError:
        print("That is not a number")

print(f"The number is {number}")
        