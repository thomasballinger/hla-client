
import json

class Event(object):
    def __init__(self, json_string):
        json.loads(json_string)

class World(object):
    """Infinite world"""
    def __init__(self, pos=(0,0)):
        self.pos = list(pos)
        self.events = []
    def register_event(self, event):
        self.events.append(event)



if __name__ == '__main__':
    w = World()
    e = Event(json.dumps({
        'x':4,
        'y':5,
        'name':'horn',
        'distance':10,
        'url':'http://www.northernsun.com/images/thumb/2241Spaceship.jpg',
        'duration':5000
        }))
    w.append_event(e)

