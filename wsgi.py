from oce import create_app
from frozen_flask import Freezer
from flask import render_template

app = create_app()
freezer = Freezer(app)  # Initialize Freezer with the app

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    freezer.freeze()  # This will generate static files for Netlify
