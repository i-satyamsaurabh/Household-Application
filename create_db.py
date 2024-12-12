from app import app, db
from eralchemy import render_er
import graphviz
print("Graphviz is installed correctly!")



# Ensure the app context is properly handled
with app.app_context():
    db.create_all()
    print("Database created successfully!")

render_er(db.Model, 'erd.png')