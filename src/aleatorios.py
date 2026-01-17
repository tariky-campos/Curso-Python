import random

print('Gerador de numeros aleatorios:')

# aqui ele gera um numero entre 1 e 10 interios
for i in range(5):
    valor = random.randint(1,10)
    print(f"Numero generated: {valor}")

#
num_float = random.random()
print(f"{num_float*10:.2f}")
print(f"Number rounded using round: {round(num_float*10, 2)}")

num_uniform = random.uniform(1,100)
print(f"Number generated: {round(num_uniform, 3)}")

L = [9,8,7,6,5,4,34,2,1]
n = random.choice(L)
print(f"Chosen number (Numero escolhido): {n}")

n = random.sample(L, 3)
print(f"Numbers chosens: {n}")

#Embaralhar a lista
n= random.shuffle(L)
print(f"List shuffle: {L}")