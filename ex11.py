def ru(valor):
    qtd_rus = 0

    while(valor >= 3.5):
        qtd_rus += 1
        valor -= 3.5

    return qtd_rus


print(ru(20))
