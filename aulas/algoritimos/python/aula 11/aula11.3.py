aventureiro = int(input("Quantos aventureiros? "))
moedas = int(input("Quantas moedas? "))

divisao = moedas/aventureiro
resto = moedas%aventureiro

print(f"{divisao:.0f} moedas para cada aventureiro")
print(f"{resto} moedas sobraram para o guia")
