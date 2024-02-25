from github import Github
from config import config as cfg

apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)
for repo in g.get_user().get_repos():
    print(repo.name)

g = Github(apikey)
repo = g.get_repo("ShamansIT/aprivateone")
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)

newContents = contentOfFile + " more stuff \n"
print(newContents)

gitHubResponse = repo.update_file(fileInfo.path, "updated by prog",
                                  newContents, fileInfo.sha)
print(gitHubResponse)

apikey = cfg["githubkey"]
