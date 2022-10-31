notas_acumulo = 0
for i in range(1,5,1):
    nota = float(input(f"Digite a {i}º nota: "))

    notas_acumulo += nota

media = notas_acumulo / 4

print(f"Sua média é igual a: {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
