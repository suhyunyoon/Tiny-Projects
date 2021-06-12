'''
1. pygame, screen 정보 초기화
2. 기본 변수들 초기화
3. 배경 띄우기
4. 위치, 이동 처리하는 캐릭터, 적, 아이템 클래스
4-1. 이동 시 속도 * dt(fps)
4-2. 충돌 감지할때는 직사각형 단위로 체크
4-3. 적, 아이템은 list에 보관

5. pygame은 while loop 안에서 작동
5-1. 이벤트 체크(종료, 키 입력, 마우스)
5-2. 캐릭터 등 이동
5-3. 캐릭터 등 화면 밖으로 나가는 지 검사
5-4. 충돌 검사
5-5. n초마다 이벤트 발생
5-6. 텍스트 처리
5-7. blit함수로 화면 내 지정 좌표에 배치
5-8. pygame.display.update()

6. pygame.quit()
'''

import pygame
import random
import time

pygame.init()

screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기")

# FPS 클럭
clock = pygame.time.Clock()

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간 및 시간 계산
total_time = 20
elapsed_time = 0
start_ticks = pygame.time.get_ticks()
# 시간 간격 저장
pivot_ticks = start_ticks
item_ticks = start_ticks

# 점수
score = 0

# 적 젠 시간 간격
enemy_gen = 1500

# 배경 이미지 불러오기
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))
# 캐릭터 이미지 불러오기 
character = pygame.image.load('character.png')
character = pygame.transform.scale(character, (30,50))
# 캐릭터 위치 정보 저장
c_size = character.get_rect().size # 사진 이미지의 가로세로 크기
c_width = c_size[0]
c_height = c_size[1]
c_x_pos = screen_width/2 - c_width/2
c_y_pos = screen_height - c_height/2

# 적
class Enemy:
    def __init__(self):
        # 적 이미지 불러오기 
        self.enemy = pygame.image.load('enemy.png')
        self.enemy = pygame.transform.scale(self.enemy, (50, 50))
        # 위치 정보
        self.e_size = self.enemy.get_rect().size
        self.e_width = self.e_size[0]
        self.e_height = self.e_size[1]
        # 속도
        self.e_init_speed = 0.5
        # 초기화
        self.reset()
    # 위치 초기화
    def reset(self):
        self.e_x_pos = random.randrange(0, screen_width - self.e_width)
        self.e_y_pos = - self.e_height
        self.e_speed = self.e_init_speed
    # 이동
    def move(self):
        self.e_y_pos += self.e_speed * dt
        self.e_speed += 0.01
    # 충돌 감지용 직사각형
    def rect(self):
        self.e_rect = self.enemy.get_rect()
        self.e_rect.left = self.e_x_pos
        self.e_rect.top = self.e_y_pos

# 아이템
class Item:
    def __init__(self):
        # 이미지 불러오기
        self.item = pygame.image.load('item.png')
        self.item = pygame.transform.scale(self.item, (50, 50))
        # 위치 정보
        self.i_size = self.item.get_rect().size
        self.i_width = self.i_size[0]
        self.i_height = self.i_size[1]
        # 속도
        self.i_init_speed = 0.5
        # 초기화
        self.reset()
    # 위치 초기화
    def reset(self):
        self.i_x_pos = random.randrange(0, screen_width - self.i_width)
        self.i_y_pos = - self.i_height
        self.i_speed = self.i_init_speed
    # 이동
    def move(self):
        self.i_y_pos += self.i_speed * dt
        self.i_speed += 0.01
    # 충돌 감지용 직사각형
    def rect(self):
        self.i_rect = self.item.get_rect()
        self.i_rect.left = self.i_x_pos
        self.i_rect.top = self.i_y_pos

enemy_list = [Enemy()]
item_list = []

# 위치의 변화량
to_x = 0
to_y = 0

# 속도
c_speed = 0.5

