nome = """
....

"""

elemento = {
    'Z': 3,
    'nome': 'Litio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}')


# Exclusao de itens em dicinarios

del elemento['densidade']
print(elemento)

elemento.clear()
print(elemento)

del elemento
print(elemento)