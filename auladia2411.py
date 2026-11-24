a= 0

while True:
    b=(input("informe um numero: "))

    if b == "sair":
        print("saiu do programa!")
        break

    b=int(b)

    if b <= 0 :
        print("digite um numero maior que zero")
        continue
    if b <=a:
        print("a ordem nao esta crescente!")
        break

    a =b