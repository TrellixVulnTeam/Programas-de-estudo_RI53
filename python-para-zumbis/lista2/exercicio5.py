#Faça um Programa que leia três números e mostre o maior e o menor deles. 
n1 = float(input('informe o primeiro numero: '))
n2 = float(input('informe o segundo numero: '))
n3 = float(input('informe o terceiro numero: '))

lista = [n1, n2, n3]
print(type(lista))


print ('O maior número é:', max(lista), 'e o menor número é:', min(lista))