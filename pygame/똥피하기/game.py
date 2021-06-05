import pygame
import random

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

enemy_list = [Enemy()]

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

    # 캐릭터의 사각형 정보
    c_rect = character.get_rect()
    c_rect.left = c_x_pos
    c_rect.top = c_y_pos
    # 적의 사각형 정보
    for e in enemy_list:
        e.rect()
        if c_rect.colliderect(e.e_rect):
            print("충돌!")
            run = False
            break
        
    # 배경을 띄우기
    screen.blit(background, (0,0))
    # 캐릭터를 창에 띄우기
    screen.blit(character, (c_x_pos, c_y_pos))
    # 적들을 띄우기
    for e in enemy_list:
        screen.blit(e.enemy, (e.e_x_pos, e.e_y_pos))

    # 1초마다 적 추가
    if (pygame.time.get_ticks() - start_ticks) // 1000 > int(elapsed_time):
        enemy_list.append(Enemy())

    # 출력할 텍스트
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render('{}'.format(int(elapsed_time)), True, (255,0,0))
    
    # 텍스트 출력
    screen.blit(timer, (10, 10))
    '''
    # 시간이 total_time보다 커지면 게임 종료
    if elapsed_time >= total_time:
        print('시간 초과!')
        run = False
    '''
    # 변경된 창을 실제 화면에 띄우기
    pygame.display.update()

pygame.quit()
