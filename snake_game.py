import sys
import pygame
from random import randint

import resources
import board_parts
from board_parts import BoardPart, SnakePart, Snake, Apple


def SNAKE_GAME_set_icon(image_path: str):
    """
    This function sets the icon of the game
    :param image_path: the path to the image of the icon (must be 32 X 32)
    :return: None
    """
    icon = pygame.image.load(image_path)
    pygame.display.set_icon(icon)


class Game(object):
    # this value determines how many blocks should spread over the screen (width, height)
    blocks_amount = (40, 20)

    def __init__(self, name: str):
        """
        Initialize the parameters of the game
        :param name: window name
        """
        pygame.init()
        self.difficulty = resources.MEDIUM
        self.bg_image = pygame.image.load(resources.BG_IMAGE)
        self.surfaces = {}
        self.snake, self.apple = self.init_objects()
        self.clock = pygame.time.Clock()
        self.direction = 'right'
        self.move_by = resources.DIRECTION_TO_MOVEMENT[self.direction]
        self.prev_direction = self.direction
        SNAKE_GAME_set_icon(resources.ICON_PATH)
        screen_size = [x * size for x, size in zip(board_parts.BLOCK_SIZE, self.blocks_amount)]
        self.screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
        pygame.display.set_caption(name)

    def game_loop(self):
        """
        Runs the game loop
        :return: None
        """
        self.display_init_grid()
        while True:
            self.clock.tick(self.difficulty)
            head = self.snake.get_snake_head()

            head_next_location = [x + y for x, y in zip(head.get_grid_location(), self.move_by)]
            if self.check_border_crash(head_next_location):
                sys.exit()

            self.screen.blit(self.bg_image, [0, 0])

            self.change_head_direction(head)

            if self.move_snake_body(head_next_location):
                sys.exit()

            self.move_snake_head(head)

            # if the apple was eaten, add a part to the snake and move the apple
            if self.apple.get_grid_location() == head.get_grid_location():
                self.move_apple()
                self.add_part()
            self.draw(self.apple)

            self.prev_direction = self.direction

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.direction = resources.KEY_STROKE_TO_DIRECTION[event.key]
                    if self.prev_direction == 'down' and self.direction == 'up':
                        self.direction = 'down'
                    if self.prev_direction == 'up' and self.direction == 'down':
                        self.direction = 'up'
                    if self.prev_direction == 'left' and self.direction == 'right':
                        self.direction = 'left'
                    if self.prev_direction == 'right' and self.direction == 'left':
                        self.direction = 'right'
                self.move_by = resources.DIRECTION_TO_MOVEMENT[self.direction]
            pygame.display.flip()

    def init_objects(self):
        """
        initialize the objects of the game (apple and snake)
        :return: snake and apple
        """
        for name in resources.IMAGES_DICT:

            self.surfaces[name] = pygame.image.load(resources.IMAGES_DICT[name]).get_rect()
        board_parts.BLOCK_SIZE = self.surfaces['apple'].get_size()
        snake = Snake(self.surfaces['head right'])
        snake.create_body(self.surfaces['body horizontal'], self.surfaces['tail right'])
        apple = Apple(surface=self.surfaces['apple'], screen_size=self.blocks_amount)

        return snake, apple

    def display_init_grid(self):
        """
        Display yhe initial grid
        :return: None
        """
        self.screen.blit(self.bg_image, [0, 0])

        self.draw(self.apple)
        for snake_part in self.snake.get_snake():
            self.draw(snake_part)

        pygame.display.flip()

    def move_snake_body(self, head_next_location: list) -> bool:
        """
        move the snake body from its current location to the next location
        :param head_next_location: the next location of the head
        :return: True if one of the body parts crashed into the head, False otherwise.
        """
        snake_length = self.snake.get_snake_length()
        for i in range(snake_length - 1, 0, -1):
            snake_part = self.snake.get_snake_part_by_index(i)
            next_snake_part = self.snake.get_snake_part_by_index(i - 1)
            next_grid_location = next_snake_part.get_grid_location()
            if head_next_location == next_grid_location:
                return True
            snake_part.set_body_direction(next_snake_part.get_body_direction())
            if i == self.snake.tail_index:
                body_type = resources.TAIL_PART_INDEX
            else:
                body_type = resources.REGULAR_PART_INDEX
            new_surface_name = resources.DIRECTIONS_TO_SURFACE_NAMES[snake_part.body_direction][body_type]
            new_surface = self.surfaces[new_surface_name]
            snake_part.set_surface(new_surface)

            snake_part.set_location(next_grid_location)
            self.draw(snake_part)
        return False

    def move_snake_head(self, head: SnakePart):
        """
        Move the snake's head
        :param head: the snake's head
        :return: None
        """
        new_grid_location = [x + y for x, y in zip(head.get_grid_location(), self.move_by)]
        head.set_location(new_grid_location)
        self.draw(head)

    def move_apple(self):
        """
        Move the apple
        :return: None
        """
        new_grid_location = [randint(0, size - 1) for size in self.blocks_amount]
        self.apple.set_location(new_grid_location)

    def add_part(self):
        """
        Add a part to the snake's body
        :return: None
        """
        location = list(self.snake.get_snake_part_by_index(-1).get_grid_location())
        new_snake_part = SnakePart(surface=self.surfaces['body horizontal'], grid_location=location)
        self.snake.add_snake_part(new_snake_part)

    def change_head_direction(self, head: SnakePart):
        """
        Change the head's direction according to the next move
        :param head: the snake's head
        :return: None
        """
        head.body_direction = self.prev_direction + '->' + self.direction
        new_surface_name = resources.DIRECTIONS_TO_SURFACE_NAMES[head.body_direction][resources.HEAD_PART_INDEX]
        new_surface = self.surfaces[new_surface_name]
        head.set_surface(new_surface)

    def draw(self, board_part: BoardPart):
        """
        Draw a board part on the screen
        :param board_part: board part (apple or snake part)
        :return: None
        """
        self.screen.blit(board_part.get_surface(), board_part.get_rect())

    def check_border_crash(self, head_next_location: list) -> bool:
        """
        Check if the head of the snake is about to crash any border
        :param head_next_location: the head's next location
        :return: True if the head is about to crash any border, False otherwise.
        """
        crashed_down = head_next_location[0] > self.blocks_amount[0] - 1
        crashed_right = head_next_location[1] > self.blocks_amount[1] - 1
        crashed_up = head_next_location[0] < 0
        crashed_left = head_next_location[1] < 0
        return crashed_up or crashed_left or crashed_right or crashed_down
