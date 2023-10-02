import requests
import json
import os

# Classe recebe como parâmetro o nome do usuário.
class ListaDeRepositorios():

    def __init__(self, usuario):
        self._usuario = usuario

# Função que faz a requisição na API
    def requisicao_api(self):
        resposta = requests.get(
            f'https://api.github.com/users/{self._usuario}/repos')
        
# Filtra a resposta da API 
    def requisicao_api(self):
        resposta = requests.get(
            f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code
        
# Copiar Repositórios para o arquivo
    def copiar_repositorios_para_arquivo(self, nome_arquivo):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            with open(nome_arquivo, 'w') as arquivo:
                for repo in dados_api:
                    arquivo.write(repo['name'] + '\n')

        else:
            print(f"Erro ao obter os dados da API. Código de status: {dados_api}")

# Listar repositorios
    def imprime_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)

# Transformar saída em arquivo
repositorios = ListaDeRepositorios('randeldarlei')
repositorios.copiar_repositorios_para_arquivo('repositorios.txt')

