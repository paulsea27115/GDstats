import requests
import time
                                         
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢄⢔⢆⢏⢎⢎⠄⠀⠀⠀⠀⠀⠀⢀⢎⢎⢇⢇⢆⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⢸⢸⢸⢸⢸⢸⠀⠀⡀⠀⠀⢀⢎⢎⢎⢎⢎⢎⢎⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⢕⢕⢕⢕⢕⢕⢕⢭⢣⢣⢫⢹⢸⢸⢸⢸⢸⢸⢸⢸⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⡠⡰⡱⡱⡱⡕⡕⣕⢕⢕⢕⢕⢕⢕⢕⢕⡕⡵⡱⡕⡕⡕⡆⡄⡀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢀⢆⢇⢇⢆⢄⢀⢔⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢤⢀⢠⢰⢪⢱⠥⡀⠀⠀⠀⠀
#⠀⠀⠀⡰⡱⡱⡱⡱⡕⡕⡕⡕⡕⡕⡕⣕⢕⢇⢇⢇⢇⢇⢇⢗⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢭⢢⠀⠀⠀
#⠀⠀⠘⡜⡜⡜⣜⢜⢜⢜⢜⢜⢜⢜⢎⢎⢎⢎⢎⢎⢇⢇⢇⢇⢇⢇⢏⢎⢎⢮⢪⢪⡪⡪⡪⡣⡣⡳⡱⡱⡱⡕⡕⡕⡕⡕⡕⠅⠀⠀
#⠀⠀⠀⠘⢜⢜⢜⢜⢜⢜⢜⡪⡕⡕⡕⡕⡕⡕⡕⡕⡕⡕⣕⢕⢵⢱⢱⢱⡱⡱⡱⡱⡱⡱⡱⡱⡱⡱⡱⡱⡱⡱⡱⡱⡹⡸⠈⠀⠀⠀
#⠀⠀⠀⠀⠈⡪⡪⡪⡪⡪⡣⡣⠣⠃⠣⠃⠇⡇⡧⡓⡭⡪⡪⡪⡪⡪⡪⡕⡎⡎⡎⡎⡎⡎⠪⠊⠪⠪⡪⣪⢪⡪⡪⡪⡪⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⡣⡣⡫⡪⡪⡊⠀⢀⡠⣤⢤⣀⠈⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⠜⠀⣀⣤⢤⢄⠀⠈⠪⡪⡪⡪⡪⡎⠄⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⡣⡣⡣⡣⣓⠀⠀⣞⢾⢽⣝⣞⡆⠀⡇⡇⡇⡇⡇⠀⠀⢑⢕⢕⢕⢕⠁⣸⣳⢽⢽⢽⣕⠀⠀⡣⡣⡣⡣⣓⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⡣⡣⡣⡣⣣⢀⠀⢫⢯⣗⣗⣗⠏⠠⡪⡪⡪⡪⡂⠀⠀⢐⢕⢕⢕⢕⠄⠸⣞⡽⣝⡷⡝⠀⢀⢇⢇⢇⢇⠧⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⡣⡣⡣⡫⡪⣒⢄⢀⠁⠃⠃⡁⡄⡇⡇⡇⡏⡎⡆⠀⠀⢐⢕⢕⢕⢇⢏⢄⡈⠉⠑⠁⡀⡄⡎⡎⡎⡎⡎⡇⠂⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢖⢔⢕⢕⢝⢜⢜⢜⢜⢜⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢭⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠑⠑⠑⠑⠕⠑⠕⠕⡕⡕⡕⡕⡕⡕⡕⣕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⠕⠕⠑⠕⠑⠑⠑⠁⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⡆⡆⡆⡆⡤⡠⠄⠀⢸⢸⢸⢸⢸⢸⡸⡀⠁⠈⠀⠁⠈⠀⠁⠈⠨⡪⡣⡣⡳⡱⡱⡑⠀⠠⡄⡤⡰⡰⡢⣒⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⢕⢕⢕⢕⢕⢕⢕⠀⠱⠱⠕⢕⢕⢕⢕⠀⢈⠮⡍⡇⡏⡝⡜⡄⠀⢕⢕⠕⠕⠕⠕⠕⠀⢜⢜⢜⢜⢜⢜⢆⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠘⡜⡜⡎⡎⡮⣒⢄⢄⣀⣀⢀⡀⡀⡀⡀⢔⢕⢕⢕⢕⢕⢕⢅⢀⢀⢀⡀⡠⡀⡄⡄⡄⡕⡕⡕⣕⢕⢕⠅⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠘⢜⢜⢜⢜⢔⢕⢕⡲⡸⡸⡸⡸⡸⡸⡸⡸⡪⡪⡪⡣⡣⡫⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⠂⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠈⠪⢪⢪⢪⢪⢪⢪⢪⢪⢪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠃⠣⠣⠣⡳⡱⡱⡱⡹⡸⡸⡪⡪⡪⣪⢪⡪⡪⣪⢪⠺⠸⠑⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠁⠁⠁⠁⠁⠉⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# This is a project where you can show your love of Godot to others.
# This code shows the repositories your GDScript is used in and the total number of commits, although it's still CLI. We'll be updating it to be distributed as a badge in the future.


# This function serves to get a list of all repositories for a specific GitHub user.
def get_user_repos(username, token):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
        headers = {"Authorization": f"token {token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            page_repos = response.json()
            if not page_repos:
                break
            repos.extend(page_repos)
            page += 1
        else:
            print(f"Error: {response.status_code}")
            return None
    return repos

# This function serves to get information about the languages used in a particular repository.
def get_repo_languages(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error:{owner}/{repo}: {response.status_code}")
        return None

# This function serves to get the total number of commits in a specific repository.
def get_repo_commits(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        commits = response.json()
        return len(commits)
    else:
        print(f"Error:{owner}/{repo}: {response.status_code}")
        return 0

if __name__ == "__main__":
    owner = ""
    token = ""  # Hardcoded code for testing purposes. We will remove it in the future.

    repos = get_user_repos(owner, token)
    if repos is None:
        exit(1)

    gdscript_repos = []

    for repo in repos:
        languages = get_repo_languages(owner, repo['name'], token)
        if languages and 'GDScript' in languages:
            gdscript_repos.append(repo['name'])

    print(f"Owner: {owner}")
    print(f"Repositories using GDScript:")
    
    total_commit = 0

    for repo in gdscript_repos:
        commits = get_repo_commits(owner, repo, token)
        total_commit += commits

        print(f"- {repo}: {commits} commits")
    print(f"Total GDScript commits: {total_commit}")

