#!/usr/bin/python3
"""Retrieve all hot post titles from a subreddit recursively."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles for a subreddit."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "ALUStudent:reddit_api:v1.0"
    }
    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
