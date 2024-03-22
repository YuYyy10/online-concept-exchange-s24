from flask import Blueprint
from flask import render_template

content = Blueprint('content', __name__)

@content.route("/content/block1")
def block1():
  return render_template("block1.html")

@content.route("/content/block2")
def block2():
  return render_template("block2.html")

@content.route("/content/block3")
def block3():
  return render_template("block3.html")

@content.route("/content/block4")
def block4():
  return render_template("block4.html")

@content.route("/content/block5")
def block5():
  return render_template("block5.html")

@content.route("/content/block6")
def block6():
  return render_template("block6.html")

@content.route("/content/block7")
def block7():
  return render_template("block7.html")

@content.route("/content/block8")
def block8():
  return render_template("block8.html")

@content.route("/content/block9")
def block9():
  return render_template("block9.html")