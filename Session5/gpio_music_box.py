# gpio music box lab

import pygame
from gpiozero import Button

pygame.init()

drum_snare_hard = pygame.mixer.Sound("/home/pi/gpio_music_box/drum_snare_hard.wav")

btn_drum = Button(10)

btn_drum.when_pressed = drum_snare_hard.play
