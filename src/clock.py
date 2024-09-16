import pygame


class Clock:
    _clock: pygame.time.Clock

    def __init__(self) -> None:
        self._clock = pygame.time.Clock()

    def tick(self, frames: int):
        self._clock.tick(frames)
