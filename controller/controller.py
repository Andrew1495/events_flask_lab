from flask import render_template
from app import app
from models.event_class import Event
from models.current_events import events


@app.route("/")
def index():
    return render_template("index.html")