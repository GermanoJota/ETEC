nome = input("Nome do guerreiro: ")
xp = int(input("quanto de xp conseguiu até agr? "))

if xp < 1000:
    rank = "aprendiz"

elif xp < 5000:
    rank = "Guerreiro"

else:
    rank = "Lenda"

print(f"O nome do guerreiro é {nome}, e o rank dele é {rank}")