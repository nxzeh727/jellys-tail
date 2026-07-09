import asyncio
import pygame
from input import InputBox

pygame.init()
screen = pygame.display.set_mode((640, 640))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
FPS = 30
minute_num = 25
break_minute_num = 5
WORK_TIME = minute_num * 60
BREAK_TIME = break_minute_num * 60
cur_time = WORK_TIME
is_working = True
timer_running = False
sessions = 0
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1000)
running = True
dt = 0
sound = pygame.mixer.Sound("potaopt.ogg")
font = pygame.font.Font("NanumPenScript-Regular.ttf", 40)
fontfont = pygame.font.Font("Flower-Regular.ttf",100)
fontfontfont = pygame.font.Font("Flower-Regular.ttf",40)
fontfontfontfont = pygame.font.Font("NanumPenScript-Regular.ttf", 30)
timerselected = True
aboutselected = False
plantselected = False


button = pygame.Rect(300,250,200,60)
start_pomodoro = pygame.Rect(300,500,200,60)
setteings = pygame.Rect(560,30,205,205)
close = pygame.Rect(600,20,50,50)
timer = pygame.Rect(20,100,140,40)
about = pygame.Rect(20,160,140,40)
worktime = InputBox(200, 160, 100, 40, screen, fontfontfontfont, (251, 245, 221), (132, 177, 121))
submitworktime = pygame.Rect(320, 160, 75,40)
breaktime = InputBox(200, 260, 100, 40, screen, fontfontfontfont, (251, 245, 221), (132, 177, 121))
submitbreaktime = pygame.Rect(320, 260, 75,40)
current_screen = "start"
break_work = "WORK :)"

imagee = pygame.image.load("plant_stages/sprite_c11_r03.png")
image1 = pygame.image.load("plant_stages/sprite_c12_r03.png")
image2 = pygame.image.load("plant_stages/sprite_c13_r03.png")
image3 = pygame.image.load("plant_stages/sprite_c14_r03.png")
image4 = pygame.image.load("plant_stages/sprite_c15_r03.png")
settings = pygame.image.load("settings-4.png")
settings = pygame.transform.scale_by(settings, 0.080)

def plants(screen, session_num):
    if session_num >= 2 and session_num <= 3:
        image = image1
        shift = 20
    elif session_num >= 4 and session_num <= 5:
        image = image2
        shift = 40
    elif session_num >= 6 and session_num <= 7:
        image = image3
        shift = 60
    elif session_num >= 8:
        image = image4
        shift = 80
    else:
        image = imagee
        shift = 0
    image = pygame.transform.scale_by(image,3)
    image_rect = image.get_rect()
    image_rect.centerx = screen_rect.centerx
    image_rect.centery = screen_rect.centery - shift
    screen.blit(image, image_rect)


