# Recursividade

#formula geral para o fatorial:
# fatorial(num) = fatorial(num-1) * num

def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    try:
        n = int(input("Input a number: "))
        res = factorial(n)
    except RecursionError:
        print("O number entered is very big or negative!")
    else:
        print(f"The factorial of {n} is: {factorial(n)}.")
