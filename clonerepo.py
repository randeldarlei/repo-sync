from github import Github
from github import Auth

auth = Auth.Token("GITHUB_TOKEN")

g = Github(auth=auth)

for repo in g.get_user().get_repos():
    print(repo.name)

g.close
