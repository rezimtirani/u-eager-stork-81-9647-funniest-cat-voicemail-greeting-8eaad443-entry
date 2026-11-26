"""Push this entry's main files to its public GitHub repository.

Usage:
    python3 gh_upload_cat_voicemail.py

The repository must already exist (created separately with create_repo.py).
Each file is created, or updated in place when it is already there,
through the GitHub Contents API. Authentication goes through the stored
GitHub credential via the dynamic-credentials surrogate, so no token
is ever written into this file.

Only main.py and README.md are uploaded here. The remaining files in
the entry folder (LICENSE, this script, entry-state.json) are uploaded
by a companion script so the GitHub tree matches the bundle snapshot.
"""

import argparse
import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request

OWNER = "rezimtirani"
REPO = "u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443-entry"
BRANCH = "main"
FILES = ("main.py", "README.md")
API_ROOT = "https://api.github.com"


def call_github(method, url, payload=None):
    body = None
    headers = {"Accept": "application/vnd.github+json"}
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=body, method=method, headers=headers)
    add_surrogate_to_request(request, "custom.github", allowed_hosts=["api.github.com"])
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def remote_sha(path):
    url = "{}/repos/{}/{}/contents/{}?ref={}".format(API_ROOT, OWNER, REPO, path, BRANCH)
    try:
        return call_github("GET", url)["sha"]
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise


def push_one(folder, name):
    encoded = base64.b64encode((folder / name).read_bytes()).decode("ascii")
    payload = {
        "message": "Add {} — Funniest Cat Voicemail Greeting entry".format(name),
        "content": encoded,
        "branch": BRANCH,
    }
    sha = remote_sha(name)
    if sha:
        payload["sha"] = sha
    url = "{}/repos/{}/{}/contents/{}".format(API_ROOT, OWNER, REPO, name)
    result = call_github("PUT", url, payload)
    print("uploaded {} -> {}".format(name, result["content"]["sha"]))


def main():
    global OWNER, REPO, BRANCH
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=REPO)
    parser.add_argument("--owner", default=OWNER)
    parser.add_argument("--branch", default=BRANCH)
    args = parser.parse_args()
    OWNER, REPO, BRANCH = args.owner, args.repo, args.branch
    folder = Path(__file__).resolve().parent
    for name in FILES:
        push_one(folder, name)
    print("done: https://github.com/{}/{}".format(OWNER, REPO))


if __name__ == "__main__":
    main()
