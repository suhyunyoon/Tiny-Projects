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
        self.speed = 0.35
        self.to_left, self.to_right = 0, 0
        self.to_up, self.to_down = 0, 0
        # 위치
        self.x_pos = (screen_width - self.width) // 2
        self.y_pos = screen_height - self.height
        # 라이프
        self.life = 3
        self.alive = True
        self.last_hit = 0
        # Fire
        self.fire = False
        self.last_fire = 0

    def move(self, dt):
        # 실제 이동
        to_x = (self.to_right - self.to_left) * dt
        to_y = (self.to_down - self.to_up) * dt
        if self.fire:
            to_x /= 1.5
            to_y /= 1.5
        self.x_pos += to_x
        self.y_pos += to_y

    # 발사
    def shoot(self, bullet_list):
        if pygame.time.get_ticks() - self.last_fire >= 200:
            # 현재 위치에서 총알 추가
            x_pos = self.x_pos + self.width // 2
            y_pos = self.y_pos - 15
            bullet_list.append([x_pos, y_pos])
            self.last_fire = pygame.time.get_ticks()

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
class Rock:
    def __init__(self, screen_width, screen_height, rock, init_speed=0.1, acc=0.002):
        self.img = rock
        # 크기 정보
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        # 속도
        self.init_speed = init_speed
        self.speed = self.init_speed
        self.x_speed = (random.random() - 0.5) / 10

        # 가속도
        self.acc = acc
        
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

# 적 기체
class Enemy:
    def __init__(self, screen_width, screen_height, img):
        self.img = img
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]

        self.life = 5
        self.alive = True

        self.x_pos = random.randrange(0, screen_width - self.width)
        self.y_pos = - self.height
        self.speed = 0.4
        self.acc = -0.005

        self.y_limit = 120

        self.last_shoot = 0

    def move(self, dt):
        if self.y_pos < self.y_limit:
            self.y_pos += self.speed * dt
            self.speed += self.acc

    def hit(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.alive = False

    def shoot(self, enemy_bullet_list):
        if pygame.time.get_ticks() - self.last_shoot > 1500:
            b_x_pos = self.x_pos + 15
            b_y_pos = self.y_pos + self.height
            enemy_bullet_list.append([b_x_pos, b_y_pos])
            
            self.last_shoot = pygame.time.get_ticks()
            
    def get_rect(self):
        self.rect = self.img.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos
        
        
