def valida_nome(nome):
    # Verifica se o nome é vazio 
    if nome.strip() == "":
        raise Exception("O nome não pode ser vazio!")
    
    # retira o espaço da string e verifica se ela contém apenas letras
    if not nome.replace(" ", "").isalpha():
        raise Exception("O nome deve conter apenas letras!")
    
def valida_nota(entrada):
    if entrada.strip() == "":
        raise Exception("A nota não pode ser vazia!")
    
    if entrada.isalpha():
        raise Exception("Digite um valor válido!")
    
    nota = float(entrada)

    if nota < 0 or nota > 10:
        raise Exception("Digite um valor entre 0 e 10!")
    
    return nota
    
def media(n1, n2, n3, nome):

    calculo = (valida_nota(n1) + valida_nota(n2) + valida_nota(n3)) / 3

    if calculo < 7:
        print("-"*30)
        print(f"| {'FICHA ESCOLAR':<{30-4}} |")
        print("-"*30)
        print(f"| {f'Nome: {nome}':<{30-4}} |")
        print(f"| {'Situação: REPROVADO!':<{30-4}} |")
        print(f"| {f'Média: {calculo:.1f}':<{30-4}} |")
        print("-"*30)
    else:
        print("-"*30)
        print(f"| {'FICHA ESCOLAR':<{30-4}} |")
        print("-"*30)
        print(f"| {f'Nome: {nome}':<{30-4}} |")
        print(f"| {'Situação: APROVADO!':<{30-4}} |")
        print(f"| {f'Média: {calculo:.1f}':<{30-4}} |")
        print("-"*30)

try:
    nome = input("Digite o nome: ")
    valida_nome(nome)

    entrada1 = input("Digite a primeira nota: ")
    valida_nota(entrada1)
    
    entrada2 = input("Digite a segunda nota: ")
    valida_nota(entrada2)

    entrada3 = input("Digite a terceira nota: ")
    valida_nota(entrada3)

except Exception as e:
    # Printa a mensagem do raise
    print(e)
else:
    media(entrada1, entrada2, entrada3, nome)    