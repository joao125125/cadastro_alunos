from colorama import Fore, Style, init   
init ()
def menu ():
    while True:
        print (Fore.LIGHTBLUE_EX + "==============================\n Sistema de Cadastro \n==============================\n")
        escolha = int(input(Fore.LIGHTCYAN_EX + "OPÇÕES\n\n1- CADASTRO\n2- LISTA DE CADASTROS\n3- ALTERAR DADOS\n4- EXCLUIR DADOS\n5- SAIR\nDigite sua escolha: "))
        if escolha == 1:
            cadastro()
        if escolha == 2:
            mostrar()
        if escolha == 3:
            alterar()
        if escolha == 4:
            excluir()
        if escolha == 5:
            print (Fore.BLUE + "\nFECHANDO PROGRAMA...")
            break

def cadastro ():
    print (Fore.LIGHTWHITE_EX + "\n==== CADASTRAR ALUNOS ===")
    nome_errado = input(Fore.LIGHTWHITE_EX + "Digite o nome do aluno: ")
    nome = nome_errado.strip()
    
    
    #validação da nota
    nota_str = input(Fore.LIGHTWHITE_EX + "Digite a nota do aluno: ")
    #converçaõ de " , " para " . "
    nota_str = nota_str.replace(",", ".")
    nota = float(nota_str)

     
    while nota <0 or nota  >10:
        print (Fore.LIGHTRED_EX + "Digite uma nota valida!\n")
        nota_str = input(Fore.LIGHTWHITE_EX + "Digite a nota do aluno: ")
        nota_str = nota_str.replace(",", ".")
        nota = float(nota_str)

    if nota >= 6:
        estado = "aprovado"
    if nota <6:
        estado = "reprovado" 

    
    with open ("dados_alunos.txt", "a", encoding= "utf-8") as arquivo:
        arquivo.write(f"{nome};{nota:.1f};{estado}\n")
    print (Fore.LIGHTGREEN_EX + "Aluno cadastrado com sucesso!\n")
    



def mostrar ():
    with open ("dados_alunos.txt", "r", encoding="UTF-8") as arquivo:
        conteudo = arquivo.readlines()

    if not conteudo:
        print(Fore.LIGHTRED_EX + "\nNenhum aluno cadastrado!\n")
        return
    
    print (Fore.LIGHTYELLOW_EX + "\n==== LISTA DE CADASTRADOS ===\n")
    print (Fore.LIGHTWHITE_EX + f"{'NOME':<10} {'NOTA':<10} ESTADO")
    print ("=" * 35)


    for linhas in conteudo:
        linhas = linhas.strip()
        partes = linhas.split(";")
        nome = partes[0]
        nota = float(partes[1])
        estado = partes[2]

        print(Fore.LIGHTWHITE_EX + f"{nome:<10} {nota:<10} {estado}")
    print ("\n")
    




def alterar ():
    print (Fore.LIGHTMAGENTA_EX + "\n=== ALTERAR NOTA ===")
    with open ("dados_alunos.txt", "r", encoding="UTF-8") as arquivo:
        cont_p_alterar = arquivo.readlines() #CRIA UMA LISTA COM OS DADOS LIDOS 

    nome_aluno = input(Fore.LIGHTWHITE_EX + "Digite o nome do aluno que deseja alterar a nota: \n")

    existe = False #CRIA UMA VARIAVEL BOLEANA 
    cont_alterado = [] #CRIA UMA LISTA VAZIA PARA OS NOVOS DADOS

    #VERIFICA SE EXISTE UMA LINHA VAZIA SE EXISTIR ELA É PULADA
    for n in cont_p_alterar:
     if  n.strip() == "":
         continue

       
     partes = n.split(";")#DIVIDE AS LINHAS POR ESPAÇOS 
     nome = partes[0] #COLOCA NOME NO "ESPAÇO 0 "
     nota = float(partes[1])#IDADE NO "ESPAÇO 1"
     estado = partes[2]#ESTADO NO "ESPAÇO 2"
     

     if nome.lower() == nome_aluno.lower():#IDENTIFICA SE O NOME DIGITADO EXISTE NOS CADASTROS
        existe = True#MUDA A VARIAVEL BOLEANA PARA VERDADEIRA 
        print (Fore.LIGHTGREEN_EX + f"ALUNO ENCONTRADO\nNOME: {nome} | NOTA ATUAL: {nota:.2} | ESTADO ATUAL: {estado}")
        nova_nota = input(Fore.LIGHTWHITE_EX + "Digite a nova nota: ")#PEDE UMA NOVA NOTA 
        nova_nota = nova_nota.replace(",", ".")
        nova_nota = float(nova_nota)

        while nova_nota <0 or nova_nota >10:#PEDE UMA NOVA NOTA CASO DIGITEM UMA NOTA MAIOR QUE 10 OU MENOR QUE 0
            print (Fore.LIGHTRED_EX + "DIGITE UMA NOTA VALIDA!")
            nova_nota = input(Fore.LIGHTWHITE_EX + "Digite a nova nota: ")#PEDE UMA NOVA NOTA 
            nova_nota = nova_nota.replace(",", ".")
            nova_nota = float(nova_nota)

        novo_estado = "aprovado" if nova_nota >= 6 else "reprovado" #ATUALIZA O ESTADO
        cont_alterado.append(f"{nome};{nova_nota:.1f};{novo_estado}\n")

     else:
      cont_alterado.append(n)
    
    if existe == True:
       print (Fore.LIGHTGREEN_EX + "NOTA ALTERADA COM SUCESSO!\n")
       with open ("dados_alunos.txt", "w", encoding="UTF-8") as arquivo:
          arquivo.writelines(cont_alterado)
    
    else:
       print (Fore.LIGHTRED_EX + "aluno não encontrado!\n")
    



def excluir ():
    print (Fore.LIGHTRED_EX + "\n=== EXCLUIR ALUNO ===")
    with open ("dados_alunos.txt", "r", encoding="UTF-8") as arquivo:
        conteudo = arquivo.readlines()


    nome_excluir = input(Fore.LIGHTWHITE_EX + "DIGITE O NOME DO ALUNO QUE DESEJA EXCLUIR: \n")

    existe_1 = False 

    for n in conteudo:
        partes = n.strip()
        partes = n.split(";")
        nome = partes [0]
        nota = float(partes[1])
        estado = partes [2]

        if nome_excluir.lower() == nome.lower():
            existe_1 = True 
            print (Fore.LIGHTGREEN_EX + f"ALUNO ENCONTRADO!\nNOME: {nome} NOTA: {nota} ESTADO: {estado}\n")

            while True:
                escolha =  input(Fore.LIGHTYELLOW_EX + "TEM CERTEZA QUE DESEJA EXCLUIR ESSE ALUNO DO SISTEMA? (S/N)\n").lower()
                if escolha == "s":
                    conteudo.remove(n)
                    with open ("dados_alunos.txt", "w", encoding="UTF-8") as arquivo:
                        arquivo.writelines(conteudo)
                    print (Fore.LIGHTGREEN_EX + "ALUNO EXCLUIDO COM SUCESSO!\n")
                    break
                    
                if escolha == "n":
                    print (Fore.LIGHTMAGENTA_EX + "EXCLUSÃO CANCELADA!\n")
                    break
                else:
                    print (Fore.LIGHTRED_EX + "DIGITE APENAS 'S' ou 'N'!\n")
                

    if existe_1 == False:
        print (Fore.LIGHTRED_EX + "ALUNO NÃO ENCONTRADO!\n")    
    




menu()