import socket
import re


HOST = 'localhost'
PORT = 8000

def protocolize(s):
    return str(len(s)) + ' ' + s

class Connection(object):
    def __init__(self, name=None):
        self.s = socket.socket()
        self.s.connect((HOST, PORT))
        self.messages = []
        self.rest = ''
        if name:
            self.name = name
        else:
            self._nick = 'no name'
    def get_event(self):
        self.s.settimeout(0.2)
        try:
            msg = self.s.recv(100)
        except: #TODO it's some kind of socket no data found error
            msg = ""
        self.s.settimeout(None)
        self.rest += msg
        return self.extract_message()
    def extract_message(self):
        print 'self.rest:', self.rest
        if not self.rest:
            return None
        m = re.match(r'(\d+) .', self.rest)
        if not m:
            print 'match not found (perhaps bad data?)'
            return None
        end = len(m.group(1))+int(m.group(1))+1
        msg = self.rest[len(m.group(1))+1:end]
        self.rest = self.rest[end:]
        return msg

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
    c = Connection()
    d = Connection()
    c.name = 'Fred'
    d.name = 'George'
    d.event('horn')
    print d.name, ':', d.get_event()
    print c.name, ':', c.get_event()
    print c.name, ':', c.get_event()




