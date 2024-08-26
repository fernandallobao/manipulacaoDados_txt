import os

def exibir_menu():
    print('1 - Ler arquivo')
    print('2 - Gravar novos dados no arquivo')
    print('3 - Sair do programa')

# função para gravar novos dados
def gravar_arquivo(dados, nome, email, porfissao):
    dados += f'\n\n{'-'*30}\n\nNome: {nome}\nEmail: {email}\n Profissão: {porfissao}'
    with open('arquivo.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(dados)

# função de leitura de arquivo
def ler_arquivo():
    with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
        dados = arquivo.read()
    return dados

#programa principal
if __name__ == '__main__':
    while True:
        dados = ler_arquivo()
        exibir_menu()
        op = input('Opção desejada: ')
        os.system('cls')
        match op:
            case '1':
                print(f'\n{dados}\n')
                continue
            case '2':
                print('NOVO CADASTRO:\n')
                novo_nome = input('Informe o nome do novo usuário: ')
                novo_email = input('Informe o nome do novo e-mail: ')
                nova_profissao = input('Informe o nome do novo profissão: ')
                gravar_arquivo(dados, novo_nome, novo_email, nova_profissao)
            case '3':
                print('Programa finalizado!')
                break
            case _:
                print('Opção inválida!')
                continue