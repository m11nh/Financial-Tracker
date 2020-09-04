from app import app
from app.client import start_client, pickle_update
from flask import render_template

system = start_client()

@app.route('/')
def index(): 
    pickle_update(system)
    return render_template("static.html")