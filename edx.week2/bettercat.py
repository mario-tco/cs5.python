def main():
    number = getNumber()
    miau(number)

def getNumber():
    while True:
        times = int(input("Gimme a number... "))
        if times > 0:
            break
    return times
    
def miau(number):
    for _ in range(number):
        print("miau")

main()