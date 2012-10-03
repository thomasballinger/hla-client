

import pyglet


def center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

class Display(state.World):
    def __init__(self):
        super(Display, self).__init__()
        self.game_window = pyglet.window.Window(800, 600)
        self.zoom = 10 # how many pixels to a game unit
    def register_event(event):
        pass
    def render(self):
        pass




if __name__ == '__main__':
    pyglet.app.run()
