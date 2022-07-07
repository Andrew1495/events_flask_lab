from models.event_class import Event
import datetime

event1 = Event(datetime.datetime.strptime("07072022","%d%m%Y").date(), "Mens Mental Health", 20, "codeclan", "Men's mental health seminar")
event2 = Event(datetime.datetime.strptime("08072022","%d%m%Y").date(), "Women's Mental Health", 20, "codeclan", "Women's mental health seminar")

events = [event1,event2]