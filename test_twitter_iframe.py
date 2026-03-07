import re

url = "https://twitter.com/OpenAI/status/1758231365825700200"
tweet_id_match = re.search(r'status/(\d+)', url)
if tweet_id_match:
    tweet_id = tweet_id_match.group(1)
    iframe_src = f"https://platform.twitter.com/embed/Tweet.html?id={tweet_id}"
    print(iframe_src)
