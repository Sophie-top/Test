import pygame

WIDTH = 360 #задала ширину экрана
HEIGHT = 480 #задала высоту экрана
FPS = 30
width1 = 50
height1 = 50

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


pygame.init()#инициализация игры
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #создание экрана
pygame.display.set_caption("Моя первая игра") #заголовок экрана
clock = pygame.time.Clock()

#Цикл игры
run = True
while run: #run = (run = True)
    #Держим цикл на правильной скорости
    clock.tick(FPS)
    #Ввод процесса(события)
    for event in pygame.event.get():  #event - событие
        if event.type == pygame.QUIT:
            run = False 

    #обновление

    #рендеринг
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (WIDTH / 2 - width1 / 2, HEIGHT / 2 - height1 / 2, width1, height1))  #Параметры: где рисовать, какого цвета, ширина, высота,
    # После отрисовкии всего, переворачиваем экран
    pygame.display.flip() 

pygame.quit()
