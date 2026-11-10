#!/usr/bin/python3
"""Count keyword occurrences in hot Reddit posts recursively."""

import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Count and print keyword occurrences in all hot posts."""
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

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
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        title_words = title.split()

        for word in word_list:
            keyword = word.lower()
            counts[keyword] += title_words.count(keyword)

    after = data.get("after")

    if after is not None:
        return count_words(subreddit, word_list, counts, after)

    results = [
        (word, count)
        for word, count in counts.items()
        if count > 0
    ]

    results.sort(key=lambda item: (-item[1], item[0]))

    for word, count in results:
        print("{}: {}".format(word, count))
