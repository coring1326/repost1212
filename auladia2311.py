x = int(input("informar o primeiro numero"))
y = int(input("informar o segundo numero"))
z = int(input("informar o terceiro numero"))

maior = max(x,y,z)
menor = min(x,y,z)
media = (x + y + z) / 3

print("Maior:", maior)
print("Menor:", menor)
print(f"Média: {media:.2f}")