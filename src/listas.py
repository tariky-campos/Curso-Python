n1 = [1,2,3]
n2 = [7,5,4]

joint = n1 + n2
print(f"{joint}")
print(f"{joint[-2]}")

#ate um certo index
print(f"{joint[0:3]}")

#quantidade de elementos
print(f"{len(joint)}")

#sem reverse=True ele imprime em ordem crescente
print(f"{sorted(joint, reverse = True)}")

print(sum(joint))
print(min(joint))
print(max(joint))

joint.append(12)
print(joint)

joint.pop(1)
print(joint)

joint.insert(3,21)
print(joint)


print(12 in joint)

players = []

for i in range(3):
    players.append(input("Input a players: "))
print(players)

players.sort()
print(players)