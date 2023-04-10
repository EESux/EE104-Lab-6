
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 17:23:29 2023

@author: Jeff
"""

import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import sys
import pgzero
from pgzero.builtins import keys

WIDTH = 1280
HEIGHT = 720
main_box = pygame.Rect(50, 40, 820, 240)
timer_box = pygame.Rect(990, 40, 240, 240)

answer_box1 = pygame.Rect(50, 358, 495, 165)
answer_box2 = pygame.Rect(735, 358, 495, 165)
answer_box3 = pygame.Rect(50, 538, 495, 165)
answer_box4 = pygame.Rect(735, 538, 495, 165)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ["What is the capital of Japan?",
      "London", "Paris", "Berlin", "Tokyo", 4]
q2 = ["what is 9+10",
      "21", "19", "14", "8", 2]
q3 = ["How do you say hello in Japanese?",
      "konnichiwa", "annyeonghaseyo", "hola", "Hello", 1]
q4 = ["Who is the Lebron of TFT?",
      "C9 k3soju", "lil bro", "Kenny Tran", "Daren Cheng", 1]
q5 = ["Who was the first member of the DK crew?",
      "Donkey Kong", "Cranky Kong", "Diddy Kong", "Funky Kong", 1]
q6 = ["Which TFT set introduced augments?", 
      "Set 4", "Set 3", "Set 7", "Set 6", 4]
q7 = ["Who is going to be the greatest striker?", 
      "Isagi Yoichi", "Barou Shouei", "Nagi Seishiro", "Kunigami Rensuke", 1]
q8 = ["Who voices Mario in the Super Mario Movie?", 
      "Chris Pratt", "Ludwig", "Jack Black", "Jackie Chan", 1]
q9 = ["Who wants to steal the Krabby Patty secret formula?", 
      "Patrick", "Squidward", "Plankton", "Pearl", 3]
q10 = ["Which company is not like the rest?", 
      "Apple", "Samsung", "Nokia", "Asus", 4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
question = questions.pop(0)


def draw(screen):
    screen.fill("antique white")
    pygame.draw.rect(screen, "azure", main_box)
    pygame.draw.rect(screen, "slate gray", timer_box)

    for box in answer_boxes:
        pygame.draw.rect(screen, "misty rose", box)

    font = pygame.font.Font(None, 46)
    question_text = font.render(question[0], True, (0, 0, 0))
    screen.blit(question_text, (main_box.x + 10, main_box.y + 10))

    text = font.render(str(time_left), True, (0, 0, 0))
    screen.blit(text, (timer_box.x + 10, timer_box.y + 10))

    index = 1
    for box in answer_boxes:
        text = font.render(question[index], True, (0, 0, 0))
        screen.blit(text, (box.x + 10, box.y + 10))
        index += 1


def game_over():
    global question, time_left
    message = ("Game over. You got %s questions correct" % str(score))
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0


def correct_answer():
    global question, score, time_left
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions")
        game_over()


def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer" + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index += 1


def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

def on_key_up(key):
    global score
    if key == keys.H:
        print("The correct answer is box number %s " % question[5])
    if key == keys.SPACE:
        score = score - 1
        correct_answer()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)  # 1000 milliseconds = 1 second

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            on_mouse_down(event.pos)
        elif event.type == pygame.USEREVENT + 1:
            update_time_left()
        elif event.type == pygame.KEYUP:  # Add this condition to handle KEYUP events
            on_key_up(event.key)  # Pass the key to the on_key_up function

    draw(screen)
    pygame.display.update()
    clock.tick(60)