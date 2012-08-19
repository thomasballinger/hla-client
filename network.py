import socket


HOST = 'localhost'
PORT = 8000

def protocolize(s):
    return str(len(s)) + ' ' + s

class Connection(object):
    def __init__(self, name=None):
        self.s = socket.socket()
        self.s.connect((HOST, PORT))
        self.messages = []
        if name:
            self.name = name
        else:
            self._nick = 'no name'
    def get_event(self):
        try:
            return self.s.recv(100)
        except:
            return None
    def check_socket(self):
        print 'checking socket for...', self
        self.s.settimeout(0.2)
        self.messages.append(self.s.recv(100))
        self.s.settimeout(None)
    def event(self, name):
        print 'sending event', name, 'from', self
        self.s.send(protocolize('/event '+name))
    def _set_nick(self, value):
        print 'sending nick change to', value, 'from', self
        self.s.send(protocolize('/nick '+value))
        self._nick = value
    def _get_nick(self):
        return self._nick
    name = property(_get_nick, _set_nick)
    def move(self, direction):
        self.s.send(protocolize('/move '+direction))

if __name__ == '__main__':
    import time
    c = Connection()
    d = Connection()
    c.name = 'Fred'
    d.name = 'George'
    d.event('woof')
    print d.name, ':', d.get_event()
    print c.name, ':', c.get_event()




