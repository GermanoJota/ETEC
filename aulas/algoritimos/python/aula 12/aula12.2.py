user = input("Usuario: ")
passw = int(input("Senha: "))

if user == "admin" and passw == "1234":
    print("Portal aberto. Bem-vindo!")
else:
    print("Acesso negado. Os guardas se aproximam...")