run = True
while run:
    dt = clock.tick(60) # 창의 초당 프레임 수
    #print("fps: %f" % clock.get_fps())
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        # 키가 눌러졌을 때
        if e.type == pygame.KEYDOWN:
            # character
            if e.key == pygame.K_LEFT:
                to_x -= c_speed # x 위치의 변화량
            elif e.key == pygame.K_RIGHT:
                to_x += c_speed # x 위치의 변화량
            elif e.key == pygame.K_UP:
                to_y -= c_speed # y 위치의 변화량
            elif e.key == pygame.K_DOWN:
                to_y += c_speed # y 위치의 변화량
                
        # 키를 뗐을 때
        if e.type == pygame.KEYUP:
            # character
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                to_x = 0
            elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                to_y = 0

    # character 이동
    c_x_pos += to_x * dt
    c_y_pos += to_y * dt

    # 적 이동(떨어짐)
    for e in enemy_list:
        e.move()

    # 아이템 이동(떨어짐)
    for i in item_list:
        i.move()
    
    # character
    # (가로)화면 영역 밖으로 나가는 지 검사
    if c_x_pos < 0:
        c_x_pos = 0
    elif c_x_pos > screen_width - c_width:
        c_x_pos = screen_width - c_width
        
    # (세로)화면 영역 밖으로 나가는 지 검사
    if c_y_pos < 0:
        c_y_pos = 0
    elif c_y_pos > screen_height - c_height:
        c_y_pos = screen_height - c_height

    # 적이 화면 밖으로 나가는 지 검사
    for e in enemy_list:
        if e.e_y_pos >= screen_height:
            e.reset()
            # 스코어 1점 추가
            score += 1
    # 아이템이 화면 밖으로 나가는 지 검사
    for i in item_list:
        if i.i_y_pos >= screen_height:
            item_list.remove(i)

    # 캐릭터의 사각형 정보
    c_rect = character.get_rect()
    c_rect.left = c_x_pos
    c_rect.top = c_y_pos
    # 적과의 충돌 검사
    for e in enemy_list:
        e.rect()
        if c_rect.colliderect(e.e_rect):
            print("충돌!")
            run = False
            break
    # 아이템 충돌 검사(먹었는지)
    for i in item_list:
        i.rect()
        if c_rect.colliderect(i.i_rect):
            print("아이템")
            # 없앤 갯수의 두배만큼 점수 증가
            add_score = len(enemy_list) * 2
            score += add_score
            enemy_list.clear()
            # 부딛힌 아이템 삭제
            item_list.remove(i)
        
    # 배경을 띄우기
    screen.blit(background, (0,0))
    # 캐릭터를 창에 띄우기
    screen.blit(character, (c_x_pos, c_y_pos))
    # 적들을 띄우기
    for e in enemy_list:
        screen.blit(e.enemy, (e.e_x_pos, e.e_y_pos))
    # 아이템 띄우기
    for i in item_list:
        screen.blit(i.item, (i.i_x_pos, i.i_y_pos))

    # n초마다 적 추가
    if (pygame.time.get_ticks() - pivot_ticks) >= enemy_gen:
        enemy_list.append(Enemy())
        pivot_ticks = pygame.time.get_ticks()

    #  10초마다 아이템 추가
    if (pygame.time.get_ticks() - item_ticks) >= 10000:
        item_list.append(Item())
        item_ticks = pygame.time.get_ticks()

    # 출력할 텍스트
    elapsed_time = pygame.time.get_ticks() - start_ticks
    #timer = game_font.render('{}'.format(int(elapsed_time)), True, (255,0,0))
    score_text = game_font.render('Score: {}'.format(int(score)), True, (0,0,255))
    
    # 텍스트 출력
    #screen.blit(timer, (10, 10))
    screen.blit(score_text, (10,10))
    '''
    # 시간이 total_time보다 커지면 게임 종료
    if elapsed_time >= total_time:
        print('시간 초과!')
        run = False
    '''
    # 변경된 창을 실제 화면에 띄우기
    pygame.display.update()

print('최종 점수:', score)
time.sleep(5)

pygame.quit()
