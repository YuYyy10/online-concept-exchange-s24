from flask import Blueprint
from flask import render_template, send_file, request, jsonify
from oce.utils.db_interface import create_post, get_post_by_uuid
from oce.utils.models import User

content = Blueprint('content', __name__)

@content.route('/content/block1')
def block1():
  return render_template('block1.html')

@content.route('/content/block2')
def block2():
  return render_template('block2.html')

@content.route('/content/block3')
def block3():
  return render_template('block3.html')

@content.route('/content/block4')
def block4():
  return render_template('block4.html')

@content.route('/content/block5')
def block5():
  return render_template('block5.html')

@content.route('/content/block6')
def block6():
  return render_template('block6.html')

@content.route('/content/block7')
def block7():
  return render_template('block7.html')

@content.route('/content/block8')
def block8():
  return render_template('block8.html')

@content.route('/content/block9')
def block9():
  return render_template('block9.html')

@content.route('/content/tiles/')
def tiles():
    return send_file('static/docs/Human-Domino-Effect-Footprint-Tiles.pdf', download_name='Human-Domino-Effect-Footprint-Tiles.pdf')

@content.route('/content/ConceptExchange/')
def concept_exchange():
    from oce.utils.db_interface import get_all_posts
    
    try:
        # Fetch all posts from the database
        posts = get_all_posts()
        return render_template('mainForum.html', posts=posts)
    except Exception as e:
        print(f"Error fetching posts: {e}")
        return render_template('mainForum.html', posts=[])

@content.route('/content/resources/<selected_age>')
def resources(selected_age):
    return render_template('resources.html', selected_age=selected_age)

@content.route('/content/Login/')
def login():
  return render_template('LoginPage.html')

@content.route('/content/calendar/')
def calendar():
  return render_template('calendar.html')

@content.route('/content/Contact/')
def contact():
  return render_template('ContactPage.html')

@content.route('/content/Shop/')
def shop():
  return render_template('Shop.html')

@content.route('/content/Cart/')
def cart():
  return render_template('Cart.html')

@content.route('/create_post', methods=['POST'])
def create_post_route():
    data = request.get_json()  # Get JSON data from the request
    text_content = data.get('text_content')  # Extract the post content
    username = data.get('username')

    if not text_content:
        return jsonify({'success': False, 'error': 'Text content is required.'}), 400

    try:
        # create_post(author=User(user_uuid="example", username="name", email="example@email.com", password="password", profile_pic=b"", about_me=''), text_content=text_content, tag1='', tag2='', tag3='', tag4='', tag5='', datetime='', location='', image=None)
        create_post(author=username, text_content=text_content)  # this should be updated when the user login feature is added to look more like the one above this line
        return jsonify({'success': True})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
