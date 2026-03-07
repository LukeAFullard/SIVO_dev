import urllib.parse
url = "https://www.facebook.com/20531316728/posts/10154009990506729/"
iframe_src = f"https://www.facebook.com/plugins/post.php?href={urllib.parse.quote(url)}&show_text=true"
print(iframe_src)
