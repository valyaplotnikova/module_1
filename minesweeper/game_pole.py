import random

from call import Call
from colorama import init

init(autoreset=True)


class GamePole:
    """ Класс ипредставляющий игровое поле. """

    def __init__(self, N, M):
        """
        Инициализатор игрового поля размером N столбцов, N строк и с M мин на поле.
        :param N: размерность поля, определяется N*N;
        :param M: количество мин на поле;
        """
        self.N = N
        self.M = M
        self.pole = [[Call() for _ in range(N)] for _ in range(N)]
        self.safe_cells_count = N * N - M
        self.init()

    def init(self):
        """ Инициализатор поля с новой расстановкой случайным образом мин на поле. """

        mine_positions = random.sample(range(self.N * self.N), self.M)
        for pos in mine_positions:
            x = pos % self.N
            y = pos // self.N
            self.pole[y][x].mine = True

        # Подсчет мин вокруг каждой клетки
        for y in range(self.N):
            for x in range(self.N):
                if self.pole[y][x].mine:
                    continue
                count = sum(
                    1 for dy in (-1, 0, 1) for dx in (-1, 0, 1)
                    if 0 <= x + dx < self.N and 0 <= y + dy < self.N and self.pole[y + dy][x + dx].mine
                )
                self.pole[y][x].around_mines = count

    def show(self):
        """ Отображает поле в консоли """
        print("  " + " ".join(str(i) for i in range(self.N)))
        for idx, row in enumerate(self.pole):
            row_display = [str(idx)]
            for cell in row:
                if cell.fl_open:
                    row_display.append(str(cell.around_mines) if cell.around_mines > 0 else ' ')
                else:
                    row_display.append('#')
            print(" ".join(row_display))

    def open_cell(self, x, y):
        """ Открывает клетку/(клетки). """
        if self.pole[y][x].fl_open:
            return True  # Возвращаем True, если клетка уже открыта
        self.pole[y][x].fl_open = True
        if self.pole[y][x].mine:
            return False  # Возвращаем False, если игрок попал на мину
        return True  # Возвращаем True, если клетка открыта успешно
