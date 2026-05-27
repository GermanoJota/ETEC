velocidade = float(input("Velicidade da carroça (km/h); "))

if velocidade > 80:
    print("MULTADO! Estás a correr demais.")
    multa = (velocidade - 80) * 7
    print(f"Multa: {multa:.2f} moedas.")

print("Boa viajem!")