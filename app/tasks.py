from app import celery
from app.models import Post
import logging

logger = logging.getLogger(__name__)

@celery.task
def analyze_post(post_id):
    try:
        post = Post.query.get(post_id)
        if post:
            words = post.content.split()
            word_count = len(words)
            avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
            result = {'word_count': word_count, 'avg_word_length': avg_word_length}

            return result
        return None
    except Exception as e:
        logger.exception(f"Error processing post {post_id}: {str(e)}")
        raise
