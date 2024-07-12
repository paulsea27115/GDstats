from flask import Flask, request, Response, send_from_directory, url_for
import requests
import os
from svg_generator import generate_svg

app = Flask(__name__)

github_token = os.getenv('GITHUB_TOKEN')

def get_user_repos(username):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
        headers = {"Authorization": f"token {github_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            page_repos = response.json()
            if not page_repos:
                break
            repos.extend(page_repos)
            page += 1
        else:
            print(f"Error fetching repositories: {response.status_code}, {response.text}")
            return None
    return repos

def get_repo_languages(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching languages for {repo}: {response.status_code}, {response.text}")
        return None

def get_repo_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        commits = response.json()
        return len(commits)
    else:
        print(f"Error fetching commits for {repo}: {response.status_code}, {response.text}")
        return 0

@app.route('/images/<path:filename>')
def send_image(filename):
    return send_from_directory('images', filename)

@app.route('/badge')
def badge():
    owner = request.args.get('username')
    if not owner:
        return "Username not provided", 400
    
    repos = get_user_repos(owner)
    if repos is None:
        return "Error fetching repositories", 500

    gdscript_repos = []
    for repo in repos: 
        languages = get_repo_languages(owner, repo['name'])
        if languages and 'GDScript' in languages:
            gdscript_repos.append(repo['name'])

    total_commit = 0
    for repo in gdscript_repos:
        commits = get_repo_commits(owner, repo)
        total_commit += commits

    godot_logo_url = url_for('send_image', filename='godot.png', _external=True)
    svg = generate_svg(owner, godot_logo_url, total_commit)

    return Response(svg, mimetype='image/svg+xml')

if __name__ == "__main__":
    app.run(debug=True)
