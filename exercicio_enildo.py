import os

#pede um nome
nome = input("Digite o nome: ")
nome = nome.strip

#cria um arquivo e coloca o nome dentro dele
with open ("nome.txt", "w") as arquivo:
    arquivo.write(nome)

print ("arquivo criado com sucesso")


#abre o arquivo em modo de leitura
with open ("nome.txt", "r") as arquivo:
    
    #cria uma variavel que dentro dela esta o conteudo do arquivo
    conteudo = arquivo.read()

#exemplo simples de menu 
opcao = int(input("1 ou 2 ? "))
if opcao == 1:

    #mostra oque esta dentro do arquivo
    print(f"Conteudo do arquivo:\n{conteudo}")
if opcao == 2:
    print ("fazer oque ne?")