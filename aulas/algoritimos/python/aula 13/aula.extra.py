opcao = 0
moedas = int(input("Quantas moedas vc tem? "))
pocao = 0

while opcao != 3 and moedas > 20:
    print("\n--- TAVERNA DO CÓDIGO ---")
    print("1. Comprar Poção")
    print("2. Ver Inventario")
    print("3. Sair da taverna")
    print("")

    
    opcao = int(input("Escolha uma ação: "))
    if opcao == 1:
        print("Poção de mana adicionada! -20 moedas")
        moedas = moedas - 20
        pocao = pocao + 1
    
    elif opcao == 2:
        if pocao == 0:
            print("O seu inventario está vazio... por agora.")
        else:
            print(f"Seu inventário tem {pocao} poções")
    
    elif opcao == 3:
        print("Até à próxima, aventureiro!")
    
    else:
        print("Opção invalida. Tente novamente")
   