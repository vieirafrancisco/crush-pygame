import random

import pygame

WIDTH = 512
HEIGHT = 640

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]


class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((32, 32))
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Slot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill((100, 100, 100))
        pygame.draw.rect(self.image, (255, 255, 255), (0, 0, 64, 64), width=1)
        self.rect = self.image.get_rect()
        self.block = None

    def add_block(self, color):
        self.block = Block(color)
        self.image.blit(self.block.image, (16, 16))


class Map(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.slots = [10, 5, 7, 9, 7, 5, 3, 10]

        for x, n_rows in enumerate(self.slots):
            for y in range(n_rows):
                slot = Slot()
                slot.add_block(random.choice(COLORS))
                slot_pos = (0, 0)

                if y < n_rows // 2:
                    slot_pos = (
                        x * 64, HEIGHT // 2 - (y * 64) - 64
                    )
                elif y == n_rows // 2:
                    slot_pos = (x * 64, HEIGHT // 2)
                elif y > n_rows // 2:
                    slot_pos = (
                        x * 64,
                        HEIGHT // 2 + (n_rows - y) * 64
                    )

                slot.rect.topleft = slot_pos
                self.add(slot)


class Game:
    def __init__(self):
        self.running = False
        self.screen = None
        self.clock = pygame.time.Clock()

    def new(self):
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True

        self.map = Map()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def render(self):
        # for x in range(0, WIDTH, 64):
        #     pygame.draw.line(self.screen, (255, 0, 0), (x, 0), (x, HEIGHT))

        self.map.draw(self.screen)

    def update(self):
        pass

    def cleanup(self):
        pygame.font.quit()
        pygame.quit()

    def execute(self):
        self.new()
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.screen.fill((100, 100, 100))
            self.render()
            self.update()
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
        self.cleanup()


if __name__ == '__main__':
    g = Game()
    g.execute()
