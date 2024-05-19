import pygame


class SpriteState:
    def __init__(self, width, height, img_url, image_width=None, image_height=None):
        self.width = width
        self.height = height
        self.img_url = img_url
        self.image_width = image_width or width
        self.image_height = image_height or height
        self.whole_image = pygame.image.load(img_url)
        self.images = []
        self.current_frame_index = 0

        print(self.whole_image.get_width(), self.whole_image.get_height())
        print(self.image_width, self.image_height)

        if (
            self.whole_image.get_width() != self.image_width
            or self.whole_image.get_height() != self.image_height
        ):
            if (
                self.whole_image.get_width() % self.image_width != 0
                and self.whole_image.get_height() % self.image_height != 0
            ):
                raise ValueError(
                    "Image width and height must be the same as the sprite or a multiple of it"
                )

        for i in range(self.whole_image.get_width() // self.image_width):
            self.images.append(
                self.whole_image.subsurface(
                    (
                        i * self.image_width,
                        0,
                        self.image_width,
                        self.image_height,
                    )
                )
            )

        print(len(self.images))

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

    def __str__(self):
        return f"{self.state_name}: {self.img_url}, {self.image_width}, {self.image_height}, {len(self.images)}"

    def __repr__(self):
        return self.__str__()
