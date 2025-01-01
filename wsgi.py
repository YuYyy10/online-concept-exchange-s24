from oce import create_app
from flask import render_template
#from flask_limiter import Limiter
#from flask_limiter.util import get_remote_address

app = create_app()
#limiter = Limiter(get_remote_address, app=app)

if __name__ == '__main__':
    app.run()

@app.route('/')
#@limiter.limit("5/minute")
def home():
  return render_template('index.html')