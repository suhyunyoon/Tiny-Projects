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

# 창 띄우기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("슈팅게임")

# 배경 띄우기
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))
# 캐릭터
C = Character(screen_width, screen_height)
# 적
rock_list = [Rock(screen_width, screen_height),
             Rock(screen_width, screen_height),
             Rock(screen_width, screen_height)]

# 게임 시작
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
        # 키를 뗐을 때
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                C.to_x = 0
            if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                C.to_y = 0

    # 이동
    C.move(dt)
    for r in rock_list:
        r.move(dt)

    # 화면 밖으로 나가는 지 검사
    if C.x_pos < 0:
        C.x_pos = 0
    elif C.x_pos > screen_width - C.width:
        C.x_pos = screen_width - C.width

    if C.y_pos < 0:
        C.y_pos = 0
    elif C.y_pos > screen_height - C.height:
        C.y_pos = screen_height - C.height
        

    # 화면에 그림 출력
    screen.blit(background, (0,0))
    screen.blit(C.img, (C.x_pos, C.y_pos))
    # 운석 출력
    for r in rock_list:
        screen.blit(r.img, (r.x_pos, r.y_pos))

    # 최종 화면 업데이트
    pygame.display.update()

pygame.quit()
