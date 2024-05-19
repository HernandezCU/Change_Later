import pygame

from SpriteState import SpriteState


class Sprite:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        color,
        states: dict[str, str],
        image_width=None,
        image_height=None,
        animate_frames=5,
        initial_state=None,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.animate_frames = animate_frames
        self.animate_frame_index = 0
        self.states = {
            state: SpriteState(width, height, img_url, image_width, image_height)
            for state, img_url in states.items()
        }
        self.current_state = (
            list(states.keys())[0] if initial_state is None else initial_state
        )

    def draw(self, surface):
        self.states[self.current_state].draw(surface, self.x, self.y)

    def animate(self):
        self.animate_frame_index += 1
        if self.animate_frame_index >= self.animate_frames:
            self.next_frame()
            self.animate_frame_index = 0

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
