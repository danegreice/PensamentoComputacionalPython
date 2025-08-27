unidadesMedida = {1: "Quilograma", 2: "Grama", 3: "Litro", 4: "Mililitro", 5: "Unidade", 6: "Metro", 7: "Centímetro"}
listaProdutos = []

class Item:
    id = 0
    def __init__(self, nome, unMedida, quantidade, descricao):
        Item.id += 1
        self.id = Item.id
        self.nome = nome
        self.unMedida = unMedida
        self.quantidade = quantidade
        self.descricao = descricao

def adicionarItem(lista):
    print("Adicione as informações do item a ser adicionado")
    nome = input("Nome do item: ")
    print("Unidade de medida: ")
    print("1 - Quilograma")
    print("2 - Grama")
    print("3 - Litro")
    print("4 - Mililitro")
    print("5 - Unidade")
    print("6 - Metro")
    print("7 - Centímetro")
    op = int(input("Digite a opção: "))
    unMedida = unidadesMedida[op]
    quantidade = int(input("Quantidade do item: "))
    descricao = input("Descricao: ")
    print("Adicionando...")
    lista.append(Item(nome, unMedida, quantidade, descricao))
    print("Item adicionado com sucesso!")

def listarProdutos(lista):
    print("Lista de produtos")
    if (len(lista) > 0):
        for i in lista:
            print("Id: ", i.id, " - Nome: ", i.nome, "Quantidade: ", i.quantidade, "Descrição: ", i.descricao)
    else:
        print("Nenhum item encontrado.")

def removerItem(lista):
    listarProdutos(lista)
    id = int(input("Digite o id do item que deseja remover: "))
    print("Removendo...")
    lista.remove(id)

def buscarItem(lista):
    nome = input("Digite o nome ou parte do nome do item que deseja buscar: ")
    listaEncontrados = []
    for i in lista:
        if nome in i.nome:
            listaEncontrados.append(i)

    print("Foram encontrado(s): ", len(listaEncontrados), " itens")
    listarProdutos(listaEncontrados)

def carrinhoCompras():
    while True:
        print("Seja bem vindo ao Carrinho de Compras")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Listar produtos")
        print("4 - Pesquisar produto")
        print("5 - Sair")

        operacao = int(input("Selecione uma opção: "))

        if operacao == 5:
            print("Obrigada por utilizar a lista de compras!")
            break

        if operacao not in range(1, 5):
            print("Opção invalida. Tente novamente.")
            continue

        if operacao == 1:
            adicionarItem(listaProdutos)
            listarProdutos(listaProdutos)
        elif operacao == 2:
            removerItem(listaProdutos)
            listarProdutos(listaProdutos)
        elif operacao == 3:
            listarProdutos(listaProdutos)
        elif operacao == 4:
            buscarItem(listaProdutos)


carrinhoCompras()