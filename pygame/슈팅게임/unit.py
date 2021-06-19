import pygame
import random

class Character:
    def __init__(self, screen_width, screen_height):
        # 사진 파일 불러오기
        self.img = pygame.image.load('character.png')
        self.img = pygame.transform.scale(self.img, (24, 24))
        # 크기 정보
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        # 속도
        self.speed = 0.4
        self.to_x = 0
        self.to_y = 0
        # 위치
        self.x_pos = (screen_width - self.width) // 2
        self.y_pos = screen_height - self.height

    def move(self, dt):
        # 실제 이동
        self.x_pos += self.to_x * dt
        self.y_pos += self.to_y * dt

    def rect(self):
        self.rect = self.img.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos
# Rock 클래스 채우기
# Rock이 떨어짐
# Rock이 화면 밖으로 나가면 배열에서 삭제
# 캐릭터랑 부딪히면 게임종료
rock_imgs = ['rock1.png', 'rock2.png', 'rock3.png']
class Rock:
    def __init__(self, screen_width, screen_height):
        self.img = pygame.image.load(random.choice(rock_imgs))
        self.img = pygame.transform.scale(self.img, (50,50))
        # 크기 정보
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        # 속도
        self.init_speed = 0.1
        self.speed = self.init_speed
        # 위치
        self.x_pos = random.randrange(0, screen_width - self.width)
        self.y_pos = - self.height
        
    def move(self, dt):
        self.y_pos += self.speed * dt
    def rect(self):
        self.rect = self.img.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos
