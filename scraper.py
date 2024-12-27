#after pip install instaloader#after pip install instaloader
import subprocess
import sys

# Install instaloader if not already installed
subprocess.check_call([sys.executable, "-m", "pip", "install", "instaloader"])

import instaloader
L = instaloader.Instaloader()

# Login (optional, but recommended to avoid rate limiting)
username = "Your Instgram Username"
password = "Your Instagram Password"
L.login(username, password)

# Specify the post shortcode (the unique identifier in the post's URL)
post_shortcode = "uniquepostshortcode"

# Retrieve the post
post = instaloader.Post.from_shortcode(L.context, post_shortcode)

# Fetch and print comments
for comment in post.get_comments():
    print(f"User: {comment.owner.username}")
    print(f"Comment: {comment.text}")
    print(f"Likes: {comment.likes_count}")
    print("---")
