opcao = 0


while opcao != 3:
    print("\n--- TAVERNA DO CÓDIGO ---")
    print("1. Comprar Poção")
    print("2. Ver Inventario")
    print("3. Sair da taverna")
    print("")

    
    opcao = int(input("Escolha uma ação: "))
    if opcao == 1:
        print("Poção de mana adicionada! -20 moedas")

    elif opcao == 2:
        print("O seu inventario está vazio... por agora.")

    elif opcao == 3:
        print("Até à próxima, aventureiro!")
    
    else:
        print("Opção invalida. Tente novamente")
   