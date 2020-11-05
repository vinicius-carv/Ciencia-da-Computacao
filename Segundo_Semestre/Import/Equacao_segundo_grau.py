import math
while True:
    a=float(input("Digite o coeficiente 'a' da equação do 2º grau:\n"))
    if a==0:
        print("Coeficiente inválido!")
        continue
    b=float(input("Digite o coeficiente 'b' da equação do 2º grau:\n"))
    c=float(input("Digite o coeficiente 'c' da equação do 2º grau:\n"))
    break
delta=pow(b,2)-4*a*c
if delta>0:
    result1=(-b+math.sqrt(delta))/(2*a)
    result2=(-b-math.sqrt(delta))/(2*a)
elif delta==0:
    result1=(-b+math.sqrt(delta))/(2*a)
if delta<0:
    print("A equação não possui raízes reais")
elif delta>0:
    print("As raízes foram {:.4f} e {:.4f}".format(result1,result2))
elif delta==0:
    print("A raiz é {:.4f}".format(result1))