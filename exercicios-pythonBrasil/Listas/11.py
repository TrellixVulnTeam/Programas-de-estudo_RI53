#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada. 

l1 = ['fernanda', 'roberta', 'lucas', 'elzi', 'filipe', 'igor', 'katia', 'pedro', 'thiago', 'bia']

l2 = [1,6, 9, 15, 16, 12, 18, 25, 62, 84]

l3 = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente']
# l3.append(zip(l1,l2))
# print(l3)
l4 = []
for x in zip(l1,l2,l3):
    l4.append(x[0])
    l4.append(x[1])
    l4.append(x[2])
print(l4)