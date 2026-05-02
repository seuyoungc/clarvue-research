import time
from pathlib import Path

import pandas as pd
import requests

subreddits = ['PMDD', 'pms', 'Periods']
search_terms = ['decision', 'brain fog', 'meal', 'schedule', 'cope', 'cant function', 'luteal']

posts = []
headers = {'User-Agent': 'CLARVUE-research/1.0'}

for sub in subreddits:
    for term in search_terms:
        url = f'https://www.reddit.com/r/{sub}/search.json?q={term}&restrict_sr=1&limit=25&sort=relevance'
        r = requests.get(url, headers=headers)
        for post in r.json()['data']['children']:
            d = post['data']
            posts.append({
                'subreddit': sub,
                'title': d['title'],
                'body': d.get('selftext', ''),
                'score': d['score'],
                'num_comments': d['num_comments'],
                'url': f"https://reddit.com{d['permalink']}",
                'search_term': term
            })
        time.sleep(2)  # be polite

out_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "posts.csv"
out_path.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame(posts).to_csv(out_path, index=False)
print(f"Wrote {len(posts)} rows to {out_path}")