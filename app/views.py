from flask import request, jsonify
from app import app, db, limiter
from app.models import Post
from app.tasks import analyze_post
from celery.result import AsyncResult

@app.route('/api/v1/posts/', methods=['POST'])
@limiter.limit("5 per minute")
def create_post():
    data = request.get_json()
    post = Post(id=data['id'], content=data['content'])
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'}), 201

@app.route('/api/v1/posts/<post_id>/analysis/', methods=['GET'])
@limiter.limit("10 per minute")
def get_analysis(post_id):
    try:
        post = Post.query.get(post_id)
        
        if post:
            result = analyze_post.delay(post_id)
            print("Celery task ID:", result.id)
            return jsonify({'message': 'Analysis in progress. Check again later.', 'task_id': result.id, 'post_id': post_id}), 202
        else:
            return jsonify({'error': 'Post not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
