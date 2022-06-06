# --------------------------------------------------
#          Grupo 1 - Cenário: Panificadora          
# --------------------------------------------------
#  Matrícula | Nome Completo
# --------------------------------------------------
#  04100558  | Caio de Oliveira Ferreira
#  04110671  | Gabriel Elieze Barros de Souza Gomes
#  04099705  | Jamille Costa de Souza
#  04086834  | Tiago Carlos Ferreira de Oliveira
# --------------------------------------------------

import pprint

# --------------------------------------------------
#                       Base
# --------------------------------------------------

produtos = [
    {'codigo': 1, 'nome': 'Pão Bengala', 'preco': 'R$ 0,30', 'quantidade': 100},
    {'codigo': 2, 'nome': 'Pão Brioche', 'preco': 'R$ 0,75', 'quantidade': 100},
    {'codigo': 3, 'nome': 'Pão Careca', 'preco': 'R$ 0,50', 'quantidade': 100},
    {'codigo': 4, 'nome': 'Pão Massa Fina', 'preco': 'R$ 0,50', 'quantidade': 100},
    {'codigo': 5, 'nome': 'Pão de Milho', 'preco': 'R$ 0,50', 'quantidade': 100},
    {'codigo': 6, 'nome': 'Café', 'preco': 'R$ 2,00', 'quantidade': 50},
    {'codigo': 7, 'nome': 'Coxinha', 'preco': 'R$ 2,50', 'quantidade': 75},
    {'codigo': 8, 'nome': 'Pastel', 'preco': 'R$ 2,50', 'quantidade': 75},
    {'codigo': 9, 'nome': 'Pão de Queijo', 'preco': 'R$ 1,50', 'quantidade': 75},
    {'codigo': 10, 'nome': 'Monteiro Lopes', 'preco': 'R$ 1,50', 'quantidade': 150},

]

# --------------------------------------------------

def menu():
    print(
        '\nBem-vindo(a) à Panificadora Bom Jesus.\n\n[Opções]\n1. Listar produtos no estoque\n2. Inserir produto no estoque\n3. Remover produto do estoque\n4. Registrar item do cliente'
    )
    return int(input('\n-> Escolha uma opção: '))

# --------------------------------------------------

opcao = menu()

# Listar produtos no estoque
if opcao == 1:
    print('\nProdutos disponíveis no estoque:\n')
    pprint.pprint(produtos)

    print('\n[Opções]\n1. Voltar ao menu principal\n2. Encerrar o programa')
    escolha = int(input('\n-> Escolha uma opção: '))

    if escolha == 1:
        menu()
    elif escolha == 2:
        print('\nO programa foi encerrado.')

# Inserir produto no estoque
elif opcao == 2:
    codigo = len(produtos) + 1
    nome = str(input('-> Qual o nome do produto? '))
    preco = str(input('-> Qual o valor do produto? R$ '))
    quantidade = int(input('-> Qual a quantidade do produto? '))
    
    novos_produtos = {
        'codigo': codigo,
        'nome': nome,
        'preco': 'R$ ' + preco,
        'quantidade': quantidade,
    }
    produtos.append(novos_produtos)

    print('Produto cadastrado com sucesso:')
    pprint.pprint(produtos)

    print('\n[Opções]\n1. Voltar ao menu principal\n2. Encerrar o programa')
    escolha = int(input('\n-> Escolha uma opção: '))

    if escolha == 1:
        menu()
    elif escolha == 2:
        print('\nO programa foi encerrado.')

# Remover produto do estoque
elif opcao == 3:
    print('\nOpção 3')

# Registrar item do cliente
elif opcao == 4:
    print('\nOpção 4')

# Opção inexistente
else:
    print('\nA opção informada não está formato correto. Por favor, tente novamente.')