lista_produtos = []
vendas_produto = []

def adicionar_produtos():
    adicionar_produtos = input("informe o produto que você deseja adicionar: \n")
    lista_produtos.append(adicionar_produtos)
    adicionar_quantidade_vendas = int(input("informe a quantidade de vendas que foi realizada do produto infotmado: \n"))
    vendas_produto.append(adicionar_quantidade_vendas)
def remover_produto():
    if len(lista_produtos) > 0:
        remover_produto = input("informe o produto que deseja remover: \n")
        indice_produto = lista_produtos.index(remover_produto)
        lista_produtos.pop(indice_produto)
        remover_vendas = int(input("informe a quantidade correspondente ao produto que você removeu: "))
        indice_vendas = vendas_produto.index(remover_vendas)
        vendas_produto.pop(indice_vendas)
    else:
        print("lista está vazia!!")
def produto_menos_vendido():
    if len(lista_produtos) > 0:
            produto_menos_vendas = min(vendas_produto)
            i = vendas_produto.index(produto_menos_vendas)
            produto_menos_vendas = lista_produtos[i]
            print('\nO produto menos vendido foi {}\n'.format(produto_menos_vendas))
    else:
        print("lista está vazia!!")
def produto_mais_vendido():
    if len(lista_produtos) > 0:
            produto_mais_vendas = max(vendas_produto)
            i=vendas_produto.index(produto_mais_vendas)
            produto_mais_vendas = lista_produtos[i]
            print('\nO produto mais vendido foi {}\n'.format(produto_mais_vendas))
    else:
        print("lista está vazia!!")
def listar_produtos():
    if len(lista_produtos) > 0:
            for i , j in zip(lista_produtos,vendas_produto): print("Foram vendidas {} unidades de {}\n".format(j,i)) 
    else: print("lista está vazia!!")
while True:
    print("bem vindo!! Essa é sua lista de controle de vendas!!\n")
    try:
        opçoes = int(input("informe o que você deseja fazer:\n[1]Adicionar a lista\n[2]remover\n[3]Ver produto menos vendido\
        \n[4]Produto mais vendido\n[5]listar\n"))
    except:
        print("Por favor, informe um valor válido!\n")
        continue
    if opçoes == 1:
        adicionar_produtos() 
    elif opçoes == 2:
       remover_produto()
    elif opçoes ==3:
        produto_menos_vendido()
    elif opçoes ==4:
        produto_mais_vendido()
    elif opçoes == 5:
       listar_produtos()
    elif opçoes == 6:
        listar_produtos()
        break
        
        

        
    
