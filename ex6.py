cond = True

while(cond):
    frase = input("Me de uma frase com mais de dois a's, meu chapa\n")
    if(frase.count('a') >= 2):
        cond = False
        
## Método um pouquinho mais bonito
# cond = True

# while(cond):
#     frase = input("Me de uma frase com mais de dois a's, meu chapa\n")
#     cond = frase.count('a') < 3
