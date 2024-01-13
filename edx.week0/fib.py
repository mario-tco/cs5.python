# We learned about this little memory trick with Dynamic Programming
# The key to reduce processing time is by only processing each number once
# Thus the compexity becomes O(n)
memory = {}

def main():
    number = input("Gimme a number: ")
    result = fib(int(number))
    print("Fibonacci of " , (number), " is ", str(result))
    
    
def fib(number):
    if(number<=2):
        return 1
    else :
        #If it already exists in memory:
        if number in memory:
            result = memory[number]
        else:
            #Fib is just the sum of fib-1 + fib-2
            result = fib(number-1) + fib(number-2)
            memory[number] = result
        
        return result

main()