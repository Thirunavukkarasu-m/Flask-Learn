from app import create_app
from extension import db

app=create_app()
with app.app_context():
    db.create_all()
    print("database created succesfully ")