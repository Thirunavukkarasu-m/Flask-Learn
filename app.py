from flask import Flask,url_for
from user import *
from auth import *
from config.config import *
# from user.routes import *
from home.route import *
from home import *
from user.models import *
import os 
from extension import *


def create_app():
  app=Flask(__name__)
  app.config.from_object(Config)
  os.makedirs(app.config['UPLOAD_FOLDER'],exist_ok=True)
  # db initalize 
  db.init_app(app)

  # login authenticate intialize 
  login_manager.init_app(app)
  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))




  app.register_blueprint(users_bp,url_prefix='/users')
  app.register_blueprint(home,url_prefix='/')

  # auth
  app.register_blueprint(auth_bp,url_prefix='/auth')




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

  return app

app=create_app()