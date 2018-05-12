lista_notas = []

for x in range(4):
    lista_notas.append(int(input("Me de um número ae meu chapa\n")))

media = 0

for nota in lista_notas:
    media += nota / 4

print("Media: ", media)
