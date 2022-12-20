insumos = []
while True:
    print("-"*5 + "Controle de Estoque" + "-"*5)
    print("1 - Codigo de Insumo:")
    print("2 - Listar os insumos:")
    print("3 - Remover insumo:")
    print("4 - Sair:")
    print("-"*20)
    opcao = int(input("Informe a opção desejada: "))
    while opcao < 1 or opcao > 4:
        print("\n")
        print("Opção inválida!")
        opcao = int(input("Informe a opção desejada: "))

    if(opcao == 4):
        opcao = input("Tem certeza que deseja sair?S/N ")
        if(opcao == "s" or opcao == "S"):
            print("Sistema Finalizado!")
            break
        else:
            continue
    elif(opcao == 1):
        codigo = int(input("Digite o código do insumo: "))
        quantidade = int(input("Digite a quantidade de insumo: "))
        achou = False
        for iterador in range(0, len(insumos)):
            if(insumos[iterador]['codigo'] == codigo):
                achou = True
                insumos[iterador]['quantidade'] += quantidade
        if(not achou):
            insumo = {}
            insumo['codigo'] = codigo
            insumo['quantidade'] = quantidade
            insumo['nome'] = input("Digite o nome do insumo: ")
            insumo['fornecedor'] = int(input("Digite o codigo do fornecedor: "))
            insumos.append(insumo)
            print("-"*20)
            print("\n")
    elif(opcao == 2):
        if(len(insumos) == 0):
            print("Nenhum item cadastrado!")
            print("\n")
        else:
            print("-"*20)
            print("Lista de insumos:")
            insumos = sorted(insumos, key=lambda k: k['quantidade'])
            for iterador in range(0, len(insumos)):
                print("Insumo: {}".format(insumos[iterador]['codigo']))
                print("Nome: {}".format(insumos[iterador]['nome']))
                print("Quantidade: {}".format(insumos[iterador]['quantidade']))
                print("Fornecedor: {}".format(insumos[iterador]['fornecedor']))
                print("\n")

    elif(opcao == 3):
        if(len(insumos) == 0):
            print("Nenhum item cadastrado!")
            print("\n")
        else:
            print("Remover insumo:")
            codigo = int(input("Código: "))
            achou = False
            for iterador in range(0, len(insumos)):     
                if(insumos[iterador]['codigo'] == codigo):
                    achou = True
                    quantidade = int(input("Informe a quantidade: "))
                    if(insumos[iterador]['quantidade'] - quantidade > 0):
                        insumos[iterador]['quantidade'] -= quantidade
                    else:
                        print("Quantidade insuficiente!")
                        print("\n")
                else:
                    continue
            if(not achou):
                print("Insumo não encontrado!")
                print("\n")