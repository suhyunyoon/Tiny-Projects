import pygame
from unit import Character, Rock, Enemy
import random

pygame.init()
screen_width = 480
screen_height = 640

#expand_ratio = 1.2
#screen_width = int(screen_width * expand_ratio)
#screen_height = int(screen_height * expand_ratio)

# FPS
clock = pygame.time.Clock()

# Font
game_font = pygame.font.Font(None, 40)

# Enemy 이미지 로드
enemy = pygame.image.load('character.png')
enemy = pygame.transform.scale(enemy, (40, 60))

# Rock 이미지 로드
rock_image_name = ['rock1.png', 'rock2.png', 'rock3.png']
rock_imgs = []
for img in rock_image_name:
    # 이미지 불러오기
    rock = pygame.image.load(img)
    rock = pygame.transform.scale(rock, (50,50))
    rock_imgs.append(rock)

# 나머지 이미지 로드
bullet = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bullet, (5, 15))
hp = pygame.image.load('hp.png')
hp = pygame.transform.scale(hp, (10,30))

enemy_bullet = pygame.image.load('enemy_bullet.png')
enemy_bullet = pygame.transform.scale(enemy_bullet, (20,20))

# 창 띄우기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("슈팅게임")

# 배경 띄우기
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))
# 캐릭터
C = Character(screen_width, screen_height)
# Rock
rock_list = [Rock(screen_width, screen_height, random.choice(rock_imgs)) for i in range(8)]

# 적 기체
enemy_list = [Enemy(screen_width, screen_height, enemy),
              Enemy(screen_width, screen_height, enemy)]

# 탄환
bullet_list = []
enemy_bullet_list = []

# 게임 시작
score = 0
run = True
while run:
    dt = clock.tick(60)
    
    for e in pygame.event.get():
        # 종료 이벤트
        if e.type == pygame.QUIT:
            run = False

        # 키를 눌렀을 때
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                C.to_x -= C.speed
            if e.key == pygame.K_RIGHT:
                C.to_x += C.speed
            if e.key == pygame.K_UP:
                C.to_y -= C.speed
            if e.key == pygame.K_DOWN:
                C.to_y += C.speed
            # 탄환 발사
            if e.key == pygame.K_SPACE:
                C.shoot(bullet_list)
        '''
        # 마우스 클릭했을 때
        if e.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                C.shoot(bullet_list)
                print(pygame.mouse.get_pos())
        '''
                
        # 키를 뗐을 때
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                C.to_x = 0
            if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                C.to_y = 0

    # 이동
    C.move(dt)
    # rock
    for r in rock_list:
        r.move(dt)
    # bullet
    for i, b in enumerate(bullet_list):
        bullet_list[i][1] -= 1 * dt
    # enemy
    for e in enemy_list:
        e.move(dt)
        # 발사
        e.shoot(enemy_bullet_list)
    # enemy bullet
    for i, b in enumerate(enemy_bullet_list):
        enemy_bullet_list[i][1] += 1 * dt

    # 화면 밖으로 나가는 지 검사
    # 캐릭터
    if C.x_pos < 0:
        C.x_pos = 0
    elif C.x_pos > screen_width - C.width:
        C.x_pos = screen_width - C.width

    if C.y_pos < 0:
        C.y_pos = 0
    elif C.y_pos > screen_height - C.height:
        C.y_pos = screen_height - C.height

    # 돌이 화면 밖으로 나가면 리스트에서 remove
    for r in rock_list:
        # 좌우로 나감
        if r.x_pos < 0 - r.width or r.x_pos > screen_width:
            r_init_speed = r.init_speed
            r_acc = r.acc
            rock_list.remove(r)
            rock_list.append(Rock(screen_width, screen_height, random.choice(rock_imgs),
                                  r_init_speed, r_acc))
            
        # 아래로 나감
        elif r.y_pos > screen_height:
            r_init_speed = r.init_speed
            r_acc = r.acc
            rock_list.remove(r)
            rock_list.append(Rock(screen_width, screen_height, random.choice(rock_imgs),
                                  r_init_speed, r_acc))

    # 총알이 화면 위로 나가면 리스트에서 remove
    for b in bullet_list:
        if b[1] < -15:
            bullet_list.remove(b)
    # 적의 총알이 화면 위로 나가면 리스트에서 remove
    for b in enemy_bullet_list:
        if b[1] > screen_height:
            enemy_bullet_list.remove(b)
    
    # 충돌 검사
    C.get_rect()
    for r in rock_list:
        r.get_rect()
        if C.rect.colliderect(r.rect):
            # 피해
            C.hit(1)
            # 게임 종료
            if not C.alive:
                run = False
            rock_list.remove(r)
            rock_list.append(Rock(screen_width, screen_height, random.choice(rock_imgs)))

        # 총알과 운석 충돌 - 부딛힌 총알&운석 remove
        for b in bullet_list:
            # 총알 사각형 정보
            b_rect = bullet.get_rect()
            b_rect.left = b[0]
            b_rect.top = b[1]
            # Rock과의 충돌 처리
            if r.rect.colliderect(b_rect):
                # 격파한 Rock은 새로 만들어질 때 init_speed와 acc를 1.1배 곱해서 새로 생성
                r_init_speed = r.init_speed * 1.1
                r_acc = r.acc * 1.1
                rock_list.remove(r)
                bullet_list.remove(b)
                rock_list.append(Rock(screen_width, screen_height,
                                      random.choice(rock_imgs), r_init_speed, r_acc))
                score += 1

    # Enemy와의 충돌 처리
    for e in enemy_list:
        e.get_rect()
        # 모든 총알에 대해
        for b in bullet_list:
            b_rect = bullet.get_rect()
            b_rect.left = b[0]
            b_rect.top = b[1]
            # 총알과 충돌
            if b_rect.colliderect(e.rect):
                e.hit(1)
                bullet_list.remove(b)
                if not e.alive:
                    enemy_list.remove(e)
                    enemy_list.append(Enemy(screen_width, screen_height, enemy))
                    enemy_list.append(Enemy(screen_width, screen_height, enemy))

    # enemy bullet과의 충돌 처리
    for b in enemy_bullet_list:
        b_rect = bullet.get_rect()
        b_rect.left = b[0]
        b_rect.top = b[1]
        # 총알과 충돌
        if b_rect.colliderect(C.rect):
            C.hit(1)
            enemy_bullet_list.remove(b)
            if not C.alive:
                run = False

    
    # 화면에 그림 출력
    screen.blit(background, (0,0))
    screen.blit(C.img, (C.x_pos, C.y_pos))
    # 운석 출력
    for r in rock_list:
        screen.blit(r.img, (r.x_pos, r.y_pos))

    # 적 기체 출력
    for e in enemy_list:
        screen.blit(e.img, (e.x_pos, e.y_pos))

    # 총알 출력
    for x_pos, y_pos in bullet_list:
        screen.blit(bullet, (x_pos, y_pos))
    for x_pos, y_pos in enemy_bullet_list:
        screen.blit(enemy_bullet, (x_pos, y_pos))

    # 라이프 출력
    for i in range(C.life):
        screen.blit(hp, (10 + i*15, 10))

    # 점수 출력
    score_text = game_font.render('Score: {}'.format(score), True, (255,255,255))
    screen.blit(score_text, (10,50))

    # 최종 화면 업데이트
    pygame.display.update()

pygame.time.delay(3000)
pygame.quit()
