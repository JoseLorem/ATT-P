n1 = float(input("digite a primeira nota"))
n2 = float(input("digite a segunda nota"))
n3 = float(input("digite a terceira nota"))
n4 = float(input("digite a quarta nota"))

media = float(n1 + n2 + n3 + n4)/ 4

print(media)

if media >= 9:
    print("nota A")
if media >= 8 and media < 9:
    print("nota B")
if media >= 7 and media < 8:
    print("nota C")
if media >= 6 and media < 7:
    print("nota D")
if media < 6:
    print("nota F")
if media < 0 or media > 10:
    print("invalido")