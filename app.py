from flask import Flask
from user import *
# from user.routes import *
from home.route import *
from home import *

app=Flask(__name__)

app.register_blueprint(users_bp,url_prefix='/users')
app.register_blueprint(home,url_prefix='/')


@app.route('/about')
def about():return 'this about page'

@app.route('/summa')
def summa():
    return 'summa page '

@app.route("/profile/<int:id>/")
def profile(id):
    return f"Profile ID: {id}"



if __name__ == "__main__":
    app.run(debug=True)