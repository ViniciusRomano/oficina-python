p1 = int(input("Me de um número ae meu chapa\n"))
p2 = int(input("Me de outro número ae meu chapa\n"))

media = (p1 + p2) / 2

if(media >= 6):
    print("Aprovado")
elif(media < 6 and media >= 4):
    print("Quebra de Pré Requisito")
else:
    print("Reprovado")
