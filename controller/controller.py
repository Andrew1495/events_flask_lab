from flask import render_template, redirect, request
from app import app
from models.event_class import Event
from models.current_events import events
from models.current_events import add_new_event


@app.route("/events")
def index():
    return render_template("index.html", events=events)

@app.route("/events/new")
def add_event():
        return render_template("add_event.html")


@app.route('/events', methods=['POST'])
def add_events():
    event_name = request.form['event_name']
    event_date = request.form['event_date']
    event_no_guests = request.form['no_of_guests']
    event_location = request.form['location']
    event_desc = request.form['description']
    new_event = Event(event_date, event_name, event_no_guests, event_location, event_desc)
    add_new_event(new_event)
    return redirect("/events")
