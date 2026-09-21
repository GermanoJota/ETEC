import json
import random
from datetime import datetime as dt

def carregar_conta():
    try:
        with open("conta.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
def salvar_conta(conta):
    try:
        with open("conta.json", "a", encoding="utf-8") as f:
            json.dump(conta, f, ensure_ascii=False, indent=2)
        if conta != None:    
            print("conta criada com sucesso")
        else:
            print("Erro ao criar conta")
    except Exception as e:
        print(f"Erro ao criar a conta: {e}")

def depositar(conta, valor):
    if valor <= 0:
        print("O valor depositado tem que ser maior que 0")
        return
    conta["saldo"] += valor
    agora = dt.now()

    extrato = {
        "data": agora.strftime('%H:%M:%S'),
        "valor": valor,
        "agencia": conta["agencia"],
        "Cx": conta["caixa"]
    }

    conta["extrato"].append(extrato)

def criar_conta():
    nome =input("Qual seu nome? ")
    try:
        idade = int(input("Qual sua idade? "))
    except TypeError:
        print("erro, isso não é um numero real")
    
    conta_nova = {
        nome:{
        "cpf": input("Qual seu cpf? "),
        "email": input("Qual seu email? "),
        "idade": idade,
        "endereço": {
            "cep": input("Qual seu cep? "),
            "rua": input("Qual sua rua? "),
            "numero": input("Qual o numero? ")
            },
        "estado_civil": input("Qual seu estado civil? "),
        "agencia": "8181",
        "conta": str(random.randint(10000, 99999))
        }}
    
    verificacao_idade = int(conta[f"{nome}"]["idade"])
    if verificacao_idade < 18:
        print("Você não pode ter uma conta no banco!!")
        conta = None
        return
    conta
    return conta



