import os 

class Config:
    SECRET_KEY="SUMMA"
    UPLOAD_FOLDER=os.path.join('static','uploads')
    MAX_CONTENT_LENGTH=5*1024*1024
    ALLOWED_EXTENSIONS={'png','jpg','jpeg','gif','pdf','txt'}

    
    
    BASE_DIR = os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))
    )

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    BASE_DIR, 'app.db'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    