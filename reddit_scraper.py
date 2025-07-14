import praw

def fetch_user_data(username):
    reddit = praw.Reddit(
        client_id="your_client_id",
        client_secret="your_actual_client_secret",
        user_agent="persona-generator-script"
    )
    user = reddit.redditor(username)
    posts = [post.title + " - " + post.selftext for post in user.submissions.new(limit=50)]
    comments = [comment.body for comment in user.comments.new(limit=50)]
    return posts, comments