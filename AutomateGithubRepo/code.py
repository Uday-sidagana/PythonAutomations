import os
import time
import subprocess
from dotenv import load_dotenv
import requests

# Load environmental variables from .env file
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Add a timestamp to ensure unique repo names
REPO_NAME = f"NewRepo_{int(time.time())}"

def folder():
    # Get the directory from the user
    directory = input("Directory Format: /Users/macbookair/Desktop/python/AutomationPython/AutomateGithubRepo/ ")
    try:
        os.makedirs(directory, exist_ok=True)  # Use makedirs to ensure parent directories are created
        print(f"Folder '{directory}' created successfully.")
        return directory
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def create_github_repo(repo_name, token):
    """Create a GitHub repository using the GitHub API."""
    url = 'https://api.github.com/user/repos'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'name': repo_name,  # The name of the repository
    }

    # Make a POST request to the GitHub API
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
        return response.json()['clone_url']
    elif response.status_code == 422:
        print(f"Repository '{repo_name}' already exists.")
        return None
    else:
        print(f"Failed to create repository: {response.json()}")
        return None

def push_to_github(directory, repo_url, repo_name):
    """Initialize git, create README.md, commit, and push to GitHub."""
    # Initialize the git repository
    print("Initializing local git repository...")
    subprocess.run(['git', 'init'], cwd=directory)

    # Create README.md file
    print(f"Creating README.md file in '{directory}'...")
    readme_path = os.path.join(directory, 'README.md')
    with open(readme_path, 'w') as f:
        f.write(f"# {repo_name}\nThis is an automatically created repository.")

    # Add, commit, and push
    print("Adding README.md to the local repository...")
    subprocess.run(['git', 'add', 'README.md'], cwd=directory)

    print("Committing changes...")
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=directory)

    print("Setting the branch to 'main'...")
    subprocess.run(['git', 'branch', '-M', 'main'], cwd=directory)

    print(f"Adding remote repository '{repo_url}'...")
    subprocess.run(['git', 'remote', 'add', 'origin', repo_url], cwd=directory)

    print("Pushing changes to GitHub...")
    subprocess.run(['git', 'push', '-u', 'origin', 'main'], cwd=directory)

def main():
    # Step 1: Create the local folder
    directory = folder()
    
    if directory:
        # Step 2: Create the GitHub repository
        repo_url = create_github_repo(REPO_NAME, GITHUB_TOKEN)
        
        # Step 3: Push the changes to GitHub
        if repo_url:
            push_to_github(directory, repo_url, REPO_NAME)
        else:
            print("Repository creation failed. Aborting push process.")

if __name__ == "__main__":
    main()
