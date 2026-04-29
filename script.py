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
    
def media(n1, n2, n3):
    calculo = (n1 + n2 + n3) / 3
    return f"{calculo:.2f}"

try:
    lista_alunos = []
    while True:
        aluno = {}
        lista_notas = []

        nome_aluno = input("Digite o nome: ")
        valida_nome(nome_aluno)
        aluno["nome"] = nome_aluno

        for trimestre in range(1, 4):
            print(f"NOTAS DO {trimestre}º TRIMESTRE")
            nota1 = input("Digite a 1ª nota: ")
            valida_nota(nota1)
            nota2 = input("Digite a 2ª nota: ")
            valida_nota(nota2)
            nota3 = input("Digite a 3ª nota: ")
            valida_nota(nota3)
            print("-"*20)

            media_trimestre = media(valida_nota(nota1), valida_nota(nota2), valida_nota(nota3))
            lista_notas.append({"trimestre": trimestre, "notas": [valida_nota(nota1), valida_nota(nota2), valida_nota(nota3)], "media": media_trimestre})
            
        aluno["notas"] = lista_notas
        lista_alunos.append(aluno)
        
        try:
            fim = input("Deseja continuar cadastrando alunos?(S/N): ")

            if fim == "S":
                continue
            elif fim == "N":
                break
            else:
                raise Exception("Digite uma opção válida!")
        except Exception as e:
            print(e)
    
    print(lista_alunos)

except Exception as e:
    # Printa a mensagem do raise
    print(e)  