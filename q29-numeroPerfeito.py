numero = int(input("Digite um número: "))
soma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

if soma_divisores == numero:
    print("O número é perfeito.")
else:
    print("O número não é perfeito.")
