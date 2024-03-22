from flask import Blueprint
from flask import render_template

content = Blueprint('content', __name__)

@content.route("/content/block1")
def block1():
  render_template("block1.html")