def excluir ():
    print ("=== EXCLUIR ALUNO ===")
    with open ("dados_alunos.txt", "r", encoding="UTF-8") as arquivo:
        conteudo = arquivo.readlines()


    nome_excluir = input("DIGITE O NOME DO ALUNO QUE DESEJA EXCLUIR: ")

    existe_1 = False 

    for n in conteudo:
        partes = n.strip()
        partes = n.split(";")
        nome = partes [0]
        nota = float(partes[1])
        estado = partes [2]

        if nome_excluir.lower() == nome.lower():
            existe_1 = True 
            print (f"ALUNO ENCONTRADO!\nNOME: {nome} NOTA: {nota} ESTADO: {estado}\n")

            while True:
                escolha =  input("TEM CERTEZA QUE DESEJA EXCLUIR ESSE ALUNO DO SISTEMA? (S/N)\n").lower()
                if escolha == "s":
                    conteudo.remove(n)
                    with open ("dados_alunos.txt", "w", encoding="UTF-8") as arquivo:
                        arquivo.writelines(conteudo)
                    print ("ALUNO EXCLUIDO COM SUCESSO!\n")
                    break
                    
                if escolha == "n":
                    print ("EXCLUSÃO CANCELADA!\n")
                    break
                else:
                    print ("DIGITE APENAS 'S' ou 'N'!\n")
                

    if existe_1 == False:
        print ("ALUNO NÃO ENCONTRADO!\n")
            






excluir ()