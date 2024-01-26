def main():
    x = input("What is x?")
    if is_valid_number(x):
        print("x squared is", square(int(x)))

def square(n):
    return n * n

def is_valid_number(input):
    try:
        value = int(input)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()