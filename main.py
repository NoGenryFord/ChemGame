import pygame as pg
import time
import random

#import elements

pg.init()

width = 1280
height = 720

screen = pg.display.set_mode((width,height))
pg.display.set_caption("Game")
bg_color_white = (255,255,255)
text_font = pg.font.Font(None, 30)

# Список для зберігання кіл
circles = []

# Змінні для FPS
clock = pg.time.Clock()
fps = 0
show_fps_on_screen = True


# Параметри гравітації
gravity = 1
drag = 0.5

#main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_f: # Натискання клавіші "F"
                show_fps_on_screen = not show_fps_on_screen  # Інвертуємо значення прапорця
        if event.type == pg.MOUSEBUTTONDOWN:  # Перевірка натискання кнопки миші
            if event.button == 1:  # 1 - ліва кнопка миші
                # Отримуємо координати кліку миші
                mouse_x, mouse_y = pg.mouse.get_pos()

                # Створюємо нове коло
                color = (50,10,150)
                radius = random.randint(8,12)
                new_circle = {"x": mouse_x, "y": mouse_y, "radius": radius, "color": color,
                              "velocity_y": 0, "velocity_x": 10}
                circles.append(new_circle)
        if event.type == pg.MOUSEBUTTONDOWN:  # Перевірка натискання кнопки миші
            if event.button == 3:  # 3 - права кнопка миші
                # Отримуємо координати кліку миші
                mouse_x, mouse_y = pg.mouse.get_pos()

                # Створюємо нове коло
                color = (150,150,10)
                radius = random.randint(8,12)
                new_circle = {"x": mouse_x, "y": mouse_y, "radius": radius, "color": color,
                              "velocity_y": 0, "velocity_x": -10}
                circles.append(new_circle)

    # Заповнення фону
    screen.fill(bg_color_white)

    # Оновлення позицій та малювання всіх кіл
    for circle in circles:
        # Застосування гравітації до кожного окремого кола
        circle["velocity_y"] += gravity
        circle["y"] += circle["velocity_y"]
        circle["x"] += circle["velocity_x"]

        # Перевірка зіткнення з дном для кожного кола
        if circle["y"] + circle["radius"] >= height:
            circle["y"] = height - circle["radius"]
            circle["velocity_y"] = -circle["velocity_y"] * 0.9
        # Перевірка зіткнення з верхом для кожного кола
        if circle["y"] + circle["radius"] < 0:
            circle["y"] = 0 + circle["radius"]
            circle["velocity_y"] = -circle["velocity_y"] * 0.9
        # Перевірка зіткнення з правою стіною для кожного кола
        if circle ["x"] + circle["radius"] >= width:
            circle["x"] = width - circle["radius"]
            circle["velocity_x"] = -circle["velocity_x"] * drag
        # Перевірка зіткнення з лівою стіною для кожного кола
        if circle ["x"] + circle["radius"] < 0:
            circle["x"] = 0 + circle["radius"]
            circle["velocity_x"] = -circle["velocity_x"] * drag
        # Перевірка зіткнення з іншим елементом

        pg.draw.circle(screen, circle["color"], (circle["x"], circle["y"]), circle["radius"])


    if show_fps_on_screen:
        fps = clock.get_fps()
        fps_text = text_font.render(f"FPS: {fps:.2f}", True, (0, 0, 0))  # Створюємо текст
        screen.blit(fps_text, (10, 10))  # Відображаємо текст на екрані

    text_LBM = text_font.render("Press LBM for blue balls", True, (0,0,0)) #creat text
    text_RBM = text_font.render("Press RBM for yellow balls", True, (0,0,0))
    text_FPS = text_font.render("Press F for check FPS", True, (0,0,0))
    screen.blit(text_LBM, (10,30))
    screen.blit(text_RBM, (10,50))
    screen.blit(text_FPS, (10,70))

    # Оновлення екрану
    pg.display.flip()

    # Обмеження FPS (за бажанням)
    clock.tick(180)  # Обмежуємо FPS

# Завершення роботи Pygame
pg.quit()