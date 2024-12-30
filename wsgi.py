from oce import create_app
from flask import render_template

app = create_app()
if __name__ == '__main__':
    app.run()

@app.route('/')
def home():
  return render_template('index.html')
