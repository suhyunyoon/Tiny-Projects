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
        # 라이프
        self.life = 3
        self.alive = True
        self.last_hit = 0

    def move(self, dt):
        # 실제 이동
        self.x_pos += self.to_x * dt
        self.y_pos += self.to_y * dt

    # 발사
    def shoot(self, bullet_list):
        # 현재 위치에서 총알 추가
        x_pos = self.x_pos + self.width // 2
        y_pos = self.y_pos - 15
        bullet_list.append([x_pos, y_pos])

    # 피격
    def hit(self, damage):
        # 무적시간
        if pygame.time.get_ticks() - self.last_hit >= 1000:
            # 데미지
            print("부딛힘!")
            self.life -= damage
            if self.life <= 0:
                self.alive = False
            self.last_hit = pygame.time.get_ticks()

    def get_rect(self):
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
        self.x_speed = (random.random() - 0.5) / 10

        # 가속도
        self.acc = 0.002
        
        # 위치
        self.x_pos = random.randrange(0, screen_width - self.width)
        self.y_pos = - self.height
        
    def move(self, dt):
        self.x_pos += self.x_speed * dt
        self.y_pos += self.speed * dt
        # 속도 증가
        #self.x_speed += self.acc
        self.speed += self.acc

    def get_rect(self):
        self.rect = self.img.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos
        
