import pygame
from unit import Character, Rock

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

# 나머지 이미지 로드
bullet = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bullet, (5, 15))
hp = pygame.image.load('hp.png')
hp = pygame.transform.scale(hp, (10,30))

# 창 띄우기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("슈팅게임")

# 배경 띄우기
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))
# 캐릭터
C = Character(screen_width, screen_height)
# 적
rock_list = [Rock(screen_width, screen_height) for i in range(8)]

# 탄환
bullet_list = []

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
            rock_list.remove(r)
            rock_list.append(Rock(screen_width, screen_height))
            
        # 아래로 나감
        elif r.y_pos > screen_height:
            rock_list.remove(r)
            rock_list.append(Rock(screen_width, screen_height))

    # 총알이 화면 위로 나가면 리스트에서 remove
    for b in bullet_list:
        if b[1] < -15:
            bullet_list.remove(b)
    
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
            rock_list.append(Rock(screen_width, screen_height))

        # 총알과 운석 충돌 - 부딛힌 총알&운석 remove
        for b in bullet_list:
            # 총알 사각형 정보
            b_rect = bullet.get_rect()
            b_rect.left = b[0]
            b_rect.top = b[1]
            # 충돌 처리
            if r.rect.colliderect(b_rect):
                rock_list.remove(r)
                bullet_list.remove(b)
                rock_list.append(Rock(screen_width, screen_height))
                score += 1

    # 화면에 그림 출력
    screen.blit(background, (0,0))
    screen.blit(C.img, (C.x_pos, C.y_pos))
    # 운석 출력
    for r in rock_list:
        screen.blit(r.img, (r.x_pos, r.y_pos))

    # 총알 출력
    for x_pos, y_pos in bullet_list:
        screen.blit(bullet, (x_pos, y_pos))

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
