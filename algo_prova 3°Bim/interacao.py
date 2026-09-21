from main import *


print("Bem vindo ao PyBank")
contas_carregadas = carregar_conta()

nome = input("Qual seu nome")
conta = contas_carregadas[f"{nome}"]

if contas_carregadas is None:
    print("Parece-me que você não tem uma conta logada, vamos cria-lá: ")
    salvar_conta(criar_conta())

