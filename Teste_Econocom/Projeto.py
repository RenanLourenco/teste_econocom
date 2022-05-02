


print("###########################")
print("###########################")
print("   Lanches da Quarentena  ")
print("###########################")
print("###########################")

while True:
    print("Clientes, digite [1]")
    print("Produtos, digite [2]")
    print("Pedidos,  digite [3]")
    print("Exibir clientes, digite [4]")
    print("Exibir pedidos,digite [5] ")
    print("Exibir total de pedidos para cada cliente [6]")
    print("Exibir total de pedidos para cada produto [7]")
    print("Exibir valor total em reais faturados até o momento [8]")
    print("Exportar dados para arquivo .txt [9]")
    print("Finalizar programa [10]")
    opcao = int(input())



    if opcao == 1:
        print("Gostaria de adicionar clientes? Sim/Nao")
        opcao_clientes = input()
        if opcao_clientes.lower() == "sim":
            print("Gostaria de adicionar quantos clientes?")
            quantidade_cadastro_clientes = int(input())
            i = 0
            clientes = []
            telefones = []
            while i < quantidade_cadastro_clientes:
                clientes.append(input("Insira o Nome do cliente: "))
                telefones.append(input("Insira o Telefone do cliente: "))
                i += 1
                print("Nome e telefone Registrado!")
        elif opcao_clientes.lower() == "nao":
            print("Gostaria de Editar informações de algum cliente? Sim/Nao")
            editar_informacoes = input()
            if editar_informacoes.lower() == "sim":
                print(clientes)
                print(telefones)
                print("Qual informação gostaria de mudar? Nome/Telefone")
                mudanca = input()
                if mudanca.lower() == "nome":
                    print(clientes)
                    print("Qual informação gostaria de mudar?")
                    resp_edit_clientes = input()
                    indice = clientes.index(resp_edit_clientes)
                    print("Insira nova informação: ")
                    nova_inf = input()
                    clientes[indice] = nova_inf
                    print(clientes)
                elif mudanca.lower() == 'telefone':
                    print(telefones)
                    print("Qual informação gostaria de mudar?")
                    resp_edit_telefones = input()
                    indice = telefones.index(resp_edit_telefones)
                    print("Insira nova informação: ")
                    nova_inf = input()
                    telefones[indice] = nova_inf
                    print(telefones)
            else:
                print("Gostaria de Excluir alguma informação dos clientes? Sim/Nao")
                excluir_informações = input()
                if excluir_informações.lower() == "sim":
                    print(clientes)
                    print(telefones)
                    print("Qual informação gostaria de excluir? Nome/Telefone")
                    exclusao = input()
                    if exclusao.lower() == "nome":
                        indice_exclusao = clientes.index(exclusao)
                        clientes.remove(exclusao)
                        print(clientes)
                    else:
                        indice_exclusao = telefones.index(exclusao)
                        telefones.remove(exclusao)
                        print(telefones)
    elif opcao == 2:
        print("Gostaria de adicionar novos produtos? Sim/Nao")
        opcao_produtos = input()
        if opcao_produtos.lower() == "sim":
            print("Gostaria de adicionar quantos produtos?")
            quantidade_cadastro_produtos = int(input())
            i = 0
            produtos = []
            valores = []
            while i < quantidade_cadastro_produtos:
                produtos.append(input("Insira o produto: "))
                valores.append(str(input(("Insira o valor:  (Somente numero!)"))))
                i += 1
                print("Produtos: ")
                print(produtos)
                print("Valores: ")
                print(valores)
        elif opcao_produtos.lower() == "nao":
            print("Gostaria de Editar informações de algum produto? Sim/Nao")
            editar_informacoes_produto = input()
            if editar_informacoes_produto.lower() == "sim":
                print("Voce gostaria de mudar o nome ou valor do produto? Nome/Valor")
                mudanca_produtos = input()
                if mudanca_produtos.lower() == "nome":
                    print("Qual produto seria?")
                    print(produtos)
                    resp_edit_produtos = input()
                    indice_produtos = produtos.index(resp_edit_produtos)
                    print("Insira nova informação: ")
                    nova_inf_produtos = input()
                    produtos[indice_produtos] = nova_inf_produtos
                    print(produtos)
                    print(valores)
                else:
                    print("Qual valor seria?")
                    print(valores)
                    resp_edit_valor = input()
                    indice_produtos = valores.index(resp_edit_valor)
                    print("Insira nova informação: ")
                    nova_inf_produtos = input()
                    valores[indice_produtos] = nova_inf_produtos
                    print(produtos)
                    print(valores)

            else:
                print("Gostaria de Excluir alguma informação dos produtos Sim/Nao")
                excluir_informações_produtos = input()
                if excluir_informações_produtos.lower() == "sim":
                    print(produtos)
                    print("Qual informação gostaria de excluir?")
                    exclusao_produtos = input()
                    indice_exclusao_produtos = produtos.index(exclusao_produtos)
                    produtos.remove(exclusao_produtos)
                    print(produtos)
                else:
                    pass
    elif opcao == 3:
        print("Gostaria de fazer um novo pedido? Sim/Não")
        opcao_pedido = input()
        if opcao_pedido.lower() == "sim":
            print("Quantos pedidos? ")
            qntd_pedidos = int(input())
            i = 0
            pedidos = []
            qntd_pedidocliente = []
            qntd_produto = []
            faturamento = []
            while i < qntd_pedidos:
                print("Para qual cliente seria? ")
                print(clientes)
                opcao_cliente = input()
                qntd_pedidocliente.append(opcao_cliente)
                indice_opcao_cliente = clientes.index(opcao_cliente)
                print("Qual produto? ")
                print(produtos)
                opcao_produto_pedido = input()
                qntd_produto.append(opcao_produto_pedido)
                indice_opcao_produto = produtos.index(opcao_produto_pedido)
                pedidos.append("Cliente: {} Produto: {} Valor total: {} reais".format(clientes[indice_opcao_cliente],produtos[indice_opcao_produto],valores[indice_opcao_produto]))
                faturamento.append(int(valores[indice_opcao_produto]))
                i += 1
                print("Pedido criado com sucesso!")
        else:
            pass

    elif opcao == 4:
        print("Clientes:")
        print(clientes)
        print("Respectivos Telefones:")
        print(telefones)

    elif opcao == 5:
        print(pedidos)

    elif opcao == 6:
        print("Qual Cliente voce deseja verificar?")
        print(clientes)
        ver_cliente = input()
        print("O cliente {}, tem o total de {} pedidos ".format(ver_cliente,qntd_pedidocliente.count(ver_cliente)))

    elif opcao == 7:
        print("Qual Produto voce deseja verificar?")
        print(produtos)
        ver_produto = input()
        print("O produto {}, tem o total de {} pedidos".format(ver_produto,qntd_produto.count(ver_produto)))

    elif opcao == 8:
        faturamento_total = sum(faturamento)
        print("O faturamento total é de: {} reais".format(faturamento_total))

    elif opcao == 9:
        with open('dados.txt','a') as arquivo:
            arquivo.write("\n"+"Pedidos: " + "\n" + str(pedidos) +"\n"+ "Clientes: " + "\n" + str(clientes) +"\n"+ "Telefones: "+"\n"+str(telefones)+ "\n"+"Produtos: "+"\n"+str(produtos)+"\n"+ "Faturamento: " + "\n" + str(sum(faturamento)) + " reais" + "\n")

    elif opcao == 10:
        break




























