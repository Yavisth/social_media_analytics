from app import celery, db
from app.models import Post

@celery.task
def analyze_post(post_id):
    post = Post.query.get(post_id)
    if post:
        words = post.content.split()
        word_count = len(words)
        avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
        return {'word_count': word_count, 'avg_word_length': avg_word_length}
    return None
