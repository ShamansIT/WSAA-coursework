from github import Github
from config import token

# Constants
ACCESS_TOKEN = token
REPO_NAME = 'https://api.github.com/repos/ShamansIT/WSAA-coursework'
FILE_PATH = 'assignments/Assignment04_github/file.txt'
OLD_NAME = 'Andrew'
NEW_NAME = 'Serhii'

# Initialize PyGithub with your access token
g = Github(token)

# Get the repository
repo = g.get_repo(REPO_NAME)

# Get the file
file_contents = repo.get_contents(FILE_PATH)

# Decode the file contents and replace the old name with the new name
decoded_content = file_contents.decoded_content.decode('utf-8')
updated_content = decoded_content.replace(OLD_NAME, NEW_NAME)

# Commit the changes back to GitHub
repo.update_file(FILE_PATH, "Replace 'Andrew' with 'Serhii'",
                 updated_content, file_contents.sha)

print(f"Updated file {FILE_PATH} in repository {REPO_NAME}")
