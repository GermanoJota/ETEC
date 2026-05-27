nome = input("Qual o nome do teu aventureiro? ")
nivel = int(input("Qual o nível inicial? "))
saude_t = 100 + (nivel * 10)


print(f"FICHA DE PERSONAGEM: {nome}")
print(f"NÍVEL: {nivel} | SAÚDE: {saude_t} HP")