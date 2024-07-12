from flask import Flask, request, Response
import requests
import base64
import os

app = Flask(__name__)

github_token = os.getenv('GITHUB_TOKEN')
if not github_token:
    print("GITHUB_TOKEN not set")

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

@app.route('/')
def indexPage():
    return """
    <!DOCTYPE HTML>
        <html>
            <head>
                <title>Page by Flask</title>
            </head>
            <body>
                <h1>This Page is stats index page. just check</h1>
            </body>
        </html>
        """

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

    godot_img_name = "godot.png"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    godot_img_path = os.path.join(current_dir, 'images', godot_img_name)

    try:
        with open(godot_img_path, "rb") as image_file:
            godot_logo_url = base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        return "Image file not found", 500

    svg = f"""
    <svg
        width="700"
        height="150"
        viewBox="0 0 700 150"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
    >
      <style>
        * {{
          font-family: 'Inter', 'Noto Sans KR', sans-serif;
        }}

        text {{
          fill: black;
        }}

        .profile-image {{
          filter: drop-shadow(rgba(0, 212, 151, 0.6) 0px 4px 8px);
        }}

        .header {{
          font-weight: 800;
          font-size: 20px;
        }}

        .bio {{
          font-size: 16px;
          overflow: hidden;
          text-overflow: ellipsis;
          display: inline-block;
          width: 400px;
          height: 30px;
          white-space: nowrap;
        }}

        .rank {{
          color: rgb(39, 226, 164);
          font-weight: 700;
          font-size: 24px;
        }}

        .exp-progress {{
          color: rgb(138, 143, 149);
          font-weight: 400;
          font-size: 14px;
        }}

        .flex-row {{
          display: flex;
          flex-direction: row;
          width: 235px;
          height: 50px;
          justify-content: flex-end;
        }}

        .item-box {{
          margin-left: 12px;
          padding-right: 10px;
          border-right: 1px solid black;
        }}

        .item-title {{
          font-weight: 400;
          font-size: 16px;
        }}

        .item-number {{
          font-weight: 600;
          font-size: 22px;
          text-align: right;
        }}
      </style>
      <rect
        data-testid="card-bg"
        x="0.5"
        y="0.5"
        rx="4.5"
        height="99%"
        stroke="#E4E2E2"
        width="699"
        fill="#FFFEFE"
      />
      <g class="profile" data-testid="card-title" transform="translate(20, 20)">
        <foreignObject class="profile-image" width="300" height="300" x="-20" y="-45">
          <xhtml:img width="120" height="120" src="data:image/png;base64,{godot_logo_url}"/>
        </foreignObject>
        <text x="105" y="20.5" class="header">{owner}</text>
        <g transform="translate(105, 28)">
          <foreignObject width="400" height="100">
            <xhtml:span class="bio">test</xhtml:span>
          </foreignObject>
        </g>
      </g>

      <g transform="translate(125, 80)">
        <foreignObject width="300" height="300">
          <xhtml:div class="rank">Noob</xhtml:div>
          <xhtml:div class="exp-progress">10/100</xhtml:div>
        </foreignObject>

        <foreignObject width="300" height="300" x="305" y="3">
          <xhtml:div class="flex-row box">
            <xhtml:div class="item-box box">
              <xhtml:div class="item-title">Total Commits</xhtml:div>
              <xhtml:div class="item-number">{total_commit}</xhtml:div>
            </xhtml:div>
          </xhtml:div>
        </foreignObject>
      </g>

      <g class="badge" data-testid="card-badge" transform="translate(585, 10)">
      </g>
    </svg>
    """

    return Response(svg, mimetype='image/svg+xml')

if __name__ == "__main__":
    app.run(debug=True)