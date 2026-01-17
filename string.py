name = "lets learn Python today"
words = name.split() # separa cada palavra no vetor
print(words)

i = len(name)
while(i > 0):
    print(name[i-1], end='')
    i -= 1

print("\n",name[::-1])

count = 0
email = input("Input your address of email: ")
for i in email:
    
    if(i == '@'):
        break
    count +=1
arroba = email.find('@')
user = email[:count]
domain = email[count+1:]

print(user)
print(domain)

objeto = "My name is Tariky"
print(objeto.upper()) #TUDO MAIUSCULO
print(objeto.lower()) #TUDO MINISCULO
print(objeto.capitalize()) # A PRIMEIRA LETRA DA STRING E MAIUSCULA SOMENTE
print(objeto.title()) #COLOCA A PRIMERIA LETRA DE CADA PALAVRA EM MAIUSCULO

suplemento = "cloreto de magnesio"
n_suplemento = suplemento.replace("magnesio", "zinco")

print(suplemento)
print(n_suplemento)

frase = "   Omega 3 e bom para a saude!     "
print(frase)
print(frase.lstrip())  #removedor de espacos a esquerda
print(frase.rstrip())   #removedor de espacos a direita
print(frase.strip())    #remove espacos a mais em toda a frase

fruta = "Abacate"

print(fruta.rjust(20))
print(fruta.center(20))
print(fruta.ljust(20, "-"))
print(fruta.center(20, "-"))

p = "Tariky"

print(p.startswith('T'))
print(p.endswith('a'))