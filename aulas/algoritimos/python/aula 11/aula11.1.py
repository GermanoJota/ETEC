turno = int(input("Quantos turnos irá jogar? "))
mana_atual = float(input("Mana atual: "))
regeneracao = float(input("Regeneração por turnos: "))
mana_apos_5_turnos = mana_atual + (regeneracao * turno)

print(f"Em {turno} turnos, terás {mana_apos_5_turnos:.2f} de mana total.")
