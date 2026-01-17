# excecao e um objeto que representa um erro que ocorreu ao executar o programa

#|Blocos try ... except

def div(a,b):
    return round(a/b,2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input("Input a number: "))
            n2 = int(input("Input other number: "))
            break
        except ValueError:
            print("Ocorred a error are read a value. Try again")
        
    try:
        r = div(n1,n2)
    except ZeroDivisionError:
        print("Not is possible divide to zero.")
    except:
        print("Ocurred a error unknown.")
    else:
        print(f"Result: {r}")
    finally:
        print(f"\nEnd of calculation")

