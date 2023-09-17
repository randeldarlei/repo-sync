import requests

# AUTH GITHUB_API
token = "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"
url = "https://api.github.com/repositories"
headers = {
    'Accept': 'application/vnd.github+json' ,
    'Authorization': f'Bearer {token}' ,
    'X-GitHub-Api-Version': '2022-11-28'
}
# Realiza a chamada de API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data =response.json()
    for repo in data:
        print(repo['name'])
else:
    print(f"Erro na chamada de API: {response.status_code} - {response.text}") 
