import requests
import json
import os

# Autenticação na AWS
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
region_name = os.environ.get("AWS_DEFAULT_REGION")

s3 = boto3.resource('s3')

# Classe recebe como parâmetro o nome do usuário.
class RepoList():

    def __init__(self, user):
        self._user = user

# Função que faz a requisição na API
    def request_api(self):
        response = requests.get(
            f'https://api.github.com/users/{self._user}/repos')
        
# Filtra a resposta da API 
    def request_api(self):
        response = requests.get(
            f'https://api.github.com/users/{self._user}/repos')
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
# Copiar Repositórios para o arquivo
    def copy_repo_to_file(self, file_name):
        data_api = self.request_api()
        if type(data_api) is not int:
            with open(file_name, 'w') as file:
                for repo in data_api:
                    file.write(repo['name'] + '\n')

        else:
            print(f"Erro ao obter os dados da API. Código de status: {data_api}")

# Listar repositorios
    def print_repos(self):
        data_api = self.request_api()
        if type(data_api) is not int:
            for i in range(len(data_api)):
                print(data_api[i]['name'])
        else:
            print(data_api)

# Transformar saída em arquivo
repositorios = RepoList('randeldarlei')
repositorios.copy_repo_to_file('repositorios.txt')