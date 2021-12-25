from random import randint

INIT_LENGTH = 9
INIT_LIVES = 3
INIT_DIRECTION = 'right->right'
BLOCK_SIZE = []


class BoardPart:
    def __init__(self, surface, grid_location):
        self._surface = surface
        self._rect = self._surface.get_rect()
        self._grid_location = grid_location
        self.set_location(grid_location)

    def get_surface(self):
        return self._surface

    def set_surface(self, new_surface):
        self._surface = new_surface
        self._rect = self._surface.get_rect()

    def set_location(self, new_grid_location):
        self._grid_location = new_grid_location
        new_location = [coordinate * pixel_size for coordinate, pixel_size in zip(self._grid_location, BLOCK_SIZE)]
        self._rect.update(new_location, BLOCK_SIZE)

    def set_grid_location(self, new_grid_location):
        self._grid_location = new_grid_location

    def get_grid_location(self):
        return self._grid_location

    def get_rect(self):
        return self._rect


class SnakePart(BoardPart):
    def __init__(self, body_part, grid_location):
        super().__init__(body_part, grid_location)
        self.body_direction = INIT_DIRECTION

    def set_body_direction(self, new_body_direction):
        self.body_direction = new_body_direction

    def get_body_direction(self):
        return self.body_direction


class Apple(BoardPart):
    def __init__(self, body_part, screen_size):
        init_location = [randint(0, size - 1) for size in screen_size]
        super().__init__(body_part, init_location)


class Snake(object):
    SNAKE_HEAD_INDEX = 0
    START_POINT = 5, 0

    def __init__(self, init_head_surface):
        head = SnakePart(body_part=init_head_surface, grid_location=Snake.START_POINT)
        self.snake = [head]
        self.tail_index = None

    def create_body(self, init_body_surface, init_tail_surface):
        for i in range(INIT_LENGTH):
            location = list(self.snake[-1].get_grid_location())
            location[0] -= 1
            init_surface = init_body_surface
            if i == INIT_LENGTH - 1:
                init_surface = init_tail_surface
            self.snake.append(SnakePart(body_part=init_surface, grid_location=location))
        self.tail_index = INIT_LENGTH

    def add_snake_part(self, new_snake_part):
        self.snake.append(new_snake_part)
        self.tail_index += 1

    def get_snake(self):
        return self.snake

    def get_snake_head(self):
        return self.snake[Snake.SNAKE_HEAD_INDEX]

    def get_snake_length(self):
        return len(self.snake)

    def get_snake_part_by_index(self, index):
        return self.snake[index]
