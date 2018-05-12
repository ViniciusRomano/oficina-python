notas = {'aluno1': [6, 7], 'aluno2': [9, 8], 'aluno3': [3, 4]}
maior_media = 0
melhor_aluno = ""

for aluno_key in notas:

    cond = True
    media = 0

    while(cond):
        nota = int(input("Me de uma nota ae meu chapa\n"))
        if(nota >= 0 and nota <= 10):
            notas.get(aluno_key).append(nota)
            cond = False

    for nota_aluno in notas.get(aluno_key):
        media += nota_aluno / 3

    if(media > maior_media):
        melhor_aluno = aluno_key
        maior_media = media

print("Melhor aluno:", melhor_aluno, "\nMaior Media: ", maior_media)
