print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("--------- Bem-vindo ao Sistema de Ouvidoria da UniXYZ ---------")
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")

recl = []  # lista de reclamações
suge = []  # lista de sugestões
elog = []  # lista de elogios

op = 0

while op != 7:
    op = int(input("\nSelecione a operação que deseja fazer:\n\n(1) Listar as manifestações\n\n(2) Listar as "
                   "manifestações por tipo\n\n(3) Criar uma nova manifestação\n\n(4) Exibir a quantidade de "
                   "manifestações\n\n(5) Pesquisar uma manifestação pelo seu código\n\n(6) Excluir uma manifestação "
                   "pelo seu código\n\n(7) Sair do Sistema\n\n"))
    if op == 1:
        if len(recl+suge+elog) != 0:
            print("Lista com todas as manifestações:\n")
            for i in range(len(recl+suge+elog)):
                print(f"{(recl+suge+elog)[i]}\n")
        else:
            print("A lista está vazia.\n")
        input("Insira qualquer valor para continuar...\n")
    if op == 2:
        if len(recl+suge+elog) != 0:
            print("Lista com todas as manifestações de acordo com o tipo:\n")
            print("RECLAMAÇÕES:\n")
            if len(recl) != 0:
                for i in recl:
                    print(f"{i}\n")
            else:
                print("Não há nenhuma reclamação.\n")
            print("SUGESTÕES:\n")
            if len(suge) != 0:
                for i in suge:
                    print(f"{i}\n")
            else:
                print("Não há nenhuma sugestão.\n")
            print("ELOGIOS:\n")
            if len(elog) != 0:
                for i in elog:
                    print(f"{i}\n")
            else:
                print("Não há nenhum elogio.\n")
        else:
            print("A lista está vazia.\n")
        input("Insira qualquer valor para continuar...\n")
    if op == 3:
        tipo = int(input("Qual tipo de manifestação você deseja fazer?\n\n(1) Reclamação\n\n(2) Sugestão\n\n(3) Elogio\n\n"))
        if 0 < tipo < 4:
            nova = input("\nEscreva sua manifestação:\n")
            if tipo == 1:
                recl.append(nova)
            elif tipo == 2:
                suge.append(nova)
            else:
                elog.append(nova)
            print("\nManifestação adicionada com sucesso.\n")
        else:
            print("Tipo inválido.\n")
        input("Insira qualquer valor para continuar...\n")
    if op == 4:
        print(f"\nNúmero total de manifestações registradas:\n{len(recl+suge+elog)}\n")
        input("Insira qualquer valor para continuar...\n")
    if op == 5:
        if len(recl+suge+elog) != 0:
            tipo2 = int(input("De qual tipo de manifestação você quer fazer a pesquisa?\n\n(1) Reclamação\n\n(2) Sugestão\n\n(3) Elogio\n\n"))
            if tipo2 == 1 or tipo2 == 2 or tipo2 == 3:
                pesq = int(input("Qual o código de índice cuja manifestação correspondente você deseja saber?\n"))
                if tipo2 == 1:
                    if len(recl)+1 > pesq > 0:
                        print(f"Essa é a reclamação presente na posição {pesq}:\n{recl[pesq-1]}\n")
                    else:
                        print("Não há reclamação alguma nesse índice.\n")
                elif tipo2 == 2:
                    if len(suge)+1 > pesq > 0:
                        print(f"Essa é a sugestão presente na posição {pesq}:\n{suge[pesq-1]}\n")
                    else:
                        print("Não há sugestão alguma nesse índice.\n")
                elif tipo2 == 3:
                    if len(elog)+1 > pesq > 0:
                        print(f"Esse é o elogio presente na posição {pesq}:\n{elog[pesq-1]}\n")
                    else:
                        print("Não há elogio algum nesse índice.\n")
            else:
                print("Tipo inválido.\n")
        else:
            print("A lista está vazia.\n")
        input("Insira qualquer valor para continuar...\n")
    if op == 6:
        if len(recl+suge+elog) != 0:
            tipo3 = int(input("De qual tipo de manifestação você quer excluir um elemento?\n\n(1) Reclamação\n\n(2) Sugestão\n\n(3) Elogio\n\n"))
            excl = int(input("Qual o código de índice cuja manifestação correspondente você deseja excluir?\n"))
            if tipo3 == 1:
                if len(recl)+1 > excl > 0:
                    recl.pop(excl-1)
                    print(f"A reclamação da posição {excl} foi excluída com sucesso.\n")
                else:
                    print("Não há reclamação alguma nesse índice.\n")
            elif tipo3 == 2:
                if len(suge)+1 > excl > 0:
                    suge.pop(excl-1)
                    print(f"A sugestão da posição {excl} foi excluída com sucesso.\n")
                else:
                    print("Não há sugestão alguma nesse índice.\n")
            elif tipo3 == 3:
                if len(elog)+1 > excl > 0:
                    elog.pop(excl-1)
                    print(f"O elogio da posição {excl} foi excluído com sucesso.\n")
                else:
                    print("Não há elogio algum nesse índice.\n")
            else:
                print("Tipo inválido.\n")
        else:
            print("A lista está vazia.\n")
        input("Insira qualquer valor para continuar...\n")
    if op > 7 or op < 0:
        print("Operação inválida.\n")
        input("Insira qualquer valor para continuar...\n")

print("\nObrigado por usar o sistema feito pelos alunos da UniFacisa!\n\nE matricule-se na Universidade XYZ!!!")