from flask import Flask, request, Response, send_from_directory
import requests
import os

app = Flask(__name__)

github_token = os.getenv('GITHUB_TOKEN')
if not github_token:
    raise EnvironmentError("GitHub token not set in environment variables")

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

def generate_svg(owner, godot_logo_url, total_commit):
    svg = f"""
    <svg width="400" height="150" xmlns="http://www.w3.org/2000/svg">
      <style>
        .title {{ font: bold 20px sans-serif; }}
        .stats {{ font: 16px sans-serif; }}
      </style>
      <rect width="400" height="150" fill="white" stroke="black" stroke-width="1"/>
      <image href="{godot_logo_url}" x="10" y="10" width="50" height="50"/>
      <text x="70" y="30" class="title">{owner}</text>
      <text x="70" y="50" class="stats">Rank: Noob</text>
      <text x="70" y="70" class="stats">Progress: 10/100</text>
      <text x="70" y="90" class="stats">Total Commits: {total_commit}</text>
    </svg>
    """
    return svg

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

    godot_logo_url = request.host_url + 'images/godot.png'
    svg = generate_svg(owner, godot_logo_url, total_commit)

    return Response(svg, mimetype='image/svg+xml')

if __name__ == "__main__":
    app.run(debug=True)