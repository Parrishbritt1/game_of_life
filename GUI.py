import pygame
from GOL import next_gen
import time


# Screen stuff
pygame.init()
# ---- PC size ----
# WIDTH, HEIGHT = 755, 800
# --- Laptop size ---
WIDTH, HEIGHT = 755, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
FPS = 60
START_BUTTON_LIGHT = "#1AC8F3"
START_BUTTON_DARK = "#3399FF"
STOP_BUTTON_LIGHT = "#FF0000"
STOP_BUTTON_DARK =  "#B92E34"

# Grid stuff
CELL_WIDTH = 20
CELL_HEIGHT = 20
MARGIN = 5
num_cell_cols = 30
num_cell_rows = 22


def update_window(pos, grid, started):
    rects = []
    for i in range(num_cell_rows):
        for j in range(num_cell_cols):
            color = "white"
            if grid[i][j] == 1:
                color = "green"
            rects.append(pygame.draw.rect(screen, color, [(MARGIN + CELL_WIDTH) * j + MARGIN,
                                            (MARGIN + CELL_HEIGHT) * i + MARGIN,
                                            CELL_WIDTH,
                                            CELL_HEIGHT]))


    # Start button hovered
    if pos_over_start(pos) and not started:
        pygame.draw.rect(screen, START_BUTTON_LIGHT, [WIDTH//2.3, 558, 120, 34])
    elif not started:
        pygame.draw.rect(screen, START_BUTTON_DARK, [WIDTH//2.3, 558, 120, 34])
    elif pos_over_start(pos) and started:
        pygame.draw.rect(screen, STOP_BUTTON_LIGHT, [WIDTH//2.3, 558, 120, 34])
    elif started:
        pygame.draw.rect(screen, STOP_BUTTON_DARK, [WIDTH//2.3, 558, 120, 34])


    font = pygame.font.SysFont("Corbel", 35)
    if started:
        text = font.render("Stop", True, "black")
    else:
        text = font.render("Start", True, "black")
    screen.blit(text, (355, 560))
    pygame.display.flip()



def is_grid_clicked(pos, grid):
    if pos[1] < 550 and pos[0] < 750:
        col = pos[0] // (CELL_WIDTH + MARGIN)
        row = pos[1] // (CELL_HEIGHT + MARGIN)
        grid[row][col] = 1

def pos_over_start(pos):
    return 328 <= pos[0] <= 447 and 560 <= pos[1] <= 590


def main():
    grid = []
    for i in range(num_cell_rows):
        grid.append([])
        for j in range(num_cell_cols):
            grid[i].append(0)

    clock = pygame.time.Clock()
    started = False
    run = True
    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Left click heled down
            elif pygame.mouse.get_pressed()[0]:
                if not started:
                    is_grid_clicked(pos, grid)

            elif event.type == pygame.MOUSEBUTTONUP:
                if pos_over_start(pos) and not started:
                    started = True
                elif pos_over_start(pos) and started:
                    started = False

        screen.fill("gray")

        if started:
            grid = next_gen(grid)
            clock.tick(10)

        update_window(pos, grid, started)
    

    pygame.quit()


if __name__ == "__main__":
    main()