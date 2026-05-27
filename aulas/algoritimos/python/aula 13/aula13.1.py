print("Iniciando treino de pontaria...")

for flecha in range (1,6):
    print(f"flecha numero {flecha} disparada!")
    acertou = input("Acertou no alvo? (s/n) ")

    if acertou == 's' or 'n':
    
        if acertou == 's':
            print("Bela mira!")
        else:
            print("Melhore para a próxima")
    else:
        print("Não entendi o que você quis dizer")

