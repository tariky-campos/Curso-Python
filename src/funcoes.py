#Funções

def mensagem():
    print("Tariky Lindo Cheiroso")

def soma(a, b,c = 0):
    if c == 0:
        print(a * b)
    else:
        print(a+b+c)

def pow(a,b):
    res = a
    for i in range(b):
        if(i == 0):
            continue
        res = res * a
    return res

verificar_paridade = lambda x: x%2 == 0

n2 = [7,5,4]
dobro = list(map(lambda x: x*2, n2))
string = ["tariky", "duke"]
maius = list(map(str.upper, string))


num = [1,2,3,4,5,6,7,8,9]
num_pares = list(filter(verificar_paridade, num))

if __name__ == '__main__':
    x = pow(2 ,2)
    print(f"{x}")

    n = int(input("Input a number: "))
    print(f"This number is (Par-True), (Impar-False), Result... -> {verificar_paridade(n)}")
    print(dobro)
    print(maius)
    print(num_pares)