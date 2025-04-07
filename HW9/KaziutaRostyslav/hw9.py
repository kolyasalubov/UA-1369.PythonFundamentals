# import random
#
# def guess_number():
#     number = random.randint(1, 100)
#
#     for i in range(1, 11):
#         try:
#             user_number = int(input(f"{i}. Enter a number: "))
#         except ValueError:
#             print("Please enter a valid integer.")
#             continue
#
#         if user_number > number:
#             print("Your number is higher.")
#         elif user_number < number:
#             print("Your number is lower.")
#         else:
#             print("\nYou are right!")
#             return
#
#     print(f"\nYou've used all attempts. The correct number was {number}.")
#
# guess_number()








# import pygame
#
# FPS = 120
#
# WIDTH_DISPLAY = 500
# HEIGHT_DISPLAY = 500
#
# WIDTH_RECTANGLE = 40
# HEIGHT_RECTANGLE = 60
# DELTA_STEP = 10
#
# BLACK_COLOR = (0, 0, 0)
# RED_COLOR = (250, 0, 0)
# GREEN_COLOR = (0, 250, 0)
#
# pygame.init()
#
# gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
#
# pygame.display.set_caption("My first game")
#
# RECT1_X = 50
# RECT1_Y = 50
#
# RECT2_X = WIDTH_DISPLAY - WIDTH_RECTANGLE - 50
# RECT2_Y = HEIGHT_DISPLAY - HEIGHT_RECTANGLE - 50
#
# run = True
# clock = pygame.time.Clock()
#
# while run:
#     pygame.time.delay(100)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_LEFT] and RECT1_X - DELTA_STEP >= 10:
#         RECT1_X -= DELTA_STEP
#         RECT2_X += DELTA_STEP
#     if keys[pygame.K_RIGHT] and RECT1_X + WIDTH_RECTANGLE + DELTA_STEP <= WIDTH_DISPLAY - 10:
#         RECT1_X += DELTA_STEP
#         RECT2_X -= DELTA_STEP
#     if keys[pygame.K_UP] and RECT1_Y - DELTA_STEP >= 10:
#         RECT1_Y -= DELTA_STEP
#         RECT2_Y += DELTA_STEP
#     if keys[pygame.K_DOWN] and RECT1_Y + HEIGHT_RECTANGLE + DELTA_STEP <= HEIGHT_DISPLAY - 10:
#         RECT1_Y += DELTA_STEP
#         RECT2_Y -= DELTA_STEP
#
#     gameDisplay.fill(BLACK_COLOR)
#     pygame.draw.rect(gameDisplay, RED_COLOR, [RECT1_X, RECT1_Y, WIDTH_RECTANGLE, HEIGHT_RECTANGLE])
#     pygame.draw.rect(gameDisplay, GREEN_COLOR, [RECT2_X, RECT2_Y, WIDTH_RECTANGLE, HEIGHT_RECTANGLE])
#
#     pygame.display.update()
#     clock.tick(FPS)
#
# pygame.quit()




















































































# from tkinter import *
# from random import randrange as rnd, choice
# import time
#
# CONST_NEGATIVE = -1000
# root = Tk()
#
# root.geometry('800x600')
#
# # задаємо назву вікна
# root.title("Caught the BALL")
#
# canv = Canvas(root, bg='white')
# canv.pack(fill=BOTH, expand=1)
#
# colors = ['red', 'orange', 'yellow', 'green', 'blue']
#
#
# def new_ball():
#     global x, y, r, ball
#     canv.delete(ball)
#     x = rnd(100, 700)
#     y = rnd(100, 500)
#     r = rnd(30, 50)
#     ball = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
#
#     delay = 1000 if points <= 10 else 500
#     root.after(delay, new_ball)
#
#
# def click(event):
#     global points, x, text
#     if (event.y - y) ** 2 + (event.x - x) ** 2 <= r ** 2:
#         points += 1
#         x = CONST_NEGATIVE
#         canv.delete(text)
#         canv.delete(ball)
#         text = canv.create_text(60, 20, text="Score: " + str(points), font='Arial 20')
#
#
# ball = canv.create_oval(CONST_NEGATIVE, 0, 0, 0)
# text = canv.create_text(60, 20, text="Score: " + str(0), font='Arial 20')
# points = 0
# new_ball()
# canv.bind('<Button-1>', click)
#
#
# mainloop()