import pygame
import numpy as np
import os
import chessBoardClass


# chess board
chessBoardPNG = pygame.image.load(os.path.join('Chess Pieces', 'Chess_Board.png'))
chessBoardPNG = pygame.transform.scale(chessBoardPNG, (1000, 1000))


# chess piece images
bBishopPNG = pygame.image.load(os.path.join('Chess Pieces', 'B_Bishop.png'))
bBishopPNG = pygame.transform.scale(bBishopPNG, (100, 100))



width, height = 1000, 1000
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess")
white: tuple = (255, 255, 255)
black: tuple = (0, 0, 0)
border: pygame.rect = pygame.Rect(width/2 - 5, 0, 10, height)
fps: int = 60




def draw_window(piecePos):


    WIN.fill(white)
    WIN.blit(chessBoardPNG, (0, 0))
    WIN.blit(bBishopPNG, (piecePos.x, piecePos.y))
    pygame.display.update()

def bishopMovement(keysPressed, red):
    if keysPressed[pygame.K_a] and red.x - 5 > 0:
        red.x -= 5
    if keysPressed[pygame.K_s] and red.y + 5 + red.height < 1000:
        red.y += 5
    if keysPressed[pygame.K_d] and red.x + 5 + red.width < border.x:
        red.x += 5
    if keysPressed[pygame.K_w] and red.y - 5 > 0:
        red.y -= 5


def bishopMovement2(red):
    red.x, red.y = pygame.mouse.get_pos()
    red.x -= 50
    red.y -= 50

def main():
    red = pygame.Rect(100, 100, 100, 100)
    clock = pygame.time.Clock()
    run = True
    while run:
        leftMouseClick: bool = pygame.mouse.get_pressed(num_buttons=3)[0] == 1
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(red)

        keysPressed = pygame.key.get_pressed()
        #bishopMovement(keysPressed, red)
        if leftMouseClick:
            bishopMovement2(red)
    pygame.quit()

if __name__ == "__main__":
    main()

