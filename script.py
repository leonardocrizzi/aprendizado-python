try:
    nome = input("Digite o nome: ")
    
    # Verifica se o nome é vazio 
    if nome.strip() == "":
        raise Exception("O nome não pode ser vazio!")
    
    # retira o espaço da string e verifica se ela contém apenas letras
    if not nome.replace(" ", "").isalpha():
        raise Exception("O nome deve conter apenas letras!")

    entrada1 = input("Digite a primeira nota: ")

    if entrada1.strip() == "":
        raise Exception("A nota não pode ser vazia!")
    
    if entrada1.isalpha():
        raise Exception("Digite um valor válido!")
    
    n1 = float(entrada1)

    if n1 < 0 or n1 > 10:
        raise Exception("Digite um valor entre 0 e 10!")
    
    entrada2 = input("Digite a segunda nota: ")

    if entrada2.strip() == "":
        raise Exception("A nota não pode ser vazia!")

    if entrada2.isalpha():
        raise Exception("Digite um valor válido!")

    n2 = float(entrada2)

    if n2 < 0 or n2 > 10:
        raise Exception("Digite um valor entre 0 e 10!")

    entrada3 = input("Digite a terceira nota: ")

    if entrada3.strip() == "":
        raise Exception("A nota não pode ser vazia!")

    if entrada3.isalpha():
        raise Exception("Digite um valor válido!")

    n3 = float(entrada3)

    if n3 < 0 or n3 > 10:
        raise Exception("Digite um valor entre 0 e 10!")

except Exception as e:
    # Printa a mensagem do raise
    print(e)
else:
    media = (n1 + n2 + n3) / 3

    if media < 7:
        print("-"*30)
        print(f"| {f'Nome: {nome}':<{30-4}} |")
        print(f"| {'Situação: REPROVADO!':<{30-4}} |")
        print(f"| {f'Média: {media:.1f}':<{30-4}} |")
        print("-"*30)
    else:
        print("-"*30)
        print(f"| {f'Nome: {nome}':<{30-4}} |")
        print(f"| {'Situação: APROVADO!':<{30-4}} |")
        print(f"| {f'Média: {media:.1f}':<{30-4}} |")
        print("-"*30)