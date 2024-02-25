from git import Repo
import os

# Constants
REPO_PATH = 'https://github.com/ShamansIT/WSAA-coursework/tree/main/assignments/Assignment04_github'
FILE_PATH = 'https://github.com/ShamansIT/WSAA-coursework/tree/main/assignments/Assignment04_github/file.txt'
NEW_NAME = 'Serhii'

# Repository path check
if not os.path.isdir(REPO_PATH):
    print("Repository path does not exist.")
else:
    # Initialize the repository object
    repo = Repo(REPO_PATH)

    # Ensure not working with a dirty repo
    if repo.is_dirty():
        print("The repository has uncommitted changes. Please commit or stash them before running this script.")
    else:
        # Full path to the target file
        target_file_path = os.path.join(REPO_PATH, FILE_PATH)

        # Read the file, replace "Andrew" with "Serhii", and write the changes
        if os.path.exists(target_file_path):
            with open(target_file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            updated_content = content.replace("Andrew", NEW_NAME)

            with open(target_file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

            # Using GitPython to commit the changes
            try:
                repo.git.add(FILE_PATH)
                repo.git.commit('-m', 'Replace "Andrew" with "Serhii"')
                repo.git.push()
                print("Changes have been pushed successfully.")
            except Exception as e:
                print(f"An error occurred while trying to push changes: {e}")
        else:
            print(f"File does not exist at {target_file_path}")
