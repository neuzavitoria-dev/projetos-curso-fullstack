lista_de_produtos = []
while True:
    menu = input("""Menu de Opição
    1 - ADICIONAR PRODUTO
    2 - VER TODOS OS PRODUTOS
    3 - EDITAR PRODUTO
    4 - EXCLUIR PRODUTO 
    0 - SAIR
    """)

    match menu:
        case "1":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            novo_produto = {
                "Nome": nome,
                "Preço": preco
            }
            lista_de_produtos.append(novo_produto)
            print("Produto cadastrado com sucesso!")
        
        case "2":
            for element in lista_de_produtos:
                print(f"""
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                {element['Nome']}, {element['Preço']:.2f}
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                """)

        case "3":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("LISTA DE PRODUTOS")
            for element in lista_de_produtos:
                print(f"Nome: {element['Nome']} - {element['Preço']:.2f}")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")    

            escolha = input("Digite o Nome do produto que deseja editar")
            produto_encontrado = 0
            for element in lista_de_produtos:
                if element['Nome'].lower() == escolha.lower():
                    produto_encontrado += 1
                    while True:
                        menu_editar = input("""
                ESCOLHA O QUE VOCÊ QUER EDITAR
                1 - NOME
                2 - PREÇO
                0 - VOLTA
                """)
                        
                        match menu_editar:
                            case "1":
                                novo_nome = input("Digite o novo nome do produto: ")
                                element['Nome'] = novo_nome.lower()
                                print("Nome alterado com sucesso!")
                            case "2":
                                novo_preco = float(input("Digite o novo preço do produto: "))
                                element['Preço'] = novo_preco
                                print("Preço alterado com sucesso!")
                            case "0":
                                break
                            case _:
                                print("Opição invalida.")
            if produto_encontrado == 0:
                print("Produto não encontrado.")
        
        case "4":
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("LISTA DE PRODUTOS")
            for element in lista_de_produtos:
                print(f"Nome: {element['Nome']} - {element['Preço']:.2f}")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")   
            escolha = input("Digite o Nome do produto que deseja excluir: ")
            produto_encontrado = 0
            for element in lista_de_produtos:
                if element['Nome'].lower() == escolha.lower():
                    lista_de_produtos.remove(element)
                    produto_encontrado += 1
                    print("Produto excluido com sucesso!")
            if produto_encontrado == 0:
                print("Produto não encontrado.")

        case "0":
            break

        case _:
            print("Opição invalida.") 
