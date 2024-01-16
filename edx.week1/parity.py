def main():
    number = int(input("Gimme a number: "))
    if is_even(number):
        print(number, "is Even.")
    else:
        print(number, "is Odd.")

def is_even(number):
    return number % 2 == 0

main()