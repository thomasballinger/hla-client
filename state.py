
import time
import json

class Event(object):
    def __init__(self, json_string):
        d = json.loads(json_string)
        self.duration = 0
        for key in ['x', 'y', 'name', 'distance', 'url', 'duration']:
            setattr(self, key, d[key])
        self.created = time.time()
        self.duration_s = self.duration / 1000.0
    def __eq__(self, other):
        return self.created == other.created

class World(object):
    """Infinite world"""
    def __init__(self, pos=(0,0)):
        self.pos = list(pos)
        self.events = []
    def register_event(self, event):
        self.events.append(event)
    def register_json_string(self, json_string):
        e = Event(json_string)
        self.register_event(e)
    def cull_events(self):
        t = time.time()
        self.events = [e for e in self.events if e.created + e.duration_s > t]
    def render(self):
        view_radius = 10
        spot_width = 3
        dim = view_radius*2+1
        l = [[' '*spot_width for i in range(dim)] for i in range(dim)]
        counter = 1
        notes = '\n world at time %0.1f' % (time.time()%100)
        notes += '\n x: self'
        l[view_radius][view_radius] = 'x'.center(spot_width)
        for e in self.events:
            display_x = e.x - self.pos[0]
            display_y = e.y - self.pos[1]
            if abs(display_x) <= view_radius and abs(display_y) <= view_radius:
                l[display_y+view_radius][display_x+view_radius] = str(counter)
                notes += '\n'+str(counter)+': '+e.name+' at %0.1f' % (e.created%100)

        s = '\n'+notes+'\n'.join([''.join(x) for x in l]) + '\n'
        print chr(27) + "[2J" # clears screen
        print s

    def get_events(self):
        return self.events


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
    w.register_event(e)
    while True:
        w.render()
        raw_input()
        w.cull_events()

