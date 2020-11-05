while True:
    lado1=float(input("Digite a medida do primeiro lado do seu triângulo:\n"))
    lado2=float(input("Digite a medida do segundo lado do seu triângulo:\n"))
    lado3=float(input("Digite a medida do terceiro lado do seu triângulo:\n"))
    if lado1<(lado2+lado3) and lado2<(lado1+lado3) and lado3<(lado2+lado1):
        break
    else:
        print("Triângulo inválido, digite outras medidas")
        continue
if lado1==lado2 and lado1==lado3:
    print("Esse é um triângulo equilátero")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    print("Esse é um triângulo isósceles")
else:
    print("Esse é um triângulo escaleno")