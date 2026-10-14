from flask import Flask,url_for
from user import *
from config.config import *
# from user.routes import *
from home.route import *
from home import *
import os 


app=Flask(__name__)
app.config.from_object(Config)
os.makedirs(app.config['UPLOAD_FOLDER'],exist_ok=True)


app.register_blueprint(users_bp,url_prefix='/users')
app.register_blueprint(home,url_prefix='/')


@app.route('/about',methods=['POST','GET'])
def about():return 'this about page'

@app.get('/summa')
def summa():
    return url_for('about')

@app.route("/profile/<int:id>/")
def profile(id):
    return f"Profile ID: {id}"



if __name__ == "__main__":
    app.run(debug=True)