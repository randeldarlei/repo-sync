import requests
import json
import os
import boto3

# Autenticação na AWS
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
region_name = os.environ.get("AWS_DEFAULT_REGION")

s3 = boto3.resource('s3')

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

for bucket in s3.buckets.all():
    print(bucket.name)

with open('repositorios.txt', 'rb') as data:
    s3.Bucket('my-bucket').put_object(Key='repositorios.txt', Body=data)    
