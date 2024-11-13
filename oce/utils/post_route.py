from flask import Flask, request, jsonify
from oce.utils.db_interface import get_db, create_post
from oce.utils.models import User

app = Flask(__name__)

@app.route('/create_post', methods=['POST'])
def create_post_route():
    data = request.get_json()
    text_content = data.get('text_content')

    if not text_content:
        return jsonify({'success': False, 'error': 'Text content is empty.'}), 400

    try:
        # Example author (replace with the actual logged-in user in your app)
        author_uuid = 'example-author-uuid'
        author = User(user_uuid=author_uuid) or "colin"

        # Call your existing function to create a new post
        create_post(
            author=author,
            text_content=text_content,
            tag1='',
            tag2='',
            tag3='',
            tag4='',
            tag5='',
            datetime='2024-11-13 12:00:00',  # Example datetime, replace with current timestamp
            location='Unknown',  # Example location, replace as needed
            image=None,
        )

        return jsonify({'success': True})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500