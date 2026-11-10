#!/usr/bin/python3
"""Query the Reddit API and print the titles of hot posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "ALUStudent:reddit_api:v1.0"
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
