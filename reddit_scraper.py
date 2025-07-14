import praw

def fetch_user_data(username):
    reddit = praw.Reddit(
        client_id="PPEaSItISFbMMJvD07lpyQ",
        client_secret="fv0kic6UCgF6pBtrnCSJ02wLugp_1Q",
        user_agent="persona-generator-script"
    )
    user = reddit.redditor(username)
    posts = [post.title + " - " + post.selftext for post in user.submissions.new(limit=50)]
    comments = [comment.body for comment in user.comments.new(limit=50)]
    return posts, comments