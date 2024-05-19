import pygame

from SpriteState import SpriteState


class Sprite:
    states: dict[str, SpriteState] = {}
    current_state: str = ""
    x: int = 0
    y: int = 0

    def __init__(self, x, y, width, height, color, states: dict[str, str]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.states = {
            state: SpriteState(width, height, img_url)
            for state, img_url in states.items()
        }
        self.current_state = list(states.keys())[0]

    def draw(self, surface):
        self.states[self.current_state].draw(surface, self.x, self.y)

    def next_frame(self):
        self.states[self.current_state].next_frame()

    def previous_frame(self):
        self.states[self.current_state].previous_frame()

    def set_state(self, state):
        self.current_state = state

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y
