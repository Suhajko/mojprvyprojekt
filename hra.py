from pygame import *


back = (210, 255, 265)
win_width = 700
win_height = 600
window = display.set_mode((win_width, win_height))
window.fill

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player.speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

        class Player(GameSprite):
            def update_r(self):
                keys = key.get_pressed()
                if keys[K_UP] and self.rect.x > 5:
                    self.rect.x -= self.speed
                if keys[K_DOWN] and self.rect.x < win_width - 80:
                    self.rect.x += self.speed
            def update_l(self):
                keys = key.get_pressed()
                if keys[K_w] and self.rect.x > 5:
                    self.rect.x -= self.speed
                if keys[K_s] and self.rect.x < win_width - 80:
                    self.rect.x += self.speed

racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("tenis.png", 400, 200, 4, 50, 150)


game = True
while game:
    pass
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    window.fill(back)
    racket1.update_l()
    racket2.update_r()

    racket1.reset()
    racket2.reset()
    ball.reset()


    display.update()
