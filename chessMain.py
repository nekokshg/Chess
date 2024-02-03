
'''
Main driver file. Responsible for handling user input and displaying current GameState object.
'''

import pygame as p
import chessEngine

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8 #dimensions of chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animations
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called once in the main
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    #Note: we can access an image by IMAGES['wP']

'''
Main driver for our code. Will handle user input and updating the graphics
'''

def main():
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState()
    print(gs.board)

main()
