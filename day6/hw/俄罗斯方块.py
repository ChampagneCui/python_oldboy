# coding : utf-8


#: pip install pygame

import random
import sys
import pygame



COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

class Block:
    width = 24
    height = 24

    @staticmethod
    def draw(s, left, top, color, bg_color):
        pygame.draw.rect(s, bg_color, pygame.Rect(left, top, Block.width, Block.height))
        pygame.draw.rect(s, color, pygame.Rect(left, top, Block.width - 1, Block.height - 1))


class Building:

    def __init__(self):

        self.form = random.choice(
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ]
            ])

    def __getitem__(self, pos):
        return self.form[pos]

    def __setitem__(self, key, value):
        self.form[key] = value


class Layout:

    def __init__(self):
        self.block_x_count = 16;
        self.block_y_count = 22;
        self.layout = [[0 if 1 < i < self.block_x_count - 2 and j < self.block_y_count - 2 else 1
                        for i in range(self.block_x_count)] for j in range(self.block_y_count)]

    @property
    def size(self):

        return (self.block_x_count * Block.width, self.block_y_count * Block.height)

    def create_new_building(self):
        self.building = Building()
        self.building_left, self.building_top = 5, 0  #

        self.drop_speed = 3
        print(self.test_building_touch_wall())
        return self.test_building_touch_wall()

    @property
    def speed(self):
        return self.drop_speed

    def test_building_touch_wall(self, x_offset=0, y_offset=0):
        for i in range(4, -1, -1):
            for j in range(5):
                if self.building[i][j]:
                    if self.layout[i + self.building_top + y_offset][j + self.building_left + x_offset]:
                        return True
        return False

    def move_left_right(self, x):

        if not self.test_building_touch_wall(x_offset=x):
            self.building_left += x

    def down_build(self):
        self.building_top += 1

    def direct_down(self):
        self.drop_speed = 50

    def convert_building(self):
        new_box = [[0 for i in range(5)] for j in range(5)]
        for i in range(5):
            for j in range(4, -1, -1):
                new_box[i][j] = self.building[4 - j][i]
        self.building = new_box

    def clear_full_lines(self):
        new_layout = [[0 if 1 < i < self.block_x_count - 2 and j < self.block_y_count - 2 else 1
                       for i in range(self.block_x_count)] for j in range(self.block_y_count)]

        row_len = self.block_x_count - 4
        new_row = self.block_y_count - 2 - 1
        for cur_row in range(self.block_y_count - 2 - 1, 0, -1):
            if sum(self.layout[cur_row][2:self.block_x_count - 2]) < row_len:
                new_layout[new_row] = self.layout[cur_row]
                new_row -= 1
        self.layout = new_layout

    def put_building_to_layout(self):
        for i in range(4, -1, -1):
            for j in range(5):
                if self.building[i][j]:
                    self.layout[i + self.building_top][j + self.building_left] = 1

        self.clear_full_lines()

    def draw_building(self, s):
        cur_left, cur_top = self.building_left * Block.width, self.building_top * Block.height
        for i in range(5):
            for j in range(5):

                if self.building[j][i]:
                    Block.draw(s, cur_left + i * Block.width, cur_top + j * Block.height, COLOR_BLACK, COLOR_WHITE)

    def draw(self, s):
        for i in range(self.block_x_count):
            for j in range(self.block_y_count):
                if self.layout[j][i] == 0:
                    Block.draw(s, i * Block.width, j * Block.height, COLOR_WHITE, COLOR_BLACK)
                else:
                    Block.draw(s, i * Block.width, j * Block.height, COLOR_BLACK, COLOR_WHITE)


# -------------------------------------------------------------------

# Main

# -------------------------------------------------------------------

def main():

    while True:
        layout = Layout()
        layout.create_new_building()
        pygame.init()
        pygame.display.set_caption('game')
        screen = pygame.display.set_mode((layout.size), 0, 32)
        is_over = False

        while not is_over:

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        layout.convert_building()
                    if e.key == pygame.K_DOWN:
                        layout.direct_down()
                    if e.key == pygame.K_LEFT:
                        layout.move_left_right(-1)
                    if e.key == pygame.K_RIGHT:
                        layout.move_left_right(1)

            if layout.test_building_touch_wall(y_offset=1):
                layout.put_building_to_layout()
                is_over = layout.create_new_building()
            else:
                layout.down_build()


            layout.draw(screen)
            layout.draw_building(screen)
            pygame.display.update()


            pygame.time.Clock().tick(layout.speed)


if __name__ == '__main__':
    main()
