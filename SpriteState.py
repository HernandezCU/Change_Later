import pygame


class SpriteState:
    images: list[pygame.Surface] = []
    current_frame_index: int = 0
    state_name: str = ""

    def __init__(self, width, height, img_url):
        self.width = width
        self.height = height
        self.whole_image = pygame.image.load(img_url)

        if (
            self.whole_image.get_width() != width
            or self.whole_image.get_height() != height
        ):
            if (
                self.whole_image.get_width() % width != 0
                and self.whole_image.get_height() % height != 0
            ):
                raise ValueError(
                    "Image width and height must be the same as the sprite or a multiple of it"
                )

        for i in range(self.whole_image.get_width() // width):
            self.images.append(
                self.whole_image.subsurface((i * width, 0, width, height))
            )

    @property
    def current_frame(self):
        return self.images[self.current_frame_index]

    def next_frame(self):
        self.current_frame_index = (self.current_frame_index + 1) % len(self.images)

    def previous_frame(self):
        self.current_frame_index = (self.current_frame_index - 1) % len(self.images)
        if self.current_frame_index < 0:
            self.current_frame_index = len(self.images) - 1

    def draw(self, surface, x, y):
        surface.blit(self.current_frame, (x, y))
