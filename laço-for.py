for i in range(1,11):
    print(f"{i} ",end='')

# range(valor_inicial, valor_final, incremento)

print("\n")
for i in range(0,11,2):
    print(f"{i} ",end='')

print('\n')

nome = 'Tariky'
for i in nome :
    print(i)

print('\n')

nome = 'Tariky'
for i in reversed(nome):
    print(i)

for i in range(1,11):
    if(i == 9):
        continue # Aqui ele vai para o inicio do for sem fazer o restante daqui para baixo
    print(i, end=' ')
