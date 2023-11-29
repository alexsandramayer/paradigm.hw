class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self): # выводит текущее состояние доски
        for i in range(0, 9, 3):
            print(self.board[i], '|', self.board[i+1], '|', self.board[i+2])
            print('---------')

    def make_move(self, position): # позволяет сделать ход игрока, проверяя его допустимость и обновляя текущего игрока
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
        else:
            print('Недопустимый ход!')

    def check_winner(self): # проверяет, есть ли победитель на текущей доске
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтальные комбинации
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикальные комбинации
            [0, 4, 8], [2, 4, 6]              # диагональные комбинации
        ]

        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return True

        return False

    def play_game(self): # запускает игру, позволяя игрокам по очереди делать ходы, пока не будет найден победитель
        while not self.check_winner():
            self.print_board()
            position = int(input('Ход игрока {}: '.format(self.current_player)))
            self.make_move(position)

        self.print_board()
        print('Игрок {} победил!'.format(self.current_player))


game = TicTacToe()
game.play_game()

""" Была выбрана объектно-ориентированную парадигму для решения этой задачи, так как она позволяет легко моделировать игровую ситуацию с помощью классов и методов. Класс TicTacToe инкапсулирует все необходимые данные и операции для игры, делая код более структурированным и поддерживаемым. """