async def main():
  global running, current_screen, timer_running, cur_time, is_working, sessions, break_work, minute_num, WORK_TIME
  global timerselected, aboutselected, plantselected

  while running:
    
    for event in pygame.event.get():
        if current_screen == "settings":
            worktime.handle_event(event)
            breaktime.handle_event(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if current_screen == "start" and button.collidepoint(event.pos):
                    current_screen = "game"

                if current_screen == "game" and start_pomodoro.collidepoint(event.pos):
                    timer_running = not timer_running
                if current_screen == "game" and setteings.collidepoint(event.pos):
                    current_screen = "settings"
                if current_screen == "settings" and close.collidepoint(event.pos):
                    current_screen = "game"
                if current_screen == "settings" and submitworktime.collidepoint(event.pos):
                    if worktime.text.isdigit():
                        minute_num = int(worktime.text)
                        WORK_TIME = minute_num * 60
                        cur_time = WORK_TIME
                if current_screen == "settings" and submitbreaktime.collidepoint(event.pos):
                    if breaktime.text.isdigit():
                        minute_num = int(breaktime.text)
                        BREAK_TIME = minute_num * 60
                        cur_time = BREAK_TIME
                if timer.collidepoint(event.pos):
                    timerselected = True 
                    aboutselected = False
                if about.collidepoint(event.pos):
                    timerselected = False
                    aboutselected = True

        elif event.type == TIMER_EVENT and timer_running:
            if cur_time > 0:
                cur_time -= 1
            else:
                if is_working:
                    sound.play()
                    break_work = "BREAK :D"
                    sessions += 1
                    cur_time = BREAK_TIME
                    is_working = False
                else:
                    break_work = "WORK :)"
                    sound.play()
                    cur_time = WORK_TIME
                    is_working = True


    
    mouse = pygame.mouse.get_pos()

    if current_screen == "start":
        screen.fill((231, 225, 177))
        name = fontfont.render("jelly's tail", True, (132, 177, 121))
        screen.blit(name, (100, 180))
        screen.blit(name, (101, 181))

        
        if button.collidepoint(mouse):
            pygame.draw.rect(screen, (162, 203, 139), button, border_radius=8)
            button.center = (320, 320)
        else:
            pygame.draw.rect(screen, (132, 177, 121), button, border_radius=8)
            button.center = (320, 320)

        button_text = font.render("start", True, (251, 245, 221))
        text = button_text.get_rect(center = button.center)
        screen.blit(button_text, text)

    elif current_screen == "game":
        screen.fill((231, 225, 177))
        name = fontfontfont.render("jelly's tail", True, (132, 177, 121))
        screen.blit(name,(30,30))
        screen.blit(name,(31,31))
        pygame.draw.rect(screen, (231, 225, 177), setteings)
        setteings.center = (560,30)
        screen.blit(settings, (560, 30))
        minutes = cur_time // 60
        seconds = cur_time % 60
        time_text = f"{minutes:02}:{seconds:02}"
        cur_time_text = font.render(time_text, True, (251, 245, 221))
        cur_rect = cur_time_text.get_rect()
        cur_rect.centerx = screen_rect.centerx
        cur_rect.centery = screen_rect.centery + 60
        screen.blit(cur_time_text, cur_rect)
        plants(screen, sessions)

        if start_pomodoro.collidepoint(mouse):
            pygame.draw.rect(screen, (132, 177, 121), start_pomodoro, border_radius=8)
            start_pomodoro.center = (320, 480)
        else:
            pygame.draw.rect(screen, (162, 203, 139), start_pomodoro, border_radius=8)
            start_pomodoro.center = (320, 480)
        lable = "pause" if timer_running else "start"
        start_pomodoro_text = font.render(lable, True, (251, 245, 221))
        text = start_pomodoro_text.get_rect(center = start_pomodoro.center)
        screen.blit(start_pomodoro_text, text)
        toxt = font.render(break_work,True, (251, 245, 221))
        toxt_rect = toxt.get_rect()
        toxt_rect.centerx = screen_rect.centerx
        toxt_rect.centery = screen_rect.centery - 160
        screen.blit(toxt, toxt_rect)

    elif current_screen == "settings":
        screen.fill((231, 225, 177))
        name = fontfontfont.render("jelly's tail", True, (132, 177, 121))
        screen.blit(name,(30,30))
        screen.blit(name,(31,31))
        pygame.draw.rect(screen, (231, 225, 177), close)
        close.center = (600,20)
        teext = font.render("x",True, (251, 245, 221))
        screen.blit(teext, (600,20))
        pygame.draw.line(screen, (251, 245, 221), (180, 80), (180, 620), 2)
        pygame.draw.rect(screen, (162, 203, 139), timer, border_radius=8)
        pygame.draw.rect(screen, (162, 203, 139), about, border_radius=8)
        timertext = fontfontfontfont.render("timer",True, (251, 245, 221))
        screen.blit(timertext, (55,105))
        abouttext = fontfontfontfont.render("about", True, (251, 245, 221))
        screen.blit(abouttext, (55,165))
        if timerselected:
            pygame.draw.rect(screen, (132, 177, 121), timer, border_radius=8)
            timeertext = fontfontfontfont.render("timer",True, (251, 245, 221))
            screen.blit(timeertext,(55,105))
            title = fontfontfontfont.render("Timer settings", True, (132, 177, 121))
            screen.blit(title, (300,60))
            worksettings = fontfontfontfont.render("work time", True, (132, 177, 121))
            screen.blit(worksettings, (200, 120))
            pygame.draw.rect(screen, (162, 203, 139),submitworktime, border_radius=8)
            submitext = fontfontfontfont.render("save",True, (251, 245, 221))
            screen.blit(submitext,(320,160))
            worktime.draw()
            breaksettings = fontfontfontfont.render("break time", True, (132, 177, 121))
            screen.blit(breaksettings, (200, 220))
            pygame.draw.rect(screen, (162, 203, 139),submitbreaktime, border_radius=8)
            submietext = fontfontfontfont.render("save",True, (251, 245, 221))
            screen.blit(submietext,(320,260))
            breaktime.draw()
        if aboutselected:
            pygame.draw.rect(screen, (132, 177, 121), about, border_radius=8)
            aboutttext = fontfontfontfont.render("about",True, (251, 245, 221))
            screen.blit(aboutttext,(55,165))
            title = fontfontfontfont.render("About", True, (132, 177, 121))
            screen.blit(title, (300,60))
            lines = ["Hi :) this is jelly's tail,",
                     "a simple pomodoro app.",
                       "this is made for typeface.",
                         " I hope you enjoy!"]
            y=120
            for line in lines:
        
                aboutt = fontfontfontfont.render(line, True, (132, 177, 121))
               
                screen.blit(aboutt, (200,y))
                y += 35









    
    pygame.display.flip()


    clock.tick(FPS)
    await asyncio.sleep(0)

  pygame.quit()

asyncio.run(main())
