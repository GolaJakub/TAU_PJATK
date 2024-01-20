import random


class SimpleGame:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.stop = None
        self.obstacles = []
        self.generate_board()

    def generate_board(self):
        # Losowanie START i STOP
        self.start = self.get_random_position()
        self.stop = self.get_random_position(exclude=[self.start])

        # Losowanie przeszkód
        num_obstacles = min(self.rows * self.cols // 4, 5)  # Maksymalnie 25% pól to przeszkody
        self.obstacles = [self.get_random_position(exclude=[self.start, self.stop] + self.obstacles) for _ in
                          range(num_obstacles)]

        # Umieszczenie START, STOP i przeszkód na planszy
        self.board[self.start[0]][self.start[1]] = 'A'
        self.board[self.stop[0]][self.stop[1]] = 'B'
        for obstacle in self.obstacles:
            self.board[obstacle[0]][obstacle[1]] = 'X'

    def get_random_position(self, exclude=[]):
        position = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
        while position in exclude:
            position = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
        return position

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def display_player(self):
        self.board[self.start[0]][self.start[1]] = 'O'

    def move(self, direction):
        current_pos = None
        if direction == 'right':
            current_pos = (self.start[0], self.start[1] + 1)
        elif direction == 'left':
            current_pos = (self.start[0], self.start[1] - 1)
        elif direction == 'up':
            current_pos = (self.start[0] - 1, self.start[1])
        elif direction == 'down':
            current_pos = (self.start[0] + 1, self.start[1])

        if 0 <= current_pos[0] < self.rows and 0 <= current_pos[1] < self.cols and current_pos not in self.obstacles:
            self.board[self.start[0]][self.start[1]] = ' '
            self.start = current_pos
            self.display_player()
            return True
        else:
            return False


if __name__ == "__main__":
    game = SimpleGame(5, 5)

    while game.start != game.stop:
        game.display_board()
        direction = input("Podaj kierunek (right, left, up, down): ")
        if game.move(direction):
            print(f'Moved {direction}')
        else:
            print(f'Cannot move {direction}')

    game.display_board()  # Dodano wywołanie funkcji display_board na koniec gry
    print("Gratulacje! Osiągnięto cel.")
