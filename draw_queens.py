gravity = 0.0001

class QueenSprite:

    def __init__(self, img, target_posn):
        """creat and initialize a queen for this target position on the board"""
        self.image = img
        self.target_posn = target_posn
        (x,y) = target_posn
        self.posn = (x,0)
        self.y_velocity = 0

    def update(self):
        self.y_velocity += gravity
        (x,y) = self.posn
        new_y_pos = y + self.y_velocity
        self.posn = (x,new_y_pos)


    def darw(self, target_surface):
        target_surface.blit(self.image, self.posn)


"""draw chess board and queen"""
import pygame

def draw_board(the_board):
    pygame.init()
    colors = [(255,0,0),(0,0,0)]
    n = len(the_board)
    surface_sz = 480
    sq_sz = surface_sz // n
    surface_sz = sq_sz * n
    surface = pygame.display.set_mode((surface_sz,surface_sz))

    ball = pygame.image.load("C:/Users/p/Desktop/ball.jpg")
    ball_offset = (sq_sz - ball.get_width()) // 2

    all_sprites = []
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball,(col*sq_sz+ball_offset,row*sq_sz+ball_offset))
        all_sprites.append(a_queen)

    while True:
        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        for sprite in all_sprites:
            sprite.update()

        # draw a fresh background (a blank chess board)
        for row in range(n):
            c_indx = row % 2
            for col in range(n):
                the_square = (col * sq_sz,row*sq_sz,sq_sz,sq_sz)
                surface.fill(colors[c_indx],the_square)
                c_indx = (c_indx + 1) % 2

        # now that squares are drawn, draw the queens
        for (col,row) in enumerate(the_board):
            surface.blit(ball,(col*sq_sz+ball_offset,row*sq_sz+ball_offset))

        # ask every sprite to draw itself.
        for sprite in all_sprites:
            sprite.draw(surface)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    draw_board([0, 5, 3, 1, 6, 4, 2])
    draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])