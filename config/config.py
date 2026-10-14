import os 

class Config:
    SECRET_KEY="SUMMA"
    UPLOAD_FOLDER=os.path.join('static','uploads')
    MAX_CONTENT_LENGTH=5*1024*1024
    ALLOWED_EXTENSIONS={'png','jpg','jpeg','gif','pdf','txt'}
