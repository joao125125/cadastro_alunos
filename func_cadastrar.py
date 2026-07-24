
def cadastro ():
    print ("==== CADASTRAR ALUNOS ===")
    nome_errado = input("Digite o nome do aluno: ")
    nome = nome_errado.strip()
    
    try:
        #validação da nota
        nota_str = input("Digite a nota do aluno: ")
        #converçaõ de " , " para " . "
        nota_str = nota_str.replace(",", ".")
        nota = float(nota_str)
    except:
        print ("Digite apenas numeros!")
        return

     
    while nota <0 or nota  >10:
        print ("Digite uma nota valida!\n")
        nota_str = input("Digite a nota do aluno: ")
        nota_str = nota_str.replace(",", ".")
        nota = float(nota_str)

    if nota >= 6:
        estado = "aprovado"
    if nota <6:
        estado = "reprovado" 

    
    with open ("dados_alunos.txt", "a", encoding= "utf-8") as arquivo:
        arquivo.write(f"{nome};{nota:.1f};{estado}\n")
    print ("Aluno cadastrado com sucesso!\n")
       
cadastro()