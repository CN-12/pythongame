from turtle import screensize
import pygame

pygame.init()

Color = (0, 0, 0)
size = [400, 400]
screen = pygame.display.set_mode(size)

done= False
clock= pygame.time.Clock()

airplane = pygame.image.load('um.jpg')
airplane = pygame.transform.scale(airplane, (60, 45))
 
# 4. pygame 무한루프
def runGame():
    global done, airplane
    x = 20
    y = 24
 
    while not done:
        myfont = pygame.font.SysFont(None,50)
        clock.tick(1000)
        screen.fill(Color)
        um = myfont.render("UM",True,(255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
 
            # 방향키 입력에 대한 이벤트 처리
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 10
                elif event.key == pygame.K_DOWN:
                    y += 10
                elif event.key == pygame.K_LEFT:
                    x -= 10
                elif event.key == pygame.K_RIGHT:
                    x += 10
                elif event.key == pygame.K_U:
                    screen.blit(um, (x+20, y))
            if(x < 0):
                x = 0
            elif(x > 400):
                x = 400
            elif(y < 0):
                y = 0
            elif(y > 400):
                y = 400
        screen.blit(airplane, (x, y))
        pygame.display.update()
 
runGame()
pygame.quit()
