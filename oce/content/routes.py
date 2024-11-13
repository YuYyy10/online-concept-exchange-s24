from flask import Blueprint
from flask import render_template, send_file

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
  return render_template('mainForum.html')

@content.route('/content/resources/<selected_age>')
def resources(selected_age):
    return render_template('resources.html', selected_age=selected_age)

@content.route('/content/Login/')
def login():
  return render_template('LoginPage.html')

@content.route('/content/Contact/')
def contact():
  return render_template('ContactPage.html')

@content.route('/content/Shop/')
def shop():
  return render_template('Shop.html')

@content.route('/content/Cart/')
def cart():
  return render_template('Cart.html')

@content.route('/content/NewPost/')
def forumPost():
  return render_template('forumPost.html')
