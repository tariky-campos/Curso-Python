#Funções

def mensagem():
    print("Tariky Lindo Cheiroso")

def soma(a, b,c = 0):
    if c == 0:
        print(a * b)
    else:
        print(a+b+c)

if __name__ == '__main__':
    soma(12,43,1)