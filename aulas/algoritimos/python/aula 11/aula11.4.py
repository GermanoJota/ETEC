
forca = int(input("Qual a força do heroi?(1 a 10) "))
if forca > 10:
    forca = 10
    print("(o numero teve de ser alterado para suprir as necessidades)")
elif forca < 1:
    forca = 1
    print("(o numero teve de ser alterado para suprir as necessidades)")
print(f"força = {forca}")

agilidade = int(input("Qual a agilidade do heroi?(1 a 10) "))
if agilidade > 10:
    agilidade = 10
    print("(o numero teve de ser alterado para suprir as necessidades)")
elif agilidade < 1:
    agilidade = 1
    print("(o numero teve de ser alterado para suprir as necessidades)")
print(f"agilidade = {agilidade}")

inteligencia = int(input("Qual a inteligencia do heroi?(1 a 10) "))
if inteligencia > 10:
    inteligencia = 10
    print("(o numero teve de ser alterado para suprir as necessidades)")
elif inteligencia < 1:
    inteligencia = 1
    print("(o numero teve de ser alterado para suprir as necessidades)")

print(f"inteligencia = {inteligencia}")


poderTotal = (forca * 3) + (agilidade * 2) + (inteligencia / 2)

print(f"O poder total do herói é: {poderTotal}")
