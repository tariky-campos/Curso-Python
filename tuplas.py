halogenios = ('F', 'Cl', "Br", "At")
print(halogenios[3])

L = [1,2,3,4,5,4,3,2,34,45,2]
print(L.count(2))

print("Br" in halogenios)

#todos os metodos que alteram a tupla, nao vai funcionar

for i in halogenios:
    print(f"Element: {i}")

#colocando a tupla em uma lista
inArray = list(halogenios)
print(inArray)

# e depois colando uma lista em uma tupla
grupo1 = tuple(inArray)
print(type(grupo1))

#o comando sorted funciona em tuplas
print(sorted(grupo1))