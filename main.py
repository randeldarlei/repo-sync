import requests
import os

# Seu token de acesso pessoal do GitHub
access_token = "SEU_TOKEN_AQUI"

# URL da API do GitHub para listar seus repositórios
repos_url = "https://api.github.com/user/repos"

# Cabeçalho HTTP com o token de acesso
headers = {
    "Authorization": f"token {access_token}"
}

# Fazendo a solicitação GET para a API do GitHub
response = requests.get(repos_url, headers=headers)

# Verificando se a solicitação foi bem-sucedida
if response.status_code == 200:
    repos = response.json()

    for repo in repos:
        repo_name = repo["name"]
        archive_url = f"https://api.github.com/repos/{repo['full_name']}/zipball"
        
        # Aqui você pode usar uma biblioteca Python para clonar o repositório, como o GitPython.

        print(f"Baixando {repo_name}...")
        response = requests.get(archive_url, headers=headers, stream=True)

        if response.status_code == 200:
        # Crie uma pasta para cada repositório e salve o arquivo zip lá
            os.makedirs(repo_name, exist_ok=True)
            zip_file_path = os.path.join(repo_name, f"{repo_name}.zip")
            
            with open(zip_file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"{repo_name} baixado com sucesso.")
        else:
            print(f"Falha ao baixar {repo_name}.")
else:
    print("Falha ao acessar a API do GitHub.")