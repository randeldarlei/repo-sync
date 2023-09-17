import requests
import os

# AUTH GITHUB_API
access_token = os.environ.get('GITHUB_TOKEN')

# REPOS VAR DECLARATION
repos_url = "https://api.github.com/randeldarlei/repos"

# MAKE REQUEST FROM GITHUB API
headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}
response = requests.get(repos_url, headers=headers)

# VALIDATE REQUEST
if response.status_code == 200:
    repos = response.json()

    for repo in repos:
        repo_name = repo["Dialog-Bot"]
        archive_url = f"https://api.github.com/repos/{repo['full_name']}/zipball"
        
        # GITPYTHON LIB DOWNLOAD A REPO.

        print(f"Download {repo_name}...")
        response = requests.get(archive_url, headers=headers, stream=True)

        if response.status_code == 200:
        # MAKE A ZIP FILE AND SAVE FILES
            os.makedirs(repo_name, exist_ok=True)
            zip_file_path = os.path.join(repo_name, f"{repo_name}.zip")
            
            with open(zip_file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"{repo_name} download susscesfull.")
        else:
            print(f"Download failed {repo_name}.")
else:
    print("Error cannot access GITHUB API.") 