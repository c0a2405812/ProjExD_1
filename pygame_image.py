import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")

    bg_img2 = pg.transform.flip(bg_img, True , False) #ren8
    kk_img = pg.image.load("fig/3.png") #ren1
    kk_img = pg.transform.flip(kk_img, True, False) #ren2
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr #ren6
        screen.blit(bg_img, [-x, 0]) #ren3  #ren6
        screen.blit(bg_img2, [-x+1600,0]) #ren7
        screen.blit(bg_img, [-x+3200, 0]) #ren9
        screen.blit(kk_img, [300,200]) #ren4
        pg.display.update()
        tmr += 1        
        clock.tick(200) #ren5

        if tmr == 3199: #ren9
            tmr = 0
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()