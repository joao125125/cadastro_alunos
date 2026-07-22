def mostrar ():
    with open ("dados_alunos.txt", "r", encoding="UTF-8") as arquivo:
        conteudo = arquivo.readlines()
   
    print (f"{'NOME':<10} {'NOTA':<10} ESTADO")
    print ("=" * 35)

    for linhas in conteudo:
        linhas = linhas.strip()
        partes = linhas.split(";")
        nome = partes[0]
        nota = float(partes[1])
        estado = partes[2]

        print(f"{nome:<10} {nota:<10} {estado}")

mostrar ()