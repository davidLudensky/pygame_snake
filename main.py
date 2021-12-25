import snake_game


def game(name):
    my_game = snake_game.Game(name)
    my_game.game_loop()


if __name__ == '__main__':
    game('snake')
