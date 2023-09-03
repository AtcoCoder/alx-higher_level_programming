#!/usr/bin/python3
"""Takes 2 arguments in order to solve this challenge:
list 10 commits (from the most recent) of the repository 'rails' by the user
'rails' using the GitHub API. print format: <sha>: <author name> (one by line)
"""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    user = sys.argv[2]

    params = {'per_page': 10}
    url = "https://api.github.com/repos/{}/{}/commits"

    response = requests.get(url.format(repo, user), params=params)
    commits = response.json()

    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
