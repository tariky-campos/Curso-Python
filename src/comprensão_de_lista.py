numeros = [1,3,5,6,75,3,7,6,0]

#Podemos usar o for para alterar o valores de cada elemento

quadra_for = [num ** 2 for num in numeros]

quadrados = list(map(lambda x: x**2, numeros))

pares = [num for num in range(11) if num % 2 == 0]

frase = " A lógica é apenas o princípio da sabedoria, e não o seu fim"

vogais = ['a','e','i','o','u','ã','í','é','ó','A','E','I','O','U']

lista_vogais = [v for v in frase if v in vogais]

#Distributiva entre valores de duas listas

distributiva = [k * m for k in [2,3,4] for m in [5,6,7]]

if __name__ == '__main__':
    print(distributiva)