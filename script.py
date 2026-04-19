n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media < 7:
    print("-"*30)
    print(f"| {'Situação: REPROVADO!':<{30-4}} |")
    print(f"| {f'Média: {media:.1f}':<{30-4}} |")
    print("-"*30)
else:
    print("-"*30)
    print(f"| {'Situação: APROVADO!':<{30-4}} |")
    print(f"| {f'Média: {media:.1f}':<{30-4}} |")
    print("-"*30)