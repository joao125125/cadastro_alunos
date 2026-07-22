def alterar ():
    print ("=== ALTERAR NOTA ===")
    with open ("dados_alunos.txt", "r", encoding="UTF-8") as arquivo:
        cont_p_alterar = arquivo.readlines() #CRIA UMA LISTA COM OS DADOS LIDOS 

    nome_aluno = input("Digite o nome do aluno que deseja alterar a nota: ")

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
        print (f"ALUNO ENCONTRADO\nNOME: {nome} | NOTA ATUAL: {nota:.2} | ESTADO ATUAL: {estado}")
        nova_nota = input("Digite a nova nota: ")#PEDE UMA NOVA NOTA 
        nova_nota = nova_nota.replace(",", ".")
        nova_nota = float(nova_nota)

        while nova_nota <0 or nova_nota >10:#PEDE UMA NOVA NOTA CASO DIGITEM UMA NOTA MAIOR QUE 10 OU MENOR QUE 0
            print ("DIGITE UMA NOTA VALIDA!")
            nova_nota = input("Digite a nova nota: ")#PEDE UMA NOVA NOTA 
            nova_nota = nova_nota.replace(",", ".")
            nova_nota = float(nova_nota)

        novo_estado = "aprovado" if nova_nota >= 6 else "reprovado" #ATUALIZA O ESTADO
        cont_alterado.append(f"{nome};{nova_nota:.1f};{novo_estado}\n\n")

     else:
      cont_alterado.append(n)
    
    if existe == True:
       print ("NOTA ALTERADA COM SUCESSO!\n")
       with open ("dados_alunos.txt", "w", encoding="UTF-8") as arquivo:
          arquivo.writelines(cont_alterado)
    
    else:
       print ("aluno não encontrado!\n")




     
     



alterar()